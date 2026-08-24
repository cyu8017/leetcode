// LeetCode 0373 - Find K Pairs with Smallest Sums

// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/



import java.util.PriorityQueue



class Solution {

    fun kSmallestPairs(nums1: IntArray, nums2: IntArray, k: Int): List<List<Int>> {

        if (nums1.isEmpty() || nums2.isEmpty() || k == 0) {

            return emptyList()

        }



        val heap = PriorityQueue<Triple<Int, Int, Int>>(compareBy { it.first })

        val result = mutableListOf<List<Int>>()



        for (index in 0 until minOf(nums1.size, k)) {

            heap.offer(Triple(nums1[index] + nums2[0], index, 0))

        }



        while (heap.isNotEmpty() && result.size < k) {

            val (_, index1, index2) = heap.poll()

            result.add(listOf(nums1[index1], nums2[index2]))

            if (index2 + 1 < nums2.size) {

                heap.offer(Triple(nums1[index1] + nums2[index2 + 1], index1, index2 + 1))

            }

        }



        return result

    }

}
