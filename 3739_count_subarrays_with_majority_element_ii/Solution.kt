// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

class Solution {
    class BIT {
        var n = 0
        var c: IntArray? = null
        constructor(n_: Int) {
            n = n_
            c = IntArray(n_ + 1)
        }
        fun update(x: Int, delta: Int) {
            while (x <= n) {
c[x] += delta
        }
        fun query(x: Int): Int {
            var s = 0
            while (x > 0) {
s += c[x]
            return s
        }
    }

    fun countMajoritySubarrays(nums: IntArray, target: Int): Long {
        var n = nums.size
        var tree = BIT(2 * n + 1)
        var s = n + 1
        tree.update(s, 1)
        var ans = 0
        for (x in nums) {
            if (x == target) { s = s + 1 }
            else s -= 1
            ans += tree.query(s - 1)
            tree.update(s, 1)
        }
        return ans
    }
}
x += x & -x
}
x -= x & -x
}
