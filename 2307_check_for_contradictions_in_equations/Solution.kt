// LeetCode 2307 - Check for Contradictions in Equations
// https://leetcode.com/problems/check-for-contradictions-in-equations/

import kotlin.math.abs

class Solution {
    private val parent = HashMap<String, String>()
    private val weight = HashMap<String, Double>()

    fun checkContradictions(equations: List<List<String>>, values: DoubleArray): Boolean {
        parent.clear()
        weight.clear()
        for (i in equations.indices) {
            val a = equations[i][0]
            val b = equations[i][1]
            val ra = find(a)
            val rb = find(b)
            if (ra == rb) {
                if (abs(weight[a]!! / weight[b]!! - values[i]) > 1e-5) return true
            } else {
                parent[ra] = rb
                weight[ra] = values[i] * weight[b]!! / weight[a]!!
            }
        }
        return false
    }

    private fun find(x: String): String {
        if (x !in parent) {
            parent[x] = x
            weight[x] = 1.0
            return x
        }
        if (parent[x] != x) {
            val p = find(parent[x]!!)
            weight[x] = weight[x]!! * weight[parent[x]!!]!!
            parent[x] = p
        }
        return parent[x]!!
    }
}
