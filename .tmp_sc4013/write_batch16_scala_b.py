#!/usr/bin/env python3
"""Write Scala Solution.scala files for batch_16 problems 3326-3357."""
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3326_minimum_division_operations_to_make_array_non_decreasing"] = """// LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

object Solution {
  private def smallestProperDivisor(x: Int): Int = {
    var d = 2
    while (d * d <= x) {
      if (x % d == 0) return d
      d += 1
    }
    x
  }

  def minOperations(nums: Array[Int]): Int = {
    var ops = 0
    var i = nums.length - 2
    while (i >= 0) {
      if (nums(i) > nums(i + 1)) {
        while (nums(i) > nums(i + 1)) {
          val d = smallestProperDivisor(nums(i))
          if (d == nums(i)) return -1
          nums(i) /= d
          ops += 1
          if (nums(i) > nums(i + 1) && smallestProperDivisor(nums(i)) == nums(i)) return -1
        }
      }
      i -= 1
    }
    ops
  }
}
"""

FILES["3327_check_if_dfs_strings_are_palindromes"] = """// LeetCode 3327 - Check DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

object Solution {
  def findAnswer(parent: Array[Int], s: String): Array[Boolean] = {
    val n = parent.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 1
    while (i < n) {
      g(parent(i)) += i
      i += 1
    }
    val ans = new Array[Boolean](n)
    def isPal(t: String): Boolean = {
      var a = 0
      var b = t.length - 1
      while (a < b) {
        if (t.charAt(a) != t.charAt(b)) return false
        a += 1
        b -= 1
      }
      true
    }
    def dfsStr(u: Int): String = {
      val out = new StringBuilder
      for (v <- g(u)) out.append(dfsStr(v))
      out.append(s.charAt(u))
      ans(u) = isPal(out.toString)
      out.toString
    }
    dfsStr(0)
    ans
  }
}
"""

FILES["3329_count_substrings_with_k_frequency_characters_ii"] = """// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

object Solution {
  def numberOfSubstrings(s: String, k: Int): Long = {
    val n = s.length
    var ans = 0L
    var i = 0
    while (i < n) {
      val freq = new Array[Int](26)
      var j = i
      var done = false
      while (j < n && !done) {
        freq(s.charAt(j) - 'a') += 1
        var ok = false
        var t = 0
        while (t < 26) {
          if (freq(t) >= k) ok = true
          t += 1
        }
        if (ok) {
          ans += n - j
          done = true
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
"""

FILES["3330_find_the_original_typed_string_i"] = """// LeetCode 3330 - Find the Original Typed String I
// https://leetcode.com/problems/find-the-original-typed-string-i/

object Solution {
  def possibleStringCount(word: String): Int = {
    var ans = 1
    var i = 1
    while (i < word.length) {
      if (word.charAt(i) == word.charAt(i - 1)) ans += 1
      i += 1
    }
    ans
  }
}
"""

FILES["3331_find_subtree_sizes_after_changes"] = """// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

object Solution {
  def findSubtreeSizes(parent: Array[Int], s: String): Array[Int] = {
    val n = parent.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 1
    while (i < n) {
      g(parent(i)) += i
      i += 1
    }
    val newParent = parent.clone()
    val last = Array.fill(26)(-1)
    def dfs1(u: Int): Unit = {
      val c = s.charAt(u) - 'a'
      val prev = last(c)
      if (prev != -1) newParent(u) = prev
      last(c) = u
      for (v <- g(u)) dfs1(v)
      last(c) = prev
    }
    dfs1(0)
    val ng = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    i = 1
    while (i < n) {
      ng(newParent(i)) += i
      i += 1
    }
    val ans = new Array[Int](n)
    def dfs2(u: Int): Int = {
      var sz = 1
      for (v <- ng(u)) sz += dfs2(v)
      ans(u) = sz
      sz
    }
    dfs2(0)
    ans
  }
}
"""

FILES["3332_maximum_points_tourist_can_earn"] = """// LeetCode 3332 - Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/

object Solution {
  def maxScore(n: Int, k: Int, stayScore: Array[Array[Int]], travelScore: Array[Array[Int]]): Int = {
    var dp = new Array[Int](n)
    var day = 0
    while (day < k) {
      val ndp = Array.fill(n)(-(1 << 30))
      var dest = 0
      while (dest < n) {
        var best = -(1 << 30)
        var src = 0
        while (src < n) {
          var v = dp(src)
          if (src == dest) v += stayScore(day)(dest)
          else v += travelScore(src)(dest)
          if (v > best) best = v
          src += 1
        }
        ndp(dest) = best
        dest += 1
      }
      dp = ndp
      day += 1
    }
    var ans = dp(0)
    var i = 1
    while (i < n) {
      if (dp(i) > ans) ans = dp(i)
      i += 1
    }
    ans
  }
}
"""

FILES["3333_find_the_original_typed_string_ii"] = """// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

object Solution {
  def possibleStringCount(word: String, k: Int): Int = {
    val mod = 1000000007
    val groups = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < word.length) {
      var j = i
      while (j < word.length && word.charAt(j) == word.charAt(i)) j += 1
      groups += j - i
      i = j
    }
    var total = 1
    for (g <- groups) total = (total.toLong * g % mod).toInt
    if (k <= groups.length) return total
    val need = k - 1
    var dp = new Array[Int](need)
    dp(0) = 1
    for (g <- groups) {
      val ndp = new Array[Int](need)
      val pref = new Array[Int](need + 1)
      i = 0
      while (i < need) {
        pref(i + 1) = (pref(i) + dp(i)) % mod
        i += 1
      }
      var s = 0
      while (s < need) {
        var lo = s - g
        if (lo < 0) lo = 0
        val hi = s - 1
        if (hi >= 0) ndp(s) = (pref(hi + 1) - pref(lo) + mod) % mod
        s += 1
      }
      dp = ndp
    }
    var bad = 0
    for (v <- dp) bad = (bad + v) % mod
    (total - bad + mod) % mod
  }
}
"""

FILES["3334_find_the_maximum_factor_score_of_array"] = """// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

object Solution {
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
  private def lcm(a: Int, b: Int): Int = a / gcd(a, b) * b

  def maxScore(nums: Array[Int]): Long = {
    val n = nums.length
    var gcdAll = nums(0)
    var lcmAll = nums(0)
    var i = 1
    while (i < n) {
      gcdAll = gcd(gcdAll, nums(i))
      lcmAll = lcm(lcmAll, nums(i))
      i += 1
    }
    var ans = gcdAll.toLong * lcmAll
    var skip = 0
    while (skip < n) {
      var g = 0
      var l = 1
      var first = true
      i = 0
      while (i < n) {
        if (i != skip) {
          if (first) { g = nums(i); l = nums(i); first = false }
          else { g = gcd(g, nums(i)); l = lcm(l, nums(i)) }
        }
        i += 1
      }
      if (!first) {
        val v = g.toLong * l
        if (v > ans) ans = v
      }
      skip += 1
    }
    ans
  }
}
"""

FILES["3335_total_characters_in_string_after_transformations_i"] = """// LeetCode 3335 - Total Characters in String After Transformations I
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

object Solution {
  def lengthAfterTransformations(s: String, t: Int): Int = {
    val mod = 1000000007
    var cnt = new Array[Int](26)
    for (c <- s) cnt(c - 'a') += 1
    var step = 0
    while (step < t) {
      val ncnt = new Array[Int](26)
      var i = 0
      while (i < 25) {
        ncnt(i + 1) = (ncnt(i + 1) + cnt(i)) % mod
        i += 1
      }
      ncnt(0) = (ncnt(0) + cnt(25)) % mod
      ncnt(1) = (ncnt(1) + cnt(25)) % mod
      cnt = ncnt
      step += 1
    }
    var ans = 0
    for (v <- cnt) ans = (ans + v) % mod
    ans
  }
}
"""

FILES["3336_find_the_number_of_subsequences_with_equal_gcd"] = """// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

object Solution {
  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    if (a == 0) return b
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  def subsequencePairCount(nums: Array[Int]): Int = {
    val mod = 1000000007
    var maxV = 0
    for (x <- nums) if (x > maxV) maxV = x
    var dp = Array.ofDim[Int](maxV + 1, maxV + 1)
    dp(0)(0) = 1
    for (x <- nums) {
      val ndp = Array.ofDim[Int](maxV + 1, maxV + 1)
      var a = 0
      while (a <= maxV) {
        Array.copy(dp(a), 0, ndp(a), 0, maxV + 1)
        a += 1
      }
      a = 0
      while (a <= maxV) {
        var b = 0
        while (b <= maxV) {
          if (dp(a)(b) != 0) {
            val na = if (a == 0) x else gcd(a, x)
            val nb = if (b == 0) x else gcd(b, x)
            ndp(na)(b) = (ndp(na)(b) + dp(a)(b)) % mod
            ndp(a)(nb) = (ndp(a)(nb) + dp(a)(b)) % mod
          }
          b += 1
        }
        a += 1
      }
      dp = ndp
    }
    var ans = 0
    var g = 1
    while (g <= maxV) {
      ans = (ans + dp(g)(g)) % mod
      g += 1
    }
    ans
  }
}
"""

FILES["3337_total_characters_in_string_after_transformations_ii"] = """// LeetCode 3337 - Total Characters in String After Transformations II
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

object Solution {
  private def matMul(a: Array[Array[Int]], b: Array[Array[Int]], mod: Int): Array[Array[Int]] = {
    val n = a.length
    val c = Array.ofDim[Int](n, n)
    var i = 0
    while (i < n) {
      var k = 0
      while (k < n) {
        if (a(i)(k) != 0) {
          var j = 0
          while (j < n) {
            c(i)(j) = (c(i)(j) + (a(i)(k).toLong * b(k)(j) % mod).toInt) % mod
            j += 1
          }
        }
        k += 1
      }
      i += 1
    }
    c
  }

  private def matPow(a0: Array[Array[Int]], e0: Int, mod: Int): Array[Array[Int]] = {
    val n = a0.length
    var a = a0
    val r = Array.ofDim[Int](n, n)
    var i = 0
    while (i < n) { r(i)(i) = 1; i += 1 }
    var e = e0
    while (e > 0) {
      if ((e & 1) != 0) {
        val nr = matMul(r, a, mod)
        i = 0
        while (i < n) { Array.copy(nr(i), 0, r(i), 0, n); i += 1 }
      }
      a = matMul(a, a, mod)
      e >>= 1
    }
    r
  }

  def lengthAfterTransformations(s: String, t: Int, nums: Array[Int]): Int = {
    val mod = 1000000007
    var mat = Array.ofDim[Int](26, 26)
    var i = 0
    while (i < 26) {
      var j = 1
      while (j <= nums(i)) {
        mat(i)((i + j) % 26) = 1
        j += 1
      }
      i += 1
    }
    mat = matPow(mat, t, mod)
    val cnt = new Array[Int](26)
    for (c <- s) cnt(c - 'a') += 1
    var ans = 0
    i = 0
    while (i < 26) {
      var j = 0
      while (j < 26) {
        ans = (ans + (cnt(i).toLong * mat(i)(j) % mod).toInt) % mod
        j += 1
      }
      i += 1
    }
    ans
  }
}
"""

FILES["3339_find_the_number_of_k_even_arrays"] = """// LeetCode 3339 - Find the Number of K-Even Arrays
// https://leetcode.com/problems/find-the-number-of-k-even-arrays/

object Solution {
  def countOfArrays(n: Int, m: Int, k: Int): Int = {
    val mod = 1000000007
    val even = m / 2
    val odd = m - even
    val dp = Array.ofDim[Int](n + 1, k + 1, 2)
    dp(1)(0)(0) = odd
    dp(1)(0)(1) = even
    var i = 1
    while (i < n) {
      var j = 0
      while (j <= k) {
        dp(i + 1)(j)(0) = (dp(i + 1)(j)(0) + (((dp(i)(j)(0).toLong + dp(i)(j)(1)) % mod) * odd % mod).toInt) % mod
        dp(i + 1)(j)(1) = (dp(i + 1)(j)(1) + (dp(i)(j)(0).toLong * even % mod).toInt) % mod
        if (j < k) {
          dp(i + 1)(j + 1)(1) = (dp(i + 1)(j + 1)(1) + (dp(i)(j)(1).toLong * even % mod).toInt) % mod
        }
        j += 1
      }
      i += 1
    }
    (dp(n)(k)(0) + dp(n)(k)(1)) % mod
  }
}
"""

FILES["3340_check_balanced_string"] = """// LeetCode 3340 - Check Balanced String
// https://leetcode.com/problems/check-balanced-string/

object Solution {
  def isBalanced(num: String): Boolean = {
    var even = 0
    var odd = 0
    var i = 0
    while (i < num.length) {
      if (i % 2 == 0) even += num.charAt(i) - '0'
      else odd += num.charAt(i) - '0'
      i += 1
    }
    even == odd
  }
}
"""

FILES["3341_find_minimum_time_to_reach_last_room_i"] = """// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

object Solution {
  def minTimeToReach(moveTime: Array[Array[Int]]): Int = {
    val m = moveTime.length
    val n = moveTime(0).length
    val dist = Array.fill(m, n)(1 << 30)
    val h = new java.util.PriorityQueue[Array[Int]]((a, b) => Integer.compare(a(0), b(0)))
    h.offer(Array(0, 0, 0))
    dist(0)(0) = 0
    val dirs = Array(Array(0, 1), Array(1, 0), Array(0, -1), Array(-1, 0))
    while (!h.isEmpty) {
      val cur = h.poll()
      val t = cur(0)
      val r = cur(1)
      val c = cur(2)
      if (t == dist(r)(c)) {
        if (r == m - 1 && c == n - 1) return t
        for (d <- dirs) {
          val nr = r + d(0)
          val nc = c + d(1)
          if (nr >= 0 && nc >= 0 && nr < m && nc < n) {
            val start = math.max(t, moveTime(nr)(nc))
            val nt = start + 1
            if (nt < dist(nr)(nc)) {
              dist(nr)(nc) = nt
              h.offer(Array(nt, nr, nc))
            }
          }
        }
      }
    }
    -1
  }
}
"""

FILES["3342_find_minimum_time_to_reach_last_room_ii"] = """// LeetCode 3342 - Find Minimum Time to Reach Last Room II
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

object Solution {
  def minTimeToReach(moveTime: Array[Array[Int]]): Int = {
    val m = moveTime.length
    val n = moveTime(0).length
    val INF = 1 << 30
    val dist = Array.fill(m, n, 2)(INF)
    val pq = new java.util.PriorityQueue[Array[Int]]((a, b) => Integer.compare(a(0), b(0)))
    dist(0)(0)(0) = 0
    pq.offer(Array(0, 0, 0, 0))
    val dirs = Array(Array(0, 1), Array(1, 0), Array(0, -1), Array(-1, 0))
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val t = cur(0)
      val r = cur(1)
      val c = cur(2)
      val parity = cur(3)
      if (t == dist(r)(c)(parity)) {
        if (r == m - 1 && c == n - 1) return t
        val cost = if (parity == 1) 2 else 1
        for (d <- dirs) {
          val nr = r + d(0)
          val nc = c + d(1)
          if (nr >= 0 && nc >= 0 && nr < m && nc < n) {
            val start = math.max(t, moveTime(nr)(nc))
            val nt = start + cost
            val np = 1 - parity
            if (nt < dist(nr)(nc)(np)) {
              dist(nr)(nc)(np) = nt
              pq.offer(Array(nt, nr, nc, np))
            }
          }
        }
      }
    }
    -1
  }
}
"""

FILES["3343_count_number_of_balanced_permutations"] = """// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

object Solution {
  private def modPow(a0: Long, e0: Long, mod: Int): Int = {
    var r = 1L
    var a = a0 % mod
    var e = e0
    while (e > 0) {
      if ((e & 1) != 0) r = r * a % mod
      a = a * a % mod
      e >>= 1
    }
    r.toInt
  }

  private def key(a: Int, b: Int): Long = (a.toLong << 32) | (b & 0xffffffffL)

  def countBalancedPermutations(num: String): Int = {
    val mod = 1000000007
    val cnt = new Array[Int](10)
    var sum = 0
    for (c <- num) {
      cnt(c - '0') += 1
      sum += c - '0'
    }
    if (sum % 2 == 1) return 0
    val n = num.length
    val halfN = n / 2
    val halfS = sum / 2
    val fact = new Array[Int](n + 1)
    val invF = new Array[Int](n + 1)
    fact(0) = 1
    var i = 1
    while (i <= n) {
      fact(i) = (fact(i - 1).toLong * i % mod).toInt
      i += 1
    }
    invF(n) = modPow(fact(n), mod - 2, mod)
    i = n
    while (i > 0) {
      invF(i - 1) = (invF(i).toLong * i % mod).toInt
      i -= 1
    }
    var dp = scala.collection.mutable.HashMap[Long, Int](key(0, 0) -> 1)
    var d = 0
    while (d <= 9) {
      val ndp = scala.collection.mutable.HashMap.empty[Long, Int]
      for ((st, ways) <- dp) {
        val used = (st >> 32).toInt
        val s = st.toInt
        var take = 0
        while (take <= cnt(d)) {
          val nu = used + take
          val ns = s + take * d
          if (nu <= halfN && ns <= halfS) {
            val w = (ways.toLong * invF(take) % mod * invF(cnt(d) - take) % mod).toInt
            val nk = key(nu, ns)
            ndp(nk) = (ndp.getOrElse(nk, 0) + w) % mod
          }
          take += 1
        }
      }
      dp = ndp
      d += 1
    }
    var ans = dp.getOrElse(key(halfN, halfS), 0)
    ans = (ans.toLong * fact(halfN) % mod * fact(n - halfN) % mod).toInt
    d = 0
    while (d <= 9) {
      ans = (ans.toLong * fact(cnt(d)) % mod).toInt
      d += 1
    }
    ans
  }
}
"""

FILES["3344_maximum_sized_array"] = """// LeetCode 3344 - Maximum Sized Array
// https://leetcode.com/problems/maximum-sized-array/

object Solution {
  private def ok(n: Long, s: Long): Boolean = {
    var sum = 0L
    var i = 0L
    while (i < n) {
      var j = 0L
      while (j < n) {
        val ij = i | j
        sum += ij * (n - 1) * n / 2
        if (sum > s) return false
        j += 1
      }
      i += 1
    }
    sum <= s
  }

  def maxSizedArray(s: Long): Int = {
    var lo = 1L
    var hi = 2000L
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(mid, s)) lo = mid
      else hi = mid - 1
    }
    lo.toInt
  }
}
"""

FILES["3345_smallest_divisible_digit_product_i"] = """// LeetCode 3345 - Smallest Divisible Digit Product I
// https://leetcode.com/problems/smallest-divisible-digit-product-i/

object Solution {
  def smallestNumber(n: Int, t: Int): Int = {
    var x = n
    while (true) {
      var p = 1
      var y = x
      while (y > 0) {
        p *= y % 10
        y /= 10
      }
      if (p % t == 0) return x
      x += 1
    }
    n
  }
}
"""

FILES["3346_maximum_frequency_of_an_element_after_performing_operations_i"] = """// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

object Solution {
  def maxFrequency(nums: Array[Int], k: Int, numOperations: Int): Int = {
    val a = nums.sorted
    val n = a.length
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- a) freq(x) = freq.getOrElse(x, 0) + 1
    var ans = 1
    for ((t, f) <- freq) {
      val lo = lowerBound(a, t - k)
      val hi = upperBound(a, t + k)
      val can = hi - lo
      val use = math.min(can, f + numOperations)
      if (use > ans) ans = use
    }
    var l = 0
    var r = 0
    while (r < n) {
      while (a(r) - a(l) > 2 * k) l += 1
      val window = math.min(r - l + 1, numOperations)
      if (window > ans) ans = window
      r += 1
    }
    ans
  }

  private def lowerBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) < x) lo = mid + 1 else hi = mid
    }
    lo
  }
  private def upperBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) <= x) lo = mid + 1 else hi = mid
    }
    lo
  }
}
"""

FILES["3347_maximum_frequency_of_an_element_after_performing_operations_ii"] = """// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

object Solution {
  def maxFrequency(nums: Array[Int], k: Int, numOperations: Int): Int = {
    val a = nums.sorted
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- a) freq(x) = freq.getOrElse(x, 0) + 1
    var ans = 1
    val candidates = scala.collection.mutable.ArrayBuffer.empty[Int]
    val seen = scala.collection.mutable.HashSet.empty[Int]
    for (x <- a) {
      for (t <- Array(x - k, x, x + k)) {
        if (seen.add(t)) candidates += t
      }
    }
    for (t <- candidates) {
      val lo = lowerBound(a, t - k)
      val hi = upperBound(a, t + k)
      val can = hi - lo
      val f = freq.getOrElse(t, 0)
      val use = math.min(can, f + numOperations)
      if (use > ans) ans = use
    }
    ans
  }

  private def lowerBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) < x) lo = mid + 1 else hi = mid
    }
    lo
  }
  private def upperBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) <= x) lo = mid + 1 else hi = mid
    }
    lo
  }
}
"""

FILES["3348_smallest_divisible_digit_product_ii"] = """// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

object Solution {
  private def dfs(res: Array[Char], i: Int, tight: Boolean, sameLen: Boolean, num: String, t: Long): Boolean = {
    if (i == res.length) {
      var prod = 1L
      for (c <- res) {
        prod *= (c - '0')
        if (prod == 0) return false
      }
      return prod % t == 0 && prod > 0
    }
    var start = if (i == 0) '1' else '0'
    if (tight && sameLen && i < num.length) start = num.charAt(i)
    var c = start
    while (c <= '9') {
      res(i) = c
      val nt = tight && sameLen && i < num.length && c == num.charAt(i)
      if (dfs(res, i + 1, nt, sameLen, num, t)) return true
      c = (c + 1).toChar
    }
    false
  }

  def smallestNumber(num: String, t: Long): String = {
    var tt = t
    var d = 9
    while (d >= 2) {
      while (tt % d == 0) tt /= d
      d -= 1
    }
    if (tt > 1) return "-1"
    var extra = 0
    while (extra <= 60) {
      val L = num.length + extra
      val res = new Array[Char](L)
      if (dfs(res, 0, true, extra == 0, num, t)) return new String(res)
      extra += 1
    }
    "-1"
  }
}
"""

FILES["3349_adjacent_increasing_subarrays_detection_i"] = """// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

object Solution {
  def hasIncreasingSubarrays(nums: Array[Int], k: Int): Boolean = {
    val n = nums.length
    var i = 0
    while (i + 2 * k <= n) {
      if (inc(nums, i, k) && inc(nums, i + k, k)) return true
      i += 1
    }
    false
  }

  private def inc(nums: Array[Int], start: Int, k: Int): Boolean = {
    var i = start
    while (i + 1 < start + k) {
      if (nums(i) >= nums(i + 1)) return false
      i += 1
    }
    true
  }
}
"""

FILES["3350_adjacent_increasing_subarrays_detection_ii"] = """// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

object Solution {
  def maxIncreasingSubarrays(nums: Array[Int]): Int = {
    val n = nums.length
    val up = new Array[Int](n)
    up(n - 1) = 1
    var i = n - 2
    while (i >= 0) {
      up(i) = if (nums(i) < nums(i + 1)) up(i + 1) + 1 else 1
      i -= 1
    }
    var lo = 1
    var hi = n / 2
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(up, n, mid)) lo = mid
      else hi = mid - 1
    }
    lo
  }

  private def ok(up: Array[Int], n: Int, k: Int): Boolean = {
    var i = 0
    while (i + 2 * k <= n) {
      if (up(i) >= k && up(i + k) >= k) return true
      i += 1
    }
    false
  }
}
"""

FILES["3351_sum_of_good_subsequences"] = """// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

object Solution {
  def sumOfGoodSubsequences(nums: Array[Int]): Int = {
    val mod = 1000000007
    val cnt = scala.collection.mutable.HashMap.empty[Int, Int]
    val sum = scala.collection.mutable.HashMap.empty[Int, Int]
    var ans = 0
    for (x <- nums) {
      var c = 1
      var s = x
      if (cnt.getOrElse(x - 1, 0) > 0) {
        c = (c + cnt(x - 1)) % mod
        s = ((s.toLong + sum(x - 1) + cnt(x - 1).toLong * x % mod) % mod).toInt
      }
      if (cnt.getOrElse(x + 1, 0) > 0) {
        c = (c + cnt(x + 1)) % mod
        s = ((s.toLong + sum(x + 1) + cnt(x + 1).toLong * x % mod) % mod).toInt
      }
      cnt(x) = (cnt.getOrElse(x, 0) + c) % mod
      sum(x) = (sum.getOrElse(x, 0) + s) % mod
      ans = (ans + s) % mod
    }
    ans
  }
}
"""

FILES["3352_count_k_reducible_numbers_less_than_n"] = """// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

object Solution {
  private def bitsPop(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x > 0) {
      c += x & 1
      x >>= 1
    }
    c
  }

  def countKReducibleNumbers(s: String, k: Int): Int = {
    val mod = 1000000007
    val red = new Array[Int](801)
    red(1) = 0
    var i = 2
    while (i <= 800) {
      red(i) = 1 + red(bitsPop(i))
      i += 1
    }
    val memo = scala.collection.mutable.HashMap.empty[Long, Int]
    def key(pos: Int, tight: Int, ones: Int): Long =
      (pos.toLong << 32) | (tight.toLong << 16) | ones
    def dfs(pos: Int, tight: Boolean, ones: Int): Int = {
      if (pos == s.length) {
        if (ones == 0) return 0
        return if (red(ones) <= k - 1) 1 else 0
      }
      val ky = key(pos, if (tight) 1 else 0, ones)
      if (memo.contains(ky)) return memo(ky)
      val up = if (tight) s.charAt(pos) - '0' else 1
      var ans = 0
      var d = 0
      while (d <= up) {
        val nt = tight && d == up
        ans = (ans + dfs(pos + 1, nt, ones + d)) % mod
        d += 1
      }
      memo(ky) = ans
      ans
    }
    dfs(0, true, 0)
  }
}
"""

FILES["3353_minimum_total_operations"] = """// LeetCode 3353 - Minimum Total Operations
// https://leetcode.com/problems/minimum-total-operations/

object Solution {
  def minimumOperations(nums: Array[Int]): Int = {
    var ops = 0
    var i = nums.length - 2
    while (i >= 0) {
      if (nums(i) != nums(i + 1)) ops += 1
      i -= 1
    }
    ops
  }
}
"""

FILES["3354_make_array_elements_equal_to_zero"] = """// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

object Solution {
  def countValidSelections(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      if (nums(i) == 0) {
        for (dir <- Array(-1, 1)) {
          val a = nums.clone()
          var cur = i
          var d = dir
          while (cur >= 0 && cur < n) {
            if (a(cur) == 0) cur += d
            else {
              a(cur) -= 1
              d = -d
              cur += d
            }
          }
          var ok = true
          for (v <- a) if (v != 0) ok = false
          if (ok) ans += 1
        }
      }
      i += 1
    }
    ans
  }
}
"""

FILES["3355_zero_array_transformation_i"] = """// LeetCode 3355 - Zero Array Transformation I
// https://leetcode.com/problems/zero-array-transformation-i/

object Solution {
  def isZeroArray(nums: Array[Int], queries: Array[Array[Int]]): Boolean = {
    val n = nums.length
    val diff = new Array[Int](n + 1)
    for (q <- queries) {
      diff(q(0)) += 1
      diff(q(1) + 1) -= 1
    }
    var cur = 0
    var i = 0
    while (i < n) {
      cur += diff(i)
      if (cur < nums(i)) return false
      i += 1
    }
    true
  }
}
"""

FILES["3356_zero_array_transformation_ii"] = """// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

object Solution {
  def minZeroArray(nums: Array[Int], queries: Array[Array[Int]]): Int = {
    val n = nums.length
    if (ok(0, nums, queries, n)) return 0
    var lo = 1
    var hi = queries.length + 1
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (mid <= queries.length && ok(mid, nums, queries, n)) hi = mid
      else lo = mid + 1
    }
    if (lo > queries.length) -1 else lo
  }

  private def ok(k: Int, nums: Array[Int], queries: Array[Array[Int]], n: Int): Boolean = {
    val diff = new Array[Long](n + 1)
    var i = 0
    while (i < k) {
      val q = queries(i)
      diff(q(0)) += q(2)
      diff(q(1) + 1) -= q(2)
      i += 1
    }
    var cur = 0L
    i = 0
    while (i < n) {
      cur += diff(i)
      if (cur < nums(i)) return false
      i += 1
    }
    true
  }
}
"""

FILES["3357_minimize_the_maximum_adjacent_element_difference"] = """// LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

object Solution {
  def minDifference(nums: Array[Int]): Int = {
    val n = nums.length
    var lo = 0
    var hi = 1000000000
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(mid, nums, n)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(d: Int, nums: Array[Int], n: Int): Boolean = {
    var prev = -1
    var i = 0
    while (i < n) {
      if (nums(i) != -1) {
        if (prev != -1 && math.abs(nums(i) - prev) > d) return false
        prev = nums(i)
      } else {
        var j = i
        while (j < n && nums(j) == -1) j += 1
        val left = prev
        val right = if (j < n) nums(j) else -1
        val gap = j - i
        if (left == -1 && right == -1) return true
        if (left != -1 && right != -1) {
          if (math.abs(left - right) > d.toLong * (gap + 1)) return false
        }
        prev = -1
        i = j - 1
      }
      i += 1
    }
    true
  }
}
"""

def main() -> None:
    written = 0
    for folder, text in FILES.items():
        path = ROOT / folder / "Solution.scala"
        path.write_text(text, encoding="utf-8")
        if path.read_bytes().startswith(b"\xef\xbb\xbf"):
            raise SystemExit(f"BOM in {folder}")
        written += 1
        print(f"wrote {folder}")
    print(f"batch B written={written}")

if __name__ == "__main__":
    main()
