// LeetCode 0388 - Longest Absolute File Path

// https://leetcode.com/problems/longest-absolute-file-path/



class Solution {

    fun lengthLongestPath(input: String): Int {

        val stack = ArrayDeque<Int>()

        var maxLength = 0



        for (line in input.split("\n")) {

            val depth = line.takeWhile { it == '\t' }.length

            val name = line.substring(depth)



            while (stack.size > depth) {

                stack.removeLast()

            }



            if ('.' in name) {

                val prefix = stack.lastOrNull() ?: 0

                maxLength = maxOf(maxLength, prefix + name.length)

            } else {

                val prefix = stack.lastOrNull() ?: 0

                stack.addLast(prefix + name.length + 1)

            }

        }



        return maxLength

    }

}
