// LeetCode 3187 - Peaks in Array
// https://leetcode.com/problems/peaks-in-array/

class Solution {
    private class BIT(private val n: Int) {
        private val c = IntArray(n + 1)

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

    fun countOfPeaks(nums: IntArray, queries: Array<IntArray>): IntArray {
        val n = nums.size
        val tree = BIT(n - 1)
        for (i in 1 until n - 1) {
            updatePeak(nums, tree, n, i, 1)
        }
        val ans = ArrayList<Int>()
        for (q in queries) {
            if (q[0] == 1) {
                val l = q[1] + 1
                val r = q[2] - 1
                var t = 0
                if (l <= r) {
                    t = tree.query(r) - tree.query(l - 1)
                }
                ans.add(t)
            } else {
                val idx = q[1]
                val `val` = q[2]
                for (i in idx - 1..idx + 1) {
                    updatePeak(nums, tree, n, i, -1)
                }
                nums[idx] = `val`
                for (i in idx - 1..idx + 1) {
                    updatePeak(nums, tree, n, i, 1)
                }
            }
        }
        return ans.toIntArray()
    }

    private fun updatePeak(nums: IntArray, tree: BIT, n: Int, i: Int, `val`: Int) {
        if (i <= 0 || i >= n - 1) return
        if (nums[i - 1] < nums[i] && nums[i] > nums[i + 1]) {
            tree.update(i, `val`)
        }
    }
}
