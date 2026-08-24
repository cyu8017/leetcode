#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3000_maximum_area_of_longest_diagonal_rectangle"] = r'''// LeetCode 3000 - Maximum Area of Longest Diagonal Rectangle
// https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

object Solution {
  def areaOfMaxDiagonal(dimensions: Array[Array[Int]]): Int = {
    var ans = 0
    var mx = 0
    for (d <- dimensions) {
      val l = d(0)
      val w = d(1)
      val t = l * l + w * w
      if (mx < t) { mx = t; ans = l * w }
      else if (mx == t) ans = math.max(ans, l * w)
    }
    ans
  }
}
'''

FILES["3001_minimum_moves_to_capture_the_queen"] = r'''// LeetCode 3001 - Minimum Moves to Capture The Queen
// https://leetcode.com/problems/minimum-moves-to-capture-the-queen/

object Solution {
  def minMovesToCaptureTheQueen(a: Int, b: Int, c: Int, d: Int, e: Int, f: Int): Int = {
    if (a == e && (c != a || (d - b) * (d - f) > 0)) return 1
    if (b == f && (d != b || (c - a) * (c - e) > 0)) return 1
    if (c - e == d - f && (a - e != b - f || (a - c) * (a - e) > 0)) return 1
    if (c - e == f - d && (a - e != f - b || (a - c) * (a - e) > 0)) return 1
    2
  }
}
'''

FILES["3002_maximum_size_of_a_set_after_removals"] = r'''// LeetCode 3002 - Maximum Size of a Set After Removals
// https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

object Solution {
  def maximumSetSize(nums1: Array[Int], nums2: Array[Int]): Int = {
    val s1 = nums1.toSet
    val s2 = nums2.toSet
    var a = 0
    var b = 0
    var c = 0
    for (x <- s1) if (!s2.contains(x)) a += 1
    for (x <- s2) {
      if (!s1.contains(x)) b += 1
      else c += 1
    }
    val n = nums1.length
    a = math.min(a, n / 2)
    b = math.min(b, n / 2)
    math.min(a + b + c, n)
  }
}
'''

FILES["3003_maximize_the_number_of_partitions_after_operations"] = r'''// LeetCode 3003 - Maximize the Number of Partitions After Operations
// https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

object Solution {
  private def popcount(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x != 0) { c += x & 1; x >>= 1 }
    c
  }

  def maxPartitionsAfterOperations(s: String, k: Int): Int = {
    val n = s.length
    val memo = scala.collection.mutable.HashMap[Long, Int]()
    def key(i: Int, cur: Int, t: Int): Long = (i.toLong << 32) | (cur.toLong << 1) | t
    def dfs(i: Int, cur: Int, t: Int): Int = {
      if (i >= n) return 1
      val kkey = key(i, cur, t)
      if (memo.contains(kkey)) return memo(kkey)
      val v = 1 << (s.charAt(i) - 'a')
      var nxt = cur | v
      var ans = if (popcount(nxt) > k) dfs(i + 1, v, t) + 1 else dfs(i + 1, nxt, t)
      if (t > 0) {
        var j = 0
        while (j < 26) {
          nxt = cur | (1 << j)
          if (popcount(nxt) > k) ans = math.max(ans, dfs(i + 1, 1 << j, 0) + 1)
          else ans = math.max(ans, dfs(i + 1, nxt, 0))
          j += 1
        }
      }
      memo(kkey) = ans
      ans
    }
    dfs(0, 0, 1)
  }
}
'''

FILES["3004_maximum_subtree_of_the_same_color"] = r'''// LeetCode 3004 - Maximum Subtree of the Same Color
// https://leetcode.com/problems/maximum-subtree-of-the-same-color/

object Solution {
  def maximumSubtreeSize(edges: Array[Array[Int]], colors: Array[Int]): Int = {
    val n = edges.length + 1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val size = Array.ofDim[Int](n)
    var ans = 0
    def dfs(a: Int, fa: Int): Boolean = {
      size(a) = 1
      var ok = true
      for (b <- g(a) if b != fa) {
        val t = dfs(b, a)
        ok = ok && t && colors(a) == colors(b)
        size(a) += size(b)
      }
      if (ok) ans = math.max(ans, size(a))
      ok
    }
    dfs(0, -1)
    ans
  }
}
'''

FILES["3005_count_elements_with_maximum_frequency"] = r'''// LeetCode 3005 - Count Elements With Maximum Frequency
// https://leetcode.com/problems/count-elements-with-maximum-frequency/

object Solution {
  def maxFrequencyElements(nums: Array[Int]): Int = {
    val cnt = Array.ofDim[Int](101)
    for (x <- nums) cnt(x) += 1
    var mx = -1
    var ans = 0
    for (x <- cnt) {
      if (mx < x) { mx = x; ans = x }
      else if (mx == x) ans += x
    }
    ans
  }
}
'''

FILES["3006_find_beautiful_indices_in_the_given_array_i"] = r'''// LeetCode 3006 - Find Beautiful Indices in the Given Array I
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

object Solution {
  private def buildLPS(lps: Array[Int], pattern: String): Unit = {
    var l = 0
    var i = 1
    val sl = pattern.length
    lps(0) = 0
    while (i < sl) {
      if (pattern.charAt(i) == pattern.charAt(l)) {
        l += 1
        lps(i) = l
        i += 1
      } else if (l != 0) l = lps(l - 1)
      else { lps(i) = l; i += 1 }
    }
  }

  private def kmp(s: String, pat: String, lps: Array[Int], index: scala.collection.mutable.ArrayBuffer[Int]): Unit = {
    val sLen = s.length
    val patL = pat.length
    var i = 0
    var j = 0
    while (sLen - i >= patL - j) {
      if (s.charAt(i) == pat.charAt(j)) { i += 1; j += 1 }
      if (j == patL) {
        index += (i - patL)
        j = lps(j - 1)
      } else if (i < sLen && s.charAt(i) != pat.charAt(j)) {
        if (j != 0) j = lps(j - 1) else i += 1
      }
    }
  }

  def beautifulIndices(s: String, a: String, b: String, k: Int): List[Int] = {
    val lpsA = Array.ofDim[Int](a.length)
    val lpsB = Array.ofDim[Int](b.length)
    val aIndex = scala.collection.mutable.ArrayBuffer.empty[Int]
    val bIndex = scala.collection.mutable.ArrayBuffer.empty[Int]
    val result = scala.collection.mutable.ListBuffer.empty[Int]
    buildLPS(lpsA, a)
    buildLPS(lpsB, b)
    kmp(s, a, lpsA, aIndex)
    kmp(s, b, lpsB, bIndex)
    var i = 0
    var j = 0
    while (i < aIndex.length && j < bIndex.length) {
      if (aIndex(i) + k >= bIndex(j) && aIndex(i) - k <= bIndex(j)) {
        result += aIndex(i)
        i += 1
      } else if (aIndex(i) - k > bIndex(j)) j += 1
      else i += 1
    }
    result.toList
  }
}
'''

FILES["3007_maximum_number_that_sum_of_the_prices_is_less_than_or_equal_to_k"] = r'''// LeetCode 3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
// https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

object Solution {
  def findMaximumNumber(k: Long, x: Int): Long = {
    var num = 0L
    var f = Array.ofDim[Long](65, 65)
    def dfs(pos: Int, cnt: Int, limit: Boolean): Long = {
      if (pos == 0) return cnt
      if (!limit && f(pos)(cnt) != -1) return f(pos)(cnt)
      var ans = 0L
      val up = if (limit) ((num >> (pos - 1)) & 1).toInt else 1
      var i = 0
      while (i <= up) {
        var v = cnt
        if (i == 1 && pos % x == 0) v += 1
        ans += dfs(pos - 1, v, limit && i == up)
        i += 1
      }
      if (!limit) f(pos)(cnt) = ans
      ans
    }
    var l = 1L
    var r = 100000000000000000L
    while (l < r) {
      val mid = (l + r + 1) >> 1
      num = mid
      var m = 0
      var t = num
      while (t > 0) { m += 1; t >>= 1 }
      var i = 0
      while (i < 65) {
        var j = 0
        while (j < 65) { f(i)(j) = -1; j += 1 }
        i += 1
      }
      if (dfs(m, 0, true) <= k) l = mid else r = mid - 1
    }
    l
  }
}
'''

FILES["3008_find_beautiful_indices_in_the_given_array_ii"] = r'''// LeetCode 3008 - Find Beautiful Indices in the Given Array II
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/

object Solution {
  private def buildLPS(lps: Array[Int], pattern: String): Unit = {
    var l = 0
    var i = 1
    val sl = pattern.length
    lps(0) = 0
    while (i < sl) {
      if (pattern.charAt(i) == pattern.charAt(l)) {
        l += 1
        lps(i) = l
        i += 1
      } else if (l != 0) l = lps(l - 1)
      else { lps(i) = l; i += 1 }
    }
  }

  private def kmp(s: String, pat: String, lps: Array[Int], index: scala.collection.mutable.ArrayBuffer[Int]): Unit = {
    val sLen = s.length
    val patL = pat.length
    var i = 0
    var j = 0
    while (sLen - i >= patL - j) {
      if (s.charAt(i) == pat.charAt(j)) { i += 1; j += 1 }
      if (j == patL) {
        index += (i - patL)
        j = lps(j - 1)
      } else if (i < sLen && s.charAt(i) != pat.charAt(j)) {
        if (j != 0) j = lps(j - 1) else i += 1
      }
    }
  }

  def beautifulIndices(s: String, a: String, b: String, k: Int): List[Int] = {
    val lpsA = Array.ofDim[Int](a.length)
    val lpsB = Array.ofDim[Int](b.length)
    val aIndex = scala.collection.mutable.ArrayBuffer.empty[Int]
    val bIndex = scala.collection.mutable.ArrayBuffer.empty[Int]
    val result = scala.collection.mutable.ListBuffer.empty[Int]
    buildLPS(lpsA, a)
    buildLPS(lpsB, b)
    kmp(s, a, lpsA, aIndex)
    kmp(s, b, lpsB, bIndex)
    var i = 0
    var j = 0
    while (i < aIndex.length && j < bIndex.length) {
      if (aIndex(i) + k >= bIndex(j) && aIndex(i) - k <= bIndex(j)) {
        result += aIndex(i)
        i += 1
      } else if (aIndex(i) - k > bIndex(j)) j += 1
      else i += 1
    }
    result.toList
  }
}
'''

FILES["3009_maximum_number_of_intersections_on_the_chart"] = r'''// LeetCode 3009 - Maximum Number of Intersections on the Chart
// https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

object Solution {
  def maxIntersectionCount(y: Array[Int]): Int = {
    val n = y.length
    val line = scala.collection.mutable.TreeMap[Int, Int]()
    var i = 1
    while (i < n) {
      val start = 2 * y(i - 1)
      var end = 2 * y(i)
      if (i != n - 1) {
        if (y(i) > y(i - 1)) end -= 1 else end += 1
      }
      var a = start
      var b = end
      if (a > b) { val t = a; a = b; b = t }
      line(a) = line.getOrElse(a, 0) + 1
      line(b + 1) = line.getOrElse(b + 1, 0) - 1
      i += 1
    }
    var ans = 0
    var cur = 0
    for (v <- line.values) {
      cur += v
      if (cur > ans) ans = cur
    }
    ans
  }
}
'''

FILES["3010_divide_an_array_into_subarrays_with_minimum_cost_i"] = r'''// LeetCode 3010 - Divide an Array Into Subarrays With Minimum Cost I
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

object Solution {
  def minimumCost(nums: Array[Int]): Int = {
    val a = nums(0)
    var b = 100
    var c = 100
    var i = 1
    while (i < nums.length) {
      val x = nums(i)
      if (x < b) { c = b; b = x }
      else if (x < c) c = x
      i += 1
    }
    a + b + c
  }
}
'''

FILES["3011_find_if_array_can_be_sorted"] = r'''// LeetCode 3011 - Find if Array Can Be Sorted
// https://leetcode.com/problems/find-if-array-can-be-sorted/

object Solution {
  private def popcount(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x != 0) { c += x & 1; x >>= 1 }
    c
  }

  def canSortArray(nums: Array[Int]): Boolean = {
    var preMx = 0
    var i = 0
    val n = nums.length
    while (i < n) {
      val cnt = popcount(nums(i))
      var j = i + 1
      var mi = nums(i)
      var mx = nums(i)
      while (j < n && popcount(nums(j)) == cnt) {
        mi = math.min(mi, nums(j))
        mx = math.max(mx, nums(j))
        j += 1
      }
      if (preMx > mi) return false
      preMx = mx
      i = j
    }
    true
  }
}
'''

FILES["3012_minimize_length_of_array_using_operations"] = r'''// LeetCode 3012 - Minimize Length of Array Using Operations
// https://leetcode.com/problems/minimize-length-of-array-using-operations/

object Solution {
  def minimumArrayLength(nums: Array[Int]): Int = {
    var mi = nums(0)
    for (x <- nums) if (x < mi) mi = x
    var cnt = 0
    for (x <- nums) {
      if (x % mi != 0) return 1
      if (x == mi) cnt += 1
    }
    (cnt + 1) / 2
  }
}
'''

FILES["3013_divide_an_array_into_subarrays_with_minimum_cost_ii"] = r'''// LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

object Solution {
  private class BITI(n_ : Int) {
    val n = n_
    val c = Array.ofDim[Int](n_ + 1)
    def upd(x0: Int, d: Int): Unit = {
      var x = x0
      while (x <= n) { c(x) += d; x += x & -x }
    }
    def qry(x0: Int): Int = {
      var x = x0
      var s = 0
      while (x > 0) { s += c(x); x -= x & -x }
      s
    }
  }
  private class BITL(n_ : Int) {
    val n = n_
    val c = Array.ofDim[Long](n_ + 1)
    def upd(x0: Int, d: Long): Unit = {
      var x = x0
      while (x <= n) { c(x) += d; x += x & -x }
    }
    def qry(x0: Int): Long = {
      var x = x0
      var s = 0L
      while (x > 0) { s += c(x); x -= x & -x }
      s
    }
  }

  private def kth(cnt: BITI, m: Int, k0: Int): Int = {
    var k = k0
    var idx = 0
    var bit = 1 << 20
    while (bit != 0) {
      val nidx = idx + bit
      if (nidx <= m && cnt.c(nidx) < k) {
        k -= cnt.c(nidx)
        idx = nidx
      }
      bit >>= 1
    }
    idx + 1
  }

  private def lowerBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (a(mid) < x) lo = mid + 1 else hi = mid
    }
    lo
  }

  private def sumSmallest(cnt: BITI, sum: BITL, uniq: Array[Int], m: Int, kk: Int): Long = {
    if (kk <= 0) return 0
    val r = kth(cnt, m, kk)
    val before = cnt.qry(r - 1)
    var s = sum.qry(r - 1)
    s += (kk - before).toLong * uniq(r - 1)
    s
  }

  def minimumCost(nums: Array[Int], k0: Int, dist: Int): Long = {
    val k = k0 - 1
    val n = nums.length
    val uniq0 = nums.clone()
    scala.util.Sorting.quickSort(uniq0)
    val tmp = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < uniq0.length) {
      if (tmp.isEmpty || uniq0(i) != tmp.last) tmp += uniq0(i)
      i += 1
    }
    val uniq = tmp.toArray
    val m = uniq.length
    val cnt = new BITI(m + 2)
    val sum = new BITL(m + 2)
    i = 1
    while (i <= math.min(dist + 1, n - 1)) {
      val r = lowerBound(uniq, nums(i)) + 1
      cnt.upd(r, 1)
      sum.upd(r, nums(i).toLong)
      i += 1
    }
    val end = math.min(dist + 1, n - 1)
    var kk = math.min(k, end)
    var ans = nums(0).toLong + sumSmallest(cnt, sum, uniq, m, kk)
    i = dist + 2
    while (i < n) {
      val rem = nums(i - dist - 1)
      val r1 = lowerBound(uniq, rem) + 1
      cnt.upd(r1, -1)
      sum.upd(r1, -rem.toLong)
      val add = nums(i)
      val r2 = lowerBound(uniq, add) + 1
      cnt.upd(r2, 1)
      sum.upd(r2, add.toLong)
      kk = math.min(k, dist + 1)
      ans = math.min(ans, nums(0).toLong + sumSmallest(cnt, sum, uniq, m, kk))
      i += 1
    }
    ans
  }
}
'''

FILES["3014_minimum_number_of_pushes_to_type_word_i"] = r'''// LeetCode 3014 - Minimum Number of Pushes to Type Word I
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

object Solution {
  def minimumPushes(word: String): Int = {
    val n = word.length
    var ans = 0
    var k = 1
    var i = 0
    while (i < n / 8) {
      ans += k * 8
      k += 1
      i += 1
    }
    ans += k * (n % 8)
    ans
  }
}
'''

FILES["3015_count_the_number_of_houses_at_a_certain_distance_i"] = r'''// LeetCode 3015 - Count the Number of Houses at a Certain Distance I
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

object Solution {
  def countOfPairs(n: Int, x0: Int, y0: Int): Array[Int] = {
    val ans = Array.ofDim[Int](n)
    val x = x0 - 1
    val y = y0 - 1
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        val a = j - i
        val b = math.abs(x - i) + math.abs(y - j) + 1
        val c = math.abs(x - j) + math.abs(y - i) + 1
        ans(math.min(a, math.min(b, c)) - 1) += 2
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3016_minimum_number_of_pushes_to_type_word_ii"] = r'''// LeetCode 3016 - Minimum Number of Pushes to Type Word II
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

object Solution {
  def minimumPushes(word: String): Int = {
    val cnt = Array.ofDim[Int](26)
    var i = 0
    while (i < word.length) { cnt(word.charAt(i) - 'a') += 1; i += 1 }
    scala.util.Sorting.quickSort(cnt)
    var ans = 0
    i = 0
    while (i < 26) {
      ans += (i / 8 + 1) * cnt(26 - i - 1)
      i += 1
    }
    ans
  }
}
'''

FILES["3017_count_the_number_of_houses_at_a_certain_distance_ii"] = r'''// LeetCode 3017 - Count the Number of Houses at a Certain Distance II
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

object Solution {
  def countOfPairs(n: Int, x0: Int, y0: Int): Array[Long] = {
    var x = x0
    var y = y0
    if (x > y) { val t = x; x = y; y = t }
    val A = Array.ofDim[Long](n)
    var i = 1
    while (i <= n) {
      A(0) += 2
      A(math.min(i - 1, math.abs(i - y) + x).toInt) -= 1
      A(math.min(n - i, math.abs(i - x) + 1 + (n - y)).toInt) -= 1
      A(math.min(math.abs(i - x), math.abs(y - i) + 1).toInt) += 1
      A(math.min(math.abs(i - x) + 1, math.abs(y - i)).toInt) += 1
      val r = math.max(x - i, 0) + math.max(i - y, 0)
      A((r + (y - x) / 2).toInt) -= 1
      A((r + (y - x + 1) / 2).toInt) -= 1
      i += 1
    }
    i = 1
    while (i < n) { A(i) += A(i - 1); i += 1 }
    A
  }
}
'''

FILES["3018_maximum_number_of_removal_queries_that_can_be_processed_i"] = r'''// LeetCode 3018 - Maximum Number of Removal Queries That Can Be Processed I
// https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

object Solution {
  def maximumProcessableQueries(nums: Array[Int], queries: Array[Int]): Int = {
    val n = nums.length
    val f = Array.ofDim[Int](n, n)
    val m = queries.length
    var i = 0
    while (i < n) {
      var j = n - 1
      while (j >= i) {
        if (i > 0) {
          val t = if (f(i - 1)(j) < m && nums(i - 1) >= queries(f(i - 1)(j))) 1 else 0
          f(i)(j) = math.max(f(i)(j), f(i - 1)(j) + t)
        }
        if (j + 1 < n) {
          val t = if (f(i)(j + 1) < m && nums(j + 1) >= queries(f(i)(j + 1))) 1 else 0
          f(i)(j) = math.max(f(i)(j), f(i)(j + 1) + t)
        }
        if (f(i)(j) == m) return m
        j -= 1
      }
      i += 1
    }
    var ans = 0
    i = 0
    while (i < n) {
      val t = if (f(i)(i) < m && nums(i) >= queries(f(i)(i))) 1 else 0
      ans = math.max(ans, f(i)(i) + t)
      i += 1
    }
    ans
  }
}
'''

FILES["3019_number_of_changing_keys"] = r'''// LeetCode 3019 - Number of Changing Keys
// https://leetcode.com/problems/number-of-changing-keys/

object Solution {
  def countKeyChanges(s0: String): Int = {
    val s = s0.toLowerCase
    var ans = 0
    var i = 1
    while (i < s.length) {
      if (s.charAt(i) != s.charAt(i - 1)) ans += 1
      i += 1
    }
    ans
  }
}
'''

FILES["3020_find_the_maximum_number_of_elements_in_subset"] = r'''// LeetCode 3020 - Find the Maximum Number of Elements in Subset
// https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

object Solution {
  def maximumLength(nums: Array[Int]): Int = {
    val cnt = scala.collection.mutable.HashMap[Long, Int]()
    for (x <- nums) cnt(x.toLong) = cnt.getOrElse(x.toLong, 0) + 1
    val ones = cnt.getOrElse(1L, 0)
    var ans = ones - ((ones % 2) ^ 1)
    cnt.remove(1L)
    val keys = cnt.keys.toList
    for (start <- keys) {
      var x = start
      var t = 0
      while (cnt.getOrElse(x, 0) > 1) {
        x = x * x
        t += 2
      }
      if (cnt.getOrElse(x, 0) > 0) t += 1 else t -= 1
      ans = math.max(ans, t)
    }
    ans
  }
}
'''

FILES["3021_alice_and_bob_playing_flower_game"] = r'''// LeetCode 3021 - Alice and Bob Playing Flower Game
// https://leetcode.com/problems/alice-and-bob-playing-flower-game/

object Solution {
  def flowerGame(n: Int, m: Int): Long = {
    val a1 = (n + 1) / 2
    val b1 = (m + 1) / 2
    val a2 = n / 2
    val b2 = m / 2
    a1.toLong * b2 + a2.toLong * b1
  }
}
'''

FILES["3022_minimize_or_of_remaining_elements_using_operations"] = r'''// LeetCode 3022 - Minimize OR of Remaining Elements Using Operations
// https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

object Solution {
  def minOrAfterOperations(nums: Array[Int], k: Int): Int = {
    var ans = 0
    var rans = 0
    var i = 29
    while (i >= 0) {
      val test = ans + (1 << i)
      var cnt = 0
      var value = 0
      for (num <- nums) {
        if (value == 0) value = test & num
        else value &= test & num
        if (value != 0) cnt += 1
      }
      if (cnt > k) rans += (1 << i)
      else ans += (1 << i)
      i -= 1
    }
    rans
  }
}
'''

FILES["3023_find_pattern_in_infinite_stream_i"] = r'''// LeetCode 3023 - Find Pattern in Infinite Stream I
// https://leetcode.com/problems/find-pattern-in-infinite-stream-i/

class InfiniteStream(_bits: Array[Int]) {
  private val bits = _bits
  private var i = 0
  def next(): Int = { val v = bits(i); i += 1; v }
}

object Solution {
  def findPattern(stream: InfiniteStream, pattern: Array[Int]): Int = {
    var a = 0
    var b = 0
    val m = pattern.length
    val half = m >> 1
    val mask1 = (1 << half) - 1
    val mask2 = (1 << (m - half)) - 1
    var i = 0
    while (i < half) { a |= pattern(i) << (half - 1 - i); i += 1 }
    i = half
    while (i < m) { b |= pattern(i) << (m - 1 - i); i += 1 }
    var x = 0
    var y = 0
    i = 1
    while (true) {
      var v = stream.next()
      y = y << 1 | v
      v = (y >> (m - half)) & 1
      y &= mask2
      x = x << 1 | v
      x &= mask1
      if (i >= m && a == x && b == y) return i - m
      i += 1
    }
    -1
  }
}
'''

FILES["3024_type_of_triangle"] = r'''// LeetCode 3024 - Type of Triangle
// https://leetcode.com/problems/type-of-triangle/

object Solution {
  def triangleType(nums: Array[Int]): String = {
    scala.util.Sorting.quickSort(nums)
    if (nums(0) + nums(1) <= nums(2)) "none"
    else if (nums(0) == nums(2)) "equilateral"
    else if (nums(0) == nums(1) || nums(1) == nums(2)) "isosceles"
    else "scalene"
  }
}
'''

def main():
    n = 0
    for folder, content in FILES.items():
        (ROOT / folder / "Solution.scala").write_text(content, encoding="utf-8", newline="\n")
        n += 1
        print("wrote", folder)
    print("total", n)

if __name__ == "__main__":
    main()
