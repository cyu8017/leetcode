// LeetCode 0670 - Maximum Swap
// https://leetcode.com/problems/maximum-swap/

public class Solution {
    public int MaximumSwap(int num) {
        char[] digits = num.ToString().ToCharArray();
        int[] last = new int[10];
        for (int i = 0; i < 10; ++i) last[i] = -1;
        for (int i = 0; i < digits.Length; ++i) last[digits[i] - '0'] = i;
        for (int i = 0; i < digits.Length; ++i) {
            for (int candidate = 9; candidate > digits[i] - '0'; --candidate) {
                if (last[candidate] > i) {
                    (digits[i], digits[last[candidate]]) = (digits[last[candidate]], digits[i]);
                    return int.Parse(new string(digits));
                }
            }
        }
        return num;
    }
}
