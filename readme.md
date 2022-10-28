# TDD with Django flamework

### This project was developed to improve knowledge about unit test and functional test in python with django framework using. Also have the objective of  help anyone that new in unit test in this tecnologies. 

# TECNOLOGIES
 - Python 
 - Django
 - Django test framework
 - HTML 
 - Selenium 

# WHAT IS SOFTWARE TESTING ?
### exists distinct types of software testing, in this project are adopted two of them, they are unit test and functional test

## UNIT TEST
#
### An unit test is the entire test application in the input and output signatures of a system. It consists of validand invalid data via I/O (input/output) being applied by developers or test analysts.

## FUNCTIONAL TEST
### Functional testing is a quality assurance process and a type of black box test that bases your test cases on the specifications of the software component under test.

## REQUISITS
 - Python
 - VitualEnv
 - Django 3
 - Selenium

# USAGE 

~~~python
   source ./TDDenv/bin/activate 

   python -m pip install django 

   python -m pip install selenium
~~~

for use the test framwork from django we need import  ``` TestCase``` class.
~~~ pythonn
from django.test import TestCase
~~~

in this project also use the ```RequestFactory``` class for simulate the resquests.


