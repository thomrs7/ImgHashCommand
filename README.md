Tested against splunk 6.2 on OSX 10.10.

==Syntax==

imghas field=<field| deafaults to img_url>

==Usage==

search * | head 1 | eval img_url="http://www.randomwebsite.com/images/head.jpg" | imghash
