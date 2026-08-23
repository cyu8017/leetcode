// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

using System;

public class Solution {
    public bool IsArmstrong(int n) {
        string digits = n.ToString();
        int power = digits.Length;
        int sum = 0;
        foreach (char d in digits) {
            sum += (int)Math.Pow(d - '0', power);
        }
        return sum == n;
    }
}
