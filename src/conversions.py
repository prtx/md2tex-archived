#!/usr/bin/env python

"""
Contains all funtions to convert markdown codes to LaTeX.
"""

import re

def headers(mkd):
	
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

#mkd = open("../tests/test_cases/sample1_header.md").read()
#print(headers(mkd))
