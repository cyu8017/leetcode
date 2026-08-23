// LeetCode 2748 - Number of Beautiful Pairs
// https://leetcode.com/problems/number-of-beautiful-pairs/

using System;

public class Solution {
    public int CountBeautifulPairs(int[] nums) {
        int ans = 0;
        int[] freq = new int[10];
        int FirstDigit(int x) { while (x >= 10) x /= 10; return x; }
        int Gcd(int a, int b) { while (b != 0) { int t = a % b; a = b; b = t; } return a; }
        foreach (int x in nums) {
            int last = x % 10;
            for (int d = 1; d <= 9; d++)
                if (freq[d] > 0 && Gcd(d, last) == 1) ans += freq[d];
            freq[FirstDigit(x)]++;
        }
        return ans;
    }
}
