# How We Solve Serialize and Deserialize BST

Preorder traversal with explicit null markers preserves BST structure.

## Steps

1. Serialize with preorder, writing `#` for null children.
2. Deserialize by reading tokens left-to-right and recursively rebuilding nodes.
3. Round-trip the tree through encode and decode.
