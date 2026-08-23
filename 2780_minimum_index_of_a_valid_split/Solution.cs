// LeetCode 2780 - Minimum Index of a Valid Split
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

using System.Collections.Generic;

public class Solution {
    public int MinimumIndex(IList<int> nums) {
        var freq = new Dictionary<int, int>();
        int dom = 0, best = 0;
        foreach (int v in nums) {
            if (!freq.ContainsKey(v)) freq[v] = 0;
            if (++freq[v] > best) { best = freq[v]; dom = v; }
        }
        int left = 0, n = nums.Count;
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] == dom) left++;
            int right = best - left;
            if (left * 2 > i + 1 && right * 2 > n - i - 1) return i;
        }
        return -1;
    }
}
