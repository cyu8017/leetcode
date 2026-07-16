// LeetCode 0386 - Lexicographical Numbers

// https://leetcode.com/problems/lexicographical-numbers/



class Solution {

    fun lexicalOrder(n: Int): List<Int> {

        val result = mutableListOf<Int>()

        dfs(1, n, result)

        return result

    }



    private fun dfs(current: Int, n: Int, result: MutableList<Int>) {

        if (current > n) {

            return

        }

        result.add(current)

        dfs(current * 10, n, result)

        if (current % 10 < 9) {

            dfs(current + 1, n, result)

        }

    }

}
