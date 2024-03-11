<h1>I'm too lazy, hence I made this</h1>
<h2>Usage</h2>
<h1>Using configuration files</h1>
<code>python3 wrap.py [configuration file] [unparsed data file]</code>
<b>NOTE:</b> Configuration files should be formated as such:

  [header]
  [body format] (use {n} for the (n+1)th data token)
  [tail]
  [token delimiter]
  [body joiner]

<h1>Using command line arguments</h1>
<code>python3 wrap.py [header] [body format] [unparsed data file] [token delimiter; default ' '] [body joiner; default ',']</code>
