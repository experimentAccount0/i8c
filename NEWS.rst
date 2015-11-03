What has changed in I8C?
========================

Changes since I8C 0.0.1
-----------------------

Source language changes
~~~~~~~~~~~~~~~~~~~~~~~

* Operators with more than one argument now require their arguments to
  be separated by commas.  Existing code using the "name" and "cast"
  operators must be updated.

* Many operators now have an optional ''folded load'' first argument.
  A folded load is exactly equivalent to a load immediately before
  the statement with the folded load, so, for example, this code::

    load 1
    add
    load 5
    bgt label

  may now be written as::

    add 1
    bgt 5, label

  Operators which may have folded loads are:

    * All binary math and logic operators: add, and, div, mod, mul,
      or, shl, shr, shra, sub, xor.

    * All comparisons: eq, ge, gt, le, lt, ne.

    * All conditional branches: beq, bge, bgt, ble, blt, bne.

    * Others: call, deref.

  Operarators which may ''not'' have folded loads are:

    * All unary math and logic operators: abs, neg, not.

    * All stack manipulation operators: drop, dup, over, pick, rot,
      swap.

    * Others: cast, goto, load, name, return.

* The "name" operator now accepts slot names as its first argument.
  This can be used to add new names to already-named slots by name.

Note format changes
~~~~~~~~~~~~~~~~~~~

* The "max_stack" field from the info chunk and the byteorder mark
  from the code chunk have been moved into a new "code info" chunk
  with a type_id of 6.

* The remainder of what was the info chunk has been moved into a new
  "signature" chunk with a type_id of 5.

* The code chunk now contains only bytecode.  Its version has been
  incremented to 2 to indicate this.

Bug fixes
~~~~~~~~~

* Older versions of unittest are detected and handled in setup.py;
  both the testsuite and I8X should now work out of the box with
  Python 2.6 and 3.1.

* "i8c -S" now outputs to a file unless "-o -" is specified on the
  command line.  (https://github.com/gbenson/i8c/issues/32)

* Stack underflow checks in I8C were off by one in some cases.

* I8C's parser now correctly raises an error if arguments are supplied
  for zero-argument operations.

* I8C's branch-elimination optimizer incorrectly regarded some
  operations as equivalent.  This caused code to be incorrectly
  optimized away in some cases.

Enhancements
~~~~~~~~~~~~

* I8C's branch-elimination optimizer now recognizes that "dup" and
  "over" are equivalents of "pick 0" and "pick 1" respectively.