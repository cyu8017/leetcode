// LeetCode 1042 - Flower Planting With No Adjacent
// https://leetcode.com/problems/flower-planting-with-no-adjacent/

class Solution {
    fun gardenNoAdj(n: Int, paths: Array<IntArray>): IntArray {
        val graph = Array(n + 1) { mutableListOf<Int>() }
        for (p in paths) {
            graph[p[0]].add(p[1])
            graph[p[1]].add(p[0])
        }
        val ans = IntArray(n + 1)
        for (garden in 1..n) {
            val used = BooleanArray(5)
            for (nei in graph[garden]) used[ans[nei]] = true
            for (c in 1..4) {
                if (!used[c]) {
                    ans[garden] = c
                    break
                }
            }
        }
        return ans.copyOfRange(1, n + 1)
    }
}
