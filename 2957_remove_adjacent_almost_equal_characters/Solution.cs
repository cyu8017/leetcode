// LeetCode 2957 - Remove Adjacent Almost-Equal Characters
// https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

using System;

public class Solution {
    public int RemoveAlmostEqualCharacters(string word) {
        int ans = 0, n = word.Length, i = 1;
        while (i < n) {
            if (Math.Abs(word[i] - word[i - 1]) <= 1) {
                ans++;
                i += 2;
            } else i++;
        }
        return ans;
    }
}
