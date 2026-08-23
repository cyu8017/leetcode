// LeetCode 2870 - Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[] nums) {
        var freq = new Dictionary<int, int>();
        foreach (int v in nums) {
            if (!freq.ContainsKey(v)) freq[v] = 0;
            freq[v]++;
        }
        int ans = 0;
        foreach (var c in freq.Values) {
            if (c == 1) return -1;
            ans += (c + 2) / 3;
        }
        return ans;
    }
}
