#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3593_minimum_increments_to_equalize_leaf_paths"] = r'''// LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
// https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

object Solution {
  def minIncrease(n: Int, edges: Array[Array[Int]], cost: Array[Int]): Int = {
    val graph = Array.fill(n)(new java.util.ArrayList[Integer]())
    for (e <- edges) {
      graph(e(0)).add(e(1))
      graph(e(1)).add(e(0))
    }
    var ans = 0

    def dfs(u: Int, p: Int): Long = {
      if (graph(u).size() == 1 && p != -1) return cost(u)
      val childVals = new java.util.ArrayList[java.lang.Long]()
      val it = graph(u).iterator()
      while (it.hasNext) {
        val v = it.next().intValue()
        if (v != p) childVals.add(dfs(v, u))
      }
      if (childVals.isEmpty) return cost(u)
      var mx = 0L
      val cit = childVals.iterator()
      while (cit.hasNext) mx = math.max(mx, cit.next())
      val cit2 = childVals.iterator()
      while (cit2.hasNext) if (cit2.next() < mx) ans += 1
      mx + cost(u)
    }

    dfs(0, -1)
    ans
  }
}
'''

FILES["3594_minimum_time_to_transport_all_individuals"] = r'''// LeetCode 3594 - Minimum Time to Transport All Individuals
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

object Solution {
  def minTime(n: Int, k: Int, m: Int, time: Array[Int], mul: Array[Double]): Double = {
    val t = time.clone()
    java.util.Arrays.sort(t)
    var total = 0.0
    var stage = 0
    var left = n
    while (left > 0) {
      val take = math.min(k, left)
      val slow = t(left - 1)
      total += slow.toDouble * mul(stage % m)
      left -= take
      stage += 1
      if (left > 0) {
        total += t(0).toDouble * mul(stage % m)
        stage += 1
      }
    }
    total
  }
}
'''

FILES["3595_once_twice"] = r'''// LeetCode 3595 - Once Twice
// https://leetcode.com/problems/once-twice/

object Solution {
  def onceTwice(nums: Array[Int]): Array[Int] = {
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) freq(x) = freq.getOrElse(x, 0) + 1
    var a = 0
    var b = 0
    for ((k, v) <- freq) {
      if (v == 1) a = k
      else if (v == 2) b = k
    }
    Array(a, b)
  }
}
'''

FILES["3596_minimum_cost_path_with_alternating_directions_i"] = r'''// LeetCode 3596 - Minimum Cost Path with Alternating Directions I
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-i/

object Solution {
  def minCost(m: Int, n: Int): Int = {
    if (m == 1 && n == 1) 1
    else if (m == 1 && n == 2) 3
    else if (m == 2 && n == 1) 3
    else -1
  }
}
'''

FILES["3597_partition_string"] = r'''// LeetCode 3597 - Partition String
// https://leetcode.com/problems/partition-string/

object Solution {
  def partitionString(s: String): java.util.List[String] = {
    val vis = new java.util.HashSet[String]()
    val ans = new java.util.ArrayList[String]()
    val t = new StringBuilder
    for (c <- s.toCharArray) {
      t.append(c)
      val cur = t.toString
      if (!vis.contains(cur)) {
        vis.add(cur)
        ans.add(cur)
        t.setLength(0)
      }
    }
    ans
  }
}
'''

FILES["3598_longest_common_prefix_between_adjacent_strings_after_removals"] = r'''// LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
// https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

object Solution {
  def calc(s: String, t: String): Int = {
    val m = math.min(s.length, t.length)
    var k = 0
    while (k < m) {
      if (s.charAt(k) != t.charAt(k)) return k
      k += 1
    }
    m
  }

  def longestCommonPrefix(words: Array[String]): Array[Int] = {
    val n = words.length
    val tm = new java.util.TreeMap[Integer, Integer]()

    def add(i: Int, j: Int): Unit = {
      if (i >= 0 && i < n && j >= 0 && j < n)
        tm.merge(calc(words(i), words(j)), 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
    }

    def remove(i: Int, j: Int): Unit = {
      if (i >= 0 && i < n && j >= 0 && j < n) {
        val x = calc(words(i), words(j))
        val c = tm.get(x)
        if (c == 1) tm.remove(x)
        else tm.put(x, c - 1)
      }
    }

    var i = 0
    while (i + 1 < n) { add(i, i + 1); i += 1 }
    val ans = new Array[Int](n)
    i = 0
    while (i < n) {
      remove(i, i + 1)
      remove(i - 1, i)
      add(i - 1, i + 1)
      if (!tm.isEmpty && tm.lastKey() > 0) ans(i) = tm.lastKey()
      remove(i - 1, i + 1)
      add(i - 1, i)
      add(i, i + 1)
      i += 1
    }
    ans
  }
}
'''

FILES["3599_partition_array_to_minimize_xor"] = r'''// LeetCode 3599 - Partition Array to Minimize XOR
// https://leetcode.com/problems/partition-array-to-minimize-xor/

object Solution {
  def minXor(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val g = new Array[Int](n + 1)
    var i = 1
    while (i <= n) { g(i) = g(i - 1) ^ nums(i - 1); i += 1 }
    val Inf = Integer.MAX_VALUE / 2
    val f = Array.fill(n + 1, k + 1)(Inf)
    f(0)(0) = 0
    i = 1
    while (i <= n) {
      var j = 1
      while (j <= math.min(i, k)) {
        var h = j - 1
        while (h < i) {
          f(i)(j) = math.min(f(i)(j), math.max(f(h)(j - 1), g(i) ^ g(h)))
          h += 1
        }
        j += 1
      }
      i += 1
    }
    f(n)(k)
  }
}
'''

FILES["3600_maximize_spanning_tree_stability_with_upgrades"] = r'''// LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

object Solution {
  class UnionFind(n: Int) {
    val p = Array.tabulate(n)(i => i)
    val size = Array.fill(n)(1)
    var cnt = n

    def find(x0: Int): Int = {
      var x = x0
      if (p(x) != x) p(x) = find(p(x))
      p(x)
    }

    def unite(a: Int, b: Int): Boolean = {
      var pa = find(a)
      var pb = find(b)
      if (pa == pb) return false
      if (size(pa) > size(pb)) {
        p(pb) = pa
        size(pa) += size(pb)
      } else {
        p(pa) = pb
        size(pb) += size(pa)
      }
      cnt -= 1
      true
    }
  }

  def maxStability(n: Int, edges: Array[Array[Int]], k: Int): Int = {
    def check(lim: Int): Boolean = {
      val uf = new UnionFind(n)
      for (e <- edges) if (e(2) >= lim) uf.unite(e(0), e(1))
      var rem = k
      for (e <- edges) {
        if (e(2) * 2 >= lim && rem > 0) {
          if (uf.unite(e(0), e(1))) rem -= 1
        }
      }
      uf.cnt == 1
    }

    val uf = new UnionFind(n)
    var mn = 1000000
    for (e <- edges) {
      if (e(3) == 1) {
        mn = math.min(mn, e(2))
        if (!uf.unite(e(0), e(1))) return -1
      }
    }
    for (e <- edges) uf.unite(e(0), e(1))
    if (uf.cnt > 1) return -1
    var l = 1
    var r = mn
    while (l < r) {
      val mid = (l + r + 1) >> 1
      if (check(mid)) l = mid
      else r = mid - 1
    }
    l
  }
}
'''

FILES["3602_hexadecimal_and_hexatrigesimal_conversion"] = r'''// LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
// https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

object Solution {
  def f(x0: Int, k: Int): String = {
    var x = x0
    val res = new StringBuilder
    while (x > 0) {
      val v = x % k
      res.append(if (v <= 9) ('0' + v).toChar else ('A' + v - 10).toChar)
      x /= k
    }
    res.reverse.toString
  }

  def concatHex36(n: Int): String = f(n * n, 16) + f(n * n * n, 36)
}
'''

FILES["3603_minimum_cost_path_with_alternating_directions_ii"] = r'''// LeetCode 3603 - Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

object Solution {
  def entry(i: Int, j: Int): Long = 1L * (i + 1) * (j + 1)

  def minCost(m: Int, n: Int, waitCost: Array[Array[Int]]): Long = {
    val INF = Long.MaxValue / 4
    val dp = Array.fill(m, n)(INF)
    dp(0)(0) = entry(0, 0)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (!(i == 0 && j == 0)) {
          if (i > 0) {
            var cand = dp(i - 1)(j) + entry(i, j)
            if (!(i - 1 == 0 && j == 0)) cand += waitCost(i - 1)(j)
            dp(i)(j) = math.min(dp(i)(j), cand)
          }
          if (j > 0) {
            var cand = dp(i)(j - 1) + entry(i, j)
            if (!(i == 0 && j - 1 == 0)) cand += waitCost(i)(j - 1)
            dp(i)(j) = math.min(dp(i)(j), cand)
          }
        }
        j += 1
      }
      i += 1
    }
    dp(m - 1)(n - 1)
  }
}
'''

FILES["3604_minimum_time_to_reach_destination_in_directed_graph"] = r'''// LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

object Solution {
  def minTime(n: Int, edges: Array[Array[Int]]): Int = {
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    for (e <- edges) g(e(0)).add(Array(e(1), e(2), e(3)))
    val Inf = 1000000000000000000L
    val dist = Array.fill(n)(Inf)
    dist(0) = 0
    val pq = new java.util.PriorityQueue[Array[Long]]((a: Array[Long], b: Array[Long]) => java.lang.Long.compare(a(0), b(0)))
    pq.offer(Array(0L, 0L))
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val t = cur(0)
      val u = cur(1).toInt
      if (t == dist(u)) {
        if (u == n - 1) return t.toInt
        val it = g(u).iterator()
        while (it.hasNext) {
          val e = it.next()
          var nt = t
          if (nt <= e(2)) {
            if (nt < e(1)) nt = e(1)
            nt += 1
            if (nt < dist(e(0))) {
              dist(e(0)) = nt
              pq.offer(Array(nt, e(0).toLong))
            }
          }
        }
      }
    }
    if (dist(n - 1) == Inf) -1 else dist(n - 1).toInt
  }
}
'''

FILES["3605_minimum_stability_factor_of_array"] = r'''// LeetCode 3605 - Minimum Stability Factor of Array
// https://leetcode.com/problems/minimum-stability-factor-of-array/

object Solution {
  def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  def ok(nums: Array[Int], maxC: Int, x: Int): Boolean = {
    val n = nums.length
    if (x >= n) return true
    var changes = 0
    var i = 0
    while (i + x < n) {
      var g = nums(i)
      var j = i + 1
      while (j <= i + x) { g = gcd(g, nums(j)); j += 1 }
      if (g > 1) {
        changes += 1
        i += x + 1
      } else i += 1
    }
    changes <= maxC
  }

  def minStable(nums: Array[Int], maxC: Int): Int = {
    val n = nums.length
    var lo = 0
    var hi = n
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(nums, maxC, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }
}
'''

FILES["3606_coupon_code_validator"] = r'''// LeetCode 3606 - Coupon Code Validator
// https://leetcode.com/problems/coupon-code-validator/

object Solution {
  def check(s: String): Boolean = {
    if (s.isEmpty) return false
    for (c <- s.toCharArray)
      if (!Character.isLetterOrDigit(c) && c != '_') return false
    true
  }

  def validateCoupons(code: Array[String], businessLine: Array[String], isActive: Array[Boolean]): java.util.List[String] = {
    val bs = new java.util.HashSet[String]()
    java.util.Collections.addAll(bs, "electronics", "grocery", "pharmacy", "restaurant")
    val idx = new java.util.ArrayList[Integer]()
    var i = 0
    while (i < code.length) {
      if (isActive(i) && bs.contains(businessLine(i)) && check(code(i))) idx.add(i)
      i += 1
    }
    idx.sort((a: Integer, b: Integer) => {
      val c = businessLine(a).compareTo(businessLine(b))
      if (c != 0) c else code(a).compareTo(code(b))
    })
    val ans = new java.util.ArrayList[String]()
    val it = idx.iterator()
    while (it.hasNext) ans.add(code(it.next()))
    ans
  }
}
'''

FILES["3607_power_grid_maintenance"] = r'''// LeetCode 3607 - Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/

object Solution {
  def processQueries(c: Int, connections: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val parent = Array.tabulate(c + 1)(i => i)

    def find(x0: Int): Int = {
      var x = x0
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }

    def unite(a: Int, b: Int): Unit = {
      val ra = find(a)
      val rb = find(b)
      if (ra != rb) {
        if (ra < rb) parent(rb) = ra
        else parent(ra) = rb
      }
    }

    for (e <- connections) unite(e(0), e(1))
    val online = Array.fill(c + 1)(true)
    val comp = scala.collection.mutable.HashMap.empty[Int, java.util.ArrayList[Integer]]
    var i = 1
    while (i <= c) {
      val r = find(i)
      if (!comp.contains(r)) comp(r) = new java.util.ArrayList[Integer]()
      comp(r).add(i)
      i += 1
    }
    for (ids <- comp.values) java.util.Collections.sort(ids)
    val ptr = scala.collection.mutable.HashMap.empty[Int, Int]
    val ans = new java.util.ArrayList[Integer]()
    for (q <- queries) {
      val t = q(0)
      val x = q(1)
      if (t == 2) online(x) = false
      else if (online(x)) ans.add(x)
      else {
        val r = find(x)
        val ids = comp(r)
        var p = ptr.getOrElse(r, 0)
        while (p < ids.size() && !online(ids.get(p))) p += 1
        ptr(r) = p
        ans.add(if (p < ids.size()) ids.get(p) else -1)
      }
    }
    val out = new Array[Int](ans.size())
    var t = 0
    while (t < ans.size()) { out(t) = ans.get(t); t += 1 }
    out
  }
}
'''

FILES["3608_minimum_time_for_k_connected_components"] = r'''// LeetCode 3608 - Minimum Time for K Connected Components
// https://leetcode.com/problems/minimum-time-for-k-connected-components/

object Solution {
  class UnionFind(n: Int) {
    val p = Array.tabulate(n)(i => i)
    val size = Array.fill(n)(1)

    def find(x0: Int): Int = {
      var x = x0
      if (p(x) != x) p(x) = find(p(x))
      p(x)
    }

    def unite(a: Int, b: Int): Boolean = {
      val pa = find(a)
      val pb = find(b)
      if (pa == pb) return false
      if (size(pa) > size(pb)) {
        p(pb) = pa
        size(pa) += size(pb)
      } else {
        p(pa) = pb
        size(pb) += size(pa)
      }
      true
    }
  }

  def minTime(n: Int, edges: Array[Array[Int]], k: Int): Int = {
    java.util.Arrays.sort(edges, (a: Array[Int], b: Array[Int]) => Integer.compare(a(2), b(2)))
    val uf = new UnionFind(n)
    var cnt = n
    var i = edges.length - 1
    while (i >= 0) {
      if (uf.unite(edges(i)(0), edges(i)(1))) {
        cnt -= 1
        if (cnt < k) return edges(i)(2)
      }
      i -= 1
    }
    0
  }
}
'''

FILES["3609_minimum_moves_to_reach_target_in_grid"] = r'''// LeetCode 3609 - Minimum Moves to Reach Target in Grid
// https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/

object Solution {
  def minMoves(sx: Int, sy: Int, tx0: Int, ty0: Int): Int = {
    var tx = tx0
    var ty = ty0
    var ans = 0
    while (tx > sx || ty > sy) {
      if (tx < sx || ty < sy) return -1
      if (tx == ty) return -1
      if (tx > ty) {
        if (ty > sy) {
          if (tx >= 2 * ty) {
            if (tx % 2 != 0) return -1
            tx /= 2
          } else tx -= ty
          ans += 1
        } else {
          if (ty != sy) return -1
          while (tx > sx) {
            if (tx >= 2 * ty) {
              if (tx % 2 != 0) return -1
              tx /= 2
            } else tx -= ty
            ans += 1
            if (tx < sx) return -1
          }
        }
      } else {
        if (tx > sx) {
          if (ty >= 2 * tx) {
            if (ty % 2 != 0) return -1
            ty /= 2
          } else ty -= tx
          ans += 1
        } else {
          if (tx != sx) return -1
          while (ty > sy) {
            if (ty >= 2 * tx) {
              if (ty % 2 != 0) return -1
              ty /= 2
            } else ty -= tx
            ans += 1
            if (ty < sy) return -1
          }
        }
      }
    }
    if (tx == sx && ty == sy) ans else -1
  }
}
'''

FILES["3610_minimum_number_of_primes_to_sum_to_target"] = r'''// LeetCode 3610 - Minimum Number of Primes to Sum to Target
// https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

object Solution {
  val primes = new java.util.ArrayList[Integer]()

  def ensurePrimes(): Unit = {
    if (primes.size() > 0) return
    var x = 2
    while (primes.size() < 1000) {
      var isPrime = true
      val it = primes.iterator()
      var done = false
      while (it.hasNext && !done) {
        val p = it.next()
        if (p * p > x) done = true
        else if (x % p == 0) { isPrime = false; done = true }
      }
      if (isPrime) primes.add(x)
      x += 1
    }
  }

  def minNumberOfPrimes(n: Int, m: Int): Int = {
    ensurePrimes()
    val Inf = Integer.MAX_VALUE / 2
    val f = Array.fill(n + 1)(Inf)
    f(0) = 0
    var pi = 0
    while (pi < m) {
      val x = primes.get(pi)
      var i = x
      while (i <= n) {
        if (f(i - x) + 1 < f(i)) f(i) = f(i - x) + 1
        i += 1
      }
      pi += 1
    }
    if (f(n) < Inf) f(n) else -1
  }
}
'''

n = 0
for folder, content in FILES.items():
    (ROOT / folder / "Solution.scala").write_text(content, encoding="utf-8")
    n += 1
    print("wrote", folder)
print("TOTAL", n)
