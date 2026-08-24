#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3612_process_string_with_special_operations_i"] = r'''// LeetCode 3612 - Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/

object Solution {
  def processStr(s: String): String = {
    val result = new StringBuilder
    s.foreach { c =>
      if (c.isLetter) result.append(c)
      else if (c == '*') {
        if (result.length > 0) result.setLength(result.length - 1)
      } else if (c == '#') result.append(result)
      else if (c == '%') result.reverse()
    }
    result.toString
  }
}
'''

FILES["3613_minimize_maximum_component_cost"] = r'''// LeetCode 3613 - Minimize Maximum Component Cost
// https://leetcode.com/problems/minimize-maximum-component-cost/

object Solution {
  def minCost(n: Int, edges: Array[Array[Int]], k: Int): Int = {
    val p = Array.tabulate(n)(i => i)
    def find(x: Int): Int = {
      if (p(x) == x) x
      else {
        p(x) = find(p(x))
        p(x)
      }
    }
    if (k == n) return 0
    val sorted = edges.sortBy(_(2))
    var cnt = n
    for (e <- sorted) {
      val pu = find(e(0))
      val pv = find(e(1))
      if (pu != pv) {
        p(pu) = pv
        cnt -= 1
        if (cnt <= k) return e(2)
      }
    }
    0
  }
}
'''

FILES["3614_process_string_with_special_operations_ii"] = r'''// LeetCode 3614 - Process String with Special Operations II
// https://leetcode.com/problems/process-string-with-special-operations-ii/

object Solution {
  def processStr(s: String, k0: Long): Char = {
    var m = 0L
    s.foreach { c =>
      if (c == '*') m = if (m > 0) m - 1 else 0
      else if (c == '#') m <<= 1
      else if (c != '%') m += 1
    }
    if (k0 >= m) return '.'
    var k = k0
    var i = s.length - 1
    while (true) {
      val c = s.charAt(i)
      if (c == '*') m += 1
      else if (c == '#') {
        m /= 2
        if (k >= m) k -= m
      } else if (c == '%') {
        k = m - 1 - k
      } else {
        m -= 1
        if (k == m) return c
      }
      i -= 1
    }
    '.'
  }
}
'''

FILES["3615_longest_palindromic_path_in_graph"] = r'''// LeetCode 3615 - Longest Palindromic Path in Graph
// https://leetcode.com/problems/longest-palindromic-path-in-graph/

object Solution {
  private def pack(a: Int, b: Int): Long =
    (a.toLong << 32) | (b.toLong & 0xffffffffL)

  private def expandPal(g: Array[java.util.List[Integer]], label: String, l: Int, r: Int): Int = {
    val vis = new java.util.HashSet[java.lang.Long]()
    val q = new java.util.ArrayDeque[Array[Int]]()
    val len0 = if (l != r) 2 else 1
    q.offer(Array(l, r, len0))
    var best = len0
    vis.add(pack(math.min(l, r), math.max(l, r)))
    while (!q.isEmpty) {
      val cur = q.poll()
      val itA = g(cur(0)).iterator()
      while (itA.hasNext) {
        val a = itA.next().intValue()
        val itB = g(cur(1)).iterator()
        while (itB.hasNext) {
          val b = itB.next().intValue()
          if (a != b && label.charAt(a) == label.charAt(b)) {
            val p = pack(math.min(a, b), math.max(a, b))
            if (!vis.contains(p)) {
              vis.add(p)
              val nl = cur(2) + 2
              best = math.max(best, nl)
              q.offer(Array(a, b, nl))
            }
          }
        }
      }
    }
    best
  }

  def maxLen(n: Int, edges: Array[Array[Int]], label: String): Int = {
    val g = Array.fill[java.util.List[Integer]](n)(new java.util.ArrayList[Integer]())
    edges.foreach { e =>
      g(e(0)).add(e(1))
      g(e(1)).add(e(0))
    }
    var ans = 1
    var i = 0
    while (i < n) {
      ans = math.max(ans, expandPal(g, label, i, i))
      val it = g(i).iterator()
      while (it.hasNext) {
        val j = it.next().intValue()
        if (i < j && label.charAt(i) == label.charAt(j))
          ans = math.max(ans, expandPal(g, label, i, j))
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3616_number_of_student_replacements"] = r'''// LeetCode 3616 - Number of Student Replacements
// https://leetcode.com/problems/number-of-student-replacements/

object Solution {
  def totalReplacements(ranks: Array[Int]): Int = {
    var ans = 0
    var cur = ranks(0)
    ranks.foreach { x =>
      if (x < cur) {
        cur = x
        ans += 1
      }
    }
    ans
  }
}
'''

FILES["3618_split_array_by_prime_indices"] = r'''// LeetCode 3618 - Split Array by Prime Indices
// https://leetcode.com/problems/split-array-by-prime-indices/

object Solution {
  private val M = 100010
  private var primesCache: Array[Boolean] = null

  private def primes(): Array[Boolean] = {
    if (primesCache == null) {
      primesCache = Array.fill(M)(true)
      primesCache(0) = false
      primesCache(1) = false
      var i = 2
      while (i < M) {
        if (primesCache(i)) {
          var j = i + i
          while (j < M) {
            primesCache(j) = false
            j += i
          }
        }
        i += 1
      }
    }
    primesCache
  }

  def splitArray(nums: Array[Int]): Long = {
    val pr = primes()
    var ans = 0L
    var i = 0
    while (i < nums.length) {
      if (pr(i)) ans += nums(i)
      else ans -= nums(i)
      i += 1
    }
    math.abs(ans)
  }
}
'''

FILES["3619_count_islands_with_total_value_divisible_by_k"] = r'''// LeetCode 3619 - Count Islands With Total Value Divisible by K
// https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

object Solution {
  def countIslands(grid: Array[Array[Int]], k: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    val dirs = Array(-1, 0, 1, 0, -1)
    def dfs(i: Int, j: Int): Long = {
      var s = grid(i)(j).toLong
      grid(i)(j) = 0
      var d = 0
      while (d < 4) {
        val x = i + dirs(d)
        val y = j + dirs(d + 1)
        if (x >= 0 && x < m && y >= 0 && y < n && grid(x)(y) > 0) s += dfs(x, y)
        d += 1
      }
      s
    }
    var ans = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) > 0 && dfs(i, j) % k == 0) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3620_network_recovery_pathways"] = r'''// LeetCode 3620 - Network Recovery Pathways
// https://leetcode.com/problems/network-recovery-pathways/

object Solution {
  def findMaxPathScore(edges: Array[Array[Int]], online: Array[Boolean], k: Long): Int = {
    val n = online.length
    val g = Array.fill[java.util.List[Array[Int]]](n)(new java.util.ArrayList[Array[Int]]())
    var l = Int.MaxValue
    var r = 0
    edges.foreach { e =>
      val u = e(0)
      val v = e(1)
      val w = e(2)
      if (online(u) && online(v)) {
        g(u).add(Array(v, w))
        l = math.min(l, w)
        r = math.max(r, w)
      }
    }
    if (l == Int.MaxValue) return -1

    def check(mid: Int): Boolean = {
      val INF = Int.MaxValue / 2
      val dist = Array.fill(n)(INF)
      dist(0) = 0
      val pq = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
      pq.offer(Array(0, 0))
      while (!pq.isEmpty) {
        val cur = pq.poll()
        val d = cur(0)
        val u = cur(1)
        if (d.toLong > k) return false
        if (u == n - 1) return true
        if (dist(u) >= d) {
          val it = g(u).iterator()
          while (it.hasNext) {
            val e = it.next()
            val v = e(0)
            val w = e(1)
            if (w >= mid) {
              val nd = d + w
              if (nd < dist(v)) {
                dist(v) = nd
                pq.offer(Array(nd, v))
              }
            }
          }
        }
      }
      false
    }

    while (l < r) {
      val mid = (l + r + 1) >> 1
      if (check(mid)) l = mid
      else r = mid - 1
    }
    if (check(l)) l else -1
  }
}
'''

FILES["3621_number_of_integers_with_popcount_depth_equal_to_k_i"] = r'''// LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

object Solution {
  def popcountDepth(n: Long, k: Int): Long = {
    if (k == 0) return if (n >= 1) 1 else 0
    val sb = new StringBuilder
    var x = n
    while (x > 0) {
      sb.append(('0' + (x & 1).toInt).toChar)
      x >>= 1
    }
    var s = sb.reverse().toString
    if (s.isEmpty) s = "0"
    val memo = new java.util.HashMap[String, java.lang.Long]()

    def depth(x0: Int): Int = {
      if (x0 <= 0) return 100
      var x = x0
      var d = 0
      while (x > 1) {
        x = Integer.bitCount(x)
        d += 1
      }
      d
    }

    def dfs(pos: Int, tight: Int, started: Int, pc: Int): Long = {
      if (pos == s.length) {
        if (started == 0) return 0
        if (pc == 1) return if (k == 1) 1 else 0
        return if (depth(pc) == k - 1) 1 else 0
      }
      val key = pos + "," + tight + "," + started + "," + pc
      if (memo.containsKey(key)) return memo.get(key)
      val up = if (tight == 1) s.charAt(pos) - '0' else 1
      var res = 0L
      var dig = 0
      while (dig <= up) {
        val nt = if (tight == 1 && dig == up) 1 else 0
        if (started == 0 && dig == 0) res += dfs(pos + 1, nt, 0, 0)
        else res += dfs(pos + 1, nt, 1, pc + dig)
        dig += 1
      }
      memo.put(key, res)
      res
    }

    dfs(0, 1, 0, 0)
  }
}
'''

FILES["3622_check_divisibility_by_digit_sum_and_product"] = r'''// LeetCode 3622 - Check Divisibility by Digit Sum and Product
// https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

object Solution {
  def checkDivisibility(n: Int): Boolean = {
    var s = 0
    var p = 1
    var x = n
    while (x != 0) {
      val v = x % 10
      x /= 10
      s += v
      p *= v
    }
    n % (s + p) == 0
  }
}
'''

FILES["3623_count_number_of_trapezoids_i"] = r'''// LeetCode 3623 - Count Number of Trapezoids I
// https://leetcode.com/problems/count-number-of-trapezoids-i/

object Solution {
  def countTrapezoids(points: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val cnt = new java.util.HashMap[Integer, Integer]()
    points.foreach { p =>
      cnt.merge(p(1), 1, Integer.sum)
    }
    var ans = 0L
    var pre = 0L
    val it = cnt.values().iterator()
    while (it.hasNext) {
      val c = it.next().intValue()
      val lines = c.toLong * (c - 1) / 2
      ans = (ans + pre * lines) % MOD
      pre = (pre + lines) % MOD
    }
    ans.toInt
  }
}
'''

FILES["3624_number_of_integers_with_popcount_depth_equal_to_k_ii"] = r'''// LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

object Solution {
  private def depth(x0: Long): Int = {
    if (x0 == 1) return 0
    var x = x0
    var d = 0
    while (x > 1) {
      x = java.lang.Long.bitCount(x).toLong
      d += 1
    }
    d
  }

  def popcountDepth(nums: Array[Long], queries: Array[Array[Long]]): Array[Int] = {
    val a = nums.clone()
    val ans = new java.util.ArrayList[Integer]()
    queries.foreach { q =>
      if (q(0) == 1) {
        val l = q(1).toInt
        val r = q(2).toInt
        val k = q(3).toInt
        var cnt = 0
        var i = l
        while (i <= r) {
          if (depth(a(i)) == k) cnt += 1
          i += 1
        }
        ans.add(cnt)
      } else {
        a(q(1).toInt) = q(2)
      }
    }
    val res = new Array[Int](ans.size())
    var i = 0
    while (i < ans.size()) {
      res(i) = ans.get(i)
      i += 1
    }
    res
  }
}
'''

FILES["3625_count_number_of_trapezoids_ii"] = r'''// LeetCode 3625 - Count Number of Trapezoids II
// https://leetcode.com/problems/count-number-of-trapezoids-ii/

object Solution {
  def countTrapezoids(points: Array[Array[Int]]): Int = {
    val n = points.length
    val cnt1 = new java.util.HashMap[java.lang.Double, java.util.Map[java.lang.Double, Integer]]()
    val cnt2 = new java.util.HashMap[Integer, java.util.Map[java.lang.Double, Integer]]()
    var i = 0
    while (i < n) {
      val x1 = points(i)(0)
      val y1 = points(i)(1)
      var j = 0
      while (j < i) {
        val x2 = points(j)(0)
        val y2 = points(j)(1)
        val dx = x2 - x1
        val dy = y2 - y1
        val k: Double = if (dx == 0) 1e9 else dy.toDouble / dx
        val b: Double = if (dx == 0) x1.toDouble else (y1.toLong * dx - x1.toLong * dy).toDouble / dx
        cnt1.computeIfAbsent(k, (_: java.lang.Double) => new java.util.HashMap[java.lang.Double, Integer]()).merge(b, 1, Integer.sum)
        val p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000)
        cnt2.computeIfAbsent(p, (_: Integer) => new java.util.HashMap[java.lang.Double, Integer]()).merge(k, 1, Integer.sum)
        j += 1
      }
      i += 1
    }
    var ans = 0
    val it1 = cnt1.values().iterator()
    while (it1.hasNext) {
      val e = it1.next()
      var s = 0
      val it = e.values().iterator()
      while (it.hasNext) {
        val t = it.next().intValue()
        ans += s * t
        s += t
      }
    }
    val it2 = cnt2.values().iterator()
    while (it2.hasNext) {
      val e = it2.next()
      var s = 0
      val it = e.values().iterator()
      while (it.hasNext) {
        val t = it.next().intValue()
        ans -= s * t
        s += t
      }
    }
    ans
  }
}
'''

FILES["3627_maximum_median_sum_of_subsequences_of_size_3"] = r'''// LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
// https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

object Solution {
  def maximumMedianSum(nums: Array[Int]): Long = {
    java.util.Arrays.sort(nums)
    val n = nums.length
    var ans = 0L
    var i = n / 3
    while (i < n) {
      ans += nums(i)
      i += 2
    }
    ans
  }
}
'''

FILES["3628_maximum_number_of_subsequences_after_one_inserting"] = r'''// LeetCode 3628 - Maximum Number of Subsequences After One Inserting
// https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

object Solution {
  private def calc(s: String, t: String): Long = {
    var cnt = 0L
    var a = 0L
    s.foreach { c =>
      if (c == t.charAt(1)) cnt += a
      if (c == t.charAt(0)) a += 1
    }
    cnt
  }

  def numOfSubsequences(s: String): Long = {
    var l = 0L
    var r = 0L
    s.foreach { c => if (c == 'T') r += 1 }
    var ans = 0L
    var mx = 0L
    s.foreach { c =>
      if (c == 'T') r -= 1
      if (c == 'C') ans += l * r
      if (c == 'L') l += 1
      mx = math.max(mx, l * r)
    }
    mx = math.max(mx, math.max(calc(s, "LC"), calc(s, "CT")))
    ans + mx
  }
}
'''

FILES["3629_minimum_jumps_to_reach_end_via_prime_teleportation"] = r'''// LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
// https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

object Solution {
  private val MX = 1000001
  private var factorsCache: Array[java.util.List[Integer]] = null

  private def factors(): Array[java.util.List[Integer]] = {
    if (factorsCache == null) {
      factorsCache = Array.fill[java.util.List[Integer]](MX)(new java.util.ArrayList[Integer]())
      var i = 2
      while (i < MX) {
        if (factorsCache(i).isEmpty) {
          var j = i
          while (j < MX) {
            factorsCache(j).add(i)
            j += i
          }
        }
        i += 1
      }
    }
    factorsCache
  }

  def minJumps(nums: Array[Int]): Int = {
    val fac = factors()
    val n = nums.length
    val g = new java.util.HashMap[Integer, java.util.List[Integer]]()
    var i = 0
    while (i < n) {
      val it = fac(nums(i)).iterator()
      while (it.hasNext) {
        val p = it.next()
        g.computeIfAbsent(p, (_: Integer) => new java.util.ArrayList[Integer]()).add(i)
      }
      i += 1
    }
    var ans = 0
    val vis = new Array[Boolean](n)
    vis(0) = true
    var q = new java.util.ArrayList[Integer]()
    q.add(0)
    while (true) {
      val nq = new java.util.ArrayList[Integer]()
      val itq = q.iterator()
      while (itq.hasNext) {
        val ii = itq.next().intValue()
        if (ii == n - 1) return ans
        val idx = new java.util.ArrayList[Integer](g.getOrDefault(nums(ii), java.util.List.of[Integer]()))
        idx.add(ii + 1)
        if (ii > 0) idx.add(ii - 1)
        val itj = idx.iterator()
        while (itj.hasNext) {
          val j = itj.next().intValue()
          if (j >= 0 && j < n && !vis(j)) {
            vis(j) = true
            nq.add(j)
          }
        }
        g.put(nums(ii), new java.util.ArrayList[Integer]())
      }
      q = nq
      ans += 1
    }
    -1
  }
}
'''

FILES["3630_partition_array_for_maximum_xor_and_and"] = r'''// LeetCode 3630 - Partition Array for Maximum XOR and AND
// https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/

object Solution {
  def maximizeXorAndXor(nums: Array[Int]): Long = {
    val n = nums.length
    var best = 0L
    var mask = 0
    while (mask < (1 << n)) {
      var andVal = -1
      var xorRest = 0
      var i = 0
      while (i < n) {
        if (((mask >> i) & 1) != 0) {
          andVal = if (andVal < 0) nums(i) else (andVal & nums(i))
        } else {
          xorRest ^= nums(i)
        }
        i += 1
      }
      if (andVal < 0) andVal = 0
      val comp = ((1 << n) - 1) ^ mask
      var sub = comp
      var done = false
      while (!done) {
        var x1 = 0
        i = 0
        while (i < n) {
          if (((sub >> i) & 1) != 0) x1 ^= nums(i)
          i += 1
        }
        val x2 = xorRest ^ x1
        best = math.max(best, andVal.toLong + x1 + x2)
        if (sub == 0) done = true
        else sub = (sub - 1) & comp
      }
      mask += 1
    }
    best
  }
}
'''

FILES["3631_sort_threats_by_severity_and_exploitability"] = r'''// LeetCode 3631 - Sort Threats by Severity and Exploitability
// https://leetcode.com/problems/sort-threats-by-severity-and-exploitability/

object Solution {
  def sortThreats(threats: Array[Array[Int]]): Array[Array[Int]] = {
    java.util.Arrays.sort(threats, (a: Array[Int], b: Array[Int]) => {
      val s1 = 2L * a(1) + a(2)
      val s2 = 2L * b(1) + b(2)
      if (s1 == s2) Integer.compare(a(0), b(0))
      else java.lang.Long.compare(s2, s1)
    })
    threats
  }
}
'''

FILES["3632_subarrays_with_xor_at_least_k"] = r'''// LeetCode 3632 - Subarrays With XOR At Least K
// https://leetcode.com/problems/subarrays-with-xor-at-least-k/

object Solution {
  def subarraysWithXorAtLeastK(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    var ans = 0L
    var i = 0
    while (i < n) {
      var x = 0
      var j = i
      while (j < n) {
        x ^= nums(j)
        if (x >= k) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3633_earliest_finish_time_for_land_and_water_rides_i"] = r'''// LeetCode 3633 - Earliest Finish Time for Land and Water Rides I
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

object Solution {
  private def calc(a1: Array[Int], t1: Array[Int], a2: Array[Int], t2: Array[Int]): Int = {
    var minEnd = Int.MaxValue
    var i = 0
    while (i < a1.length) {
      minEnd = math.min(minEnd, a1(i) + t1(i))
      i += 1
    }
    var ans = Int.MaxValue
    i = 0
    while (i < a2.length) {
      ans = math.min(ans, math.max(minEnd, a2(i)) + t2(i))
      i += 1
    }
    ans
  }

  def earliestFinishTime(landStartTime: Array[Int], landDuration: Array[Int], waterStartTime: Array[Int], waterDuration: Array[Int]): Int = {
    math.min(
      calc(landStartTime, landDuration, waterStartTime, waterDuration),
      calc(waterStartTime, waterDuration, landStartTime, landDuration)
    )
  }
}
'''

FILES["3634_minimum_removals_to_balance_array"] = r'''// LeetCode 3634 - Minimum Removals to Balance Array
// https://leetcode.com/problems/minimum-removals-to-balance-array/

object Solution {
  private def lowerBound(a: Array[Int], target: Long): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) < target) lo = mid + 1
      else hi = mid
    }
    lo
  }

  def minRemoval(nums: Array[Int], k: Int): Int = {
    java.util.Arrays.sort(nums)
    val n = nums.length
    var cnt = 0
    var i = 0
    while (i < n) {
      var j = n
      if (1L * nums(i) * k <= nums(n - 1)) {
        val target = 1L * nums(i) * k + 1
        j = lowerBound(nums, target)
      }
      cnt = math.max(cnt, j - i)
      i += 1
    }
    n - cnt
  }
}
'''

FILES["3635_earliest_finish_time_for_land_and_water_rides_ii"] = r'''// LeetCode 3635 - Earliest Finish Time for Land and Water Rides II
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

object Solution {
  private def calc(a1: Array[Int], t1: Array[Int], a2: Array[Int], t2: Array[Int]): Int = {
    var minEnd = Int.MaxValue
    var i = 0
    while (i < a1.length) {
      minEnd = math.min(minEnd, a1(i) + t1(i))
      i += 1
    }
    var ans = Int.MaxValue
    i = 0
    while (i < a2.length) {
      ans = math.min(ans, math.max(minEnd, a2(i)) + t2(i))
      i += 1
    }
    ans
  }

  def earliestFinishTime(landStartTime: Array[Int], landDuration: Array[Int], waterStartTime: Array[Int], waterDuration: Array[Int]): Int = {
    math.min(
      calc(landStartTime, landDuration, waterStartTime, waterDuration),
      calc(waterStartTime, waterDuration, landStartTime, landDuration)
    )
  }
}
'''

FILES["3636_threshold_majority_queries"] = r'''// LeetCode 3636 - Threshold Majority Queries
// https://leetcode.com/problems/threshold-majority-queries/

object Solution {
  def subarrayMajority(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val ans = new Array[Int](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val l = queries(qi)(0)
      val r = queries(qi)(1)
      val t = queries(qi)(2)
      val cnt = new java.util.HashMap[Integer, Integer]()
      var i = l
      while (i <= r) {
        cnt.merge(nums(i), 1, Integer.sum)
        i += 1
      }
      var best = -1
      var bestC = 0
      val it = cnt.entrySet().iterator()
      while (it.hasNext) {
        val e = it.next()
        val v = e.getKey.intValue()
        val c = e.getValue.intValue()
        if (c >= t && (c > bestC || (c == bestC && (best == -1 || v < best)))) {
          bestC = c
          best = v
        }
      }
      ans(qi) = best
      qi += 1
    }
    ans
  }
}
'''

FILES["3637_trionic_array_i"] = r'''// LeetCode 3637 - Trionic Array I
// https://leetcode.com/problems/trionic-array-i/

object Solution {
  def isTrionic(nums: Array[Int]): Boolean = {
    val n = nums.length
    var p = 0
    while (p < n - 2 && nums(p) < nums(p + 1)) p += 1
    if (p == 0) return false
    var q = p
    while (q < n - 1 && nums(q) > nums(q + 1)) q += 1
    if (q == p || q == n - 1) return false
    while (q < n - 1 && nums(q) < nums(q + 1)) q += 1
    q == n - 1
  }
}
'''

FILES["3638_maximum_balanced_shipments"] = r'''// LeetCode 3638 - Maximum Balanced Shipments
// https://leetcode.com/problems/maximum-balanced-shipments/

object Solution {
  def maxBalancedShipments(weight: Array[Int]): Int = {
    var ans = 0
    var mx = 0
    weight.foreach { x =>
      mx = math.max(mx, x)
      if (x < mx) {
        ans += 1
        mx = 0
      }
    }
    ans
  }
}
'''

FILES["3639_minimum_time_to_activate_string"] = r'''// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

object Solution {
  def minTime(s: String, order: Array[Int], k: Int): Int = {
    val n = s.length
    val total = 1L * n * (n + 1) / 2
    if (k > total) return -1

    def countValid(t: Int): Long = {
      val star = Array.fill(n)(false)
      var i = 0
      while (i <= t) {
        star(order(i)) = true
        i += 1
      }
      var invalid = 0L
      i = 0
      while (i < n) {
        if (star(i)) i += 1
        else {
          var j = i
          while (j < n && !star(j)) j += 1
          val L = (j - i).toLong
          invalid += L * (L + 1) / 2
          i = j
        }
      }
      total - invalid
    }

    var lo = 0
    var hi = n - 1
    var ans = -1
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      if (countValid(mid) >= k) {
        ans = mid
        hi = mid - 1
      } else lo = mid + 1
    }
    ans
  }
}
'''

FILES["3640_trionic_array_ii"] = r'''// LeetCode 3640 - Trionic Array II
// https://leetcode.com/problems/trionic-array-ii/

object Solution {
  def maxSumTrionic(nums: Array[Int]): Long = {
    val n = nums.length
    var i = 0
    var ans = Long.MinValue
    while (i < n) {
      val l = i
      i += 1
      while (i < n && nums(i - 1) < nums(i)) i += 1
      if (i != l + 1) {
        val p = i - 1
        var s = nums(p - 1).toLong + nums(p)
        while (i < n && nums(i - 1) > nums(i)) {
          s += nums(i)
          i += 1
        }
        if (!(i == p + 1 || i == n || nums(i - 1) == nums(i))) {
          val q = i - 1
          s += nums(i)
          i += 1
          var mx = 0L
          var t = 0L
          while (i < n && nums(i - 1) < nums(i)) {
            t += nums(i)
            i += 1
            mx = math.max(mx, t)
          }
          s += mx
          mx = 0
          t = 0
          var j = p - 2
          while (j >= l) {
            t += nums(j)
            mx = math.max(mx, t)
            j -= 1
          }
          s += mx
          ans = math.max(ans, s)
          i = q
        }
      }
    }
    ans
  }
}
'''

FILES["3641_longest_semi_repeating_subarray"] = r'''// LeetCode 3641 - Longest Semi-Repeating Subarray
// https://leetcode.com/problems/longest-semi-repeating-subarray/

object Solution {
  def longestSubarray(nums: Array[Int], k: Int): Int = {
    val cnt = new java.util.HashMap[Integer, Integer]()
    var ans = 0
    var cur = 0
    var l = 0
    var r = 0
    while (r < nums.length) {
      if (cnt.merge(nums(r), 1, Integer.sum) == 2) cur += 1
      while (cur > k) {
        if (cnt.merge(nums(l), -1, Integer.sum) == 1) cur -= 1
        l += 1
      }
      ans = math.max(ans, r - l + 1)
      r += 1
    }
    ans
  }
}
'''

def main():
    written = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "Solution.scala"
        path.write_text(content, encoding="utf-8", newline="\n")
        if path.read_bytes().startswith(b"\xef\xbb\xbf"):
            raise SystemExit(f"BOM in {folder}")
        written += 1
        print(f"wrote {folder}")
    print(f"total {written}")

if __name__ == "__main__":
    main()
