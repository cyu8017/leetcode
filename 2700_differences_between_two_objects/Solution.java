// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/

import java.util.*;

// JS objDiff stand-in: keys where values differ
class Solution {
    public TreeMap<String, int[]> objDiff(TreeMap<String, Integer> obj1, TreeMap<String, Integer> obj2) {
        TreeMap<String, int[]> diff = new TreeMap<>();
        for (Map.Entry<String, Integer> kv : obj1.entrySet()) {
            Integer v2 = obj2.get(kv.getKey());
            if (v2 != null && !v2.equals(kv.getValue()))
                diff.put(kv.getKey(), new int[] {kv.getValue(), v2});
        }
        return diff;
    }
}
