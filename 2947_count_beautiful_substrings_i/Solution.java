// LeetCode 2947 - Count Beautiful Substrings I
// https://leetcode.com/problems/count-beautiful-substrings-i/

class Solution {
    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    public int beautifulSubstrings(String s, int k) {
        int ans = 0, n = s.length();
        for (int i = 0; i < n; i++) {
            int v = 0, c = 0;
            for (int j = i; j < n; j++) {
                if (isVowel(s.charAt(j))) v++;
                else c++;
                if (v == c && (v * c) % k == 0) ans++;
            }
        }
        return ans;
    }
}
