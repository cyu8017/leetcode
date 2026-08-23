// LeetCode 3035 - Maximum Palindromes After Operations
// https://leetcode.com/problems/maximum-palindromes-after-operations/

import java.util.Arrays;

class Solution {
    private static int popcount(int x) {
        int c = 0;
        while (x != 0) { c += x & 1; x >>= 1; }
        return c;
    }

    public int maxPalindromesAfterOperations(String[] words) {
        int s = 0, mask = 0;
        for (String w : words) {
            s += w.length();
            for (int i = 0; i < w.length(); i++) mask ^= 1 << (w.charAt(i) - 'a');
        }
        s -= popcount(mask);
        Arrays.sort(words, (a, b) -> Integer.compare(a.length(), b.length()));
        int ans = 0;
        for (String w : words) {
            s -= w.length() / 2 * 2;
            if (s < 0) break;
            ans++;
        }
        return ans;
    }
}
