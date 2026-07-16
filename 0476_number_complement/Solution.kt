// LeetCode 0476 - Number Complement
// https://leetcode.com/problems/number-complement/

class Solution {
    fun findComplement(num: Int): Int {
        var mask = num
        mask = mask or (mask ushr 1)
        mask = mask or (mask ushr 2)
        mask = mask or (mask ushr 4)
        mask = mask or (mask ushr 8)
        mask = mask or (mask ushr 16)
        return num xor mask
    }
}
