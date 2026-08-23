// LeetCode 0948 - Bag of Tokens
// https://leetcode.com/problems/bag-of-tokens/

using System;

public class Solution {
    public int BagOfTokensScore(int[] tokens, int power) {
        Array.Sort(tokens);
        int i = 0, j = tokens.Length - 1, score = 0, ans = 0;
        while (i <= j) {
            if (power >= tokens[i]) {
                power -= tokens[i++];
                score++;
                ans = Math.Max(ans, score);
            } else if (score > 0) {
                power += tokens[j--];
                score--;
            } else break;
        }
        return ans;
    }
}
