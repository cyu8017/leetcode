// LeetCode 0399 - Evaluate Division

// https://leetcode.com/problems/evaluate-division/



class Solution {

    fun calcEquation(

        equations: List<List<String>>,

        values: DoubleArray,

        queries: List<List<String>>,

    ): DoubleArray {

        val graph = mutableMapOf<String, MutableMap<String, Double>>()



        for (index in equations.indices) {

            val (dividend, divisor) = equations[index]

            val value = values[index]

            graph.getOrPut(dividend) { mutableMapOf() }[divisor] = value

            graph.getOrPut(divisor) { mutableMapOf() }[dividend] = 1.0 / value

        }



        return DoubleArray(queries.size) { index ->

            dfs(queries[index][0], queries[index][1], graph, mutableSetOf())

        }

    }



    private fun dfs(

        start: String,

        end: String,

        graph: Map<String, Map<String, Double>>,

        visited: MutableSet<String>,

    ): Double {

        if (start !in graph || end !in graph) {

            return -1.0

        }

        if (start == end) {

            return 1.0

        }



        visited.add(start)

        for ((neighbor, weight) in graph.getValue(start)) {

            if (neighbor in visited) {

                continue

            }

            val result = dfs(neighbor, end, graph, visited)

            if (result != -1.0) {

                return weight * result

            }

        }



        return -1.0

    }

}
