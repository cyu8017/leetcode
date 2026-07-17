// LeetCode 1726 - Tuple with Same Product
// https://leetcode.com/problems/tuple-with-same-product/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int tupleSameProduct(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                counts.merge(nums[i] * nums[j], 1, Integer::sum);
            }
        }
        long result = 0;
        for (int count : counts.values()) {
            result += (long) count * (count - 1) * 4;
        }
        return (int) result;
    }
}
