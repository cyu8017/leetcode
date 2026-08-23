// LeetCode 2019 - The Score of Students Solving Math Expression
// https://leetcode.com/problems/the-score-of-students-solving-math-expression/

import java.util.*;

class Solution {
    private String s;
    private Set<Integer>[][] dp;

    private int evalCorrect(String s) {
        List<Integer> nums = new ArrayList<>();
        List<Character> ops = new ArrayList<>();
        for (char c : s.toCharArray()) {
            if (c >= '0' && c <= '9') nums.add(c - '0');
            else ops.add(c);
        }
        List<Integer> newNums = new ArrayList<>();
        newNums.add(nums.get(0));
        List<Character> newOps = new ArrayList<>();
        for (int j = 0; j < ops.size(); j++) {
            if (ops.get(j) == '*') newNums.set(newNums.size() - 1, newNums.get(newNums.size() - 1) * nums.get(j + 1));
            else { newOps.add(ops.get(j)); newNums.add(nums.get(j + 1)); }
        }
        int res = newNums.get(0);
        for (int j = 0; j < newOps.size(); j++) res += newNums.get(j + 1);
        return res;
    }

    public int scoreOfStudents(String s, int[] answers) {
        this.s = s;
        int n = s.length();
        int correct = evalCorrect(s);
        dp = new HashSet[n][n];
        Set<Integer> possible = dfs(0, n - 1);
        int ans = 0;
        for (int a : answers) {
            if (a == correct) ans += 5;
            else if (possible.contains(a)) ans += 2;
        }
        return ans;
    }

    private Set<Integer> dfs(int l, int r) {
        if (dp[l][r] != null) return dp[l][r];
        Set<Integer> res = new HashSet<>();
        if (l == r) { res.add(s.charAt(l) - '0'); dp[l][r] = res; return res; }
        for (int i = l + 1; i < r; i += 2) {
            for (int a : dfs(l, i - 1))
                for (int b : dfs(i + 1, r)) {
                    int v = s.charAt(i) == '+' ? a + b : a * b;
                    if (v <= 1000) res.add(v);
                }
        }
        dp[l][r] = res;
        return res;
    }
}
