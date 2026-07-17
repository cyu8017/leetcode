// LeetCode 1737 - Change Minimum Characters to Satisfy One of Three Conditions
// https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

class Solution {
    public int minCharacters(String a, String b) {
        int[] ca = new int[26];
        int[] cb = new int[26];
        for (int i = 0; i < a.length(); i++) {
            ca[a.charAt(i) - 'a']++;
        }
        for (int i = 0; i < b.length(); i++) {
            cb[b.charAt(i) - 'a']++;
        }
        int n = a.length();
        int m = b.length();
        int maxCount = 0;
        for (int i = 0; i < 26; i++) {
            maxCount = Math.max(maxCount, Math.max(ca[i], cb[i]));
        }
        int ans = n + m - maxCount;
        int preA = 0;
        int preB = 0;
        for (int code = 0; code < 25; code++) {
            preA += ca[code];
            preB += cb[code];
            ans = Math.min(ans, Math.min(n - preA + preB, m - preB + preA));
        }
        return ans;
    }
}
