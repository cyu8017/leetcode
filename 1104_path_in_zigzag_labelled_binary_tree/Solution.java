// LeetCode 1104 - Path In Zigzag Labelled Binary Tree
// https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

import java.util.*;

class Solution {
    public List<Integer> pathInZigZagTree(int label) {
        List<Integer> path = new ArrayList<>();
        path.add(label);
        while (label > 1) {
            int level = 31 - Integer.numberOfLeadingZeros(label);
            label >>= 1;
            label = (1 << level) - 1 - label + (1 << (level - 1));
            path.add(label);
        }
        Collections.reverse(path);
        return path;
    }
}
