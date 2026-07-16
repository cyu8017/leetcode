// LeetCode 0269 - Alien Dictionary
// https://leetcode.com/problems/alien-dictionary/

class Solution {
    fun alienOrder(words: Array<String>): String {
        val graph = HashMap<Char, MutableSet<Char>>()
        val indegree = HashMap<Char, Int>()

        for (word in words) {
            for (char in word) {
                graph.putIfAbsent(char, mutableSetOf())
                indegree.putIfAbsent(char, 0)
            }
        }

        for (i in 0 until words.size - 1) {
            val first = words[i]
            val second = words[i + 1]
            if (first.length > second.length && first.startsWith(second)) {
                return ""
            }
            val limit = minOf(first.length, second.length)
            for (j in 0 until limit) {
                val left = first[j]
                val right = second[j]
                if (left != right) {
                    if (!graph[left]!!.contains(right)) {
                        graph[left]!!.add(right)
                        indegree[right] = indegree[right]!! + 1
                    }
                    break
                }
            }
        }

        val queue = ArrayDeque<Char>()
        for ((char, degree) in indegree) {
            if (degree == 0) {
                queue.add(char)
            }
        }

        val order = StringBuilder()
        while (queue.isNotEmpty()) {
            val char = queue.removeFirst()
            order.append(char)
            for (next in graph[char]!!) {
                indegree[next] = indegree[next]!! - 1
                if (indegree[next] == 0) {
                    queue.add(next)
                }
            }
        }

        return if (order.length == indegree.size) order.toString() else ""
    }
}
