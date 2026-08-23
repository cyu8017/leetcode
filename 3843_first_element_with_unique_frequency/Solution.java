// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int firstUniqueFreq(int[] nums) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int x : nums) cnt.put(x, cnt.getOrDefault(x, 0) + 1);
        Map<Integer, Integer> freq = new HashMap<>();
        for (int v : cnt.values()) freq.put(v, freq.getOrDefault(v, 0) + 1);
        for (int x : nums) {
            if (freq.get(cnt.get(x)) == 1) return x;
        }
        return -1;
    }
}
