<h1>I'm too lazy, hence I made this</h1>
<h2>Usage</h2>
<h3>wrapcli.py</h3>
<h4>Using configuration files</h4>
<code>python3 wrapcli.py [configuration file] [unparsed data file]</code>
<br><br><b>NOTE:</b> Configuration files should be formated as such:

  [header]<br>
  [body format] (use {n} for the (n+1)th data token)<br>
  [footer]<br>
  [token delimiter]<br>
  [body joiner]<br>

<h4>Using command line arguments</h4>
<code>python3 wrapcli.py [header] [body format] [unparsed data file] [footer] [token delimiter; default ' '] [body joiner; default ',']</code>

<h3>wrap.py</h3>
Contains a class named Wrapper with the same capabilities of wrapcli but as a python object
<h4>Set(header, body_format, footer, axe, glue)</h4>
<ul>
<li>header: the header</li>
<li>body_format: how to parse the file data (use {n} for the (n+1)th data token)</li>
<li>footer: the footer</li>
<li>axe: string separating each token per record in the data file</li>
<li>glue: string joining each body segment (record) after wrapping</li>
<h4>Wrap(filepath)</h4>
<li>filepath: path to data file (has to be consistent with axe aka token_delimiter)</li>
<li></li>
</ul>
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
