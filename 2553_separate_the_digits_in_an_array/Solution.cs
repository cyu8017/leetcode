// LeetCode 2553 - Separate the Digits in an Array
// https://leetcode.com/problems/separate-the-digits-in-an-array/

using System.Collections.Generic;

public class Solution {
    public int[] SeparateDigits(int[] nums) {
        var ans = new List<int>();
        foreach (int num in nums) {
            int x = num;
            var digits = new List<int>();
            while (x > 0) {
                digits.Add(x % 10);
                x /= 10;
            }
            for (int i = digits.Count - 1; i >= 0; --i) ans.Add(digits[i]);
        }
        return ans.ToArray();
    }
}
