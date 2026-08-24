// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

class Solution {
    fun maxSubstringLength(s: String, k: Int): Boolean {
        val n = s.length
        val first = IntArray(26) { n }
        val last = IntArray(26) { -1 }
        for (i in 0 until n) {
            val ci = s[i] - 'a'
            if (first[ci] == n) first[ci] = i
            last[ci] = i
        }
        val segs = ArrayList<IntArray>()
        for (c in 0 until 26) {
            if (last[c] == -1) continue
            var l = first[c]
            var r = last[c]
            var i = l
            while (i <= r) {
                val ci = s[i] - 'a'
                if (first[ci] < l) {
                    l = first[ci]
                    i = l
                    continue
                }
                if (last[ci] > r) r = last[ci]
                i++
            }
            if (!(l == 0 && r == n - 1)) segs.add(intArrayOf(l, r))
        }
        val uniq = HashSet<Long>()
        val arr = ArrayList<IntArray>()
        for (sg in segs) {
            val key = (sg[0].toLong() shl 32) or (sg[1].toLong() and 0xffffffffL)
            if (uniq.add(key)) arr.add(sg)
        }
        arr.sortBy { it[1] }
        var cnt = 0
        var end = -1
        for (sg in arr) {
            if (sg[0] > end) {
                cnt++
                end = sg[1]
            }
        }
        return cnt >= k
    }
}
