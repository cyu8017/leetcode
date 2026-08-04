// LeetCode 1902 - Depth of BST Given Insertion Order
// https://leetcode.com/problems/depth-of-bst-given-insertion-order/

import java.util.*;

class Solution {
    public int maxDepthBST(int[] order) {
        TreeMap<Integer, Integer> map = new TreeMap<>();
        int ans = 0;
        for (int value : order) {
            Map.Entry<Integer, Integer> lo = map.floorEntry(value);
            Map.Entry<Integer, Integer> hi = map.ceilingEntry(value);
            int depth = 1;
            if (lo != null) depth = Math.max(depth, lo.getValue() + 1);
            if (hi != null) depth = Math.max(depth, hi.getValue() + 1);
            map.put(value, depth);
            ans = Math.max(ans, depth);
        }
        return ans;
    }
}
