// LeetCode 3072 - Distribute Elements Into Two Arrays II
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

class Solution {
    class BIT(private val n: Int) {
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

    fun resultArray(nums: IntArray): IntArray {
        val st = nums.copyOf()
        st.sort()
        val n = st.size
        val tree1 = BIT(n + 1)
        val tree2 = BIT(n + 1)
        val arr1 = ArrayList<Int>()
        val arr2 = ArrayList<Int>()
        arr1.add(nums[0])
        arr2.add(nums[1])
        tree1.update(idx(st, nums[0]), 1)
        tree2.update(idx(st, nums[1]), 1)
        for (i in 2 until nums.size) {
            val x = nums[i]
            val id = idx(st, x)
            val a = arr1.size - tree1.query(id)
            val b = arr2.size - tree2.query(id)
            if (a > b || (a == b && arr1.size <= arr2.size)) {
                arr1.add(x)
                tree1.update(id, 1)
            } else {
                arr2.add(x)
                tree2.update(id, 1)
            }
        }
        arr1.addAll(arr2)
        return arr1.toIntArray()
    }

    private fun idx(st: IntArray, x: Int): Int {
        var lo = 0
        var hi = st.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (st[mid] < x) lo = mid + 1 else hi = mid
        }
        return lo + 1
    }
}
