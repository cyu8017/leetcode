// LeetCode 0967 - Numbers With Same Consecutive Differences
// https://leetcode.com/problems/numbers-with-same-consecutive-differences/

using System.Collections.Generic;

public class Solution {
    public int[] NumsSameConsecDiff(int n, int k) {
        var ans = new List<int>();
        void Dfs(int num, int length) {
            if (length == n) {
                ans.Add(num);
                return;
            }
            int last = num % 10;
            var nexts = new HashSet<int> { last + k, last - k };
            foreach (int nxt in nexts) {
                if (nxt >= 0 && nxt <= 9) Dfs(num * 10 + nxt, length + 1);
            }
        }
        for (int start = 1; start <= 9; start++) Dfs(start, 1);
        return ans.ToArray();
    }
}
