// LeetCode 2287 - Rearrange Characters to Make Target String
// https://leetcode.com/problems/rearrange-characters-to-make-target-string/

class Solution {
    public int rearrangeCharacters(String s, String target) {
        int[] sc = new int[26], tc = new int[26];
        for (char c : s.toCharArray()) sc[c - 'a']++;
        for (char c : target.toCharArray()) tc[c - 'a']++;
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < 26; i++) {
            if (tc[i] == 0) continue;
            ans = Math.min(ans, sc[i] / tc[i]);
        }
        return ans;
    }
}
