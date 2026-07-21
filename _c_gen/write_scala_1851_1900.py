#!/usr/bin/env python3
"""Write Scala solutions for LeetCode 1851-1900 (non-SQL)."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOLUTIONS: dict[int, str] = {}

SOLUTIONS[1851] = r'''// LeetCode 1851 - Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/

import scala.collection.mutable

object Solution {
  def minInterval(intervals: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
    val sorted = intervals.sortBy(_(0))
    val indexed = queries.zipWithIndex.sortBy(_._1)
    val heap = mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](-_._1))
    val answer = Array.fill(queries.length)(-1)
    var intervalIdx = 0

    for ((query, queryIdx) <- indexed) {
      while (intervalIdx < sorted.length && sorted(intervalIdx)(0) <= query) {
        val left = sorted(intervalIdx)(0)
        val right = sorted(intervalIdx)(1)
        heap.enqueue((right - left + 1, right))
        intervalIdx += 1
      }
      while (heap.nonEmpty && heap.head._2 < query) {
        heap.dequeue()
      }
      if (heap.nonEmpty) {
        answer(queryIdx) = heap.head._1
      }
    }
    answer
  }
}
'''

SOLUTIONS[1852] = r'''// LeetCode 1852 - Distinct Numbers in Each Subarray
// https://leetcode.com/problems/distinct-numbers-in-each-subarray/

import scala.collection.mutable

object Solution {
  def distinctNumbers(nums: Array[Int], k: Int): Array[Int] = {
    val counts = mutable.Map.empty[Int, Int]
    for (i <- 0 until k) {
      counts(nums(i)) = counts.getOrElse(nums(i), 0) + 1
    }
    val result = mutable.ArrayBuffer(counts.size)
    var left = 0
    for (right <- k until nums.length) {
      counts(nums(right)) = counts.getOrElse(nums(right), 0) + 1
      val outgoing = nums(left)
      counts(outgoing) = counts(outgoing) - 1
      if (counts(outgoing) == 0) counts.remove(outgoing)
      left += 1
      result += counts.size
    }
    result.toArray
  }
}
'''

SOLUTIONS[1854] = r'''// LeetCode 1854 - Maximum Population Year
// https://leetcode.com/problems/maximum-population-year/

object Solution {
  def maximumPopulation(logs: Array[Array[Int]]): Int = {
    val diff = Array.fill(101)(0)
    for (log <- logs) {
      diff(log(0) - 1950) += 1
      diff(log(1) - 1950) -= 1
    }
    var bestYear = 1950
    var bestPopulation = 0
    var population = 0
    for (offset <- 0 until 101) {
      population += diff(offset)
      if (population > bestPopulation) {
        bestPopulation = population
        bestYear = 1950 + offset
      }
    }
    bestYear
  }
}
'''

SOLUTIONS[1855] = r'''// LeetCode 1855 - Maximum Distance Between a Pair of Values
// https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

object Solution {
  def maxDistance(nums1: Array[Int], nums2: Array[Int]): Int = {
    var answer = 0
    var j = 0
    for (i <- nums1.indices) {
      while (j < nums2.length && nums1(i) <= nums2(j)) {
        j += 1
      }
      answer = math.max(answer, j - i - 1)
    }
    answer
  }
}
'''

SOLUTIONS[1856] = r'''// LeetCode 1856 - Maximum Subarray Min-Product
// https://leetcode.com/problems/maximum-subarray-min-product/

import scala.collection.mutable

object Solution {
  def maxSumMinProduct(nums: Array[Int]): Int = {
    val mod = 1000000007
    val n = nums.length
    val prefix = Array.ofDim[Long](n + 1)
    for (i <- nums.indices) {
      prefix(i + 1) = prefix(i) + nums(i)
    }

    val leftBound = Array.fill(n)(-1)
    val stack = mutable.ArrayBuffer.empty[Int]
    for (i <- nums.indices) {
      while (stack.nonEmpty && nums(stack.last) >= nums(i)) {
        stack.remove(stack.length - 1)
      }
      leftBound(i) = if (stack.isEmpty) -1 else stack.last
      stack += i
    }

    val rightBound = Array.fill(n)(n)
    stack.clear()
    for (i <- n - 1 to 0 by -1) {
      while (stack.nonEmpty && nums(stack.last) >= nums(i)) {
        stack.remove(stack.length - 1)
      }
      rightBound(i) = if (stack.isEmpty) n else stack.last
      stack += i
    }

    var best = 0L
    for (i <- nums.indices) {
      val total = prefix(rightBound(i)) - prefix(leftBound(i) + 1)
      best = math.max(best, total * nums(i))
    }
    (best % mod).toInt
  }
}
'''

SOLUTIONS[1857] = r'''// LeetCode 1857 - Largest Color Value in a Directed Graph
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

import scala.collection.mutable

object Solution {
  def largestPathValue(colors: String, edges: Array[Array[Int]]): Int = {
    val n = colors.length
    val indegree = Array.fill(n)(0)
    val adjacency = Array.fill(n)(mutable.ArrayBuffer.empty[Int])
    for (edge <- edges) {
      adjacency(edge(0)) += edge(1)
      indegree(edge(1)) += 1
    }

    val queue = mutable.Queue[Int]()
    for (node <- 0 until n if indegree(node) == 0) {
      queue.enqueue(node)
    }

    val dp = Array.fill(n, 26)(0)
    for (node <- 0 until n) {
      dp(node)(colors(node) - 'a') = 1
    }

    var processed = 0
    var answer = 0
    while (queue.nonEmpty) {
      val node = queue.dequeue()
      processed += 1
      answer = math.max(answer, dp(node).max)
      for (neighbor <- adjacency(node)) {
        val neighborColor = colors(neighbor) - 'a'
        for (colorIndex <- 0 until 26) {
          var candidate = dp(node)(colorIndex)
          if (colorIndex == neighborColor) candidate += 1
          if (candidate > dp(neighbor)(colorIndex)) {
            dp(neighbor)(colorIndex) = candidate
          }
        }
        indegree(neighbor) -= 1
        if (indegree(neighbor) == 0) queue.enqueue(neighbor)
      }
    }
    if (processed == n) answer else -1
  }
}
'''

SOLUTIONS[1858] = r'''// LeetCode 1858 - Longest Word With All Prefixes
// https://leetcode.com/problems/longest-word-with-all-prefixes/

object Solution {
  def longestWord(words: Array[String]): String = {
    val wordSet = words.toSet
    var best = ""
    for (word <- words) {
      var prefix = word
      var valid = true
      while (prefix.nonEmpty && valid) {
        if (!wordSet.contains(prefix)) valid = false
        else prefix = prefix.substring(0, prefix.length - 1)
      }
      if (valid && (word.length > best.length || (word.length == best.length && word < best))) {
        best = word
      }
    }
    best
  }
}
'''

SOLUTIONS[1859] = r'''// LeetCode 1859 - Sorting the Sentence
// https://leetcode.com/problems/sorting-the-sentence/

object Solution {
  def sortSentence(s: String): String = {
    val tokens = s.split(" ")
    val ordered = Array.fill(tokens.length)("")
    for (token <- tokens) {
      val position = token.last.asDigit - 1
      ordered(position) = token.substring(0, token.length - 1)
    }
    ordered.mkString(" ")
  }
}
'''

SOLUTIONS[1860] = r'''// LeetCode 1860 - Incremental Memory Leak
// https://leetcode.com/problems/incremental-memory-leak/

object Solution {
  def memLeak(memory1: Int, memory2: Int): Array[Int] = {
    var m1 = memory1
    var m2 = memory2
    var second = 1
    while (m1 >= second || m2 >= second) {
      if (m1 >= m2) m1 -= second
      else m2 -= second
      second += 1
    }
    Array(second, m1, m2)
  }
}
'''

SOLUTIONS[1861] = r'''// LeetCode 1861 - Rotating the Box
// https://leetcode.com/problems/rotating-the-box/

object Solution {
  def rotateTheBox(boxGrid: Array[Array[Char]]): Array[Array[Char]] = {
    val m = boxGrid.length
    val n = boxGrid(0).length
    val rotated = Array.fill(n, m)('.')
    for (i <- 0 until n; j <- 0 until m) {
      rotated(i)(j) = boxGrid(m - 1 - j)(i)
    }
    for (col <- 0 until m) {
      var row = n - 1
      for (i <- n - 1 to 0 by -1) {
        if (rotated(i)(col) == '*') {
          row = i - 1
        } else if (rotated(i)(col) == '#') {
          rotated(i)(col) = '.'
          rotated(row)(col) = '#'
          row -= 1
        }
      }
    }
    rotated
  }
}
'''

SOLUTIONS[1862] = r'''// LeetCode 1862 - Sum of Floored Pairs
// https://leetcode.com/problems/sum-of-floored-pairs/

object Solution {
  def sumOfFlooredPairs(nums: Array[Int]): Int = {
    val mod = 1000000007
    val maxVal = nums.max
    val count = Array.fill(maxVal + 1)(0)
    for (num <- nums) count(num) += 1

    val prefix = Array.fill(maxVal + 1)(0)
    prefix(0) = count(0)
    for (value <- 1 to maxVal) {
      prefix(value) = prefix(value - 1) + count(value)
    }

    var answer = 0L
    for (divisor <- 1 to maxVal if count(divisor) > 0) {
      var quotient = 1
      while (quotient.toLong * divisor <= maxVal) {
        val low = quotient * divisor
        val high = math.min((quotient + 1) * divisor - 1, maxVal)
        val matches = prefix(high) - (if (low > 0) prefix(low - 1) else 0)
        answer = (answer + count(divisor).toLong * matches * quotient) % mod
        quotient += 1
      }
    }
    answer.toInt
  }
}
'''

SOLUTIONS[1863] = r'''// LeetCode 1863 - Sum of All Subset XOR Totals
// https://leetcode.com/problems/sum-of-all-subset-xor-totals/

object Solution {
  def subsetXORSum(nums: Array[Int]): Int = {
    var bits = 0
    for (num <- nums) bits |= num
    var total = 0
    var bit = 1
    while (bit <= bits) {
      if ((bits & bit) != 0) total += bit
      bit <<= 1
    }
    total << (nums.length - 1)
  }
}
'''

SOLUTIONS[1864] = r'''// LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

object Solution {
  def minSwaps(s: String): Int = {
    val zeros = s.count(_ == '0')
    val ones = s.length - zeros
    if (math.abs(zeros - ones) > 1) return -1

    def mismatches(start: Char): Int = {
      var count = 0
      for (i <- s.indices) {
        val expected = if (i % 2 == 0) start else (if (start == '0') '1' else '0')
        if (s(i) != expected) count += 1
      }
      count / 2
    }

    if (zeros == ones) math.min(mismatches('0'), mismatches('1'))
    else if (zeros > ones) mismatches('0')
    else mismatches('1')
  }
}
'''

SOLUTIONS[1865] = r'''// LeetCode 1865 - Finding Pairs With a Certain Sum
// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

import scala.collection.mutable

class FindSumPairs(_nums1: Array[Int], _nums2: Array[Int]) {
  private val nums1 = _nums1
  private val nums2 = _nums2.clone()
  private val counts = mutable.Map.empty[Int, Int]
  for (num <- nums2) {
    counts(num) = counts.getOrElse(num, 0) + 1
  }

  def add(index: Int, `val`: Int): Unit = {
    counts(nums2(index)) = counts(nums2(index)) - 1
    nums2(index) += `val`
    counts(nums2(index)) = counts.getOrElse(nums2(index), 0) + 1
  }

  def count(tot: Int): Int = {
    var answer = 0
    for (num <- nums1) {
      answer += counts.getOrElse(tot - num, 0)
    }
    answer
  }
}
'''

SOLUTIONS[1866] = r'''// LeetCode 1866 - Number of Ways to Rearrange Sticks With K Sticks Visible
// https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

object Solution {
  def rearrangeSticks(n: Int, k: Int): Int = {
    val mod = 1000000007
    if (k == 0 || k > n) return 0
    val dp = Array.fill(n + 1, n + 1)(0L)
    dp(1)(1) = 1
    for (sticks <- 2 to n) {
      dp(sticks)(1) = (sticks - 1) * dp(sticks - 1)(1) % mod
      for (visible <- 2 to sticks) {
        dp(sticks)(visible) = (
          dp(sticks - 1)(visible - 1) + (sticks - 1) * dp(sticks - 1)(visible)
        ) % mod
      }
    }
    dp(n)(k).toInt
  }
}
'''

SOLUTIONS[1868] = r'''// LeetCode 1868 - Product of Two Run-Length Encoded Arrays
// https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

import scala.collection.mutable

object Solution {
  def findRLEArray(encoded1: Array[Array[Int]], encoded2: Array[Array[Int]]): Array[Array[Int]] = {
    val result = mutable.ArrayBuffer.empty[Array[Int]]
    var i = 0
    var j = 0
    var rem1 = encoded1(0)(1)
    var rem2 = encoded2(0)(1)

    while (i < encoded1.length) {
      val take = math.min(rem1, rem2)
      val value = encoded1(i)(0) * encoded2(j)(0)
      if (result.nonEmpty && result.last(0) == value) {
        result.last(1) += take
      } else {
        result += Array(value, take)
      }
      rem1 -= take
      rem2 -= take
      if (rem1 == 0) {
        i += 1
        if (i < encoded1.length) rem1 = encoded1(i)(1)
      }
      if (rem2 == 0) {
        j += 1
        if (j < encoded2.length) rem2 = encoded2(j)(1)
      }
    }
    result.toArray
  }
}
'''

SOLUTIONS[1869] = r'''// LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

object Solution {
  def checkZeroOnes(s: String): Boolean = {
    var maxZeros = 0
    var maxOnes = 0
    var zeros = 0
    var ones = 0
    for (ch <- s) {
      if (ch == '0') {
        zeros += 1
        ones = 0
        maxZeros = math.max(maxZeros, zeros)
      } else {
        ones += 1
        zeros = 0
        maxOnes = math.max(maxOnes, ones)
      }
    }
    maxOnes > maxZeros
  }
}
'''

SOLUTIONS[1870] = r'''// LeetCode 1870 - Minimum Speed to Arrive on Time
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

object Solution {
  def minSpeedOnTime(dist: Array[Int], hour: Double): Int = {
    val n = dist.length
    if (n - 1 >= hour) return -1

    def canArrive(speed: Int): Boolean = {
      var time = 0.0
      for (i <- 0 until n - 1) {
        time += (dist(i) + speed - 1) / speed
      }
      time += dist(n - 1).toDouble / speed
      time <= hour
    }

    if (!canArrive(10000000)) return -1
    var lo = 1
    var hi = 10000000
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (canArrive(mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }
}
'''

SOLUTIONS[1871] = r'''// LeetCode 1871 - Jump Game VII
// https://leetcode.com/problems/jump-game-vii/

object Solution {
  def canReach(s: String, minJump: Int, maxJump: Int): Boolean = {
    val n = s.length
    val reachable = Array.fill(n)(false)
    reachable(0) = true
    val prefix = Array.fill(n + 1)(0)
    for (i <- 0 until n) {
      if (i > 0 && s(i) == '0') {
        val left = math.max(0, i - maxJump)
        val right = i - minJump
        if (right >= left && prefix(right + 1) - prefix(left) > 0) {
          reachable(i) = true
        }
      }
      prefix(i + 1) = prefix(i) + (if (reachable(i)) 1 else 0)
    }
    reachable(n - 1)
  }
}
'''

SOLUTIONS[1872] = r'''// LeetCode 1872 - Stone Game VIII
// https://leetcode.com/problems/stone-game-viii/

object Solution {
  def stoneGameVIII(stones: Array[Int]): Int = {
    val n = stones.length
    for (i <- 1 until n) {
      stones(i) += stones(i - 1)
    }
    var score = stones(n - 1)
    for (i <- n - 2 to 1 by -1) {
      score = math.max(stones(i) - score, score)
    }
    score
  }
}
'''

SOLUTIONS[1874] = r'''// LeetCode 1874 - Minimize Product Sum of Two Arrays
// https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

object Solution {
  def minProductSum(nums1: Array[Int], nums2: Array[Int]): Int = {
    val a = nums1.sorted
    val b = nums2.sorted.reverse
    a.zip(b).map { case (x, y) => x * y }.sum
  }
}
'''

SOLUTIONS[1876] = r'''// LeetCode 1876 - Substrings of Size Three with Distinct Characters
// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

object Solution {
  def countGoodSubstrings(s: String): Int = {
    if (s.length < 3) return 0
    var count = 0
    for (i <- 0 until s.length - 2) {
      val window = s.substring(i, i + 3)
      if (window.toSet.size == 3) count += 1
    }
    count
  }
}
'''

SOLUTIONS[1877] = r'''// LeetCode 1877 - Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

object Solution {
  def minPairSum(nums: Array[Int]): Int = {
    val sorted = nums.sorted
    var best = 0
    for (i <- 0 until sorted.length / 2) {
      best = math.max(best, sorted(i) + sorted(sorted.length - 1 - i))
    }
    best
  }
}
'''

SOLUTIONS[1878] = r'''// LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

import scala.collection.mutable

object Solution {
  def getBiggestThree(grid: Array[Array[Int]]): Array[Int] = {
    val m = grid.length
    val n = grid(0).length
    val s1 = Array.fill(m + 1, n + 2)(0)
    val s2 = Array.fill(m + 1, n + 2)(0)

    for (i <- 1 to m; j <- 1 to n) {
      val value = grid(i - 1)(j - 1)
      s1(i)(j) = s1(i - 1)(j - 1) + value
      s2(i)(j) = s2(i - 1)(j + 1) + value
    }

    val rhombusSums = mutable.Set.empty[Int]
    for (i <- 1 to m; j <- 1 to n) {
      val value = grid(i - 1)(j - 1)
      val limit = math.min(math.min(i - 1, m - i), math.min(j - 1, n - j))
      rhombusSums += value
      for (k <- 1 to limit) {
        val a = s1(i + k)(j) - s1(i)(j - k)
        val b = s1(i)(j + k) - s1(i - k)(j)
        val c = s2(i)(j - k) - s2(i - k)(j)
        val d = s2(i + k)(j) - s2(i)(j + k)
        rhombusSums += a + b + c + d - grid(i + k - 1)(j - 1) + grid(i - k - 1)(j - 1)
      }
    }
    rhombusSums.toArray.sorted.reverse.take(3)
  }
}
'''

SOLUTIONS[1879] = r'''// LeetCode 1879 - Minimum XOR Sum of Two Arrays
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

object Solution {
  def minimumXORSum(nums1: Array[Int], nums2: Array[Int]): Int = {
    val n = nums1.length
    val dp = Array.fill(1 << n)(Int.MaxValue / 2)
    dp(0) = 0
    for (mask <- 0 until (1 << n)) {
      val i = Integer.bitCount(mask)
      if (i < n) {
        for (j <- 0 until n if (mask & (1 << j)) == 0) {
          val nextMask = mask | (1 << j)
          val cost = dp(mask) + (nums1(i) ^ nums2(j))
          if (cost < dp(nextMask)) dp(nextMask) = cost
        }
      }
    }
    dp((1 << n) - 1)
  }
}
'''

SOLUTIONS[1880] = r'''// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

object Solution {
  def isSumEqual(firstWord: String, secondWord: String, targetWord: String): Boolean = {
    def value(word: String): Int =
      word.map(ch => (ch - 'a').toString).mkString.toInt

    value(firstWord) + value(secondWord) == value(targetWord)
  }
}
'''

SOLUTIONS[1881] = r'''// LeetCode 1881 - Maximum Value after Insertion
// https://leetcode.com/problems/maximum-value-after-insertion/

object Solution {
  def maxValue(n: String, x: Int): String = {
    val neg = n(0) == '-'
    val start = if (neg) 1 else 0
    for (i <- start until n.length) {
      val d = n(i) - '0'
      if (neg) {
        if (d > x) return n.substring(0, i) + x + n.substring(i)
      } else if (d < x) {
        return n.substring(0, i) + x + n.substring(i)
      }
    }
    n + x
  }
}
'''

SOLUTIONS[1882] = r'''// LeetCode 1882 - Process Tasks Using Servers
// https://leetcode.com/problems/process-tasks-using-servers/

import scala.collection.mutable

object Solution {
  def assignTasks(servers: Array[Int], tasks: Array[Int]): Array[Int] = {
    val available = mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), (Int, Int)](t => (t._1, t._2)).reverse)
    for (index <- servers.indices) {
      available.enqueue((servers(index), index))
    }
    val busy = mutable.PriorityQueue.empty[(Long, Int, Int)](
      Ordering.by[(Long, Int, Int), (Long, Int, Int)](t => (t._1, t._2, t._3)).reverse
    )
    val answer = Array.ofDim[Int](tasks.length)
    var time = 0L

    for (moment <- tasks.indices) {
      val task = tasks(moment)
      time = math.max(time, moment.toLong)
      while (busy.nonEmpty && busy.head._1 <= time) {
        val (_, weight, index) = busy.dequeue()
        available.enqueue((weight, index))
      }
      while (available.isEmpty) {
        time = busy.head._1
        while (busy.nonEmpty && busy.head._1 <= time) {
          val (_, weight, index) = busy.dequeue()
          available.enqueue((weight, index))
        }
      }
      val (weight, index) = available.dequeue()
      busy.enqueue((time + task, weight, index))
      answer(moment) = index
    }
    answer
  }
}
'''

SOLUTIONS[1883] = r'''// LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

object Solution {
  def minSkips(dist: Array[Int], speed: Int, hoursBefore: Int): Int = {
    val limit = hoursBefore.toLong * speed
    val n = dist.length
    val INF = Long.MaxValue / 4
    var dp = Array.fill(n + 1)(INF)
    dp(0) = 0L
    for (road <- dist) {
      val nxt = Array.fill(n + 1)(INF)
      for (skips <- 0 until n if dp(skips) < INF) {
        val ceiled = ((dp(skips) + road + speed - 1) / speed) * speed
        nxt(skips) = math.min(nxt(skips), ceiled)
        nxt(skips + 1) = math.min(nxt(skips + 1), dp(skips) + road)
      }
      dp = nxt
    }
    for (skips <- dp.indices if dp(skips) <= limit) {
      return skips
    }
    -1
  }
}
'''

SOLUTIONS[1884] = r'''// LeetCode 1884 - Egg Drop With 2 Eggs and N Floors
// https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

object Solution {
  def twoEggDrop(n: Int): Int = {
    var moves = 0
    var covered = 0
    while (covered < n) {
      moves += 1
      covered += moves
    }
    moves
  }
}
'''

SOLUTIONS[1885] = r'''// LeetCode 1885 - Count Pairs in Two Arrays
// https://leetcode.com/problems/count-pairs-in-two-arrays/

object Solution {
  def countPairs(nums1: Array[Int], nums2: Array[Int]): Long = {
    val diff = nums1.zip(nums2).map { case (a, b) => a - b }.sorted
    var answer = 0L
    val n = diff.length
    for (i <- 0 until n) {
      val target = -diff(i)
      var lo = i + 1
      var hi = n
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (diff(mid) <= target) lo = mid + 1
        else hi = mid
      }
      answer += n - lo
    }
    answer
  }
}
'''

SOLUTIONS[1886] = r'''// LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

object Solution {
  def findRotation(mat: Array[Array[Int]], target: Array[Array[Int]]): Boolean = {
    var current = mat
    for (_ <- 0 until 4) {
      if (current.indices.forall(r => current(r).sameElements(target(r)))) return true
      val n = current.length
      current = Array.tabulate(n, n) { (col, row) => current(n - 1 - row)(col) }
    }
    false
  }
}
'''

SOLUTIONS[1887] = r'''// LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

object Solution {
  def reductionOperations(nums: Array[Int]): Int = {
    val sorted = nums.sorted
    var answer = 0
    var rank = 0
    for (i <- 1 until sorted.length) {
      if (sorted(i) != sorted(i - 1)) rank += 1
      answer += rank
    }
    answer
  }
}
'''

SOLUTIONS[1888] = r'''// LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

object Solution {
  def minFlips(s: String): Int = {
    val n = s.length
    val doubled = s + s
    var alt0 = 0
    var alt1 = 0
    for (i <- 0 until n) {
      val expect0 = if (i % 2 == 0) '0' else '1'
      val expect1 = if (i % 2 == 0) '1' else '0'
      if (doubled(i) != expect0) alt0 += 1
      if (doubled(i) != expect1) alt1 += 1
    }
    var answer = math.min(alt0, alt1)
    for (i <- 0 until n) {
      val expect0i = if (i % 2 == 0) '0' else '1'
      val expect0n = if ((i + n) % 2 == 0) '0' else '1'
      if (doubled(i) != expect0i) alt0 -= 1
      if (doubled(i + n) != expect0n) alt0 += 1

      val expect1i = if (i % 2 == 0) '1' else '0'
      val expect1n = if ((i + n) % 2 == 0) '1' else '0'
      if (doubled(i) != expect1i) alt1 -= 1
      if (doubled(i + n) != expect1n) alt1 += 1

      answer = math.min(answer, math.min(alt0, alt1))
    }
    answer
  }
}
'''

SOLUTIONS[1889] = r'''// LeetCode 1889 - Minimum Space Wasted From Packaging
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/

object Solution {
  def minWastedSpace(packages: Array[Int], boxes: Array[Array[Int]]): Int = {
    val sortedPackages = packages.sorted
    val prefix = Array.ofDim[Long](sortedPackages.length)
    prefix(0) = sortedPackages(0)
    for (i <- 1 until sortedPackages.length) {
      prefix(i) = prefix(i - 1) + sortedPackages(i)
    }

    var answer = Long.MaxValue
    for (supplier <- boxes) {
      val sortedBoxes = supplier.sorted
      var start = 0
      var wasted = 0L
      var ok = true
      for (box <- sortedBoxes if ok) {
        var lo = start
        var hi = sortedPackages.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (sortedPackages(mid) <= box) lo = mid + 1
          else hi = mid
        }
        val end = lo
        if (end != start) {
          val packageSum = prefix(end - 1) - (if (start > 0) prefix(start - 1) else 0L)
          wasted += box.toLong * (end - start) - packageSum
          start = end
        }
      }
      if (start == sortedPackages.length) {
        answer = math.min(answer, wasted)
      }
    }
    if (answer == Long.MaxValue) -1 else (answer % 1000000007L).toInt
  }
}
'''

SOLUTIONS[1891] = r'''// LeetCode 1891 - Cutting Ribbons
// https://leetcode.com/problems/cutting-ribbons/

object Solution {
  def maxLength(ribbons: Array[Int], k: Int): Int = {
    def can(length: Int): Boolean = {
      var total = 0L
      for (ribbon <- ribbons) {
        total += ribbon / length
        if (total >= k) return true
      }
      total >= k
    }

    var lo = 1
    var hi = ribbons.max
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (can(mid)) lo = mid
      else hi = mid - 1
    }
    if (can(lo)) lo else 0
  }
}
'''

SOLUTIONS[1893] = r'''// LeetCode 1893 - Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

object Solution {
  def isCovered(ranges: Array[Array[Int]], left: Int, right: Int): Boolean = {
    val covered = Array.fill(51)(false)
    for (r <- ranges; value <- r(0) to r(1)) {
      covered(value) = true
    }
    (left to right).forall(covered)
  }
}
'''

SOLUTIONS[1894] = r'''// LeetCode 1894 - Find the Student that Will Replace the Chalk
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

object Solution {
  def chalkReplacer(chalk: Array[Int], k: Int): Int = {
    var remaining = k.toLong % chalk.map(_.toLong).sum
    for (index <- chalk.indices) {
      if (remaining < chalk(index)) return index
      remaining -= chalk(index)
    }
    0
  }
}
'''

SOLUTIONS[1895] = r'''// LeetCode 1895 - Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/

object Solution {
  def largestMagicSquare(grid: Array[Array[Int]]): Int = {
    val rows = grid.length
    val cols = grid(0).length
    val rowPrefix = Array.fill(rows, cols + 1)(0)
    val colPrefix = Array.fill(cols, rows + 1)(0)
    for (i <- 0 until rows; j <- 0 until cols) {
      rowPrefix(i)(j + 1) = rowPrefix(i)(j) + grid(i)(j)
      colPrefix(j)(i + 1) = colPrefix(j)(i) + grid(i)(j)
    }

    def rowSum(row: Int, colStart: Int, colEnd: Int): Int =
      rowPrefix(row)(colEnd + 1) - rowPrefix(row)(colStart)

    def colSum(col: Int, rowStart: Int, rowEnd: Int): Int =
      colPrefix(col)(rowEnd + 1) - colPrefix(col)(rowStart)

    def isMagic(rowStart: Int, colStart: Int, size: Int): Boolean = {
      val target = rowSum(rowStart, colStart, colStart + size - 1)
      for (row <- rowStart until rowStart + size) {
        if (rowSum(row, colStart, colStart + size - 1) != target) return false
      }
      for (col <- colStart until colStart + size) {
        if (colSum(col, rowStart, rowStart + size - 1) != target) return false
      }
      var diag1 = 0
      var diag2 = 0
      for (offset <- 0 until size) {
        diag1 += grid(rowStart + offset)(colStart + offset)
        diag2 += grid(rowStart + offset)(colStart + size - 1 - offset)
      }
      diag1 == target && diag2 == target
    }

    for (size <- math.min(rows, cols) to 1 by -1) {
      for (rowStart <- 0 to rows - size; colStart <- 0 to cols - size) {
        if (isMagic(rowStart, colStart, size)) return size
      }
    }
    1
  }
}
'''

SOLUTIONS[1896] = r'''// LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

object Solution {
  def minOperationsToFlip(expression: String): Int = {
    def combine(left: Array[Int], op: Char, right: Array[Int]): Array[Int] = {
      val Array(leftVal, leftToZero, leftToOne) = left
      val Array(rightVal, rightToZero, rightToOne) = right
      if (op == '&') {
        val andVal = leftVal & rightVal
        val andToZero = math.min(leftToZero, leftToOne + rightToZero)
        val andToOne = leftToOne + rightToOne
        val orToZero = leftToZero + rightToZero
        val orToOne = math.min(leftToOne, math.min(leftToZero + rightToOne, rightToZero + leftToOne))
        Array(andVal, math.min(andToZero, 1 + orToZero), math.min(andToOne, 1 + orToOne))
      } else {
        val orVal = leftVal | rightVal
        val orToZero = leftToZero + rightToZero
        val orToOne = math.min(leftToOne, math.min(leftToZero + rightToOne, rightToZero + leftToOne))
        val andToZero = math.min(leftToZero, leftToOne + rightToZero)
        val andToOne = leftToOne + rightToOne
        Array(orVal, math.min(orToZero, 1 + andToZero), math.min(orToOne, 1 + andToOne))
      }
    }

    var index = 0

    def parseFactor(): Array[Int] = {
      if (expression(index) == '0' || expression(index) == '1') {
        val value = expression(index) - '0'
        index += 1
        Array(value, if (value == 0) 0 else 1, if (value == 0) 1 else 0)
      } else {
        index += 1
        val node = parseExpr()
        index += 1
        node
      }
    }

    def parseExpr(): Array[Int] = {
      var node = parseFactor()
      while (index < expression.length && (expression(index) == '&' || expression(index) == '|')) {
        val op = expression(index)
        index += 1
        node = combine(node, op, parseFactor())
      }
      node
    }

    val Array(value, toZero, toOne) = parseExpr()
    if (value == 0) toOne else toZero
  }
}
'''

SOLUTIONS[1897] = r'''// LeetCode 1897 - Redistribute Characters to Make All Strings Equal
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

object Solution {
  def makeEqual(words: Array[String]): Boolean = {
    val counts = Array.fill(26)(0)
    for (word <- words; ch <- word) {
      counts(ch - 'a') += 1
    }
    val n = words.length
    counts.forall(_ % n == 0)
  }
}
'''

SOLUTIONS[1898] = r'''// LeetCode 1898 - Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

object Solution {
  def maximumRemovals(s: String, p: String, removable: Array[Int]): Int = {
    def stillSubsequence(k: Int): Boolean = {
      val removed = removable.take(k).toSet
      var index = 0
      for (position <- s.indices if !removed.contains(position)) {
        if (index < p.length && s(position) == p(index)) index += 1
      }
      index == p.length
    }

    var lo = 0
    var hi = removable.length
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (stillSubsequence(mid)) lo = mid
      else hi = mid - 1
    }
    lo
  }
}
'''

SOLUTIONS[1899] = r'''// LeetCode 1899 - Merge Triplets to Form Target Triplet
// https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

object Solution {
  def mergeTriplets(triplets: Array[Array[Int]], target: Array[Int]): Boolean = {
    val merged = Array(0, 0, 0)
    for (t <- triplets) {
      if (t(0) <= target(0) && t(1) <= target(1) && t(2) <= target(2)) {
        merged(0) = math.max(merged(0), t(0))
        merged(1) = math.max(merged(1), t(1))
        merged(2) = math.max(merged(2), t(2))
      }
    }
    merged.sameElements(target)
  }
}
'''

SOLUTIONS[1900] = r'''// LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

import scala.collection.mutable

object Solution {
  def earliestAndLatest(n: Int, firstPlayer: Int, secondPlayer: Int): Array[Int] = {
    val first = firstPlayer
    val second = secondPlayer
    val memo = mutable.Map.empty[List[Int], Array[Int]]

    def dfs(players: List[Int]): Array[Int] = {
      memo.get(players) match {
        case Some(cached) => return cached
        case None =>
      }
      val count = players.length
      val firstIndex = players.indexOf(first)
      val secondIndex = players.indexOf(second)
      if (firstIndex + secondIndex == count - 1) {
        val result = Array(1, 1)
        memo(players) = result
        return result
      }

      val choices = mutable.ArrayBuffer.empty[List[Int]]
      for (index <- 0 until count / 2) {
        val left = players(index)
        val right = players(count - 1 - index)
        if (left == first || left == second) choices += List(left)
        else if (right == first || right == second) choices += List(right)
        else choices += List(left, right)
      }
      if (count % 2 == 1) choices += List(players(count / 2))

      var earliest = Int.MaxValue / 2
      var latest = 0

      def explore(i: Int, picks: mutable.ArrayBuffer[Int]): Unit = {
        if (i == choices.length) {
          val winners = picks.sorted.toList
          val Array(early, late) = dfs(winners)
          earliest = math.min(earliest, early + 1)
          latest = math.max(latest, late + 1)
          return
        }
        for (pick <- choices(i)) {
          picks += pick
          explore(i + 1, picks)
          picks.remove(picks.length - 1)
        }
      }

      explore(0, mutable.ArrayBuffer.empty[Int])
      val result = Array(earliest, latest)
      memo(players) = result
      result
    }

    dfs((1 to n).toList)
  }
}
'''


def main() -> None:
    skip = {1853, 1867, 1873, 1875, 1890, 1892}
    written = []
    for num, content in sorted(SOLUTIONS.items()):
        if num in skip:
            continue
        folders = list(ROOT.glob(f"{num:04d}_*"))
        if not folders:
            raise SystemExit(f"Missing folder for {num}")
        path = folders[0] / "Solution.scala"
        path.write_text(content.lstrip("\n"), encoding="utf-8", newline="\n")
        written.append(folders[0].name)
    print(f"Wrote {len(written)} Solution.scala files")
    for name in written:
        print(f"  {name}")


if __name__ == "__main__":
    main()
