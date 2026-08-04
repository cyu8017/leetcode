// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

import java.util.*;

class Solution {
    public int maxEqualFreq(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        Map<Integer, Integer> freq = new HashMap<>();
        int answer = 0;
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            int old = count.getOrDefault(x, 0);
            if (old > 0) freq.put(old, freq.get(old) - 1);
            count.put(x, old + 1);
            freq.put(old + 1, freq.getOrDefault(old + 1, 0) + 1);
            int high = Collections.max(freq.keySet());
            if (high == 1
                    || freq.get(high) * high + 1 == i + 1
                    || (freq.get(high) == 1 && (high - 1) * freq.getOrDefault(high - 1, 0) + high == i + 1)) {
                answer = i + 1;
            }
        }
        return answer;
    }
}

