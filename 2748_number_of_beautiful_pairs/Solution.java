// LeetCode 2748 - Number of Beautiful Pairs
// https://leetcode.com/problems/number-of-beautiful-pairs/

class Solution {
    public int countBeautifulPairs(int[] nums) {
        int ans = 0;
        int[] freq = new int[10];
        for (int x : nums) {
            int last = x % 10;
            for (int d = 1; d <= 9; d++)
                if (freq[d] > 0 && gcd(d, last) == 1) ans += freq[d];
            freq[firstDigit(x)]++;
        }
        return ans;
    }

    private int firstDigit(int x) {
        while (x >= 10) x /= 10;
        return x;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
