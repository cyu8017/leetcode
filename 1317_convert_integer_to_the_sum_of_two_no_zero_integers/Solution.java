// LeetCode 1317 - Convert Integer To The Sum Of Two No Zero Integers
// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution {
    public int[] getNoZeroIntegers(int n) {
        for (int first = 1; first < n; first++) {
            if (valid(first) && valid(n - first)) return new int[]{first, n - first};
        }
        return new int[]{};
    }

    private boolean valid(int value) {
        return String.valueOf(value).indexOf('0') < 0;
    }
}
