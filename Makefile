
I= gettysburg.txt
KEY= abc
#VERBOSE= -v
#MF= -f Makefile-class
PY= python3
#PY= python

RED= \033[0;31m
GREEN= \033[0;32m
NC= \033[0m

all:
	make ${MF} test-1
	make ${MF} test-2
	make ${MF} clean


test-1:
	cat $I | ${PY} vigenere.py ${KEY} > vigenere.out
	diff -w vigenere.out proj1-ref1.txt
	@echo "*** ${GREEN}PASSED the test ${NC}***"

test-2:
	cat proj1-ref1.txt | ${PY} vigenere.py -d ${KEY} > vigenere.out
	diff -w vigenere.out proj1-ref2.txt
	@echo "*** ${GREEN}PASSED the test ${NC}***"

clean:
	-rm vigenere.out
