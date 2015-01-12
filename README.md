#ImgHashCommand

Tested against splunk 6.2 on OSX 10.10.

##Example
There is an Image Hash Example dashborad that deminstrares usage. 

##Syntax

imghas field=&lt;field| deafaults to img_url&gt;

##Usage

search * | head 1 | eval img_url="http://www.randomwebsite.com/images/head.jpg" | imghash
