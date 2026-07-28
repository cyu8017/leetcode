// LeetCode 1012 - Numbers With Repeated Digits
// https://leetcode.com/problems/numbers-with-repeated-digits/

class Solution {
    public int numDupDigitsAtMostN(int n) {
        String s = Integer.toString(n);
        int m = s.length();
        int totalUnique = 0;
        for (int length = 1; length < m; length++) {
            totalUnique += 9 * P(9, length - 1);
        }
        boolean[] used = new boolean[10];
        boolean broken = false;
        for (int i = 0; i < m; i++) {
            int d = s.charAt(i) - '0';
            int start = i == 0 ? 1 : 0;
            for (int x = start; x < d; x++) {
                if (used[x]) continue;
                totalUnique += P(9 - i, m - i - 1);
            }
            if (used[d]) {
                broken = true;
                break;
            }
            used[d] = true;
        }
        if (!broken) totalUnique++;
        return n - totalUnique;
    }

    private int P(int a, int b) {
        int res = 1;
        for (int i = 0; i < b; i++) res *= a - i;
        return res;
    }
}
