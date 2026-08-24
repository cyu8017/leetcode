// LeetCode 0936 - Stamping The Sequence
// https://leetcode.com/problems/stamping-the-sequence/

class Solution {
    fun movesToStamp(stamp: String, target: String): IntArray {
        val n = target.length
        val m = stamp.length
        val done = BooleanArray(n)
        val ans = mutableListOf<Int>()
        var changed = true
        while (changed) {
            changed = false
            for (i in n - m downTo 0) {
                var ok = true
                var any = false
                for (j in 0 until m) {
                    if (!done[i + j] && target[i + j] != stamp[j]) { ok = false; break }
                    if (!done[i + j]) any = true
                }
                if (ok && any) {
                    for (j in 0 until m) done[i + j] = true
                    ans.add(i)
                    changed = true
                    break
                }
            }
        }
        for (d in done) if (!d) return IntArray(0)
        ans.reverse()
        return ans.toIntArray()
    }
}
