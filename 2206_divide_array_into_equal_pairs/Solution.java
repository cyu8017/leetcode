// LeetCode 2206 - Divide Array Into Equal Pairs
// https://leetcode.com/problems/divide-array-into-equal-pairs/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean divideArray(int[] nums) {
        var freq = new HashMap<Integer, Integer>();
        for (int x : nums) {
            int c = freq.getOrDefault(x, 0);
            freq.put(x, c + 1);
        }
        for (var c : freq.values()) if (c % 2 != 0) return false;
        return true;
    }
}
