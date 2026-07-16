// LeetCode 0347 - Top K Frequent Elements

// https://leetcode.com/problems/top-k-frequent-elements/



class Solution {

    fun topKFrequent(nums: IntArray, k: Int): IntArray {

        val counts = mutableMapOf<Int, Int>()

        for (num in nums) {

            counts[num] = counts.getOrDefault(num, 0) + 1

        }



        val buckets = Array(nums.size + 1) { mutableListOf<Int>() }

        for ((value, count) in counts) {

            buckets[count].add(value)

        }



        val result = IntArray(k)

        var writeIndex = 0

        for (index in buckets.indices.reversed()) {

            for (value in buckets[index]) {

                result[writeIndex++] = value

                if (writeIndex == k) {

                    return result

                }

            }

        }



        return result

    }

}
