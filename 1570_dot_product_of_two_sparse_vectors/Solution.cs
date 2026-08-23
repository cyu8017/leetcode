// LeetCode 1570 - Dot Product of Two Sparse Vectors
// https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

using System.Collections.Generic;

public class SparseVector {
    private readonly Dictionary<int, int> values = new Dictionary<int, int>();

    public SparseVector(int[] nums) {
        for (int i = 0; i < nums.Length; i++)
            if (nums[i] != 0) values[i] = nums[i];
    }

    public int DotProduct(SparseVector vec) {
        if (values.Count > vec.values.Count) return vec.DotProduct(this);
        int sum = 0;
        foreach (var kv in values) {
            if (vec.values.TryGetValue(kv.Key, out int other)) sum += kv.Value * other;
        }
        return sum;
    }
}

public class Solution {
    public int DotProduct(int[] nums1, int[] nums2) {
        return new SparseVector(nums1).DotProduct(new SparseVector(nums2));
    }
}
