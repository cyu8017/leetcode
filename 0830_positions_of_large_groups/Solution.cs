// LeetCode 0830 - Positions of Large Groups
// https://leetcode.com/problems/positions-of-large-groups/

using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> LargeGroupPositions(string s) {
        var ans = new List<IList<int>>();
        int n = s.Length, i = 0;
        while (i < n) {
            int j = i;
            while (j < n && s[j] == s[i]) j++;
            if (j - i >= 3) ans.Add(new List<int> { i, j - 1 });
            i = j;
        }
        return ans;
    }
}
