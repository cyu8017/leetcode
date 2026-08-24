// LeetCode 0364 - Nested List Weight Sum II

// https://leetcode.com/problems/nested-list-weight-sum-ii/



class NestedInteger {

    private var integer: Int? = null

    private val list = mutableListOf<NestedInteger>()



    constructor()



    constructor(value: Int) {

        integer = value

    }



    fun isInteger(): Boolean = integer != null



    fun getInteger(): Int = integer ?: 0



    fun getList(): List<NestedInteger> = list

}



class Solution {

    fun depthSum(nestedList: List<NestedInteger>): Int {

        val weighted = mutableListOf<Pair<Int, Int>>()

        dfs(nestedList, 1, weighted)

        if (weighted.isEmpty()) {

            return 0

        }



        val maxDepth = weighted.maxOf { it.second }

        return weighted.sumOf { (value, depth) -> value * (maxDepth - depth + 1) }

    }



    private fun dfs(items: List<NestedInteger>, depth: Int, weighted: MutableList<Pair<Int, Int>>) {

        for (item in items) {

            if (item.isInteger()) {

                weighted.add(item.getInteger() to depth)

            } else {

                dfs(item.getList(), depth + 1, weighted)

            }

        }

    }

}
