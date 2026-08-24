#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["2962_count_subarrays_where_max_element_appears_at_least_k_times"] = r'''// LeetCode 2962 - Count Subarrays Where Max Element Appears at Least K Times
// https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

object Solution {
  def countSubarrays(nums: Array[Int], k: Int): Long = {
    var mx = nums(0)
    for (v <- nums) if (v > mx) mx = v
    var ans = 0L
    var cnt = 0
    var left = 0
    var right = 0
    while (right < nums.length) {
      if (nums(right) == mx) cnt += 1
      while (cnt >= k) {
        if (nums(left) == mx) cnt -= 1
        left += 1
      }
      ans += left
      right += 1
    }
    ans
  }
}
'''

FILES["2963_count_the_number_of_good_partitions"] = r'''// LeetCode 2963 - Count the Number of Good Partitions
// https://leetcode.com/problems/count-the-number-of-good-partitions/

object Solution {
  def numberOfGoodPartitions(nums: Array[Int]): Int = {
    val mod = 1000000007
    val last = scala.collection.mutable.HashMap[Int, Int]()
    var i = 0
    while (i < nums.length) { last(nums(i)) = i; i += 1 }
    var ans = 1
    var end = 0
    i = 0
    while (i < nums.length) {
      if (last(nums(i)) > end) end = last(nums(i))
      if (i == end && i != nums.length - 1) ans = ((ans * 2L) % mod).toInt
      i += 1
    }
    ans
  }
}
'''

FILES["2964_number_of_divisible_triplet_sums"] = r'''// LeetCode 2964 - Number of Divisible Triplet Sums
// https://leetcode.com/problems/number-of-divisible-triplet-sums/

object Solution {
  def divisibleTripletCount(nums: Array[Int], d: Int): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      val freq = scala.collection.mutable.HashMap[Int, Int]()
      var j = i + 1
      while (j < n) {
        val need = (d - (nums(i) + nums(j)) % d) % d
        ans += freq.getOrElse(need, 0)
        val key = nums(j) % d
        freq(key) = freq.getOrElse(key, 0) + 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["2965_find_missing_and_repeated_values"] = r'''// LeetCode 2965 - Find Missing and Repeated Values
// https://leetcode.com/problems/find-missing-and-repeated-values/

object Solution {
  def findMissingAndRepeatedValues(grid: Array[Array[Int]]): Array[Int] = {
    val n = grid.length
    val freq = Array.ofDim[Int](n * n + 1)
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) { freq(grid(i)(j)) += 1; j += 1 }
      i += 1
    }
    var rep = 0
    var miss = 0
    i = 1
    while (i <= n * n) {
      if (freq(i) == 2) rep = i
      if (freq(i) == 0) miss = i
      i += 1
    }
    Array(rep, miss)
  }
}
'''

FILES["2966_divide_array_into_arrays_with_max_difference"] = r'''// LeetCode 2966 - Divide Array Into Arrays With Max Difference
// https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

object Solution {
  def divideArray(nums: Array[Int], k: Int): Array[Array[Int]] = {
    scala.util.Sorting.quickSort(nums)
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var i = 0
    while (i < nums.length) {
      if (nums(i + 2) - nums(i) > k) return Array.empty[Array[Int]]
      ans += Array(nums(i), nums(i + 1), nums(i + 2))
      i += 3
    }
    ans.toArray
  }
}
'''

FILES["2967_minimum_cost_to_make_array_equalindromic"] = r'''// LeetCode 2967 - Minimum Cost to Make Array Equalindromic
// https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

object Solution {
  private def makePal(x: Int): Int = {
    val ch = x.toString.toCharArray
    var i = 0
    var j = ch.length - 1
    while (i < j) { ch(j) = ch(i); i += 1; j -= 1 }
    new String(ch).toInt
  }

  private def cost(nums: Array[Int], p: Int): Long = {
    var c = 0L
    for (v <- nums) c += math.abs(v.toLong - p)
    c
  }

  def minimumCost(nums: Array[Int]): Long = {
    scala.util.Sorting.quickSort(nums)
    val n = nums.length
    val median = nums(n / 2)
    val candidates = scala.collection.mutable.ArrayBuffer[Int](makePal(median))
    val s = median.toString
    val half = s.substring(0, (s.length + 1) / 2).toInt
    var d = -2
    while (d <= 2) {
      val h = half + d
      if (h > 0) {
        val hs = h.toString
        val pal = if (s.length % 2 == 0) {
          val rb = hs.toCharArray
          var i = 0
          var j = rb.length - 1
          while (i < j) { val tmp = rb(i); rb(i) = rb(j); rb(j) = tmp; i += 1; j -= 1 }
          hs + new String(rb)
        } else {
          val prefix = hs.substring(0, hs.length - 1)
          val rb = prefix.toCharArray
          var i = 0
          var j = rb.length - 1
          while (i < j) { val tmp = rb(i); rb(i) = rb(j); rb(j) = tmp; i += 1; j -= 1 }
          hs + new String(rb)
        }
        try { candidates += pal.toInt } catch { case _: NumberFormatException => () }
      }
      d += 1
    }
    for (v <- Array(1, 9, 11, 99, 101)) candidates += v
    var ans = Long.MaxValue / 4
    for (p <- candidates) if (p > 0) ans = math.min(ans, cost(nums, p))
    ans
  }
}
'''

FILES["2968_apply_operations_to_maximize_frequency_score"] = r'''// LeetCode 2968 - Apply Operations to Maximize Frequency Score
// https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

object Solution {
  private def cost(nums: Array[Int], pref: Array[Long], l: Int, r: Int): Long = {
    val mid = (l + r) / 2
    val left = nums(mid).toLong * (mid - l) - (pref(mid) - pref(l))
    val right = (pref(r + 1) - pref(mid + 1)) - nums(mid).toLong * (r - mid)
    left + right
  }

  def maxFrequencyScore(nums: Array[Int], k: Long): Int = {
    scala.util.Sorting.quickSort(nums)
    val n = nums.length
    val pref = Array.ofDim[Long](n + 1)
    var i = 0
    while (i < n) { pref(i + 1) = pref(i) + nums(i); i += 1 }
    var ans = 1
    var left = 0
    var right = 0
    while (right < n) {
      while (cost(nums, pref, left, right) > k) left += 1
      ans = math.max(ans, right - left + 1)
      right += 1
    }
    ans
  }
}
'''

FILES["2969_minimum_number_of_coins_for_fruits_ii"] = r'''// LeetCode 2969 - Minimum Number of Coins for Fruits II
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/

object Solution {
  def minimumCoins(prices: Array[Int]): Int = {
    val n = prices.length
    val dp = Array.fill(n + 1)(1 << 30)
    dp(0) = 0
    var i = 1
    while (i <= n) {
      var j = i
      while (j <= n && j <= 2 * i) {
        dp(j) = math.min(dp(j), dp(i - 1) + prices(i - 1))
        j += 1
      }
      i += 1
    }
    dp(n)
  }
}
'''

FILES["2970_count_the_number_of_incremovable_subarrays_i"] = r'''// LeetCode 2970 - Count the Number of Incremovable Subarrays I
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

object Solution {
  def incremovableSubarrayCount(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      var j = i
      while (j < n) {
        var prev = -1
        var ok = true
        var t = 0
        while (t < n && ok) {
          if (t < i || t > j) {
            if (nums(t) <= prev) ok = false
            else prev = nums(t)
          }
          t += 1
        }
        if (ok) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["2971_find_polygon_with_the_largest_perimeter"] = r'''// LeetCode 2971 - Find Polygon With the Largest Perimeter
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

object Solution {
  def largestPerimeter(nums: Array[Int]): Long = {
    scala.util.Sorting.quickSort(nums)
    var sum = 0L
    for (v <- nums) sum += v
    var i = nums.length - 1
    while (i >= 2) {
      sum -= nums(i)
      if (sum > nums(i)) return sum + nums(i)
      i -= 1
    }
    -1
  }
}
'''

FILES["2972_count_the_number_of_incremovable_subarrays_ii"] = r'''// LeetCode 2972 - Count the Number of Incremovable Subarrays II
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/

object Solution {
  def incremovableSubarrayCount(nums: Array[Int]): Long = {
    val n = nums.length
    var left = 0
    while (left + 1 < n && nums(left) < nums(left + 1)) left += 1
    if (left == n - 1) return n.toLong * (n + 1) / 2
    var ans = left + 2L
    var right = n - 1
    while (right > 0 && (right == n - 1 || nums(right) < nums(right + 1))) {
      while (left >= 0 && nums(left) >= nums(right)) left -= 1
      ans += left + 2
      right -= 1
      if (right > 0 && nums(right) >= nums(right + 1)) return ans
    }
    ans
  }
}
'''

FILES["2973_find_number_of_coins_to_place_in_tree_nodes"] = r'''// LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
// https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

object Solution {
  def placedCoins(edges: Array[Array[Int]], cost: Array[Int]): Array[Long] = {
    val n = cost.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val ans = Array.ofDim[Long](n)

    def dfs(u: Int, p: Int): scala.collection.mutable.ArrayBuffer[Int] = {
      val vals = scala.collection.mutable.ArrayBuffer[Int](cost(u))
      for (v <- g(u) if v != p) vals ++= dfs(v, u)
      val sorted = vals.sorted
      if (sorted.length < 3) ans(u) = 1
      else {
        val m = sorted.length
        val cand1 = sorted(m - 1).toLong * sorted(m - 2) * sorted(m - 3)
        val cand2 = sorted(0).toLong * sorted(1) * sorted(m - 1)
        var best = math.max(cand1, cand2)
        if (best < 0) best = 0
        ans(u) = best
      }
      if (sorted.length <= 5) sorted
      else scala.collection.mutable.ArrayBuffer(sorted(0), sorted(1), sorted(sorted.length - 3), sorted(sorted.length - 2), sorted(sorted.length - 1))
    }

    dfs(0, -1)
    ans
  }
}
'''

FILES["2974_minimum_number_game"] = r'''// LeetCode 2974 - Minimum Number Game
// https://leetcode.com/problems/minimum-number-game/

object Solution {
  def numberGame(nums: Array[Int]): Array[Int] = {
    scala.util.Sorting.quickSort(nums)
    var i = 0
    while (i + 1 < nums.length) {
      val t = nums(i)
      nums(i) = nums(i + 1)
      nums(i + 1) = t
      i += 2
    }
    nums
  }
}
'''

FILES["2975_maximum_square_area_by_removing_fences_from_a_field"] = r'''// LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

object Solution {
  private def gaps(fences: Array[Int], bound: Int): Set[Int] = {
    val list = scala.collection.mutable.ArrayBuffer[Int](1)
    for (f <- fences) list += f
    list += bound
    val sorted = list.sorted
    val gs = scala.collection.mutable.HashSet[Int]()
    var i = 0
    while (i < sorted.length) {
      var j = i + 1
      while (j < sorted.length) {
        gs += sorted(j) - sorted(i)
        j += 1
      }
      i += 1
    }
    gs.toSet
  }

  def maximizeSquareArea(m: Int, n: Int, hFences: Array[Int], vFences: Array[Int]): Int = {
    val mod = 1000000007
    val hg = gaps(hFences, m)
    val vg = gaps(vFences, n)
    var best = -1L
    for (g <- hg) if (vg.contains(g) && g > best) best = g
    if (best < 0) -1 else ((best * best) % mod).toInt
  }
}
'''

FILES["2976_minimum_cost_to_convert_string_i"] = r'''// LeetCode 2976 - Minimum Cost to Convert String I
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/

object Solution {
  def minimumCost(source: String, target: String, original: Array[Char], changed: Array[Char], cost: Array[Int]): Long = {
    val inf = 1L << 60
    val dist = Array.fill(26, 26)(inf)
    var i = 0
    while (i < 26) { dist(i)(i) = 0; i += 1 }
    i = 0
    while (i < original.length) {
      val u = original(i) - 'a'
      val v = changed(i) - 'a'
      val ww = cost(i).toLong
      if (ww < dist(u)(v)) dist(u)(v) = ww
      i += 1
    }
    var k = 0
    while (k < 26) {
      i = 0
      while (i < 26) {
        var j = 0
        while (j < 26) {
          if (dist(i)(k) + dist(k)(j) < dist(i)(j)) dist(i)(j) = dist(i)(k) + dist(k)(j)
          j += 1
        }
        i += 1
      }
      k += 1
    }
    var ans = 0L
    i = 0
    while (i < source.length) {
      val a = source.charAt(i) - 'a'
      val b = target.charAt(i) - 'a'
      if (dist(a)(b) >= inf / 2) return -1
      ans += dist(a)(b)
      i += 1
    }
    ans
  }
}
'''

FILES["2977_minimum_cost_to_convert_string_ii"] = r'''// LeetCode 2977 - Minimum Cost to Convert String II
// https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

object Solution {
  def minimumCost(source: String, target: String, original: Array[String], changed: Array[String], cost: Array[Int]): Long = {
    val INF = 1L << 60
    val ids = scala.collection.mutable.LinkedHashMap[String, Int]()
    var i = 0
    while (i < original.length) {
      if (!ids.contains(original(i))) ids(original(i)) = ids.size
      if (!ids.contains(changed(i))) ids(changed(i)) = ids.size
      i += 1
    }
    val m = ids.size
    val dist = Array.fill(m, m)(INF)
    i = 0
    while (i < m) { dist(i)(i) = 0; i += 1 }
    i = 0
    while (i < original.length) {
      val u = ids(original(i))
      val v = ids(changed(i))
      val ww = cost(i).toLong
      if (ww < dist(u)(v)) dist(u)(v) = ww
      i += 1
    }
    var k = 0
    while (k < m) {
      i = 0
      while (i < m) {
        var j = 0
        while (j < m) {
          if (dist(i)(k) + dist(k)(j) < dist(i)(j)) dist(i)(j) = dist(i)(k) + dist(k)(j)
          j += 1
        }
        i += 1
      }
      k += 1
    }
    val n = source.length
    val dp = Array.fill(n + 1)(INF)
    dp(0) = 0
    val lens = ids.keys.map(_.length).toSet
    i = 0
    while (i < n) {
      if (dp(i) < INF / 2) {
        if (source.charAt(i) == target.charAt(i) && dp(i) < dp(i + 1)) dp(i + 1) = dp(i)
        for (L <- lens if i + L <= n) {
          val ss = source.substring(i, i + L)
          val tt = target.substring(i, i + L)
          val iu = ids.get(ss)
          val iv = ids.get(tt)
          if (iu.isDefined && iv.isDefined && dist(iu.get)(iv.get) < INF / 2) {
            val cand = dp(i) + dist(iu.get)(iv.get)
            if (cand < dp(i + L)) dp(i + L) = cand
          }
        }
      }
      i += 1
    }
    if (dp(n) >= INF / 2) -1 else dp(n)
  }
}
'''

FILES["2979_most_expensive_item_that_can_not_be_bought"] = r'''// LeetCode 2979 - Most Expensive Item That Can Not Be Bought
// https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/

object Solution {
  def mostExpensiveItem(primeOne: Int, primeTwo: Int): Int =
    primeOne * primeTwo - primeOne - primeTwo
}
'''

FILES["2980_check_if_bitwise_or_has_trailing_zeros"] = r'''// LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
// https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

object Solution {
  def hasTrailingZeros(nums: Array[Int]): Boolean = {
    var even = 0
    for (v <- nums) {
      if (v % 2 == 0) {
        even += 1
        if (even >= 2) return true
      }
    }
    false
  }
}
'''

FILES["2981_find_longest_special_substring_that_occurs_thrice_i"] = r'''// LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

object Solution {
  def maximumLength(s: String): Int = {
    val n = s.length
    var ans = -1
    var i = 0
    while (i < n) {
      var j = i
      var stop = false
      while (j < n && !stop) {
        if (s.charAt(j) != s.charAt(i)) stop = true
        else {
          val len = j - i + 1
          var cnt = 0
          var k = 0
          while (k + len <= n) {
            var ok = true
            var t = 0
            while (t < len && ok) {
              if (s.charAt(k + t) != s.charAt(i + t)) ok = false
              t += 1
            }
            if (ok) cnt += 1
            k += 1
          }
          if (cnt >= 3 && len > ans) ans = len
          j += 1
        }
      }
      i += 1
    }
    ans
  }
}
'''

FILES["2982_find_longest_special_substring_that_occurs_thrice_ii"] = r'''// LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

object Solution {
  def maximumLength(s: String): Int = {
    val groups = Array.fill(26)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val n = s.length
    var i = 0
    while (i < n) {
      var j = i
      while (j < n && s.charAt(j) == s.charAt(i)) j += 1
      groups(s.charAt(i) - 'a') += (j - i)
      i = j
    }
    var ans = -1
    var c = 0
    while (c < 26) {
      val arr = groups(c)
      if (arr.nonEmpty) {
        val sorted = arr.sorted(Ordering[Int].reverse)
        var L = sorted(0)
        var done = false
        while (L >= 1 && !done) {
          var cnt = 0
          for (g <- sorted) if (g >= L) cnt += g - L + 1
          if (cnt >= 3) {
            if (L > ans) ans = L
            done = true
          }
          L -= 1
        }
      }
      c += 1
    }
    ans
  }
}
'''

FILES["2983_palindrome_rearrangement_queries"] = r'''// LeetCode 2983 - Palindrome Rearrangement Queries
// https://leetcode.com/problems/palindrome-rearrangement-queries/

object Solution {
  def canMakePalindromeQueries(s0: String, queries: Array[Array[Int]]): Array[Boolean] = {
    val n = s0.length
    val m = n / 2
    val tArr = s0.substring(m).toCharArray
    var ii = 0
    var jj = tArr.length - 1
    while (ii < jj) { val tmp = tArr(ii); tArr(ii) = tArr(jj); tArr(jj) = tmp; ii += 1; jj -= 1 }
    val t = new String(tArr)
    val s = s0.substring(0, m)
    val pre1 = Array.ofDim[Array[Int]](m + 1)
    val pre2 = Array.ofDim[Array[Int]](m + 1)
    val diff = Array.ofDim[Int](m + 1)
    pre1(0) = Array.ofDim[Int](26)
    pre2(0) = Array.ofDim[Int](26)
    var i = 1
    while (i <= m) {
      pre1(i) = pre1(i - 1).clone()
      pre2(i) = pre2(i - 1).clone()
      pre1(i)(s.charAt(i - 1) - 'a') += 1
      pre2(i)(t.charAt(i - 1) - 'a') += 1
      diff(i) = diff(i - 1) + (if (s.charAt(i - 1) == t.charAt(i - 1)) 0 else 1)
      i += 1
    }

    def count(pre: Array[Array[Int]], a: Int, b: Int): Array[Int] = {
      val cnt = Array.ofDim[Int](26)
      var k = 0
      while (k < 26) { cnt(k) = pre(b + 1)(k) - pre(a)(k); k += 1 }
      cnt
    }
    def sub(cnt1: Array[Int], cnt2: Array[Int]): Array[Int] = {
      val cnt = Array.ofDim[Int](26)
      var i = 0
      while (i < 26) {
        cnt(i) = cnt1(i) - cnt2(i)
        if (cnt(i) < 0) return null
        i += 1
      }
      cnt
    }
    def eq(a: Array[Int], b: Array[Int]): Boolean = {
      var i = 0
      while (i < 26) { if (a(i) != b(i)) return false; i += 1 }
      true
    }
    def check(p1: Array[Array[Int]], p2: Array[Array[Int]], a: Int, b: Int, c: Int, d: Int): Boolean = {
      if (diff(a) > 0 || diff(diff.length - 1) - diff(math.max(b, d) + 1) > 0) return false
      if (d <= b) return eq(count(p1, a, b), count(p2, a, b))
      if (b < c) {
        return diff(c) - diff(b + 1) == 0 && eq(count(p1, a, b), count(p2, a, b)) &&
          eq(count(p1, c, d), count(p2, c, d))
      }
      val cnt1 = sub(count(p1, a, b), count(p2, a, c - 1))
      val cnt2 = sub(count(p2, c, d), count(p1, b + 1, d))
      cnt1 != null && cnt2 != null && eq(cnt1, cnt2)
    }

    val ans = Array.ofDim[Boolean](queries.length)
    i = 0
    while (i < queries.length) {
      val q = queries(i)
      val a = q(0)
      val b = q(1)
      val c = n - 1 - q(3)
      val d = n - 1 - q(2)
      ans(i) = if (a <= c) check(pre1, pre2, a, b, c, d) else check(pre2, pre1, c, d, a, b)
      i += 1
    }
    ans
  }
}
'''

FILES["2992_number_of_self_divisible_permutations"] = r'''// LeetCode 2992 - Number of Self-Divisible Permutations
// https://leetcode.com/problems/number-of-self-divisible-permutations/

object Solution {
  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) { val t = a % b; a = b; b = t }
    a
  }

  def selfDivisiblePermutationCount(n: Int): Int = {
    var ans = 0
    val used = Array.ofDim[Boolean](n + 1)
    def dfs(pos: Int): Unit = {
      if (pos > n) { ans += 1; return }
      var v = 1
      while (v <= n) {
        if (!used(v) && gcd(v, pos) == 1) {
          used(v) = true
          dfs(pos + 1)
          used(v) = false
        }
        v += 1
      }
    }
    dfs(1)
    ans
  }
}
'''

FILES["2996_smallest_missing_integer_greater_than_sequential_prefix_sum"] = r'''// LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
// https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

object Solution {
  def missingInteger(nums: Array[Int]): Int = {
    var sum = nums(0)
    var i = 1
    while (i < nums.length && nums(i) == nums(i - 1) + 1) {
      sum += nums(i)
      i += 1
    }
    val seen = nums.toSet
    while (seen.contains(sum)) sum += 1
    sum
  }
}
'''

FILES["2997_minimum_number_of_operations_to_make_array_xor_equal_to_k"] = r'''// LeetCode 2997 - Minimum Number of Operations to Make Array XOR Equal to K
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Int = {
    var xorr = 0
    for (v <- nums) xorr ^= v
    var diff = xorr ^ k
    var ans = 0
    while (diff > 0) {
      ans += diff & 1
      diff >>= 1
    }
    ans
  }
}
'''

FILES["2998_minimum_number_of_operations_to_make_x_and_y_equal"] = r'''// LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
// https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

object Solution {
  def minimumOperationsToMakeEqual(x: Int, y: Int): Int = {
    if (x <= y) return y - x
    val q = scala.collection.mutable.Queue[(Int, Int)]()
    q.enqueue((x, 0))
    val seen = scala.collection.mutable.HashSet[Int](x)
    while (q.nonEmpty) {
      val (v, d) = q.dequeue()
      if (v == y) return d
      val cands = Array(v + 1, v - 1, if (v % 11 == 0) v / 11 else -1, if (v % 5 == 0) v / 5 else -1)
      for (nxt <- cands) {
        if (nxt > 0 && nxt < 2 * x + 20 && seen.add(nxt)) q.enqueue((nxt, d + 1))
      }
    }
    -1
  }
}
'''

FILES["2999_count_the_number_of_powerful_integers"] = r'''// LeetCode 2999 - Count the Number of Powerful Integers
// https://leetcode.com/problems/count-the-number-of-powerful-integers/

object Solution {
  def numberOfPowerfulInt(start: Long, finish: Long, limit: Int, s: String): Long = {
    def count(num: Long): Long = {
      if (num < 0) return 0
      var i = 0
      while (i < s.length) {
        if (s.charAt(i) - '0' > limit) return 0
        i += 1
      }
      val t = num.toString
      val n = t.length
      val sn = s.length
      if (n < sn) return 0
      var ans = 0L
      var length = sn
      while (length < n) {
        val preLen = length - sn
        if (preLen == 0) ans += 1
        else {
          var ways = limit.toLong
          var j = 1
          while (j < preLen) { ways *= (limit + 1); j += 1 }
          ans += ways
        }
        length += 1
      }
      val pref = n - sn
      val memo = scala.collection.mutable.HashMap[Long, Long]()
      def dfs(i: Int, tight: Boolean): Long = {
        if (i == pref) {
          if (tight) return if (t.substring(pref).compareTo(s) >= 0) 1 else 0
          return 1
        }
        val key = (i.toLong << 1) | (if (tight) 1 else 0)
        if (memo.contains(key)) return memo(key)
        var up = if (tight) t.charAt(i) - '0' else limit
        if (up > limit) up = limit
        var res = 0L
        var d = 0
        while (d <= up) {
          if (!(i == 0 && d == 0)) res += dfs(i + 1, tight && d == (t.charAt(i) - '0'))
          d += 1
        }
        memo(key) = res
        res
      }
      ans += dfs(0, true)
      ans
    }
    count(finish) - count(start - 1)
  }
}
'''

def main():
    n = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "Solution.scala"
        path.write_text(content, encoding="utf-8", newline="\n")
        n += 1
        print("wrote", folder)
    print("total", n)

if __name__ == "__main__":
    main()
