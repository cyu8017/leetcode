// LeetCode 2019 - The Score of Students Solving Math Expression
// https://leetcode.com/problems/the-score-of-students-solving-math-expression/

using System.Collections.Generic;

public class Solution {
    private int EvalCorrect(string s) {
        var nums = new List<int>();
        var ops = new List<char>();
        foreach (char c in s) {
            if (c >= '0' && c <= '9') nums.Add(c - '0');
            else ops.Add(c);
        }
        var newNums = new List<int> { nums[0] };
        var newOps = new List<char>();
        for (int j = 0; j < ops.Count; j++) {
            if (ops[j] == '*') newNums[newNums.Count - 1] *= nums[j + 1];
            else { newOps.Add(ops[j]); newNums.Add(nums[j + 1]); }
        }
        int res = newNums[0];
        for (int j = 0; j < newOps.Count; j++) res += newNums[j + 1];
        return res;
    }

    public int ScoreOfStudents(string s, int[] answers) {
        int n = s.Length;
        int correct = EvalCorrect(s);
        var dp = new HashSet<int>[n, n];
        HashSet<int> Dfs(int l, int r) {
            if (dp[l, r] != null) return dp[l, r];
            var res = new HashSet<int>();
            if (l == r) { res.Add(s[l] - '0'); dp[l, r] = res; return res; }
            for (int i = l + 1; i < r; i += 2) {
                var left = Dfs(l, i - 1);
                var right = Dfs(i + 1, r);
                foreach (int a in left) foreach (int b in right) {
                    int v = s[i] == '+' ? a + b : a * b;
                    if (v <= 1000) res.Add(v);
                }
            }
            dp[l, r] = res;
            return res;
        }
        var possible = Dfs(0, n - 1);
        int ans = 0;
        foreach (int a in answers) {
            if (a == correct) ans += 5;
            else if (possible.Contains(a)) ans += 2;
        }
        return ans;
    }
}
