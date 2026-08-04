// LeetCode 1554 - Strings Differ by One Character
// https://leetcode.com/problems/strings-differ-by-one-character/

class Solution {
    fun differByOne(dict: Array<String>): Boolean {
        val seen = HashSet<String>()
        for (word in dict) {
            val b = word.toCharArray()
            for (i in b.indices) {
                val orig = b[i]
                b[i] = '*'
                val pattern = String(b)
                if (pattern in seen) return true
                seen.add(pattern)
                b[i] = orig
            }
        }
        return false
    }
}
