import xml.etree.ElementTree as ET
import sys
import datetime

file = ET.fromstring( open( sys.argv[1], "r" ).read() )
for post in file.findall("{http://www.w3.org/2005/Atom}entry"):
    if "#post" in post[3].attrib["term"]:
        ts = datetime.datetime.strptime( post[1].text, "%Y-%m-%dT%H:%M:%S.%fZ" )
        title = post.find("{http://www.w3.org/2005/Atom}title").text
        body = post.find("{http://www.w3.org/2005/Atom}content").text
        if body == None:
            continue
        if title == None:
            title = "Hmm"
        f = open( ts.strftime("%Y-%m-%d") + "-" + title.replace(" ", "-").replace(".", "") + ".markdown", "wt" )
        f.write( "---\n" )
        f.write( "layout: post\n" )
        f.write( "title: %s\n" % title.replace( ":", "" ) )
        f.write( "---\n" )
        f.write( body.encode( "UTF8" ) )
