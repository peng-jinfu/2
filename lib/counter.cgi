#!/usr/bin/perl 

use strict;
use CGI;
my($cgi) = new CGI;
print $cgi->header(type=>'text/html',charset=>'gb2312');
my($name) = "大帅哥";
my($num1) = "";
$num1 = $cgi->param('num1') if defined $cgi->param('num1');
my($num2) = "";
$num2 = $cgi->param('num2') if defined $cgi->param('num2');
my($num) = "";
$num=$num1+$num2;
print "<html>";
print "<head>";
print '<meta charset="utf-8">';
print '<title>POST方式页面</title>';
print "</head>";
print "<body>";
print '<div style="text-align:center">';
print "<h1>$name，欢迎来到CGI动态页面！</h1>";
print "<h1>计算结果：$num1+$num2=$num！</h1>";
print "</div>";
print "</body>";
print "</html>";

