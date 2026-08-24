// LeetCode 2306 - Naming a Company
// https://leetcode.com/problems/naming-a-company/

class Solution {
    fun distinctNames(ideas: Array<String>): Long {
        val groups = Array(26) { HashSet<String>() }
        for (idea in ideas) {
            groups[idea[0] - 'a'].add(idea.substring(1))
        }
        var ans = 0L
        for (i in 0 until 26) {
            for (j in i + 1 until 26) {
                var overlap = 0
                for (s in groups[i]) if (s in groups[j]) overlap++
                ans += (groups[i].size - overlap).toLong() * (groups[j].size - overlap) * 2
            }
        }
        return ans
    }
}
