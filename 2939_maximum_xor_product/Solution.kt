// LeetCode 2939 - Maximum Xor Product
// https://leetcode.com/problems/maximum-xor-product/

class Solution {
    fun maximumXorProduct(a: Long, b: Long, n: Int): Int {
        val mod = 1000000007
        var aa = a
        var bb = b
        for (i in n - 1 downTo 0) {
            val bit = 1L shl i
            val abit = aa and bit
            val bbit = bb and bit
            if (abit == bbit) {
                aa = aa or bit
                bb = bb or bit
            } else if (aa > bb) {
                bb = bb or bit
                aa = aa and bit.inv()
            } else {
                aa = aa or bit
                bb = bb and bit.inv()
            }
        }
        return ((aa % mod) * (bb % mod) % mod).toInt()
    }
}
