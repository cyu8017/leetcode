// LeetCode 2575 - Find the Divisibility Array of a String
// https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

class Solution {
    public int[] divisibilityArray(String word, int m) {
        int[] ans = new int[word.length()];
        long cur = 0;
        for (int i = 0; i < word.length(); ++i) {
            cur = (cur * 10 + (word.charAt(i) - '0')) % m;
            if (cur == 0) ans[i] = 1;
        }
        return ans;
    }
}
