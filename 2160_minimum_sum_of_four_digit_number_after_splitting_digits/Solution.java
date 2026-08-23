// LeetCode 2160 - Minimum Sum of Four Digit Number After Splitting Digits
// https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

import java.util.Arrays;

class Solution {
    public int minimumSum(int num) {
        int[] d = {num / 1000, (num / 100) % 10, (num / 10) % 10, num % 10};
        Arrays.sort(d);
        return 10 * d[0] + d[2] + 10 * d[1] + d[3];
    }
}
