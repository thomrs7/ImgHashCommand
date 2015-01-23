#!/usr/bin/env python

import sys
import urllib, cStringIO
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators
import imagehash



@Configuration()
class ImgHashCommand(StreamingCommand):
    """ %(synopsis)

    ##Syntax

    %(syntax)

    ##Description

    %(description)

    """
    h1 = Option(
        doc=''' hash 1 ''',
        default='' )

    h2 = Option(
        doc=''' hash 2 ''',
        default='')



    field = Option(
        doc=''' field to put value in ''',
        default='hash_difference')




    def stream(self, events):
        """

        :param events:
        :return:
        """

        for event in events:
            self.logger.debug("start")

            hash1 = imagehash.hex_to_hash(self.h1)
            hash2 = imagehash.hex_to_hash(self.h2)

            event[self.field] = hash1- hash2


            yield event


dispatch(ImgHashCommand, sys.argv, sys.stdin, sys.stdout, __name__)
