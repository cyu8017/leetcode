// LeetCode 1720 - Decode XORed Array
// https://leetcode.com/problems/decode-xored-array/

class Solution {
    fun decode(encoded: IntArray, first: Int): IntArray {
        val ans = IntArray(encoded.size + 1)
        ans[0] = first
        for (i in encoded.indices) {
            ans[i + 1] = ans[i] xor encoded[i]
        }
        return ans
    }
}
