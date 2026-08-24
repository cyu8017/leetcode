// LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
// https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

class Solution {
    private lateinit var unique: IntArray

    fun maxSubarraySum(nums: IntArray, k: Int): Long {
        val n = nums.size
        unique = nums.copyOf()
        unique.sort()
        var u = 0
        for (i in unique.indices) {
            if (u == 0 || unique[i] != unique[u - 1]) unique[u++] = unique[i]
        }
        unique = unique.copyOf(u)
        val rank = IntArray(n)
        val globalCount = IntArray(unique.size + 1)
        val globalSum = LongArray(unique.size + 1)
        for (i in 0 until n) {
            rank[i] = lowerBound(unique, nums[i]) + 1
            add(globalCount, globalSum, rank[i], 1)
        }
        var answer = -(1L shl 60)
        for (left in 0 until n) {
            val insideCount = IntArray(unique.size + 1)
            val insideSum = LongArray(unique.size + 1)
            val outsideCount = globalCount.copyOf()
            val outsideSum = globalSum.copyOf()
            var subarraySum = 0L
            for (right in left until n) {
                add(outsideCount, outsideSum, rank[right], -1)
                add(insideCount, insideSum, rank[right], 1)
                subarraySum += nums[right]
                val insideSize = right - left + 1
                val outsideSize = n - insideSize
                val limit = minOf(k, minOf(insideSize, outsideSize))
                var low = 0
                var high = limit
                while (low < high) {
                    val mid = (low + high + 1) / 2
                    val insideValue = unique[kth(insideCount, mid) - 1]
                    val outsideOrder = outsideSize - mid + 1
                    val outsideValue = unique[kth(outsideCount, outsideOrder) - 1]
                    if (outsideValue > insideValue) low = mid else high = mid - 1
                }
                val swaps = low
                var gain = 0L
                if (swaps > 0) {
                    val smallInside = sumSmallest(insideCount, insideSum, swaps)
                    val totalOutside = querySum(outsideSum, unique.size)
                    val largeOutside = totalOutside - sumSmallest(outsideCount, outsideSum, outsideSize - swaps)
                    gain = largeOutside - smallInside
                }
                answer = maxOf(answer, subarraySum + gain)
            }
        }
        return answer
    }

    private fun add(count: IntArray, sum: LongArray, index0: Int, delta: Int) {
        var index = index0
        val value = unique[index - 1].toLong()
        while (index < count.size) {
            count[index] += delta
            sum[index] += delta.toLong() * value
            index += index and -index
        }
    }

    private fun queryCount(bit: IntArray, index0: Int): Int {
        var index = index0
        var result = 0
        while (index > 0) {
            result += bit[index]
            index -= index and -index
        }
        return result
    }

    private fun querySum(bit: LongArray, index0: Int): Long {
        var index = index0
        var result = 0L
        while (index > 0) {
            result += bit[index]
            index -= index and -index
        }
        return result
    }

    private fun kth(bit: IntArray, order0: Int): Int {
        var order = order0
        var index = 0
        var step = 1
        while ((step shl 1) < bit.size) step = step shl 1
        while (step > 0) {
            val next = index + step
            if (next < bit.size && bit[next] < order) {
                index = next
                order -= bit[next]
            }
            step = step shr 1
        }
        return index + 1
    }

    private fun sumSmallest(count: IntArray, sum: LongArray, amount: Int): Long {
        if (amount <= 0) return 0
        val index = kth(count, amount)
        val countBefore = queryCount(count, index - 1)
        val sumBefore = querySum(sum, index - 1)
        return sumBefore + (amount - countBefore).toLong() * unique[index - 1]
    }

    private fun lowerBound(a: IntArray, x: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) ushr 1
            if (a[mid] < x) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
