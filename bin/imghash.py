#!/usr/bin/env python

import sys
import urllib, cStringIO
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators
import imagehash
from PIL import Image


@Configuration()
class ImgHashCommand(StreamingCommand):
    """ %(synopsis)

    ##Syntax

    %(syntax)

    ##Description

    %(description)

    """
    avg = Option(
        doc=''' average hashing (aHash) ''',
        default='average_hash')

    per = Option(
        doc=''' perception hashing (pHash) ''',
        default='perception_hash')

    diff = Option(
        doc=''' difference hashing (dHash) ''',
        default='difference_hash')

    field = Option(
        doc='''
        **Syntax:** **pattern=***<regular-expression>*
        **Description:** Regular expression pattern to match''',
        default='img_url')

    def stream(self, events):
        """

        :param events:
        :return:
        """

        for event in events:
            self.logger.debug("start")

            try:
                self.logger.debug(event[self.field])

                raw_file = cStringIO.StringIO(
                    urllib.urlopen(event[self.field]).read())
                img = Image.open(raw_file)

                event[self.avg] = str(imagehash.average_hash(img))
                event[self.per] = str(imagehash.phash(img))
                event[self.diff] = str(imagehash.dhash(img))

            except Exception as e:
                self.logger.error(e)

                event[self.avg] = -1
                event[self.per] = -1
                event[self.diff] = -1

            self.logger.debug("end")
            yield event


dispatch(ImgHashCommand, sys.argv, sys.stdin, sys.stdout, __name__)
