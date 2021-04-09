# Binary Tree

A tree where the elements have <= 2 children is a binary tree. The children are called the left and right child respectively.

If you are storing hierarchical information, this data structure is a good bet. For example, the file system on a computer.

If you ensure the tree in ordered in a certain way (eg binary search tree), you can access data faster than a linked-list but slower than arrays. You can insert data faster than arrays  but slower than a linked list.

There is no upper limit on the number of nodes because they do not need to be in contiguous memory.

Each node in the tree contains:

- data
- an optional pointer to the left child
- an optional pointer to the right child

## Binary Tree Properties

- The *maximum* number of nodes on level L of the tree is 2^L, where L=0 at the root level. This sequenece proceeeds as 1, 2, 4, 8, ...
- The *maximum* number of nodes in a binary tree of height H, is (2^H)-1. Eg a tree of height = 3 has a max of 7 nodes. 1 + 2 + 4 = 7.
- If there are N nodes in a tree, the maximum possible height is H=Log_2(N+1). This is just maths from the step above
- A binary tree with L leaves has *at least* log_2(L) + 1 levels. The minimum height of a tree with L leaves is when all rows are filled.

number nodes on level l = 2^(l-1)
L = 2^(l-1)
l = ceil(log_2(L)) + 1

If L = 4, the minimum height = 3. If L = 2, the minimum height = 2.

- In a binary tree where every node has 0 or 2 children, the number of leaf nodes is always 1 more than the number of nodes with 2 children.

## Types of binary tree

- In a *full binary tree* every node has 0 or 2 children.
- In a *complete binary tree*, all levels are filled, excluding the final level which must be filled from the left.
- In a *perfect binary tree*, all internal nodes have 2 children and all leaves are at the same level. A ancestral family tree is an example of this. Put yourself at the root. You have 2 parents. They each have 2 parents and so on.
- A *balanced binary tree* has height = Log(n). The height of the left and right subtrees at *every node* must differ by no more than 1.
- In a *pathological binary tree* every internal node has one child (eg linked list)

## Binary Search Trees

- For every node in a BST, all nodes in left subtree <= current < all nodes in right subtree

## Traversal

### In-order traversal

Visits the left, the node and then the right (in order).

### Pre-order traversal

Visits the node before (pre) the children.

### Post-order traversal

Visits the node after (post) the children.

### Level-order traversal (bread first traversal)

Visit nodes level by level from left to right

# Binary Heaps (Min-heaps and max-heaps)

A min heap is a complete binary tree where every node is smaller than it's children. They have 2 key operations:

- insert(element) - add the element at the bottom right, then fix the tree to maintain min-heap properties. We bubble up the new element, swapping it with it's parent as many times as possible.
- extract_min() - Remove the minimum element and replace it with the last element in the heap. Bubble down the last element to restore the heap property. O(log(n))
