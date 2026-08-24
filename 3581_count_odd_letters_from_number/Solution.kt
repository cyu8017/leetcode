// LeetCode 3581 - Count Odd Letters from Number
// https://leetcode.com/problems/count-odd-letters-from-number/

class Solution {
    fun countOddLetters(n0: Int): Int {
        var n = n0
        val d = HashMap<Int, String>()
        d[0] = "zero"; d[1] = "one"; d[2] = "two"; d[3] = "three"; d[4] = "four"
        d[5] = "five"; d[6] = "six"; d[7] = "seven"; d[8] = "eight"; d[9] = "nine"
        var mask = 0
        while (n > 0) {
            for (c in d[n % 10]!!) mask = mask xor (1 shl (c - 'a'))
            n /= 10
        }
        return mask.countOneBits()
    }
}
