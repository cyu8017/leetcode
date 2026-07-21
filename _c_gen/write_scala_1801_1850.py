#!/usr/bin/env python3
"""Write Scala Solution.scala for LeetCode 1801-1850 (non-SQL)."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FOLDERS: dict[int, str] = {
    1801: "1801_number_of_orders_in_the_backlog",
    1802: "1802_maximum_value_at_a_given_index_in_a_bounded_array",
    1803: "1803_count_pairs_with_xor_in_a_range",
    1804: "1804_implement_trie_ii_prefix_tree",
    1805: "1805_number_of_different_integers_in_a_string",
    1806: "1806_minimum_number_of_operations_to_reinitialize_a_permutation",
    1807: "1807_evaluate_the_bracket_pairs_of_a_string",
    1808: "1808_maximize_number_of_nice_divisors",
    1810: "1810_minimum_path_cost_in_a_hidden_grid",
    1812: "1812_determine_color_of_a_chessboard_square",
    1813: "1813_sentence_similarity_iii",
    1814: "1814_count_nice_pairs_in_an_array",
    1815: "1815_maximum_number_of_groups_getting_fresh_donuts",
    1816: "1816_truncate_sentence",
    1817: "1817_finding_the_users_active_minutes",
    1818: "1818_minimum_absolute_sum_difference",
    1819: "1819_number_of_different_subsequences_gcds",
    1820: "1820_maximum_number_of_accepted_invitations",
    1822: "1822_sign_of_the_product_of_an_array",
    1823: "1823_find_the_winner_of_the_circular_game",
    1824: "1824_minimum_sideway_jumps",
    1825: "1825_finding_mk_average",
    1826: "1826_faulty_sensor",
    1827: "1827_minimum_operations_to_make_the_array_increasing",
    1828: "1828_queries_on_number_of_points_inside_a_circle",
    1829: "1829_maximum_xor_for_each_query",
    1830: "1830_minimum_number_of_operations_to_make_string_sorted",
    1832: "1832_check_if_the_sentence_is_pangram",
    1833: "1833_maximum_ice_cream_bars",
    1834: "1834_single_threaded_cpu",
    1835: "1835_find_xor_sum_of_all_pairs_bitwise_and",
    1836: "1836_remove_duplicates_from_an_unsorted_linked_list",
    1837: "1837_sum_of_digits_in_base_k",
    1838: "1838_frequency_of_the_most_frequent_element",
    1839: "1839_longest_substring_of_all_vowels_in_order",
    1840: "1840_maximum_building_height",
    1842: "1842_next_palindrome_using_same_digits",
    1844: "1844_replace_all_digits_with_characters",
    1845: "1845_seat_reservation_manager",
    1846: "1846_maximum_element_after_decreasing_and_rearranging",
    1847: "1847_closest_room",
    1848: "1848_minimum_distance_to_the_target_element",
    1849: "1849_splitting_a_string_into_descending_consecutive_values",
    1850: "1850_minimum_adjacent_swaps_to_reach_the_kth_smallest_number",
}

SOLUTIONS: dict[int, str] = {}

SOLUTIONS[1801] = r'''// LeetCode 1801 - Number of Orders in the Backlog
// https://leetcode.com/problems/number-of-orders-in-the-backlog/

object Solution {
  def getNumberOfBacklogOrders(orders: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val buy = scala.collection.mutable.PriorityQueue.empty[(Int, Int)]
    val sell = scala.collection.mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](_._1).reverse)

    for (order <- orders) {
      val price = order(0)
      var amount = order(1)
      val orderType = order(2)
      if (orderType == 0) buy.enqueue((price, amount))
      else sell.enqueue((price, amount))

      while (buy.nonEmpty && sell.nonEmpty && buy.head._1 >= sell.head._1) {
        val (bp, ba) = buy.dequeue()
        val (sp, sa) = sell.dequeue()
        val matched = math.min(ba, sa)
        val buyLeft = ba - matched
        val sellLeft = sa - matched
        if (buyLeft > 0) buy.enqueue((bp, buyLeft))
        if (sellLeft > 0) sell.enqueue((sp, sellLeft))
      }
    }

    var total = 0L
    while (buy.nonEmpty) total = (total + buy.dequeue()._2) % MOD
    while (sell.nonEmpty) total = (total + sell.dequeue()._2) % MOD
    total.toInt
  }
}
'''

SOLUTIONS[1802] = r'''// LeetCode 1802 - Maximum Value at a Given Index in a Bounded Array
// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

object Solution {
  def maxValue(n: Int, index: Int, maxSum: Int): Int = {
    def minSideSum(value: Long, count: Long): Long = {
      if (value > count) (value - 1 + value - count) * count / 2
      else value * (value - 1) / 2 + (count - value + 1)
    }

    var lo = 1
    var hi = maxSum
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      val total = minSideSum(mid, index) + mid + minSideSum(mid, n - index - 1)
      if (total <= maxSum) lo = mid else hi = mid - 1
    }
    lo
  }
}
'''

SOLUTIONS[1803] = r'''// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

object Solution {
  private class TrieNode {
    var count = 0
    val children = Array.fill[TrieNode](2)(null)
  }

  def countPairs(nums: Array[Int], low: Int, high: Int): Int =
    countSmallerThan(nums, high + 1) - countSmallerThan(nums, low)

  private def countSmallerThan(nums: Array[Int], limit: Int): Int = {
    if (limit <= 0) return 0
    val root = new TrieNode
    var total = 0
    val maxBit = 15
    for (num <- nums) {
      total += query(root, num, limit, maxBit)
      insert(root, num, maxBit)
    }
    total
  }

  private def insert(root: TrieNode, num: Int, bit: Int): Unit = {
    var node = root
    var i = bit
    while (i >= 0) {
      val b = (num >> i) & 1
      if (node.children(b) == null) node.children(b) = new TrieNode
      node = node.children(b)
      node.count += 1
      i -= 1
    }
  }

  private def query(root: TrieNode, num: Int, limit: Int, bit: Int): Int = {
    if (root == null || bit < 0) return 0
    val numBit = (num >> bit) & 1
    val limitBit = (limit >> bit) & 1
    val child = root.children(numBit)
    if (limitBit == 1) {
      val same = if (child != null) child.count else 0
      same + query(root.children(1 - numBit), num, limit, bit - 1)
    } else {
      query(child, num, limit, bit - 1)
    }
  }
}
'''

SOLUTIONS[1804] = r'''// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

import scala.collection.mutable

class Trie() {
  private class TrieNode {
    val children = mutable.Map.empty[Char, TrieNode]
    var wordCount = 0
    var prefixCount = 0
  }

  private val root = new TrieNode

  def insert(word: String): Unit = {
    var node = root
    for (ch <- word) {
      node = node.children.getOrElseUpdate(ch, new TrieNode)
      node.prefixCount += 1
    }
    node.wordCount += 1
  }

  def countWordsEqualTo(word: String): Int = {
    val node = find(word)
    if (node == null) 0 else node.wordCount
  }

  def countWordsStartingWith(prefix: String): Int = {
    val node = find(prefix)
    if (node == null) 0 else node.prefixCount
  }

  def erase(word: String): Unit = {
    var node = root
    for (ch <- word) {
      node = node.children(ch)
      node.prefixCount -= 1
    }
    node.wordCount -= 1
  }

  private def find(text: String): TrieNode = {
    var node = root
    for (ch <- text) {
      node = node.children.getOrElse(ch, null)
      if (node == null) return null
    }
    node
  }
}
'''

SOLUTIONS[1805] = r'''// LeetCode 1805 - Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/

object Solution {
  def numDifferentIntegers(word: String): Int = {
    val seen = scala.collection.mutable.Set.empty[String]
    var i = 0
    while (i < word.length) {
      if (word(i).isDigit) {
        var j = i
        while (j < word.length && word(j).isDigit) j += 1
        var start = i
        while (start < j - 1 && word(start) == '0') start += 1
        seen += word.substring(start, j)
        i = j
      } else i += 1
    }
    seen.size
  }
}
'''

SOLUTIONS[1806] = r'''// LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

object Solution {
  def reinitializePermutation(n: Int): Int = {
    var perm = Array.tabulate(n)(identity)
    val target = Array.tabulate(n)(identity)
    var operations = 0
    while (true) {
      val next = Array.ofDim[Int](n)
      for (i <- 0 until n) {
        if (i % 2 == 0) next(i) = perm(i / 2)
        else next(i) = perm(n / 2 + (i - 1) / 2)
      }
      perm = next
      operations += 1
      if (perm.sameElements(target)) return operations
    }
    operations
  }
}
'''

SOLUTIONS[1807] = r'''// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

object Solution {
  def evaluate(s: String, knowledge: Array[Array[String]]): String = {
    val lookup = knowledge.map(p => p(0) -> p(1)).toMap
    val sb = new StringBuilder
    var i = 0
    while (i < s.length) {
      if (s(i) == '(') {
        val j = s.indexOf(')', i + 1)
        val key = s.substring(i + 1, j)
        sb.append(lookup.getOrElse(key, "?"))
        i = j + 1
      } else {
        sb.append(s(i))
        i += 1
      }
    }
    sb.toString
  }
}
'''

SOLUTIONS[1808] = r'''// LeetCode 1808 - Maximize Number of Nice Divisors
// https://leetcode.com/problems/maximize-number-of-nice-divisors/

object Solution {
  def maxNiceDivisors(primeFactors: Int): Int = {
    val MOD = BigInt(1000000007)
    if (primeFactors <= 3) return primeFactors
    if (primeFactors % 3 == 0) BigInt(3).modPow(primeFactors / 3, MOD).toInt
    else if (primeFactors % 3 == 1)
      ((BigInt(3).modPow(primeFactors / 3 - 1, MOD) * 4) % MOD).toInt
    else
      ((BigInt(3).modPow(primeFactors / 3, MOD) * 2) % MOD).toInt
  }
}
'''

SOLUTIONS[1810] = r'''// LeetCode 1810 - Minimum Path Cost in a Hidden Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

object Solution {
  // Test harness passes the revealed grid plus start/target coordinates.
  def findShortestPath(grid: Array[Array[Int]], r1: Int, c1: Int, r2: Int, c2: Int): Int = {
    if (r1 == r2 && c1 == c2) return 0
    val m = grid.length
    val n = grid(0).length
    val dirs = Array((-1, 0), (1, 0), (0, -1), (0, 1))
    val dist = Array.fill(m, n)(Int.MaxValue)
    val heap = scala.collection.mutable.PriorityQueue.empty[(Int, Int, Int)](
      Ordering.by[(Int, Int, Int), Int](_._1).reverse
    )
    dist(r1)(c1) = 0
    heap.enqueue((0, r1, c1))

    while (heap.nonEmpty) {
      val (d, r, c) = heap.dequeue()
      if (r == r2 && c == c2) return d
      if (d <= dist(r)(c)) {
        for ((dr, dc) <- dirs) {
          val nr = r + dr
          val nc = c + dc
          if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) != 0) {
            val nd = d + grid(nr)(nc)
            if (nd < dist(nr)(nc)) {
              dist(nr)(nc) = nd
              heap.enqueue((nd, nr, nc))
            }
          }
        }
      }
    }
    -1
  }
}
'''

SOLUTIONS[1812] = r'''// LeetCode 1812 - Determine Color of a Chessboard Square
// https://leetcode.com/problems/determine-color-of-a-chessboard-square/

object Solution {
  def squareIsWhite(coordinates: String): Boolean = {
    val col = coordinates(0) - 'a' + 1
    val row = coordinates(1) - '0'
    (col + row) % 2 == 1
  }
}
'''

SOLUTIONS[1813] = r'''// LeetCode 1813 - Sentence Similarity III
// https://leetcode.com/problems/sentence-similarity-iii/

object Solution {
  def areSentencesSimilar(sentence1: String, sentence2: String): Boolean = {
    val words1 = sentence1.split(" ")
    val words2 = sentence2.split(" ")
    val n1 = words1.length
    val n2 = words2.length
    var i = 0
    while (i < n1 && i < n2 && words1(i) == words2(i)) i += 1
    if (i == n1 || i == n2) return true
    var j1 = n1 - 1
    var j2 = n2 - 1
    while (j1 >= i && j2 >= i && words1(j1) == words2(j2)) {
      j1 -= 1
      j2 -= 1
    }
    j1 < i || j2 < i
  }
}
'''

SOLUTIONS[1814] = r'''// LeetCode 1814 - Count Nice Pairs in an Array
// https://leetcode.com/problems/count-nice-pairs-in-an-array/

object Solution {
  def countNicePairs(nums: Array[Int]): Int = {
    val MOD = 1000000007
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0
    for (num <- nums) {
      val diff = num - rev(num)
      ans = (ans + freq.getOrElse(diff, 0)) % MOD
      freq(diff) = freq.getOrElse(diff, 0) + 1
    }
    ans
  }

  private def rev(x: Int): Int = x.toString.reverse.toInt
}
'''

SOLUTIONS[1815] = r'''// LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

object Solution {
  def maxHappyGroups(batchSize: Int, groups: Array[Int]): Int = {
    val count = Array.fill(batchSize)(0)
    for (size <- groups) count(size % batchSize) += 1
    val memo = scala.collection.mutable.Map.empty[String, Int]

    def dfs(remainder: Int, state: Array[Int]): Int = {
      val key = remainder + "|" + state.mkString(",")
      if (memo.contains(key)) return memo(key)
      var best = 0
      var mod = 1
      while (mod < batchSize) {
        if (state(mod) > 0) {
          state(mod) -= 1
          best = math.max(best, dfs((remainder + mod) % batchSize, state))
          state(mod) += 1
        }
        mod += 1
      }
      if (remainder == 0) best += 1
      memo(key) = best
      best
    }

    var ans = dfs(0, count.clone())
    if (count(0) > 0) ans += count(0) - 1
    ans
  }
}
'''

SOLUTIONS[1816] = r'''// LeetCode 1816 - Truncate Sentence
// https://leetcode.com/problems/truncate-sentence/

object Solution {
  def truncateSentence(s: String, k: Int): String =
    s.split(" ").take(k).mkString(" ")
}
'''

SOLUTIONS[1817] = r'''// LeetCode 1817 - Finding the Users Active Minutes
// https://leetcode.com/problems/finding-the-users-active-minutes/

object Solution {
  def findingUsersActiveMinutes(logs: Array[Array[Int]], k: Int): Array[Int] = {
    val userMinutes = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.Set[Int]]
    for (log <- logs) {
      val userId = log(0)
      val minute = log(1)
      userMinutes.getOrElseUpdate(userId, scala.collection.mutable.Set.empty[Int]) += minute
    }
    val answer = Array.fill(k)(0)
    for (minutes <- userMinutes.values) {
      val uam = minutes.size
      if (uam <= k) answer(uam - 1) += 1
    }
    answer
  }
}
'''

SOLUTIONS[1818] = r'''// LeetCode 1818 - Minimum Absolute Sum Difference
// https://leetcode.com/problems/minimum-absolute-sum-difference/

object Solution {
  def minAbsoluteSumDiff(nums1: Array[Int], nums2: Array[Int]): Int = {
    val MOD = 1000000007
    val sorted = nums1.sorted
    var total = 0L
    var bestGain = 0
    for (i <- nums1.indices) {
      val current = math.abs(nums1(i) - nums2(i))
      total += current
      val target = nums2(i)
      var lo = 0
      var hi = sorted.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (sorted(mid) < target) lo = mid + 1 else hi = mid
      }
      for (j <- Seq(lo - 1, lo) if j >= 0 && j < sorted.length) {
        bestGain = math.max(bestGain, current - math.abs(sorted(j) - target))
      }
    }
    ((total - bestGain) % MOD).toInt
  }
}
'''

SOLUTIONS[1819] = r'''// LeetCode 1819 - Number of Different Subsequences GCDs
// https://leetcode.com/problems/number-of-different-subsequences-gcds/

object Solution {
  def countDifferentSubsequenceGCDs(nums: Array[Int]): Int = {
    val maxVal = nums.max
    val present = Array.fill(maxVal + 1)(false)
    for (num <- nums) present(num) = true
    var ans = 0
    for (g <- 1 to maxVal) {
      var has = false
      var gcdVal = 0
      var multiple = g
      while (multiple <= maxVal) {
        if (present(multiple)) {
          has = true
          gcdVal = gcd(gcdVal, multiple / g)
          if (gcdVal == 1) { multiple = maxVal + 1 }
          else multiple += g
        } else multiple += g
      }
      if (has && gcdVal == 1) ans += 1
    }
    ans
  }

  private def gcd(a: Int, b: Int): Int = {
    var x = a
    var y = b
    while (y != 0) {
      val t = x % y
      x = y
      y = t
    }
    x
  }
}
'''

SOLUTIONS[1820] = r'''// LeetCode 1820 - Maximum Number of Accepted Invitations
// https://leetcode.com/problems/maximum-number-of-accepted-invitations/

object Solution {
  def maximumInvitations(grid: Array[Array[Int]]): Int = {
    val boys = grid.length
    val girls = grid(0).length
    val matchGirl = Array.fill(girls)(-1)

    def dfs(boy: Int, seen: Array[Boolean]): Boolean = {
      for (girl <- 0 until girls if grid(boy)(girl) == 1 && !seen(girl)) {
        seen(girl) = true
        if (matchGirl(girl) == -1 || dfs(matchGirl(girl), seen)) {
          matchGirl(girl) = boy
          return true
        }
      }
      false
    }

    var ans = 0
    for (boy <- 0 until boys) {
      if (dfs(boy, Array.fill(girls)(false))) ans += 1
    }
    ans
  }
}
'''

SOLUTIONS[1822] = r'''// LeetCode 1822 - Sign of the Product of an Array
// https://leetcode.com/problems/sign-of-the-product-of-an-array/

object Solution {
  def arraySign(nums: Array[Int]): Int = {
    var sign = 1
    for (num <- nums) {
      if (num == 0) return 0
      if (num < 0) sign = -sign
    }
    sign
  }
}
'''

SOLUTIONS[1823] = r'''// LeetCode 1823 - Find the Winner of the Circular Game
// https://leetcode.com/problems/find-the-winner-of-the-circular-game/

object Solution {
  def findTheWinner(n: Int, k: Int): Int = {
    var pos = 0
    for (size <- 2 to n) pos = (pos + k) % size
    pos + 1
  }
}
'''

SOLUTIONS[1824] = r'''// LeetCode 1824 - Minimum Sideway Jumps
// https://leetcode.com/problems/minimum-sideway-jumps/

object Solution {
  def minSideJumps(obstacles: Array[Int]): Int = {
    val INF = Int.MaxValue / 4
    var dp = Array(1, 0, 1)
    for (obs <- obstacles) {
      val blocked = Array(obs == 1, obs == 2, obs == 3)
      val ndp = Array(INF, INF, INF)
      for (lane <- 0 until 3 if !blocked(lane)) {
        for (other <- 0 until 3 if !blocked(other) && dp(other) < INF) {
          ndp(lane) = math.min(ndp(lane), dp(other) + (if (lane != other) 1 else 0))
        }
      }
      dp = ndp
    }
    dp.min
  }
}
'''

SOLUTIONS[1825] = r'''// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

import scala.collection.mutable

class MKAverage(_m: Int, _k: Int) {
  private val m = _m
  private val k = _k
  private val stream = mutable.ArrayBuffer.empty[Int]

  def addElement(num: Int): Unit = {
    stream += num
  }

  def calculateMKAverage(): Int = {
    if (stream.size < m) return -1
    val window = stream.takeRight(m).sorted
    val middle = window.slice(k, window.length - k)
    middle.sum / middle.length
  }
}
'''

SOLUTIONS[1826] = r'''// LeetCode 1826 - Faulty Sensor
// https://leetcode.com/problems/faulty-sensor/

object Solution {
  def badSensor(sensor1: Array[Int], sensor2: Array[Int]): Int = {
    if (sensor1.sameElements(sensor2)) return -1

    def isDefective(correct: Array[Int], faulty: Array[Int]): Boolean = {
      val n = correct.length
      var i = 0
      while (i < n && correct(i) == faulty(i)) i += 1
      if (i == n) return false
      var j = i
      while (j < n - 1 && correct(j + 1) == faulty(j)) j += 1
      j == n - 1
    }

    val s1Bad = isDefective(sensor2, sensor1)
    val s2Bad = isDefective(sensor1, sensor2)
    if (s1Bad && s2Bad) -1
    else if (s1Bad) 1
    else if (s2Bad) 2
    else -1
  }
}
'''

SOLUTIONS[1827] = r'''// LeetCode 1827 - Minimum Operations to Make the Array Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    var ops = 0
    var prev = nums(0)
    for (i <- 1 until nums.length) {
      if (nums(i) <= prev) {
        val needed = prev + 1
        ops += needed - nums(i)
        prev = needed
      } else prev = nums(i)
    }
    ops
  }
}
'''

SOLUTIONS[1828] = r'''// LeetCode 1828 - Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

object Solution {
  def countPoints(points: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    queries.map { q =>
      val xq = q(0); val yq = q(1); val r = q(2)
      val r2 = r * r
      points.count { p =>
        val dx = p(0) - xq
        val dy = p(1) - yq
        dx * dx + dy * dy <= r2
      }
    }
  }
}
'''

SOLUTIONS[1829] = r'''// LeetCode 1829 - Maximum XOR for Each Query
// https://leetcode.com/problems/maximum-xor-for-each-query/

object Solution {
  def getMaximumXor(nums: Array[Int], maximumBit: Int): Array[Int] = {
    val limit = (1 << maximumBit) - 1
    var current = 0
    for (num <- nums) current ^= num
    val result = Array.ofDim[Int](nums.length)
    var idx = 0
    for (i <- nums.indices.reverse) {
      result(idx) = current ^ limit
      idx += 1
      current ^= nums(i)
    }
    result
  }
}
'''

SOLUTIONS[1830] = r'''// LeetCode 1830 - Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/

object Solution {
  def makeStringSorted(s: String): Int = {
    val MOD = 1000000007L
    val n = s.length
    val fact = Array.fill(n + 1)(1L)
    for (i <- 2 to n) fact(i) = fact(i - 1) * i % MOD
    val invFact = Array.fill(n + 1)(1L)
    invFact(n) = modPow(fact(n), MOD - 2, MOD)
    for (i <- n - 1 to 0 by -1) invFact(i) = invFact(i + 1) * (i + 1) % MOD

    val freq = Array.fill(26)(0)
    for (ch <- s) freq(ch - 'a') += 1

    var ans = 0L
    for (i <- 0 until n) {
      val c = s(i) - 'a'
      for (smaller <- 0 until c if freq(smaller) > 0) {
        freq(smaller) -= 1
        var ways = fact(n - i - 1)
        for (count <- freq) ways = ways * invFact(count) % MOD
        ans = (ans + ways) % MOD
        freq(smaller) += 1
      }
      freq(c) -= 1
    }
    ans.toInt
  }

  private def modPow(base: Long, exp: Long, mod: Long): Long = {
    var b = base % mod
    var e = exp
    var res = 1L
    while (e > 0) {
      if ((e & 1) == 1) res = res * b % mod
      b = b * b % mod
      e >>= 1
    }
    res
  }
}
'''

SOLUTIONS[1832] = r'''// LeetCode 1832 - Check if the Sentence Is Pangram
// https://leetcode.com/problems/check-if-the-sentence-is-pangram/

object Solution {
  def checkIfPangram(sentence: String): Boolean =
    sentence.toSet.size == 26
}
'''

SOLUTIONS[1833] = r'''// LeetCode 1833 - Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/

object Solution {
  def maxIceCream(costs: Array[Int], coins: Int): Int = {
    val sorted = costs.sorted
    var remaining = coins
    var count = 0
    for (cost <- sorted) {
      if (remaining < cost) return count
      remaining -= cost
      count += 1
    }
    count
  }
}
'''

SOLUTIONS[1834] = r'''// LeetCode 1834 - Single-Threaded CPU
// https://leetcode.com/problems/single-threaded-cpu/

object Solution {
  def getOrder(tasks: Array[Array[Int]]): Array[Int] = {
    val indexed = tasks.indices.map(i => (i, tasks(i)(0), tasks(i)(1))).sortBy(t => (t._2, t._1))
    val heap = scala.collection.mutable.PriorityQueue.empty[(Int, Int)](
      Ordering.by[(Int, Int), (Int, Int)](identity).reverse
    )
    var i = 0
    var time = 0L
    val order = scala.collection.mutable.ArrayBuffer.empty[Int]
    val n = tasks.length

    while (i < n || heap.nonEmpty) {
      if (i < n && heap.isEmpty) time = math.max(time, indexed(i)._2.toLong)
      while (i < n && indexed(i)._2 <= time) {
        heap.enqueue((indexed(i)._3, indexed(i)._1))
        i += 1
      }
      val (duration, idx) = heap.dequeue()
      time += duration
      order += idx
    }
    order.toArray
  }
}
'''

SOLUTIONS[1835] = r'''// LeetCode 1835 - Find XOR Sum of All Pairs Bitwise AND
// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

object Solution {
  def getXORSum(arr1: Array[Int], arr2: Array[Int]): Int =
    arr1.foldLeft(0)(_ ^ _) & arr2.foldLeft(0)(_ ^ _)
}
'''

SOLUTIONS[1836] = r'''// LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def deleteDuplicatesUnsorted(head: ListNode): ListNode = {
    val counts = scala.collection.mutable.Map.empty[Int, Int]
    var node = head
    while (node != null) {
      counts(node.x) = counts.getOrElse(node.x, 0) + 1
      node = node.next
    }
    val dummy = new ListNode(0, head)
    var prev = dummy
    node = head
    while (node != null) {
      if (counts(node.x) > 1) {
        prev.next = node.next
        node = node.next
      } else {
        prev = node
        node = node.next
      }
    }
    dummy.next
  }
}
'''

SOLUTIONS[1837] = r'''// LeetCode 1837 - Sum of Digits in Base K
// https://leetcode.com/problems/sum-of-digits-in-base-k/

object Solution {
  def sumBase(n: Int, k: Int): Int = {
    var x = n
    var total = 0
    while (x > 0) {
      total += x % k
      x /= k
    }
    total
  }
}
'''

SOLUTIONS[1838] = r'''// LeetCode 1838 - Frequency of the Most Frequent Element
// https://leetcode.com/problems/frequency-of-the-most-frequent-element/

object Solution {
  def maxFrequency(nums: Array[Int], k: Int): Int = {
    val sorted = nums.sorted
    var left = 0
    var windowSum = 0L
    var best = 0
    for (right <- sorted.indices) {
      val value = sorted(right).toLong
      windowSum += value
      while (value * (right - left + 1) - windowSum > k) {
        windowSum -= sorted(left)
        left += 1
      }
      best = math.max(best, right - left + 1)
    }
    best
  }
}
'''

SOLUTIONS[1839] = r'''// LeetCode 1839 - Longest Substring Of All Vowels in Order
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

object Solution {
  def longestBeautifulSubstring(word: String): Int = {
    val vowels = "aeiou"
    var best = 0
    for (start <- word.indices if word(start) == 'a') {
      val counts = Array.fill(5)(0)
      var end = start
      var cont = true
      while (end < word.length && cont) {
        val current = word(end)
        if (end > start && current < word(end - 1)) cont = false
        else {
          val idx = vowels.indexOf(current)
          if (idx < 0) cont = false
          else {
            counts(idx) += 1
            if (idx > 0 && counts(idx - 1) == 0) cont = false
            else if (counts.forall(_ > 0)) best = math.max(best, end - start + 1)
          }
        }
        if (cont) end += 1
      }
    }
    best
  }
}
'''

SOLUTIONS[1840] = r'''// LeetCode 1840 - Maximum Building Height
// https://leetcode.com/problems/maximum-building-height/

object Solution {
  def maxBuilding(n: Int, restrictions: Array[Array[Int]]): Int = {
    val points = scala.collection.mutable.ArrayBuffer((1, 0))
    points ++= restrictions.map(r => (r(0), r(1))).sortBy(_._1)
    if (points.last._1 != n) points += ((n, n - 1))

    for (i <- 1 until points.length) {
      val (prevId, prevH) = points(i - 1)
      val (currId, currH) = points(i)
      points(i) = (currId, math.min(currH, prevH + currId - prevId))
    }
    for (i <- points.length - 2 to 0 by -1) {
      val (nextId, nextH) = points(i + 1)
      val (currId, currH) = points(i)
      points(i) = (currId, math.min(currH, nextH + nextId - currId))
    }

    var best = points.map(_._2).max
    for (i <- 0 until points.length - 1) {
      val (id1, h1) = points(i)
      val (id2, h2) = points(i + 1)
      best = math.max(best, (h1 + h2 + id2 - id1) / 2)
    }
    best
  }
}
'''

SOLUTIONS[1842] = r'''// LeetCode 1842 - Next Palindrome Using Same Digits
// https://leetcode.com/problems/next-palindrome-using-same-digits/

object Solution {
  def nextPalindrome(num: String): String = {
    val nums = num.toArray
    if (!nextPermutation(nums)) return ""
    val n = nums.length
    for (i <- 0 until n / 2) nums(n - i - 1) = nums(i)
    new String(nums)
  }

  private def nextPermutation(nums: Array[Char]): Boolean = {
    val n = nums.length / 2
    var i = n - 2
    while (i >= 0 && nums(i) >= nums(i + 1)) i -= 1
    if (i < 0) return false
    var j = n - 1
    while (nums(j) <= nums(i)) j -= 1
    val tmp = nums(i); nums(i) = nums(j); nums(j) = tmp
    var l = i + 1
    var r = n - 1
    while (l < r) {
      val t = nums(l); nums(l) = nums(r); nums(r) = t
      l += 1; r -= 1
    }
    true
  }
}
'''

SOLUTIONS[1844] = r'''// LeetCode 1844 - Replace All Digits with Characters
// https://leetcode.com/problems/replace-all-digits-with-characters/

object Solution {
  def replaceDigits(s: String): String = {
    val chars = s.toArray
    var i = 1
    while (i < chars.length) {
      chars(i) = (chars(i - 1) + (chars(i) - '0')).toChar
      i += 2
    }
    new String(chars)
  }
}
'''

SOLUTIONS[1845] = r'''// LeetCode 1845 - Seat Reservation Manager
// https://leetcode.com/problems/seat-reservation-manager/

class SeatManager(_n: Int) {
  private val available = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
  for (i <- 1 to _n) available.enqueue(i)

  def reserve(): Int = available.dequeue()

  def unreserve(seatNumber: Int): Unit = available.enqueue(seatNumber)
}
'''

SOLUTIONS[1846] = r'''// LeetCode 1846 - Maximum Element After Decreasing and Rearranging
// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

object Solution {
  def maximumElementAfterDecrementingAndRearranging(arr: Array[Int]): Int = {
    val a = arr.sorted
    a(0) = 1
    for (i <- 1 until a.length) a(i) = math.min(a(i), a(i - 1) + 1)
    a.max
  }
}
'''

SOLUTIONS[1847] = r'''// LeetCode 1847 - Closest Room
// https://leetcode.com/problems/closest-room/

object Solution {
  def closestRoom(rooms: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val sortedRooms = rooms.sortBy(_(1))
    val indexed = queries.indices.map(i => (i, queries(i)(0), queries(i)(1))).sortBy(-_._3)
    val available = scala.collection.mutable.SortedSet.empty[Int]
    var roomIndex = sortedRooms.length - 1
    val answer = Array.fill(queries.length)(-1)

    for ((queryIndex, preferred, minSize) <- indexed) {
      while (roomIndex >= 0 && sortedRooms(roomIndex)(1) >= minSize) {
        available += sortedRooms(roomIndex)(0)
        roomIndex -= 1
      }
      if (available.nonEmpty) {
        val ge = available.rangeFrom(preferred)
        val le = available.rangeTo(preferred)
        var bestId = -1
        var bestDist = Int.MaxValue
        if (ge.nonEmpty) {
          val roomId = ge.head
          val dist = math.abs(roomId - preferred)
          if (dist < bestDist || (dist == bestDist && roomId < bestId)) {
            bestId = roomId
            bestDist = dist
          }
        }
        if (le.nonEmpty) {
          val roomId = le.last
          val dist = math.abs(roomId - preferred)
          if (dist < bestDist || (dist == bestDist && roomId < bestId)) {
            bestId = roomId
          }
        }
        answer(queryIndex) = bestId
      }
    }
    answer
  }
}
'''

SOLUTIONS[1848] = r'''// LeetCode 1848 - Minimum Distance to the Target Element
// https://leetcode.com/problems/minimum-distance-to-the-target-element/

object Solution {
  def getMinDistance(nums: Array[Int], target: Int, start: Int): Int = {
    var best = nums.length
    for (i <- nums.indices if nums(i) == target) {
      best = math.min(best, math.abs(i - start))
    }
    best
  }
}
'''

SOLUTIONS[1849] = r'''// LeetCode 1849 - Splitting a String Into Descending Consecutive Values
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

object Solution {
  def splitString(s: String): Boolean = {
    val n = s.length

    def dfs(index: Int, previous: Option[BigInt], parts: Int): Boolean = {
      if (index == n) return parts >= 2
      var end = index + 1
      while (end <= n) {
        val value = BigInt(s.substring(index, end))
        previous match {
          case None =>
            if (dfs(end, Some(value), parts + 1)) return true
          case Some(prev) =>
            if (value == prev - 1) {
              if (dfs(end, Some(value), parts + 1)) return true
            } else if (value > prev - 1) return false
        }
        end += 1
      }
      false
    }

    dfs(0, None, 0)
  }
}
'''

SOLUTIONS[1850] = r'''// LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

object Solution {
  def getMinSwaps(num: String, k: Int): Int = {
    def nextPermutation(arr: Array[Char]): Unit = {
      var i = arr.length - 2
      while (i >= 0 && arr(i) >= arr(i + 1)) i -= 1
      if (i < 0) {
        var l = 0
        var r = arr.length - 1
        while (l < r) {
          val t = arr(l); arr(l) = arr(r); arr(r) = t
          l += 1; r -= 1
        }
        return
      }
      var j = arr.length - 1
      while (arr(j) <= arr(i)) j -= 1
      val tmp = arr(i); arr(i) = arr(j); arr(j) = tmp
      var l = i + 1
      var r = arr.length - 1
      while (l < r) {
        val t = arr(l); arr(l) = arr(r); arr(r) = t
        l += 1; r -= 1
      }
    }

    val target = num.toArray
    for (_ <- 0 until k) nextPermutation(target)
    val source = num.toArray
    var swaps = 0
    for (i <- source.indices if source(i) != target(i)) {
      var j = i
      while (source(j) != target(i)) j += 1
      while (j > i) {
        val t = source(j); source(j) = source(j - 1); source(j - 1) = t
        swaps += 1
        j -= 1
      }
    }
    swaps
  }
}
'''


def main() -> None:
    assert len(SOLUTIONS) == 44
    written = 0
    for num, body in sorted(SOLUTIONS.items()):
        folder = ROOT / FOLDERS[num]
        path = folder / "Solution.scala"
        path.write_text(body.lstrip("\n") if body.startswith("\n") else body, encoding="utf-8")
        if not path.read_text(encoding="utf-8").endswith("\n"):
            path.write_text(path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        written += 1
        print(f"wrote {path.relative_to(ROOT)}")
    print(f"done: {written} files")


if __name__ == "__main__":
    main()
