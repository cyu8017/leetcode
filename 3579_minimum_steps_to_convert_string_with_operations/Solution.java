// LeetCode 3579 - Minimum Steps to Convert String with Operations
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

class Solution {
    String word1, word2;

    int calc(int l, int r, boolean rev) {
        int[][] cnt = new int[26][26];
        int res = 0;
        for (int i = l; i <= r; i++) {
            int j = rev ? r - (i - l) : i;
            int a = word1.charAt(j) - 'a';
            int b = word2.charAt(i) - 'a';
            if (a != b) {
                if (cnt[b][a] > 0) cnt[b][a]--;
                else {
                    cnt[a][b]++;
                    res++;
                }
            }
        }
        return res;
    }

    public int minOperations(String word1, String word2) {
        this.word1 = word1;
        this.word2 = word2;
        int n = word1.length();
        int[] f = new int[n + 1];
        java.util.Arrays.fill(f, Integer.MAX_VALUE / 2);
        f[0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                int a = calc(j, i - 1, false);
                int b = 1 + calc(j, i - 1, true);
                f[i] = Math.min(f[i], f[j] + Math.min(a, b));
            }
        }
        return f[n];
    }
}
