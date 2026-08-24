// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

class Solution {
    fun mostVisitedPattern(username: Array<String>, timestamp: IntArray, website: Array<String>): List<String> {
        val visits = mutableMapOf<String, MutableList<Pair<Int, String>>>()
        for (i in username.indices) {
            visits.getOrPut(username[i]) { mutableListOf() }.add(timestamp[i] to website[i])
        }
        val scores = mutableMapOf<List<String>, Int>()
        for ((_, list) in visits) {
            val sites = list.sortedBy { it.first }.map { it.second }
            val patterns = mutableSetOf<List<String>>()
            for (i in sites.indices) {
                for (j in i + 1 until sites.size) {
                    for (k in j + 1 until sites.size) {
                        patterns.add(listOf(sites[i], sites[j], sites[k]))
                    }
                }
            }
            for (pattern in patterns) {
                scores[pattern] = scores.getOrDefault(pattern, 0) + 1
            }
        }
        return scores.minWith(compareBy<Map.Entry<List<String>, Int>> { -it.value }.thenBy { it.key.joinToString("\u0000") }).key
    }
}
