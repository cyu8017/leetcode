// LeetCode 1865 - Finding Pairs With a Certain Sum
// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

class FindSumPairs(nums1: IntArray, nums2: IntArray) {
    private val nums1 = nums1
    private val nums2 = nums2
    private val counts = HashMap<Int, Int>()

    init {
        for (num in nums2) {
            counts[num] = counts.getOrDefault(num, 0) + 1
        }
    }

    fun add(index: Int, `val`: Int) {
        val old = nums2[index]
        counts[old] = counts[old]!! - 1
        nums2[index] += `val`
        counts[nums2[index]] = counts.getOrDefault(nums2[index], 0) + 1
    }

    fun count(tot: Int): Int {
        var answer = 0
        for (num in nums1) {
            answer += counts.getOrDefault(tot - num, 0)
        }
        return answer
    }
}
