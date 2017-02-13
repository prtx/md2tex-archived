#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

#Set directories for test environment
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
TEST_DIR = "./tests/test_cases/"
os.environ.setdefault("OUTPUT_DIR", TEST_DIR)
os.environ.setdefault("TEMPLATE_DIR", "./src/templates/")

import unittest, mock
from src.conversions import convert_headers, convert_bold, convert_italics
from src.md2tex import main, parse_args


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

	
	def test_bold(self):
		
		mkd = open(TEST_DIR+"sample_bold.md").read()
		tex = open(TEST_DIR+"sample_bold.tex").read()
		self.assertEqual(convert_bold(mkd).split(), tex.split())
		
	
	def test_italics(self):

		mkd = open(TEST_DIR+"sample_italics.md").read()
		tex = open(TEST_DIR+"sample_italics.tex").read()
		self.assertEqual(convert_italics(mkd).split(), tex.split())



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
	
	def test_images(self):
	
		#Write markdown content
		mkd = open(TEST_DIR+SAMPLE_TEST_FILE+".md","w")
		mkd.write(open(TEST_DIR+"sample_image.md").read())
		mkd.close()

		#Convert to LaTeX
		main(parse_args([SAMPLE_TEST_FILE]))
		
		tex1 = open(TEST_DIR+SAMPLE_TEST_FILE+".tex").read()
		tex2 = open(TEST_DIR+"sample_image.tex").read()
		self.assertEqual(tex1.split(), tex2.split())
	
	def test_links(self):
	
		#Write markdown content
		mkd = open(TEST_DIR+SAMPLE_TEST_FILE+".md","w")
		mkd.write(open(TEST_DIR+"sample_links.md").read())
		mkd.close()

		#Convert to LaTeX
		main(parse_args([SAMPLE_TEST_FILE]))
		
		tex1 = open(TEST_DIR+SAMPLE_TEST_FILE+".tex").read()
		tex2 = open(TEST_DIR+"sample_links.tex").read()
		self.assertEqual(tex1.split(), tex2.split())

	def test_lists1(self):
		
		"""
		Test unordered lists	
		"""

		#Write markdown content
		mkd = open(TEST_DIR+SAMPLE_TEST_FILE+".md","w")
		mkd.write(open(TEST_DIR+"sample_ul.md").read())
		mkd.close()

		#Convert to LaTeX
		main(parse_args([SAMPLE_TEST_FILE]))
		
		tex1 = open(TEST_DIR+SAMPLE_TEST_FILE+".tex").read()
		tex2 = open(TEST_DIR+"sample_ul.tex").read()
		self.assertEqual(tex1.split(), tex2.split())

	
	def test_lists2(self):
		
		"""
		Test ordered lists	
		"""

		#Write markdown content
		mkd = open(TEST_DIR+SAMPLE_TEST_FILE+".md","w")
		mkd.write(open(TEST_DIR+"sample_ol.md").read())
		mkd.close()

		#Convert to LaTeX
		main(parse_args([SAMPLE_TEST_FILE]))
		
		tex1 = open(TEST_DIR+SAMPLE_TEST_FILE+".tex").read()
		tex2 = open(TEST_DIR+"sample_ol.tex").read()
		self.assertEqual(tex1.split(), tex2.split())

	def test_lists3(self):
		
		"""
		Test combined unordered and orderd lists	
		"""

		#Write markdown content
		mkd = open(TEST_DIR+SAMPLE_TEST_FILE+".md","w")
		mkd.write(open(TEST_DIR+"sample_list.md").read())
		mkd.close()

		#Convert to LaTeX
		main(parse_args([SAMPLE_TEST_FILE]))
		
		tex1 = open(TEST_DIR+SAMPLE_TEST_FILE+".tex").read()
		tex2 = open(TEST_DIR+"sample_list.tex").read()
		self.assertEqual(tex1.split(), tex2.split())

	def test_tables(self):
		
		"""
		Test tables
		"""

		#Write markdown content
		mkd = open(TEST_DIR+SAMPLE_TEST_FILE+".md","w")
		mkd.write(open(TEST_DIR+"sample_table.md").read())
		mkd.close()

		#Convert to LaTeX
		main(parse_args([SAMPLE_TEST_FILE]))
		
		tex1 = open(TEST_DIR+SAMPLE_TEST_FILE+".tex").read()
		tex2 = open(TEST_DIR+"sample_table.tex").read()
		self.assertEqual(tex1.split(), tex2.split())

unittest.main()
