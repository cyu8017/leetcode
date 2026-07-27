// LeetCode 1640 - Check Array Formation Through Concatenation
// https://leetcode.com/problems/check-array-formation-through-concatenation/

import java.util.*;

class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        Map<Integer, int[]> byFirst = new HashMap<>();
        for (int[] p : pieces) byFirst.put(p[0], p);
        int i = 0;
        while (i < arr.length) {
            if (!byFirst.containsKey(arr[i])) return false;
            int[] p = byFirst.get(arr[i]);
            for (int x : p) {
                if (i >= arr.length || arr[i++] != x) return false;
            }
        }
        return true;
    }
}
