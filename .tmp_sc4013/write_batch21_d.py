#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("3897_maximum_value_of_concatenated_binary_segments", r'''
// LeetCode 3897 - Maximum Value Of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

object Solution {
  private val MOD = 1000000007

  private def group(p: Array[Int]): Int = {
    if (p(1) == 0) 0
    else if (p(0) > 0) 1
    else 2
  }

  def maxValue(nums1: Array[Int], nums0: Array[Int]): Int = {
    val n = nums1.length
    val pairs = Array.ofDim[Int](n, 2)
    var b = 0
    var i = 0
    while (i < n) {
      pairs(i)(0) = nums1(i)
      pairs(i)(1) = nums0(i)
      b += nums1(i) + nums0(i)
      i += 1
    }
    java.util.Arrays.sort(pairs, new java.util.Comparator[Array[Int]] {
      def compare(a: Array[Int], c: Array[Int]): Int = {
        val g1 = group(a)
        val g2 = group(c)
        if (g1 != g2) Integer.compare(g1, g2)
        else if (g1 == 0) Integer.compare(c(0), a(0))
        else if (g1 == 1) {
          if (a(0) != c(0)) Integer.compare(c(0), a(0))
          else Integer.compare(a(1), c(1))
        } else Integer.compare(a(1), c(1))
      }
    })
    val p = new Array[Int](b)
    p(0) = 1
    i = 1
    while (i < b) {
      p(i) = ((2L * p(i - 1)) % MOD).toInt
      i += 1
    }
    var ans = 0
    b -= 1
    pairs.foreach { pr =>
      var cnt1 = pr(0)
      var cnt0 = pr(1)
      while (cnt1 > 0) {
        ans = (ans + p(b)) % MOD
        b -= 1
        cnt1 -= 1
      }
      b -= cnt0
    }
    ans
  }
}
''')

w("3898_find_the_degree_of_each_vertex", r'''
// LeetCode 3898 - Find The Degree Of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

object Solution {
  def findDegrees(matrix: Array[Array[Int]]): Array[Int] = {
    val ans = new Array[Int](matrix.length)
    var i = 0
    while (i < matrix.length) {
      matrix(i).foreach { x => ans(i) += x }
      i += 1
    }
    ans
  }
}
''')

w("3899_angles_of_a_triangle", r'''
// LeetCode 3899 - Angles Of A Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

object Solution {
  def internalAngles(sides: Array[Int]): Array[Double] = {
    java.util.Arrays.sort(sides)
    val a = sides(0)
    val b = sides(1)
    val c = sides(2)
    if (a + b <= c) return Array.emptyDoubleArray
    val PI = math.acos(-1.0)
    val A = math.acos((b.toLong * b + c.toLong * c - a.toLong * a).toDouble / (2.0 * b * c)) * 180.0 / PI
    val B = math.acos((a.toLong * a + c.toLong * c - b.toLong * b).toDouble / (2.0 * a * c)) * 180.0 / PI
    val C = 180.0 - A - B
    Array(A, B, C)
  }
}
''')

w("3900_longest_balanced_substring_after_one_swap", r'''
// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

object Solution {
  def longestBalanced(s: String): Int = {
    var cnt0 = 0
    s.foreach { c => if (c == '0') cnt0 += 1 }
    val cnt1 = s.length - cnt0
    val pos = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    pos(0) = scala.collection.mutable.ArrayBuffer(-1)
    var ans = 0
    var pre = 0
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == '1') pre += 1
      else pre -= 1
      pos.getOrElseUpdate(pre, scala.collection.mutable.ArrayBuffer.empty[Int]) += i
      ans = math.max(ans, i - pos(pre)(0))
      if (pos.contains(pre - 2)) {
        val p = pos(pre - 2)
        if ((i - p(0) - 2) / 2 < cnt0) ans = math.max(ans, i - p(0))
        else if (p.length > 1) ans = math.max(ans, i - p(1))
      }
      if (pos.contains(pre + 2)) {
        val p = pos(pre + 2)
        if ((i - p(0) - 2) / 2 < cnt1) ans = math.max(ans, i - p(0))
        else if (p.length > 1) ans = math.max(ans, i - p(1))
      }
      i += 1
    }
    ans
  }
}
''')

w("3901_good_subsequence_queries", r'''
// LeetCode 3901 - Good Subsequence Queries
// https://leetcode.com/problems/good-subsequence-queries/

object Solution {
  private class Node {
    var l = 0
    var r = 0
    var g = 0
  }

  private class SegmentTree(n: Int) {
    val tr: Array[Node] = Array.fill(n << 2)(new Node)
    build(1, 1, n)

    def build(u: Int, l: Int, r: Int): Unit = {
      tr(u).l = l
      tr(u).r = r
      tr(u).g = 0
      if (l == r) return
      val mid = (l + r) >> 1
      build(u << 1, l, mid)
      build(u << 1 | 1, mid + 1, r)
    }

    def pushup(u: Int): Unit = { tr(u).g = gcd(tr(u << 1).g, tr(u << 1 | 1).g) }

    def modify(u: Int, x: Int, v: Int): Unit = {
      if (tr(u).l == tr(u).r) { tr(u).g = v; return }
      val mid = (tr(u).l + tr(u).r) >> 1
      if (x <= mid) modify(u << 1, x, v)
      else modify(u << 1 | 1, x, v)
      pushup(u)
    }

    def query(u: Int, l: Int, r: Int): Int = {
      if (l > r) return 0
      if (tr(u).l >= l && tr(u).r <= r) return tr(u).g
      val mid = (tr(u).l + tr(u).r) >> 1
      if (r <= mid) return query(u << 1, l, r)
      if (l > mid) return query(u << 1 | 1, l, r)
      gcd(query(u << 1, l, mid), query(u << 1 | 1, mid + 1, r))
    }
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

  def countGoodSubseq(nums: Array[Int], p: Int, queries: Array[Array[Int]]): Int = {
    val n = nums.length
    val tree = new SegmentTree(n)
    var cnt = 0
    var i = 0
    while (i < n) {
      if (nums(i) % p == 0) {
        tree.modify(1, i + 1, nums(i))
        cnt += 1
      }
      i += 1
    }
    var ans = 0
    queries.foreach { q =>
      val idx = q(0)
      val value = q(1)
      if (nums(idx) % p == 0) {
        tree.modify(1, idx + 1, 0)
        cnt -= 1
      }
      if (value % p == 0) {
        tree.modify(1, idx + 1, value)
        cnt += 1
      }
      nums(idx) = value
      if (tree.tr(1).g == p) {
        if (cnt < n || n > 6) ans += 1
        else {
          var found = false
          i = 1
          while (i <= n && !found) {
            val leftG = tree.query(1, 1, i - 1)
            val rightG = tree.query(1, i + 1, n)
            if (gcd(leftG, rightG) == p) { ans += 1; found = true }
            i += 1
          }
        }
      }
    }
    ans
  }
}
''')

w("3902_zigzag_level_sum_of_binary_tree", r'''
// LeetCode 3902 - Zigzag Level Sum Of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def zigzagLevelSum(root: TreeNode): Array[Long] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Long]
    var q = scala.collection.mutable.ArrayBuffer[TreeNode](root)
    var left = true
    while (q.nonEmpty) {
      val nq = scala.collection.mutable.ArrayBuffer.empty[TreeNode]
      q.foreach { node =>
        if (node.left != null) nq += node.left
        if (node.right != null) nq += node.right
      }
      val m = q.length
      var s = 0L
      var i = 0
      var stop = false
      while (i < m && !stop) {
        val node = if (left) q(i) else q(m - i - 1)
        val child = if (left) node.left else node.right
        if (child == null) stop = true
        else s += node.value
        i += 1
      }
      ans += s
      left = !left
      q = nq
    }
    ans.toArray
  }
}
''')

w("3903_smallest_stable_index_i", r'''
// LeetCode 3903 - Smallest Stable Index I
// https://leetcode.com/problems/smallest-stable-index-i/

object Solution {
  def firstStableIndex(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val right = new Array[Int](n)
    right(n - 1) = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      right(i) = math.min(right(i + 1), nums(i))
      i -= 1
    }
    var left = 0
    i = 0
    while (i < n) {
      left = math.max(left, nums(i))
      if (left - right(i) <= k) return i
      i += 1
    }
    -1
  }
}
''')

w("3904_smallest_stable_index_ii", r'''
// LeetCode 3904 - Smallest Stable Index II
// https://leetcode.com/problems/smallest-stable-index-ii/

object Solution {
  def firstStableIndex(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val right = new Array[Int](n)
    right(n - 1) = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      right(i) = math.min(right(i + 1), nums(i))
      i -= 1
    }
    var left = 0
    i = 0
    while (i < n) {
      left = math.max(left, nums(i))
      if (left - right(i) <= k) return i
      i += 1
    }
    -1
  }
}
''')

w("3905_multi_source_flood_fill", r'''
// LeetCode 3905 - Multi Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

object Solution {
  def colorGrid(n: Int, m: Int, sources: Array[Array[Int]]): Array[Array[Int]] = {
    val ans = Array.ofDim[Int](n, m)
    var q = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    sources.foreach { s => q += s }
    val dirs = Array(-1, 0, 1, 0, -1)
    q.foreach { s => ans(s(0))(s(1)) = s(2) }
    while (q.nonEmpty) {
      val vis = scala.collection.mutable.TreeMap.empty[Long, Int]
      q.foreach { curr =>
        val r = curr(0)
        val c = curr(1)
        val color = curr(2)
        var i = 0
        while (i < 4) {
          val x = r + dirs(i)
          val y = c + dirs(i + 1)
          if (x >= 0 && x < n && y >= 0 && y < m && ans(x)(y) == 0) {
            val key = (x.toLong << 32) | (y.toLong & 0xffffffffL)
            if (!vis.contains(key) || color > vis(key)) vis(key) = color
          }
          i += 1
        }
      }
      q.clear()
      vis.foreach { case (key, color) =>
        val x = (key >> 32).toInt
        val y = key.toInt
        ans(x)(y) = color
        q += Array(x, y, color)
      }
    }
    ans
  }
}
''')

w("3906_count_good_integers_on_a_grid_path", r'''
// LeetCode 3906 - Count Good Integers On A Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

object Solution {
  private val key = new Array[Boolean](16)
  private var s = ""
  private val f = Array.ofDim[Long](16, 10)

  def countGoodIntegersOnPath(l: Long, r: Long, directions: String): Long = {
    java.util.Arrays.fill(key, false)
    var row = 0
    var col = 0
    key(0) = true
    directions.foreach { c =>
      if (c == 'D') row += 1
      else col += 1
      key(row * 4 + col) = true
    }
    calc(r) - calc(l - 1)
  }

  private def dfs(pos: Int, last: Int, lim: Boolean): Long = {
    if (pos == 16) return 1
    if (!lim && f(pos)(last) != -1) return f(pos)(last)
    var res = 0L
    val start = if (key(pos)) last else 0
    val end = if (lim) s.charAt(pos) - '0' else 9
    var i = start
    while (i <= end) {
      val nextLast = if (key(pos)) i else last
      res += dfs(pos + 1, nextLast, lim && (i == end))
      i += 1
    }
    if (!lim) f(pos)(last) = res
    res
  }

  private def calc(x: Long): Long = {
    if (x < 0) return 0
    val t = x.toString
    s = "0" * (16 - t.length) + t
    var i = 0
    while (i < 16) {
      java.util.Arrays.fill(f(i), -1L)
      i += 1
    }
    dfs(0, 0, true)
  }
}
''')

w("3907_count_smaller_elements_with_opposite_parity", r'''
// LeetCode 3907 - Count Smaller Elements With Opposite Parity
// https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

object Solution {
  private class BIT(n_ : Int) {
    val n = n_
    val c = new Array[Int](n_ + 1)

    def update(x0: Int, delta: Int): Unit = {
      var x = x0
      while (x <= n) {
        c(x) += delta
        x += x & -x
      }
    }

    def query(x0: Int): Int = {
      var s = 0
      var x = x0
      while (x > 0) {
        s += c(x)
        x -= x & -x
      }
      s
    }
  }

  def countSmallerOppositeParity(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val sorted = nums.clone()
    java.util.Arrays.sort(sorted)
    var m = 0
    var i = 0
    while (i < sorted.length) {
      if (i == 0 || sorted(i) != sorted(i - 1)) {
        sorted(m) = sorted(i)
        m += 1
      }
      i += 1
    }
    val uniq = java.util.Arrays.copyOf(sorted, m)
    val bits = Array(new BIT(m), new BIT(m))
    val ans = new Array[Int](n)
    i = n - 1
    while (i >= 0) {
      var x = java.util.Arrays.binarySearch(uniq, nums(i))
      if (x < 0) x = ~x
      x += 1
      ans(i) = bits((nums(i) & 1) ^ 1).query(x - 1)
      bits(nums(i) & 1).update(x, 1)
      i -= 1
    }
    ans
  }
}
''')

w("3908_valid_digit_number", r'''
// LeetCode 3908 - Valid Digit Number
// https://leetcode.com/problems/valid-digit-number/

object Solution {
  def validDigit(n0: Int, x: Int): Boolean = {
    var n = n0
    var hasX = false
    while (n > 9) {
      hasX = hasX || (n % 10 == x)
      n /= 10
    }
    hasX && (n != x)
  }
}
''')

w("3909_compare_sums_of_bitonic_parts", r'''
// LeetCode 3909 - Compare Sums Of Bitonic Parts
// https://leetcode.com/problems/compare-sums-of-bitonic-parts/

object Solution {
  def compareBitonicSums(nums: Array[Int]): Int = {
    var l = nums(0).toLong
    var r = 0L
    nums.foreach { x => r += x }
    var i = 1
    var stop = false
    while (i < nums.length && !stop) {
      if (nums(i - 1) > nums(i)) stop = true
      else {
        l += nums(i)
        r -= nums(i - 1)
        i += 1
      }
    }
    if (l == r) -1
    else if (l > r) 0
    else 1
  }
}
''')

w("3910_count_connected_subgraphs_with_even_node_sum", r'''
// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

object Solution {
  private var g: Array[scala.collection.mutable.ArrayBuffer[Int]] = _
  private var vis: Int = _
  private var m: Int = _

  def evenSumSubgraphs(nums: Array[Int], edges: Array[Array[Int]]): Int = {
    val n = nums.length
    g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    m = (1 << n) - 1
    var ans = 0
    var sub = 1
    while (sub <= m) {
      var s = 0
      var i = 0
      while (i < n) {
        if (((sub >> i) & 1) != 0) s += nums(i)
        i += 1
      }
      if (s % 2 == 0) {
        vis = m ^ sub
        val start = 31 - Integer.numberOfLeadingZeros(sub)
        dfs(start)
        if (vis == m) ans += 1
      }
      sub += 1
    }
    ans
  }

  private def dfs(u: Int): Unit = {
    vis |= 1 << u
    g(u).foreach { v =>
      if (((vis >> v) & 1) == 0) dfs(v)
    }
  }
}
''')

w("3911_k_th_smallest_remaining_even_integer_in_subarray_queries", r'''
// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

object Solution {
  def kthSmallestEven(nums: Array[Int], queries: Array[Array[Int]]): Array[Long] = {
    val n = nums.length
    val evenPrefix = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      evenPrefix(i + 1) = evenPrefix(i) + (if (nums(i) % 2 == 0) 1 else 0)
      i += 1
    }
    val ans = new Array[Long](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val l = queries(qi)(0)
      val r = queries(qi)(1)
      val k = queries(qi)(2).toLong
      var lo = 1L
      var hi = k + (r - l + 1)
      while (lo < hi) {
        val mid = (lo + hi) / 2
        var pos = upperBound(nums, 2 * mid)
        if (pos > r + 1) pos = r + 1
        var removed = 0
        if (pos > l) removed = evenPrefix(pos) - evenPrefix(l)
        if (mid - removed >= k) hi = mid
        else lo = mid + 1
      }
      ans(qi) = 2 * lo
      qi += 1
    }
    ans
  }

  private def upperBound(a: Array[Int], x: Long): Int = {
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

w("3912_valid_elements_in_an_array", r'''
// LeetCode 3912 - Valid Elements In An Array
// https://leetcode.com/problems/valid-elements-in-an-array/

object Solution {
  def findValidElements(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val right = new Array[Int](n)
    right(n - 1) = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      right(i) = math.max(right(i + 1), nums(i))
      i -= 1
    }
    var left = 0
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    i = 0
    while (i < n) {
      val x = nums(i)
      if (x > left || i == n - 1 || x > right(i + 1)) ans += x
      left = math.max(left, x)
      i += 1
    }
    ans.toArray
  }
}
''')

w("3913_sort_vowels_by_frequency", r'''
// LeetCode 3913 - Sort Vowels By Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

object Solution {
  def sortVowels(s: String): String = {
    val st = Set('a', 'e', 'i', 'o', 'u')
    val vowels = scala.collection.mutable.ArrayBuffer.empty[Char]
    val cnt = scala.collection.mutable.Map.empty[Char, Int]
    s.foreach { c =>
      if (st.contains(c)) {
        if (!cnt.contains(c)) { vowels += c; cnt(c) = 0 }
        cnt(c) = cnt(c) + 1
      }
    }
    val sortedVowels = vowels.sortBy(c => -cnt(c))
    val ans = s.toCharArray
    var i = 0
    var k = 0
    while (k < s.length) {
      if (st.contains(s.charAt(k))) {
        val ch = sortedVowels(i)
        ans(k) = ch
        cnt(ch) = cnt(ch) - 1
        if (cnt(ch) == 0) i += 1
      }
      k += 1
    }
    new String(ans)
  }
}
''')

w("3914_minimum_operations_to_make_array_non_decreasing", r'''
// LeetCode 3914 - Minimum Operations To Make Array Non Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

object Solution {
  def minOperations(nums: Array[Int]): Long = {
    var ans = 0L
    var i = 1
    while (i < nums.length) {
      ans += math.max(0L, nums(i - 1).toLong - nums(i))
      i += 1
    }
    ans
  }
}
''')

w("3915_maximum_sum_of_alternating_subsequence_with_distance_at_least_k", r'''
// LeetCode 3915 - Maximum Sum Of Alternating Subsequence With Distance At Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

object Solution {
  private class Fenwick(n: Int) {
    val f = new Array[Long](n)

    def update(i0: Int, value: Long): Unit = {
      var i = i0
      while (i < f.length) {
        f(i) = math.max(f(i), value)
        i += i & -i
      }
    }

    def preMax(i0: Int): Long = {
      var res = 0L
      var i = i0
      while (i > 0) {
        res = math.max(res, f(i))
        i &= i - 1
      }
      res
    }
  }

  def maxAlternatingSum(nums: Array[Int], k: Int): Long = {
    val sorted = nums.clone()
    java.util.Arrays.sort(sorted)
    var m = 0
    var i = 0
    while (i < sorted.length) {
      if (i == 0 || sorted(i) != sorted(i - 1)) {
        sorted(m) = sorted(i)
        m += 1
      }
      i += 1
    }
    val uniq = java.util.Arrays.copyOf(sorted, m)
    val n = nums.length
    val fInc = new Array[Long](n)
    val fDec = new Array[Long](n)
    val inc = new Fenwick(m + 1)
    val dec = new Fenwick(m + 1)
    var ans = 0L
    val ranks = new Array[Int](n)
    i = 0
    while (i < n) {
      val x = nums(i)
      if (i >= k) {
        val j = ranks(i - k)
        inc.update(m - j, fInc(i - k))
        dec.update(j + 1, fDec(i - k))
      }
      var jr = java.util.Arrays.binarySearch(uniq, x)
      if (jr < 0) jr = ~jr
      ranks(i) = jr
      fInc(i) = dec.preMax(jr) + x
      fDec(i) = inc.preMax(m - 1 - jr) + x
      ans = math.max(ans, math.max(fInc(i), fDec(i)))
      i += 1
    }
    ans
  }
}
''')

w("3916_number_of_zigzag_arrays_iii", r'''
// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

object Solution {
  def zigZagArrays(n: Int, l: Int, r: Int): Int = {
    val mod = 1000000007L
    val points = n + 1
    val values = new Array[Long](points + 1)
    var mm = 1
    while (mm <= points) {
      var up = new Array[Long](mm)
      var down = new Array[Long](mm)
      var value = 0
      while (value < mm) {
        up(value) = value
        down(value) = mm - 1 - value
        value += 1
      }
      var length = 3
      while (length <= n) {
        val nextUp = new Array[Long](mm)
        val nextDown = new Array[Long](mm)
        var prefix = 0L
        value = 0
        while (value < mm) {
          nextUp(value) = prefix
          prefix = (prefix + down(value)) % mod
          value += 1
        }
        var suffix = 0L
        value = mm - 1
        while (value >= 0) {
          nextDown(value) = suffix
          suffix = (suffix + up(value)) % mod
          value -= 1
        }
        up = nextUp
        down = nextDown
        length += 1
      }
      value = 0
      while (value < mm) {
        values(mm) = (values(mm) + up(value) + down(value)) % mod
        value += 1
      }
      mm += 1
    }
    val x = (r.toLong - l + 1) % mod
    if (r.toLong - l + 1 <= points) return values(r - l + 1).toInt
    val prefixA = new Array[Long](points + 2)
    val suffixA = new Array[Long](points + 2)
    prefixA(0) = 1
    var i = 1
    while (i <= points) {
      prefixA(i) = prefixA(i - 1) * ((x - i + mod) % mod) % mod
      i += 1
    }
    suffixA(points + 1) = 1
    i = points
    while (i >= 1) {
      suffixA(i) = suffixA(i + 1) * ((x - i + mod) % mod) % mod
      i -= 1
    }
    val factorial = new Array[Long](points + 1)
    factorial(0) = 1
    i = 1
    while (i <= points) {
      factorial(i) = factorial(i - 1) * i % mod
      i += 1
    }
    var answer = 0L
    i = 1
    while (i <= points) {
      val numerator = prefixA(i - 1) * suffixA(i + 1) % mod
      val denominator = factorial(i - 1) * factorial(points - i) % mod
      val term = values(i) * numerator % mod * powm(denominator, mod - 2, mod) % mod
      if ((points - i) % 2 == 1) answer -= term
      else answer += term
      answer %= mod
      i += 1
    }
    if (answer < 0) answer += mod
    answer.toInt
  }

  private def powm(a0: Long, e0: Long, mod: Long): Long = {
    var a = a0
    var e = e0
    var res = 1L
    while (e > 0) {
      if ((e & 1) != 0) res = res * a % mod
      a = a * a % mod
      e >>= 1
    }
    res
  }
}
''')

w("3917_count_indices_with_opposite_parity", r'''
// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

object Solution {
  def countOppositeParity(nums: Array[Int]): Array[Int] = {
    val cnt = Array(0, 0)
    nums.foreach { x => cnt(x & 1) += 1 }
    val n = nums.length
    val ans = new Array[Int](n)
    var i = 0
    while (i < n) {
      val x = nums(i)
      cnt(x & 1) -= 1
      ans(i) = cnt((x & 1) ^ 1)
      i += 1
    }
    ans
  }
}
''')

w("3918_sum_of_primes_between_number_and_its_reverse", r'''
// LeetCode 3918 - Sum Of Primes Between Number And Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

object Solution {
  private var ready = false
  private var isPrime: Array[Boolean] = _

  private def init(): Unit = {
    if (ready) return
    isPrime = Array.fill(1001)(true)
    isPrime(0) = false
    isPrime(1) = false
    var i = 2
    while (i * i <= 1000) {
      if (isPrime(i)) {
        var j = i * i
        while (j <= 1000) {
          isPrime(j) = false
          j += i
        }
      }
      i += 1
    }
    ready = true
  }

  def sumOfPrimesInRange(n: Int): Int = {
    init()
    var r = 0
    var x = n
    while (x > 0) {
      r = r * 10 + x % 10
      x /= 10
    }
    val low = math.min(n, r)
    val high = math.max(n, r)
    var ans = 0
    var v = low
    while (v <= high) {
      if (isPrime(v)) ans += v
      v += 1
    }
    ans
  }
}
''')

w("3919_minimum_cost_to_move_between_indices", r'''
// LeetCode 3919 - Minimum Cost To Move Between Indices
// https://leetcode.com/problems/minimum-cost-to-move-between-indices/

object Solution {
  def minCost(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = nums.length
    val s1 = new Array[Int](n)
    val s2 = new Array[Int](n)
    var i = 1
    while (i < n) {
      var c1 = 1
      if (i > 1 && nums(i - 1) - nums(i - 2) <= nums(i) - nums(i - 1)) c1 = nums(i) - nums(i - 1)
      var c2 = 1
      if (i < n - 1 && nums(i) - nums(i - 1) > nums(i + 1) - nums(i)) c2 = nums(i) - nums(i - 1)
      s1(i) = s1(i - 1) + c1
      s2(i) = s2(i - 1) + c2
      i += 1
    }
    val ans = new Array[Int](queries.length)
    i = 0
    while (i < queries.length) {
      val l = queries(i)(0)
      val r = queries(i)(1)
      ans(i) = if (l < r) s1(r) - s1(l) else s2(l) - s2(r)
      i += 1
    }
    ans
  }
}
''')

w("3920_maximize_fixed_points_after_deletions", r'''
// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

object Solution {
  def maxFixedPoints(nums: Array[Int]): Int = {
    val tails = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < nums.length) {
      if (i >= nums(i)) {
        val d = i - nums(i)
        var lo = 0
        var hi = tails.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (tails(mid) < d) lo = mid + 1
          else hi = mid
        }
        if (lo == tails.length) tails += d
        else tails(lo) = d
      }
      i += 1
    }
    tails.length
  }
}
''')

w("3921_score_validator", r'''
// LeetCode 3921 - Score Validator
// https://leetcode.com/problems/score-validator/

object Solution {
  def scoreValidator(events: Array[String]): Array[Int] = {
    var score = 0
    var counter = 0
    var stop = false
    events.foreach { eventStr =>
      if (!stop) {
        var isNum = eventStr.length > 0
        var num = 0
        var start = 0
        if (isNum && eventStr.charAt(0) == '-') start = 1
        var i = start
        while (i < eventStr.length && isNum) {
          if (eventStr.charAt(i) < '0' || eventStr.charAt(i) > '9') isNum = false
          else num = num * 10 + (eventStr.charAt(i) - '0')
          i += 1
        }
        if (isNum && !(start == 1 && eventStr.length == 1)) {
          if (start == 1) num = -num
          score += num
        } else if (eventStr == "W") {
          counter += 1
          if (counter == 10) stop = true
        } else {
          score += 1
        }
      }
    }
    Array(score, counter)
  }
}
''')

w("3922_minimum_flips_to_make_binary_string_coherent", r'''
// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

object Solution {
  def minFlips(s: String): Int = {
    var ones = 0
    s.foreach { c => if (c == '1') ones += 1 }
    var answer = ones
    if (ones > 0) answer = ones - 1
    val zeros = s.length - ones
    answer = math.min(answer, zeros)
    if (s.length >= 2) {
      var cost = 0
      var i = 0
      while (i < s.length) {
        val want = if (i == 0 || i == s.length - 1) '1' else '0'
        if (s.charAt(i) != want) cost += 1
        i += 1
      }
      answer = math.min(answer, cost)
    }
    answer
  }
}
''')

print("batch D done")
