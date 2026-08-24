#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("3719_longest_balanced_subarray_i", r'''
// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

object Solution {
  def longestBalanced(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      val vis = new java.util.HashSet[Integer]()
      val cnt = Array(0, 0)
      var j = i
      while (j < n) {
        if (!vis.contains(nums(j))) {
          vis.add(nums(j))
          cnt(nums(j) & 1) += 1
        }
        if (cnt(0) == cnt(1)) ans = math.max(ans, j - i + 1)
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("3720_lexicographically_smallest_permutation_greater_than_target", r'''
// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

object Solution {
  def lexGreaterPermutation(s: String, target: String): String = {
    val cnt = Array.fill(26)(0)
    s.foreach(c => cnt(c - 'a') += 1)
    val n = s.length
    val ans = new Array[Char](n)

    def dfs(pos: Int, greater: Boolean): Boolean = {
      if (pos == n) return greater
      val start = if (greater) 0 else target.charAt(pos) - 'a'
      var c = start
      while (c < 26) {
        if (cnt(c) != 0) {
          cnt(c) -= 1
          ans(pos) = ('a' + c).toChar
          val ng = greater || c > (target.charAt(pos) - 'a')
          if (dfs(pos + 1, ng)) return true
          cnt(c) += 1
        }
        c += 1
      }
      false
    }

    if (dfs(0, false)) new String(ans) else ""
  }
}
''')

w("3721_longest_balanced_subarray_ii", r'''
// LeetCode 3721 - Longest Balanced Subarray II
// https://leetcode.com/problems/longest-balanced-subarray-ii/

object Solution {
  private class Node {
    var l: Int = 0
    var r: Int = 0
    var mn: Int = 0
    var mx: Int = 0
    var lazy: Int = 0
  }

  private class SegmentTree(n: Int) {
    val tr: Array[Node] = Array.fill(n << 2)(new Node())
    build(1, 0, n)

    def build(u: Int, l: Int, r: Int): Unit = {
      tr(u).l = l; tr(u).r = r; tr(u).mn = 0; tr(u).mx = 0; tr(u).lazy = 0
      if (l == r) return
      val mid = (l + r) >> 1
      build(u << 1, l, mid)
      build(u << 1 | 1, mid + 1, r)
    }

    def apply(u: Int, v: Int): Unit = {
      tr(u).mn += v
      tr(u).mx += v
      tr(u).lazy += v
    }

    def pushup(u: Int): Unit = {
      tr(u).mn = math.min(tr(u << 1).mn, tr(u << 1 | 1).mn)
      tr(u).mx = math.max(tr(u << 1).mx, tr(u << 1 | 1).mx)
    }

    def pushdown(u: Int): Unit = {
      if (tr(u).lazy != 0) {
        val v = tr(u).lazy
        apply(u << 1, v)
        apply(u << 1 | 1, v)
        tr(u).lazy = 0
      }
    }

    def modify(u: Int, l: Int, r: Int, v: Int): Unit = {
      if (tr(u).l >= l && tr(u).r <= r) {
        apply(u, v)
        return
      }
      pushdown(u)
      val mid = (tr(u).l + tr(u).r) >> 1
      if (l <= mid) modify(u << 1, l, r, v)
      if (r > mid) modify(u << 1 | 1, l, r, v)
      pushup(u)
    }

    def query(u: Int, target: Int): Int = {
      if (tr(u).l == tr(u).r) return tr(u).l
      pushdown(u)
      val left = u << 1
      val right = u << 1 | 1
      if (tr(left).mn <= target && target <= tr(left).mx) query(left, target)
      else query(right, target)
    }
  }

  def longestBalanced(nums: Array[Int]): Int = {
    val n = nums.length
    val st = new SegmentTree(n)
    val last = new java.util.HashMap[Integer, Integer]()
    var now = 0
    var ans = 0
    var i = 1
    while (i <= n) {
      val x = nums(i - 1)
      val det = if ((x & 1) != 0) 1 else -1
      if (last.containsKey(x)) {
        st.modify(1, last.get(x), n, -det)
        now -= det
      }
      last.put(x, i)
      st.modify(1, i, n, det)
      now += det
      val pos = st.query(1, now)
      ans = math.max(ans, i - pos)
      i += 1
    }
    ans
  }
}
''')

w("3722_lexicographically_smallest_string_after_reverse", r'''
// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

object Solution {
  def lexSmallest(s: String): String = {
    var ans = s
    val n = s.length
    var k = 1
    while (k <= n) {
      val a1 = s.toCharArray
      reverse(a1, 0, 0 + k)
      val t1 = new String(a1)
      val a2 = s.toCharArray
      reverse(a2, n - k, n - k + k)
      val t2 = new String(a2)
      if (t1.compareTo(ans) < 0) ans = t1
      if (t2.compareTo(ans) < 0) ans = t2
      k += 1
    }
    ans
  }

  private def reverse(a: Array[Char], l: Int, r: Int): Unit = {
    var i = l
    var j = r - 1
    while (i < j) {
      val t = a(i); a(i) = a(j); a(j) = t
      i += 1
      j -= 1
    }
  }
}
''')

w("3723_maximize_sum_of_squares_of_digits", r'''
// LeetCode 3723 - Maximize Sum Of Squares Of Digits
// https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

object Solution {
  def maxSumOfSquares(num: Int, sum: Int): String = {
    if (num * 9 < sum) return ""
    val k = sum / 9
    val s = sum % 9
    val ans = new StringBuilder
    var i = 0
    while (i < k) {
      ans.append('9')
      i += 1
    }
    if (s > 0) ans.append(('0' + s).toChar)
    while (ans.length < num) ans.append('0')
    ans.toString
  }
}
''')

w("3724_minimum_operations_to_transform_array", r'''
// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

object Solution {
  def minOperations(nums1: Array[Int], nums2: Array[Int]): Long = {
    var ans = 1L
    val n = nums1.length
    var ok = false
    var d = 1 << 30
    var i = 0
    while (i < n) {
      val x = math.max(nums1(i), nums2(i))
      val y = math.min(nums1(i), nums2(i))
      ans += x - y
      d = math.min(d, math.min(math.abs(x - nums2(n)), math.abs(y - nums2(n))))
      if (nums2(n) >= y && nums2(n) <= x) ok = true
      i += 1
    }
    if (!ok) ans += d
    ans
  }
}
''')

w("3725_count_ways_to_choose_coprime_integers_from_rows", r'''
// LeetCode 3725 - Count Ways To Choose Coprime Integers From Rows
// https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

object Solution {
  def countCoprime(mat: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val m = mat.length
    var dp = new java.util.HashMap[Integer, Integer]()
    mat(0).foreach { v =>
      dp.merge(v, 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
    }
    var i = 1
    while (i < m) {
      val ndp = new java.util.HashMap[Integer, Integer]()
      mat(i).foreach { v =>
        val it = dp.entrySet().iterator()
        while (it.hasNext) {
          val e = it.next()
          val ng = gcd(e.getKey, v)
          ndp.merge(ng, e.getValue, (a: Integer, b: Integer) => Integer.valueOf((a + b) % MOD))
        }
      }
      dp = ndp
      i += 1
    }
    dp.getOrDefault(1, 0)
  }

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
}
''')

w("3726_remove_zeros_in_decimal_representation", r'''
// LeetCode 3726 - Remove Zeros in Decimal Representation
// https://leetcode.com/problems/remove-zeros-in-decimal-representation/

object Solution {
  def removeZeros(n0: Long): Long = {
    var n = n0
    var ans = 0L
    var k = 1L
    while (n > 0) {
      val x = n % 10
      if (x > 0) {
        ans = k * x + ans
        k *= 10
      }
      n /= 10
    }
    ans
  }
}
''')

w("3727_maximum_alternating_sum_of_squares", r'''
// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

object Solution {
  def maxAlternatingSum(nums: Array[Int]): Long = {
    var i = 0
    while (i < nums.length) {
      nums(i) *= nums(i)
      i += 1
    }
    java.util.Arrays.sort(nums)
    val m = nums.length / 2
    var ans = 0L
    i = 0
    while (i < m) {
      ans -= nums(i)
      i += 1
    }
    i = m
    while (i < nums.length) {
      ans += nums(i)
      i += 1
    }
    ans
  }
}
''')

w("3728_stable_subarrays_with_equal_boundary_and_interior_sum", r'''
// LeetCode 3728 - Stable Subarrays With Equal Boundary And Interior Sum
// https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

object Solution {
  def countStableSubarrays(capacity: Array[Int]): Long = {
    val n = capacity.length
    val s = new Array[Long](n + 1)
    var i = 1
    while (i <= n) {
      s(i) = s(i - 1) + capacity(i - 1)
      i += 1
    }
    val cnt = new java.util.HashMap[String, Integer]()
    var ans = 0L
    var r = 2
    while (r < n) {
      val l = r - 2
      val keyL = capacity(l) + "#" + (capacity(l) + s(l + 1))
      cnt.merge(keyL, 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
      val keyR = capacity(r) + "#" + s(r)
      ans += cnt.getOrDefault(keyR, 0)
      r += 1
    }
    ans
  }
}
''')

w("3729_count_distinct_subarrays_divisible_by_k_in_sorted_array", r'''
// LeetCode 3729 - Count Distinct Subarrays Divisible By K In Sorted Array
// https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

object Solution {
  def numGoodSubarrays(nums: Array[Int], k: Int): Long = {
    var ans = 0L
    var s = 0
    val cnt = new java.util.HashMap[Integer, Integer]()
    cnt.put(0, 1)
    nums.foreach { x =>
      s = (s + x) % k
      ans += cnt.getOrDefault(s, 0)
      cnt.merge(s, 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
    }
    val n = nums.length
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n && nums(j) == nums(i)) j += 1
      val m = j - i
      var h = 1
      while (h <= m) {
        if (1L * nums(i) * h % k == 0) ans -= (m - h)
        h += 1
      }
      i = j
    }
    ans
  }
}
''')

w("3730_maximum_calories_burnt_from_jumps", r'''
// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

object Solution {
  def maxCaloriesBurnt(heights: Array[Int]): Long = {
    java.util.Arrays.sort(heights)
    var ans = 0L
    var pre = 0
    var l = 0
    var r = heights.length - 1
    while (l < r) {
      val d1 = heights(r).toLong - pre
      ans += d1 * d1
      val d2 = heights(l).toLong - heights(r)
      ans += d2 * d2
      pre = heights(l)
      l += 1
      r -= 1
    }
    val d = heights(r).toLong - pre
    ans += d * d
    ans
  }
}
''')

w("3731_find_missing_elements", r'''
// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

object Solution {
  def findMissingElements(nums: Array[Int]): Array[Int] = {
    var mn = 100
    var mx = 0
    val s = new java.util.HashSet[Integer]()
    nums.foreach { x =>
      mn = math.min(mn, x)
      mx = math.max(mx, x)
      s.add(x)
    }
    val ans = new java.util.ArrayList[Integer]()
    var x = mn + 1
    while (x < mx) {
      if (!s.contains(x)) ans.add(x)
      x += 1
    }
    val out = new Array[Int](ans.size())
    var i = 0
    while (i < out.length) {
      out(i) = ans.get(i)
      i += 1
    }
    out
  }
}
''')

w("3732_maximum_product_of_three_elements_after_one_replacement", r'''
// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

object Solution {
  def maxProduct(nums: Array[Int]): Long = {
    java.util.Arrays.sort(nums)
    val n = nums.length
    val a = nums(0).toLong
    val b = nums(1).toLong
    val c = nums(n - 2).toLong
    val d = nums(n - 1).toLong
    val x = 100000L
    math.max(math.max(a * b * x, c * d * x), -a * d * x)
  }
}
''')

w("3733_minimum_time_to_complete_all_deliveries", r'''
// LeetCode 3733 - Minimum Time To Complete All Deliveries
// https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

object Solution {
  def minimumTime(d: Array[Int], r: Array[Int]): Long = {
    var lo = 1L
    var hi = 8e18.toLong
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (ok(mid, d, r)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(T: Long, d: Array[Int], r: Array[Int]): Boolean = {
    val w0 = T - T / r(0)
    val w1 = T - T / r(1)
    w0 + w1 >= d(0).toLong + d(1)
  }
}
''')

w("3734_lexicographically_smallest_palindromic_permutation_greater_than_target", r'''
// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

object Solution {
  def lexPalindromicPermutation(s: String, target: String): String = {
    val cnt = Array.fill(26)(0)
    s.foreach(c => cnt(c - 'a') += 1)
    var odd = 0
    var mid = -1
    var i = 0
    while (i < 26) {
      if (cnt(i) % 2 == 1) { odd += 1; mid = i }
      i += 1
    }
    if (odd > 1) return ""
    val half = Array.fill(26)(0)
    i = 0
    while (i < 26) {
      half(i) = cnt(i) / 2
      i += 1
    }
    val n = s.length
    val halfLen = n / 2
    val left = new Array[Char](halfLen)

    def dfs(pos: Int, greater: Boolean): Boolean = {
      if (pos == halfLen) {
        if (mid >= 0) {
          if (greater) return true
          return ('a' + mid).toChar > target.charAt(halfLen)
        }
        return greater
      }
      val start = if (greater) 0 else target.charAt(pos) - 'a'
      var c = start
      while (c < 26) {
        if (half(c) != 0) {
          half(c) -= 1
          left(pos) = ('a' + c).toChar
          if (dfs(pos + 1, greater || c > (target.charAt(pos) - 'a'))) return true
          half(c) += 1
        }
        c += 1
      }
      false
    }

    if (!dfs(0, false)) return ""
    val res = new StringBuilder
    res.append(left)
    if (mid >= 0) res.append(('a' + mid).toChar)
    i = halfLen - 1
    while (i >= 0) {
      res.append(left(i))
      i -= 1
    }
    val out = res.toString
    if (out.compareTo(target) <= 0) "" else out
  }
}
''')

w("3735_lexicographically_smallest_string_after_reverse_ii", r'''
// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

object Solution {
  def lexSmallest(s: String): String = {
    val n = s.length
    var best = s
    var i = 1
    while (i <= n) {
      val t = s.toCharArray
      reverse(t, 0, 0 + i)
      val ts = new String(t)
      if (ts.compareTo(best) < 0) best = ts
      i += 1
    }
    i = 0
    while (i < n) {
      val t = s.toCharArray
      reverse(t, i, i + n - i)
      val ts = new String(t)
      if (ts.compareTo(best) < 0) best = ts
      i += 1
    }
    best
  }

  private def reverse(a: Array[Char], l: Int, r: Int): Unit = {
    var i = l
    var j = r - 1
    while (i < j) {
      val t = a(i); a(i) = a(j); a(j) = t
      i += 1
      j -= 1
    }
  }
}
''')

w("3736_minimum_moves_to_equal_array_elements_iii", r'''
// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

object Solution {
  def minMoves(nums: Array[Int]): Int = {
    var mx = 0
    var s = 0
    nums.foreach { x =>
      mx = math.max(mx, x)
      s += x
    }
    mx * nums.length - s
  }
}
''')

w("3737_count_subarrays_with_majority_element_i", r'''
// LeetCode 3737 - Count Subarrays With Majority Element I
// https://leetcode.com/problems/count-subarrays-with-majority-element-i/

object Solution {
  def countMajoritySubarrays(nums: Array[Int], target: Int): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      var cnt = 0
      var j = i
      while (j < n) {
        if (nums(j) == target) cnt += 1
        if (cnt * 2 > j - i + 1) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("3738_longest_non_decreasing_subarray_after_replacing_at_most_one_element", r'''
// LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

object Solution {
  def longestSubarray(nums: Array[Int]): Int = {
    val n = nums.length
    val left = Array.fill(n)(1)
    val right = Array.fill(n)(1)
    var i = 1
    while (i < n) {
      if (nums(i) >= nums(i - 1)) left(i) = left(i - 1) + 1
      i += 1
    }
    i = n - 2
    while (i >= 0) {
      if (nums(i) <= nums(i + 1)) right(i) = right(i + 1) + 1
      i -= 1
    }
    var ans = 0
    left.foreach(v => ans = math.max(ans, v))
    i = 0
    while (i < n) {
      val a = if (i > 0) left(i - 1) else 0
      val b = if (i + 1 < n) right(i + 1) else 0
      if (i > 0 && i + 1 < n && nums(i - 1) > nums(i + 1)) {
        ans = math.max(ans, math.max(a + 1, b + 1))
      } else {
        ans = math.max(ans, a + b + 1)
      }
      i += 1
    }
    ans
  }
}
''')

w("3739_count_subarrays_with_majority_element_ii", r'''
// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

object Solution {
  private class BIT(n_ : Int) {
    val n: Int = n_
    val c: Array[Int] = new Array[Int](n_ + 1)
    def update(x0: Int, delta: Int): Unit = {
      var x = x0
      while (x <= n) {
        c(x) += delta
        x += x & -x
      }
    }
    def query(x0: Int): Int = {
      var x = x0
      var s = 0
      while (x > 0) {
        s += c(x)
        x -= x & -x
      }
      s
    }
  }

  def countMajoritySubarrays(nums: Array[Int], target: Int): Long = {
    val n = nums.length
    val tree = new BIT(2 * n + 1)
    var s = n + 1
    tree.update(s, 1)
    var ans = 0L
    nums.foreach { x =>
      if (x == target) s += 1 else s -= 1
      ans += tree.query(s - 1)
      tree.update(s, 1)
    }
    ans
  }
}
''')

w("3740_minimum_distance_between_three_equal_elements_i", r'''
// LeetCode 3740 - Minimum Distance Between Three Equal Elements I
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

object Solution {
  def minimumDistance(nums: Array[Int]): Int = {
    val g = new java.util.HashMap[Integer, java.util.List[Integer]]()
    var i = 0
    while (i < nums.length) {
      g.computeIfAbsent(nums(i), _ => new java.util.ArrayList[Integer]()).add(i)
      i += 1
    }
    val inf = 1 << 30
    var ans = inf
    val it = g.values().iterator()
    while (it.hasNext) {
      val ls = it.next()
      val m = ls.size()
      var h = 0
      while (h < m - 2) {
        ans = math.min(ans, (ls.get(h + 2) - ls.get(h)) * 2)
        h += 1
      }
    }
    if (ans == inf) -1 else ans
  }
}
''')

w("3741_minimum_distance_between_three_equal_elements_ii", r'''
// LeetCode 3741 - Minimum Distance Between Three Equal Elements II
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

object Solution {
  def minimumDistance(nums: Array[Int]): Int = {
    val g = new java.util.HashMap[Integer, java.util.List[Integer]]()
    var i = 0
    while (i < nums.length) {
      g.computeIfAbsent(nums(i), _ => new java.util.ArrayList[Integer]()).add(i)
      i += 1
    }
    val inf = 1 << 30
    var ans = inf
    val it = g.values().iterator()
    while (it.hasNext) {
      val ls = it.next()
      val m = ls.size()
      var h = 0
      while (h < m - 2) {
        ans = math.min(ans, (ls.get(h + 2) - ls.get(h)) * 2)
        h += 1
      }
    }
    if (ans == inf) -1 else ans
  }
}
''')

w("3742_maximum_path_score_in_a_grid", r'''
// LeetCode 3742 - Maximum Path Score In A Grid
// https://leetcode.com/problems/maximum-path-score-in-a-grid/

object Solution {
  private val INF = 1 << 30

  def maxPathScore(grid: Array[Array[Int]], k: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    val f = Array.fill(m, n, k + 1)(-1)

    def dfs(i: Int, j: Int, kk: Int): Int = {
      if (i < 0 || j < 0 || kk < 0) return -INF
      if (i == 0 && j == 0) return 0
      if (f(i)(j)(kk) != -1) return f(i)(j)(kk)
      var res = grid(i)(j)
      var nk = kk
      if (grid(i)(j) != 0) nk -= 1
      val a = dfs(i - 1, j, nk)
      val b = dfs(i, j - 1, nk)
      res += math.max(a, b)
      f(i)(j)(kk) = res
      res
    }

    val ans = dfs(m - 1, n - 1, k)
    if (ans < 0) -1 else ans
  }
}
''')

w("3743_maximize_cyclic_partition_score", r'''
// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize-cyclic-partition-score/

object Solution {
  def maximumScore(nums: Array[Int], k0: Int): Long = {
    val n = nums.length
    val a = new Array[Int](n * 2)
    System.arraycopy(nums, 0, a, 0, n)
    System.arraycopy(nums, 0, a, n, n)
    var k = k0
    if (k > n) k = n
    var best = 0L
    val NEG = -(1L << 60)
    var start = 0
    while (start < n) {
      val seg = java.util.Arrays.copyOfRange(a, start, start + n)
      val dp = Array.fill(n + 1, k + 1)(NEG)
      dp(0)(0) = 0
      var i = 1
      while (i <= n) {
        var j = 1
        while (j <= k && j <= i) {
          var mx = NEG
          var t = i
          while (t >= j) {
            if (seg(t - 1) > mx) mx = seg(t - 1)
            if (dp(t - 1)(j - 1) > NEG) {
              val cand = dp(t - 1)(j - 1) + mx
              if (cand > dp(i)(j)) dp(i)(j) = cand
            }
            t -= 1
          }
          j += 1
        }
        i += 1
      }
      if (dp(n)(k) > best) best = dp(n)(k)
      start += 1
    }
    best
  }
}
''')
