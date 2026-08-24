#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3344_maximum_sized_array"] = """// LeetCode 3344 - Maximum Sized Array
// https://leetcode.com/problems/maximum-sized-array/

object Solution {
  private def ok(n: Long, s: Long): Boolean = {
    var sum = 0L
    var i = 0L
    while (i < n) {
      var j = 0L
      while (j < n) {
        val ij = i | j
        sum += ij * (n - 1) * n / 2
        if (sum > s) return false
        j += 1
      }
      i += 1
    }
    sum <= s
  }

  def maxSizedArray(s: Long): Int = {
    var lo = 1L
    var hi = 2000L
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(mid, s)) lo = mid
      else hi = mid - 1
    }
    lo.toInt
  }
}
"""

FILES["3345_smallest_divisible_digit_product_i"] = """// LeetCode 3345 - Smallest Divisible Digit Product I
// https://leetcode.com/problems/smallest-divisible-digit-product-i/

object Solution {
  def smallestNumber(n: Int, t: Int): Int = {
    var x = n
    while (true) {
      var p = 1
      var y = x
      while (y > 0) {
        p *= y % 10
        y /= 10
      }
      if (p % t == 0) return x
      x += 1
    }
    n
  }
}
"""

FILES["3346_maximum_frequency_of_an_element_after_performing_operations_i"] = """// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

object Solution {
  private def lowerBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) < x) lo = mid + 1 else hi = mid
    }
    lo
  }
  private def upperBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) <= x) lo = mid + 1 else hi = mid
    }
    lo
  }

  def maxFrequency(nums: Array[Int], k: Int, numOperations: Int): Int = {
    scala.util.Sorting.quickSort(nums)
    val n = nums.length
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) freq(x) = freq.getOrElse(x, 0) + 1
    var ans = 1
    for ((t, f) <- freq) {
      val lo = lowerBound(nums, t - k)
      val hi = upperBound(nums, t + k)
      val can = hi - lo
      val use = math.min(can, f + numOperations)
      if (use > ans) ans = use
    }
    var l = 0
    var r = 0
    while (r < n) {
      while (nums(r) - nums(l) > 2 * k) l += 1
      val window = math.min(r - l + 1, numOperations)
      if (window > ans) ans = window
      r += 1
    }
    ans
  }
}
"""

FILES["3347_maximum_frequency_of_an_element_after_performing_operations_ii"] = """// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

object Solution {
  private def lowerBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) < x) lo = mid + 1 else hi = mid
    }
    lo
  }
  private def upperBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) <= x) lo = mid + 1 else hi = mid
    }
    lo
  }

  def maxFrequency(nums: Array[Int], k: Int, numOperations: Int): Int = {
    scala.util.Sorting.quickSort(nums)
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) freq(x) = freq.getOrElse(x, 0) + 1
    var ans = 1
    val candidates = scala.collection.mutable.ArrayBuffer.empty[Int]
    val seen = scala.collection.mutable.HashSet.empty[Int]
    for (x <- nums) {
      for (t <- Array(x - k, x, x + k)) {
        if (seen.add(t)) candidates += t
      }
    }
    for (t <- candidates) {
      val lo = lowerBound(nums, t - k)
      val hi = upperBound(nums, t + k)
      val can = hi - lo
      val f = freq.getOrElse(t, 0)
      val use = math.min(can, f + numOperations)
      if (use > ans) ans = use
    }
    ans
  }
}
"""

FILES["3348_smallest_divisible_digit_product_ii"] = """// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

object Solution {
  private def dfs(res: Array[Char], i: Int, tight: Boolean, sameLen: Boolean, num: String, t: Long): Boolean = {
    if (i == res.length) {
      var prod = 1L
      for (c <- res) {
        prod *= (c - '0')
        if (prod == 0) return false
      }
      return prod % t == 0 && prod > 0
    }
    var start = if (i == 0) '1' else '0'
    if (tight && sameLen && i < num.length) start = num.charAt(i)
    var c = start
    while (c <= '9') {
      res(i) = c
      val nt = tight && sameLen && i < num.length && c == num.charAt(i)
      if (dfs(res, i + 1, nt, sameLen, num, t)) return true
      c = (c + 1).toChar
    }
    false
  }

  def smallestNumber(num: String, t: Long): String = {
    var tt = t
    var d = 9
    while (d >= 2) {
      while (tt % d == 0) tt /= d
      d -= 1
    }
    if (tt > 1) return "-1"
    var extra = 0
    while (extra <= 60) {
      val L = num.length + extra
      val res = new Array[Char](L)
      if (dfs(res, 0, true, extra == 0, num, t)) return new String(res)
      extra += 1
    }
    "-1"
  }
}
"""

FILES["3349_adjacent_increasing_subarrays_detection_i"] = """// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

object Solution {
  def hasIncreasingSubarrays(nums: Array[Int], k: Int): Boolean = {
    val n = nums.length
    var i = 0
    while (i + 2 * k <= n) {
      if (inc(nums, i, k) && inc(nums, i + k, k)) return true
      i += 1
    }
    false
  }

  private def inc(nums: Array[Int], start: Int, k: Int): Boolean = {
    var i = start
    while (i + 1 < start + k) {
      if (nums(i) >= nums(i + 1)) return false
      i += 1
    }
    true
  }
}
"""

FILES["3350_adjacent_increasing_subarrays_detection_ii"] = """// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

object Solution {
  def maxIncreasingSubarrays(nums: Array[Int]): Int = {
    val n = nums.length
    val up = new Array[Int](n)
    up(n - 1) = 1
    var i = n - 2
    while (i >= 0) {
      up(i) = if (nums(i) < nums(i + 1)) up(i + 1) + 1 else 1
      i -= 1
    }
    var lo = 1
    var hi = n / 2
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(up, n, mid)) lo = mid
      else hi = mid - 1
    }
    lo
  }

  private def ok(up: Array[Int], n: Int, k: Int): Boolean = {
    var i = 0
    while (i + 2 * k <= n) {
      if (up(i) >= k && up(i + k) >= k) return true
      i += 1
    }
    false
  }
}
"""

FILES["3351_sum_of_good_subsequences"] = """// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

object Solution {
  def sumOfGoodSubsequences(nums: Array[Int]): Int = {
    val mod = 1000000007
    val cnt = scala.collection.mutable.HashMap.empty[Int, Int]
    val sum = scala.collection.mutable.HashMap.empty[Int, Int]
    var ans = 0
    for (x <- nums) {
      var c = 1
      var s = x
      if (cnt.getOrElse(x - 1, 0) > 0) {
        c = (c + cnt(x - 1)) % mod
        s = ((s.toLong + sum(x - 1) + cnt(x - 1).toLong * x % mod) % mod).toInt
      }
      if (cnt.getOrElse(x + 1, 0) > 0) {
        c = (c + cnt(x + 1)) % mod
        s = ((s.toLong + sum(x + 1) + cnt(x + 1).toLong * x % mod) % mod).toInt
      }
      cnt(x) = (cnt.getOrElse(x, 0) + c) % mod
      sum(x) = (sum.getOrElse(x, 0) + s) % mod
      ans = (ans + s) % mod
    }
    ans
  }
}
"""

FILES["3352_count_k_reducible_numbers_less_than_n"] = """// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

object Solution {
  private def bitsPop(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x > 0) { c += x & 1; x >>= 1 }
    c
  }

  def countKReducibleNumbers(s: String, k: Int): Int = {
    val mod = 1000000007
    val red = new Array[Int](801)
    red(1) = 0
    var i = 2
    while (i <= 800) {
      red(i) = 1 + red(bitsPop(i))
      i += 1
    }
    val memo = scala.collection.mutable.HashMap.empty[Long, Int]
    def key(pos: Int, tight: Int, ones: Int): Long =
      (pos.toLong << 32) | (tight.toLong << 16) | ones
    def dfs(pos: Int, tight: Boolean, ones: Int): Int = {
      if (pos == s.length) {
        if (ones == 0) return 0
        return if (red(ones) <= k - 1) 1 else 0
      }
      val ky = key(pos, if (tight) 1 else 0, ones)
      if (memo.contains(ky)) return memo(ky)
      val up = if (tight) s.charAt(pos) - '0' else 1
      var ans = 0
      var d = 0
      while (d <= up) {
        val nt = tight && d == up
        ans = (ans + dfs(pos + 1, nt, ones + d)) % mod
        d += 1
      }
      memo(ky) = ans
      ans
    }
    dfs(0, true, 0)
  }
}
"""

FILES["3353_minimum_total_operations"] = """// LeetCode 3353 - Minimum Total Operations
// https://leetcode.com/problems/minimum-total-operations/

object Solution {
  def minimumOperations(nums: Array[Int]): Int = {
    var ops = 0
    var i = nums.length - 2
    while (i >= 0) {
      if (nums(i) != nums(i + 1)) ops += 1
      i -= 1
    }
    ops
  }
}
"""

FILES["3354_make_array_elements_equal_to_zero"] = """// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

object Solution {
  def countValidSelections(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      if (nums(i) == 0) {
        for (dir <- Array(-1, 1)) {
          val a = nums.clone()
          var cur = i
          var d = dir
          while (cur >= 0 && cur < n) {
            if (a(cur) == 0) cur += d
            else {
              a(cur) -= 1
              d = -d
              cur += d
            }
          }
          var ok = true
          for (v <- a) if (v != 0) ok = false
          if (ok) ans += 1
        }
      }
      i += 1
    }
    ans
  }
}
"""

FILES["3355_zero_array_transformation_i"] = """// LeetCode 3355 - Zero Array Transformation I
// https://leetcode.com/problems/zero-array-transformation-i/

object Solution {
  def isZeroArray(nums: Array[Int], queries: Array[Array[Int]]): Boolean = {
    val n = nums.length
    val diff = new Array[Int](n + 1)
    for (q <- queries) {
      diff(q(0)) += 1
      diff(q(1) + 1) -= 1
    }
    var cur = 0
    var i = 0
    while (i < n) {
      cur += diff(i)
      if (cur < nums(i)) return false
      i += 1
    }
    true
  }
}
"""

FILES["3356_zero_array_transformation_ii"] = """// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

object Solution {
  def minZeroArray(nums: Array[Int], queries: Array[Array[Int]]): Int = {
    val n = nums.length
    if (ok(0, nums, queries, n)) return 0
    var lo = 1
    var hi = queries.length + 1
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (mid <= queries.length && ok(mid, nums, queries, n)) hi = mid
      else lo = mid + 1
    }
    if (lo > queries.length) -1 else lo
  }

  private def ok(k: Int, nums: Array[Int], queries: Array[Array[Int]], n: Int): Boolean = {
    val diff = new Array[Long](n + 1)
    var i = 0
    while (i < k) {
      val q = queries(i)
      diff(q(0)) += q(2)
      diff(q(1) + 1) -= q(2)
      i += 1
    }
    var cur = 0L
    i = 0
    while (i < n) {
      cur += diff(i)
      if (cur < nums(i)) return false
      i += 1
    }
    true
  }
}
"""

FILES["3357_minimize_the_maximum_adjacent_element_difference"] = """// LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

object Solution {
  def minDifference(nums: Array[Int]): Int = {
    val n = nums.length
    var lo = 0
    var hi = 1000000000
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(mid, nums, n)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(d: Int, nums: Array[Int], n: Int): Boolean = {
    var prev = -1
    var i = 0
    while (i < n) {
      if (nums(i) != -1) {
        if (prev != -1 && math.abs(nums(i) - prev) > d) return false
        prev = nums(i)
      } else {
        var j = i
        while (j < n && nums(j) == -1) j += 1
        val left = prev
        val right = if (j < n) nums(j) else -1
        val gap = j - i
        if (left == -1 && right == -1) return true
        if (left == -1 || right == -1) {
          prev = -1
          i = j - 1
        } else {
          if (math.abs(left - right) > d.toLong * (gap + 1)) return false
          prev = -1
          i = j - 1
        }
      }
      i += 1
    }
    true
  }
}
"""

FILES["3359_find_sorted_submatrices_with_maximum_element_at_most_k"] = """// LeetCode 3359 - Find Sorted Submatrices With Maximum Element at Most K
// https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/

object Solution {
  def countSortedMatrices(grid: Array[Array[Int]], k: Int): Long = {
    val m = grid.length
    val n = grid(0).length
    var ans = 0L
    var r1 = 0
    while (r1 < m) {
      var r2 = r1
      while (r2 < m) {
        var c1 = 0
        while (c1 < n) {
          var c2 = c1
          while (c2 < n) {
            var ok = true
            var i = r1
            while (i <= r2 && ok) {
              var j = c1
              while (j <= c2 && ok) {
                if (grid(i)(j) > k) ok = false
                else if (j > c1 && grid(i)(j) < grid(i)(j - 1)) ok = false
                else if (i > r1 && grid(i)(j) < grid(i - 1)(j)) ok = false
                j += 1
              }
              i += 1
            }
            if (ok) ans += 1
            c2 += 1
          }
          c1 += 1
        }
        r2 += 1
      }
      r1 += 1
    }
    ans
  }
}
"""

FILES["3360_stone_removal_game"] = """// LeetCode 3360 - Stone Removal Game
// https://leetcode.com/problems/stone-removal-game/

object Solution {
  def canAliceWin(n: Int): Boolean = {
    var nn = n
    var take = 10
    var alice = true
    while (nn >= take && take > 0) {
      nn -= take
      take -= 1
      alice = !alice
    }
    !alice
  }
}
"""

FILES["3361_shift_distance_between_two_strings"] = """// LeetCode 3361 - Shift Distance Between Two Strings
// https://leetcode.com/problems/shift-distance-between-two-strings/

object Solution {
  def shiftDistance(s: String, t: String, nextCost: Array[Int], previousCost: Array[Int]): Long = {
    var ans = 0L
    var i = 0
    while (i < s.length) {
      val a = s.charAt(i) - 'a'
      val b = t.charAt(i) - 'a'
      if (a != b) {
        var fwd = 0L
        var x = a
        while (x != b) {
          fwd += nextCost(x)
          x = (x + 1) % 26
        }
        var bwd = 0L
        x = a
        while (x != b) {
          bwd += previousCost(x)
          x = (x + 25) % 26
        }
        ans += (if (fwd < bwd) fwd else bwd)
      }
      i += 1
    }
    ans
  }
}
"""

FILES["3362_zero_array_transformation_iii"] = """// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

object Solution {
  def maxRemoval(nums: Array[Int], queries: Array[Array[Int]]): Int = {
    val qs = queries.sortBy(_(0))
    val h = new java.util.PriorityQueue[Int]((a: Int, b: Int) => Integer.compare(b, a))
    val n = nums.length
    val diff = new Array[Int](n + 1)
    var j = 0
    var used = 0
    var cur = 0
    var i = 0
    while (i < n) {
      cur += diff(i)
      while (j < qs.length && qs(j)(0) == i) {
        h.offer(qs(j)(1))
        j += 1
      }
      while (cur < nums(i)) {
        if (h.isEmpty || h.peek() < i) return -1
        val r = h.poll()
        cur += 1
        diff(r + 1) -= 1
        used += 1
      }
      i += 1
    }
    qs.length - used
  }
}
"""

FILES["3363_find_the_maximum_number_of_fruits_collected"] = """// LeetCode 3363 - Find the Maximum Number of Fruits Collected
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

object Solution {
  def maxCollectedFruits(fruits: Array[Array[Int]]): Int = {
    val n = fruits.length
    var ans = 0
    var i = 0
    while (i < n) {
      ans += fruits(i)(i)
      fruits(i)(i) = 0
      i += 1
    }
    val neg = -(1 << 30)
    val dp2 = Array.fill(n, n)(neg)
    val dp3 = Array.fill(n, n)(neg)
    dp2(0)(n - 1) = fruits(0)(n - 1)
    i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (dp2(i)(j) != neg) {
          for (dj <- Array(-1, 0, 1)) {
            val ni = i + 1
            val nj = j + dj
            if (ni < n && nj >= 0 && nj < n && nj > ni) {
              val v = dp2(i)(j) + fruits(ni)(nj)
              if (v > dp2(ni)(nj)) dp2(ni)(nj) = v
            }
          }
        }
        j += 1
      }
      i += 1
    }
    dp3(n - 1)(0) = fruits(n - 1)(0)
    var j = 0
    while (j < n) {
      i = 0
      while (i < n) {
        if (dp3(i)(j) != neg) {
          for (di <- Array(-1, 0, 1)) {
            val ni = i + di
            val nj = j + 1
            if (ni >= 0 && ni < n && nj < n && ni > nj) {
              val v = dp3(i)(j) + fruits(ni)(nj)
              if (v > dp3(ni)(nj)) dp3(ni)(nj) = v
            }
          }
        }
        i += 1
      }
      j += 1
    }
    ans += dp2(n - 1)(n - 1) + dp3(n - 1)(n - 1)
    ans
  }
}
"""

FILES["3364_minimum_positive_sum_subarray"] = """// LeetCode 3364 - Minimum Positive Sum Subarray
// https://leetcode.com/problems/minimum-positive-sum-subarray/

object Solution {
  def minimumSumSubarray(nums: Array[Int], l: Int, r: Int): Int = {
    val n = nums.length
    val pref = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + nums(i)
      i += 1
    }
    var ans = Int.MaxValue
    var found = false
    i = 0
    while (i < n) {
      var length = l
      while (length <= r && i + length <= n) {
        val s = pref(i + length) - pref(i)
        if (s > 0 && s < ans) {
          ans = s
          found = true
        }
        length += 1
      }
      i += 1
    }
    if (found) ans else -1
  }
}
"""

FILES["3365_rearrange_k_substrings_to_form_target_string"] = """// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

object Solution {
  def isPossibleToRearrange(s: String, t: String, k: Int): Boolean = {
    val n = s.length
    val sz = n / k
    val cnt = scala.collection.mutable.HashMap.empty[String, Int]
    var i = 0
    while (i < n) {
      val a = s.substring(i, i + sz)
      val b = t.substring(i, i + sz)
      cnt(a) = cnt.getOrElse(a, 0) + 1
      cnt(b) = cnt.getOrElse(b, 0) - 1
      i += sz
    }
    cnt.values.forall(_ == 0)
  }
}
"""

FILES["3366_minimum_array_sum"] = """// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

object Solution {
  def minArraySum(nums: Array[Int], k: Int, op1: Int, op2: Int): Int = {
    val inf = 1000000000000000000L
    var dp = Array.fill(op1 + 1, op2 + 1)(inf)
    dp(0)(0) = 0
    def tryCand(ndp: Array[Array[Long]], base: Long, na: Int, nb: Int, v: Int): Unit = {
      if (base + v < ndp(na)(nb)) ndp(na)(nb) = base + v
    }
    for (x <- nums) {
      val ndp = Array.fill(op1 + 1, op2 + 1)(inf)
      var a = 0
      while (a <= op1) {
        var b = 0
        while (b <= op2) {
          if (dp(a)(b) != inf) {
            tryCand(ndp, dp(a)(b), a, b, x)
            if (a < op1) tryCand(ndp, dp(a)(b), a + 1, b, (x + 1) / 2)
            if (b < op2 && x >= k) tryCand(ndp, dp(a)(b), a, b + 1, x - k)
            if (a < op1 && b < op2) {
              val v1 = (x + 1) / 2
              if (v1 >= k) tryCand(ndp, dp(a)(b), a + 1, b + 1, v1 - k)
              if (x >= k) tryCand(ndp, dp(a)(b), a + 1, b + 1, (x - k + 1) / 2)
            }
          }
          b += 1
        }
        a += 1
      }
      dp = ndp
    }
    var ans = inf
    var a = 0
    while (a <= op1) {
      var b = 0
      while (b <= op2) {
        if (dp(a)(b) < ans) ans = dp(a)(b)
        b += 1
      }
      a += 1
    }
    ans.toInt
  }
}
"""

FILES["3367_maximize_sum_of_weights_after_edge_removals"] = """// LeetCode 3367 - Maximize Sum of Weights after Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

object Solution {
  def maximizeSumOfWeights(edges: Array[Array[Int]], k: Int): Long = {
    val n = edges.length + 1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    for (e <- edges) {
      g(e(0)) += ((e(1), e(2)))
      g(e(1)) += ((e(0), e(2)))
    }
    def dfs(u: Int, p: Int): Array[Long] = {
      var base = 0L
      val gains = scala.collection.mutable.ArrayBuffer.empty[Long]
      for ((to, w) <- g(u)) {
        if (to != p) {
          val child = dfs(to, u)
          base += child(1)
          val gain = child(0) + w - child(1)
          if (gain > 0) gains += gain
        }
      }
      val sorted = gains.sorted.reverse
      var withP = base
      var without = base
      var i = 0
      while (i < sorted.length && i < k - 1) {
        withP += sorted(i)
        i += 1
      }
      i = 0
      while (i < sorted.length && i < k) {
        without += sorted(i)
        i += 1
      }
      Array(withP, without)
    }
    dfs(0, -1)(1)
  }
}
"""

FILES["3369_design_an_array_statistics_tracker"] = """// LeetCode 3369 - Design an Array Statistics Tracker
// https://leetcode.com/problems/design-an-array-statistics-tracker/

class StatisticsTracker() {
  private val arr = scala.collection.mutable.ArrayBuffer.empty[Int]
  private var sum = 0L
  private val freq = scala.collection.mutable.HashMap.empty[Int, Int]
  private var modeFreq = 0
  private val modes = scala.collection.mutable.HashSet.empty[Int]

  def addNumber(num: Int): Unit = {
    arr += num
    sum += num
    val f = freq.getOrElse(num, 0) + 1
    freq(num) = f
    if (f > modeFreq) {
      modeFreq = f
      modes.clear()
      modes += num
    } else if (f == modeFreq) {
      modes += num
    }
  }

  def removeFirst(): Unit = {
    if (arr.isEmpty) return
    val num = arr.remove(0)
    sum -= num
    val f = freq(num) - 1
    if (f == 0) freq.remove(num)
    else freq(num) = f
    modeFreq = 0
    modes.clear()
    for ((v, ff) <- freq) {
      if (ff > modeFreq) {
        modeFreq = ff
        modes.clear()
        modes += v
      } else if (ff == modeFreq) {
        modes += v
      }
    }
  }

  def getMean(): Int = {
    if (arr.isEmpty) 0
    else (sum / arr.length).toInt
  }

  def getMedian(): Int = {
    val n = arr.length
    val tmp = arr.sorted
    if (n % 2 == 1) tmp(n / 2) else tmp(n / 2 - 1)
  }

  def getMode(): Int = {
    var best = Long.MaxValue
    for (v <- modes) if (v < best) best = v
    if (best == Long.MaxValue) 0 else best.toInt
  }
}
"""

FILES["3370_smallest_number_with_all_set_bits"] = """// LeetCode 3370 - Smallest Number With All Set Bits
// https://leetcode.com/problems/smallest-number-with-all-set-bits/

object Solution {
  def smallestNumber(n: Int): Int = {
    var x = 1
    while (x < n) x = x * 2 + 1
    x
  }
}
"""

FILES["3371_identify_the_largest_outlier_in_an_array"] = """// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

object Solution {
  def getLargestOutlier(nums: Array[Int]): Int = {
    var sum = 0
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) {
      sum += x
      freq(x) = freq.getOrElse(x, 0) + 1
    }
    var ans = Int.MinValue
    for (x <- nums) {
      freq(x) = freq(x) - 1
      val rem = sum - x
      if (rem % 2 == 0) {
        val cand = rem / 2
        if (freq.getOrElse(cand, 0) > 0 && x > ans) ans = x
      }
      freq(x) = freq(x) + 1
    }
    ans
  }
}
"""

def main() -> None:
    written = 0
    for folder, text in FILES.items():
        path = ROOT / folder / "Solution.scala"
        path.write_text(text, encoding="utf-8", newline="\n")
        if text.startswith("\ufeff"):
            raise SystemExit(f"BOM in {folder}")
        written += 1
        print(f"wrote {folder}")
    print(f"batch_c written={written}")

if __name__ == "__main__":
    main()
