// LeetCode 2115 - Find All Possible Recipes from Given Supplies
// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

import java.util.ArrayDeque

class Solution {
    fun findAllRecipes(recipes: Array<String>, ingredients: List<List<String>>, supplies: Array<String>): List<String> {
        val have = HashSet(supplies.asList())
        val indeg = HashMap<String, Int>()
        val graph = HashMap<String, MutableList<String>>()
        for (i in recipes.indices) {
            indeg[recipes[i]] = ingredients[i].size
            for (ing in ingredients[i]) {
                graph.getOrPut(ing) { mutableListOf() }.add(recipes[i])
            }
        }
        val q = ArrayDeque(have)
        val ans = mutableListOf<String>()
        while (q.isNotEmpty()) {
            val cur = q.poll()
            val nbrs = graph[cur] ?: continue
            for (nxt in nbrs) {
                val left = indeg.merge(nxt, -1) { a, b -> a + b }!!
                if (left == 0) {
                    ans.add(nxt)
                    q.offer(nxt)
                }
            }
        }
        return ans
    }
}
