## Unit 1 Classwork

# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.

def findLink(page, start):
    start_link = page.find('<a href=', start)
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    return page[start_quote+1:end_quote], end_quote
    
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
# print findLink(page)


## Homework 1, Question 1
page = '<html xmlns="http://www.w3.org/1999/xhtml"><br/> <head><br/><title>Udacity</title> <br/></head><br/><br/><body> <br/><h1>Udacity</h1><br/><br/> <p><b>Udacity</b> is a private institution of <a href="http://www.wikipedia.org/wiki/Higher_education"> higher education founded by</a> <a href="http://www.wikipedia.org/wiki/Sebastian_Thrun">Sebastian Thrun</a>, David Stavens, and Mike Sokolsky with the goal to provide university-level education that is "both high quality and low cost".<br/>It is the outgrowth of a free computer science class offered in 2011 through Stanford University. Currently, Udacity is working on its second course on building a search engine. Udacity was announced at the 2012 <a href="http://www.wikipedia.org/wiki/Digital_Life_Design">Digital Life Design</a> conference.</p><br/></body><br/></html>'

def printAllLinks(page):
    i = 0
    while i < page.rfind('<a href='):
        link,i = findLink(page,i)
        print link
        
printAllLinks(page)