// LeetCode 3646 - Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/

class Solution {
    private lateinit var cands: ArrayList<Long>
    private lateinit var halfCnt: IntArray
    private var mid = 0
    private var halfLen = 0

    private fun dfs(pos: Int, cur: ArrayList<Int>) {
        if (pos == halfLen) {
            val left = StringBuilder()
            for (x in cur) left.append(x)
            val s = StringBuilder(left)
            if (mid > 0) s.append(mid)
            for (i in left.length - 1 downTo 0) s.append(left[i])
            cands.add(s.toString().toLong())
            return
        }
        for (d in 1..9) {
            if (halfCnt[d] == 0) continue
            halfCnt[d]--
            cur.add(d)
            dfs(pos + 1, cur)
            cur.removeAt(cur.size - 1)
            halfCnt[d]++
        }
    }

    private fun gen(mask: Int) {
        var total = 0
        var odd = 0
        for (d in 1..9) {
            if (((mask shr d) and 1) != 0) {
                total += d
                if (d % 2 == 1) odd++
            }
        }
        if (total == 0 || total > 18 || odd > 1) return
        halfCnt = IntArray(10)
        mid = 0
        for (d in 1..9) {
            if (((mask shr d) and 1) == 0) continue
            halfCnt[d] = d / 2
            if (d % 2 == 1) mid = d
        }
        halfLen = total / 2
        dfs(0, ArrayList())
    }

    fun specialPalindrome(n: Long): Long {
        cands = ArrayList()
        for (mask in 1 until (1 shl 10)) {
            if ((mask and 1) != 0) continue
            gen(mask)
        }
        cands.sort()
        for (v in cands) if (v > n) return v
        return -1
    }
}
