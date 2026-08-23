// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/
// JS generator stand-in returning factorial sequence.

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> factorialGenerator(int n) {
        var ans = new ArrayList<Integer>();
        int cur = 1;
        for (int i = 1; i <= n; i++) {
            cur *= i;
            ans.add(cur);
        }
        return ans;
    }
}
