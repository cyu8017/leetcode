// LeetCode 1456 - Maximum Number Of Vowels In A Substring Of Given Length
// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

public class Solution {
    public int MaxVowels(string s, int k) {
        bool V(char c) => c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        int cur = 0;
        for (int i = 0; i < k; i++) if (V(s[i])) cur++;
        int ans = cur;
        for (int i = k; i < s.Length; i++) {
            if (V(s[i])) cur++;
            if (V(s[i - k])) cur--;
            ans = System.Math.Max(ans, cur);
        }
        return ans;
    }
}
