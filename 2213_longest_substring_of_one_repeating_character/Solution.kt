// LeetCode 2213 - Longest Substring of One Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/

class Solution {
    private class Seg {
        var lChar = '\u0000'
        var rChar = '\u0000'
        var lLen = 0
        var rLen = 0
        var best = 0
        var size = 0
    }

    private fun merge(a: Seg, b: Seg): Seg {
        if (a.size == 0) return b
        if (b.size == 0) return a
        val res = Seg()
        res.lChar = a.lChar
        res.rChar = b.rChar
        res.size = a.size + b.size
        res.best = maxOf(a.best, b.best)
        res.lLen = a.lLen
        res.rLen = b.rLen
        if (a.rChar == b.lChar) {
            val mid = a.rLen + b.lLen
            res.best = maxOf(res.best, mid)
            if (a.lLen == a.size) res.lLen = a.size + b.lLen
            if (b.rLen == b.size) res.rLen = b.size + a.rLen
        }
        return res
    }

    private lateinit var tree: Array<Seg?>
    private lateinit var s: CharArray
    private var n = 0

    private fun build(idx: Int, l: Int, r: Int) {
        if (l == r) {
            tree[idx] = Seg()
            tree[idx]!!.lChar = s[l]
            tree[idx]!!.rChar = s[l]
            tree[idx]!!.lLen = 1
            tree[idx]!!.rLen = 1
            tree[idx]!!.best = 1
            tree[idx]!!.size = 1
            return
        }
        val mid = (l + r) / 2
        build(idx * 2, l, mid)
        build(idx * 2 + 1, mid + 1, r)
        tree[idx] = merge(tree[idx * 2]!!, tree[idx * 2 + 1]!!)
    }

    private fun update(idx: Int, l: Int, r: Int, pos: Int, ch: Char) {
        if (l == r) {
            s[pos] = ch
            tree[idx] = Seg()
            tree[idx]!!.lChar = ch
            tree[idx]!!.rChar = ch
            tree[idx]!!.lLen = 1
            tree[idx]!!.rLen = 1
            tree[idx]!!.best = 1
            tree[idx]!!.size = 1
            return
        }
        val mid = (l + r) / 2
        if (pos <= mid) update(idx * 2, l, mid, pos, ch)
        else update(idx * 2 + 1, mid + 1, r, pos, ch)
        tree[idx] = merge(tree[idx * 2]!!, tree[idx * 2 + 1]!!)
    }

    fun longestRepeating(s_: String, queryCharacters: String, queryIndices: IntArray): IntArray {
        s = s_.toCharArray()
        n = s.size
        tree = arrayOfNulls(4 * n + 5)
        build(1, 0, n - 1)
        val ans = IntArray(queryIndices.size)
        for (i in queryIndices.indices) {
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i])
            ans[i] = tree[1]!!.best
        }
        return ans
    }
}
