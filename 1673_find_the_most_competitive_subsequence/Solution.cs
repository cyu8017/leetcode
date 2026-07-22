// LeetCode 1673 - Find the Most Competitive Subsequence
// https://leetcode.com/problems/find-the-most-competitive-subsequence/

using System.Collections.Generic;

public class Solution {
    public int[] MostCompetitive(int[] nums, int k) {
        var st = new List<int>();
        for (int i = 0; i < nums.Length; i++) {
            int x = nums[i];
            while (st.Count > 0 && st[^1] > x && st.Count - 1 + nums.Length - i >= k)
                st.RemoveAt(st.Count - 1);
            if (st.Count < k) st.Add(x);
        }
        return st.ToArray();
    }
}
