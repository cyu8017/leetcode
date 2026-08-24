// LeetCode 0555 - Split Concatenated Strings
// https://leetcode.com/problems/split-concatenated-strings/


class Solution {
    fun splitLoopedString(strs: Array<String>): String {
        val bestForms = Array(strs.size) { i ->
            val s = strs[i]
            val rev = s.reversed()
            if (s >= rev) s else rev
        }
        var answer = ""
        for (i in strs.indices) {
            val mid = StringBuilder()
            for (j in i + 1 until strs.size) mid.append(bestForms[j])
            for (j in 0 until i) mid.append(bestForms[j])
            val midStr = mid.toString()
            for (candidate in arrayOf(strs[i], strs[i].reversed())) {
                for (cut in candidate.indices) {
                    val formed = candidate.substring(cut) + midStr + candidate.substring(0, cut)
                    if (formed > answer) answer = formed
                }
            }
        }
        return answer
    }
}
