// LeetCode 3325 - Count Substrings With K-Frequency Characters I
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

public class Solution {
    public int NumberOfSubstrings(string s, int k) {
        int n = s.Length, ans = 0;
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
