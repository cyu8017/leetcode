// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

public class Solution {
    public long NumberOfSubstrings(string s, int k) {
        int n = s.Length;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int[] freq = new int[26];
            for (int j = i; j < n; j++) {
                freq[s[j] - 'a']++;
                bool ok = false;
                foreach (int f in freq) if (f >= k) { ok = true; break; }
                if (ok) { ans += n - j; break; }
            }
        }
        return ans;
    }
}
