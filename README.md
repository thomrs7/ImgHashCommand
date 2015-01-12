#ImgHashCommand

Tested against splunk 6.2 on OSX 10.10.

##Example
There is an Image Hash Example dashborad that deminstrares usage. 

##Syntax

imghas field=&lt;field| deafaults to img_url&gt;

##Usage

search * | head 1 | eval img_url="http://www.randomwebsite.com/images/head.jpg" | imghash

##Requirements
The follow PKGS as included for  OSX 10.10.  If using a different OS the
following packages should be updated with versions from your system.  Simply
install the pkks with PIP and move them from yur site-packages to this apps bin
directory.

* PIL or Pillow
* numpy
* scipy

