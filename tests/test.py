#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.conversions import headers

class Test_Conversions(unittest.TestCase):
	
	"""Test cases or conversion modules"""
	
	def test_headers(self):
		
		mkd = open("tests/test_cases/sample1_header.md").read()
		tex = open("tests/test_cases/sample1_header.tex").read()
		self.assertEqual(headers(mkd).split(), tex.split())
		
		mkd = open("tests/test_cases/sample2_header.md").read()
		tex = open("tests/test_cases/sample2_header.tex").read()
		self.assertEqual(headers(mkd).split(), tex.split())

unittest.main()

