// LeetCode 0339 - Nested List Weight Sum

// https://leetcode.com/problems/nested-list-weight-sum/



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

    fun depthSum(nestedList: List<NestedInteger>): Int = dfs(nestedList, 1)



    private fun dfs(items: List<NestedInteger>, depth: Int): Int {

        var total = 0

        for (item in items) {

            if (item.isInteger()) {

                total += item.getInteger() * depth

            } else {

                total += dfs(item.getList(), depth + 1)

            }

        }

        return total

    }

}
