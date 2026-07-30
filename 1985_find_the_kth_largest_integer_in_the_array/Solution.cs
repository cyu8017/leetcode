// LeetCode 1985 - Find the Kth Largest Integer in the Array
// https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

using System;
using System.Linq;

public class Solution {
    public string KthLargestNumber(string[] nums, int k) {
        return nums.OrderByDescending(x => x.Length).ThenByDescending(x => x).ElementAt(k - 1);
    }
}