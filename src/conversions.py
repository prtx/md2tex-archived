#!/usr/bin/env python

"""
Contains all funtions to convert markdown codes to LaTeX.
"""

import re

def convert_headers(mkd):
	
	"""
	Convert header tags (#,##...) to LaTeX section, subsections....

	:param mkd: markdown text
	:type mkd: string
	:return: corresponding LaTeX codes
	:rtype: string
	"""
	
	for md_code in re.findall(r"^(#####[^#].*)", mkd, re.M):
		tex_code = "\subparagraph{" + re.findall(r"#####(.*)", md_code)[0] + "}"
		mkd = mkd.replace(md_code, tex_code)
	for md_code in re.findall(r"^(####[^#].*)", mkd, re.M):
		tex_code = "\paragraph{" + re.findall(r"####(.*)", md_code)[0] + "}"
		mkd = mkd.replace(md_code, tex_code)
	for md_code in re.findall(r"^(###[^#].*)", mkd, re.M):
		tex_code = "\subsubsection{" + re.findall(r"###(.*)", md_code)[0] + "}"
		mkd = mkd.replace(md_code, tex_code)
	for md_code in re.findall(r"^(##[^#].*)", mkd, re.M):
		tex_code = "\subsection{" + re.findall(r"##(.*)", md_code)[0] + "}"
		mkd = mkd.replace(md_code, tex_code)
	for md_code in re.findall(r"^(#[^#].*)", mkd, re.M):
		tex_code = "\section{" + re.findall(r"#(.*)", md_code)[0] + "}"
		mkd = mkd.replace(md_code, tex_code)

	return mkd


def convert_bold(mkd):
	
	"""
	Convert bold tags (**,__) to LaTeX textbf

	:param mkd: markdown text
	:type mkd: string
	:return: corresponding LaTeX codes
	:rtype: string
	"""
	
	return mkd


def convert_italics(mkd):
	
	"""
	Convert bold tags (*,_) to LaTeX textit

	:param mkd: markdown text
	:type mkd: string
	:return: corresponding LaTeX codes
	:rtype: string
	"""
	
	return mkd


def convert_images(mkd):
	
	"""
	Convert image tags to LaTeX codes

	:param mkd: markdown text
	:type mkd: string
	:return: corresponding LaTeX codes
	:rtype: string
	"""
	
	return mkd


def convert_links(mkd):
	
	"""
	Convert markdown links to LaTeX code

	:param mkd: markdown text
	:type mkd: string
	:return: corresponding LaTeX codes
	:rtype: string
	"""
	
	return mkd


mkd = open("../tests/test_cases/sample_bold.md").read()
print(convert_bold(mkd))
