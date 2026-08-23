// LeetCode 3325 - Count Substrings With K-Frequency Characters I
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

class Solution {
    public int numberOfSubstrings(String s, int k) {
        int n = s.length(), ans = 0;
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
