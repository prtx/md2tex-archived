#!/usr/bin/python

import argparse, re, os
import xml.etree.cElementTree as ET

OUTPUT_DIR = "./samples/"


def init_project(document):
	
	"""
	Initialize LaTeX document. Reads LaTeX attributes to XML
	:param document: name of document
	:type document: str
	"""
	
	root = ET.Element("document", name=document)
	tree = ET.ElementTree(root)
	
	print("Document: ", document)
	title = ET.SubElement(root, "title").text = input("Title: ")
	author = title = ET.SubElement(root, "author").text = input("Author: ")
	document_class = title = ET.SubElement(root, "document_class").text = input("Document Class: ") or "article"
	font_size = title = ET.SubElement(root, "font_size").text = input("Font Size(12pt): ") or "12"

	tree.write(OUTPUT_DIR+document+".xml")


def create_tex_file(document):
	
	"""
	Create TeX file based on user defined XML attributes.
	:param document: name of document
	:type document: str
	"""

	base_tex_content = open("templates/init.txt").read()
	
	tree = ET.parse(OUTPUT_DIR+document+".xml")
	root = tree.getroot()

	varibles = {
		"TITLE": root.findall("./title")[0].text,
		"AUTHOR": root.findall("./author")[0].text,
		"DOCUMENT_CLASS": root.findall("./document_class")[0].text,
		"FONT_SIZE": root.findall("./font_size")[0].text,
	}

	for key in varibles:
		base_tex_content = base_tex_content.replace(key, varibles[key])
	
	tex_file = open(OUTPUT_DIR+document+".tex", "w")
	tex_file.write(base_tex_content)
	tex_file.close()

	md_file = open(OUTPUT_DIR+document+".md", "w")
	md_file.close()


def generate_pdf(document, clean):
	
	"""
	Generate pdf from TeX file based on user provided attribute.
	:param document: name of document
	:type document: str
	:param clean: argument clean from argparse
	:type clean: bool
	"""

	os.system("pdflatex "+OUTPUT_DIR+document+".tex")
	if clean:
		os.system("rm "+document+".aux "+document+".log")


def main():
	
	"""
	Main Function. It all started with the big bang. BANG!
	"""
	
	parser = argparse.ArgumentParser(description="Convert markdown to LaTeX.")
	parser.add_argument("-n", "--newdocument", type=str, help="start new document")
	parser.add_argument("-c", "--clean", action='store_true', help="generate only pdf and no other files")
	args = parser.parse_args()
	
	# Start new document project
	if args.newdocument:
		init_project(args.newdocument)
		create_tex_file(args.newdocument)
		generate(args.newdocument, args.clean)


if __name__=="__main__":
	main()
