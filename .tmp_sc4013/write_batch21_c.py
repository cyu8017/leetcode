#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("3872_longest_arithmetic_sequence_after_changing_at_most_one_element", r'''
// LeetCode 3872 - Longest Arithmetic Sequence After Changing At Most One Element
// https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

object Solution {
  def longestArithmetic(nums: Array[Int]): Int = {
    val n = nums.length
    val d = new Array[Int](n)
    var i = 1
    while (i < n) {
      d(i) = nums(i) - nums(i - 1)
      i += 1
    }
    val f = Array.fill(n)(2)
    val g = Array.fill(n)(2)
    f(0) = 1
    g(n - 1) = 1
    i = 2
    while (i < n) {
      if (d(i) == d(i - 1)) f(i) = f(i - 1) + 1
      i += 1
    }
    i = n - 3
    while (i >= 0) {
      if (d(i + 1) == d(i + 2)) g(i) = g(i + 1) + 1
      i -= 1
    }
    var ans = 3
    i = 0
    while (i < n) {
      ans = math.max(ans, math.max(f(i), g(i)))
      if (i > 0) ans = math.max(ans, f(i - 1) + 1)
      if (i + 1 < n) ans = math.max(ans, g(i + 1) + 1)
      if (i > 0 && i < n - 1) {
        var diff = nums(i + 1) - nums(i - 1)
        if (diff % 2 == 0) {
          diff /= 2
          var k = 3
          if (i > 1 && diff == d(i - 1)) k += f(i - 1) - 1
          if (i < n - 2 && diff == d(i + 2)) k += g(i + 1) - 1
          ans = math.max(ans, k)
        }
      }
      i += 1
    }
    ans
  }
}
''')

w("3873_maximum_points_activated_with_one_addition", r'''
// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

object Solution {
  private class UnionFind {
    val p = scala.collection.mutable.Map.empty[Long, Long]
    val size = scala.collection.mutable.Map.empty[Long, Int]

    def find(x: Long): Long = {
      if (!p.contains(x)) {
        p(x) = x
        size(x) = 1
      }
      if (p(x) != x) p(x) = find(p(x))
      p(x)
    }

    def unite(a: Long, b: Long): Boolean = {
      var pa = find(a)
      var pb = find(b)
      if (pa == pb) return false
      if (size(pa) > size(pb)) {
        p(pb) = pa
        size(pa) = size(pa) + size(pb)
      } else {
        p(pa) = pb
        size(pb) = size(pb) + size(pa)
      }
      true
    }
  }

  def maxActivated(points: Array[Array[Int]]): Int = {
    val uf = new UnionFind
    val m = 3000000000L
    points.foreach { pt => uf.unite(pt(0).toLong, pt(1).toLong + m) }
    val cnt = scala.collection.mutable.Map.empty[Long, Int]
    points.foreach { pt =>
      val r = uf.find(pt(0).toLong)
      cnt(r) = cnt.getOrElse(r, 0) + 1
    }
    var mx1 = 0
    var mx2 = 0
    cnt.values.foreach { x =>
      if (mx1 < x) { mx2 = mx1; mx1 = x }
      else if (mx2 < x) mx2 = x
    }
    mx1 + mx2 + 1
  }
}
''')

w("3874_valid_subarrays_with_exactly_one_peak", r'''
// LeetCode 3874 - Valid Subarrays With Exactly One Peak
// https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

object Solution {
  def validSubarrays(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val peaks = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 1
    while (i < n - 1) {
      if (nums(i) > nums(i - 1) && nums(i) > nums(i + 1)) peaks += i
      i += 1
    }
    var ans = 0L
    var j = 0
    while (j < peaks.length) {
      val p = peaks(j)
      var leftMin = math.max(p - k, 0)
      if (j > 0) leftMin = math.max(leftMin, peaks(j - 1) + 1)
      var rightMax = math.min(p + k, n - 1)
      if (j < peaks.length - 1) rightMax = math.min(rightMax, peaks(j + 1) - 1)
      ans += (p - leftMin + 1).toLong * (rightMax - p + 1)
      j += 1
    }
    ans
  }
}
''')

w("3875_construct_uniform_parity_array_i", r'''
// LeetCode 3875 - Construct Uniform Parity Array I
// https://leetcode.com/problems/construct-uniform-parity-array-i/

object Solution {
  def uniformArray(nums1: Array[Int]): Boolean = true
}
''')

w("3876_construct_uniform_parity_array_ii", r'''
// LeetCode 3876 - Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

object Solution {
  def uniformArray(nums1: Array[Int]): Boolean = {
    var mn = Int.MaxValue
    nums1.foreach { x => if (x % 2 == 1 && x < mn) mn = x }
    nums1.foreach { x =>
      if (x % 2 == 0 && mn != Int.MaxValue && x < mn) return false
    }
    true
  }
}
''')

w("3877_minimum_removals_to_achieve_target_xor", r'''
// LeetCode 3877 - Minimum Removals To Achieve Target Xor
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

object Solution {
  def minRemovals(nums: Array[Int], target: Int): Int = {
    var mx = 0
    nums.foreach { x => mx = math.max(mx, x) }
    var m = 0
    if (mx > 0) {
      var u = mx
      while (u != 0) { m += 1; u >>= 1 }
    }
    if ((1 << m) <= target) return -1
    val n = nums.length
    val N = 1 << m
    val f = Array.ofDim[Int](n + 1, N)
    var i = 0
    while (i <= n) {
      java.util.Arrays.fill(f(i), Int.MinValue)
      i += 1
    }
    f(0)(0) = 0
    i = 1
    while (i <= n) {
      val x = nums(i - 1)
      var j = 0
      while (j < N) {
        f(i)(j) = f(i - 1)(j)
        if (f(i - 1)(j ^ x) != Int.MinValue) {
          f(i)(j) = math.max(f(i)(j), f(i - 1)(j ^ x) + 1)
        }
        j += 1
      }
      i += 1
    }
    if (f(n)(target) < 0) return -1
    n - f(n)(target)
  }
}
''')

w("3878_count_good_subarrays", r'''
// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

object Solution {
  def countGoodSubarrays(nums: Array[Int]): Long = {
    val n = nums.length
    val l = Array.fill(n)(-1)
    val stk = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < n) {
      val x = nums(i)
      while (stk.nonEmpty && nums(stk.last) < x && (nums(stk.last) | x) == x) {
        stk.remove(stk.length - 1)
      }
      if (stk.nonEmpty) l(i) = stk.last
      stk += i
      i += 1
    }
    val r = Array.fill(n)(n)
    stk.clear()
    i = n - 1
    while (i >= 0) {
      while (stk.nonEmpty && (nums(stk.last) | nums(i)) == nums(i)) {
        stk.remove(stk.length - 1)
      }
      if (stk.nonEmpty) r(i) = stk.last
      stk += i
      i -= 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      ans += (i - l(i)).toLong * (r(i) - i)
      i += 1
    }
    ans
  }
}
''')

w("3879_maximum_distinct_path_sum_in_a_binary_tree", r'''
// LeetCode 3879 - Maximum Distinct Path Sum In A Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  private val g = scala.collection.mutable.Map.empty[TreeNode, Array[TreeNode]]
  private val vis = scala.collection.mutable.Map.empty[Int, Boolean]

  private def dfs(node: TreeNode, p: TreeNode): Unit = {
    if (node == null) return
    g(node) = Array(p, node.left, node.right)
    dfs(node.left, node)
    dfs(node.right, node)
  }

  private def dfs2(node: TreeNode): Int = {
    if (node == null || vis.getOrElse(node.value, false)) return 0
    vis(node.value) = true
    val res = node.value
    var best = 0
    g(node).foreach { nxt => best = math.max(best, dfs2(nxt)) }
    vis(node.value) = false
    res + best
  }

  def maxSum(root: TreeNode): Int = {
    g.clear()
    vis.clear()
    dfs(root, null)
    var ans = Int.MinValue
    g.keys.foreach { node =>
      ans = math.max(ans, dfs2(node))
      vis.clear()
    }
    ans
  }
}
''')

w("3880_minimum_absolute_difference_between_two_values", r'''
// LeetCode 3880 - Minimum Absolute Difference Between Two Values
// https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

object Solution {
  def minAbsoluteDifference(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = n + 1
    val last = Array(-ans, -ans, -ans)
    var i = 0
    while (i < n) {
      val x = nums(i)
      if (x != 0) {
        ans = math.min(ans, i - last(3 - x))
        last(x) = i
      }
      i += 1
    }
    if (ans > n) -1 else ans
  }
}
''')

w("3881_direction_assignments_with_exactly_k_visible_people", r'''
// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

object Solution {
  private val N = 100001
  private val MOD = 1000000007
  private var fact: Array[Long] = _
  private var invFact: Array[Long] = _
  private var ready = false

  private def qmi(a0: Long, k0: Long, p: Long): Long = {
    var a = a0
    var k = k0
    var res = 1L
    while (k != 0) {
      if ((k & 1) != 0) res = res * a % p
      k >>= 1
      a = a * a % p
    }
    res
  }

  private def init(): Unit = {
    if (ready) return
    fact = new Array[Long](N)
    invFact = new Array[Long](N)
    fact(0) = 1
    invFact(0) = 1
    var i = 1
    while (i < N) {
      fact(i) = fact(i - 1) * i % MOD
      invFact(i) = qmi(fact(i), MOD - 2, MOD)
      i += 1
    }
    ready = true
  }

  private def comb(n: Int, k: Int): Long =
    fact(n) * invFact(k) % MOD * invFact(n - k) % MOD

  def countVisiblePeople(n: Int, pos: Int, k: Int): Int = {
    init()
    val l = pos
    val r = n - pos - 1
    var ans = 0L
    var a = 0
    while (a <= math.min(k, l)) {
      val b = k - a
      if (b <= r) {
        ans = (ans + 2 * comb(l, a) % MOD * comb(r, b) % MOD) % MOD
      }
      a += 1
    }
    ans.toInt
  }
}
''')

w("3882_minimum_xor_path_in_a_grid", r'''
// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

object Solution {
  def minXor(grid: Array[Array[Int]]): Int = {
    val rows = grid.length
    val cols = grid(0).length
    val dp = Array.fill(cols)(new Array[Boolean](1024))
    var row = 0
    while (row < rows) {
      var left = new Array[Boolean](1024)
      var col = 0
      while (col < cols) {
        val next = new Array[Boolean](1024)
        val value = grid(row)(col)
        if (row == 0 && col == 0) {
          next(value) = true
        } else {
          var xorv = 0
          while (xorv < 1024) {
            if (dp(col)(xorv) || left(xorv)) next(xorv ^ value) = true
            xorv += 1
          }
        }
        dp(col) = next
        left = next
        col += 1
      }
      row += 1
    }
    var xorv = 0
    while (xorv < 1024) {
      if (dp(cols - 1)(xorv)) return xorv
      xorv += 1
    }
    -1
  }
}
''')

w("3883_count_non_decreasing_arrays_with_given_digit_sums", r'''
// LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

object Solution {
  def countNonDecreasingArrays(digitSum: Array[Int]): Int = {
    val mod = 1000000007
    val groups = Array.fill(51)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var x = 0
    while (x <= 5000) {
      var s = 0
      var y = x
      while (y > 0) { s += y % 10; y /= 10 }
      groups(s) += x
      x += 1
    }
    var prevVals = groups(digitSum(0))
    var dp = Array.fill(prevVals.length)(1)
    var pos = 1
    while (pos < digitSum.length) {
      val curVals = groups(digitSum(pos))
      val next = new Array[Int](curVals.length)
      var j = 0
      var prefix = 0
      var i = 0
      while (i < curVals.length) {
        val xv = curVals(i)
        while (j < prevVals.length && prevVals(j) <= xv) {
          prefix += dp(j)
          if (prefix >= mod) prefix -= mod
          j += 1
        }
        next(i) = prefix
        i += 1
      }
      prevVals = curVals
      dp = next
      pos += 1
    }
    var ans = 0
    dp.foreach { v =>
      ans += v
      if (ans >= mod) ans -= mod
    }
    ans
  }
}
''')

w("3884_first_matching_character_from_both_ends", r'''
// LeetCode 3884 - First Matching Character From Both Ends
// https://leetcode.com/problems/first-matching-character-from-both-ends/

object Solution {
  def firstMatchingIndex(s: String): Int = {
    val n = s.length
    var i = 0
    while (i < n / 2 + 1) {
      if (s.charAt(i) == s.charAt(n - i - 1)) return i
      i += 1
    }
    -1
  }
}
''')

w("3885_design_event_manager", r'''
// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

class EventManager(events: Array[Array[Int]]) {
  private val sl = scala.collection.mutable.TreeSet.empty[(Long, Long)]
  private val d = scala.collection.mutable.Map.empty[Int, Int]

  events.foreach { e =>
    val eventId = e(0)
    val priority = e(1)
    sl += ((-priority.toLong, eventId.toLong))
    d(eventId) = priority
  }

  def updatePriority(eventId: Int, newPriority: Int): Unit = {
    val old = d(eventId)
    sl -= ((-old.toLong, eventId.toLong))
    sl += ((-newPriority.toLong, eventId.toLong))
    d(eventId) = newPriority
  }

  def pollHighest(): Int = {
    if (sl.isEmpty) return -1
    val top = sl.head
    sl -= top
    d.remove(top._2.toInt)
    top._2.toInt
  }
}
''')

w("3886_sum_of_sortable_integers", r'''
// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

object Solution {
  private def rotationMatches(block: Array[Int], target: Array[Int]): Boolean = {
    val k = block.length
    val prefix = new Array[Int](k)
    var i = 1
    while (i < k) {
      var j = prefix(i - 1)
      while (j > 0 && target(i) != target(j)) j = prefix(j - 1)
      if (target(i) == target(j)) j += 1
      prefix(i) = j
      i += 1
    }
    var matched = 0
    i = 0
    while (i < 2 * k - 1) {
      val x = block(i % k)
      while (matched > 0 && x != target(matched)) matched = prefix(matched - 1)
      if (x == target(matched)) matched += 1
      if (matched == k) return true
      i += 1
    }
    false
  }

  def sumOfSortableIntegers(nums: Array[Int]): Int = {
    val n = nums.length
    val sorted = nums.clone()
    java.util.Arrays.sort(sorted)
    val divisors = scala.collection.mutable.ArrayBuffer.empty[Int]
    var d = 1
    while (d * d <= n) {
      if (n % d == 0) {
        divisors += d
        if (d * d != n) divisors += n / d
      }
      d += 1
    }
    var answer = 0
    divisors.foreach { k =>
      var ok = true
      var start = 0
      while (start < n && ok) {
        val block = java.util.Arrays.copyOfRange(nums, start, start + k)
        val target = java.util.Arrays.copyOfRange(sorted, start, start + k)
        if (!rotationMatches(block, target)) ok = false
        start += k
      }
      if (ok) answer += k
    }
    answer
  }
}
''')

w("3887_incremental_even_weighted_cycle_queries", r'''
// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

object Solution {
  private var parent: Array[Int] = _
  private var size: Array[Int] = _
  private var parity: Array[Int] = _

  private def find(x: Int): Array[Int] = {
    if (parent(x) == x) return Array(x, 0)
    val res = find(parent(x))
    val root = res(0)
    val p = res(1)
    parity(x) ^= p
    parent(x) = root
    Array(root, parity(x))
  }

  def countValidEdges(n: Int, edges: Array[Array[Int]]): Int = {
    parent = new Array[Int](n)
    size = new Array[Int](n)
    parity = new Array[Int](n)
    var i = 0
    while (i < n) {
      parent(i) = i
      size(i) = 1
      i += 1
    }
    var ans = 0
    edges.foreach { e =>
      val fu = find(e(0))
      val fv = find(e(1))
      var ru = fu(0)
      var pu = fu(1)
      var rv = fv(0)
      var pv = fv(1)
      if (ru == rv) {
        if ((pu ^ pv) == e(2)) ans += 1
      } else {
        if (size(ru) < size(rv)) {
          val t = ru; ru = rv; rv = t
          val t2 = pu; pu = pv; pv = t2
        }
        parent(rv) = ru
        parity(rv) = pu ^ pv ^ e(2)
        size(ru) += size(rv)
        ans += 1
      }
    }
    ans
  }
}
''')

w("3888_minimum_operations_to_make_all_grid_elements_equal", r'''
// LeetCode 3888 - Minimum Operations To Make All Grid Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

object Solution {
  private var grid: Array[Array[Int]] = _
  private var k: Int = _
  private var m: Int = _
  private var n: Int = _

  def minOperations(grid: Array[Array[Int]], k: Int): Long = {
    this.grid = grid
    this.k = k
    m = grid.length
    n = grid(0).length
    var maxVal = grid(0)(0)
    grid.foreach { row => row.foreach { x => maxVal = math.max(maxVal, x) } }
    var t = maxVal
    while (t <= maxVal + 1) {
      val res = check(t)
      if (res != -1) return res
      t += 1
    }
    -1L
  }

  private def check(target: Int): Long = {
    val diff = Array.ofDim[Long](m + 2, n + 2)
    var totalOps = 0L
    var i = 1
    while (i <= m) {
      var j = 1
      while (j <= n) {
        diff(i)(j) += diff(i - 1)(j) + diff(i)(j - 1) - diff(i - 1)(j - 1)
        val curVal = grid(i - 1)(j - 1).toLong + diff(i)(j)
        if (curVal > target) return -1
        if (curVal < target) {
          if (i + k - 1 > m || j + k - 1 > n) return -1
          val needed = target - curVal
          totalOps += needed
          diff(i)(j) += needed
          diff(i + k)(j) -= needed
          diff(i)(j + k) -= needed
          diff(i + k)(j + k) += needed
        }
        j += 1
      }
      i += 1
    }
    totalOps
  }
}
''')

w("3889_mirror_frequency_distance", r'''
// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

object Solution {
  def mirrorFrequency(s: String): Int = {
    val freq = scala.collection.mutable.Map.empty[Char, Int]
    s.foreach { c => freq(c) = freq.getOrElse(c, 0) + 1 }
    var ans = 0
    val vis = scala.collection.mutable.Map.empty[Char, Boolean]
    freq.foreach { case (c, v) =>
      val m = if (c >= 'a' && c <= 'z') ('a' + 25 - (c - 'a')).toChar
              else ('0' + (9 - (c - '0'))).toChar
      if (!vis.getOrElse(m, false)) {
        vis(c) = true
        val mv = freq.getOrElse(m, 0)
        ans += math.abs(v - mv)
      }
    }
    ans
  }
}
''')

w("3890_integers_with_multiple_sum_of_two_cubes", r'''
// LeetCode 3890 - Integers With Multiple Sum Of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

object Solution {
  private var GOOD: Array[Int] = _
  private var ready = false

  private def init(): Unit = {
    if (ready) return
    val LIMIT = 1000000000L
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    val cubes = new Array[Long](1001)
    var i = 0
    while (i <= 1000) {
      cubes(i) = i.toLong * i * i
      i += 1
    }
    var a = 1
    while (a <= 1000) {
      var b = a
      var stop = false
      while (b <= 1000 && !stop) {
        val x = cubes(a) + cubes(b)
        if (x > LIMIT) stop = true
        else {
          val xi = x.toInt
          cnt(xi) = cnt.getOrElse(xi, 0) + 1
        }
        b += 1
      }
      a += 1
    }
    val buf = scala.collection.mutable.ArrayBuffer.empty[Int]
    cnt.foreach { case (k, v) => if (v > 1) buf += k }
    GOOD = buf.sorted.toArray
    ready = true
  }

  def findGoodIntegers(n: Int): Array[Int] = {
    init()
    var lo = 0
    var hi = GOOD.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (GOOD(mid) <= n) lo = mid + 1
      else hi = mid
    }
    val ans = new Array[Int](lo)
    iCopy(ans, lo)
    ans
  }

  private def iCopy(ans: Array[Int], lo: Int): Unit = {
    var i = 0
    while (i < lo) {
      ans(i) = GOOD(i)
      i += 1
    }
  }
}
''')

w("3891_minimum_increase_to_maximize_special_indices", r'''
// LeetCode 3891 - Minimum Increase To Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

object Solution {
  private var nums: Array[Int] = _
  private var f: Array[Array[Long]] = _
  private var n: Int = _

  def minIncrease(nums: Array[Int]): Long = {
    this.nums = nums
    n = nums.length
    f = Array.fill(n, 2)(-1L)
    dfs(1, (n & 1) ^ 1)
  }

  private def dfs(i: Int, j: Int): Long = {
    if (i >= n - 1) return 0
    if (f(i)(j) != -1) return f(i)(j)
    val cost = math.max(0, math.max(nums(i - 1), nums(i + 1)) + 1 - nums(i))
    var ans = cost.toLong + dfs(i + 2, j)
    if (j > 0) ans = math.min(ans, dfs(i + 1, 0))
    f(i)(j) = ans
    ans
  }
}
''')

w("3892_minimum_operations_to_achieve_at_least_k_peaks", r'''
// LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

object Solution {
  private var cost: Array[Long] = _
  private val INF = 1L << 60

  def minOperations(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    if (k == 0) return 0
    if (k > n / 2) return -1
    cost = new Array[Long](n)
    var i = 0
    while (i < n) {
      val left = nums((i + n - 1) % n)
      val right = nums((i + 1) % n)
      val need = math.max(left, right)
      if (need >= nums(i)) cost(i) = need.toLong - nums(i) + 1
      i += 1
    }
    var answer = line(1, n - 1, k)
    var withFirst = line(2, n - 2, k - 1)
    if (withFirst != INF) {
      withFirst += cost(0)
      answer = math.min(answer, withFirst)
    }
    if (answer == INF) -1 else answer
  }

  private def line(left: Int, right: Int, choose: Int): Long = {
    if (choose == 0) return 0
    if (left > right || choose > (right - left + 2) / 2) return INF
    var prev2 = Array.fill(choose + 1)(INF)
    var prev1 = Array.fill(choose + 1)(INF)
    prev2(0) = 0
    prev1(0) = 0
    var i = left
    while (i <= right) {
      val current = prev1.clone()
      var j = 1
      while (j <= choose) {
        if (prev2(j - 1) != INF && prev2(j - 1) + cost(i) < current(j)) {
          current(j) = prev2(j - 1) + cost(i)
        }
        j += 1
      }
      prev2 = prev1
      prev1 = current
      i += 1
    }
    prev1(choose)
  }
}
''')

w("3893_maximum_team_size_with_overlapping_intervals", r'''
// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

object Solution {
  def maximumTeamSize(startTime: Array[Int], endTime: Array[Int]): Int = {
    val n = startTime.length
    val st = startTime.clone()
    val en = endTime.clone()
    java.util.Arrays.sort(st)
    java.util.Arrays.sort(en)
    var ans = 0
    var t = 0
    while (t < n) {
      val l = startTime(t)
      val r = endTime(t)
      val i = upperBound(en, l - 1)
      val j = upperBound(st, r)
      ans = math.max(ans, j - i)
      t += 1
    }
    ans
  }

  private def upperBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) <= x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
''')

w("3894_traffic_signal_color", r'''
// LeetCode 3894 - Traffic Signal Color
// https://leetcode.com/problems/traffic-signal-color/

object Solution {
  def trafficSignal(timer: Int): String = {
    if (timer == 0) "Green"
    else if (timer == 30) "Orange"
    else if (timer > 30 && timer <= 90) "Red"
    else "Invalid"
  }
}
''')

w("3895_count_digit_appearances", r'''
// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

object Solution {
  def countDigitOccurrences(nums: Array[Int], digit: Int): Int = {
    var ans = 0
    nums.foreach { num =>
      var x = num
      while (x > 0) {
        if (x % 10 == digit) ans += 1
        x /= 10
      }
    }
    ans
  }
}
''')

w("3896_minimum_operations_to_transform_array_into_alternating_prime", r'''
// LeetCode 3896 - Minimum Operations To Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

object Solution {
  private val MX = 200000
  private var isPrime: Array[Boolean] = _
  private var primes: Array[Int] = _
  private var ready = false

  private def init(): Unit = {
    if (ready) return
    isPrime = Array.fill(MX + 1)(true)
    isPrime(0) = false
    isPrime(1) = false
    var i = 2
    while (i <= MX / i) {
      if (isPrime(i)) {
        var j = i * i
        while (j <= MX) {
          isPrime(j) = false
          j += i
        }
      }
      i += 1
    }
    val buf = scala.collection.mutable.ArrayBuffer.empty[Int]
    i = 2
    while (i <= MX) {
      if (isPrime(i)) buf += i
      i += 1
    }
    primes = buf.toArray
    ready = true
  }

  def minOperations(nums: Array[Int]): Int = {
    init()
    var ans = 0
    var i = 0
    while (i < nums.length) {
      val x = nums(i)
      if (i % 2 == 0) {
        var lo = 0
        var hi = primes.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (primes(mid) < x) lo = mid + 1
          else hi = mid
        }
        ans += primes(lo) - x
      } else if (isPrime(x)) {
        ans += (if (x == 2) 2 else 1)
      }
      i += 1
    }
    ans
  }
}
''')

print("batch C done")
