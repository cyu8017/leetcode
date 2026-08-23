// LeetCode 3039 - Apply Operations to Make String Empty
// https://leetcode.com/problems/apply-operations-to-make-string-empty/

class Solution {
    public String lastNonEmptyString(String s) {
        int[] cnt = new int[26], last = new int[26];
        int mx = 0;
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            cnt[c]++;
            last[c] = i;
            mx = Math.max(mx, cnt[c]);
        }
        var ans = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            if (cnt[c] == mx && last[c] == i) ans.append(s.charAt(i));
        }
        return ans.toString();
    }
}
