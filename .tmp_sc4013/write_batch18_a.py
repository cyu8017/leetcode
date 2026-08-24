#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3504_longest_palindrome_after_substring_concatenation_ii"] = r'''// LeetCode 3504 - Longest Palindrome After Substring Concatenation II
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/

object Solution {
  def expand(s: String, g: Array[Int], l0: Int, r0: Int): Unit = {
    var l = l0
    var r = r0
    while (l >= 0 && r < s.length && s.charAt(l) == s.charAt(r)) {
      g(l) = math.max(g(l), r - l + 1)
      l -= 1
      r += 1
    }
  }

  def calc(s: String): Array[Int] = {
    val n = s.length
    val g = new Array[Int](n)
    var i = 0
    while (i < n) {
      expand(s, g, i, i)
      expand(s, g, i, i + 1)
      i += 1
    }
    g
  }

  def longestPalindrome(s: String, t0: String): Int = {
    val m = s.length
    val n = t0.length
    val tc = t0.toCharArray
    var _i = 0
    var _j = tc.length - 1
    while (_i < _j) {
      val tmp = tc(_i)
      tc(_i) = tc(_j)
      tc(_j) = tmp
      _i += 1
      _j -= 1
    }
    val t = new String(tc)
    val g1 = calc(s)
    val g2 = calc(t)
    var ans = 0
    for (v <- g1) ans = math.max(ans, v)
    for (v <- g2) ans = math.max(ans, v)
    val f = Array.ofDim[Int](m + 1, n + 1)
    var i = 1
    while (i <= m) {
      var j = 1
      while (j <= n) {
        if (s.charAt(i - 1) == t.charAt(j - 1)) {
          f(i)(j) = f(i - 1)(j - 1) + 1
          val a = if (i < m) g1(i) else 0
          val b = if (j < n) g2(j) else 0
          ans = math.max(ans, f(i)(j) * 2 + a)
          ans = math.max(ans, f(i)(j) * 2 + b)
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3505_minimum_operations_to_make_elements_within_k_subarrays_equal"] = r'''// LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

object Solution {
  def minOperations(nums: Array[Int], x: Int, k: Int): Long = {
    val n = nums.length
    val minOps = new Array[Long](n - x + 1)
    var i = 0
    while (i + x <= n) {
      val w = java.util.Arrays.copyOfRange(nums, i, i + x)
      java.util.Arrays.sort(w)
      val med = w((x - 1) / 2)
      var ops = 0L
      for (v <- w) ops += math.abs(v - med).toLong
      minOps(i) = ops
      i += 1
    }
    val Inf = 1L << 62
    val dp = Array.fill(n + 1, k + 1)(Inf)
    dp(n)(0) = 0
    i = n - 1
    while (i >= 0) {
      var j = 0
      while (j <= k) {
        dp(i)(j) = dp(i + 1)(j)
        if (j > 0 && i + x <= n && minOps(i) + dp(i + x)(j - 1) < dp(i)(j))
          dp(i)(j) = minOps(i) + dp(i + x)(j - 1)
        j += 1
      }
      i -= 1
    }
    dp(0)(k)
  }
}
'''

FILES["3506_find_time_required_to_eliminate_bacterial_strains"] = r'''// LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
// https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

object Solution {
  def minEliminationTime(timeReq: Array[Int], splitTime: Int): Long = {
    val pq = new java.util.PriorityQueue[Integer]()
    for (v <- timeReq) pq.offer(v)
    while (pq.size() > 1) {
      pq.poll()
      val x = pq.poll()
      pq.offer(x + splitTime)
    }
    pq.peek().toLong
  }
}
'''

FILES["3507_minimum_pair_removal_to_sort_array_i"] = r'''// LeetCode 3507 - Minimum Pair Removal to Sort Array I
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

object Solution {
  def isNonDecreasing(a: java.util.List[Integer]): Boolean = {
    var i = 1
    while (i < a.size()) {
      if (a.get(i) < a.get(i - 1)) return false
      i += 1
    }
    true
  }

  def minimumPairRemoval(nums: Array[Int]): Int = {
    val arr = new java.util.ArrayList[Integer]()
    for (x <- nums) arr.add(x)
    var ans = 0
    while (!isNonDecreasing(arr)) {
      var k = 0
      var s = arr.get(0) + arr.get(1)
      var i = 1
      while (i + 1 < arr.size()) {
        val t = arr.get(i) + arr.get(i + 1)
        if (s > t) { s = t; k = i }
        i += 1
      }
      arr.set(k, s)
      arr.remove(k + 1)
      ans += 1
    }
    ans
  }
}
'''

FILES["3508_implement_router"] = r'''// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

class Router(_memoryLimit: Int) {
  private var lim: Int = _memoryLimit
  private val vis = new java.util.HashSet[Long]()
  private val q = new java.util.ArrayDeque[Array[Int]]()
  private val idx = new java.util.HashMap[Integer, Integer]()
  private val d = new java.util.HashMap[Integer, java.util.List[Integer]]()

  private def f(a: Int, b: Int, c: Int): Long =
    (a.toLong << 46) | (b.toLong << 29) | c.toLong

  def addPacket(source: Int, destination: Int, timestamp: Int): Boolean = {
    val x = f(source, destination, timestamp)
    if (vis.contains(x)) return false
    vis.add(x)
    if (q.size() >= lim) forwardPacket()
    q.addLast(Array(source, destination, timestamp))
    d.computeIfAbsent(destination, _ => new java.util.ArrayList[Integer]()).add(timestamp)
    true
  }

  def forwardPacket(): Array[Int] = {
    if (q.isEmpty) return Array.empty[Int]
    val packet = q.pollFirst()
    val s = packet(0)
    val dest = packet(1)
    val t = packet(2)
    vis.remove(f(s, dest, t))
    idx.put(dest, idx.getOrDefault(destinationKey(dest), 0) + 1)
    Array(s, dest, t)
  }

  private def destinationKey(dest: Int): Integer = dest

  def getCount(destination: Int, startTime: Int, endTime: Int): Int = {
    val ls = d.get(destination)
    if (ls == null) return 0
    val k = idx.getOrDefault(destination, 0)
    lowerBound(ls, k, endTime + 1) - lowerBound(ls, k, startTime)
  }

  private def lowerBound(a: java.util.List[Integer], from: Int, target: Int): Int = {
    var lo = from
    var hi = a.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a.get(mid) < target) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
'''

# Fix Router - I used a helper incorrectly. Let me write a cleaner version without destinationKey.
FILES["3508_implement_router"] = r'''// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

class Router(_memoryLimit: Int) {
  private val lim: Int = _memoryLimit
  private val vis = new java.util.HashSet[Long]()
  private val q = new java.util.ArrayDeque[Array[Int]]()
  private val idx = scala.collection.mutable.HashMap.empty[Int, Int]
  private val d = scala.collection.mutable.HashMap.empty[Int, java.util.ArrayList[Integer]]

  private def f(a: Int, b: Int, c: Int): Long =
    (a.toLong << 46) | (b.toLong << 29) | c.toLong

  def addPacket(source: Int, destination: Int, timestamp: Int): Boolean = {
    val x = f(source, destination, timestamp)
    if (vis.contains(x)) return false
    vis.add(x)
    if (q.size() >= lim) forwardPacket()
    q.addLast(Array(source, destination, timestamp))
    if (!d.contains(destination)) d(destination) = new java.util.ArrayList[Integer]()
    d(destination).add(timestamp)
    true
  }

  def forwardPacket(): Array[Int] = {
    if (q.isEmpty) return Array.empty[Int]
    val packet = q.pollFirst()
    val s = packet(0)
    val dest = packet(1)
    val t = packet(2)
    vis.remove(f(s, dest, t))
    idx(dest) = idx.getOrElse(dest, 0) + 1
    Array(s, dest, t)
  }

  def getCount(destination: Int, startTime: Int, endTime: Int): Int = {
    val ls = d.getOrElse(destination, null)
    if (ls == null) return 0
    val k = idx.getOrElse(destination, 0)
    lowerBound(ls, k, endTime + 1) - lowerBound(ls, k, startTime)
  }

  private def lowerBound(a: java.util.ArrayList[Integer], from: Int, target: Int): Int = {
    var lo = from
    var hi = a.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a.get(mid) < target) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
'''

FILES["3509_maximum_product_of_subsequences_with_an_alternating_sum_equal_to_k"] = r'''// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

object Solution {
  val MIN = -5000

  def maxProduct(nums: Array[Int], k: Int, limit: Int): Int = {
    val memo = scala.collection.mutable.HashMap.empty[String, Int]
    var sumAll = 0
    for (v <- nums) sumAll += v
    if (math.abs(k) > sumAll) return -1

    def dp(i: Int, product: Int, state: Int, kk: Int): Int = {
      if (i == nums.length) {
        if (kk == 0 && state != 0 && product <= limit) return product
        return MIN
      }
      val key = i + "," + product + "," + state + "," + kk
      if (memo.contains(key)) return memo(key)
      var res = dp(i + 1, product, state, kk)
      if (state == 0) res = math.max(res, dp(i + 1, nums(i), 1, kk - nums(i)))
      if (state == 1) {
        var np = product * nums(i)
        if (np > limit + 1) np = limit + 1
        res = math.max(res, dp(i + 1, np, 2, kk + nums(i)))
      }
      if (state == 2) {
        var np = product * nums(i)
        if (np > limit + 1) np = limit + 1
        res = math.max(res, dp(i + 1, np, 1, kk - nums(i)))
      }
      memo(key) = res
      res
    }

    val ans = dp(0, 1, 0, k)
    if (ans == MIN) -1 else ans
  }
}
'''

FILES["3510_minimum_pair_removal_to_sort_array_ii"] = r'''// LeetCode 3510 - Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

object Solution {
  def minimumPairRemoval(nums: Array[Int]): Int = {
    val n = nums.length
    var inv = 0
    var ans = 0
    val sl = new java.util.TreeSet[Array[Long]]((a: Array[Long], b: Array[Long]) => {
      if (a(0) != b(0)) java.lang.Long.compare(a(0), b(0)) else java.lang.Long.compare(a(1), b(1))
    })
    val idx = new java.util.TreeSet[Integer]()
    var i = 0
    while (i < n) { idx.add(i); i += 1 }
    i = 0
    while (i < n - 1) {
      if (nums(i) > nums(i + 1)) inv += 1
      sl.add(Array(nums(i).toLong + nums(i + 1), i.toLong))
      i += 1
    }
    while (inv > 0) {
      ans += 1
      val p = sl.pollFirst()
      val s = p(0).toInt
      i = p(1).toInt
      val j = idx.ceiling(i + 1)
      if (nums(i) > nums(j)) inv -= 1
      val h = idx.floor(i - 1)
      if (h != null) {
        if (nums(h) > nums(i)) inv -= 1
        sl.remove(Array(nums(h).toLong + nums(i), h.toLong))
        if (nums(h) > s) inv += 1
        sl.add(Array(nums(h).toLong + s, h.toLong))
      }
      val k = idx.ceiling(j + 1)
      if (k != null) {
        if (nums(j) > nums(k)) inv -= 1
        sl.remove(Array(nums(j).toLong + nums(k), j.toLong))
        if (s > nums(k)) inv += 1
        sl.add(Array(s.toLong + nums(k), i.toLong))
      }
      nums(i) = s
      idx.remove(j)
    }
    ans
  }
}
'''

FILES["3511_make_a_positive_array"] = r'''// LeetCode 3511 - Make a Positive Array
// https://leetcode.com/problems/make-a-positive-array/

object Solution {
  def makeArrayPositive(nums: Array[Int]): Int = {
    var ans = 0
    var l = -1
    var preMx = 0L
    var s = 0L
    var r = 0
    while (r < nums.length) {
      s += nums(r)
      if (r - l > 2 && s <= preMx) {
        ans += 1
        l = r
        preMx = 0
        s = 0
      } else if (r - l >= 2) {
        preMx = math.max(preMx, s - nums(r) - nums(r - 1))
      }
      r += 1
    }
    ans
  }
}
'''

FILES["3512_minimum_operations_to_make_array_sum_divisible_by_k"] = r'''// LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Int = {
    var ans = 0
    for (x <- nums) ans = (ans + x) % k
    ans
  }
}
'''

FILES["3513_number_of_unique_xor_triplets_i"] = r'''// LeetCode 3513 - Number of Unique XOR Triplets I
// https://leetcode.com/problems/number-of-unique-xor-triplets-i/

object Solution {
  def uniqueXorTriplets(nums: Array[Int]): Int = {
    val n = nums.length
    if (n <= 2) return n
    var x = n
    var len = 0
    while (x != 0) { len += 1; x >>= 1 }
    1 << len
  }
}
'''

FILES["3514_number_of_unique_xor_triplets_ii"] = r'''// LeetCode 3514 - Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

object Solution {
  def uniqueXorTriplets(nums: Array[Int]): Int = {
    var mx = 0
    for (v <- nums) mx = math.max(mx, v)
    mx <<= 1
    val st = new Array[Boolean](mx)
    for (a <- nums; b <- nums) st(a ^ b) = true
    val s = new Array[Int](mx)
    var ab = 0
    while (ab < mx) {
      if (st(ab)) for (c <- nums) s(ab ^ c) = 1
      ab += 1
    }
    var ans = 0
    for (v <- s) ans += v
    ans
  }
}
'''

FILES["3515_shortest_path_in_a_weighted_tree"] = r'''// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

object Solution {
  def treeQueries(n: Int, edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val g = Array.fill(n + 1)(new java.util.ArrayList[Array[Int]]())
    val weight = scala.collection.mutable.HashMap.empty[Long, Int]
    for (e <- edges) {
      val u = e(0); val v = e(1); val w = e(2)
      g(u).add(Array(v, w))
      g(v).add(Array(u, w))
      val a = math.min(u, v)
      val b = math.max(u, v)
      weight((a.toLong << 32) | b) = w
    }
    val inT = new Array[Int](n + 1)
    val outT = new Array[Int](n + 1)
    val dist = new Array[Int](n + 1)
    val parent = new Array[Int](n + 1)
    var time = 0

    def dfs(u: Int, p: Int): Unit = {
      inT(u) = time
      time += 1
      val it = g(u).iterator()
      while (it.hasNext) {
        val e = it.next()
        val to = e(0); val w = e(1)
        if (to != p) {
          parent(to) = u
          dist(to) = dist(u) + w
          dfs(to, u)
        }
      }
      outT(u) = time - 1
    }

    dfs(1, 0)
    val bit = new Array[Int](n + 2)

    def add(i0: Int, v: Int): Unit = {
      var i = i0
      while (i <= n) {
        bit(i) += v
        i += i & -i
      }
    }

    def rangeAdd(l: Int, r: Int, v: Int): Unit = {
      add(l + 1, v)
      add(r + 2, -v)
    }

    def point(i0: Int): Int = {
      var s = 0
      var i = i0 + 1
      while (i > 0) {
        s += bit(i)
        i -= i & -i
      }
      s
    }

    var i = 1
    while (i <= n) {
      rangeAdd(inT(i), inT(i), dist(i))
      i += 1
    }
    val ans = new java.util.ArrayList[Integer]()
    for (q <- queries) {
      if (q(0) == 1) {
        val u = q(1); val v = q(2); val nw = q(3)
        val a = math.min(u, v)
        val b = math.max(u, v)
        val key = (a.toLong << 32) | b
        val ow = weight(key)
        val delta = nw - ow
        weight(key) = nw
        val child = if (parent(u) == v) u else v
        rangeAdd(inT(child), outT(child), delta)
      } else {
        ans.add(point(inT(q(1))))
      }
    }
    val out = new Array[Int](ans.size())
    var t = 0
    while (t < ans.size()) { out(t) = ans.get(t); t += 1 }
    out
  }
}
'''

FILES["3516_find_closest_person"] = r'''// LeetCode 3516 - Find Closest Person
// https://leetcode.com/problems/find-closest-person/

object Solution {
  def findClosest(x: Int, y: Int, z: Int): Int = {
    val a = math.abs(x - z)
    val b = math.abs(y - z)
    if (a == b) 0 else if (a < b) 1 else 2
  }
}
'''

FILES["3517_smallest_palindromic_rearrangement_i"] = r'''// LeetCode 3517 - Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

object Solution {
  def smallestPalindrome(s: String): String = {
    val cnt = new Array[Int](26)
    for (c <- s.toCharArray) cnt(c - 'a') += 1
    val t = new StringBuilder
    var ch: Char = 0
    var c = 'a'
    while (c <= 'z') {
      val v = cnt(c - 'a') / 2
      var i = 0
      while (i < v) { t.append(c); i += 1 }
      cnt(c - 'a') -= v * 2
      if (cnt(c - 'a') == 1) ch = c
      c = (c + 1).toChar
    }
    val sb = new StringBuilder(t.toString)
    if (ch != 0) sb.append(ch)
    var i = t.length - 1
    while (i >= 0) { sb.append(t.charAt(i)); i -= 1 }
    sb.toString
  }
}
'''

FILES["3518_smallest_palindromic_rearrangement_ii"] = r'''// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

object Solution {
  val MAX = 1000001

  def nCk(n0: Int, kk0: Int): Int = {
    if (kk0 < 0 || kk0 > n0) return 0
    var res = 1L
    var kk = kk0
    val n = n0
    if (kk > n - kk) kk = n - kk
    var i = 1
    while (i <= kk) {
      res = res * (n - i + 1) / i
      if (res >= MAX) return MAX
      i += 1
    }
    res.toInt
  }

  def countArr(h: Array[Int]): Int = {
    var total = 0
    for (f <- h) total += f
    var res = 1L
    for (f <- h) {
      res *= nCk(total, f)
      if (res >= MAX) return MAX
      total -= f
    }
    res.toInt
  }

  def smallestPalindrome(s: String, k0: Int): String = {
    val cnt = new Array[Int](26)
    for (c <- s.toCharArray) cnt(c - 'a') += 1
    var odd = 0
    for (c <- cnt) if (c % 2 != 0) odd += 1
    if (odd > 1) return ""
    val half = new Array[Int](26)
    var mid: Char = 0
    var i = 0
    while (i < 26) {
      half(i) = cnt(i) / 2
      if (cnt(i) % 2 != 0) mid = ('a' + i).toChar
      i += 1
    }
    var k = k0
    if (countArr(half) < k) return ""
    var halfLen = 0
    for (f <- half) halfLen += f
    val left = new StringBuilder
    var t = 0
    while (t < halfLen) {
      i = 0
      var placed = false
      while (i < 26 && !placed) {
        if (half(i) != 0) {
          half(i) -= 1
          val arr = countArr(half)
          if (arr >= k) {
            left.append(('a' + i).toChar)
            placed = true
          } else {
            k -= arr
            half(i) += 1
          }
        }
        if (!placed) i += 1
      }
      t += 1
    }
    val res = new StringBuilder
    res.append(left)
    if (mid != 0) res.append(mid)
    i = left.length - 1
    while (i >= 0) { res.append(left.charAt(i)); i -= 1 }
    res.toString
  }
}
'''

FILES["3519_count_numbers_with_non_decreasing_digits"] = r'''// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

object Solution {
  val MOD = 1000000007

  def toDigits(s0: String, b: Int): java.util.ArrayList[Integer] = {
    var s = s0
    if (s == "0") {
      val z = new java.util.ArrayList[Integer]()
      z.add(0)
      return z
    }
    val digs = new java.util.ArrayList[Integer]()
    while (!(s.length == 1 && s.charAt(0) == '0')) {
      var rem = 0
      val q = new StringBuilder
      for (c <- s.toCharArray) {
        val cur = rem * 10 + (c - '0')
        val d = cur / b
        rem = cur % b
        if (q.length > 0 || d != 0) q.append(('0' + d).toChar)
      }
      digs.add(rem)
      s = if (q.length == 0) "0" else q.toString
    }
    java.util.Collections.reverse(digs)
    digs
  }

  def dec(s: String): String = {
    val a = s.toCharArray
    var i = a.length - 1
    while (i >= 0 && a(i) == '0') { a(i) = '9'; i -= 1 }
    if (i < 0) return "0"
    a(i) = (a(i) - 1).toChar
    val t = new String(a)
    var p = 0
    while (p + 1 < t.length && t.charAt(p) == '0') p += 1
    t.substring(p)
  }

  def dfs(pos: Int, last: Int, tight: Boolean, digs: java.util.List[Integer], b: Int, m: Int, memo: scala.collection.mutable.HashMap[String, Int]): Int = {
    if (pos == m) return 1
    val key = pos + "," + last + "," + (if (tight) 1 else 0)
    if (memo.contains(key)) return memo(key)
    val up = if (tight) digs.get(pos).intValue() else b - 1
    var res = 0
    var d = last
    while (d <= up) {
      res = (res + dfs(pos + 1, d, tight && d == up, digs, b, m, memo)) % MOD
      d += 1
    }
    memo(key) = res
    res
  }

  def countUpto(digs: java.util.List[Integer], b: Int): Int = {
    val m = digs.size()
    val memo = scala.collection.mutable.HashMap.empty[String, Int]
    dfs(0, 0, true, digs, b, m, memo)
  }

  def countNumbers(l: String, r: String, b: Int): Int = {
    val rd = toDigits(r, b)
    val ld = toDigits(dec(l), b)
    (countUpto(rd, b) - countUpto(ld, b) + MOD) % MOD
  }
}
'''

FILES["3520_minimum_threshold_for_inversion_pairs_count"] = r'''// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

object Solution {
  def upperBound(a: java.util.ArrayList[Integer], target: Int): Int = {
    var lo = 0
    var hi = a.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a.get(mid) <= target) lo = mid + 1
      else hi = mid
    }
    lo
  }

  def countInv(nums: Array[Int], k: Int, threshold: Int): Boolean = {
    val sorted = new java.util.ArrayList[Integer]()
    var inv = 0L
    for (num <- nums) {
      val left = upperBound(sorted, num)
      val right = upperBound(sorted, num + threshold)
      inv += right - left
      sorted.add(upperBound(sorted, num), num)
    }
    inv >= k
  }

  def minThreshold(nums: Array[Int], k: Int): Int = {
    var mx = 0
    for (v <- nums) if (v > mx) mx = v
    var l = 0
    var r = mx + 1
    while (l < r) {
      val m = (l + r) / 2
      if (countInv(nums, k, m)) r = m
      else l = m + 1
    }
    if (l > mx) -1 else l
  }
}
'''

FILES["3522_calculate_score_after_performing_instructions"] = r'''// LeetCode 3522 - Calculate Score After Performing Instructions
// https://leetcode.com/problems/calculate-score-after-performing-instructions/

object Solution {
  def calculateScore(instructions: Array[String], values: Array[Int]): Long = {
    val n = values.length
    val vis = new Array[Boolean](n)
    var ans = 0L
    var i = 0
    while (i >= 0 && i < n && !vis(i)) {
      vis(i) = true
      if (instructions(i).charAt(0) == 'a') {
        ans += values(i)
        i += 1
      } else {
        i += values(i)
      }
    }
    ans
  }
}
'''

FILES["3523_make_array_non_decreasing"] = r'''// LeetCode 3523 - Make Array Non-decreasing
// https://leetcode.com/problems/make-array-non-decreasing/

object Solution {
  def maximumPossibleSize(nums: Array[Int]): Int = {
    var ans = 0
    var mx = 0
    for (x <- nums) {
      if (mx <= x) {
        ans += 1
        mx = x
      }
    }
    ans
  }
}
'''

n = 0
for folder, content in FILES.items():
    p = ROOT / folder / "Solution.scala"
    p.write_text(content, encoding="utf-8")
    n += 1
    print("wrote", folder)
print("TOTAL", n)
