// LeetCode 0421 - Maximum XOR of Two Numbers in an Array
// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int findMaximumXOR(int[] nums) {
        int maximum = nums[0];
        for (int num : nums) {
            maximum = Math.max(maximum, num);
        }
        int maxBit = 32 - Integer.numberOfLeadingZeros(maximum);
        if (maxBit == 0) {
            maxBit = 1;
        }

        Map<Integer, Object> root = new HashMap<>();
        for (int number : nums) {
            Map<Integer, Object> node = root;
            for (int bit = maxBit - 1; bit >= 0; bit--) {
                int current = (number >> bit) & 1;
                @SuppressWarnings("unchecked")
                Map<Integer, Object> next = (Map<Integer, Object>) node.get(current);
                if (next == null) {
                    next = new HashMap<>();
                    node.put(current, next);
                }
                node = next;
            }
        }

        int best = 0;
        for (int number : nums) {
            Map<Integer, Object> node = root;
            int candidate = 0;
            for (int bit = maxBit - 1; bit >= 0; bit--) {
                int current = (number >> bit) & 1;
                int target = 1 - current;
                @SuppressWarnings("unchecked")
                Map<Integer, Object> next = (Map<Integer, Object>) node.get(target);
                if (next != null) {
                    candidate |= 1 << bit;
                    node = next;
                } else {
                    @SuppressWarnings("unchecked")
                    Map<Integer, Object> fallback = (Map<Integer, Object>) node.get(current);
                    node = fallback;
                }
            }
            best = Math.max(best, candidate);
        }

        return best;
    }
}
