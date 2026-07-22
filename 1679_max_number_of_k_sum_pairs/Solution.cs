// LeetCode 1679 - Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

using System.Collections.Generic;

public class Solution {
    public int MaxOperations(int[] nums, int k) {
        var c = new Dictionary<int, int>();
        int ans = 0;
        foreach (int x in nums) {
            int need = k - x;
            if (c.TryGetValue(need, out int cnt) && cnt > 0) {
                c[need] = cnt - 1;
                ans++;
            } else {
                c[x] = c.GetValueOrDefault(x) + 1;
            }
        }
        return ans;
    }
}
