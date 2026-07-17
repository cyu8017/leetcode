// LeetCode 1748 - Sum of Unique Elements
// https://leetcode.com/problems/sum-of-unique-elements/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int sumOfUnique(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int value : nums) {
            counts.merge(value, 1, Integer::sum);
        }
        int total = 0;
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            if (entry.getValue() == 1) {
                total += entry.getKey();
            }
        }
        return total;
    }
}
