// LeetCode 1570 - Dot Product of Two Sparse Vectors
// https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

import java.util.*;

class SparseVector {
    private final Map<Integer, Integer> values;

    SparseVector(int[] nums) {
        values = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                values.put(i, nums[i]);
            }
        }
    }

    public int dotProduct(SparseVector vec) {
        if (values.size() > vec.values.size()) {
            return vec.dotProduct(this);
        }
        int sum = 0;
        for (Map.Entry<Integer, Integer> entry : values.entrySet()) {
            sum += entry.getValue() * vec.values.getOrDefault(entry.getKey(), 0);
        }
        return sum;
    }
}

class Solution {
    public int dotProduct(int[] nums1, int[] nums2) {
        return new SparseVector(nums1).dotProduct(new SparseVector(nums2));
    }
}
