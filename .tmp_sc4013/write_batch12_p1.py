#!/usr/bin/env python3
"""Write Scala solutions for batch_12 folders 2832-2868."""
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2832_maximal_range_that_each_element_is_maximum_in_it"] = r'''// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

object Solution {
  def maximumLength(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val left = Array.fill(n)(0)
    val right = Array.fill(n)(0)
    val st = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (i <- 0 until n) {
      while (st.nonEmpty && nums(st.last) < nums(i)) st.remove(st.length - 1)
      left(i) = if (st.isEmpty) -1 else st.last
      st += i
    }
    st.clear()
    for (i <- n - 1 to 0 by -1) {
      while (st.nonEmpty && nums(st.last) <= nums(i)) st.remove(st.length - 1)
      right(i) = if (st.isEmpty) n else st.last
      st += i
    }
    Array.tabulate(n)(i => right(i) - left(i) - 1)
  }
}
'''

FILES["2833_furthest_point_from_origin"] = r'''// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

object Solution {
  def furthestDistanceFromOrigin(moves: String): Int = {
    var L = 0
    var R = 0
    var u = 0
    moves.foreach { c =>
      if (c == 'L') L += 1
      else if (c == 'R') R += 1
      else u += 1
    }
    math.abs(L - R) + u
  }
}
'''

FILES["2834_find_the_minimum_possible_sum_of_a_beautiful_array"] = r'''// LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
// https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

object Solution {
  def minimumPossibleSum(n: Int, target: Int): Int = {
    val MOD = 1000000007
    val m = target / 2
    if (n <= m) return (1L * n * (n + 1) / 2 % MOD).toInt
    var sum = 1L * m * (m + 1) / 2
    val remain = n - m
    sum += 1L * remain * target + 1L * remain * (remain - 1) / 2
    (sum % MOD).toInt
  }
}
'''

FILES["2835_minimum_operations_to_form_subsequence_with_target_sum"] = r'''// LeetCode 2835 - Minimum Operations to Form Subsequence With Target Sum
// https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

object Solution {
  def minOperations(nums: Array[Int], target: Int): Int = {
    val cnt = Array.fill(32)(0)
    var sum = 0L
    nums.foreach { v =>
      sum += v
      var b = 0
      while ((1 << b) < v) b += 1
      cnt(b) += 1
    }
    if (sum < target) return -1
    var ans = 0
    for (i <- 0 until 31) {
      if ((target & (1 << i)) != 0) {
        if (cnt(i) > 0) cnt(i) -= 1
        else {
          var j = i + 1
          while (j < 32 && cnt(j) == 0) j += 1
          if (j == 32) return -1
          while (j > i) {
            cnt(j) -= 1
            cnt(j - 1) += 2
            ans += 1
            j -= 1
          }
          cnt(i) -= 1
        }
      }
      cnt(i + 1) += cnt(i) / 2
    }
    ans
  }
}
'''

FILES["2836_maximize_value_of_function_in_a_ball_passing_game"] = r'''// LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

object Solution {
  def getMaxFunctionValue(receiver: Array[Int], k: Long): Long = {
    val n = receiver.length
    val LOG = 36
    val up = Array.ofDim[Int](LOG, n)
    val sum = Array.ofDim[Long](LOG, n)
    for (i <- 0 until n) {
      up(0)(i) = receiver(i)
      sum(0)(i) = receiver(i)
    }
    for (j <- 1 until LOG) {
      for (i <- 0 until n) {
        val mid = up(j - 1)(i)
        up(j)(i) = up(j - 1)(mid)
        sum(j)(i) = sum(j - 1)(i) + sum(j - 1)(mid)
      }
    }
    var ans = 0L
    for (i <- 0 until n) {
      var cur = i
      var total = i.toLong
      var kk = k
      for (j <- 0 until LOG) {
        if ((kk & (1L << j)) != 0) {
          total += sum(j)(cur)
          cur = up(j)(cur)
        }
      }
      ans = math.max(ans, total)
    }
    ans
  }
}
'''

FILES["2838_maximum_coins_heroes_can_collect"] = r'''// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/

object Solution {
  def maximumCoins(heroes: Array[Int], monsters: Array[Int], coins: Array[Int]): Array[Long] = {
    val n = monsters.length
    val idx = (0 until n).toArray.sortBy(monsters)
    val pref = Array.fill(n + 1)(0L)
    val ms = Array.fill(n)(0)
    for (i <- 0 until n) {
      ms(i) = monsters(idx(i))
      pref(i + 1) = pref(i) + coins(idx(i))
    }
    heroes.map { h =>
      pref(upperBound(ms, h))
    }
  }

  private def upperBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (a(mid) <= x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
'''

FILES["2839_check_if_strings_can_be_made_equal_with_operations_i"] = r'''// LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

object Solution {
  def canBeEqual(s1: String, s2: String): Boolean = {
    val a = Array(s1.charAt(0), s1.charAt(2)).sorted
    val b = Array(s2.charAt(0), s2.charAt(2)).sorted
    val c = Array(s1.charAt(1), s1.charAt(3)).sorted
    val d = Array(s2.charAt(1), s2.charAt(3)).sorted
    a.sameElements(b) && c.sameElements(d)
  }
}
'''

FILES["2840_check_if_strings_can_be_made_equal_with_operations_ii"] = r'''// LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

object Solution {
  def checkStrings(s1: String, s2: String): Boolean = {
    val even1 = Array.fill(26)(0)
    val odd1 = Array.fill(26)(0)
    val even2 = Array.fill(26)(0)
    val odd2 = Array.fill(26)(0)
    for (i <- s1.indices) {
      if (i % 2 == 0) {
        even1(s1.charAt(i) - 'a') += 1
        even2(s2.charAt(i) - 'a') += 1
      } else {
        odd1(s1.charAt(i) - 'a') += 1
        odd2(s2.charAt(i) - 'a') += 1
      }
    }
    even1.sameElements(even2) && odd1.sameElements(odd2)
  }
}
'''

FILES["2841_maximum_sum_of_almost_unique_subarray"] = r'''// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

object Solution {
  def maxSum(nums: Array[Int], m: Int, k: Int): Long = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var sum = 0L
    var ans = 0L
    for (i <- nums.indices) {
      freq(nums(i)) = freq.getOrElse(nums(i), 0) + 1
      sum += nums(i)
      if (i >= k) {
        val out = nums(i - k)
        sum -= out
        val c = freq(out) - 1
        if (c == 0) freq.remove(out) else freq(out) = c
      }
      if (i >= k - 1 && freq.size >= m) ans = math.max(ans, sum)
    }
    ans
  }
}
'''

FILES["2842_count_k_subsequences_of_a_string_with_maximum_beauty"] = r'''// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

object Solution {
  private val MOD = 1000000007

  def countKSubsequencesWithMaxBeauty(s: String, k: Int): Int = {
    val freq = Array.fill(26)(0)
    s.foreach(c => freq(c - 'a') += 1)
    val vals = freq.filter(_ > 0).toBuffer
    if (vals.length < k) return 0
    val sorted = vals.sorted(Ordering[Int].reverse)
    val threshold = sorted(k - 1)
    var need = 0
    var avail = 0
    var prod = 1L
    sorted.foreach { v =>
      if (v > threshold) {
        prod = prod * v % MOD
        need += 1
      } else if (v == threshold) avail += 1
    }
    val remain = k - need
    prod = prod * comb(avail, remain) % MOD
    for (_ <- 0 until remain) prod = prod * threshold % MOD
    prod.toInt
  }

  private def modPow(a0: Long, b0: Long): Long = {
    var res = 1L
    var a = a0 % MOD
    var b = b0
    while (b > 0) {
      if ((b & 1) != 0) res = res * a % MOD
      a = a * a % MOD
      b >>= 1
    }
    res
  }

  private def comb(n: Int, r: Int): Long = {
    if (r < 0 || r > n) return 0
    var num = 1L
    var den = 1L
    for (i <- 0 until r) {
      num = num * (n - i) % MOD
      den = den * (i + 1) % MOD
    }
    num * modPow(den, MOD - 2) % MOD
  }
}
'''

FILES["2843_count_symmetric_integers"] = r'''// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

object Solution {
  def countSymmetricIntegers(low: Int, high: Int): Int = {
    var ans = 0
    for (x <- low to high) {
      val s = x.toString
      if (s.length % 2 == 0) {
        val mid = s.length / 2
        var a = 0
        var b = 0
        for (i <- 0 until mid) {
          a += s.charAt(i) - '0'
          b += s.charAt(mid + i) - '0'
        }
        if (a == b) ans += 1
      }
    }
    ans
  }
}
'''

FILES["2844_minimum_operations_to_make_a_special_number"] = r'''// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

object Solution {
  def minimumOperations(num: String): Int = {
    val n = num.length
    var ans = n
    if (num.contains('0')) ans = math.min(ans, n - 1)
    val targets = Array("00", "25", "50", "75")
    targets.foreach { t =>
      var j = n - 1
      while (j >= 0 && num.charAt(j) != t.charAt(1)) j -= 1
      if (j >= 0) {
        var i = j - 1
        while (i >= 0 && num.charAt(i) != t.charAt(0)) i -= 1
        if (i >= 0) ans = math.min(ans, n - i - 2)
      }
    }
    ans
  }
}
'''

FILES["2845_count_of_interesting_subarrays"] = r'''// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

object Solution {
  def countInterestingSubarrays(nums: Array[Int], modulo: Int, k: Int): Long = {
    val freq = scala.collection.mutable.Map(0 -> 1)
    var ans = 0L
    var pref = 0
    nums.foreach { v =>
      if (v % modulo == k) pref += 1
      var need = (pref - k) % modulo
      if (need < 0) need += modulo
      ans += freq.getOrElse(need, 0)
      val key = pref % modulo
      freq(key) = freq.getOrElse(key, 0) + 1
    }
    ans
  }
}
'''

FILES["2846_minimum_edge_weight_equilibrium_queries_in_a_tree"] = r'''// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

object Solution {
  private val LOG = 15
  private var g: Array[scala.collection.mutable.ArrayBuffer[Array[Int]]] = _
  private var up: Array[Array[Int]] = _
  private var depth: Array[Int] = _
  private var cnt: Array[Array[Int]] = _

  def minOperationsQueries(n: Int, edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Array[Int]])
    edges.foreach { e =>
      g(e(0)) += Array(e(1), e(2))
      g(e(1)) += Array(e(0), e(2))
    }
    up = Array.ofDim[Int](LOG, n)
    depth = Array.fill(n)(0)
    cnt = Array.ofDim[Int](n, 27)
    dfs(0, 0)
    for (j <- 1 until LOG; i <- 0 until n) up(j)(i) = up(j - 1)(up(j - 1)(i))
    queries.map { q =>
      val a = q(0)
      val b = q(1)
      val c = lca(a, b)
      val total = depth(a) + depth(b) - 2 * depth(c)
      var best = 0
      for (w <- 1 to 26) {
        val f = cnt(a)(w) + cnt(b)(w) - 2 * cnt(c)(w)
        best = math.max(best, f)
      }
      total - best
    }
  }

  private def dfs(u: Int, p: Int): Unit = {
    up(0)(u) = p
    g(u).foreach { e =>
      val v = e(0)
      val w = e(1)
      if (v != p) {
        depth(v) = depth(u) + 1
        Array.copy(cnt(u), 0, cnt(v), 0, 27)
        cnt(v)(w) += 1
        dfs(v, u)
      }
    }
  }

  private def lca(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    if (depth(a) < depth(b)) {
      val t = a
      a = b
      b = t
    }
    val diff = depth(a) - depth(b)
    for (j <- 0 until LOG) if ((diff & (1 << j)) != 0) a = up(j)(a)
    if (a == b) return a
    for (j <- LOG - 1 to 0 by -1) {
      if (up(j)(a) != up(j)(b)) {
        a = up(j)(a)
        b = up(j)(b)
      }
    }
    up(0)(a)
  }
}
'''

FILES["2847_smallest_number_with_given_digit_product"] = r'''// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

object Solution {
  def smallestNumber(n: Long): String = {
    if (n == 0) return "0"
    if (n == 1) return "1"
    val digits = new StringBuilder
    var x = n
    for (d <- 9 to 2 by -1) {
      while (x % d == 0) {
        digits.append(('0' + d).toChar)
        x /= d
      }
    }
    if (x > 1) "-1" else digits.reverse.toString
  }
}
'''

FILES["2848_points_that_intersect_with_cars"] = r'''// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/

object Solution {
  def numberOfPoints(nums: Array[Array[Int]]): Int = {
    val cov = Array.fill(102)(0)
    nums.foreach { r =>
      for (x <- r(0) to r(1)) cov(x) = 1
    }
    cov.sum
  }
}
'''

FILES["2849_determine_if_a_cell_is_reachable_at_a_given_time"] = r'''// LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

object Solution {
  def isReachableAtTime(sx: Int, sy: Int, fx: Int, fy: Int, t: Int): Boolean = {
    val need = math.max(math.abs(sx - fx), math.abs(sy - fy))
    if (need == 0) t != 1 else t >= need
  }
}
'''

FILES["2850_minimum_moves_to_spread_stones_over_grid"] = r'''// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

object Solution {
  private var extras: scala.collection.mutable.ArrayBuffer[Array[Int]] = _
  private var zeros: scala.collection.mutable.ArrayBuffer[Array[Int]] = _
  private var best: Int = _

  def minimumMoves(grid: Array[Array[Int]]): Int = {
    extras = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    zeros = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    for (i <- 0 until 3; j <- 0 until 3) {
      if (grid(i)(j) == 0) zeros += Array(i, j)
      else if (grid(i)(j) > 1) {
        for (_ <- 0 until grid(i)(j) - 1) extras += Array(i, j)
      }
    }
    if (zeros.isEmpty) return 0
    best = 1 << 30
    dfs(0, 0)
    best
  }

  private def dfs(i: Int, cost: Int): Unit = {
    if (cost >= best) return
    if (i == zeros.length) {
      best = cost
      return
    }
    for (j <- extras.indices) {
      if (extras(j)(0) >= 0) {
        val e = extras(j)
        extras(j) = Array(-1, e(1))
        val d = math.abs(e(0) - zeros(i)(0)) + math.abs(e(1) - zeros(i)(1))
        dfs(i + 1, cost + d)
        extras(j) = e
      }
    }
  }
}
'''

FILES["2851_string_transformation"] = r'''// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

object Solution {
  private val MOD = 1000000007

  def numberOfWays(s: String, t: String, k: Long): Int = {
    val n = s.length
    val ss = s + s
    if (!ss.substring(0, 2 * n - 1).contains(t)) return 0
    var cnt = 0
    for (i <- 0 until n) if (ss.substring(i, i + n) == t) cnt += 1
    val same = s == t
    val pk = modPow(n - 1, k)
    val invn = modPow(n, MOD - 2)
    val sign = if (k % 2 == 1) MOD - 1 else 1
    val waysSame = ((1L * pk + 1L * ((n - 1) % MOD) * sign % MOD) % MOD * invn % MOD).toInt
    val waysDiff = ((1L * pk - sign + MOD) % MOD * invn % MOD).toInt
    if (same) waysSame else (1L * waysDiff * cnt % MOD).toInt
  }

  private def modPow(a0: Long, b0: Long): Int = {
    var res = 1L
    var a = a0 % MOD
    var b = b0
    while (b > 0) {
      if ((b & 1) != 0) res = res * a % MOD
      a = a * a % MOD
      b >>= 1
    }
    res.toInt
  }
}
'''

FILES["2852_sum_of_remoteness_of_all_cells"] = r'''// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

object Solution {
  def sumRemoteness(grid: Array[Array[Int]]): Long = {
    val m = grid.length
    val n = grid(0).length
    val seen = Array.ofDim[Boolean](m, n)
    val dirs = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))
    var total = 0L
    for (i <- 0 until m; j <- 0 until n) if (grid(i)(j) != -1) total += grid(i)(j)
    var ans = 0L
    for (i <- 0 until m; j <- 0 until n) {
      if (grid(i)(j) != -1 && !seen(i)(j)) {
        val q = scala.collection.mutable.Queue(Array(i, j))
        seen(i)(j) = true
        var sum = 0L
        var cnt = 0
        while (q.nonEmpty) {
          val cur = q.dequeue()
          val x = cur(0)
          val y = cur(1)
          sum += grid(x)(y)
          cnt += 1
          dirs.foreach { d =>
            val ni = x + d(0)
            val nj = y + d(1)
            if (ni >= 0 && nj >= 0 && ni < m && nj < n && !seen(ni)(nj) && grid(ni)(nj) != -1) {
              seen(ni)(nj) = true
              q.enqueue(Array(ni, nj))
            }
          }
        }
        ans += (total - sum) * cnt
      }
    }
    ans
  }
}
'''

FILES["2855_minimum_right_shifts_to_sort_the_array"] = r'''// LeetCode 2855 - Minimum Right Shifts to Sort the Array
// https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

object Solution {
  def minimumRightShifts(nums: Array[Int]): Int = {
    val n = nums.length
    var drops = 0
    var idx = -1
    for (i <- 0 until n) {
      if (nums(i) > nums((i + 1) % n)) {
        drops += 1
        idx = i
      }
    }
    if (drops == 0) 0
    else if (drops > 1) -1
    else n - 1 - idx
  }
}
'''

FILES["2856_minimum_array_length_after_pair_removals"] = r'''// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

object Solution {
  def minLengthAfterRemovals(nums: Array[Int]): Int = {
    val n = nums.length
    var mx = 0
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    nums.foreach { v =>
      freq(v) = freq.getOrElse(v, 0) + 1
      mx = math.max(mx, freq(v))
    }
    if (mx <= n / 2) n % 2 else 2 * mx - n
  }
}
'''

FILES["2857_count_pairs_of_points_with_distance_k"] = r'''// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

object Solution {
  def countPairs(coordinates: Array[Array[Int]], k: Int): Int = {
    val freq = scala.collection.mutable.Map.empty[Long, Int]
    var ans = 0
    coordinates.foreach { p =>
      val x = p(0)
      val y = p(1)
      for (a <- 0 to k) {
        val b = k - a
        ans += freq.getOrElse(key(x ^ a, y ^ b), 0)
      }
      val kk = key(x, y)
      freq(kk) = freq.getOrElse(kk, 0) + 1
    }
    ans
  }

  private def key(x: Int, y: Int): Long =
    (x.toLong << 32) ^ (y.toLong & 0xffffffffL)
}
'''

FILES["2858_minimum_edge_reversals_so_every_node_is_reachable"] = r'''// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

object Solution {
  private var g: Array[scala.collection.mutable.ArrayBuffer[Array[Int]]] = _
  private var ans: Array[Int] = _

  def minEdgeReversals(n: Int, edges: Array[Array[Int]]): Array[Int] = {
    g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Array[Int]])
    edges.foreach { e =>
      val u = e(0)
      val v = e(1)
      g(u) += Array(v, 0)
      g(v) += Array(u, 1)
    }
    ans = Array.fill(n)(0)
    dfs1(0, -1)
    dfs2(0, -1)
    ans
  }

  private def dfs1(u: Int, p: Int): Unit = {
    g(u).foreach { e =>
      val v = e(0)
      val ww = e(1)
      if (v != p) {
        ans(0) += ww
        dfs1(v, u)
      }
    }
  }

  private def dfs2(u: Int, p: Int): Unit = {
    g(u).foreach { e =>
      val v = e(0)
      val ww = e(1)
      if (v != p) {
        ans(v) = if (ww == 0) ans(u) + 1 else ans(u) - 1
        dfs2(v, u)
      }
    }
  }
}
'''

FILES["2859_sum_of_values_at_indices_with_k_set_bits"] = r'''// LeetCode 2859 - Sum of Values at Indices With K Set Bits
// https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

object Solution {
  def sumIndicesWithKSetBits(nums: Array[Int], k: Int): Int = {
    var ans = 0
    for (i <- nums.indices) if (Integer.bitCount(i) == k) ans += nums(i)
    ans
  }
}
'''

FILES["2860_happy_students"] = r'''// LeetCode 2860 - Happy Students
// https://leetcode.com/problems/happy-students/

object Solution {
  def countWays(nums: Array[Int]): Int = {
    val a = nums.sorted
    val n = a.length
    var ans = 0
    if (a(0) > 0) ans += 1
    for (i <- 0 until n) {
      val selected = i + 1
      if (selected > a(i) && (i == n - 1 || selected < a(i + 1))) ans += 1
    }
    ans
  }
}
'''

FILES["2861_maximum_number_of_alloys"] = r'''// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/

object Solution {
  def maxNumberOfAlloys(
      n: Int,
      k: Int,
      budget: Int,
      composition: Array[Array[Int]],
      stock: Array[Int],
      cost: Array[Int]
  ): Int = {
    var lo = 0L
    var hi = 1000000000L
    var ans = 0L
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      if (ok(mid, n, budget, composition, stock, cost)) {
        ans = mid
        lo = mid + 1
      } else hi = mid - 1
    }
    ans.toInt
  }

  private def ok(
      machines: Long,
      n: Int,
      budget: Int,
      composition: Array[Array[Int]],
      stock: Array[Int],
      cost: Array[Int]
  ): Boolean = {
    composition.exists { comp =>
      var spend = 0L
      for (i <- 0 until n) {
        val need = machines * comp(i) - stock(i)
        if (need > 0) spend += need * cost(i)
      }
      spend <= budget
    }
  }
}
'''

FILES["2862_maximum_element_sum_of_a_complete_subset_of_indices"] = r'''// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

object Solution {
  def maximumSum(nums: Array[Int]): Long = {
    val n = nums.length
    val groups = scala.collection.mutable.Map.empty[Int, Long]
    var ans = 0L
    for (i <- 1 to n) {
      val sf = squareFree(i)
      val sum = groups.getOrElse(sf, 0L) + nums(i - 1)
      groups(sf) = sum
      if (sum > ans) ans = sum
    }
    ans
  }

  private def squareFree(x0: Int): Int = {
    var x = x0
    var res = 1
    var p = 2
    while (p * p <= x) {
      var cnt = 0
      while (x % p == 0) {
        x /= p
        cnt += 1
      }
      if (cnt % 2 == 1) res *= p
      p += 1
    }
    if (x > 1) res *= x
    res
  }
}
'''

FILES["2863_maximum_length_of_semi_decreasing_subarrays"] = r'''// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

object Solution {
  def maxSubarrayLength(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    val st = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (i <- n - 1 to 0 by -1) {
      if (st.isEmpty || nums(i) > nums(st.last)) st += i
    }
    for (i <- 0 until n) {
      while (st.nonEmpty && nums(i) > nums(st.last)) {
        val j = st.remove(st.length - 1)
        if (j - i + 1 > ans) ans = j - i + 1
      }
    }
    ans
  }
}
'''

FILES["2864_maximum_odd_binary_number"] = r'''// LeetCode 2864 - Maximum Odd Binary Number
// https://leetcode.com/problems/maximum-odd-binary-number/

object Solution {
  def maximumOddBinaryNumber(s: String): String = {
    val ones = s.count(_ == '1')
    val zeros = s.length - ones
    "1" * (ones - 1) + "0" * zeros + "1"
  }
}
'''

FILES["2865_beautiful_towers_i"] = r'''// LeetCode 2865 - Beautiful Towers I
// https://leetcode.com/problems/beautiful-towers-i/

object Solution {
  def maximumSumOfHeights(heights: Array[Int]): Long = {
    val n = heights.length
    var ans = 0L
    for (peak <- 0 until n) {
      var sum = heights(peak).toLong
      var mn = heights(peak)
      for (i <- peak - 1 to 0 by -1) {
        if (heights(i) < mn) mn = heights(i)
        sum += mn
      }
      mn = heights(peak)
      for (i <- peak + 1 until n) {
        if (heights(i) < mn) mn = heights(i)
        sum += mn
      }
      if (sum > ans) ans = sum
    }
    ans
  }
}
'''

FILES["2866_beautiful_towers_ii"] = r'''// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

object Solution {
  def maximumSumOfHeights(maxHeights: Array[Int]): Long = {
    val n = maxHeights.length
    val left = Array.fill(n)(0L)
    val st = scala.collection.mutable.ArrayBuffer(-1)
    var sum = 0L
    for (i <- 0 until n) {
      while (st.length > 1 && maxHeights(st.last) >= maxHeights(i)) {
        val j = st.remove(st.length - 1)
        sum -= 1L * maxHeights(j) * (j - st.last)
      }
      sum += 1L * maxHeights(i) * (i - st.last)
      left(i) = sum
      st += i
    }
    val right = Array.fill(n)(0L)
    st.clear()
    st += n
    sum = 0
    for (i <- n - 1 to 0 by -1) {
      while (st.length > 1 && maxHeights(st.last) >= maxHeights(i)) {
        val j = st.remove(st.length - 1)
        sum -= 1L * maxHeights(j) * (st.last - j)
      }
      sum += 1L * maxHeights(i) * (st.last - i)
      right(i) = sum
      st += i
    }
    var ans = 0L
    for (i <- 0 until n) {
      val cand = left(i) + right(i) - maxHeights(i)
      if (cand > ans) ans = cand
    }
    ans
  }
}
'''

FILES["2867_count_valid_paths_in_a_tree"] = r'''// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

object Solution {
  private var isPrime: Array[Boolean] = _
  private var g: Array[scala.collection.mutable.ArrayBuffer[Int]] = _

  def countPaths(n: Int, edges: Array[Array[Int]]): Long = {
    isPrime = Array.fill(n + 1)(true)
    isPrime(0) = false
    isPrime(1) = false
    var i = 2
    while (i * i <= n) {
      if (isPrime(i)) {
        var j = i * i
        while (j <= n) {
          isPrime(j) = false
          j += i
        }
      }
      i += 1
    }
    g = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    var ans = 0L
    for (u <- 1 to n if isPrime(u)) {
      var total = 0L
      g(u).foreach { v =>
        val c = dfs(v, u)
        ans += c
        ans += total * c
        total += c
      }
    }
    ans
  }

  private def dfs(u: Int, p: Int): Int = {
    if (isPrime(u)) return 0
    var sz = 1
    g(u).foreach { v => if (v != p) sz += dfs(v, u) }
    sz
  }
}
'''

FILES["2868_the_wording_game"] = r'''// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

object Solution {
  def canAliceWin(a: Array[String], b: Array[String]): Boolean = {
    var i = 0
    var j = 0
    var last: Char = 0
    var alice = true
    while (true) {
      if (alice) {
        while (i < a.length && a(i).charAt(0) <= last) i += 1
        if (i == a.length) return false
        last = a(i).charAt(a(i).length - 1)
        i += 1
      } else {
        while (j < b.length && b(j).charAt(0) <= last) j += 1
        if (j == b.length) return true
        last = b(j).charAt(b(j).length - 1)
        j += 1
      }
      alice = !alice
    }
    false
  }
}
'''

def main() -> None:
    written = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "Solution.scala"
        path.write_text(content, encoding="utf-8", newline="\n")
        if path.read_bytes().startswith(b"\xef\xbb\xbf"):
            raise SystemExit(f"BOM in {path}")
        written += 1
        print(f"wrote {folder}")
    print(f"written={written}")


if __name__ == "__main__":
    main()
