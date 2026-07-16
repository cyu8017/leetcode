// LeetCode 0360 - Sort Transformed Array

// https://leetcode.com/problems/sort-transformed-array/



class Solution {

    fun sortTransformedArray(nums: IntArray, a: Int, b: Int, c: Int): IntArray {

        var left = 0

        var right = nums.size - 1

        val result = IntArray(nums.size)

        var index = if (a > 0) nums.size - 1 else 0

        val step = if (a > 0) -1 else 1



        while (left <= right) {

            val leftValue = transform(nums[left], a, b, c)

            val rightValue = transform(nums[right], a, b, c)



            if (a > 0) {

                if (leftValue > rightValue) {

                    result[index] = leftValue

                    left++

                } else {

                    result[index] = rightValue

                    right--

                }

            } else if (leftValue < rightValue) {

                result[index] = leftValue

                left++

            } else {

                result[index] = rightValue

                right--

            }



            index += step

        }



        return result

    }



    private fun transform(value: Int, a: Int, b: Int, c: Int): Int {

        return a * value * value + b * value + c

    }

}
