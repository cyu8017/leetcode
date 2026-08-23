// LeetCode 2341 - Maximum Number of Pairs in Array
// https://leetcode.com/problems/maximum-number-of-pairs-in-array/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] numberOfPairs(int[] nums) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int x : nums) cnt.put(x, cnt.getOrDefault(x, 0) + 1);
        int pairs = 0, left = 0;
        for (int c : cnt.values()) {
            pairs += c / 2;
            left += c % 2;
        }
        return new int[] {pairs, left};
    }
}
