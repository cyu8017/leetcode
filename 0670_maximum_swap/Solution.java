// LeetCode 0670 - Maximum Swap
// https://leetcode.com/problems/maximum-swap/

class Solution {
    public int maximumSwap(int num) {
        char[] digits = String.valueOf(num).toCharArray();
        int[] last = new int[10];
        for (int i = 0; i < 10; ++i) {
            last[i] = -1;
        }
        for (int i = 0; i < digits.length; ++i) {
            last[digits[i] - '0'] = i;
        }
        for (int i = 0; i < digits.length; ++i) {
            for (int candidate = 9; candidate > digits[i] - '0'; --candidate) {
                if (last[candidate] > i) {
                    char tmp = digits[i];
                    digits[i] = digits[last[candidate]];
                    digits[last[candidate]] = tmp;
                    return Integer.parseInt(new String(digits));
                }
            }
        }
        return num;
    }
}
