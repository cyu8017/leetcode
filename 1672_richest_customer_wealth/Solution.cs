// LeetCode 1672 - Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/

using System;
using System.Linq;

public class Solution {
    public int MaximumWealth(int[][] accounts) {
        return accounts.Max(row => row.Sum());
    }
}
