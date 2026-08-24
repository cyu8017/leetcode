// LeetCode 3226 - Number of Bit Changes to Make Two Integers Equal
// https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/

class Solution {
    fun minChanges(n: Int, k: Int): Int {
        if ((n & k) != k) return -1
        return (n ^ k).countOneBits()
    }
}
