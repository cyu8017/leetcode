// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

import java.util.*;

class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        freq.put(0, 1);
        int odd = 0, answer = 0;
        for (int x : nums) {
            odd += x & 1;
            answer += freq.getOrDefault(odd - k, 0);
            freq.put(odd, freq.getOrDefault(odd, 0) + 1);
        }
        return answer;
    }
}

