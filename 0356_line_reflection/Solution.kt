// LeetCode 0356 - Line Reflection

// https://leetcode.com/problems/line-reflection/



class Solution {

    fun isReflected(points: Array<IntArray>): Boolean {

        val pointSet = mutableSetOf<String>()

        var minX = Int.MAX_VALUE

        var maxX = Int.MIN_VALUE



        for ((x, y) in points) {

            pointSet.add("$x,$y")

            minX = minOf(minX, x)

            maxX = maxOf(maxX, x)

        }



        val target = minX + maxX

        for ((x, y) in points) {

            if ("${target - x},$y" !in pointSet) {

                return false

            }

        }



        return true

    }

}
