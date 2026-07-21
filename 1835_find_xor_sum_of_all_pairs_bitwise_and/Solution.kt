// LeetCode 1835 - Find XOR Sum of All Pairs Bitwise AND
// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

class Solution {
    fun getXORSum(arr1: IntArray, arr2: IntArray): Int {
        var xor1 = 0
        for (x in arr1) xor1 = xor1 xor x
        var xor2 = 0
        for (x in arr2) xor2 = xor2 xor x
        return xor1 and xor2
    }
}
