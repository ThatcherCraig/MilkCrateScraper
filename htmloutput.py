f = open('test.html','w')
number = 7
message = """<!DOCTYPE html>
<html>
<head></head>
<body>
<p>As of *date* at 9:15am in the wallstreetbets Discussion Post " + ticker + " had " + mentions.toString() + " in " + comments.toString() + " comments. At market open " + ticker + " was valued at: $" + openprice.toString() + " at market close " + ticker.toString() + " was valued at: $" + closeprice.toString()</p>
</body>
</html>"""
f.write(message)
f.close()
