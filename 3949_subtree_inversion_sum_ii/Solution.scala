// LeetCode 3949 - Subtree Inversion Sum II
// https://leetcode.com/problems/subtree-inversion-sum-ii/

import scala.collection.mutable

object Solution {
  def maxSubtreeInversionSum(edges: Array[Array[Int]], nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val graph = Array.fill(n)(mutable.ArrayBuffer.empty[Int])
    for (edge <- edges) {
      graph(edge(0)) += edge(1)
      graph(edge(1)) += edge(0)
    }
    val parent = Array.fill(n)(-2)
    parent(0) = -1
    val order = mutable.ArrayBuffer(0)
    var i = 0
    while (i < order.size) {
      val u = order(i)
      for (v <- graph(u)) {
        if (parent(v) == -2) {
          parent(v) = u
          order += v
        }
      }
      i += 1
    }
    val infinity = 1L << 60
    val maximum = new Array[Array[Long]](n)
    val minimum = new Array[Array[Long]](n)
    var oi = n - 1
    while (oi >= 0) {
      val u = order(oi)
      var currentMax = Array.fill(k + 1)(-infinity)
      var currentMin = Array.fill(k + 1)(infinity)
      currentMax(k) = nums(u)
      currentMin(k) = nums(u)
      for (v <- graph(u)) {
        if (parent(v) == u) {
          val nextMax = Array.fill(k + 1)(-infinity)
          val nextMin = Array.fill(k + 1)(infinity)
          var first = 0
          while (first <= k) {
            if (currentMax(first) != -infinity) {
              var childDistance = 0
              while (childDistance <= k) {
                if (maximum(v)(childDistance) != -infinity) {
                  var second = childDistance + 1
                  if (second > k) second = k
                  if (!(first < k && second < k && first + second < k)) {
                    val distance = math.min(first, second)
                    val maxValue = currentMax(first) + maximum(v)(childDistance)
                    val minValue = currentMin(first) + minimum(v)(childDistance)
                    nextMax(distance) = math.max(nextMax(distance), maxValue)
                    nextMin(distance) = math.min(nextMin(distance), minValue)
                  }
                }
                childDistance += 1
              }
            }
            first += 1
          }
          currentMax = nextMax
          currentMin = nextMin
        }
      }
      if (-currentMin(k) > currentMax(0)) currentMax(0) = -currentMin(k)
      if (-currentMax(k) < currentMin(0)) currentMin(0) = -currentMax(k)
      maximum(u) = currentMax
      minimum(u) = currentMin
      oi -= 1
    }
    var answer = -(1L << 60)
    for (value <- maximum(0)) answer = math.max(answer, value)
    answer
  }
}
