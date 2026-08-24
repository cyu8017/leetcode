// LeetCode 2092 - Find All People With Secret
// https://leetcode.com/problems/find-all-people-with-secret/

class Solution {
    private lateinit var parent: IntArray

    private fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }

    private fun unite(a0: Int, b0: Int) {
        var a = find(a0)
        var b = find(b0)
        if (a != b) parent[a] = b
    }

    fun findAllPeople(n: Int, meetings: Array<IntArray>, firstPerson: Int): List<Int> {
        meetings.sortBy { it[2] }
        parent = IntArray(n) { it }
        val know = BooleanArray(n)
        know[0] = true
        know[firstPerson] = true
        unite(0, firstPerson)
        var i = 0
        while (i < meetings.size) {
            var j = i
            while (j < meetings.size && meetings[j][2] == meetings[i][2]) j++
            for (k in i until j) unite(meetings[k][0], meetings[k][1])
            val root0 = find(0)
            val reset = mutableListOf<Int>()
            for (k in i until j) {
                val a = meetings[k][0]
                val b = meetings[k][1]
                if (find(a) != root0) {
                    reset.add(a)
                    reset.add(b)
                } else {
                    know[a] = true
                    know[b] = true
                }
            }
            for (x in reset) parent[x] = x
            i = j
        }
        val ans = mutableListOf<Int>()
        for (i in 0 until n) if (find(i) == find(0) || know[i]) ans.add(i)
        return ans
    }
}
