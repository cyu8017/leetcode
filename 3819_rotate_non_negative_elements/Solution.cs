// LeetCode 3819 - Rotate Non Negative Elements
// https://leetcode.com/problems/rotate-non-negative-elements/

using System.Collections.Generic;

public class Solution {
    public int[] RotateElements(int[] nums, int k) {
        var t = new List<int>();
        foreach (int x in nums) if (x >= 0) t.Add(x);
        int m = t.Count;
        if (m == 0) return nums;
        int[] d = new int[m];
        for (int i = 0; i < m; i++) d[((i - k) % m + m) % m] = t[i];
        int j = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] >= 0) nums[i] = d[j++];
        }
        return nums;
    }
}
