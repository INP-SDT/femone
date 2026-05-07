<!--
{
  "webtitle": "Modules \u2014 femone documentation",
  "codeblocks": false
}
-->

# femone.mesh

Mesh object.

## getmesh()

<pre class="py-sign">femone.mesh.<b>getmesh</b>(points)</pre>

Creates a mesh object.

<b>Parameters</b>

<p><span class="vardef"><code>points</code> : <em>flat-float-array</em></span></p>

<dl><dd>
  Input points.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>Mesh</em></span></p>

<dl><dd>
  Mesh object.
</dd></dl>

## Mesh

<pre class="py-sign"><b><em>class</em></b> femone.mesh.<b>Mesh</b>(points, elements)</pre>

Mesh object.

<b>Properties</b>

Name      |  Description
----------|---------------------------
`steps`   | Element sizes
`centrs`  | Element midpoints