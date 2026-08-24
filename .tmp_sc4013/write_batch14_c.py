#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("3114_latest_time_you_can_obtain_after_replacing_characters", r'''
// LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
// https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

object Solution {
  def findLatestTime(s: String): String = {
    var h = 11
    while (true) {
      var m = 59
      while (m >= 0) {
        val t = f"%02d:%02d".format(h, m)
        var ok = true
        var i = 0
        while (i < 5 && ok) {
          if (s.charAt(i) != '?' && s.charAt(i) != t.charAt(i)) ok = false
          i += 1
        }
        if (ok) return t
        m -= 1
      }
      h -= 1
    }
    ""
  }
}
''')

w("3115_maximum_prime_difference", r'''
// LeetCode 3115 - Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/

object Solution {
  def maximumPrimeDifference(nums: Array[Int]): Int = {
    def isPrime(n: Int): Boolean = {
      if (n < 2) return false
      var i = 2
      while (i <= n / i) {
        if (n % i == 0) return false
        i += 1
      }
      true
    }

    var i = 0
    while (true) {
      if (isPrime(nums(i))) {
        var j = nums.length - 1
        while (true) {
          if (isPrime(nums(j))) return j - i
          j -= 1
        }
      }
      i += 1
    }
    0
  }
}
''')

w("3116_kth_smallest_amount_with_single_denomination_combination", r'''
// LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

object Solution {
  def findKthSmallest(coins: Array[Int], k: Int): Long = {
    val r = 100000000000L
    val n = coins.length
    var lo = 1L
    var hi = r
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (check(coins, n, mid, k)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def gcdll(a0: Long, b0: Long): Long = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  private def lcmll(a: Long, b: Long): Long = a / gcdll(a, b) * b

  private def bitCount(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x != 0) {
      c += x & 1
      x >>= 1
    }
    c
  }

  private def check(coins: Array[Int], n: Int, mx: Long, k: Int): Boolean = {
    var cnt = 0L
    var i = 1
    while (i < (1 << n)) {
      var v = 1L
      var j = 0
      while (j < n) {
        if (((i >> j) & 1) != 0) {
          v = lcmll(v, coins(j))
          if (v > mx) j = n
        }
        j += 1
      }
      val m = bitCount(i)
      if (m % 2 == 1) cnt += mx / v
      else cnt -= mx / v
      i += 1
    }
    cnt >= k
  }
}
''')

w("3117_minimum_sum_of_values_by_dividing_array", r'''
// LeetCode 3117 - Minimum Sum of Values by Dividing Array
// https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

object Solution {
  private val INF = 1 << 29

  def minimumValueSum(nums: Array[Int], andValues: Array[Int]): Int = {
    val n = nums.length
    val m = andValues.length
    val f = scala.collection.mutable.Map.empty[Long, Int]

    def dfs(i: Int, j: Int, a0: Int): Int = {
      if (n - i < m - j) return INF
      if (j == m) return if (i == n) 0 else INF
      val a = a0 & nums(i)
      if (a < andValues(j)) return INF
      val key = (i.toLong << 36) | (j.toLong << 32) | (a.toLong & 0xffffffffL)
      f.get(key) match {
        case Some(cached) => cached
        case None =>
          var ans = dfs(i + 1, j, a)
          if (a == andValues(j)) ans = math.min(ans, dfs(i + 1, j + 1, -1) + nums(i))
          f(key) = ans
          ans
      }
    }

    val ans = dfs(0, 0, -1)
    if (ans < INF) ans else -1
  }
}
''')

w("3119_maximum_number_of_potholes_that_can_be_fixed", r'''
// LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
// https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/

object Solution {
  def maxPotholes(road0: String, budget0: Int): Int = {
    val road = road0 + "."
    val n = road.length
    val cnt = new Array[Int](n)
    var k = 0
    var ans = 0
    var i = 0
    while (i < n) {
      val c = road.charAt(i)
      if (c == 'x') k += 1
      else if (k > 0) {
        cnt(k) += 1
        k = 0
      }
      i += 1
    }
    var budget = budget0
    k = n - 1
    while (k > 0 && budget > 0) {
      val t = math.min(budget / (k + 1), cnt(k))
      ans += t * k
      budget -= t * (k + 1)
      cnt(k - 1) += cnt(k) - t
      k -= 1
    }
    ans
  }
}
''')

w("3120_count_the_number_of_special_characters_i", r'''
// LeetCode 3120 - Count the Number of Special Characters I
// https://leetcode.com/problems/count-the-number-of-special-characters-i/

object Solution {
  def numberOfSpecialChars(word: String): Int = {
    val s = new Array[Boolean](128)
    var i = 0
    while (i < word.length) {
      s(word.charAt(i)) = true
      i += 1
    }
    var ans = 0
    i = 0
    while (i < 26) {
      if (s('a' + i) && s('A' + i)) ans += 1
      i += 1
    }
    ans
  }
}
''')

w("3121_count_the_number_of_special_characters_ii", r'''
// LeetCode 3121 - Count the Number of Special Characters II
// https://leetcode.com/problems/count-the-number-of-special-characters-ii/

object Solution {
  def numberOfSpecialChars(word: String): Int = {
    val first = new Array[Int](128)
    val last = new Array[Int](128)
    var i = 0
    while (i < word.length) {
      val c = word.charAt(i)
      if (first(c) == 0) first(c) = i + 1
      last(c) = i + 1
      i += 1
    }
    var ans = 0
    i = 0
    while (i < 26) {
      if (last('a' + i) > 0 && last('a' + i) < first('A' + i)) ans += 1
      i += 1
    }
    ans
  }
}
''')

w("3122_minimum_number_of_operations_to_satisfy_conditions", r'''
// LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
// https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

object Solution {
  def minimumOperations(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val INF = 1 << 29
    val f = Array.fill(n, 10)(INF)
    var i = 0
    while (i < n) {
      val cnt = new Array[Int](10)
      var j = 0
      while (j < m) {
        cnt(grid(j)(i)) += 1
        j += 1
      }
      if (i == 0) {
        j = 0
        while (j < 10) {
          f(i)(j) = m - cnt(j)
          j += 1
        }
      } else {
        j = 0
        while (j < 10) {
          var k = 0
          while (k < 10) {
            if (j != k) f(i)(j) = math.min(f(i)(j), f(i - 1)(k) + m - cnt(j))
            k += 1
          }
          j += 1
        }
      }
      i += 1
    }
    var ans = INF
    var j = 0
    while (j < 10) {
      ans = math.min(ans, f(n - 1)(j))
      j += 1
    }
    ans
  }
}
''')

w("3123_find_edges_in_shortest_paths", r'''
// LeetCode 3123 - Find Edges in Shortest Paths
// https://leetcode.com/problems/find-edges-in-shortest-paths/

object Solution {
  def findAnswer(n: Int, edges: Array[Array[Int]]): Array[Boolean] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Array[Int]])
    var i = 0
    while (i < edges.length) {
      val a = edges(i)(0)
      val b = edges(i)(1)
      val w = edges(i)(2)
      g(a) += Array(b, w, i)
      g(b) += Array(a, w, i)
      i += 1
    }
    val INF = 1 << 30
    val dist = Array.fill(n)(INF)
    dist(0) = 0
    val pq = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) => a(0) - b(0))
    pq.offer(Array(0, 0))
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val da = cur(0)
      val a = cur(1)
      if (da <= dist(a)) {
        g(a).foreach { e =>
          val b = e(0)
          val w = e(1)
          if (dist(b) > dist(a) + w) {
            dist(b) = dist(a) + w
            pq.offer(Array(dist(b), b))
          }
        }
      }
    }
    val ans = new Array[Boolean](edges.length)
    if (dist(n - 1) == INF) return ans
    val q = new java.util.ArrayDeque[Integer]()
    q.offer(n - 1)
    while (!q.isEmpty) {
      val a = q.poll()
      g(a).foreach { e =>
        val b = e(0)
        val w = e(1)
        val ei = e(2)
        if (dist(a) == dist(b) + w) {
          ans(ei) = true
          q.offer(b)
        }
      }
    }
    ans
  }
}
''')

w("3125_maximum_number_that_makes_result_of_bitwise_and_zero", r'''
// LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
// https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/

object Solution {
  def maxNumber(n: Long): Long = {
    val len = 64 - java.lang.Long.numberOfLeadingZeros(n)
    (1L << (len - 1)) - 1
  }
}
''')

w("3127_make_a_square_with_the_same_color", r'''
// LeetCode 3127 - Make a Square with the Same Color
// https://leetcode.com/problems/make-a-square-with-the-same-color/

object Solution {
  def canMakeSquare(grid: Array[Array[Char]]): Boolean = {
    val dirs = Array(0, 0, 1, 1, 0)
    var i = 0
    while (i < 2) {
      var j = 0
      while (j < 2) {
        var cnt1 = 0
        var cnt2 = 0
        var k = 0
        while (k < 4) {
          val x = i + dirs(k)
          val y = j + dirs(k + 1)
          if (grid(x)(y) == 'W') cnt1 += 1
          else cnt2 += 1
          k += 1
        }
        if (cnt1 != cnt2) return true
        j += 1
      }
      i += 1
    }
    false
  }
}
''')

w("3128_right_triangles", r'''
// LeetCode 3128 - Right Triangles
// https://leetcode.com/problems/right-triangles/

object Solution {
  def numberOfRightTriangles(grid: Array[Array[Int]]): Long = {
    val m = grid.length
    val n = grid(0).length
    val rows = new Array[Int](m)
    val cols = new Array[Int](n)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        rows(i) += grid(i)(j)
        cols(j) += grid(i)(j)
        j += 1
      }
      i += 1
    }
    var ans = 0L
    i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 1) ans += (rows(i) - 1).toLong * (cols(j) - 1)
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("3129_find_all_possible_stable_binary_arrays_i", r'''
// LeetCode 3129 - Find All Possible Stable Binary Arrays I
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

object Solution {
  private val MOD = 1000000007

  def numberOfStableArrays(zero: Int, one: Int, limit: Int): Int = {
    val f = Array.fill(zero + 1, one + 1, 2)(-1)

    def dfs(i: Int, j: Int, k: Int): Int = {
      if (i < 0 || j < 0) return 0
      if (i == 0) return if (k == 1 && j <= limit) 1 else 0
      if (j == 0) return if (k == 0 && i <= limit) 1 else 0
      if (f(i)(j)(k) != -1) return f(i)(j)(k)
      val res =
        if (k == 0) (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - dfs(i - limit - 1, j, 1) + MOD) % MOD
        else (dfs(i, j - 1, 0) + dfs(i, j - 1, 1) - dfs(i, j - limit - 1, 0) + MOD) % MOD
      f(i)(j)(k) = res
      res
    }

    (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD
  }
}
''')

w("3130_find_all_possible_stable_binary_arrays_ii", r'''
// LeetCode 3130 - Find All Possible Stable Binary Arrays II
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

object Solution {
  private val MOD = 1000000007

  def numberOfStableArrays(zero: Int, one: Int, limit: Int): Int = {
    val f = Array.fill(zero + 1, one + 1, 2)(-1)

    def dfs(i: Int, j: Int, k: Int): Int = {
      if (i < 0 || j < 0) return 0
      if (i == 0) return if (k == 1 && j <= limit) 1 else 0
      if (j == 0) return if (k == 0 && i <= limit) 1 else 0
      if (f(i)(j)(k) != -1) return f(i)(j)(k)
      val res =
        if (k == 0) (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - dfs(i - limit - 1, j, 1) + MOD) % MOD
        else (dfs(i, j - 1, 0) + dfs(i, j - 1, 1) - dfs(i, j - limit - 1, 0) + MOD) % MOD
      f(i)(j)(k) = res
      res
    }

    (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD
  }
}
''')

w("3131_find_the_integer_added_to_array_i", r'''
// LeetCode 3131 - Find the Integer Added to Array I
// https://leetcode.com/problems/find-the-integer-added-to-array-i/

object Solution {
  def addedInteger(nums1: Array[Int], nums2: Array[Int]): Int = {
    var min1 = nums1(0)
    var min2 = nums2(0)
    nums1.foreach(x => min1 = math.min(min1, x))
    nums2.foreach(x => min2 = math.min(min2, x))
    min2 - min1
  }
}
''')

w("3132_find_the_integer_added_to_array_ii", r'''
// LeetCode 3132 - Find the Integer Added to Array II
// https://leetcode.com/problems/find-the-integer-added-to-array-ii/

object Solution {
  def minimumAddedInteger(nums1: Array[Int], nums2: Array[Int]): Int = {
    val a = nums1.sorted
    val b = nums2.sorted
    var ans = 1 << 30
    var t = 0
    while (t < 3) {
      val x = b(0) - a(t)
      if (ok(a, b, x)) ans = math.min(ans, x)
      t += 1
    }
    ans
  }

  private def ok(nums1: Array[Int], nums2: Array[Int], x: Int): Boolean = {
    var i = 0
    var j = 0
    var cnt = 0
    while (i < nums1.length && j < nums2.length) {
      if (nums2(j) - nums1(i) != x) cnt += 1
      else j += 1
      i += 1
    }
    cnt <= 2
  }
}
''')

w("3133_minimum_array_end", r'''
// LeetCode 3133 - Minimum Array End
// https://leetcode.com/problems/minimum-array-end/

object Solution {
  def minEnd(n0: Int, x: Int): Long = {
    var n = n0 - 1
    var ans = x.toLong
    var i = 0
    while (i < 31) {
      if (((x >> i) & 1) == 0) {
        ans |= (n & 1).toLong << i
        n >>= 1
      }
      i += 1
    }
    ans |= n.toLong << 31
    ans
  }
}
''')

w("3134_find_the_median_of_the_uniqueness_array", r'''
// LeetCode 3134 - Find the Median of the Uniqueness Array
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

object Solution {
  def medianOfUniquenessArray(nums: Array[Int]): Int = {
    val n = nums.length
    val m = (1L + n) * n / 2
    var lo = 1
    var hi = n
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (check(nums, n, m, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def check(nums: Array[Int], n: Int, m: Long, mx: Int): Boolean = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var l = 0
    var k = 0L
    var r = 0
    while (r < n) {
      cnt(nums(r)) = cnt.getOrElse(nums(r), 0) + 1
      while (cnt.size > mx) {
        val y = nums(l)
        l += 1
        val nv = cnt(y) - 1
        if (nv == 0) cnt.remove(y)
        else cnt(y) = nv
      }
      k += r - l + 1
      if (k >= (m + 1) / 2) return true
      r += 1
    }
    false
  }
}
''')

w("3135_equalize_strings_by_adding_or_removing_characters_at_ends", r'''
// LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
// https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

object Solution {
  def minOperations(initial: String, target: String): Int = {
    val m = initial.length
    val n = target.length
    val f = Array.ofDim[Int](m + 1, n + 1)
    var mx = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (initial.charAt(i) == target.charAt(j)) {
          f(i + 1)(j + 1) = f(i)(j) + 1
          mx = math.max(mx, f(i + 1)(j + 1))
        }
        j += 1
      }
      i += 1
    }
    m + n - 2 * mx
  }
}
''')

w("3136_valid_word", r'''
// LeetCode 3136 - Valid Word
// https://leetcode.com/problems/valid-word/

object Solution {
  def isValid(word: String): Boolean = {
    if (word.length < 3) return false
    var hasVowel = false
    var hasConsonant = false
    val vs = new Array[Boolean](26)
    "aeiou".foreach(c => vs(c - 'a') = true)
    var i = 0
    while (i < word.length) {
      val c = word.charAt(i)
      if (Character.isLetter(c)) {
        val lower = Character.toLowerCase(c)
        if (vs(lower - 'a')) hasVowel = true
        else hasConsonant = true
      } else if (!Character.isDigit(c)) {
        return false
      }
      i += 1
    }
    hasVowel && hasConsonant
  }
}
''')

w("3137_minimum_number_of_operations_to_make_word_k_periodic", r'''
// LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
// https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

object Solution {
  def minimumOperationsToMakeKPeriodic(word: String, k: Int): Int = {
    val cnt = scala.collection.mutable.Map.empty[String, Int]
    val n = word.length
    var mx = 0
    var i = 0
    while (i < n) {
      val s = word.substring(i, i + k)
      val v = cnt.getOrElse(s, 0) + 1
      cnt(s) = v
      mx = math.max(mx, v)
      i += k
    }
    n / k - mx
  }
}
''')

w("3138_minimum_length_of_anagram_concatenation", r'''
// LeetCode 3138 - Minimum Length of Anagram Concatenation
// https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

object Solution {
  def minAnagramLength(s: String): Int = {
    val n = s.length
    val cnt = new Array[Int](26)
    var i = 0
    while (i < n) {
      cnt(s.charAt(i) - 'a') += 1
      i += 1
    }
    i = 1
    while (true) {
      if (n % i == 0 && check(s, n, cnt, i)) return i
      i += 1
    }
    n
  }

  private def check(s: String, n: Int, cnt: Array[Int], k: Int): Boolean = {
    var i = 0
    while (i < n) {
      val cnt1 = new Array[Int](26)
      var j = i
      while (j < i + k) {
        cnt1(s.charAt(j) - 'a') += 1
        j += 1
      }
      j = 0
      while (j < 26) {
        if (cnt1(j) * (n / k) != cnt(j)) return false
        j += 1
      }
      i += k
    }
    true
  }
}
''')

w("3139_minimum_cost_to_equalize_array", r'''
// LeetCode 3139 - Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/

object Solution {
  def minCostToEqualizeArray(nums: Array[Int], cost1: Int, cost2: Int): Int = {
    val MOD = 1000000007
    val n = nums.length
    var minNum = nums(0)
    var maxNum = nums(0)
    var sum = 0L
    nums.foreach { v =>
      minNum = math.min(minNum, v)
      maxNum = math.max(maxNum, v)
      sum += v
    }
    if (cost1 * 2L <= cost2 || n < 3) {
      val totalGap = maxNum.toLong * n - sum
      return ((cost1.toLong * totalGap) % MOD).toInt
    }
    var ans = Long.MaxValue
    var target = maxNum
    while (target < 2 * maxNum) {
      val maxGap = target - minNum
      val totalGap = target.toLong * n - sum
      var pairs = totalGap / 2
      val alt = totalGap - maxGap
      if (alt < pairs) pairs = alt
      val cost = cost1.toLong * (totalGap - 2 * pairs) + cost2.toLong * pairs
      ans = math.min(ans, cost)
      target += 1
    }
    (ans % MOD).toInt
  }
}
''')

w("3141_maximum_hamming_distances", r'''
// LeetCode 3141 - Maximum Hamming Distances
// https://leetcode.com/problems/maximum-hamming-distances/

object Solution {
  def maxHammingDistances(nums: Array[Int], m: Int): Array[Int] = {
    val dist = Array.fill(1 << m)(-1)
    var q = scala.collection.mutable.ArrayBuffer.empty[Int]
    nums.foreach { x =>
      dist(x) = 0
      q += x
    }
    var k = 1
    while (q.nonEmpty) {
      val t = scala.collection.mutable.ArrayBuffer.empty[Int]
      q.foreach { x =>
        var i = 0
        while (i < m) {
          val y = x ^ (1 << i)
          if (dist(y) == -1) {
            dist(y) = k
            t += y
          }
          i += 1
        }
      }
      q = t
      k += 1
    }
    var i = 0
    while (i < nums.length) {
      val x = nums(i)
      nums(i) = m - dist(x ^ ((1 << m) - 1))
      i += 1
    }
    nums
  }
}
''')

w("3142_check_if_grid_satisfies_conditions", r'''
// LeetCode 3142 - Check if Grid Satisfies Conditions
// https://leetcode.com/problems/check-if-grid-satisfies-conditions/

object Solution {
  def satisfiesConditions(grid: Array[Array[Int]]): Boolean = {
    val m = grid.length
    val n = grid(0).length
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val x = grid(i)(j)
        if (i + 1 < m && x != grid(i + 1)(j)) return false
        if (j + 1 < n && x == grid(i)(j + 1)) return false
        j += 1
      }
      i += 1
    }
    true
  }
}
''')

w("3143_maximum_points_inside_the_square", r'''
// LeetCode 3143 - Maximum Points Inside the Square
// https://leetcode.com/problems/maximum-points-inside-the-square/

object Solution {
  def maxPointsInsideSquare(points: Array[Array[Int]], s: String): Int = {
    val g = new java.util.TreeMap[Integer, java.util.List[Integer]]()
    var i = 0
    while (i < points.length) {
      val key = math.max(math.max(points(i)(0), -points(i)(0)), math.max(points(i)(1), -points(i)(1)))
      g.computeIfAbsent(key, (_: Integer) => new java.util.ArrayList[Integer]()).add(i)
      i += 1
    }
    val vis = new Array[Boolean](26)
    var ans = 0
    val it = g.entrySet().iterator()
    while (it.hasNext) {
      val e = it.next()
      val vals = e.getValue
      var vi = 0
      while (vi < vals.size()) {
        val idx = vals.get(vi)
        val j = s.charAt(idx) - 'a'
        if (vis(j)) return ans
        vis(j) = true
        vi += 1
      }
      ans += vals.size()
    }
    ans
  }
}
''')
