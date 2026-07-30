// LeetCode 1317 - Convert Integer To The Sum Of Two No Zero Integers
// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

public class Solution {
    public int[] GetNoZeroIntegers(int n) {
        bool Valid(int value) => !value.ToString().Contains('0');
        for (int first = 1; first < n; first++)
            if (Valid(first) && Valid(n - first))
                return new[] { first, n - first };
        return System.Array.Empty<int>();
    }
}
