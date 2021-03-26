# Python---Crossword-Puzzle
Objective: To pratice using 2D arrays, loops and comparisons.

General Application: a crossword puzzle game

Source: Horstmann, Big Java

Instructions

Arrays store a linear arrangement of values, accessed by a single index. Two-dimensional arrays or matrices store a tabular arrangement of values, accessed by two indices, for example matrix[i][j], where i is the row index, and j is the column index.

Crosswords are a type of puzzle where the "pieces" of the puzzle have letters in common. For example, these pieces share the letter 'o'.

      d
      
a c r o s s

      w 
      
      n

The program will accept a list of words into an array list of strings, then make a 20 x 20 matrix of characters (strings of length 1) that contains a crossword puzzle with these words.

For example, when given the list [addle, apple, clowning, incline, plan, burr], the program might display:

  a d d l e 
  
  p
  
  p
  
c l o w n i n g 

  e       n
  
          c
          
          l
          
          i
          
    p l a n e
    
          e

Below is an example which is not legal because of words touching each other. Note how "prove" is added in a fashion which is illegal since it creates additional words "dr", "do", "lv", and "ee". Similarly, the addition of "no" vertically is illegal since it creates the extra word "no" horizontally. 

  a d d l e 
  
  p r o v e 
  
  p
  
c l o w n i n g 

  e       n o
  
          c 
          
          l
          
          i
          
    p l a n
    
          e
 
Here is another example of how a word can be added legally -- the addition of "loon" uses two letters that are in the puzzle already, which creates no problem since there are no new words created other than the single word added "loon".)

  a d d l e 
  
  p     o
  
  p     o
  
c l o w n i n g

  e       n
  
          c
          
          l 
          
          i
          
    p l a n
    
          e

To summarize: A legal placement of a word W has the following properties:

i.	All of the word W lies on the 20x20 grid;

ii.	If W is not the first word, then W must intersect with one or more words on the grid;

iii.	The placement of W must not create any new 'words', i.e., W cannot be adjacent to any letter which is not in the word(s) with which W intersects.
