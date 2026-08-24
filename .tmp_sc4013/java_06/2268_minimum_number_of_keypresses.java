// LeetCode 2268 - Minimum Number of Keypresses
// https://leetcode.com/problems/minimum-number-of-keypresses/

import java.util.Arrays;

class Solution {
    public int minimumKeypresses(String s) {
        Integer[] freq = new Integer[26];
        Arrays.fill(freq, 0);
        for (char c : s.toCharArray()) freq[c - 'a']++;
        Arrays.sort(freq, (a, b) -> Integer.compare(b, a));
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] == 0) break;
            ans += freq[i] * (i / 9 + 1);
        }
        return ans;
    }
}
