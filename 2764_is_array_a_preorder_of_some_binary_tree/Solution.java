// LeetCode 2764 - Is Array a Preorder of Some Binary Tree
// https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public boolean isPreorder(List<List<Integer>> nodes) {
        if (nodes.size() == 0) return true;
        var stack = new ArrayList<Integer>();
        stack.add(nodes[0][0]);
        for (int i = 1; i < nodes.size(); i++) {
            int id = nodes[i][0], parent = nodes[i][1];
            while (stack.size() > 0 && stack.get(^1) != parent) stack.remove(stack.size() - 1);
            if (stack.size() == 0) return false;
            stack.add(id);
        }
        return true;
    }
}
