// LeetCode 1522 - Diameter of N-Ary Tree
// https://leetcode.com/problems/diameter-of-n-ary-tree/

import java.util.*;

class Node {
    public int val;
    public List<Node> children;

    public Node() {
        children = new ArrayList<>();
    }

    public Node(int val) {
        this.val = val;
        children = new ArrayList<>();
    }

    public Node(int val, List<Node> children) {
        this.val = val;
        this.children = children;
    }
}

class Solution {
    private int answer;

    public int diameter(Node root) {
        answer = 0;
        if (root != null) {
            depth(root);
        }
        return answer;
    }

    private int depth(Node node) {
        int longest = 0;
        int second = 0;
        for (Node child : node.children) {
            int value = depth(child) + 1;
            if (value > longest) {
                second = longest;
                longest = value;
            } else if (value > second) {
                second = value;
            }
        }
        answer = Math.max(answer, longest + second);
        return longest;
    }
}
