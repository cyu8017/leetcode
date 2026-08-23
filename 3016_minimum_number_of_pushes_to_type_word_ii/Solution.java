// LeetCode 3016 - Minimum Number of Pushes to Type Word II
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

import java.util.Arrays;

class Solution {
    public int minimumPushes(String word) {
        int[] cnt = new int[26];
        for (int i = 0; i < word.length(); i++) cnt[word.charAt(i) - 'a']++;
        Arrays.sort(cnt);
        int ans = 0;
        for (int i = 0; i < 26; i++) ans += (i / 8 + 1) * cnt[26 - i - 1];
        return ans;
    }
}
