// LeetCode 2048 - Next Greater Numerically Balanced Number
// https://leetcode.com/problems/next-greater-numerically-balanced-number/

public class Solution {
    public int NextBeautifulNumber(int n) {
        bool Balanced(int x) {
            int[] cnt = new int[10];
            while (x > 0) { cnt[x % 10]++; x /= 10; }
            for (int d = 0; d < 10; d++) if (cnt[d] != 0 && cnt[d] != d) return false;
            return true;
        }
        for (int x = n + 1; ; x++) if (Balanced(x)) return x;
    }
}
