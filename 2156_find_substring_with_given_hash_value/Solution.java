// LeetCode 2156 - Find Substring With Given Hash Value
// https://leetcode.com/problems/find-substring-with-given-hash-value/

class Solution {
    public String subStrHash(String s, int power, int modulo, int k, int hashValue) {
        int n = s.length();
        long pk = 1;
        for (int i = 0; i < k - 1; i++) pk = pk * power % modulo;
        long h = 0;
        int ans = 0;
        for (int i = n - 1; i >= n - k; i--)
            h = (h * power + (s.charAt(i) - 'a' + 1)) % modulo;
        if (h == hashValue) ans = n - k;
        for (int i = n - k - 1; i >= 0; i--) {
            h = (h - (s.charAt(i + k) - 'a' + 1) * pk % modulo + modulo) % modulo;
            h = (h * power + (s.charAt(i) - 'a' + 1)) % modulo;
            if (h == hashValue) ans = i;
        }
        return s.substring(ans, ans + k);
    }
}
