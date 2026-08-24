// LeetCode 3762 - Minimum Operations To Equalize Subarrays
// https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

object Solution {
  private class Node {
    var left: Int = 0
    var right: Int = 0
    var count: Int = 0
    var sum: Long = 0
    def this(o: Node) = {
      this()
      left = o.left; right = o.right; count = o.count; sum = o.sum
    }
  }

  def minOperations(nums: Array[Int], k: Int, queries: Array[Array[Int]]): Array[Long] = {
    val n = nums.length
    val quotient = new Array[Int](n)
    val remainder = new Array[Int](n)
    var values = new Array[Int](n)
    var i = 0
    while (i < n) {
      quotient(i) = nums(i) / k
      remainder(i) = nums(i) % k
      values(i) = quotient(i)
      i += 1
    }
    java.util.Arrays.sort(values)
    var vu = 1
    i = 1
    while (i < n) {
      if (values(i) != values(vu - 1)) {
        values(vu) = values(i)
        vu += 1
      }
      i += 1
    }
    values = java.util.Arrays.copyOf(values, vu)

    val nodes = new java.util.ArrayList[Node]()
    nodes.add(new Node())
    val roots = new Array[Int](n + 1)
    val umax = values.length - 1

    def update(previous: Int, lo: Int, hi: Int, position: Int, value: Int): Int = {
      val current = nodes.size()
      nodes.add(new Node(nodes.get(previous)))
      nodes.get(current).count += 1
      nodes.get(current).sum += value
      if (lo < hi) {
        val mid = (lo + hi) / 2
        if (position <= mid) nodes.get(current).left = update(nodes.get(previous).left, lo, mid, position, value)
        else nodes.get(current).right = update(nodes.get(previous).right, mid + 1, hi, position, value)
      }
      current
    }

    def kth(rightRoot: Int, leftRoot: Int, lo: Int, hi: Int, rank: Int): Int = {
      if (lo == hi) return lo
      val leftCount = nodes.get(nodes.get(rightRoot).left).count - nodes.get(nodes.get(leftRoot).left).count
      val mid = (lo + hi) / 2
      if (rank <= leftCount) kth(nodes.get(rightRoot).left, nodes.get(leftRoot).left, lo, mid, rank)
      else kth(nodes.get(rightRoot).right, nodes.get(leftRoot).right, mid + 1, hi, rank - leftCount)
    }

    def prefixStats(rightRoot: Int, leftRoot: Int, lo: Int, hi: Int, end: Int): Array[Long] = {
      if (end < lo) return Array(0L, 0L)
      if (hi <= end) return Array(
        (nodes.get(rightRoot).count - nodes.get(leftRoot).count).toLong,
        nodes.get(rightRoot).sum - nodes.get(leftRoot).sum
      )
      val mid = (lo + hi) / 2
      val left = prefixStats(nodes.get(rightRoot).left, nodes.get(leftRoot).left, lo, mid, end)
      var count = left(0)
      var sum = left(1)
      if (end > mid) {
        val right = prefixStats(nodes.get(rightRoot).right, nodes.get(leftRoot).right, mid + 1, hi, end)
        count += right(0)
        sum += right(1)
      }
      Array(count, sum)
    }

    def lowerBound(a: Array[Int], x: Int): Int = {
      var lo = 0
      var hi = a.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (a(mid) < x) lo = mid + 1
        else hi = mid
      }
      lo
    }

    i = 0
    while (i < n) {
      val position = lowerBound(values, quotient(i))
      roots(i + 1) = update(roots(i), 0, umax, position, quotient(i))
      i += 1
    }

    val logv = new Array[Int](n + 1)
    i = 2
    while (i <= n) {
      logv(i) = logv(i / 2) + 1
      i += 1
    }
    val levels = logv(n) + 1
    val minTable = new Array[Array[Int]](levels)
    val maxTable = new Array[Array[Int]](levels)
    minTable(0) = remainder.clone()
    maxTable(0) = remainder.clone()
    var level = 1
    while (level < levels) {
      val length = n - (1 << level) + 1
      minTable(level) = new Array[Int](length)
      maxTable(level) = new Array[Int](length)
      val half = 1 << (level - 1)
      i = 0
      while (i < length) {
        minTable(level)(i) = math.min(minTable(level - 1)(i), minTable(level - 1)(i + half))
        maxTable(level)(i) = math.max(maxTable(level - 1)(i), maxTable(level - 1)(i + half))
        i += 1
      }
      level += 1
    }

    val answer = new Array[Long](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val left = queries(qi)(0)
      val right = queries(qi)(1)
      val length = right - left + 1
      val lv = logv(length)
      val offset = right - (1 << lv) + 1
      val minR = math.min(minTable(lv)(left), minTable(lv)(offset))
      val maxR = math.max(maxTable(lv)(left), maxTable(lv)(offset))
      if (minR != maxR) {
        answer(qi) = -1
      } else {
        val medianIndex = kth(roots(right + 1), roots(left), 0, umax, (length + 1) / 2)
        val median = values(medianIndex)
        val stats = prefixStats(roots(right + 1), roots(left), 0, umax, medianIndex)
        val leftCount = stats(0).toInt
        val leftSum = stats(1)
        val totalSum = nodes.get(roots(right + 1)).sum - nodes.get(roots(left)).sum
        answer(qi) = 1L * median * leftCount - leftSum + (totalSum - leftSum) - 1L * median * (length - leftCount)
      }
      qi += 1
    }
    answer
  }
}
