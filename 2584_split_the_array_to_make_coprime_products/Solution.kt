// LeetCode 2584 - Split the Array to Make Coprime Products
// https://leetcode.com/problems/split-the-array-to-make-coprime-products/

class Solution {
    private val first = HashMap<Int, Int>()
    private val last = HashMap<Int, Int>()

    fun findValidSplit(nums: IntArray): Int {
        val n = nums.size
        for (i in 0 until n) factorize(nums[i], i)
        var far = 0
        for (i in 0 until n - 1) {
            var x = nums[i]
            var p = 2
            while (p * p <= x) {
                if (x % p == 0) {
                    if (last[p]!! > far) far = last[p]!!
                    while (x % p == 0) x /= p
                }
                p += 1
            }
            if (x > 1 && last[x]!! > far) far = last[x]!!
            if (far == i) return i
        }
        return -1
    }

    private fun factorize(x0: Int, idx: Int) {
        var x = x0
        var p = 2
        while (p * p <= x) {
            if (x % p == 0) {
                first.putIfAbsent(p, idx)
                last[p] = idx
                while (x % p == 0) x /= p
            }
            p += 1
        }
        if (x > 1) {
            first.putIfAbsent(x, idx)
            last[x] = idx
        }
    }
}
