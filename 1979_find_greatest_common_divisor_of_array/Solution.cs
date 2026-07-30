// LeetCode 1979 - Find Greatest Common Divisor of Array
// https://leetcode.com/problems/find-greatest-common-divisor-of-array/

using System;
using System.Linq;

public class Solution {
    public int FindGCD(int[] nums) {
        int a = nums.Min(), b = nums.Max();
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }
}