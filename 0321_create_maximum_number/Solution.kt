// LeetCode 0321 - Create Maximum Number

// https://leetcode.com/problems/create-maximum-number/



class Solution {

    fun maxNumber(nums1: IntArray, nums2: IntArray, k: Int): IntArray {

        var best = intArrayOf()

        val minFirst = maxOf(0, k - nums2.size)

        val maxFirst = minOf(k, nums1.size)

        for (takeFirst in minFirst..maxFirst) {

            val takeSecond = k - takeFirst

            val candidate = merge(pickMax(nums1, takeFirst), pickMax(nums2, takeSecond))

            if (compare(candidate, best) > 0) {

                best = candidate

            }

        }

        return best

    }



    private fun pickMax(values: IntArray, count: Int): IntArray {

        var drop = values.size - count

        val stack = mutableListOf<Int>()

        for (value in values) {

            while (drop > 0 && stack.isNotEmpty() && stack.last() < value) {

                stack.removeAt(stack.lastIndex)

                drop--

            }

            stack.add(value)

        }

        return stack.take(count).toIntArray()

    }



    private fun merge(first: IntArray, second: IntArray): IntArray {

        val result = IntArray(first.size + second.size)

        var left = 0

        var right = 0

        var write = 0

        while (left < first.size && right < second.size) {

            if (compareSuffix(first, left, second, right) > 0) {

                result[write++] = first[left++]

            } else {

                result[write++] = second[right++]

            }

        }

        while (left < first.size) {

            result[write++] = first[left++]

        }

        while (right < second.size) {

            result[write++] = second[right++]

        }

        return result

    }



    private fun compareSuffix(first: IntArray, left: Int, second: IntArray, right: Int): Int {

        var index = left

        var other = right

        while (index < first.size && other < second.size) {

            if (first[index] != second[other]) {

                return first[index].compareTo(second[other])

            }

            index++

            other++

        }

        return (first.size - left).compareTo(second.size - right)

    }



    private fun compare(left: IntArray, right: IntArray): Int {

        if (left.size != right.size) {

            return left.size.compareTo(right.size)

        }

        for (index in left.indices) {

            if (left[index] != right[index]) {

                return left[index].compareTo(right[index])

            }

        }

        return 0

    }

}

