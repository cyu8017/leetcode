// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

class Solution {
    public long numberOfSubstrings(String s, int k) {
        int n = s.length();
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int[] freq = new int[26];
            for (int j = i; j < n; j++) {
                freq[s.charAt(j) - 'a']++;
                boolean ok = false;
                for (int f : freq) if (f >= k) { ok = true; break; }
                if (ok) { ans += n - j; break; }
            }
        }
        return ans;
    }
}
