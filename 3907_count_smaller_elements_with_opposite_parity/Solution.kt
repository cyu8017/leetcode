// LeetCode 3907 - Count Smaller Elements With Opposite Parity
// https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

class Solution {
    private class BIT(n_: Int) {
        val n = n_
        val c = IntArray(n_ + 1)

        fun update(x0: Int, delta: Int) {
            var x = x0
            while (x <= n) {
                c[x] += delta
                x += x and -x
            }
        }

        fun query(x0: Int): Int {
            var x = x0
            var s = 0
            while (x > 0) {
                s += c[x]
                x -= x and -x
            }
            return s
        }
    }

    fun countSmallerOppositeParity(nums: IntArray): IntArray {
        val n = nums.size
        var sorted = nums.clone()
        sorted.sort()
        var m = 0
        for (i in sorted.indices) {
            if (i == 0 || sorted[i] != sorted[i - 1]) sorted[m++] = sorted[i]
        }
        sorted = sorted.copyOf(m)
        val bits = arrayOf(BIT(m), BIT(m))
        val ans = IntArray(n)
        for (i in n - 1 downTo 0) {
            var x = sorted.binarySearch(nums[i])
            if (x < 0) x = x.inv()
            x++
            ans[i] = bits[(nums[i] and 1) xor 1].query(x - 1)
            bits[nums[i] and 1].update(x, 1)
        }
        return ans
    }
}
