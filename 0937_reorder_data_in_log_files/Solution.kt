// LeetCode 0937 - Reorder Data in Log Files
// https://leetcode.com/problems/reorder-data-in-log-files/

class Solution {
    fun reorderLogFiles(logs: Array<String>): Array<String> {
        val letter = mutableListOf<String>()
        val digit = mutableListOf<String>()
        for (log in logs) {
            val sp = log.indexOf(' ')
            if (log[sp + 1].isLetter()) letter.add(log)
            else digit.add(log)
        }
        letter.sortWith { a, b ->
            val spa = a.indexOf(' ')
            val spb = b.indexOf(' ')
            val cmp = a.substring(spa + 1).compareTo(b.substring(spb + 1))
            if (cmp != 0) cmp
            else a.substring(0, spa).compareTo(b.substring(0, spb))
        }
        return (letter + digit).toTypedArray()
    }
}
