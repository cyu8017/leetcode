// LeetCode 3049 - Earliest Second to Mark Indices II
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

object Solution {
  def earliestSecondToMarkIndices(nums: Array[Int], changeIndices: Array[Int]): Int = {
    val secondToIndex = getSecondToIndex(nums, changeIndices)
    var numsSum = 0L
    nums.foreach(v => numsSum += v)
    var l = 0
    var r = changeIndices.length + 1
    while (l < r) {
      val m = (l + r) / 2
      if (canMark(nums, secondToIndex, m, numsSum)) r = m
      else l = m + 1
    }
    if (l <= changeIndices.length) l else -1
  }

  private def getSecondToIndex(nums: Array[Int], changeIndices: Array[Int]): java.util.HashMap[Integer, Integer] = {
    val indexToFirstSecond = new java.util.HashMap[Integer, Integer]()
    var second = 0
    while (second < changeIndices.length) {
      val index = changeIndices(second) - 1
      if (nums(index) > 0 && !indexToFirstSecond.containsKey(index)) {
        indexToFirstSecond.put(index, second)
      }
      second += 1
    }
    val secondToIndex = new java.util.HashMap[Integer, Integer]()
    val it = indexToFirstSecond.entrySet().iterator()
    while (it.hasNext) {
      val e = it.next()
      secondToIndex.put(e.getValue, e.getKey)
    }
    secondToIndex
  }

  private def canMark(
      nums: Array[Int],
      secondToIndex: java.util.HashMap[Integer, Integer],
      maxSecond: Int,
      numsSum: Long
  ): Boolean = {
    val h = new java.util.PriorityQueue[Integer]()
    var marks = 0
    var second = maxSecond - 1
    while (second >= 0) {
      if (secondToIndex.containsKey(second)) {
        h.offer(nums(secondToIndex.get(second)))
        if (marks == 0) {
          h.poll()
          marks += 1
        } else {
          marks -= 1
        }
      } else {
        marks += 1
      }
      second -= 1
    }
    val heapSize = h.size()
    var heapSum = 0L
    while (!h.isEmpty) heapSum += h.poll()
    val decrementAndMarkCost = numsSum - heapSum + (nums.length - heapSize)
    val zeroAndMarkCost = heapSize.toLong + heapSize
    decrementAndMarkCost + zeroAndMarkCost <= maxSecond
  }
}
