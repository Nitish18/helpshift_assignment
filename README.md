# README for helpshift take home assignment.

## Problem statement : 
You have to make a Contacts application which supports the following two operations: 
1. Add contact
2. Search Contact

## Assumptions :
1. Contact list is case-sensitive i.e Alex and alex will be treated distinct.

## Language and DS used :
1. Python3.6
2. For storing all contacts, I have used Trie data structure instead of normal Linear datastrucutre since it was mentioned in problem statement that the contact list can have many items . Time complexity for searching in case of Trie DS is O(m), where m is length of string to be searched, is very efficient as compared to any other linear DS like List of objects, etc.

## How to run:
1. go to base directory after extracting the tar file.
2. run:
```
python3.6 main.py
```
3. select the approp. option from CLI.
4. output will be printed on STDOUT.

## How to run unit-test cases :
1. go to base directory after extracting the tar file.
2. run:
```
python3.6 -m unittest test.py
```
3. output of all test-cases will be printed on STDOUT.