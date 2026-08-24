// LeetCode 3199 - Count Triplets with Even XOR Set Bits I
// https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/

class Solution {
    fun tripletCount(a: IntArray, b: IntArray, c: IntArray): Int {
        val cnt1 = IntArray(2)
        val cnt2 = IntArray(2)
        val cnt3 = IntArray(2)
        for (x in a) cnt1[x.countOneBits() % 2]++
        for (x in b) cnt2[x.countOneBits() % 2]++
        for (x in c) cnt3[x.countOneBits() % 2]++
        var ans = 0
        for (i in 0 until 2) {
            for (j in 0 until 2) {
                for (k in 0 until 2) {
                    if ((i + j + k) % 2 == 0) ans += cnt1[i] * cnt2[j] * cnt3[k]
                }
            }
        }
        return ans
    }
}
