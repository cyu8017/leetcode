// LeetCode 0323 - Number of Connected Components in an Undirected Graph

// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/



class Solution {

    fun countComponents(n: Int, edges: Array<IntArray>): Int {

        val parent = IntArray(n) { it }

        val rank = IntArray(n)

        var components = n

        for ((left, right) in edges) {

            var rootLeft = find(parent, left)

            var rootRight = find(parent, right)

            if (rootLeft == rootRight) {

                continue

            }

            if (rank[rootLeft] < rank[rootRight]) {

                val temp = rootLeft

                rootLeft = rootRight

                rootRight = temp

            }

            parent[rootRight] = rootLeft

            if (rank[rootLeft] == rank[rootRight]) {

                rank[rootLeft]++

            }

            components--

        }

        return components

    }



    private fun find(parent: IntArray, node: Int): Int {

        if (parent[node] != node) {

            parent[node] = find(parent, parent[node])

        }

        return parent[node]

    }

}

