#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest, mock
from src.conversions import convert_headers
from src.md2tex import main, parse_args

#Set directory for test environment
TEST_DIR = "./tests/test_cases/"
os.environ["DIR"] = TEST_DIR

SAMPLE_TEST_FILE = "test_sample"

class Test_Conversions(unittest.TestCase):
	
	"""Test cases or conversion modules"""
	
	def test_headers(self):
		
		mkd = open(TEST_DIR+"sample_header1.md").read()
		tex = open(TEST_DIR+"sample_header1.tex").read()
		self.assertEqual(convert_headers(mkd).split(), tex.split())
		
		mkd = open(TEST_DIR+"sample_header2.md").read()
		tex = open(TEST_DIR+"sample_header2.tex").read()
		self.assertEqual(convert_headers(mkd).split(), tex.split())


class Integration_Tests(unittest.TestCase):

	"""Integration tests"""

	def test_header_integration(self):
		
		#Creat new document
		inputs = ["Sample", "Pratik", "article", "12"]
		with mock.patch('__builtin__.input', side_effect=inputs):
			main(parse_args(["-n", SAMPLE_TEST_FILE]))
		
		#Write markdown content
		mkd = open(TEST_DIR+SAMPLE_TEST_FILE+".md","w")
		mkd.write(open(TEST_DIR+"sample_header2.md").read())
		mkd.close()

		#Convert to LaTeX
		main(parse_args([SAMPLE_TEST_FILE]))
		
		tex1 = open(TEST_DIR+SAMPLE_TEST_FILE+".tex").read()
		tex2 = open(TEST_DIR+"sample_header_integration.tex").read()
		self.assertEqual(tex1.split(), tex2.split())


unittest.main()

