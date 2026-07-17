// LeetCode 1737 - Change Minimum Characters to Satisfy One of Three Conditions
// https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

public class Solution {
    public int MinCharacters(string a, string b) {
        var ca = new int[26];
        var cb = new int[26];
        foreach (char ch in a) {
            ca[ch - 'a']++;
        }
        foreach (char ch in b) {
            cb[ch - 'a']++;
        }
        int n = a.Length;
        int m = b.Length;
        int maxCount = 0;
        for (int i = 0; i < 26; i++) {
            maxCount = Math.Max(maxCount, Math.Max(ca[i], cb[i]));
        }
        int ans = n + m - maxCount;
        int preA = 0;
        int preB = 0;
        for (int code = 0; code < 25; code++) {
            preA += ca[code];
            preB += cb[code];
            ans = Math.Min(ans, Math.Min(n - preA + preB, m - preB + preA));
        }
        return ans;
    }
}
