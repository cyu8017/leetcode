// LeetCode 1672 - Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/

class Solution {
    fun maximumWealth(accounts: Array<IntArray>): Int {
        return accounts.maxOf { it.sum() }
    }
}
