#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3395_subsequences_with_a_unique_middle_mode_i"] = r'''// LeetCode 3395 - Subsequences with a Unique Middle Mode I
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/

object Solution {
  private def uniqueMode(a: Array[Int]): Boolean = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    a.foreach { x => freq(x) = freq.getOrElse(x, 0) + 1 }
    var best = 0
    var cnt = 0
    freq.values.foreach { f =>
      if (f > best) { best = f; cnt = 1 }
      else if (f == best) cnt += 1
    }
    cnt == 1
  }

  def subsequencesWithMiddleMode(nums: Array[Int]): Int = {
    val mod = 1000000007
    val n = nums.length
    var ans = 0
    var mid = 2
    while (mid < n - 2) {
      var a = 0
      while (a < mid) {
        var b = a + 1
        while (b < mid) {
          var c = mid + 1
          while (c < n) {
            var d = c + 1
            while (d < n) {
              val seq = Array(nums(a), nums(b), nums(mid), nums(c), nums(d))
              if (uniqueMode(seq)) ans += 1
              d += 1
            }
            c += 1
          }
          b += 1
        }
        a += 1
      }
      mid += 1
    }
    ans % mod
  }
}
'''

FILES["3396_minimum_number_of_operations_to_make_elements_in_array_distinct"] = r'''// LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

object Solution {
  def minimumOperations(nums: Array[Int]): Int = {
    val list = scala.collection.mutable.ArrayBuffer.from(nums)
    var ops = 0
    while (true) {
      val seen = scala.collection.mutable.Set.empty[Int]
      var dup = false
      list.foreach { x =>
        if (!dup && !seen.add(x)) dup = true
      }
      if (!dup) return ops
      if (list.size <= 3) return ops + 1
      list.remove(0, 3)
      ops += 1
    }
    ops
  }
}
'''

FILES["3397_maximum_number_of_distinct_elements_after_operations"] = r'''// LeetCode 3397 - Maximum Number of Distinct Elements After Operations
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

object Solution {
  def maxDistinctElements(nums: Array[Int], k: Int): Int = {
    java.util.Arrays.sort(nums)
    var ans = 0
    var prev = Long.MinValue / 2
    nums.foreach { x =>
      var cur = x.toLong - k
      if (cur <= prev) cur = prev + 1
      if (cur <= x.toLong + k) {
        ans += 1
        prev = cur
      }
    }
    ans
  }
}
'''

FILES["3398_smallest_substring_with_identical_characters_i"] = r'''// LeetCode 3398 - Smallest Substring With Identical Characters I
// https://leetcode.com/problems/smallest-substring-with-identical-characters-i/

object Solution {
  def minLength(s: String, numOps: Int): Int = {
    val n = s.length
    var lo = 1
    var hi = n
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(s, n, numOps, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(s: String, n: Int, numOps: Int, L: Int): Boolean = {
    if (L == 0) return false
    var ops = 0
    var i = 0
    while (i < n) {
      var j = i
      while (j < n && s.charAt(j) == s.charAt(i)) j += 1
      ops += (j - i) / (L + 1)
      i = j
    }
    ops <= numOps
  }
}
'''

FILES["3399_smallest_substring_with_identical_characters_ii"] = r'''// LeetCode 3399 - Smallest Substring With Identical Characters II
// https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/

object Solution {
  def minLength(s: String, numOps: Int): Int = {
    val n = s.length
    var lo = 1
    var hi = n
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(s, n, numOps, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(s: String, n: Int, numOps: Int, L: Int): Boolean = {
    var ops = 0
    var i = 0
    while (i < n) {
      var j = i
      while (j < n && s.charAt(j) == s.charAt(i)) j += 1
      ops += (j - i) / (L + 1)
      i = j
    }
    ops <= numOps
  }
}
'''

FILES["3400_maximum_number_of_matching_indices_after_right_shifts"] = r'''// LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
// https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

object Solution {
  def maximumMatchingIndices(nums1: Array[Int], nums2: Array[Int]): Int = {
    val n = nums1.length
    var ans = 0
    var shift = 0
    while (shift < n) {
      var cnt = 0
      var i = 0
      while (i < n) {
        if (nums1((i - shift + n) % n) == nums2(i)) cnt += 1
        i += 1
      }
      if (cnt > ans) ans = cnt
      shift += 1
    }
    ans
  }
}
'''

FILES["3402_minimum_operations_to_make_columns_strictly_increasing"] = r'''// LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
// https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

object Solution {
  def minimumOperations(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var ans = 0
    var j = 0
    while (j < n) {
      var i = 1
      while (i < m) {
        if (grid(i)(j) <= grid(i - 1)(j)) {
          val need = grid(i - 1)(j) + 1
          ans += need - grid(i)(j)
          grid(i)(j) = need
        }
        i += 1
      }
      j += 1
    }
    ans
  }
}
'''

FILES["3403_find_the_lexicographically_largest_string_from_the_box_i"] = r'''// LeetCode 3403 - Find the Lexicographically Largest String From the Box I
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

object Solution {
  def answerString(word: String, numFriends: Int): String = {
    if (numFriends == 1) return word
    val n = word.length
    val maxLen = n - (numFriends - 1)
    var ans = ""
    var i = 0
    while (i < n) {
      var end = i + maxLen
      if (end > n) end = n
      val cand = word.substring(i, end)
      if (cand.compareTo(ans) > 0) ans = cand
      i += 1
    }
    ans
  }
}
'''

FILES["3404_count_special_subsequences"] = r'''// LeetCode 3404 - Count Special Subsequences
// https://leetcode.com/problems/count-special-subsequences/

object Solution {
  def numberOfSubsequences(nums: Array[Int]): Long = {
    val n = nums.length
    var ans = 0L
    var i = 0
    while (i < n) {
      var j = i + 2
      while (j < n) {
        var k = j + 2
        while (k < n) {
          var l = k + 2
          while (l < n) {
            if (nums(i).toLong * nums(k) == nums(j).toLong * nums(l)) ans += 1
            l += 1
          }
          k += 1
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3405_count_the_number_of_arrays_with_k_matching_adjacent_elements"] = r'''// LeetCode 3405 - Count the Number of Arrays with K Matching Adjacent Elements
// https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

object Solution {
  private def modPow(a0: Long, e0: Long, mod: Int): Long = {
    var a = if (a0 < 0) 0L else a0
    var e = e0
    var r = 1L
    a %= mod
    while (e > 0) {
      if ((e & 1) != 0) r = r * a % mod
      a = a * a % mod
      e >>= 1
    }
    r
  }

  private def comb(n: Int, k: Int, mod: Int): Int = {
    if (k < 0 || k > n) return 0
    var num = 1L
    var den = 1L
    var i = 0
    while (i < k) {
      num = num * (n - i) % mod
      den = den * (i + 1) % mod
      i += 1
    }
    (num * modPow(den, mod - 2, mod) % mod).toInt
  }

  def countGoodArrays(n: Int, m: Int, k: Int): Int = {
    val mod = 1000000007
    (comb(n - 1, k, mod).toLong * m % mod * modPow(m - 1L, n - 1L - k, mod) % mod).toInt
  }
}
'''

FILES["3406_find_the_lexicographically_largest_string_from_the_box_ii"] = r'''// LeetCode 3406 - Find the Lexicographically Largest String From the Box II
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-ii/

object Solution {
  def answerString(word: String, numFriends: Int): String = {
    if (numFriends == 1) return word
    val n = word.length
    val maxLen = n - (numFriends - 1)
    var ans = ""
    var i = 0
    while (i < n) {
      var end = i + maxLen
      if (end > n) end = n
      val cand = word.substring(i, end)
      if (cand.compareTo(ans) > 0) ans = cand
      i += 1
    }
    ans
  }
}
'''

FILES["3407_substring_matching_pattern"] = r'''// LeetCode 3407 - Substring Matching Pattern
// https://leetcode.com/problems/substring-matching-pattern/

object Solution {
  def hasMatch(s: String, p: String): Boolean = {
    val i = p.indexOf('*')
    val left = p.substring(0, i)
    val right = p.substring(i + 1)
    val li = s.indexOf(left)
    if (li < 0) return false
    s.indexOf(right, li + left.length) >= 0
  }
}
'''

FILES["3408_design_task_manager"] = r'''// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

class TaskManager(tasks: List[List[Int]]) {
  private case class Item(pri: Int, taskId: Int, userId: Int)
  private val h = new java.util.PriorityQueue[Item]((a: Item, b: Item) => {
    if (a.pri != b.pri) java.lang.Integer.compare(b.pri, a.pri)
    else java.lang.Integer.compare(b.taskId, a.taskId)
  })
  private val pri = scala.collection.mutable.Map.empty[Int, Int]
  private val user = scala.collection.mutable.Map.empty[Int, Int]

  tasks.foreach { t => add(t(0), t(1), t(2)) }

  def add(userId: Int, taskId: Int, priority: Int): Unit = {
    pri(taskId) = priority
    user(taskId) = userId
    h.offer(Item(priority, taskId, userId))
  }

  def edit(taskId: Int, newPriority: Int): Unit = {
    pri(taskId) = newPriority
    h.offer(Item(newPriority, taskId, user(taskId)))
  }

  def rmv(taskId: Int): Unit = {
    pri.remove(taskId)
    user.remove(taskId)
  }

  def execTop(): Int = {
    while (!h.isEmpty) {
      val top = h.poll()
      val p = pri.get(top.taskId)
      if (p.isDefined && p.get == top.pri && user.get(top.taskId).contains(top.userId)) {
        pri.remove(top.taskId)
        val uid = user.remove(top.taskId).get
        return uid
      }
    }
    -1
  }
}
'''

FILES["3409_longest_subsequence_with_decreasing_adjacent_difference"] = r'''// LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
// https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

object Solution {
  def longestSubsequence(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 1
    val dp = Array.fill(n, 301)(0)
    var i = 0
    while (i < n) {
      var j = 0
      while (j < i) {
        val d = math.abs(nums(i) - nums(j))
        var best = 1
        var pd = d
        while (pd <= 300) {
          if (dp(j)(pd) > best) best = dp(j)(pd)
          pd += 1
        }
        if (best + 1 > dp(i)(d)) dp(i)(d) = best + 1
        if (dp(i)(d) > ans) ans = dp(i)(d)
        j += 1
      }
      if (dp(i)(0) < 1) dp(i)(0) = 1
      i += 1
    }
    ans
  }
}
'''

FILES["3410_maximize_subarray_sum_after_removing_all_occurrences_of_one_element"] = r'''// LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

object Solution {
  private def kadane(a: Seq[Int]): Long = {
    var best = -(1L << 62)
    var cur = 0L
    a.foreach { x =>
      cur += x
      if (cur > best) best = cur
      if (cur < 0) cur = 0
    }
    var allNeg = true
    var mx = a.head
    a.foreach { x =>
      if (x > mx) mx = x
      if (x >= 0) allNeg = false
    }
    if (allNeg) mx else best
  }

  def maxSubarraySum(nums: Array[Int]): Long = {
    var ans = kadane(nums)
    val uniq = scala.collection.mutable.Set.empty[Int]
    nums.foreach { x => if (x < 0) uniq += x }
    uniq.foreach { v =>
      val b = nums.filter(_ != v)
      if (b.nonEmpty) {
        val cand = kadane(b)
        if (cand > ans) ans = cand
      }
    }
    ans
  }
}
'''

FILES["3411_maximum_subarray_with_equal_products"] = r'''// LeetCode 3411 - Maximum Subarray With Equal Products
// https://leetcode.com/problems/maximum-subarray-with-equal-products/

object Solution {
  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  def maxLength(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 1
    var i = 0
    while (i < n) {
      var prod = 1L
      var g = 0
      var l = 1
      var j = i
      var stop = false
      while (j < n && !stop) {
        if (prod > 1000000000L / nums(j)) stop = true
        else {
          prod *= nums(j)
          if (g == 0) {
            g = nums(j)
            l = nums(j)
          } else {
            g = gcd(g, nums(j))
            l = l / gcd(l, nums(j)) * nums(j)
          }
          if (prod == l.toLong * g && j - i + 1 > ans) ans = j - i + 1
          j += 1
        }
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3412_find_mirror_score_of_a_string"] = r'''// LeetCode 3412 - Find Mirror Score of a String
// https://leetcode.com/problems/find-mirror-score-of-a-string/

object Solution {
  def calculateScore(s: String): Long = {
    val stacks = Array.fill(26)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var ans = 0L
    var i = 0
    while (i < s.length) {
      val ci = s.charAt(i) - 'a'
      val mir = 25 - ci
      if (stacks(mir).nonEmpty) {
        val j = stacks(mir).remove(stacks(mir).length - 1)
        ans += i - j
      } else {
        stacks(ci) += i
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3413_maximum_coins_from_k_consecutive_bags"] = r'''// LeetCode 3413 - Maximum Coins From K Consecutive Bags
// https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

object Solution {
  def maximumCoins(coins: Array[Array[Int]], k: Int): Long = {
    java.util.Arrays.sort(coins, (a: Array[Int], b: Array[Int]) => java.lang.Integer.compare(a(0), b(0)))
    var ans = 0L
    val n = coins.length
    var i = 0
    while (i < n) {
      var sum = 0L
      val start = coins(i)(0)
      val end = start + k - 1
      var j = i
      while (j < n && coins(j)(0) <= end) {
        var l = coins(j)(0)
        var r = coins(j)(1)
        if (r > end) r = end
        if (l < start) l = start
        if (l <= r) sum += (r - l + 1).toLong * coins(j)(2)
        j += 1
      }
      if (sum > ans) ans = sum
      i += 1
    }
    i = 0
    while (i < n) {
      var sum = 0L
      val end = coins(i)(1)
      val start = end - k + 1
      var j = 0
      while (j <= i) {
        var l = coins(j)(0)
        var r = coins(j)(1)
        if (l < start) l = start
        if (r > end) r = end
        if (l <= r) sum += (r - l + 1).toLong * coins(j)(2)
        j += 1
      }
      if (sum > ans) ans = sum
      i += 1
    }
    ans
  }
}
'''

FILES["3414_maximum_score_of_non_overlapping_intervals"] = r'''// LeetCode 3414 - Maximum Score of Non-overlapping Intervals
// https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

object Solution {
  private case class It(l: Int, r: Int, w: Int, i: Int)
  private class State(var score: Long = 0, var idx: java.util.ArrayList[Integer] = new java.util.ArrayList[Integer]()) {
    def copy(): State = {
      val s = new State(score)
      s.idx = new java.util.ArrayList[Integer](idx)
      s
    }
  }

  private def better(a: State, b: State): State = {
    if (a.score != b.score) return if (a.score > b.score) a else b
    val n = math.min(a.idx.size, b.idx.size)
    var i = 0
    while (i < n) {
      if (!a.idx.get(i).equals(b.idx.get(i))) return if (a.idx.get(i) < b.idx.get(i)) a else b
      i += 1
    }
    if (a.idx.size <= b.idx.size) a else b
  }

  def maximumWeight(intervals: Array[Array[Int]]): Array[Int] = {
    val n = intervals.length
    val arr = Array.tabulate(n)(i => It(intervals(i)(0), intervals(i)(1), intervals(i)(2), i))
    java.util.Arrays.sort(arr, (a: It, b: It) => java.lang.Integer.compare(a.r, b.r))
    val dp = Array.tabulate(n + 1, 5)((_, _) => new State())
    var i = 1
    while (i <= n) {
      val cur = arr(i - 1)
      var t = 0
      while (t <= 4) {
        dp(i)(t) = dp(i - 1)(t).copy()
        t += 1
      }
      var lo = 0
      var hi = i - 1
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (arr(mid).r < cur.l) lo = mid + 1
        else hi = mid
      }
      val prev = lo
      t = 1
      while (t <= 4) {
        val prevState = dp(prev)(t - 1)
        val cand = prevState.copy()
        cand.score = prevState.score + cur.w
        cand.idx.add(cur.i)
        java.util.Collections.sort(cand.idx)
        dp(i)(t) = better(dp(i)(t), cand)
        t += 1
      }
      i += 1
    }
    var best = dp(n)(0)
    t = 1
    while (t <= 4) {
      best = better(best, dp(n)(t))
      t += 1
    }
    Array.tabulate(best.idx.size)(i => best.idx.get(i).intValue())
  }
}
'''

FILES["3416_subsequences_with_a_unique_middle_mode_ii"] = r'''// LeetCode 3416 - Subsequences with a Unique Middle Mode II
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-ii/

object Solution {
  private def uniqueMode(a: Array[Int]): Boolean = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    a.foreach { x => freq(x) = freq.getOrElse(x, 0) + 1 }
    var best = 0
    var cnt = 0
    freq.values.foreach { f =>
      if (f > best) { best = f; cnt = 1 }
      else if (f == best) cnt += 1
    }
    cnt == 1
  }

  def subsequencesWithMiddleMode(nums: Array[Int]): Int = {
    val mod = 1000000007
    val n = nums.length
    var ans = 0
    var mid = 2
    while (mid < n - 2) {
      var a = 0
      while (a < mid) {
        var b = a + 1
        while (b < mid) {
          var c = mid + 1
          while (c < n) {
            var d = c + 1
            while (d < n) {
              val seq = Array(nums(a), nums(b), nums(mid), nums(c), nums(d))
              if (uniqueMode(seq)) ans = (ans + 1) % mod
              d += 1
            }
            c += 1
          }
          b += 1
        }
        a += 1
      }
      mid += 1
    }
    ans
  }
}
'''

FILES["3417_zigzag_grid_traversal_with_skip"] = r'''// LeetCode 3417 - Zigzag Grid Traversal With Skip
// https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

object Solution {
  def zigzagTraversal(grid: Array[Array[Int]]): Array[Int] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var skip = false
    var i = 0
    while (i < grid.length) {
      val row = grid(i)
      if (i % 2 == 0) {
        row.foreach { v =>
          if (!skip) ans += v
          skip = !skip
        }
      } else {
        var j = row.length - 1
        while (j >= 0) {
          if (!skip) ans += row(j)
          skip = !skip
          j -= 1
        }
      }
      i += 1
    }
    ans.toArray
  }
}
'''

FILES["3418_maximum_amount_of_money_robot_can_earn"] = r'''// LeetCode 3418 - Maximum Amount of Money Robot Can Earn
// https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

object Solution {
  def maximumAmount(coins: Array[Array[Int]]): Int = {
    val m = coins.length
    val n = coins(0).length
    val neg = -(1 << 30)
    val dp = Array.fill(m, n, 3)(neg)
    if (coins(0)(0) < 0) {
      dp(0)(0)(0) = coins(0)(0)
      dp(0)(0)(1) = 0
      dp(0)(0)(2) = 0
    } else {
      dp(0)(0)(0) = coins(0)(0)
      dp(0)(0)(1) = coins(0)(0)
      dp(0)(0)(2) = coins(0)(0)
    }
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (!(i == 0 && j == 0)) {
          var k = 0
          while (k < 3) {
            var best = neg
            if (i > 0) best = math.max(best, dp(i - 1)(j)(k))
            if (j > 0) best = math.max(best, dp(i)(j - 1)(k))
            if (best != neg) {
              if (coins(i)(j) >= 0) dp(i)(j)(k) = best + coins(i)(j)
              else dp(i)(j)(k) = math.max(dp(i)(j)(k), best + coins(i)(j))
            }
            k += 1
          }
          k = 1
          while (k < 3) {
            var best = neg
            if (i > 0) best = math.max(best, dp(i - 1)(j)(k - 1))
            if (j > 0) best = math.max(best, dp(i)(j - 1)(k - 1))
            if (best != neg && coins(i)(j) < 0) dp(i)(j)(k) = math.max(dp(i)(j)(k), best)
            k += 1
          }
        }
        j += 1
      }
      i += 1
    }
    math.max(dp(m - 1)(n - 1)(0), math.max(dp(m - 1)(n - 1)(1), dp(m - 1)(n - 1)(2)))
  }
}
'''

FILES["3419_minimize_the_maximum_edge_weight_of_graph"] = r'''// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

object Solution {
  def minMaxWeight(n: Int, edges: Array[Array[Int]], threshold: Int): Int = {
    var lo = 1
    var hi = 1000001
    var ans = -1
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(n, edges, mid)) {
        ans = mid
        hi = mid
      } else lo = mid + 1
    }
    ans
  }

  private def ok(n: Int, edges: Array[Array[Int]], mid: Int): Boolean = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      if (e(2) <= mid) g(e(1)) += e(0)
    }
    val vis = Array.fill(n)(false)
    val q = new java.util.ArrayDeque[Integer]()
    q.offer(0)
    vis(0) = true
    var cnt = 1
    while (!q.isEmpty) {
      val u = q.poll()
      g(u).foreach { v =>
        if (!vis(v)) {
          vis(v) = true
          cnt += 1
          q.offer(v)
        }
      }
    }
    cnt == n
  }
}
'''

FILES["3420_count_non_decreasing_subarrays_after_k_operations"] = r'''// LeetCode 3420 - Count Non-Decreasing Subarrays After K Operations
// https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

object Solution {
  def countNonDecreasingSubarrays(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    var ans = 0L
    var i = 0
    while (i < n) {
      var cost = 0L
      var maxV = nums(i)
      var j = i
      var stop = false
      while (j < n && !stop) {
        if (nums(j) >= maxV) maxV = nums(j)
        else cost += maxV - nums(j)
        if (cost > k) stop = true
        else ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3422_minimum_operations_to_make_subarray_elements_equal"] = r'''// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    var ans = 1L << 62
    var i = 0
    while (i + k <= n) {
      val sub = java.util.Arrays.copyOfRange(nums, i, i + k)
      java.util.Arrays.sort(sub)
      val med = sub(k / 2)
      var cost = 0L
      sub.foreach { x => cost += math.abs(x - med) }
      if (cost < ans) ans = cost
      i += 1
    }
    ans
  }
}
'''

for folder, text in FILES.items():
    path = ROOT / folder / "Solution.scala"
    path.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", folder)
print("count", len(FILES))
