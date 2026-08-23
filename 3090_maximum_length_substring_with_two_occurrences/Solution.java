// LeetCode 3090 - Maximum Length Substring With Two Occurrences
// https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

class Solution {
    public int maximumLengthSubstring(String s) {
        int l = 0, ans = 0;
        int[] cnt = new int[26];
        for (int r = 0; r < s.length(); r++) {
            int idx = s.charAt(r) - 'a';
            cnt[idx]++;
            while (cnt[idx] > 2) {
                cnt[s.charAt(l) - 'a']--;
                l++;
            }
            ans = Math.max(ans, r - l + 1);
        }
        return ans;
    }
}
