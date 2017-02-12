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
	
	for md_code in re.findall(r"^#####[^#].*", mkd, re.M):
		tex_code = "\subparagraph{" + re.findall(r"#####(.*)", md_code, re.M)[0] + "}"
		mkd = mkd.replace(md_code, tex_code)

	for md_code in re.findall(r"^####[^#].*", mkd, re.M):
		tex_code = "\paragraph{" + re.findall(r"####(.*)", md_code, re.M)[0] + "}"
		mkd = mkd.replace(md_code, tex_code)

	for md_code in re.findall(r"^###[^#].*", mkd, re.M):
		tex_code = "\subsubsection{" + re.findall(r"###(.*)", md_code, re.M)[0] + "}"
		mkd = mkd.replace(md_code, tex_code)

	for md_code in re.findall(r"^##[^#].*", mkd, re.M):
		tex_code = "\subsection{" + re.findall(r"##(.*)", md_code, re.M)[0] + "}"
		mkd = mkd.replace(md_code, tex_code)

	for md_code in re.findall(r"^#[^#].*", mkd, re.M):
		tex_code = "\section{" + re.findall(r"#(.*)", md_code, re.M)[0] + "}"
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
	
	for md_code in re.findall(r"\*\*.*?\*\*", mkd, re.M):
		tex_code = "\\textbf{" + re.findall(r"\*\*(.*?)\*\*", md_code, re.M)[0] + "}"
		mkd = mkd.replace(md_code, tex_code)
	
	for md_code in re.findall(r"__.*?__", mkd, re.M):
		tex_code = "\\textbf{" + re.findall(r"__(.*?)__", md_code, re.M)[0] + "}"
		mkd = mkd.replace(md_code, tex_code)
	
	return mkd


def convert_italics(mkd):
	
	"""
	Convert bold tags (*,_) to LaTeX textit

	:param mkd: markdown text
	:type mkd: string
	:return: corresponding LaTeX codes
	:rtype: string
	"""
	
	for md_code in re.findall(r"\*.*?\*", mkd, re.M):
		tex_code = "\\textit{" + re.findall(r"\*(.*?)\*", md_code, re.M)[0] + "}"
		mkd = mkd.replace(md_code, tex_code)
	
	for md_code in re.findall(r"_.*?_", mkd, re.M):
		tex_code = "\\textit{" + re.findall(r"_(.*?)_", md_code, re.M)[0] + "}"
		mkd = mkd.replace(md_code, tex_code)

	return mkd


def convert_images(mkd):
	
	"""
	Convert image tags to LaTeX codes

	:param mkd: markdown text
	:type mkd: string
	:return: corresponding LaTeX codes
	:rtype: string
	"""
	
	md_image_caption_codes = re.findall(r"!\[alt text\]\(.*?\".*?\".*?\)", mkd, re.M)
	for md_code in md_image_caption_codes:
		image, caption = re.findall(r"!\[alt text\]\((.*?)\"(.*?)\".*?\)", md_code, re.M)[0]
		tex_code = "\\begin{figure}[p]\n\centering\n\includegraphics{" + image.strip() + "}\n\caption{" + caption.strip() + "}\n\end{figure}"
		mkd = mkd.replace(md_code, tex_code)
	
	md_image_codes = re.findall(r"!\[alt text\]\(.*?\)", mkd, re.M)
	for md_code in md_image_codes:
		image = re.findall(r"!\[alt text\]\((.*?)\)", md_code, re.M)[0]
		tex_code = "\\begin{figure}[p]\n\centering\n\includegraphics{" + image.strip() + "}\n\end{figure}"
		mkd = mkd.replace(md_code, tex_code)
	
	#The bool below is to flag if there has been any code to convert. If True, packages need to be added on top of the tex file
	return mkd, bool(md_image_codes or md_image_caption_codes)


def convert_links(mkd):
	
	"""
	Convert markdown links to LaTeX code

	:param mkd: markdown text
	:type mkd: string
	:return: corresponding LaTeX codes
	:rtype: string
	"""
	
	md_link_codes = re.findall(r"\[.*?\]\(.*?\)", mkd, re.M)
	for md_code in md_link_codes:
		label, link = re.findall(r"\[(.*?)\]\((.*?)\)", md_code, re.M)[0]
		tex_code = "\\href{" + link + "}{" + label + "}"
		mkd = mkd.replace(md_code, tex_code)

	return mkd, bool(md_link_codes)


def convert_lists(mkd, tab_level=0):
	
	"""
	Convert markdown lists to LaTeX code. Works recursively to convert lists on current indent level.

	:param mkd: markdown text
	:type mkd: string
	:param tab_level: track indentation currently working on
	:type tab_level: int
	:return: corresponding LaTeX codes
	:rtype: string
	"""
	
	#list all unordered list codes for current indent level
	md_unordered_list_codes = re.findall(r"^\t{"+str(tab_level)+"}[\*\-\+] .+(?:\n\t{"+str(tab_level)+",}[\*|\-|\+] .+)*", mkd, re.M)
	for md_code in md_unordered_list_codes:
		
		#add itemize begin/end block
		tex_code = "\\begin{itemize}\n" + md_code + "\n\end{itemize}"
		mkd = mkd.replace(md_code, tex_code)

		#convert each element of list for current indent level
		md_item_codes = re.findall(r"^\t{"+str(tab_level)+"}[\*\-\+] .*$", md_code, re.M)
		for md_code in md_item_codes:
			item = re.findall(r"^\t{"+str(tab_level)+"}[\*\-\+] (.*)$", md_code, re.M)[0]
			tex_code = "\item " + item
			mkd = mkd.replace(md_code, tex_code)
	

	#ordered list conversion works similar to unordered list conversion
	md_ordered_list_codes = re.findall(r"^\t{"+str(tab_level)+"}[0-9]+\. .+(?:\n\t{"+str(tab_level)+",}[0-9]+\. .+)*", mkd, re.M)
	for md_code in md_ordered_list_codes:
		tex_code = "\\begin{enumerate}\n" + md_code + "\n\end{enumerate}"
		mkd = mkd.replace(md_code, tex_code)

		md_item_codes = re.findall(r"^\t{"+str(tab_level)+"}[0-9]+\. .*$", md_code, re.M)
		for md_code in md_item_codes:
			item = re.findall(r"^\t{"+str(tab_level)+"}[0-9]+\. (.*)$", md_code, re.M)[0]
			tex_code = "\item " + item
			mkd = mkd.replace(md_code, tex_code)


	if md_unordered_list_codes or md_ordered_list_codes:
		mkd = convert_lists(mkd, tab_level+1)
	
	return mkd


#mkd = open("../tests/test_cases/sample_ol.md").read()
#print(convert_lists(mkd))
