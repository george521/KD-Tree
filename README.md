# KD-Tree #

This is an implementation of a 2D KD-Tree.

## Interface ##

The interface of the structure is in the file KDtree.py with the functions:

   * __insert(self, Point)__ Inserts a given point in the structure.
   * __search(self, top_left, bottom_right)__ Returns a List of points included inside the created rectangle.
   * __delete()__ Not implemented yet.
   
   ## Project structure ##

 *  __KDtree.py__ Provides an interface for the structure.
 *  __Node.py__ Represents a node in the tree. Implements all the funcionality of the structure.
 *  __Point.py__ Represents a 2D point stored in the tree.
 *  __Rectangle.py__ Represents a 2D range to query the tree.
