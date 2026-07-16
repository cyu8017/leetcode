// LeetCode 0532 - K-diff Pairs in an Array
// https://leetcode.com/problems/k-diff-pairs-in-an-array/

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int findPairs(int[] nums, int k) {
        if (k < 0) {
            return 0;
        }

        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        int pairs = 0;
        for (int num : freq.keySet()) {
            if (k == 0) {
                if (freq.get(num) > 1) {
                    pairs++;
                }
            } else if (freq.containsKey(num + k)) {
                pairs++;
            }
        }
        return pairs;
    }
}
