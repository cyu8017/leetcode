// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/
// JS generator stand-in returning factorial sequence.

using System.Collections.Generic;

public class Solution {
    public IList<int> FactorialGenerator(int n) {
        var ans = new List<int>();
        int cur = 1;
        for (int i = 1; i <= n; i++) {
            cur *= i;
            ans.Add(cur);
        }
        return ans;
    }
}
