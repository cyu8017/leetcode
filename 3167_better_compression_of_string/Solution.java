// LeetCode 3167 - Better Compression of String
// https://leetcode.com/problems/better-compression-of-string/

class Solution {
    public String betterCompression(String compressed) {
        int[] cnt = new int[26];
        int n = compressed.length();
        for (int i = 0; i < n; ) {
            char c = compressed.charAt(i);
            int j = i + 1, x = 0;
            while (j < n) {
                char d = compressed.charAt(j);
                if (d < '0' || d > '9') break;
                x = x * 10 + (d - '0');
                j++;
            }
            cnt[c - 'a'] += x;
            i = j;
        }
        StringBuilder ans = new StringBuilder();
        for (char c = 'a'; c <= 'z'; c++) {
            if (cnt[c - 'a'] > 0) {
                ans.append(c);
                ans.append(cnt[c - 'a']);
            }
        }
        return ans.toString();
    }
}
