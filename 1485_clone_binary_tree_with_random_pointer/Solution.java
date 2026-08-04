// LeetCode 1485 - Clone Binary Tree With Random Pointer
// https://leetcode.com/problems/clone-binary-tree-with-random-pointer/

import java.util.*;

class Node {
    public int val; public Node left; public Node right; public Node random;
    public Node(int val = 0) { this.val = val; }
}
class Solution {
    Map<Node, Node> copies = new HashMap<>();
    public Node copyRandomBinaryTree(Node root) {
        if (root == null) return null;
        if (!copies.containsKey(root)) {
            copies[root] = new Node(root.val);
            copies[root].left = CopyRandomBinaryTree(root.left);
            copies[root].right = CopyRandomBinaryTree(root.right);
            copies[root].random = CopyRandomBinaryTree(root.random);
        }
        return copies[root];
    }
}
