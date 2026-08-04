// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

class Solution {
    fun encode(num: Int): String = Integer.toBinaryString(num + 1).substring(1)
}
