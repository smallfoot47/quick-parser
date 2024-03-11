<h1>I'm too lazy, hence I made this</h1>
<h2>Usage</h2>
<h3>Using configuration files</h3>
<code>python3 wrap.py [configuration file] [unparsed data file]</code>
<br><br><b>NOTE:</b> Configuration files should be formated as such:

  [header]<br>
  [body format] (use {n} for the (n+1)th data token)<br>
  [tail]<br>
  [token delimiter]<br>
  [body joiner]<br>

<h3>Using command line arguments</h3>
<code>python3 wrap.py [header] [body format] [unparsed data file] [token delimiter; default ' '] [body joiner; default ',']</code>

<h2>Future Directions</h2>
<ul>
  <li>Adaptive body format</li>
  <li>Soft scripting support<ul>
    <li>header logic based on data</li>
    <li>body format logic based on data</li>
    <li>tail logic based on data</li>
    <li>token delimiter based on data</li>
    <li>body joiner based on data</li>
  </ul></li>
</ul>
