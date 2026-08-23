// LeetCode 2575 - Find the Divisibility Array of a String
// https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

public class Solution {
    public int[] DivisibilityArray(string word, int m) {
        int[] ans = new int[word.Length];
        long cur = 0;
        for (int i = 0; i < word.Length; ++i) {
            cur = (cur * 10 + (word[i] - '0')) % m;
            if (cur == 0) ans[i] = 1;
        }
        return ans;
    }
}
