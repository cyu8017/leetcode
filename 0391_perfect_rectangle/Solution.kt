// LeetCode 0391 - Perfect Rectangle

// https://leetcode.com/problems/perfect-rectangle/



class Solution {

    fun isRectangleCover(rectangles: Array<IntArray>): Boolean {

        val points = mutableSetOf<Long>()

        var area = 0L

        var minX = Int.MAX_VALUE

        var minY = Int.MAX_VALUE

        var maxX = Int.MIN_VALUE

        var maxY = Int.MIN_VALUE



        for ((x1, y1, x2, y2) in rectangles) {

            area += (x2 - x1).toLong() * (y2 - y1)

            minX = minOf(minX, x1)

            minY = minOf(minY, y1)

            maxX = maxOf(maxX, x2)

            maxY = maxOf(maxY, y2)



            for ((x, y) in arrayOf(x1 to y1, x1 to y2, x2 to y1, x2 to y2)) {

                val point = encode(x, y)

                if (point in points) {

                    points.remove(point)

                } else {

                    points.add(point)

                }

            }

        }



        val expectedCorners = setOf(

            encode(minX, minY),

            encode(minX, maxY),

            encode(maxX, minY),

            encode(maxX, maxY),

        )

        if (points != expectedCorners) {

            return false

        }



        return area == (maxX - minX).toLong() * (maxY - minY)

    }



    private fun encode(x: Int, y: Int): Long = (x.toLong() shl 32) or (y.toLong() and 0xffffffffL)

}
