// LeetCode 0351 - Android Unlock Patterns

// https://leetcode.com/problems/android-unlock-patterns/



class Solution {

    companion object {

        private val jump = Array(9) { IntArray(9) }



        init {

            fun setJump(from: Int, to: Int, middle: Int) {

                jump[from][to] = middle

            }



            setJump(0, 2, 1)

            setJump(2, 0, 1)

            setJump(0, 6, 3)

            setJump(6, 0, 3)

            setJump(0, 8, 4)

            setJump(8, 0, 4)

            setJump(2, 8, 5)

            setJump(8, 2, 5)

            setJump(2, 6, 7)

            setJump(6, 2, 7)

            setJump(6, 8, 7)

            setJump(8, 6, 7)

            setJump(1, 7, 8)

            setJump(7, 1, 8)

            setJump(3, 7, 6)

            setJump(7, 3, 6)

            setJump(1, 5, 4)

            setJump(5, 1, 4)

            setJump(3, 5, 5)

            setJump(5, 3, 5)

            setJump(1, 3, 2)

            setJump(3, 1, 2)

            setJump(4, 5, 5)

            setJump(5, 4, 5)

            setJump(4, 7, 8)

            setJump(7, 4, 8)

            setJump(4, 3, 5)

            setJump(3, 4, 5)

            setJump(4, 1, 2)

            setJump(1, 4, 2)

            setJump(4, 6, 7)

            setJump(6, 4, 7)

            setJump(4, 8, 6)

            setJump(8, 4, 6)

            setJump(4, 0, 2)

            setJump(0, 4, 2)

            setJump(4, 2, 6)

            setJump(2, 4, 6)

        }

    }



    fun numberOfPatterns(m: Int, n: Int): Int {

        return dfs(1 shl 0, 0, 1, m, n) * 4

            + dfs(1 shl 1, 1, 1, m, n) * 4

            + dfs(1 shl 4, 4, 1, m, n)

    }



    private fun dfs(visited: Int, last: Int, length: Int, m: Int, n: Int): Int {

        if (length > n) {

            return 0

        }



        var count = if (length in m..n) 1 else 0

        for (next in 0 until 9) {

            if (isValid(visited, last, next)) {

                count += dfs(visited or (1 shl next), next, length + 1, m, n)

            }

        }

        return count

    }



    private fun isValid(visited: Int, last: Int, next: Int): Boolean {

        if (visited and (1 shl next) != 0) {

            return false

        }



        val middle = jump[last][next]

        if (middle > 0) {

            return visited and (1 shl middle) == 0

        }



        return kotlin.math.abs(last / 3 - next / 3) <= 1

            && kotlin.math.abs(last % 3 - next % 3) <= 1

    }

}
