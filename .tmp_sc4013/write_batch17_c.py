#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3450_maximum_students_on_a_single_bench"] = r'''// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

object Solution {
  def maxStudentsOnBench(students: Array[Array[Int]]): Int = {
    val bench = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.Set[Int]]
    students.foreach { s =>
      bench.getOrElseUpdate(s(1), scala.collection.mutable.Set.empty[Int]) += s(0)
    }
    var ans = 0
    bench.values.foreach { set => if (set.size > ans) ans = set.size }
    ans
  }
}
'''

FILES["3452_sum_of_good_numbers"] = r'''// LeetCode 3452 - Sum of Good Numbers
// https://leetcode.com/problems/sum-of-good-numbers/

object Solution {
  def sumOfGoodNumbers(nums: Array[Int], k: Int): Int = {
    var ans = 0
    val n = nums.length
    var i = 0
    while (i < n) {
      val x = nums(i)
      var good = true
      if (i - k >= 0 && x <= nums(i - k)) good = false
      if (i + k < n && x <= nums(i + k)) good = false
      if (good) ans += x
      i += 1
    }
    ans
  }
}
'''

FILES["3453_separate_squares_i"] = r'''// LeetCode 3453 - Separate Squares I
// https://leetcode.com/problems/separate-squares-i/

object Solution {
  def separateSquares(squares: Array[Array[Int]]): Double = {
    var total = 0.0
    squares.foreach { sq =>
      val l = sq(2).toDouble
      total += l * l
    }
    var lo = 0.0
    var hi = 2e9
    var it = 0
    while (it < 60) {
      val mid = (lo + hi) / 2
      if (okArea(squares, mid) * 2 < total) lo = mid
      else hi = mid
      it += 1
    }
    hi
  }

  private def okArea(squares: Array[Array[Int]], y: Double): Double = {
    var below = 0.0
    squares.foreach { sq =>
      val yi = sq(1).toDouble
      val l = sq(2).toDouble
      val top = yi + l
      if (y > yi) {
        if (y >= top) below += l * l
        else below += l * (y - yi)
      }
    }
    below
  }
}
'''

FILES["3454_separate_squares_ii"] = r'''// LeetCode 3454 - Separate Squares II
// https://leetcode.com/problems/separate-squares-ii/

object Solution {
  def separateSquares(squares: Array[Array[Int]]): Double = {
    var total = 0.0
    squares.foreach { sq =>
      val l = sq(2).toDouble
      total += l * l
    }
    var lo = 0.0
    var hi = 2e9
    var it = 0
    while (it < 60) {
      val mid = (lo + hi) / 2
      if (areaBelow(squares, mid) * 2 < total) lo = mid
      else hi = mid
      it += 1
    }
    hi
  }

  private def areaBelow(squares: Array[Array[Int]], y: Double): Double = {
    var below = 0.0
    squares.foreach { sq =>
      val yi = sq(1).toDouble
      val l = sq(2).toDouble
      val top = yi + l
      if (y > yi) {
        if (y >= top) below += l * l
        else below += l * (y - yi)
      }
    }
    below
  }
}
'''

FILES["3455_shortest_matching_substring"] = r'''// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

object Solution {
  def shortestMatchingSubstring(s: String, p: String): Int = {
    val parts = new java.util.ArrayList[String]()
    val cur = new StringBuilder
    p.foreach { c =>
      if (c == '*') {
        parts.add(cur.toString)
        cur.setLength(0)
      } else cur.append(c)
    }
    parts.add(cur.toString)
    while (parts.size() < 3) parts.add("")
    val a = parts.get(0)
    val b = parts.get(1)
    val c = parts.get(2)
    val n = s.length
    val posA = findAll(s, a)
    val posB = findAll(s, b)
    val posC = findAll(s, c)
    var ans = n + 1
    val ita = posA.iterator()
    while (ita.hasNext) {
      val ia = ita.next()
      val endA = ia + a.length
      var bi = sortSearch(posB, endA)
      var done = false
      while (bi < posB.size() && !done) {
        val endB = posB.get(bi) + b.length
        val ci = sortSearch(posC, endB)
        if (ci < posC.size()) {
          val length = posC.get(ci) + c.length - ia
          if (length < ans) ans = length
        }
        done = true
        bi += 1
      }
    }
    if (ans == n + 1) -1 else ans
  }

  private def findAll(s: String, sub: String): java.util.ArrayList[Integer] = {
    val res = new java.util.ArrayList[Integer]()
    val n = s.length
    if (sub.isEmpty) {
      var i = 0
      while (i <= n) { res.add(i); i += 1 }
      return res
    }
    var i = 0
    while (i + sub.length <= n) {
      if (s.regionMatches(i, sub, 0, sub.length)) res.add(i)
      i += 1
    }
    res
  }

  private def sortSearch(arr: java.util.ArrayList[Integer], x: Int): Int = {
    val i = java.util.Collections.binarySearch(arr, Integer.valueOf(x))
    if (i >= 0) i else -i - 1
  }
}
'''

FILES["3456_find_special_substring_of_length_k"] = r'''// LeetCode 3456 - Find Special Substring of Length K
// https://leetcode.com/problems/find-special-substring-of-length-k/

object Solution {
  def hasSpecialSubstring(s: String, k: Int): Boolean = {
    val n = s.length
    var i = 0
    while (i + k <= n) {
      var ok = true
      var j = i + 1
      while (j < i + k) {
        if (s.charAt(j) != s.charAt(i)) { ok = false; j = i + k }
        else j += 1
      }
      if (ok && !(i > 0 && s.charAt(i - 1) == s.charAt(i)) && !(i + k < n && s.charAt(i + k) == s.charAt(i))) {
        return true
      }
      i += 1
    }
    false
  }
}
'''

FILES["3457_eat_pizzas"] = r'''// LeetCode 3457 - Eat Pizzas!
// https://leetcode.com/problems/eat-pizzas/

object Solution {
  def maxWeight(pizzas: Array[Int]): Long = {
    java.util.Arrays.sort(pizzas)
    val n = pizzas.length
    val days = n / 4
    var ans = 0L
    val oddDays = (days + 1) / 2
    val evenDays = days / 2
    var idx = n - 1
    var i = 0
    while (i < oddDays) {
      ans += pizzas(idx)
      idx -= 1
      i += 1
    }
    i = 0
    while (i < evenDays) {
      idx -= 1
      ans += pizzas(idx)
      idx -= 1
      i += 1
    }
    ans
  }
}
'''

FILES["3458_select_k_disjoint_special_substrings"] = r'''// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

object Solution {
  def maxSubstringLength(s: String, k: Int): Boolean = {
    val n = s.length
    val first = Array.fill(26)(n)
    val last = Array.fill(26)(-1)
    var i = 0
    while (i < n) {
      val ci = s.charAt(i) - 'a'
      if (first(ci) == n) first(ci) = i
      last(ci) = i
      i += 1
    }
    val segs = new java.util.ArrayList[Array[Int]]()
    var c = 0
    while (c < 26) {
      if (last(c) != -1) {
        var l = first(c)
        var r = last(c)
        i = l
        while (i <= r) {
          val ci = s.charAt(i) - 'a'
          if (first(ci) < l) {
            l = first(ci)
            i = l
          } else {
            if (last(ci) > r) r = last(ci)
            i += 1
          }
        }
        if (!(l == 0 && r == n - 1)) segs.add(Array(l, r))
      }
      c += 1
    }
    val uniq = scala.collection.mutable.Set.empty[Long]
    val arr = new java.util.ArrayList[Array[Int]]()
    val it = segs.iterator()
    while (it.hasNext) {
      val sg = it.next()
      val key = (sg(0).toLong << 32) | (sg(1) & 0xffffffffL)
      if (uniq.add(key)) arr.add(sg)
    }
    arr.sort((a: Array[Int], b: Array[Int]) => java.lang.Integer.compare(a(1), b(1)))
    var cnt = 0
    var end = -1
    val it2 = arr.iterator()
    while (it2.hasNext) {
      val sg = it2.next()
      if (sg(0) > end) {
        cnt += 1
        end = sg(1)
      }
    }
    cnt >= k
  }
}
'''

FILES["3459_length_of_longest_v_shaped_diagonal_segment"] = r'''// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

object Solution {
  private var m = 0
  private var n = 0
  private var grid: Array[Array[Int]] = _
  private val dirs = Array(Array(1, 1), Array(1, -1), Array(-1, -1), Array(-1, 1))
  private val nextDir = Array(1, 2, 3, 0)
  private val memo = new java.util.HashMap[java.lang.Long, Integer]()

  def lenOfVDiagonal(grid0: Array[Array[Int]]): Int = {
    grid = grid0
    m = grid.length
    n = grid(0).length
    memo.clear()
    var ans = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 1) {
          var d = 0
          while (d < 4) {
            val ni = i + dirs(d)(0)
            val nj = j + dirs(d)(1)
            val best = 1 + dfs(ni, nj, d, 0, 2)
            if (best > ans) ans = best
            d += 1
          }
          if (ans < 1) ans = 1
        }
        j += 1
      }
      i += 1
    }
    ans
  }

  private def key(i: Int, j: Int, d: Int, turned: Int, expect: Int): Long =
    ((((i.toLong * 101L + j) * 5L + d) * 3L + turned) * 5L + expect)

  private def dfs(i: Int, j: Int, d: Int, turned: Int, expect: Int): Int = {
    if (i < 0 || j < 0 || i >= m || j >= n || grid(i)(j) != expect) return 0
    val k = key(i, j, d, turned, expect)
    val cached = memo.get(k)
    if (cached != null) return cached
    val ni = i + dirs(d)(0)
    val nj = j + dirs(d)(1)
    val nx = if (expect == 2) 0 else 2
    var best = 1 + dfs(ni, nj, d, turned, nx)
    if (turned == 0) {
      val nd = nextDir(d)
      val ti = i + dirs(nd)(0)
      val tj = j + dirs(nd)(1)
      val cand = 1 + dfs(ti, tj, nd, 1, nx)
      if (cand > best) best = cand
    }
    memo.put(k, best)
    best
  }
}
'''

FILES["3460_longest_common_prefix_after_at_most_one_removal"] = r'''// LeetCode 3460 - Longest Common Prefix After at Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

object Solution {
  def longestCommonPrefix(s: String, t: String): Int = {
    var i = 0
    var j = 0
    var removed = false
    while (i < s.length && j < t.length) {
      if (s.charAt(i) == t.charAt(j)) {
        i += 1
        j += 1
      } else {
        if (removed) return j
        removed = true
        i += 1
      }
    }
    j
  }
}
'''

FILES["3461_check_if_digits_are_equal_in_string_after_operations_i"] = r'''// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

object Solution {
  def hasSameDigits(s: String): Boolean = {
    var b = s.toCharArray
    while (b.length > 2) {
      val nb = new Array[Char](b.length - 1)
      var i = 0
      while (i + 1 < b.length) {
        nb(i) = ('0' + (b(i) - '0' + b(i + 1) - '0') % 10).toChar
        i += 1
      }
      b = nb
    }
    b(0) == b(1)
  }
}
'''

FILES["3462_maximum_sum_with_at_most_k_elements"] = r'''// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

object Solution {
  def maxSum(grid: Array[Array[Int]], limits: Array[Int], k: Int): Long = {
    val h = new java.util.PriorityQueue[Integer]()
    var sum = 0L
    var i = 0
    while (i < grid.length) {
      val r = grid(i).clone()
      java.util.Arrays.sort(r)
      var lim = limits(i)
      if (lim > r.length) lim = r.length
      var j = 0
      while (j < lim) {
        val `val` = r(r.length - 1 - j)
        h.offer(`val`)
        sum += `val`
        if (h.size() > k) sum -= h.poll()
        j += 1
      }
      i += 1
    }
    sum
  }
}
'''

FILES["3463_check_if_digits_are_equal_in_string_after_operations_ii"] = r'''// LeetCode 3463 - Check If Digits Are Equal in String After Operations II
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

object Solution {
  private def modPowP(a0: Int, e0: Int, p: Int): Int = {
    var a = a0
    var e = e0
    var r = 1
    while (e > 0) {
      if ((e & 1) != 0) r = r * a % p
      a = a * a % p
      e >>= 1
    }
    r
  }
  private def modInvPrime(a: Int, p: Int): Int = modPowP(a, p - 2, p)
  private def binomMod(n: Int, k: Int, p: Int): Int = {
    if (k < 0 || k > n) return 0
    var num = 1
    var den = 1
    var i = 0
    while (i < k) {
      num = num * (n - i) % p
      den = den * (i + 1) % p
      i += 1
    }
    num * modInvPrime(den, p) % p
  }
  private def crt(a1: Int, m1: Int, a2: Int, m2: Int): Int = {
    var x = 0
    while (x < m1 * m2) {
      if (x % m1 == a1 && x % m2 == a2) return x
      x += 1
    }
    0
  }
  private def binomMod10(n: Int, k: Int): Int = crt(binomMod(n, k, 2), 2, binomMod(n, k, 5), 5)
  private def combineDigit(s: String, n: Int, offset: Int): Int = {
    var sum = 0
    var i = 0
    while (i <= n - 2) {
      sum = (sum + binomMod10(n - 2, i) * (s.charAt(i + offset) - '0')) % 10
      i += 1
    }
    sum
  }
  def hasSameDigits(s: String): Boolean = {
    val n = s.length
    combineDigit(s, n, 0) == combineDigit(s, n, 1)
  }
}
'''

FILES["3464_maximize_the_distance_between_points_on_a_square"] = r'''// LeetCode 3464 - Maximize the Distance Between Points on a Square
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

object Solution {
  private def canPlace(arr: Array[Int], perim: Int, k: Int, mid: Int): Boolean = {
    val n = arr.length
    var s = 0
    while (s < n) {
      var cnt = 1
      var last = arr(s)
      var idx = s
      var stop = false
      while (cnt < k && !stop) {
        val target = last + mid
        var found = false
        var step = 1
        while (step < n && !found) {
          val ni = (idx + step) % n
          val `val` = arr(ni)
          val add = if (ni <= idx) perim else 0
          if (`val` + add >= target) {
            last = `val` + add
            idx = ni
            cnt += 1
            found = true
          }
          step += 1
        }
        if (!found) stop = true
      }
      if (cnt == k && last - arr(s) <= perim - mid) return true
      s += 1
    }
    false
  }

  def maxDistance(side: Int, points: Array[Array[Int]], k: Int): Int = {
    val arr = new Array[Int](points.length)
    var i = 0
    while (i < points.length) {
      val x = points(i)(0)
      val y = points(i)(1)
      val d =
        if (y == 0) x
        else if (x == side) side + y
        else if (y == side) 2 * side + (side - x)
        else 3 * side + (side - y)
      arr(i) = d
      i += 1
    }
    java.util.Arrays.sort(arr)
    val perim = 4 * side
    var lo = 0
    var hi = 2 * side
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (canPlace(arr, perim, k, mid)) lo = mid
      else hi = mid - 1
    }
    lo
  }
}
'''

FILES["3466_maximum_coin_collection"] = r'''// LeetCode 3466 - Maximum Coin Collection
// https://leetcode.com/problems/maximum-coin-collection/

object Solution {
  def maxCoins(lane1: Array[Int], lane2: Array[Int]): Long = {
    val n = lane1.length
    val neg = -1L << 60
    val dp = Array.ofDim[Long](2, 2)
    dp(0)(0) = lane1(0)
    dp(1)(0) = lane2(0)
    dp(0)(1) = neg
    dp(1)(1) = neg
    var ans = math.max(dp(0)(0), dp(1)(0))
    var i = 1
    while (i < n) {
      val ndp = Array.ofDim[Long](2, 2)
      ndp(0)(0) = math.max(dp(0)(0), 0L) + lane1(i)
      ndp(1)(0) = math.max(dp(1)(0), 0L) + lane2(i)
      ndp(0)(1) = math.max(dp(0)(1), dp(1)(0)) + lane1(i)
      ndp(1)(1) = math.max(dp(1)(1), dp(0)(0)) + lane2(i)
      if (lane1(i) > ndp(0)(0)) ndp(0)(0) = lane1(i)
      if (lane2(i) > ndp(1)(0)) ndp(1)(0) = lane2(i)
      var a = 0
      while (a < 2) {
        var b = 0
        while (b < 2) {
          dp(a)(b) = ndp(a)(b)
          if (dp(a)(b) > ans) ans = dp(a)(b)
          b += 1
        }
        a += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3467_transform_array_by_parity"] = r'''// LeetCode 3467 - Transform Array by Parity
// https://leetcode.com/problems/transform-array-by-parity/

object Solution {
  def transformArray(nums: Array[Int]): Array[Int] = {
    var i = 0
    while (i < nums.length) {
      nums(i) %= 2
      i += 1
    }
    var j = 0
    i = 0
    while (i < nums.length) {
      if (nums(i) == 0) {
        val t = nums(i); nums(i) = nums(j); nums(j) = t
        j += 1
      }
      i += 1
    }
    nums
  }
}
'''

FILES["3468_find_the_number_of_copy_arrays"] = r'''// LeetCode 3468 - Find the Number of Copy Arrays
// https://leetcode.com/problems/find-the-number-of-copy-arrays/

object Solution {
  def countArrays(original: Array[Int], bounds: Array[Array[Int]]): Int = {
    val n = original.length
    var lo = bounds(0)(0)
    var hi = bounds(0)(1)
    var i = 1
    while (i < n) {
      val diff = original(i) - original(i - 1)
      val lo2 = bounds(i)(0)
      val hi2 = bounds(i)(1)
      var nlo = lo + diff
      var nhi = hi + diff
      if (nlo < lo2) nlo = lo2
      if (nhi > hi2) nhi = hi2
      if (nlo > nhi) return 0
      lo = nlo
      hi = nhi
      i += 1
    }
    hi - lo + 1
  }
}
'''

FILES["3469_find_minimum_cost_to_remove_array_elements"] = r'''// LeetCode 3469 - Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

object Solution {
  private val memo = new java.util.HashMap[java.lang.Long, Integer]()
  private var nums: Array[Int] = _
  private var n = 0

  private def max2(a: Int, b: Int): Int = if (a > b) a else b
  private def min3(a: Int, b: Int, c: Int): Int = math.min(a, math.min(b, c))
  private def key(i: Int, prev: Int): Long = (i.toLong << 32) | (prev & 0xffffffffL)

  private def dfs(i: Int, prev: Int): Int = {
    if (i >= n) return if (prev == -1) 0 else nums(prev)
    val k = key(i, prev)
    val cached = memo.get(k)
    if (cached != null) return cached
    val res =
      if (prev == -1) {
        if (i + 1 >= n) nums(i)
        else if (i + 2 >= n) max2(nums(i), nums(i + 1))
        else {
          val a = nums(i)
          val b = nums(i + 1)
          val c = nums(i + 2)
          min3(max2(b, c) + dfs(i + 3, i), max2(a, c) + dfs(i + 3, i + 1), max2(a, b) + dfs(i + 3, i + 2))
        }
      } else {
        if (i + 1 >= n) max2(nums(prev), nums(i))
        else {
          val a = nums(prev)
          val b = nums(i)
          val c = nums(i + 1)
          min3(max2(b, c) + dfs(i + 2, prev), max2(a, c) + dfs(i + 2, i), max2(a, b) + dfs(i + 2, i + 1))
        }
      }
    memo.put(k, res)
    res
  }

  def minCost(nums0: Array[Int]): Int = {
    nums = nums0
    n = nums.length
    memo.clear()
    dfs(0, -1)
  }
}
'''

FILES["3470_permutations_iv"] = r'''// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

object Solution {
  private var fact: Array[Long] = _
  private var used: Array[Boolean] = _
  private var ans: java.util.ArrayList[Integer] = _
  private var k: Long = 0
  private var n: Int = 0

  def permute(n0: Int, k0: Long): Array[Int] = {
    n = n0
    k = k0
    fact = new Array[Long](n + 1)
    fact(0) = 1
    var i = 1
    while (i <= n) {
      fact(i) = fact(i - 1) * i
      if (fact(i) > 1e18.toLong) fact(i) = 1e18.toLong + 1
      i += 1
    }
    used = new Array[Boolean](n + 1)
    ans = new java.util.ArrayList[Integer]()
    if (!dfs(0)) return Array.empty[Int]
    Array.tabulate(ans.size())(i => ans.get(i).intValue())
  }

  private def dfs(pos: Int): Boolean = {
    if (pos == n) return true
    var x = 1
    while (x <= n) {
      if (!used(x) && !(pos > 0 && ans.get(pos - 1) % 2 == x % 2)) {
        val rem = n - pos - 1
        val cnt = fact(rem)
        if (cnt >= k) {
          used(x) = true
          ans.add(x)
          if (dfs(pos + 1)) return true
          ans.remove(ans.size() - 1)
          used(x) = false
        } else {
          k -= cnt
        }
      }
      x += 1
    }
    false
  }
}
'''

FILES["3471_find_the_largest_almost_missing_integer"] = r'''// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

object Solution {
  def largestInteger(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var i = 0
    while (i + k <= n) {
      val seen = scala.collection.mutable.Set.empty[Int]
      var j = i
      while (j < i + k) { seen += nums(j); j += 1 }
      seen.foreach { x => cnt(x) = cnt.getOrElse(x, 0) + 1 }
      i += 1
    }
    var ans = -1
    cnt.foreach { case (key, value) =>
      if (value == 1 && key > ans) ans = key
    }
    ans
  }
}
'''

FILES["3472_longest_palindromic_subsequence_after_at_most_k_operations"] = r'''// LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
// https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

object Solution {
  private var dp: Array[Array[Array[Int]]] = _
  private var s: String = _

  def longestPalindromicSubsequence(s0: String, k: Int): Int = {
    s = s0
    val n = s.length
    dp = Array.fill(n, n, k + 1)(-1)
    dfs(0, n - 1, k)
  }

  private def distCirc(a: Char, b: Char): Int = {
    val d = math.abs(a - b)
    math.min(d, 26 - d)
  }

  private def dfs(i: Int, j: Int, ops: Int): Int = {
    if (i > j) return 0
    if (i == j) return 1
    if (dp(i)(j)(ops) != -1) return dp(i)(j)(ops)
    var best = dfs(i + 1, j, ops)
    best = math.max(best, dfs(i, j - 1, ops))
    val cost = distCirc(s.charAt(i), s.charAt(j))
    if (cost <= ops) best = math.max(best, 2 + dfs(i + 1, j - 1, ops - cost))
    dp(i)(j)(ops) = best
    best
  }
}
'''

FILES["3473_sum_of_k_subarrays_with_length_at_least_m"] = r'''// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

object Solution {
  def maxSum(nums: Array[Int], k: Int, m: Int): Long = {
    val n = nums.length
    val pref = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + nums(i)
      i += 1
    }
    val neg = -(1L << 60)
    val dp = Array.fill(k + 1, n + 1)(neg)
    i = 0
    while (i <= n) { dp(0)(i) = 0; i += 1 }
    var t = 1
    while (t <= k) {
      var best = neg
      i = t * m
      while (i <= n) {
        val j = i - m
        best = math.max(best, dp(t - 1)(j) - pref(j))
        dp(t)(i) = best + pref(i)
        i += 1
      }
      i = 1
      while (i <= n) {
        dp(t)(i) = math.max(dp(t)(i), dp(t)(i - 1))
        i += 1
      }
      t += 1
    }
    dp(k)(n)
  }
}
'''

FILES["3474_lexicographically_smallest_generated_string"] = r'''// LeetCode 3474 - Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/

object Solution {
  def generateString(str1: String, str2: String): String = {
    val n = str1.length
    val m = str2.length
    val L = n + m - 1
    val ans = Array.fill(L)('?')
    var i = 0
    while (i < n) {
      if (str1.charAt(i) == 'T') {
        var j = 0
        while (j < m) {
          if (ans(i + j) != '?' && ans(i + j) != str2.charAt(j)) return ""
          ans(i + j) = str2.charAt(j)
          j += 1
        }
      }
      i += 1
    }
    i = 0
    while (i < L) {
      if (ans(i) == '?') ans(i) = 'a'
      i += 1
    }
    i = 0
    while (i < n) {
      if (str1.charAt(i) == 'F') {
        var match = true
        var j = 0
        while (j < m) {
          if (ans(i + j) != str2.charAt(j)) { match = false; j = m }
          else j += 1
        }
        if (match) {
          var changed = false
          j = m - 1
          while (j >= 0 && !changed) {
            val pos = i + j
            var forced = false
            var t = 0
            while (t < n && !forced) {
              if (str1.charAt(t) == 'T' && pos >= t && pos < t + m) forced = true
              t += 1
            }
            if (!forced) {
              ans(pos) = 'b'
              changed = true
            }
            j -= 1
          }
          if (!changed) return ""
        }
      }
      i += 1
    }
    i = 0
    while (i < n) {
      var match = true
      var j = 0
      while (j < m) {
        if (ans(i + j) != str2.charAt(j)) { match = false; j = m }
        else j += 1
      }
      if (str1.charAt(i) == 'T' && !match) return ""
      if (str1.charAt(i) == 'F' && match) return ""
      i += 1
    }
    new String(ans)
  }
}
'''

FILES["3476_maximize_profit_from_task_assignment"] = r'''// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

object Solution {
  def maxProfit(workers: Array[Int], tasks: Array[Array[Int]]): Long = {
    java.util.Arrays.sort(workers)
    java.util.Arrays.sort(tasks, (a: Array[Int], b: Array[Int]) => java.lang.Integer.compare(a(0), b(0)))
    var ans = 0L
    val used = new Array[Boolean](tasks.length)
    workers.foreach { w =>
      var best = -1
      var bi = -1
      var i = 0
      var stop = false
      while (i < tasks.length && !stop) {
        if (!used(i)) {
          if (tasks(i)(0) > w) stop = true
          else if (tasks(i)(1) > best) {
            best = tasks(i)(1)
            bi = i
          }
        }
        i += 1
      }
      if (bi >= 0) {
        used(bi) = true
        ans += best
      }
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
