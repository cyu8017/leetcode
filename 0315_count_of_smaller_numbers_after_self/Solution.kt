// LeetCode 0315 - Count of Smaller Numbers After Self

// https://leetcode.com/problems/count-of-smaller-numbers-after-self/



class Solution {

    fun countSmaller(nums: IntArray): List<Int> {

        val sortedNums = mutableListOf<Int>()

        val result = mutableListOf<Int>()

        for (index in nums.indices.reversed()) {

            val num = nums[index]

            val position = lowerBound(sortedNums, num)

            result.add(position)

            sortedNums.add(position, num)

        }

        result.reverse()

        return result

    }



    private fun lowerBound(list: List<Int>, target: Int): Int {

        var left = 0

        var right = list.size

        while (left < right) {

            val mid = left + (right - left) / 2

            if (list[mid] < target) {

                left = mid + 1

            } else {

                right = mid

            }

        }

        return left

    }

}

