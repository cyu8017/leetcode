// LeetCode 2262 - Total Appeal of A String
// https://leetcode.com/problems/total-appeal-of-a-string/

using System;

public class Solution {
    public long AppealSum(string s) {
        int[] last = new int[26];
        Array.Fill(last, -1);
        long ans = 0, cur = 0;
        for (int i = 0; i < s.Length; i++) {
            int c = s[i] - 'a';
            cur += i - last[c];
            last[c] = i;
            ans += cur;
        }
        return ans;
    }
}
