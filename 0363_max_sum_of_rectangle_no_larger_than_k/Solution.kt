// LeetCode 0363 - Max Sum of Rectangle No Larger Than K

// https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/



class Solution {

    fun maxSumSubmatrix(matrix: Array<IntArray>, k: Int): Int {

        val rows = matrix.size

        val cols = if (rows == 0) 0 else matrix[0].size

        var result = Int.MIN_VALUE



        for (top in 0 until rows) {

            val colSums = IntArray(cols)

            for (bottom in top until rows) {

                val prefixSums = mutableListOf(0L)

                var running = 0L



                for (col in 0 until cols) {

                    colSums[col] += matrix[bottom][col]

                    running += colSums[col]

                    val index = prefixSums.binarySearch(running - k).let {

                        if (it >= 0) it else -(it + 1)

                    }

                    if (index < prefixSums.size) {

                        result = maxOf(result, (running - prefixSums[index]).toInt())

                    }

                    prefixSums.add(index, running)

                }

            }

        }



        return result

    }

}
