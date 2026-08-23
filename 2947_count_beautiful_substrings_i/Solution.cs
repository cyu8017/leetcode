// LeetCode 2947 - Count Beautiful Substrings I
// https://leetcode.com/problems/count-beautiful-substrings-i/

public class Solution {
    public int BeautifulSubstrings(string s, int k) {
        bool IsVowel(char c) => c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        int ans = 0, n = s.Length;
        for (int i = 0; i < n; i++) {
            int v = 0, c = 0;
            for (int j = i; j < n; j++) {
                if (IsVowel(s[j])) v++;
                else c++;
                if (v == c && (v * c) % k == 0) ans++;
            }
        }
        return ans;
    }
}
