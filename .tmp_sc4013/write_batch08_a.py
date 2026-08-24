#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("2416_sum_of_prefix_scores_of_strings", r'''
// LeetCode 2416 - Sum of Prefix Scores of Strings
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

object Solution {
  private class TrieNode {
    val child = Array.fill[TrieNode](26)(null)
    var cnt = 0
  }

  def sumPrefixScores(words: Array[String]): Array[Int] = {
    val root = new TrieNode()
    words.foreach { w =>
      var cur = root
      var i = 0
      while (i < w.length) {
        val c = w.charAt(i) - 'a'
        if (cur.child(c) == null) cur.child(c) = new TrieNode()
        cur = cur.child(c)
        cur.cnt += 1
        i += 1
      }
    }
    val ans = new Array[Int](words.length)
    var wi = 0
    while (wi < words.length) {
      var cur = root
      var sum = 0
      var i = 0
      val w = words(wi)
      while (i < w.length) {
        cur = cur.child(w.charAt(i) - 'a')
        sum += cur.cnt
        i += 1
      }
      ans(wi) = sum
      wi += 1
    }
    ans
  }
}
''')

w("2417_closest_fair_integer", r'''
// LeetCode 2417 - Closest Fair Integer
// https://leetcode.com/problems/closest-fair-integer/

object Solution {
  def closestFair(n: Int): Int = {
    var x = n
    while (true) {
      val s = x.toString
      if (s.length % 2 != 0) {
        var p = 1
        var i = 0
        while (i < s.length) {
          p *= 10
          i += 1
        }
        return closestFair(p)
      }
      var even = 0
      var odd = 0
      var i = 0
      while (i < s.length) {
        if ((s.charAt(i) - '0') % 2 == 0) even += 1
        else odd += 1
        i += 1
      }
      if (even == odd) return x
      x += 1
    }
    0
  }
}
''')

w("2418_sort_the_people", r'''
// LeetCode 2418 - Sort the People
// https://leetcode.com/problems/sort-the-people/

object Solution {
  def sortPeople(names: Array[String], heights: Array[Int]): Array[String] = {
    val n = names.length
    val idx = Array.tabulate(n)(identity)
    scala.util.Sorting.stableSort(idx, (a: Int, b: Int) => heights(a) > heights(b))
    Array.tabulate(n)(i => names(idx(i)))
  }
}
''')

w("2419_longest_subarray_with_maximum_bitwise_and", r'''
// LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

object Solution {
  def longestSubarray(nums: Array[Int]): Int = {
    var mx = nums(0)
    var i = 1
    while (i < nums.length) {
      if (nums(i) > mx) mx = nums(i)
      i += 1
    }
    var ans = 0
    var cur = 0
    i = 0
    while (i < nums.length) {
      if (nums(i) == mx) {
        cur += 1
        if (cur > ans) ans = cur
      } else {
        cur = 0
      }
      i += 1
    }
    ans
  }
}
''')

w("2420_find_all_good_indices", r'''
// LeetCode 2420 - Find All Good Indices
// https://leetcode.com/problems/find-all-good-indices/

object Solution {
  def goodIndices(nums: Array[Int], k: Int): List[Int] = {
    val n = nums.length
    val dec = new Array[Int](n)
    val inc = new Array[Int](n)
    dec(0) = 1
    var i = 1
    while (i < n) {
      dec(i) = if (nums(i) <= nums(i - 1)) dec(i - 1) + 1 else 1
      i += 1
    }
    inc(n - 1) = 1
    i = n - 2
    while (i >= 0) {
      inc(i) = if (nums(i) <= nums(i + 1)) inc(i + 1) + 1 else 1
      i -= 1
    }
    val ans = scala.collection.mutable.ListBuffer.empty[Int]
    i = k
    while (i < n - k) {
      if (dec(i - 1) >= k && inc(i + 1) >= k) ans += i
      i += 1
    }
    ans.toList
  }
}
''')

w("2421_number_of_good_paths", r'''
// LeetCode 2421 - Number of Good Paths
// https://leetcode.com/problems/number-of-good-paths/

object Solution {
  def numberOfGoodPaths(vals: Array[Int], edges: Array[Array[Int]]): Int = {
    val n = vals.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val parent = Array.tabulate(n)(identity)
    val size = Array.fill(n)(1)

    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }

    val nodes = Array.tabulate(n)(identity)
    scala.util.Sorting.stableSort(nodes, (a: Int, b: Int) => vals(a) < vals(b) || (vals(a) == vals(b) && a < b))
    var ans = n
    var i = 0
    while (i < n) {
      var j = i
      while (j < n && vals(nodes(j)) == vals(nodes(i))) j += 1
      var k = i
      while (k < j) {
        val u = nodes(k)
        g(u).foreach { v =>
          if (vals(v) <= vals(u)) {
            val ru = find(u)
            val rv = find(v)
            if (ru != rv) {
              parent(ru) = rv
              size(rv) += size(ru)
            }
          }
        }
        k += 1
      }
      val freq = scala.collection.mutable.Map.empty[Int, Int]
      k = i
      while (k < j) {
        val r = find(nodes(k))
        freq(r) = freq.getOrElse(r, 0) + 1
        k += 1
      }
      freq.values.foreach { c => ans += c * (c - 1) / 2 }
      i = j
    }
    ans
  }
}
''')

w("2422_merge_operations_to_turn_array_into_a_palindrome", r'''
// LeetCode 2422 - Merge Operations to Turn Array Into a Palindrome
// https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

object Solution {
  def minimumOperations(nums: Array[Int]): Int = {
    var l = 0
    var r = nums.length - 1
    var left = nums(l).toLong
    var right = nums(r).toLong
    var ans = 0
    while (l < r) {
      if (left == right) {
        l += 1
        r -= 1
        if (l < r) {
          left = nums(l)
          right = nums(r)
        }
      } else if (left < right) {
        l += 1
        left += nums(l)
        ans += 1
      } else {
        r -= 1
        right += nums(r)
        ans += 1
      }
    }
    ans
  }
}
''')

w("2423_remove_letter_to_equalize_frequency", r'''
// LeetCode 2423 - Remove Letter To Equalize Frequency
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

object Solution {
  def equalFrequency(word: String): Boolean = {
    var skip = 0
    while (skip < word.length) {
      val cnt = new Array[Int](26)
      var i = 0
      while (i < word.length) {
        if (i != skip) cnt(word.charAt(i) - 'a') += 1
        i += 1
      }
      val freq = scala.collection.mutable.Map.empty[Int, Int]
      i = 0
      while (i < 26) {
        if (cnt(i) > 0) freq(cnt(i)) = freq.getOrElse(cnt(i), 0) + 1
        i += 1
      }
      if (freq.size == 1) return true
      skip += 1
    }
    false
  }
}
''')

w("2424_longest_uploaded_prefix", r'''
// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix(_n: Int) {
  private val uploaded = new Array[Boolean](_n + 2)
  private var prefixLen = 0

  def upload(video: Int): Unit = {
    uploaded(video) = true
    while (uploaded(prefixLen + 1)) prefixLen += 1
  }

  def longest(): Int = prefixLen
}
''')

w("2425_bitwise_xor_of_all_pairings", r'''
// LeetCode 2425 - Bitwise XOR of All Pairings
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

object Solution {
  def xorAllNums(nums1: Array[Int], nums2: Array[Int]): Int = {
    var ans = 0
    if (nums2.length % 2 == 1) {
      var i = 0
      while (i < nums1.length) {
        ans ^= nums1(i)
        i += 1
      }
    }
    if (nums1.length % 2 == 1) {
      var i = 0
      while (i < nums2.length) {
        ans ^= nums2(i)
        i += 1
      }
    }
    ans
  }
}
''')

w("2426_number_of_pairs_satisfying_inequality", r'''
// LeetCode 2426 - Number of Pairs Satisfying Inequality
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

object Solution {
  def numberOfPairs(nums1: Array[Int], nums2: Array[Int], diff: Int): Long = {
    val n = nums1.length
    val arr = Array.tabulate(n)(i => nums1(i) - nums2(i))
    val tmp = new Array[Int](n)

    def mergeCount(l: Int, r: Int): Long = {
      if (r - l <= 1) return 0L
      val m = (l + r) / 2
      var ans = mergeCount(l, m) + mergeCount(m, r)
      var j = m
      var i = l
      while (i < m) {
        while (j < r && arr(j) < arr(i) - diff) j += 1
        ans += r - j
        i += 1
      }
      var p = l
      var q = m
      var i2 = l
      while (p < m && q < r) {
        if (arr(p) <= arr(q)) {
          tmp(i2) = arr(p); p += 1
        } else {
          tmp(i2) = arr(q); q += 1
        }
        i2 += 1
      }
      while (p < m) { tmp(i2) = arr(p); p += 1; i2 += 1 }
      while (q < r) { tmp(i2) = arr(q); q += 1; i2 += 1 }
      var t = l
      while (t < r) { arr(t) = tmp(t); t += 1 }
      ans
    }

    mergeCount(0, n)
  }
}
''')

w("2427_number_of_common_factors", r'''
// LeetCode 2427 - Number of Common Factors
// https://leetcode.com/problems/number-of-common-factors/

object Solution {
  def commonFactors(a: Int, b: Int): Int = {
    def gcd(x: Int, y: Int): Int = {
      var aa = x
      var bb = y
      while (bb != 0) {
        val t = aa % bb
        aa = bb
        bb = t
      }
      aa
    }
    val g = gcd(a, b)
    var ans = 0
    var i = 1
    while (i.toLong * i <= g) {
      if (g % i == 0) {
        ans += 1
        if (i.toLong * i != g) ans += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("2428_maximum_sum_of_an_hourglass", r'''
// LeetCode 2428 - Maximum Sum of an Hourglass
// https://leetcode.com/problems/maximum-sum-of-an-hourglass/

object Solution {
  def maxSum(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var ans = 0
    var i = 0
    while (i + 2 < m) {
      var j = 0
      while (j + 2 < n) {
        val s = grid(i)(j) + grid(i)(j + 1) + grid(i)(j + 2) +
          grid(i + 1)(j + 1) +
          grid(i + 2)(j) + grid(i + 2)(j + 1) + grid(i + 2)(j + 2)
        if (s > ans) ans = s
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("2429_minimize_xor", r'''
// LeetCode 2429 - Minimize XOR
// https://leetcode.com/problems/minimize-xor/

object Solution {
  def minimizeXor(num1: Int, num2: Int): Int = {
    var bits = 0
    var x = num2
    while (x != 0) {
      bits += 1
      x &= x - 1
    }
    var ans = 0
    var i = 31
    while (i >= 0 && bits > 0) {
      if (((num1 >> i) & 1) != 0) {
        ans |= 1 << i
        bits -= 1
      }
      i -= 1
    }
    i = 0
    while (i < 32 && bits > 0) {
      if (((ans >> i) & 1) == 0) {
        ans |= 1 << i
        bits -= 1
      }
      i += 1
    }
    ans
  }
}
''')

w("2430_maximum_deletions_on_a_string", r'''
// LeetCode 2430 - Maximum Deletions on a String
// https://leetcode.com/problems/maximum-deletions-on-a-string/

object Solution {
  def deleteString(s: String): Int = {
    val n = s.length
    val lcp = Array.ofDim[Int](n + 1, n + 1)
    var i = n - 1
    while (i >= 0) {
      var j = n - 1
      while (j >= 0) {
        if (s.charAt(i) == s.charAt(j)) lcp(i)(j) = lcp(i + 1)(j + 1) + 1
        j -= 1
      }
      i -= 1
    }
    val dp = new Array[Int](n)
    i = n - 1
    while (i >= 0) {
      dp(i) = 1
      var len = 1
      while (i + 2 * len <= n) {
        if (lcp(i)(i + len) >= len) {
          val v = 1 + dp(i + len)
          if (v > dp(i)) dp(i) = v
        }
        len += 1
      }
      i -= 1
    }
    dp(0)
  }
}
''')

w("2431_maximize_total_tastiness_of_purchased_fruits", r'''
// LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
// https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

object Solution {
  def maxTastiness(price: Array[Int], tastiness: Array[Int], maxAmount: Int, maxCoupons: Int): Int = {
    val n = price.length
    val dp = Array.fill(maxAmount + 1, maxCoupons + 1)(Int.MinValue / 2)
    dp(0)(0) = 0
    var i = 0
    while (i < n) {
      val p = price(i)
      val t = tastiness(i)
      var a = maxAmount
      while (a >= 0) {
        var c = maxCoupons
        while (c >= 0) {
          if (dp(a)(c) >= 0) {
            if (a + p <= maxAmount) {
              val v = dp(a)(c) + t
              if (v > dp(a + p)(c)) dp(a + p)(c) = v
            }
            if (c + 1 <= maxCoupons && a + p / 2 <= maxAmount) {
              val v = dp(a)(c) + t
              if (v > dp(a + p / 2)(c + 1)) dp(a + p / 2)(c + 1) = v
            }
          }
          c -= 1
        }
        a -= 1
      }
      i += 1
    }
    var ans = 0
    aLoop()
    def aLoop(): Unit = {
      var a = 0
      while (a <= maxAmount) {
        var c = 0
        while (c <= maxCoupons) {
          if (dp(a)(c) > ans) ans = dp(a)(c)
          c += 1
        }
        a += 1
      }
    }
    ans
  }
}
''')

w("2432_the_employee_that_worked_on_the_longest_task", r'''
// LeetCode 2432 - The Employee That Worked on the Longest Task
// https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

object Solution {
  def hardestWorker(n: Int, logs: Array[Array[Int]]): Int = {
    var ans = logs(0)(0)
    var best = logs(0)(1)
    var prev = 0
    var i = 0
    while (i < logs.length) {
      val log = logs(i)
      val dur = log(1) - prev
      if (dur > best || (dur == best && log(0) < ans)) {
        best = dur
        ans = log(0)
      }
      prev = log(1)
      i += 1
    }
    ans
  }
}
''')

w("2433_find_the_original_array_of_prefix_xor", r'''
// LeetCode 2433 - Find The Original Array of Prefix Xor
// https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

object Solution {
  def findArray(pref: Array[Int]): Array[Int] = {
    val ans = new Array[Int](pref.length)
    ans(0) = pref(0)
    var i = 1
    while (i < pref.length) {
      ans(i) = pref(i) ^ pref(i - 1)
      i += 1
    }
    ans
  }
}
''')

w("2434_using_a_robot_to_print_the_lexicographically_smallest_string", r'''
// LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

object Solution {
  def robotWithString(s: String): String = {
    val n = s.length
    val minSuf = new Array[Char](n + 1)
    minSuf(n) = ('z' + 1).toChar
    var i = n - 1
    while (i >= 0) {
      minSuf(i) = if (s.charAt(i) < minSuf(i + 1)) s.charAt(i) else minSuf(i + 1)
      i -= 1
    }
    val stack = new StringBuilder()
    val ans = new StringBuilder()
    i = 0
    while (i < n) {
      stack.append(s.charAt(i))
      while (stack.length > 0 && stack.charAt(stack.length - 1) <= minSuf(i + 1)) {
        ans.append(stack.charAt(stack.length - 1))
        stack.setLength(stack.length - 1)
      }
      i += 1
    }
    while (stack.length > 0) {
      ans.append(stack.charAt(stack.length - 1))
      stack.setLength(stack.length - 1)
    }
    ans.toString
  }
}
''')

w("2435_paths_in_matrix_whose_sum_is_divisible_by_k", r'''
// LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

object Solution {
  def numberOfPaths(grid: Array[Array[Int]], k: Int): Int = {
    val mod = 1000000007
    val m = grid.length
    val n = grid(0).length
    val dp = Array.ofDim[Int](m, n, k)
    dp(0)(0)(grid(0)(0) % k) = 1
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        var r = 0
        while (r < k) {
          if (dp(i)(j)(r) != 0) {
            if (i + 1 < m) {
              val nr = (r + grid(i + 1)(j)) % k
              dp(i + 1)(j)(nr) = (dp(i + 1)(j)(nr) + dp(i)(j)(r)) % mod
            }
            if (j + 1 < n) {
              val nr = (r + grid(i)(j + 1)) % k
              dp(i)(j + 1)(nr) = (dp(i)(j + 1)(nr) + dp(i)(j)(r)) % mod
            }
          }
          r += 1
        }
        j += 1
      }
      i += 1
    }
    dp(m - 1)(n - 1)(0)
  }
}
''')

w("2436_minimum_split_into_subarrays_with_gcd_greater_than_one", r'''
// LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
// https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

object Solution {
  def minimumSplits(nums: Array[Int]): Int = {
    def gcd(x: Int, y: Int): Int = {
      var a = x
      var b = y
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    var ans = 1
    var g = nums(0)
    var i = 1
    while (i < nums.length) {
      val ng = gcd(g, nums(i))
      if (ng == 1) {
        ans += 1
        g = nums(i)
      } else {
        g = ng
      }
      i += 1
    }
    ans
  }
}
''')

w("2437_number_of_valid_clock_times", r'''
// LeetCode 2437 - Number of Valid Clock Times
// https://leetcode.com/problems/number-of-valid-clock-times/

object Solution {
  def countTime(time: String): Int = {
    var ans = 0
    var h = 0
    while (h < 24) {
      var m = 0
      while (m < 60) {
        val h0 = ('0' + h / 10).toChar
        val h1 = ('0' + h % 10).toChar
        val m0 = ('0' + m / 10).toChar
        val m1 = ('0' + m % 10).toChar
        if ((time.charAt(0) == '?' || time.charAt(0) == h0) &&
            (time.charAt(1) == '?' || time.charAt(1) == h1) &&
            (time.charAt(3) == '?' || time.charAt(3) == m0) &&
            (time.charAt(4) == '?' || time.charAt(4) == m1)) {
          ans += 1
        }
        m += 1
      }
      h += 1
    }
    ans
  }
}
''')

w("2438_range_product_queries_of_powers", r'''
// LeetCode 2438 - Range Product Queries of Powers
// https://leetcode.com/problems/range-product-queries-of-powers/

object Solution {
  def productQueries(n: Int, queries: Array[Array[Int]]): Array[Int] = {
    val mod = 1000000007
    val powers = scala.collection.mutable.ArrayBuffer.empty[Int]
    var bit = 0
    while (bit < 31) {
      if (((n >> bit) & 1) != 0) powers += (1 << bit)
      bit += 1
    }
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      var prod = 1L
      var j = queries(i)(0)
      while (j <= queries(i)(1)) {
        prod = prod * powers(j) % mod
        j += 1
      }
      ans(i) = prod.toInt
      i += 1
    }
    ans
  }
}
''')

w("2439_minimize_maximum_of_array", r'''
// LeetCode 2439 - Minimize Maximum of Array
// https://leetcode.com/problems/minimize-maximum-of-array/

object Solution {
  def minimizeArrayValue(nums: Array[Int]): Int = {
    var sum = 0L
    var ans = 0
    var i = 0
    while (i < nums.length) {
      sum += nums(i)
      val avg = ((sum + i) / (i + 1)).toInt
      if (avg > ans) ans = avg
      i += 1
    }
    ans
  }
}
''')

w("2440_create_components_with_same_value", r'''
// LeetCode 2440 - Create Components With Same Value
// https://leetcode.com/problems/create-components-with-same-value/

object Solution {
  def componentValue(nums: Array[Int], edges: Array[Array[Int]]): Int = {
    val n = nums.length
    var total = 0
    var i = 0
    while (i < n) { total += nums(i); i += 1 }
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }

    def dfs(u: Int, p: Int, target: Int): Int = {
      var sum = nums(u)
      g(u).foreach { v =>
        if (v != p) {
          val sub = dfs(v, u, target)
          if (sub < 0) return -1
          sum += sub
        }
      }
      if (sum > target) return -1
      if (sum == target) 0 else sum
    }

    var parts = n
    while (parts >= 1) {
      if (total % parts == 0) {
        val target = total / parts
        if (dfs(0, -1, target) == 0) return parts - 1
      }
      parts -= 1
    }
    0
  }
}
''')
