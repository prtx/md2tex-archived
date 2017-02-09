#!/usr/bin/env python

import argparse, re, os
import xml.etree.cElementTree as ET
from conversions import convert_headers, convert_links, convert_images

OUTPUT_DIR = os.environ.get("OUTPUT_DIR") or "./samples/"
TEMPLATES_DIR = os.environ.get("TEMPLATE_DIR") or "./templates/"

	
def parse_args(args=None):
	
	"""
	Function to parse command line arguments
	
	:param args: parser arguments
	:type args: list
	:return: command line argument information
	:rtype: argparse.Namespace
	"""

	parser = argparse.ArgumentParser(description="Convert markdown to LaTeX.")
	parser.add_argument("document", type=str, help="Provide markdown file to convert to LaTeX")
	parser.add_argument("-n", "--newdocument", action="store_true", help="Start new document")
	parser.add_argument("-o", "--output", action="store_true", help="Generatee output PDF")
	parser.add_argument("-c", "--clean", action="store_true", help="generate only pdf and no other files")
	
	#if arguments passed as parameters then parse them else not
	if args:
		return parser.parse_args(args)
	return parser.parse_args()


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
	
	md_file = open(OUTPUT_DIR+document+".md", "w")
	md_file.close()




def create_tex_file(document):
	
	"""
	Create TeX file based on user defined XML attributes.
	
	:param document: name of document
	:type document: str
	"""

	base_tex_content = open(TEMPLATES_DIR+"base.tex").read()
	
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


def add_tex_package(document, package, option):
	
	"""
	Add required packages and options to tex file
	
	:param document: name of document
	:type document: str
	:param package: name of package
	:type package: str
	:param option: packag options
	:type option: str
	"""
	
	package_code ="%packages\n\\usepackage["+option+"]{"+package+"}"

	tex_content = open(OUTPUT_DIR+document+".tex").read()
	tex_content = tex_content.replace("%packages", package_code)
	
	tex_file = open(OUTPUT_DIR+document+".tex", "w")
	tex_file.write(tex_content)
	tex_file.close()


def convert_markdown(document):
	
	"""
	Convert markdown code to LaTeX.
	
	:param document: name of document
	:type document: str
	"""
	
	mkd = open(OUTPUT_DIR+document+".md").read()
	
	mkd = convert_headers(mkd)
	mkd, image_converted = convert_images(mkd)
	if image_converted:
		add_tex_package(document, "graphicx", "")
	mkd, link_converted = convert_links(mkd)
	if link_converted:
		add_tex_package(document, "hyperref", "")

	tex_file = open(OUTPUT_DIR+document+".tex")
	tex = tex_file.read()
	tex_file.close()
	
	tex_file = open(OUTPUT_DIR+document+".tex", "w")
	tex = tex.replace("%CONTENTS", mkd)
	tex_file.write(tex)
	tex_file.close()


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


def main(args):
	
	"""
	Main Function. It all started with the big bang. BANG!
	
	:paran args: command line argument information
	:type args: argparse.Namespace
	"""
	
	# Start new document project
	if args.newdocument:
		init_project(args.document)
	
	create_tex_file(args.document)
	convert_markdown(args.document)

	if args.output:
		generate_pdf(args.document, args.clean)



if __name__=="__main__":
	main(parse_args())
