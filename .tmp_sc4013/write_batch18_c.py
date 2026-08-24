#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3546_equal_sum_grid_partition_i"] = r'''// LeetCode 3546 - Equal Sum Grid Partition I
// https://leetcode.com/problems/equal-sum-grid-partition-i/

object Solution {
  def canPartitionGrid(grid: Array[Array[Int]]): Boolean = {
    var s = 0L
    for (row <- grid; x <- row) s += x
    if (s % 2 != 0) return false
    val m = grid.length
    val n = grid(0).length
    var pre = 0L
    var i = 0
    while (i < m) {
      for (x <- grid(i)) pre += x
      if (pre * 2 == s && i + 1 < m) return true
      i += 1
    }
    pre = 0
    var j = 0
    while (j < n) {
      i = 0
      while (i < m) { pre += grid(i)(j); i += 1 }
      if (pre * 2 == s && j + 1 < n) return true
      j += 1
    }
    false
  }
}
'''

FILES["3547_maximum_sum_of_edge_values_in_a_graph"] = r'''// LeetCode 3547 - Maximum Sum of Edge Values in a Graph
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

object Solution {
  def calc(left: Int, right: Int, isCycle: Boolean): Long = {
    var w0 = right
    var w1 = right
    var score = 0L
    var value = right - 1
    while (value >= left) {
      score += 1L * w0 * value
      w0 = w1
      w1 = value
      value -= 1
    }
    if (isCycle) score += 1L * w0 * w1
    score
  }

  def getComp(start: Int, graph: Array[java.util.ArrayList[Integer]], seen: Array[Boolean]): java.util.ArrayList[Integer] = {
    val comp = new java.util.ArrayList[Integer]()
    comp.add(start)
    seen(start) = true
    var i = 0
    while (i < comp.size()) {
      val it = graph(comp.get(i)).iterator()
      while (it.hasNext) {
        val v = it.next()
        if (!seen(v)) { seen(v) = true; comp.add(v) }
      }
      i += 1
    }
    comp
  }

  def maxScore(n: Int, edges: Array[Array[Int]]): Long = {
    val graph = Array.fill(n)(new java.util.ArrayList[Integer]())
    for (e <- edges) {
      graph(e(0)).add(e(1))
      graph(e(1)).add(e(0))
    }
    val seen = new Array[Boolean](n)
    val cycleSizes = new java.util.ArrayList[Integer]()
    val pathSizes = new java.util.ArrayList[Integer]()
    var i = 0
    while (i < n) {
      if (!seen(i)) {
        val comp = getComp(i, graph, seen)
        var allDeg2 = true
        val it = comp.iterator()
        while (it.hasNext) {
          val u = it.next()
          if (graph(u).size() != 2) allDeg2 = false
        }
        if (allDeg2) cycleSizes.add(comp.size())
        else if (comp.size() > 1) pathSizes.add(comp.size())
      }
      i += 1
    }
    var ans = 0L
    var curN = n
    val cit = cycleSizes.iterator()
    while (cit.hasNext) {
      val cs = cit.next().intValue()
      ans += calc(curN - cs + 1, curN, true)
      curN -= cs
    }
    pathSizes.sort(java.util.Collections.reverseOrder())
    val pit = pathSizes.iterator()
    while (pit.hasNext) {
      val ps = pit.next().intValue()
      ans += calc(curN - ps + 1, curN, false)
      curN -= ps
    }
    ans
  }
}
'''

FILES["3548_equal_sum_grid_partition_ii"] = r'''// LeetCode 3548 - Equal Sum Grid Partition II
// https://leetcode.com/problems/equal-sum-grid-partition-ii/

object Solution {
  def rotate(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val t = Array.ofDim[Int](n, m)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) { t(j)(i) = grid(i)(j); j += 1 }
      i += 1
    }
    t
  }

  def check(g: Array[Array[Int]]): Boolean = {
    val m = g.length
    val n = g(0).length
    var s1 = 0L
    var s2 = 0L
    val cnt1 = scala.collection.mutable.HashMap.empty[Long, Int]
    val cnt2 = scala.collection.mutable.HashMap.empty[Long, Int]
    for (row <- g; x <- row) {
      val v = x.toLong
      s2 += v
      cnt2(v) = cnt2.getOrElse(v, 0) + 1
    }
    var i = 0
    while (i < m - 1) {
      for (x <- g(i)) {
        val v = x.toLong
        s1 += v; s2 -= v
        cnt1(v) = cnt1.getOrElse(v, 0) + 1
        cnt2(v) = cnt2(v) - 1
      }
      if (s1 == s2) return true
      if (s1 < s2) {
        val diff = s2 - s1
        if (cnt2.getOrElse(diff, 0) > 0) {
          if ((m - i - 1 > 1 && n > 1) ||
              (i == m - 2 && (g(i + 1)(0) == diff || g(i + 1)(n - 1) == diff)) ||
              (n == 1 && (g(i + 1)(0) == diff || g(m - 1)(0) == diff)))
            return true
        }
      } else {
        val diff = s1 - s2
        if (cnt1.getOrElse(diff, 0) > 0) {
          if ((i + 1 > 1 && n > 1) ||
              (i == 0 && (g(0)(0) == diff || g(0)(n - 1) == diff)) ||
              (n == 1 && (g(0)(0) == diff || g(i)(0) == diff)))
            return true
        }
      }
      i += 1
    }
    false
  }

  def canPartitionGrid(grid: Array[Array[Int]]): Boolean =
    check(grid) || check(rotate(grid))
}
'''

FILES["3549_multiply_two_polynomials"] = r'''// LeetCode 3549 - Multiply Two Polynomials
// https://leetcode.com/problems/multiply-two-polynomials/

object Solution {
  class Complex(var re: Double, var im: Double) {
    def mul(o: Complex): Complex = new Complex(re * o.re - im * o.im, re * o.im + im * o.re)
    def add(o: Complex): Complex = new Complex(re + o.re, im + o.im)
    def sub(o: Complex): Complex = new Complex(re - o.re, im - o.im)
    def div(x: Double): Complex = new Complex(re / x, im / x)
  }

  def fft(a: Array[Complex], invert: Boolean): Unit = {
    val n = a.length
    var i = 1
    var j = 0
    while (i < n) {
      var bit = n >> 1
      while ((j & bit) != 0) { j ^= bit; bit >>= 1 }
      j ^= bit
      if (i < j) {
        val t = a(i)
        a(i) = a(j)
        a(j) = t
      }
      i += 1
    }
    var length = 2
    while (length <= n) {
      val angle = 2 * math.acos(-1.0) / length * (if (invert) -1 else 1)
      val wlen = new Complex(math.cos(angle), math.sin(angle))
      i = 0
      while (i < n) {
        var w = new Complex(1, 0)
        val half = length >> 1
        var jj = 0
        while (jj < half) {
          val u = a(i + jj)
          val v = a(i + jj + half).mul(w)
          a(i + jj) = u.add(v)
          a(i + jj + half) = u.sub(v)
          w = w.mul(wlen)
          jj += 1
        }
        i += length
      }
      length <<= 1
    }
    if (invert) {
      i = 0
      while (i < n) { a(i) = a(i).div(n); i += 1 }
    }
  }

  def multiply(poly1: Array[Int], poly2: Array[Int]): Array[Long] = {
    if (poly1.length == 0 || poly2.length == 0) return Array.empty[Long]
    val m = poly1.length + poly2.length - 1
    var n = 1
    while (n < m) n <<= 1
    val fa = new Array[Complex](n)
    val fb = new Array[Complex](n)
    var i = 0
    while (i < n) {
      fa(i) = new Complex(if (i < poly1.length) poly1(i).toDouble else 0, 0)
      fb(i) = new Complex(if (i < poly2.length) poly2(i).toDouble else 0, 0)
      i += 1
    }
    fft(fa, false)
    fft(fb, false)
    i = 0
    while (i < n) { fa(i) = fa(i).mul(fb(i)); i += 1 }
    fft(fa, true)
    val res = new Array[Long](m)
    i = 0
    while (i < m) { res(i) = math.round(fa(i).re); i += 1 }
    res
  }
}
'''

FILES["3550_smallest_index_with_digit_sum_equal_to_index"] = r'''// LeetCode 3550 - Smallest Index With Digit Sum Equal to Index
// https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

object Solution {
  def smallestIndex(nums: Array[Int]): Int = {
    var i = 0
    while (i < nums.length) {
      var x = nums(i)
      var s = 0
      while (x > 0) { s += x % 10; x /= 10 }
      if (s == i) return i
      i += 1
    }
    -1
  }
}
'''

FILES["3551_minimum_swaps_to_sort_by_digit_sum"] = r'''// LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
// https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

object Solution {
  def f(x0: Int): Int = {
    var x = x0
    var s = 0
    while (x != 0) { s += x % 10; x /= 10 }
    s
  }

  def minSwaps(nums: Array[Int]): Int = {
    val n = nums.length
    val arr = Array.ofDim[Int](n, 2)
    var i = 0
    while (i < n) { arr(i) = Array(f(nums(i)), nums(i)); i += 1 }
    java.util.Arrays.sort(arr, (a: Array[Int], b: Array[Int]) =>
      if (a(0) != b(0)) Integer.compare(a(0), b(0)) else Integer.compare(a(1), b(1)))
    val d = scala.collection.mutable.HashMap.empty[Int, Int]
    i = 0
    while (i < n) { d(arr(i)(1)) = i; i += 1 }
    val vis = new Array[Boolean](n)
    var ans = n
    i = 0
    while (i < n) {
      if (!vis(i)) {
        ans -= 1
        var j = i
        while (!vis(j)) {
          vis(j) = true
          j = d(nums(j))
        }
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3552_grid_teleportation_traversal"] = r'''// LeetCode 3552 - Grid Teleportation Traversal
// https://leetcode.com/problems/grid-teleportation-traversal/

object Solution {
  def minMoves(matrix: Array[String]): Int = {
    val m = matrix.length
    val n = matrix(0).length
    val g = scala.collection.mutable.HashMap.empty[Char, java.util.ArrayList[Array[Int]]]
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val c = matrix(i).charAt(j)
        if (Character.isLetter(c)) {
          if (!g.contains(c)) g(c) = new java.util.ArrayList[Array[Int]]()
          g(c).add(Array(i, j))
        }
        j += 1
      }
      i += 1
    }
    val dirs = Array(-1, 0, 1, 0, -1)
    val INF = 1 << 30
    val dist = Array.fill(m, n)(INF)
    dist(0)(0) = 0
    val q = new java.util.ArrayDeque[Array[Int]]()
    q.add(Array(0, 0))
    while (!q.isEmpty) {
      val cur = q.pollFirst()
      i = cur(0)
      val j = cur(1)
      val d = dist(i)(j)
      if (i == m - 1 && j == n - 1) return d
      val c = matrix(i).charAt(j)
      if (g.contains(c)) {
        val it = g(c).iterator()
        while (it.hasNext) {
          val p = it.next()
          val x = p(0); val y = p(1)
          if (d < dist(x)(y)) {
            dist(x)(y) = d
            q.addFirst(Array(x, y))
          }
        }
        g.remove(c)
      }
      var idx = 0
      while (idx < 4) {
        val x = i + dirs(idx)
        val y = j + dirs(idx + 1)
        if (0 <= x && x < m && 0 <= y && y < n && matrix(x).charAt(y) != '#' && d + 1 < dist(x)(y)) {
          dist(x)(y) = d + 1
          q.addLast(Array(x, y))
        }
        idx += 1
      }
    }
    -1
  }
}
'''

FILES["3553_minimum_weighted_subgraph_with_the_required_paths_ii"] = r'''// LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

object Solution {
  val LOG = 17

  def minimumWeight(edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val n = edges.length + 1
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    for (e <- edges) {
      g(e(0)).add(Array(e(1), e(2)))
      g(e(1)).add(Array(e(0), e(2)))
    }
    val parent = Array.fill(LOG, n)(-1)
    val depth = new Array[Int](n)
    val dist = new Array[Int](n)

    def dfs(u: Int, p: Int): Unit = {
      parent(0)(u) = p
      val it = g(u).iterator()
      while (it.hasNext) {
        val e = it.next()
        val to = e(0); val w = e(1)
        if (to != p) {
          depth(to) = depth(u) + 1
          dist(to) = dist(u) + w
          dfs(to, u)
        }
      }
    }

    def lca(u0: Int, v0: Int): Int = {
      var u = u0
      var v = v0
      if (depth(u) < depth(v)) { val t = u; u = v; v = t }
      var k = LOG - 1
      while (k >= 0) {
        if (parent(k)(u) != -1 && depth(parent(k)(u)) >= depth(v)) u = parent(k)(u)
        k -= 1
      }
      if (u == v) return u
      k = LOG - 1
      while (k >= 0) {
        if (parent(k)(u) != -1 && parent(k)(u) != parent(k)(v)) {
          u = parent(k)(u)
          v = parent(k)(v)
        }
        k -= 1
      }
      parent(0)(u)
    }

    def path(u: Int, v: Int): Int = {
      val a = lca(u, v)
      dist(u) + dist(v) - 2 * dist(a)
    }

    dfs(0, -1)
    var k = 1
    while (k < LOG) {
      var v = 0
      while (v < n) {
        if (parent(k - 1)(v) != -1) parent(k)(v) = parent(k - 1)(parent(k - 1)(v))
        v += 1
      }
      k += 1
    }
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      val a = queries(i)(0); val b = queries(i)(1); val c = queries(i)(2)
      ans(i) = (path(a, b) + path(b, c) + path(a, c)) / 2
      i += 1
    }
    ans
  }
}
'''

FILES["3555_smallest_subarray_to_sort_in_every_sliding_window"] = r'''// LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
// https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

object Solution {
  def f(nums: Array[Int], i: Int, j: Int, inf: Int): Int = {
    var mi = inf
    var mx = -inf
    var l = -1
    var r = -1
    var p = i
    while (p <= j) {
      if (nums(p) < mx) r = p
      else mx = nums(p)
      val q = j - p + i
      if (nums(q) > mi) l = q
      else mi = nums(q)
      p += 1
    }
    if (r == -1) 0 else r - l + 1
  }

  def minSubarraySort(nums: Array[Int], k: Int): Array[Int] = {
    val inf = 1 << 30
    val n = nums.length
    val ans = new Array[Int](n - k + 1)
    var i = 0
    while (i <= n - k) {
      ans(i) = f(nums, i, i + k - 1, inf)
      i += 1
    }
    ans
  }
}
'''

FILES["3556_sum_of_largest_prime_substrings"] = r'''// LeetCode 3556 - Sum of Largest Prime Substrings
// https://leetcode.com/problems/sum-of-largest-prime-substrings/

object Solution {
  def isPrime(x: Long): Boolean = {
    if (x < 2) return false
    val sqrtX = math.sqrt(x.toDouble).toLong
    var i = 2L
    while (i <= sqrtX) {
      if (x % i == 0) return false
      i += 1
    }
    true
  }

  def sumOfLargestPrimes(s: String): Long = {
    val st = new java.util.HashSet[java.lang.Long]()
    val n = s.length
    var i = 0
    while (i < n) {
      var x = 0L
      var j = i
      while (j < n) {
        x = x * 10 + (s.charAt(j) - '0')
        if (isPrime(x)) st.add(x)
        j += 1
      }
      i += 1
    }
    val nums = new java.util.ArrayList[java.lang.Long](st)
    nums.sort(null)
    var ans = 0L
    i = nums.size() - 1
    while (i >= 0 && nums.size() - i <= 3) {
      ans += nums.get(i)
      i -= 1
    }
    ans
  }
}
'''

FILES["3557_find_maximum_number_of_non_intersecting_substrings"] = r'''// LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
// https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

object Solution {
  def maxSubstrings(word: String): Int = {
    var ans = 0
    val first = scala.collection.mutable.HashMap.empty[Char, Int]
    var i = 0
    while (i < word.length) {
      val c = word.charAt(i)
      if (!first.contains(c)) first(c) = i
      else if (i - first(c) + 1 >= 4) {
        ans += 1
        first.clear()
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3558_number_of_ways_to_assign_edge_weights_i"] = r'''// LeetCode 3558 - Number of Ways to Assign Edge Weights I
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

object Solution {
  def dfs(i: Int, fa: Int, g: Array[java.util.ArrayList[Integer]]): Int = {
    var res = 0
    val it = g(i).iterator()
    while (it.hasNext) {
      val j = it.next().intValue()
      if (j != fa) res = math.max(res, dfs(j, i, g) + 1)
    }
    res
  }

  def pow2(exp0: Int, mod: Int): Int = {
    var exp = exp0
    var a = 2L
    var res = 1L
    while (exp > 0) {
      if ((exp & 1) != 0) res = res * a % mod
      a = a * a % mod
      exp >>= 1
    }
    res.toInt
  }

  def assignEdgeWeights(edges: Array[Array[Int]]): Int = {
    val mod = 1000000007
    val n = edges.length + 1
    val g = Array.fill(n + 1)(new java.util.ArrayList[Integer]())
    for (e <- edges) {
      g(e(0)).add(e(1))
      g(e(1)).add(e(0))
    }
    pow2(dfs(1, 0, g) - 1, mod)
  }
}
'''

FILES["3559_number_of_ways_to_assign_edge_weights_ii"] = r'''// LeetCode 3559 - Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

object Solution {
  val MOD = 1000000007
  val LOG = 17

  def assignEdgeWeights(edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val n = edges.length + 1
    val depth = new Array[Int](n + 1)
    val graph = Array.fill(n + 1)(new java.util.ArrayList[Integer]())
    val parent = Array.fill(LOG, n + 1)(-1)
    for (e <- edges) {
      graph(e(0)).add(e(1))
      graph(e(1)).add(e(0))
    }

    def dfs(u: Int, p: Int): Unit = {
      parent(0)(u) = p
      val it = graph(u).iterator()
      while (it.hasNext) {
        val v = it.next().intValue()
        if (v != p) {
          depth(v) = depth(u) + 1
          dfs(v, u)
        }
      }
    }

    def lca(u0: Int, v0: Int): Int = {
      var u = u0
      var v = v0
      if (depth(u) < depth(v)) { val t = u; u = v; v = t }
      var k = LOG - 1
      while (k >= 0) {
        if (parent(k)(u) != -1 && depth(parent(k)(u)) >= depth(v)) u = parent(k)(u)
        k -= 1
      }
      if (u == v) return u
      k = LOG - 1
      while (k >= 0) {
        if (parent(k)(u) != -1 && parent(k)(u) != parent(k)(v)) {
          u = parent(k)(u)
          v = parent(k)(v)
        }
        k -= 1
      }
      parent(0)(u)
    }

    def modPow(exp0: Int): Int = {
      var exp = exp0
      var base = 2L
      var res = 1L
      while (exp > 0) {
        if ((exp & 1) != 0) res = res * base % MOD
        base = base * base % MOD
        exp >>= 1
      }
      res.toInt
    }

    dfs(1, -1)
    var k = 1
    while (k < LOG) {
      var v = 1
      while (v <= n) {
        if (parent(k - 1)(v) != -1) parent(k)(v) = parent(k - 1)(parent(k - 1)(v))
        v += 1
      }
      k += 1
    }
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      val u = queries(i)(0)
      val v = queries(i)(1)
      if (u == v) ans(i) = 0
      else {
        val a = lca(u, v)
        val d = depth(u) + depth(v) - 2 * depth(a)
        ans(i) = modPow(d - 1)
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3560_find_minimum_log_transportation_cost"] = r'''// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

object Solution {
  def minCuttingCost(n: Int, m: Int, k: Int): Long = {
    val x = math.max(n, m)
    if (x <= k) 0L else 1L * k * (x - k)
  }
}
'''

FILES["3561_resulting_string_after_adjacent_removals"] = r'''// LeetCode 3561 - Resulting String After Adjacent Removals
// https://leetcode.com/problems/resulting-string-after-adjacent-removals/

object Solution {
  def isContiguous(a: Char, b: Char): Boolean = {
    val x = math.abs(a - b)
    x == 1 || x == 25
  }

  def resultingString(s: String): String = {
    val stk = new StringBuilder
    for (c <- s.toCharArray) {
      if (stk.length > 0 && isContiguous(stk.charAt(stk.length - 1), c))
        stk.deleteCharAt(stk.length - 1)
      else stk.append(c)
    }
    stk.toString
  }
}
'''

FILES["3562_maximum_profit_from_trading_stocks_with_discounts"] = r'''// LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
// https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

object Solution {
  def maxProfit(n: Int, present: Array[Int], future: Array[Int], hierarchy: Array[Array[Int]], budget: Int): Int = {
    val g = Array.fill(n + 1)(new java.util.ArrayList[Integer]())
    for (e <- hierarchy) g(e(0)).add(e(1))

    def dfs(u: Int): Array[Array[Int]] = {
      val nxt = Array.ofDim[Int](budget + 1, 2)
      val it = g(u).iterator()
      while (it.hasNext) {
        val v = it.next().intValue()
        val fv = dfs(v)
        var j = budget
        while (j >= 0) {
          var jv = 0
          while (jv <= j) {
            var pre = 0
            while (pre < 2) {
              nxt(j)(pre) = math.max(nxt(j)(pre), nxt(j - jv)(pre) + fv(jv)(pre))
              pre += 1
            }
            jv += 1
          }
          j -= 1
        }
      }
      val f = Array.ofDim[Int](budget + 1, 2)
      val price = future(u - 1)
      var j = 0
      while (j <= budget) {
        var pre = 0
        while (pre < 2) {
          val cost = present(u - 1) / (pre + 1)
          if (j >= cost) {
            val buyProfit = nxt(j - cost)(1) + (price - cost)
            f(j)(pre) = math.max(nxt(j)(0), buyProfit)
          } else {
            f(j)(pre) = nxt(j)(0)
          }
          pre += 1
        }
        j += 1
      }
      f
    }

    dfs(1)(budget)(0)
  }
}
'''

FILES["3563_lexicographically_smallest_string_after_adjacent_removals"] = r'''// LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

object Solution {
  def isConsec(a: Char, b: Char): Boolean = {
    val d = math.abs(a - b)
    d == 1 || d == 25
  }

  def lexicographicallySmallestString(s: String): String = {
    val n = s.length
    val dp = Array.fill(n + 1, n + 1)("")
    var length = 1
    while (length <= n) {
      var i = 0
      while (i + length <= n) {
        val j = i + length
        var minStr = s.charAt(i) + dp(i + 1)(j)
        var k = i + 1
        while (k < j) {
          if (isConsec(s.charAt(i), s.charAt(k)) && dp(i + 1)(k).isEmpty) {
            val cand = dp(k + 1)(j)
            if (cand.compareTo(minStr) < 0) minStr = cand
          }
          k += 1
        }
        dp(i)(j) = minStr
        i += 1
      }
      length += 1
    }
    dp(0)(n)
  }
}
'''

FILES["3565_sequential_grid_path_cover"] = r'''// LeetCode 3565 - Sequential Grid Path Cover
// https://leetcode.com/problems/sequential-grid-path-cover/

object Solution {
  def findPath(grid: Array[Array[Int]], k: Int): java.util.List[java.util.List[Integer]] = {
    val m = grid.length
    val n = grid(0).length
    var st = 0L
    val path = new java.util.ArrayList[java.util.List[Integer]]()
    val dirs = Array(-1, 0, 1, 0, -1)

    def f(i: Int, j: Int): Int = i * n + j

    def dfs(i: Int, j: Int, v0: Int): Boolean = {
      var v = v0
      val cell = new java.util.ArrayList[Integer]()
      cell.add(i); cell.add(j)
      path.add(cell)
      if (path.size() == m * n) return true
      val idx = f(i, j)
      st |= 1L << idx
      if (grid(i)(j) == v) v += 1
      var t = 0
      while (t < 4) {
        val x = i + dirs(t)
        val y = j + dirs(t + 1)
        if (0 <= x && x < m && 0 <= y && y < n) {
          val idx2 = f(x, y)
          if (((st >> idx2) & 1L) == 0 && (grid(x)(y) == 0 || grid(x)(y) == v)) {
            if (dfs(x, y, v)) return true
          }
        }
        t += 1
      }
      path.remove(path.size() - 1)
      st ^= 1L << idx
      false
    }

    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 0 || grid(i)(j) == 1) {
          if (dfs(i, j, 1)) return path
          path.clear()
          st = 0
        }
        j += 1
      }
      i += 1
    }
    new java.util.ArrayList[java.util.List[Integer]]()
  }
}
'''

FILES["3566_partition_array_into_two_equal_product_subsets"] = r'''// LeetCode 3566 - Partition Array into Two Equal Product Subsets
// https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

object Solution {
  def checkEqualPartitions(nums: Array[Int], target: Long): Boolean = {
    val n = nums.length
    var i = 0
    while (i < (1 << n)) {
      var x = 1L
      var y = 1L
      var j = 0
      var overflow = false
      while (j < n && !overflow) {
        if (((i >> j) & 1) != 0) x *= nums(j)
        else y *= nums(j)
        if (x > target || y > target) overflow = true
        j += 1
      }
      if (x == target && y == target) return true
      i += 1
    }
    false
  }
}
'''

FILES["3567_minimum_absolute_difference_in_sliding_submatrix"] = r'''// LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
// https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

object Solution {
  def minAbsDiff(grid: Array[Array[Int]], k: Int): Array[Array[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val ans = Array.ofDim[Int](m - k + 1, n - k + 1)
    var i = 0
    while (i <= m - k) {
      var j = 0
      while (j <= n - k) {
        val nums = new java.util.ArrayList[Integer]()
        var x = i
        while (x < i + k) {
          var y = j
          while (y < j + k) { nums.add(grid(x)(y)); y += 1 }
          x += 1
        }
        nums.sort(null)
        var d = Integer.MAX_VALUE
        var t = 1
        while (t < nums.size()) {
          if (nums.get(t) != nums.get(t - 1))
            d = math.min(d, math.abs(nums.get(t) - nums.get(t - 1)))
          t += 1
        }
        if (d != Integer.MAX_VALUE) ans(i)(j) = d
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3568_minimum_moves_to_clean_the_classroom"] = r'''// LeetCode 3568 - Minimum Moves to Clean the Classroom
// https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

object Solution {
  def minMoves(classroom: Array[String], energy: Int): Int = {
    val m = classroom.length
    val n = classroom(0).length
    val d = Array.ofDim[Int](m, n)
    var x = 0
    var y = 0
    var cnt = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val c = classroom(i).charAt(j)
        if (c == 'S') { x = i; y = j }
        else if (c == 'L') { d(i)(j) = cnt; cnt += 1 }
        j += 1
      }
      i += 1
    }
    if (cnt == 0) return 0
    val vis = Array.ofDim[Boolean](m, n, energy + 1, 1 << cnt)
    var q = new java.util.ArrayList[Array[Int]]()
    q.add(Array(x, y, energy, (1 << cnt) - 1))
    vis(x)(y)(energy)((1 << cnt) - 1) = true
    val dirs = Array(-1, 0, 1, 0, -1)
    var ans = 0
    while (!q.isEmpty) {
      val t = q
      q = new java.util.ArrayList[Array[Int]]()
      val it = t.iterator()
      while (it.hasNext) {
        val s = it.next()
        i = s(0)
        val j = s(1)
        val curEnergy = s(2)
        val mask = s(3)
        if (mask == 0) return ans
        if (curEnergy > 0) {
          var k = 0
          while (k < 4) {
            val nx = i + dirs(k)
            val ny = j + dirs(k + 1)
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && classroom(nx).charAt(ny) != 'X') {
              val nxtEnergy = if (classroom(nx).charAt(ny) == 'R') energy else curEnergy - 1
              var nxtMask = mask
              if (classroom(nx).charAt(ny) == 'L') nxtMask &= ~(1 << d(nx)(ny))
              if (!vis(nx)(ny)(nxtEnergy)(nxtMask)) {
                vis(nx)(ny)(nxtEnergy)(nxtMask) = true
                q.add(Array(nx, ny, nxtEnergy, nxtMask))
              }
            }
            k += 1
          }
        }
      }
      ans += 1
    }
    -1
  }
}
'''

FILES["3569_maximize_count_of_distinct_primes_after_split"] = r'''// LeetCode 3569 - Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

object Solution {
  def maximumCount(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    var mx = 0
    for (v <- nums) mx = math.max(mx, v)
    for (q <- queries) mx = math.max(mx, q(1))
    val isP = new Array[Boolean](mx + 1)
    var i = 2
    while (i <= mx) { isP(i) = true; i += 1 }
    i = 2
    while (i * i <= mx) {
      if (isP(i)) {
        var j = i * i
        while (j <= mx) { isP(j) = false; j += i }
      }
      i += 1
    }
    val ans = new Array[Int](queries.length)
    var qi = 0
    while (qi < queries.length) {
      nums(queries(qi)(0)) = queries(qi)(1)
      var best = 0
      val left = scala.collection.mutable.HashMap.empty[Int, Int]
      val right = scala.collection.mutable.HashMap.empty[Int, Int]
      for (v <- nums) if (v <= mx && isP(v)) right(v) = right.getOrElse(v, 0) + 1
      i = 0
      while (i < nums.length - 1) {
        val v = nums(i)
        if (v <= mx && isP(v)) {
          left(v) = left.getOrElse(v, 0) + 1
          val c = right(v) - 1
          if (c == 0) right.remove(v)
          else right(v) = c
        }
        best = math.max(best, left.size + right.size)
        i += 1
      }
      ans(qi) = best
      qi += 1
    }
    ans
  }
}
'''

FILES["3571_find_the_shortest_superstring_ii"] = r'''// LeetCode 3571 - Find the Shortest Superstring II
// https://leetcode.com/problems/find-the-shortest-superstring-ii/

object Solution {
  def shortestSuperstring(s1: String, s2: String): String = {
    if (s1.length > s2.length) return shortestSuperstring(s2, s1)
    val m = s1.length
    if (s2.contains(s1)) return s2
    var i = 0
    while (i < m) {
      if (s2.startsWith(s1.substring(i))) return s1.substring(0, i) + s2
      val len = m - i
      if (s2.length >= len && s2.substring(s2.length - len) == s1.substring(0, len))
        return s2 + s1.substring(m - i)
      i += 1
    }
    s1 + s2
  }
}
'''

FILES["3572_maximize_ysum_by_picking_a_triplet_of_distinct_xvalues"] = r'''// LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
// https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

object Solution {
  def maxSumDistinctTriplet(x: Array[Int], y: Array[Int]): Int = {
    val n = x.length
    val arr = Array.ofDim[Int](n, 2)
    var i = 0
    while (i < n) { arr(i) = Array(x(i), y(i)); i += 1 }
    java.util.Arrays.sort(arr, (a: Array[Int], b: Array[Int]) => Integer.compare(b(1), a(1)))
    var ans = 0
    val vis = scala.collection.mutable.HashSet.empty[Int]
    i = 0
    while (i < n) {
      val a = arr(i)(0)
      val b = arr(i)(1)
      if (!vis.contains(a)) {
        vis.add(a)
        ans += b
        if (vis.size == 3) return ans
      }
      i += 1
    }
    -1
  }
}
'''

FILES["3573_best_time_to_buy_and_sell_stock_v"] = r'''// LeetCode 3573 - Best Time to Buy and Sell Stock V
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

object Solution {
  def maximumProfit(prices: Array[Int], k: Int): Long = {
    val n = prices.length
    val f = Array.ofDim[Long](n, k + 1, 3)
    var j = 1
    while (j <= k) {
      f(0)(j)(1) = -prices(0)
      f(0)(j)(2) = prices(0)
      j += 1
    }
    var i = 1
    while (i < n) {
      j = 1
      while (j <= k) {
        f(i)(j)(0) = math.max(f(i - 1)(j)(0), math.max(f(i - 1)(j)(1) + prices(i), f(i - 1)(j)(2) - prices(i)))
        f(i)(j)(1) = math.max(f(i - 1)(j)(1), f(i - 1)(j - 1)(0) - prices(i))
        f(i)(j)(2) = math.max(f(i - 1)(j)(2), f(i - 1)(j - 1)(0) + prices(i))
        j += 1
      }
      i += 1
    }
    f(n - 1)(k)(0)
  }
}
'''

FILES["3574_maximize_subarray_gcd_score"] = r'''// LeetCode 3574 - Maximize Subarray GCD Score
// https://leetcode.com/problems/maximize-subarray-gcd-score/

object Solution {
  def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) { val t = a % b; a = b; b = t }
    a
  }

  def maxGCDScore(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val cnt = new Array[Int](n)
    var i = 0
    while (i < n) {
      var x = nums(i)
      while (x % 2 == 0) { cnt(i) += 1; x /= 2 }
      i += 1
    }
    var ans = 0L
    var l = 0
    while (l < n) {
      var g = 0
      var mi = Integer.MAX_VALUE
      var t = 0
      var r = l
      while (r < n) {
        g = gcd(g, nums(r))
        if (cnt(r) < mi) { mi = cnt(r); t = 1 }
        else if (cnt(r) == mi) t += 1
        var score = 1L * g * (r - l + 1)
        if (t <= k) score *= 2
        ans = math.max(ans, score)
        r += 1
      }
      l += 1
    }
    ans
  }
}
'''

n = 0
for folder, content in FILES.items():
    (ROOT / folder / "Solution.scala").write_text(content, encoding="utf-8")
    n += 1
    print("wrote", folder)
print("TOTAL", n)
