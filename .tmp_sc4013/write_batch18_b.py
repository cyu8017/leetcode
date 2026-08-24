#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3524_find_x_value_of_array_i"] = r'''// LeetCode 3524 - Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/

object Solution {
  def resultArray(nums: Array[Int], k: Int): Array[Long] = {
    val ans = new Array[Long](k)
    var dp = new Array[Long](k)
    for (num <- nums) {
      val newDp = new Array[Long](k)
      val nm = num % k
      newDp(nm) = 1
      var i = 0
      while (i < k) { newDp((i * nm) % k) += dp(i); i += 1 }
      i = 0
      while (i < k) { ans(i) += newDp(i); i += 1 }
      dp = newDp
    }
    ans
  }
}
'''

FILES["3525_find_x_value_of_array_ii"] = r'''// LeetCode 3525 - Find X Value of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/

object Solution {
  def resultArray(nums: Array[Int], k: Int, queries: Array[Array[Int]]): Array[Int] = {
    val n = nums.length
    val ans = new Array[Int](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val idx = queries(qi)(0)
      val `val` = queries(qi)(1)
      val start = queries(qi)(2)
      val x = queries(qi)(3)
      nums(idx) = `val`
      var prod = 1
      var cnt = 0
      var i = start
      while (i < n) {
        prod = prod * (nums(i) % k) % k
        if (prod == x) cnt += 1
        i += 1
      }
      ans(qi) = cnt
      qi += 1
    }
    ans
  }
}
'''

FILES["3526_range_xor_queries_with_subarray_reversals"] = r'''// LeetCode 3526 - Range XOR Queries with Subarray Reversals
// https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

object Solution {
  def getResults(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val a = nums.clone()
    val ans = new java.util.ArrayList[Integer]()
    for (q <- queries) {
      val typ = q(0)
      if (typ == 1) {
        var l = q(1)
        var r = q(2)
        while (l < r) {
          val tmp = a(l); a(l) = a(r); a(r) = tmp
          l += 1; r -= 1
        }
      } else if (typ == 2) {
        val l = q(1); val r = q(2)
        var x = 0
        var i = l
        while (i <= r) { x ^= a(i); i += 1 }
        ans.add(x)
      } else {
        a(q(1)) = q(2)
      }
    }
    val out = new Array[Int](ans.size())
    var t = 0
    while (t < ans.size()) { out(t) = ans.get(t); t += 1 }
    out
  }
}
'''

FILES["3527_find_the_most_common_response"] = r'''// LeetCode 3527 - Find the Most Common Response
// https://leetcode.com/problems/find-the-most-common-response/

object Solution {
  def findCommonResponse(responses: java.util.List[java.util.List[String]]): String = {
    val cnt = scala.collection.mutable.HashMap.empty[String, Int]
    val it = responses.iterator()
    while (it.hasNext) {
      val ws = it.next()
      val s = scala.collection.mutable.HashSet.empty[String]
      val wit = ws.iterator()
      while (wit.hasNext) {
        val w = wit.next()
        if (s.add(w)) cnt(w) = cnt.getOrElse(w, 0) + 1
      }
    }
    var ans = responses.get(0).get(0)
    for ((w, v) <- cnt) {
      if (cnt(ans) < v || (cnt(ans) == v && w.compareTo(ans) < 0)) ans = w
    }
    ans
  }
}
'''

FILES["3528_unit_conversion_i"] = r'''// LeetCode 3528 - Unit Conversion I
// https://leetcode.com/problems/unit-conversion-i/

object Solution {
  def baseUnitConversions(conversions: Array[Array[Int]]): Array[Int] = {
    val mod = 1000000007
    val n = conversions.length + 1
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    for (e <- conversions) g(e(0)).add(Array(e(1), e(2)))
    val ans = new Array[Int](n)
    def dfs(s: Int, mul: Int): Unit = {
      ans(s) = mul
      val it = g(s).iterator()
      while (it.hasNext) {
        val e = it.next()
        dfs(e(0), ((1L * mul * e(1)) % mod).toInt)
      }
    }
    dfs(0, 1)
    ans
  }
}
'''

FILES["3529_count_cells_in_overlapping_horizontal_and_vertical_substrings"] = r'''// LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
// https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

object Solution {
  def countCells(grid: Array[Array[Char]], pattern: String): Int = {
    val m = grid.length
    val n = grid(0).length
    val row = new StringBuilder(m * n)
    val col = new StringBuilder(m * n)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) { row.append(grid(i)(j)); j += 1 }
      i += 1
    }
    var j = 0
    while (j < n) {
      i = 0
      while (i < m) { col.append(grid(i)(j)); i += 1 }
      j += 1
    }
    val rowS = row.toString
    val colS = col.toString
    val hMark = Array.ofDim[Boolean](m, n)
    val vMark = Array.ofDim[Boolean](m, n)
    val plen = pattern.length
    i = 0
    while (i + plen <= rowS.length) {
      if (rowS.substring(i, i + plen) == pattern) {
        var t = 0
        while (t < plen) {
          val pos = i + t
          hMark(pos / n)(pos % n) = true
          t += 1
        }
      }
      i += 1
    }
    i = 0
    while (i + plen <= colS.length) {
      if (colS.substring(i, i + plen) == pattern) {
        var t = 0
        while (t < plen) {
          val pos = i + t
          vMark(pos % m)(pos / m) = true
          t += 1
        }
      }
      i += 1
    }
    var ans = 0
    i = 0
    while (i < m) {
      j = 0
      while (j < n) {
        if (hMark(i)(j) && vMark(i)(j)) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3530_maximum_profit_from_valid_topological_order_in_dag"] = r'''// LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
// https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

object Solution {
  def pop(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x != 0) { c += x & 1; x >>= 1 }
    c
  }

  def maxProfit(n: Int, edges: Array[Array[Int]], score: Array[Int]): Int = {
    val need = new Array[Int](n)
    val dp = Array.fill(1 << n)(-1)
    dp(0) = 0
    for (e <- edges) need(e(1)) |= 1 << e(0)
    var mask = 0
    while (mask < (1 << n)) {
      if (dp(mask) >= 0) {
        val pos = pop(mask) + 1
        var i = 0
        while (i < n) {
          if (((mask >> i) & 1) == 0 && (mask & need(i)) == need(i)) {
            val nm = mask | (1 << i)
            val v = dp(mask) + score(i) * pos
            if (v > dp(nm)) dp(nm) = v
          }
          i += 1
        }
      }
      mask += 1
    }
    dp((1 << n) - 1)
  }
}
'''

FILES["3531_count_covered_buildings"] = r'''// LeetCode 3531 - Count Covered Buildings
// https://leetcode.com/problems/count-covered-buildings/

object Solution {
  def countCoveredBuildings(n: Int, buildings: Array[Array[Int]]): Int = {
    val g1 = scala.collection.mutable.HashMap.empty[Int, java.util.ArrayList[Integer]]
    val g2 = scala.collection.mutable.HashMap.empty[Int, java.util.ArrayList[Integer]]
    for (b <- buildings) {
      if (!g1.contains(b(0))) g1(b(0)) = new java.util.ArrayList[Integer]()
      if (!g2.contains(b(1))) g2(b(1)) = new java.util.ArrayList[Integer]()
      g1(b(0)).add(b(1))
      g2(b(1)).add(b(0))
    }
    for (list <- g1.values) java.util.Collections.sort(list)
    for (list <- g2.values) java.util.Collections.sort(list)
    var ans = 0
    for (b <- buildings) {
      val x = b(0); val y = b(1)
      val l1 = g1(x)
      val l2 = g2(y)
      if (l2.get(0) < x && x < l2.get(l2.size() - 1) && l1.get(0) < y && y < l1.get(l1.size() - 1)) ans += 1
    }
    ans
  }
}
'''

FILES["3532_path_existence_queries_in_a_graph_i"] = r'''// LeetCode 3532 - Path Existence Queries in a Graph I
// https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

object Solution {
  def pathExistenceQueries(n: Int, nums: Array[Int], maxDiff: Int, queries: Array[Array[Int]]): Array[Boolean] = {
    val g = new Array[Int](n)
    var cnt = 0
    var i = 1
    while (i < n) {
      if (nums(i) - nums(i - 1) > maxDiff) cnt += 1
      g(i) = cnt
      i += 1
    }
    val ans = new Array[Boolean](queries.length)
    i = 0
    while (i < queries.length) {
      ans(i) = g(queries(i)(0)) == g(queries(i)(1))
      i += 1
    }
    ans
  }
}
'''

FILES["3533_concatenated_divisibility"] = r'''// LeetCode 3533 - Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/

object Solution {
  def concatenatedDivisibility(nums0: Array[Int], k: Int): Array[Int] = {
    java.util.Arrays.sort(nums0)
    val nums = nums0
    val n = nums.length
    val pows = new Array[Int](n)
    var i = 0
    while (i < n) {
      var p = 1
      val num = nums(i)
      if (num == 0) p = 10 % k
      else {
        var x = num
        while (x > 0) { p = p * 10 % k; x /= 10 }
      }
      pows(i) = p
      i += 1
    }
    val memo = scala.collection.mutable.HashMap.empty[Long, Boolean]

    def dp(mask: Int, mod: Int): Boolean = {
      if (mask == (1 << n) - 1) return mod == 0
      val key = (mask.toLong << 32) | mod
      if (memo.contains(key)) return memo(key)
      var i = 0
      while (i < n) {
        if (((mask >> i) & 1) == 0) {
          val nm = (mod * pows(i) + nums(i)) % k
          if (dp(mask | (1 << i), nm)) {
            memo(key) = true
            return true
          }
        }
        i += 1
      }
      memo(key) = false
      false
    }

    def reconstruct(mask: Int, mod: Int): java.util.ArrayList[Integer] = {
      var i = 0
      while (i < n) {
        if (((mask >> i) & 1) == 0) {
          val nm = (mod * pows(i) + nums(i)) % k
          if (dp(mask | (1 << i), nm)) {
            val rest = reconstruct(mask | (1 << i), nm)
            rest.add(0, nums(i))
            return rest
          }
        }
        i += 1
      }
      new java.util.ArrayList[Integer]()
    }

    if (!dp(0, 0)) return Array.empty[Int]
    val res = reconstruct(0, 0)
    val out = new Array[Int](res.size())
    var t = 0
    while (t < res.size()) { out(t) = res.get(t); t += 1 }
    out
  }
}
'''

FILES["3534_path_existence_queries_in_a_graph_ii"] = r'''// LeetCode 3534 - Path Existence Queries in a Graph II
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

object Solution {
  def pathExistenceQueries(n: Int, nums: Array[Int], maxDiff: Int, queries: Array[Array[Int]]): Array[Int] = {
    val pairs = Array.ofDim[Int](n, 2)
    var i = 0
    while (i < n) { pairs(i) = Array(nums(i), i); i += 1 }
    java.util.Arrays.sort(pairs, (a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    val m = 20
    val f = Array.ofDim[Int](n, m)
    var r = n - 1
    var l = n - 1
    while (l >= 0) {
      while (pairs(r)(0) - pairs(l)(0) > maxDiff) r -= 1
      i = pairs(l)(1)
      val j = pairs(r)(1)
      f(i)(0) = j
      var k = 1
      while (k < m) { f(i)(k) = f(f(i)(k - 1))(k - 1); k += 1 }
      l -= 1
    }
    val ans = new java.util.ArrayList[Integer]()
    for (q <- queries) {
      var ii = q(0)
      var jj = q(1)
      if (nums(ii) > nums(jj)) { val tmp = ii; ii = jj; jj = tmp }
      if (ii == jj) ans.add(0)
      else if (nums(ii) == nums(jj)) ans.add(1)
      else {
        var d = 0
        var k = m - 1
        while (k >= 0) {
          if (nums(f(ii)(k)) < nums(jj)) {
            d |= 1 << k
            ii = f(ii)(k)
          }
          k -= 1
        }
        if (nums(f(ii)(0)) < nums(jj)) ans.add(-1)
        else ans.add(d + 1)
      }
    }
    val out = new Array[Int](ans.size())
    var t = 0
    while (t < ans.size()) { out(t) = ans.get(t); t += 1 }
    out
  }
}
'''

FILES["3535_unit_conversion_ii"] = r'''// LeetCode 3535 - Unit Conversion II
// https://leetcode.com/problems/unit-conversion-ii/

object Solution {
  val MOD = 1000000007

  def qpow(x0: Long, n0: Int): Long = {
    var x = x0
    var n = n0
    var res = 1L
    while (n > 0) {
      if ((n & 1) != 0) res = res * x % MOD
      x = x * x % MOD
      n >>= 1
    }
    res
  }

  def queryConversions(conversions: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val n = conversions.length + 1
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    for (e <- conversions) g(e(0)).add(Array(e(1), e(2)))
    val res = new Array[Int](n)
    def dfs(s: Int, mul: Int): Unit = {
      res(s) = mul
      val it = g(s).iterator()
      while (it.hasNext) {
        val e = it.next()
        dfs(e(0), ((1L * mul * e(1)) % MOD).toInt)
      }
    }
    dfs(0, 1)
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      ans(i) = ((1L * res(queries(i)(1)) * qpow(res(queries(i)(0)), MOD - 2)) % MOD).toInt
      i += 1
    }
    ans
  }
}
'''

FILES["3536_maximum_product_of_two_digits"] = r'''// LeetCode 3536 - Maximum Product of Two Digits
// https://leetcode.com/problems/maximum-product-of-two-digits/

object Solution {
  def maxProduct(n0: Int): Int = {
    var n = n0
    var a = 0
    var b = 0
    while (n > 0) {
      val x = n % 10
      if (a < x) { b = a; a = x }
      else if (b < x) b = x
      n /= 10
    }
    a * b
  }
}
'''

FILES["3537_fill_a_special_grid"] = r'''// LeetCode 3537 - Fill a Special Grid
// https://leetcode.com/problems/fill-a-special-grid/

object Solution {
  def specialGrid(n: Int): Array[Array[Int]] = {
    val m = 1 << n
    val ans = Array.ofDim[Int](m, m)
    var value = 0
    def dfs(x: Int, y: Int, k: Int): Unit = {
      if (k == 1) {
        ans(x)(y) = value
        value += 1
        return
      }
      val h = k / 2
      dfs(x, y, h)
      dfs(x + h, y, h)
      dfs(x + h, y - h, h)
      dfs(x, y - h, h)
    }
    dfs(0, m - 1, m)
    ans
  }
}
'''

FILES["3538_merge_operations_for_minimum_travel_time"] = r'''// LeetCode 3538 - Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

object Solution {
  val INF = 1000000000000000000L

  def minTravelTime(l: Int, n: Int, k: Int, position: Array[Int], time: Array[Int]): Int = {
    val prefix = new Array[Int](n)
    prefix(0) = time(0)
    var i = 1
    while (i < n) { prefix(i) = prefix(i - 1) + time(i); i += 1 }
    val memo = scala.collection.mutable.HashMap.empty[String, Long]

    def dp(i: Int, skips: Int, last: Int): Long = {
      if (i == n - 1) return if (skips == 0) 0L else INF
      val key = i + "," + skips + "," + last
      if (memo.contains(key)) return memo(key)
      var rate = prefix(i)
      if (last > 0) rate -= prefix(last - 1)
      var res = INF
      var end = n - 1
      if (i + skips + 1 < end) end = i + skips + 1
      var j = i + 1
      while (j <= end) {
        val cand = 1L * (position(j) - position(i)) * rate + dp(j, skips - (j - i - 1), i + 1)
        if (cand < res) res = cand
        j += 1
      }
      memo(key) = res
      res
    }

    dp(0, k, 0).toInt
  }
}
'''

FILES["3539_find_sum_of_array_product_of_magical_sequences"] = r'''// LeetCode 3539 - Find Sum of Array Product of Magical Sequences
// https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

object Solution {
  val N = 31
  val MOD = 1000000007
  val f = new Array[Long](N)
  val g = new Array[Long](N)
  var inited = false

  def qpow(a0: Long, k0: Long): Long = {
    var a = a0
    var k = k0
    var res = 1L
    while (k > 0) {
      if ((k & 1) != 0) res = res * a % MOD
      a = a * a % MOD
      k >>= 1
    }
    res
  }

  def initFact(): Unit = {
    if (inited) return
    f(0) = 1
    g(0) = 1
    var i = 1
    while (i < N) {
      f(i) = f(i - 1) * i % MOD
      g(i) = qpow(f(i), MOD - 2)
      i += 1
    }
    inited = true
  }

  def comb(m: Int, nn: Int): Long = {
    if (nn < 0 || nn > m) return 0
    f(m) * g(nn) % MOD * g(m - nn) % MOD
  }

  def magicalSum(m: Int, k: Int, nums: Array[Int]): Int = {
    initFact()
    val n = nums.length
    val dp = Array.fill(n + 1, m + 1, k + 1, N)(-1L)

    def dfs(i: Int, j: Int, kk: Int, st: Int): Long = {
      if (kk < 0 || (i == n && j > 0)) return 0
      if (i == n) {
        var k2 = kk
        var st2 = st
        while (st2 > 0) { k2 -= st2 & 1; st2 >>= 1 }
        return if (k2 == 0) 1 else 0
      }
      if (dp(i)(j)(kk)(st) != -1) return dp(i)(j)(kk)(st)
      var res = 0L
      var t = 0
      while (t <= j) {
        val nt = t + st
        val nk = kk - (nt & 1)
        val p = qpow(nums(i), t)
        val tmp = comb(j, t) * p % MOD * dfs(i + 1, j - t, nk, nt >> 1) % MOD
        res = (res + tmp) % MOD
        t += 1
      }
      dp(i)(j)(kk)(st) = res
      res
    }

    dfs(0, m, k, 0).toInt
  }
}
'''

FILES["3540_minimum_time_to_visit_all_houses"] = r'''// LeetCode 3540 - Minimum Time to Visit All Houses
// https://leetcode.com/problems/minimum-time-to-visit-all-houses/

object Solution {
  def minTotalTime(forward: Array[Int], backward: Array[Int], queries: Array[Int]): Long = {
    val n = forward.length
    var sumB = 0
    for (v <- backward) sumB += v
    val pf = new Array[Int](n + 1)
    val pb = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      pf(i + 1) = pf(i) + forward(i)
      pb(i + 1) = pb(i) + backward(i)
      i += 1
    }
    var ans = 0L
    var pos = 0
    for (q <- queries) {
      var r = 0
      if (q < pos) r = pf(n)
      r += pf(q) - pf(pos)
      var l = 0
      if (q > pos) l = sumB
      l += pb(pos) - pb(q)
      ans += math.min(l, r)
      pos = q
    }
    ans
  }
}
'''

FILES["3541_find_most_frequent_vowel_and_consonant"] = r'''// LeetCode 3541 - Find Most Frequent Vowel and Consonant
// https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

object Solution {
  def maxFreqSum(s: String): Int = {
    val cnt = new Array[Int](26)
    for (c <- s.toCharArray) cnt(c - 'a') += 1
    var a = 0
    var b = 0
    var i = 0
    while (i < 26) {
      val c = ('a' + i).toChar
      if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') a = math.max(a, cnt(i))
      else b = math.max(b, cnt(i))
      i += 1
    }
    a + b
  }
}
'''

FILES["3542_minimum_operations_to_convert_all_elements_to_zero"] = r'''// LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    val stk = new java.util.ArrayList[Integer]()
    var ans = 0
    for (x <- nums) {
      while (stk.size() > 0 && stk.get(stk.size() - 1) > x) {
        ans += 1
        stk.remove(stk.size() - 1)
      }
      if (x != 0 && (stk.size() == 0 || stk.get(stk.size() - 1) != x)) stk.add(x)
    }
    ans += stk.size()
    ans
  }
}
'''

FILES["3543_maximum_weighted_k_edge_path"] = r'''// LeetCode 3543 - Maximum Weighted K-Edge Path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/

object Solution {
  def maxWeight(n: Int, edges: Array[Array[Int]], k: Int, t: Int): Int = {
    val graph = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    for (e <- edges) graph(e(0)).add(Array(e(1), e(2)))
    val dp = Array.fill(n, k + 1)(new java.util.HashSet[Integer]())
    var u = 0
    while (u < n) { dp(u)(0).add(0); u += 1 }
    var i = 0
    while (i < k) {
      u = 0
      while (u < n) {
        val it = dp(u)(i).iterator()
        while (it.hasNext) {
          val sum = it.next().intValue()
          val eit = graph(u).iterator()
          while (eit.hasNext) {
            val e = eit.next()
            val ns = sum + e(1)
            if (ns < t) dp(e(0))(i + 1).add(ns)
          }
        }
        u += 1
      }
      i += 1
    }
    var ans = -1
    u = 0
    while (u < n) {
      val it = dp(u)(k).iterator()
      while (it.hasNext) {
        val sum = it.next().intValue()
        if (sum > ans) ans = sum
      }
      u += 1
    }
    ans
  }
}
'''

FILES["3544_subtree_inversion_sum"] = r'''// LeetCode 3544 - Subtree Inversion Sum
// https://leetcode.com/problems/subtree-inversion-sum/

object Solution {
  def subtreeInversionSum(edges: Array[Array[Int]], nums: Array[Int], k: Int): Long = {
    val n = edges.length + 1
    val graph = Array.fill(n)(new java.util.ArrayList[Integer]())
    for (e <- edges) {
      graph(e(0)).add(e(1))
      graph(e(1)).add(e(0))
    }
    val parent = Array.fill(n)(-1)
    val memo = scala.collection.mutable.HashMap.empty[String, Long]

    def dp(u: Int, steps: Int, inv: Boolean): Long = {
      val key = u + "," + steps + "," + inv
      if (memo.contains(key)) return memo(key)
      var num = nums(u).toLong
      if (inv) num = -num
      var negNum = -num
      val it = graph(u).iterator()
      while (it.hasNext) {
        val v = it.next().intValue()
        if (v != parent(u)) {
          parent(v) = u
          var ns = steps + 1
          if (ns > k) ns = k
          num += dp(v, ns, inv)
          if (steps == k) negNum += dp(v, 1, !inv)
        }
      }
      var res = num
      if (steps == k && negNum > res) res = negNum
      memo(key) = res
      res
    }

    dp(0, k, false)
  }
}
'''

FILES["3545_minimum_deletions_for_at_most_k_distinct_characters"] = r'''// LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
// https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

object Solution {
  def minDeletion(s: String, k: Int): Int = {
    val cnt = new Array[Int](26)
    for (c <- s.toCharArray) cnt(c - 'a') += 1
    java.util.Arrays.sort(cnt)
    var ans = 0
    var i = 0
    while (i + k < 26) { ans += cnt(i); i += 1 }
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
