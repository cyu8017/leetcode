// LeetCode 2452 - Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

class Solution {
    fun twoEditWords(queries: Array<String>, dictionary: Array<String>): List<String> {
        val ans = ArrayList<String>()
        for (q in queries) {
            var ok = false
            for (d in dictionary) {
                var diff = 0
                for (i in q.indices) {
                    if (q[i] != d[i]) {
                        diff++
                        if (diff > 2) break
                    }
                }
                if (diff <= 2) {
                    ok = true
                    break
                }
            }
            if (ok) ans.add(q)
        }
        return ans
    }
}
