// LeetCode 2048 - Next Greater Numerically Balanced Number
// https://leetcode.com/problems/next-greater-numerically-balanced-number/

class Solution {
    public int nextBeautifulNumber(int n) {
        for (int x = n + 1; ; x++) if (balanced(x)) return x;
    }

    private boolean balanced(int x) {
        int[] cnt = new int[10];
        while (x > 0) { cnt[x % 10]++; x /= 10; }
        for (int d = 0; d < 10; d++) if (cnt[d] != 0 && cnt[d] != d) return false;
        return true;
    }
}
