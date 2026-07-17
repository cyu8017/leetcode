// LeetCode 1734 - Decode XORed Permutation
// https://leetcode.com/problems/decode-xored-permutation/

class Solution {
    fun decode(encoded: IntArray): IntArray {
        val n = encoded.size + 1
        var total = 0
        for (value in 1..n) {
            total = total xor value
        }
        var odd = 0
        for (i in 1 until encoded.size step 2) {
            odd = odd xor encoded[i]
        }
        val ans = IntArray(n)
        ans[0] = total xor odd
        for (i in encoded.indices) {
            ans[i + 1] = ans[i] xor encoded[i]
        }
        return ans
    }
}
