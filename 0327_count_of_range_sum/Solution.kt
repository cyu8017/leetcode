// LeetCode 0327 - Count of Range Sum

// https://leetcode.com/problems/count-of-range-sum/



class Solution {

    private lateinit var prefix: LongArray

    private lateinit var temp: LongArray



    fun countRangeSum(nums: IntArray, lower: Int, upper: Int): Int {

        prefix = LongArray(nums.size + 1)

        temp = LongArray(prefix.size)

        for (index in nums.indices) {

            prefix[index + 1] = prefix[index] + nums[index]

        }

        return mergeSort(0, prefix.lastIndex, lower.toLong(), upper.toLong())

    }



    private fun mergeSort(left: Int, right: Int, lower: Long, upper: Long): Int {

        if (left >= right) {

            return 0

        }

        val mid = (left + right) / 2

        var count = mergeSort(left, mid, lower, upper) + mergeSort(mid + 1, right, lower, upper)

        var start = mid + 1

        var end = mid + 1

        for (index in left..mid) {

            while (start <= right && prefix[start] - prefix[index] < lower) {

                start++

            }

            while (end <= right && prefix[end] - prefix[index] <= upper) {

                end++

            }

            count += end - start

        }

        var tempLeft = left

        var tempRight = mid + 1

        var write = left

        while (tempLeft <= mid && tempRight <= right) {

            if (prefix[tempLeft] <= prefix[tempRight]) {

                temp[write++] = prefix[tempLeft++]

            } else {

                temp[write++] = prefix[tempRight++]

            }

        }

        while (tempLeft <= mid) {

            temp[write++] = prefix[tempLeft++]

        }

        while (tempRight <= right) {

            temp[write++] = prefix[tempRight++]

        }

        for (index in left..right) {

            prefix[index] = temp[index]

        }

        return count

    }

}

