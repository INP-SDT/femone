<!--
{
  "webtitle": "Modules \u2014 femone documentation",
  "codeblocks": false
}
-->

# femone.fem

Finite element (P1) solver.

## getunit()

<pre class="py-sign">femone.fem.<b>getunit</b>(mesh)</pre>

Creates a FEM computing unit.

<b>Parameters</b>

<p><span class="vardef"><code>mesh</code> : <em>Mesh</em></span></p>

<dl><dd>
  Mesh object.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>FEMUnit</em></span></p>

<dl><dd>
  Resulting FEM unit.
</dd></dl>

## FEMUnit

<pre class="py-sign"><b><em>class</em></b> femone.fem.<b>FEMUnit</b>(mesh, meta)</pre>

FEM computing unit.

<b>Properties</b>

Basic FEM operators as data-streams:

Name        | Description
------------|------------------------------------
`massmat`   | Mass-matrix
`massdig`   | Mass-matrix (lumped)
`diff_1x`   | 1st derivative (weak)
`grad_1x`   | 1st derivative (strong)
`diff_2x`   | 2nd derivative (weak)

Indexers of a data-stream:

Name        | Description
------------|-------------------------------------
`ij_r`      | Row numbers in a data stream
`ij_c`      | Column numbers in a data stream
`ij_e`      | Element numbers in a data stream

General properties:

Name        | Description
------------|-------------------------------------
`xax`       | Shortcut for mesh points.
`cax`       | Shortcut for mesh midpoints.
`mass`      | Mass matrix.

### makemat()

<pre class="py-sign">FEMUnit.<b>makemat</b>(<em>self</em>, operator)</pre>

Creates a FEM matrix.

<b>Parameters</b>

<p><span class="vardef"><code>operator</code> : <em>flat-float-array</em></span></p>

<dl><dd>
  FEM operator as a linear combination of basic FEM operators.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>csc_array</em></span></p>

<dl><dd>
  Sparse matrix in CSC form.
</dd></dl>

### vec_from_func()

<pre class="py-sign">FEMUnit.<b>vec_from_func</b>(<em>self</em>, func)</pre>

Creates a vector defined on mesh points.

<b>Parameters</b>

<p><span class="vardef"><code>func</code> : <em>Callable</em></span></p>

<dl><dd>
  Defines vector data.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>flat-float-array</em></span></p>

<dl><dd>
  Resulting vector.
</dd></dl>

### vec_with_body()

<pre class="py-sign">FEMUnit.<b>vec_with_body</b>(<em>self</em>, body)</pre>

Creates a vector defined on mesh points.

<b>Parameters</b>

<p><span class="vardef"><code>body</code> : <em>float | flat-float-array</em></span></p>

<dl><dd>
  Defines the vector body.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>flat-float-array</em></span></p>

<dl><dd>
  Resulting vector.
</dd></dl>

### project_p0_p1()

<pre class="py-sign">FEMUnit.<b>project_p0_p1</b>(<em>self</em>, data)</pre>

Projects P0 data to P1 space.

<b>Parameters</b>

<p><span class="vardef"><code>data</code> : <em>flat-float-array</em></span></p>

<dl><dd>
  Input P0 data.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>flat-float-array</em></span></p>

<dl><dd>
  Resulting P1 data.
</dd></dl>

### project_p1_p0()

<pre class="py-sign">FEMUnit.<b>project_p1_p0</b>(<em>self</em>, data)</pre>

Projects P1 data to P0 space.

<b>Parameters</b>

<p><span class="vardef"><code>data</code> : <em>flat-float-array</em></span></p>

<dl><dd>
  Input P1 data.
</dd></dl>

<b>Returns</b>

<p><span class="vardef"><em>flat-float-array</em></span></p>

<dl><dd>
  Resulting P0 data.
</dd></dl>