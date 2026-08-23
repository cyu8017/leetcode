// LeetCode 1577 - Number of Ways Where Square of Number Is Equal to Product of Two Numbers
// https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

import java.util.*;

class Solution {
    public int numTriplets(int[] nums1, int[] nums2) {
        return count(nums1, nums2) + count(nums2, nums1);
    }

    private int count(int[] a, int[] b) {
        Map<Long, Integer> squares = new HashMap<>();
        for (int x : a) {
            long sq = 1L * x * x;
            squares.put(sq, squares.getOrDefault(sq, 0) + 1);
        }
        Map<Long, Integer> products = new HashMap<>();
        for (int i = 0; i < b.length; i++) {
            for (int j = i + 1; j < b.length; j++) {
                long prod = 1L * b[i] * b[j];
                products.put(prod, products.getOrDefault(prod, 0) + 1);
            }
        }
        int total = 0;
        for (Map.Entry<Long, Integer> entry : squares.entrySet()) {
            total += entry.getValue() * products.getOrDefault(entry.getKey(), 0);
        }
        return total;
    }
}
