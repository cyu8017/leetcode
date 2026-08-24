// LeetCode 3777 - Minimum Deletions To Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

class Solution {
    class BIT {
        var n = 0
        var c: IntArray? = null
        constructor(n_: Int) { n = n_; c = IntArray(n_ + 1) }
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

    fun minDeletions(s: String, queries: Array<IntArray>): IntArray {
        var n = s.length
        var nums = IntArray(n)
        var bit = BIT(n)
        for (i in 1 until n) {
            if (s[i] == s[i - 1]) {
                nums[i] = 1
                bit.update(i + 1, 1)
            }
        }
        var ans = ArrayList<Int>()
        for (q in queries) {
            if (q[0] == 1) {
                var j = q[1]
                var delta = (nums[j] ^ 1) - nums[j]
                nums[j] ^= 1
                bit.update(j + 1, delta)
                if (j + 1 < n) {
                    delta = (nums[j + 1] ^ 1) - nums[j + 1]
                    nums[j + 1] ^= 1
                    bit.update(j + 2, delta)
                }
            } else {
                var l = q[1]
                var r = q[2]
                ans.add(bit.query(r + 1) - bit.query(l + 1))
            }
        }
        return ans.toIntArray()
    }
}
x += x & -x
}
x -= x & -x
}
