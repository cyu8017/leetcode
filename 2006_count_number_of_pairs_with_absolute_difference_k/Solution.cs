// LeetCode 2006 - Count Number of Pairs With Absolute Difference K
// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

using System.Collections.Generic;

public class Solution {
    public int CountKDifference(int[] nums, int k) {
        var freq = new Dictionary<int, int>();
        int ans = 0;
        foreach (int x in nums) {
            if (freq.TryGetValue(x - k, out int a)) ans += a;
            if (freq.TryGetValue(x + k, out int b)) ans += b;
            if (!freq.ContainsKey(x)) freq[x] = 0;
            freq[x]++;
        }
        return ans;
    }
}
