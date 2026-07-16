// LeetCode 0370 - Range Addition

// https://leetcode.com/problems/range-addition/



class Solution {

    fun getModifiedArray(length: Int, updates: Array<IntArray>): IntArray {

        val diff = IntArray(length + 1)



        for ((start, end, inc) in updates) {

            diff[start] += inc

            if (end + 1 < diff.size) {

                diff[end + 1] -= inc

            }

        }



        val result = IntArray(length)

        var running = 0

        for (index in 0 until length) {

            running += diff[index]

            result[index] = running

        }

        return result

    }

}
