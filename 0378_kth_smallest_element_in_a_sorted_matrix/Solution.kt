// LeetCode 0378 - Kth Smallest Element in a Sorted Matrix

// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/



class Solution {

    fun kthSmallest(matrix: Array<IntArray>, k: Int): Int {

        val rows = matrix.size

        var left = matrix[0][0]

        var right = matrix[rows - 1][rows - 1]



        while (left < right) {

            val mid = left + (right - left) / 2

            var count = 0

            var column = rows - 1



            for (row in 0 until rows) {

                while (column >= 0 && matrix[row][column] > mid) {

                    column--

                }

                count += column + 1

            }



            if (count < k) {

                left = mid + 1

            } else {

                right = mid

            }

        }



        return left

    }

}
