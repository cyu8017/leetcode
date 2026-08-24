// LeetCode 3901 - Good Subsequence Queries
// https://leetcode.com/problems/good-subsequence-queries/

class Solution {
    private class Node {
        var l = 0
        var r = 0
        var g = 0
    }

    private class SegmentTree(n: Int) {
        val tr = Array(n shl 2) { Node() }

        init {
            build(1, 1, n)
        }

        private fun build(u: Int, l: Int, r: Int) {
            tr[u].l = l
            tr[u].r = r
            tr[u].g = 0
            if (l == r) return
            val mid = (l + r) shr 1
            build(u shl 1, l, mid)
            build(u shl 1 or 1, mid + 1, r)
        }

        private fun pushup(u: Int) {
            tr[u].g = gcd(tr[u shl 1].g, tr[u shl 1 or 1].g)
        }

        fun modify(u: Int, x: Int, v: Int) {
            if (tr[u].l == tr[u].r) {
                tr[u].g = v
                return
            }
            val mid = (tr[u].l + tr[u].r) shr 1
            if (x <= mid) modify(u shl 1, x, v)
            else modify(u shl 1 or 1, x, v)
            pushup(u)
        }

        fun query(u: Int, l: Int, r: Int): Int {
            if (l > r) return 0
            if (tr[u].l >= l && tr[u].r <= r) return tr[u].g
            val mid = (tr[u].l + tr[u].r) shr 1
            if (r <= mid) return query(u shl 1, l, r)
            if (l > mid) return query(u shl 1 or 1, l, r)
            return gcd(query(u shl 1, l, mid), query(u shl 1 or 1, mid + 1, r))
        }

        companion object {
            fun gcd(a0: Int, b0: Int): Int {
                var a = a0
                var b = b0
                while (b != 0) {
                    val t = a % b
                    a = b
                    b = t
                }
                return a
            }
        }
    }

    fun countGoodSubseq(nums: IntArray, p: Int, queries: Array<IntArray>): Int {
        val n = nums.size
        val tree = SegmentTree(n)
        var cnt = 0
        for (i in 0 until n) {
            if (nums[i] % p == 0) {
                tree.modify(1, i + 1, nums[i])
                cnt++
            }
        }
        var ans = 0
        for (q in queries) {
            val idx = q[0]
            val `val` = q[1]
            if (nums[idx] % p == 0) {
                tree.modify(1, idx + 1, 0)
                cnt--
            }
            if (`val` % p == 0) {
                tree.modify(1, idx + 1, `val`)
                cnt++
            }
            nums[idx] = `val`
            if (tree.tr[1].g != p) continue
            if (cnt < n || n > 6) {
                ans++
                continue
            }
            for (i in 1..n) {
                val leftG = tree.query(1, 1, i - 1)
                val rightG = tree.query(1, i + 1, n)
                var g = leftG
                var b = rightG
                while (b != 0) {
                    val t = g % b
                    g = b
                    b = t
                }
                if (g == p) {
                    ans++
                    break
                }
            }
        }
        return ans
    }
}
