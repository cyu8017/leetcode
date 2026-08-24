// LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
// https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

object Solution {
  private var unique: Array[Int] = Array.empty

  def maxSubarraySum(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    unique = nums.clone()
    java.util.Arrays.sort(unique)
    var u = 0
    var i = 0
    while (i < unique.length) {
      if (u == 0 || unique(i) != unique(u - 1)) {
        unique(u) = unique(i)
        u += 1
      }
      i += 1
    }
    unique = unique.take(u)
    val rank = new Array[Int](n)
    val globalCount = new Array[Int](unique.length + 1)
    val globalSum = new Array[Long](unique.length + 1)
    i = 0
    while (i < n) {
      rank(i) = lowerBound(unique, nums(i)) + 1
      add(globalCount, globalSum, rank(i), 1)
      i += 1
    }
    var answer = -(1L << 60)
    var left = 0
    while (left < n) {
      val insideCount = new Array[Int](unique.length + 1)
      val insideSum = new Array[Long](unique.length + 1)
      val outsideCount = globalCount.clone()
      val outsideSum = globalSum.clone()
      var subarraySum = 0L
      var right = left
      while (right < n) {
        add(outsideCount, outsideSum, rank(right), -1)
        add(insideCount, insideSum, rank(right), 1)
        subarraySum += nums(right)
        val insideSize = right - left + 1
        val outsideSize = n - insideSize
        val limit = math.min(k, math.min(insideSize, outsideSize))
        var low = 0
        var high = limit
        while (low < high) {
          val mid = (low + high + 1) / 2
          val insideValue = unique(kth(insideCount, mid) - 1)
          val outsideOrder = outsideSize - mid + 1
          val outsideValue = unique(kth(outsideCount, outsideOrder) - 1)
          if (outsideValue > insideValue) low = mid
          else high = mid - 1
        }
        val swaps = low
        var gain = 0L
        if (swaps > 0) {
          val smallInside = sumSmallest(insideCount, insideSum, swaps)
          val totalOutside = querySum(outsideSum, unique.length)
          val largeOutside = totalOutside - sumSmallest(outsideCount, outsideSum, outsideSize - swaps)
          gain = largeOutside - smallInside
        }
        answer = math.max(answer, subarraySum + gain)
        right += 1
      }
      left += 1
    }
    answer
  }

  private def add(count: Array[Int], sum: Array[Long], start: Int, delta: Int): Unit = {
    val value = unique(start - 1)
    var index = start
    while (index < count.length) {
      count(index) += delta
      sum(index) += delta.toLong * value
      index += index & -index
    }
  }

  private def queryCount(bit: Array[Int], start: Int): Int = {
    var result = 0
    var index = start
    while (index > 0) {
      result += bit(index)
      index -= index & -index
    }
    result
  }

  private def querySum(bit: Array[Long], start: Int): Long = {
    var result = 0L
    var index = start
    while (index > 0) {
      result += bit(index)
      index -= index & -index
    }
    result
  }

  private def kth(bit: Array[Int], startOrder: Int): Int = {
    var index = 0
    var order = startOrder
    var step = 1
    while ((step << 1) < bit.length) step <<= 1
    while (step > 0) {
      val next = index + step
      if (next < bit.length && bit(next) < order) {
        index = next
        order -= bit(next)
      }
      step >>= 1
    }
    index + 1
  }

  private def sumSmallest(count: Array[Int], sum: Array[Long], amount: Int): Long = {
    if (amount <= 0) return 0
    val index = kth(count, amount)
    val countBefore = queryCount(count, index - 1)
    val sumBefore = querySum(sum, index - 1)
    sumBefore + (amount - countBefore).toLong * unique(index - 1)
  }

  private def lowerBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (a(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
