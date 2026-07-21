// LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

class Solution {
    fun getMinSwaps(num: String, k: Int): Int {
        fun nextPermutation(arr: CharArray) {
            var i = arr.size - 2
            while (i >= 0 && arr[i] >= arr[i + 1]) i--
            if (i < 0) {
                arr.reverse()
                return
            }
            var j = arr.size - 1
            while (arr[j] <= arr[i]) j--
            val tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            var left = i + 1
            var right = arr.size - 1
            while (left < right) {
                val t = arr[left]
                arr[left] = arr[right]
                arr[right] = t
                left++
                right--
            }
        }

        val target = num.toCharArray()
        repeat(k) { nextPermutation(target) }

        val source = num.toCharArray()
        var swaps = 0
        for (i in source.indices) {
            if (source[i] == target[i]) continue
            var j = i
            while (source[j] != target[i]) j++
            while (j > i) {
                val tmp = source[j]
                source[j] = source[j - 1]
                source[j - 1] = tmp
                swaps++
                j--
            }
        }
        return swaps
    }
}
