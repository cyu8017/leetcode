#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["2937_make_three_strings_equal"] = r'''// LeetCode 2937 - Make Three Strings Equal
// https://leetcode.com/problems/make-three-strings-equal/

object Solution {
  def findMinimumOperations(s1: String, s2: String, s3: String): Int = {
    val n = math.min(s1.length, math.min(s2.length, s3.length))
    var i = 0
    while (i < n && s1.charAt(i) == s2.charAt(i) && s2.charAt(i) == s3.charAt(i)) i += 1
    if (i == 0) -1 else s1.length + s2.length + s3.length - 3 * i
  }
}
'''

FILES["2938_separate_black_and_white_balls"] = r'''// LeetCode 2938 - Separate Black and White Balls
// https://leetcode.com/problems/separate-black-and-white-balls/

object Solution {
  def minimumSteps(s: String): Long = {
    var ans = 0L
    var zeros = 0L
    var i = s.length - 1
    while (i >= 0) {
      if (s.charAt(i) == '0') zeros += 1
      else ans += zeros
      i -= 1
    }
    ans
  }
}
'''

FILES["2939_maximum_xor_product"] = r'''// LeetCode 2939 - Maximum Xor Product
// https://leetcode.com/problems/maximum-xor-product/

object Solution {
  def maximumXorProduct(a0: Long, b0: Long, n: Int): Int = {
    val mod = 1000000007
    var a = a0
    var b = b0
    var i = n - 1
    while (i >= 0) {
      val bit = 1L << i
      val abit = a & bit
      val bbit = b & bit
      if (abit == bbit) {
        a |= bit
        b |= bit
      } else if (a > b) {
        b |= bit
        a &= ~bit
      } else {
        a |= bit
        b &= ~bit
      }
      i -= 1
    }
    ((a % mod) * (b % mod) % mod).toInt
  }
}
'''

FILES["2940_find_building_where_alice_and_bob_can_meet"] = r'''// LeetCode 2940 - Find Building Where Alice and Bob Can Meet
// https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

object Solution {
  def leftmostBuildingQueries(heights: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val qn = queries.length
    val ans = Array.fill(qn)(-1)
    val buckets = Array.fill(heights.length)(scala.collection.mutable.ArrayBuffer.empty[Array[Int]])
    var qi = 0
    while (qi < qn) {
      var a = queries(qi)(0)
      var b = queries(qi)(1)
      if (a > b) { val t = a; a = b; b = t }
      if (a == b || heights(a) < heights(b)) ans(qi) = b
      else buckets(b) += Array(heights(a), qi)
      qi += 1
    }
    val st = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var i = heights.length - 1
    while (i >= 0) {
      for (p <- buckets(i)) {
        val h = p(0)
        val qii = p(1)
        var lo = 0
        var hi = st.length - 1
        var pos = -1
        while (lo <= hi) {
          val mid = (lo + hi) / 2
          if (st(mid)(0) > h) {
            pos = st(mid)(1)
            lo = mid + 1
          } else hi = mid - 1
        }
        ans(qii) = pos
      }
      while (st.nonEmpty && st.last(0) <= heights(i)) st.remove(st.length - 1)
      st += Array(heights(i), i)
      i -= 1
    }
    ans
  }
}
'''

FILES["2941_maximum_gcd_sum_of_a_subarray"] = r'''// LeetCode 2941 - Maximum GCD-Sum of a Subarray
// https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

object Solution {
  def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) { val t = a % b; a = b; b = t }
    a
  }

  def maxGcdSum(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val pref = Array.ofDim[Long](n + 1)
    var i = 0
    while (i < n) { pref(i + 1) = pref(i) + nums(i); i += 1 }
    var ans = 0L
    var st = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    i = 0
    while (i < n) {
      val nst = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
      nst += Array(nums(i), i)
      for (p <- st) {
        val g = gcd(p(0), nums(i))
        if (nst.last(0) != g) nst += Array(g, p(1))
      }
      st = nst
      for (p <- st) {
        val g = p(0)
        val idx = p(1)
        if (i - idx + 1 >= k) {
          val cand = (pref(i + 1) - pref(idx)) * g
          if (cand > ans) ans = cand
        }
      }
      i += 1
    }
    ans
  }
}
'''

FILES["2942_find_words_containing_character"] = r'''// LeetCode 2942 - Find Words Containing Character
// https://leetcode.com/problems/find-words-containing-character/

object Solution {
  def findWordsContaining(words: Array[String], x: Char): List[Int] = {
    val ans = scala.collection.mutable.ListBuffer.empty[Int]
    var i = 0
    while (i < words.length) {
      if (words(i).indexOf(x) >= 0) ans += i
      i += 1
    }
    ans.toList
  }
}
'''

FILES["2943_maximize_area_of_square_hole_in_grid"] = r'''// LeetCode 2943 - Maximize Area of Square Hole in Grid
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

object Solution {
  private def maxGap(bars0: Array[Int]): Int = {
    if (bars0.length == 0) return 1
    val bars = bars0.clone()
    scala.util.Sorting.quickSort(bars)
    var best = 1
    var cur = 1
    var i = 1
    while (i < bars.length) {
      if (bars(i) == bars(i - 1) + 1) cur += 1
      else cur = 1
      if (cur > best) best = cur
      i += 1
    }
    best + 1
  }

  def maximizeSquareHoleArea(n: Int, m: Int, hBars: Array[Int], vBars: Array[Int]): Int = {
    var side = maxGap(hBars)
    val vs = maxGap(vBars)
    if (vs < side) side = vs
    side * side
  }
}
'''

FILES["2944_minimum_number_of_coins_for_fruits"] = r'''// LeetCode 2944 - Minimum Number of Coins for Fruits
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

object Solution {
  def minimumCoins(prices: Array[Int]): Int = {
    val n = prices.length
    val dp = Array.fill(n + 1)(1 << 30)
    dp(0) = 0
    var i = 1
    while (i <= n) {
      var j = i
      while (j <= n && j <= i + i) {
        val cand = dp(i - 1) + prices(i - 1)
        if (cand < dp(j)) dp(j) = cand
        j += 1
      }
      i += 1
    }
    dp(n)
  }
}
'''

FILES["2945_find_maximum_non_decreasing_array_length"] = r'''// LeetCode 2945 - Find Maximum Non-decreasing Array Length
// https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

object Solution {
  def findMaximumLength(nums: Array[Int]): Int = {
    val n = nums.length
    val pref = Array.ofDim[Long](n + 1)
    val last = Array.ofDim[Long](n + 1)
    var i = 0
    while (i < n) { pref(i + 1) = pref(i) + nums(i); i += 1 }
    val dp = Array.ofDim[Int](n + 1)
    val dq = scala.collection.mutable.ArrayBuffer[Array[Long]](Array(0L, 0L))
    i = 1
    while (i <= n) {
      while (dq.length > 1 && dq(1)(1) <= pref(i)) dq.remove(0)
      val j = dq(0)(0).toInt
      dp(i) = dp(j) + 1
      last(i) = pref(i) - pref(j)
      val value = pref(i) + last(i)
      while (dq.nonEmpty && dq.last(1) >= value) dq.remove(dq.length - 1)
      dq += Array(i.toLong, value)
      i += 1
    }
    dp(n)
  }
}
'''

FILES["2946_matrix_similarity_after_cyclic_shifts"] = r'''// LeetCode 2946 - Matrix Similarity After Cyclic Shifts
// https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

object Solution {
  def areSimilar(mat: Array[Array[Int]], k: Int): Boolean = {
    val m = mat.length
    val n = mat(0).length
    var i = 0
    while (i < m) {
      var shift = if (i % 2 == 0) {
        val s = n - (k % n)
        if (s == n) 0 else s
      } else k % n
      var j = 0
      while (j < n) {
        if (mat(i)(j) != mat(i)((j + shift) % n)) return false
        j += 1
      }
      i += 1
    }
    true
  }
}
'''

FILES["2947_count_beautiful_substrings_i"] = r'''// LeetCode 2947 - Count Beautiful Substrings I
// https://leetcode.com/problems/count-beautiful-substrings-i/

object Solution {
  private def isVowel(c: Char): Boolean =
    c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'

  def beautifulSubstrings(s: String, k: Int): Int = {
    var ans = 0
    val n = s.length
    var i = 0
    while (i < n) {
      var v = 0
      var c = 0
      var j = i
      while (j < n) {
        if (isVowel(s.charAt(j))) v += 1 else c += 1
        if (v == c && (v * c) % k == 0) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["2948_make_lexicographically_smallest_array_by_swapping_elements"] = r'''// LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
// https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

object Solution {
  def lexicographicallySmallestArray(nums: Array[Int], limit: Int): Array[Int] = {
    val n = nums.length
    val idx = Array.tabulate(n)(identity)
    scala.util.Sorting.stableSort(idx, (a: Int, b: Int) => nums(a) < nums(b) || (nums(a) == nums(b) && a < b))
    val ans = Array.ofDim[Int](n)
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n && nums(idx(j)) - nums(idx(j - 1)) <= limit) j += 1
      val groupIdx = Array.tabulate(j - i)(t => idx(i + t))
      scala.util.Sorting.quickSort(groupIdx)
      var t = 0
      while (t < j - i) {
        ans(groupIdx(t)) = nums(idx(i + t))
        t += 1
      }
      i = j
    }
    ans
  }
}
'''

FILES["2949_count_beautiful_substrings_ii"] = r'''// LeetCode 2949 - Count Beautiful Substrings II
// https://leetcode.com/problems/count-beautiful-substrings-ii/

object Solution {
  private def isVowel(c: Char): Boolean =
    c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'

  def beautifulSubstrings(s: String, k: Int): Long = {
    var x = 1
    while ((x * x) % k != 0) x += 1
    val freq = scala.collection.mutable.HashMap[Long, Int]()
    freq(0L) = 1
    var bal = 0
    var vowels = 0
    var ans = 0L
    var i = 0
    while (i < s.length) {
      val ch = s.charAt(i)
      if (isVowel(ch)) { bal += 1; vowels += 1 } else bal -= 1
      val kk = (bal.toLong << 32) | (vowels % x)
      val f = freq.getOrElse(kk, 0)
      ans += f
      freq(kk) = f + 1
      i += 1
    }
    ans
  }
}
'''

FILES["2950_number_of_divisible_substrings"] = r'''// LeetCode 2950 - Number of Divisible Substrings
// https://leetcode.com/problems/number-of-divisible-substrings/

object Solution {
  def countDivisibleSubstrings(word: String): Int = {
    val vals = Array(1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9)
    var ans = 0
    val n = word.length
    var i = 0
    while (i < n) {
      var sum = 0
      var j = i
      while (j < n) {
        sum += vals(word.charAt(j) - 'a')
        if (sum % (j - i + 1) == 0) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["2951_find_the_peaks"] = r'''// LeetCode 2951 - Find the Peaks
// https://leetcode.com/problems/find-the-peaks/

object Solution {
  def findPeaks(mountain: Array[Int]): List[Int] = {
    val ans = scala.collection.mutable.ListBuffer.empty[Int]
    var i = 1
    while (i + 1 < mountain.length) {
      if (mountain(i) > mountain(i - 1) && mountain(i) > mountain(i + 1)) ans += i
      i += 1
    }
    ans.toList
  }
}
'''

FILES["2952_minimum_number_of_coins_to_be_added"] = r'''// LeetCode 2952 - Minimum Number of Coins to be Added
// https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

object Solution {
  def minimumAddedCoins(coins: Array[Int], target: Int): Int = {
    scala.util.Sorting.quickSort(coins)
    var ans = 0
    var reach = 0
    var i = 0
    while (reach < target) {
      if (i < coins.length && coins(i) <= reach + 1) {
        reach += coins(i)
        i += 1
      } else {
        reach += reach + 1
        ans += 1
      }
    }
    ans
  }
}
'''

FILES["2953_count_complete_substrings"] = r'''// LeetCode 2953 - Count Complete Substrings
// https://leetcode.com/problems/count-complete-substrings/

object Solution {
  def countCompleteSubstrings(word: String, k: Int): Int = {
    val n = word.length
    var ans = 0
    var i = 0
    while (i < n) {
      var j = i
      while (j + 1 < n && math.abs(word.charAt(j + 1) - word.charAt(j)) <= 2) j += 1
      val seg = word.substring(i, j + 1)
      val m = seg.length
      var chars = 1
      var stop = false
      while (chars <= 26 && !stop) {
        val length = chars * k
        if (length > m) stop = true
        else {
          val freq = Array.ofDim[Int](26)
          var unique = 0
          var r = 0
          while (r < m) {
            val c = seg.charAt(r) - 'a'
            freq(c) += 1
            if (freq(c) == 1) unique += 1
            if (r >= length) {
              val c2 = seg.charAt(r - length) - 'a'
              freq(c2) -= 1
              if (freq(c2) == 0) unique -= 1
            }
            if (r >= length - 1 && unique == chars) {
              var ok = true
              var fi = 0
              while (fi < 26 && ok) {
                if (freq(fi) != 0 && freq(fi) != k) ok = false
                fi += 1
              }
              if (ok) ans += 1
            }
            r += 1
          }
        }
        chars += 1
      }
      i = j + 1
    }
    ans
  }
}
'''

FILES["2954_count_the_number_of_infection_sequences"] = r'''// LeetCode 2954 - Count the Number of Infection Sequences
// https://leetcode.com/problems/count-the-number-of-infection-sequences/

object Solution {
  private val MOD = 1000000007

  private def modPow(a0: Long, b0: Int): Int = {
    var a = a0
    var b = b0
    var res = 1L
    while (b > 0) {
      if ((b & 1) != 0) res = res * a % MOD
      a = a * a % MOD
      b >>= 1
    }
    res.toInt
  }

  def numberOfSequence(n: Int, sick: Array[Int]): Int = {
    val fact = Array.ofDim[Int](n + 1)
    val invFact = Array.ofDim[Int](n + 1)
    fact(0) = 1
    var i = 1
    while (i <= n) { fact(i) = ((1L * fact(i - 1) * i) % MOD).toInt; i += 1 }
    invFact(n) = modPow(fact(n).toLong, MOD - 2)
    i = n
    while (i > 0) { invFact(i - 1) = ((1L * invFact(i) * i) % MOD).toInt; i -= 1 }
    val m = sick.length
    val totalEmpty = n - m
    var ans = fact(totalEmpty).toLong
    var prev = -1
    for (s <- sick) {
      val gap = s - prev - 1
      if (prev == -1) ans = ans * invFact(gap) % MOD
      else if (gap > 0) ans = ans * invFact(gap) % MOD * modPow(2, gap - 1) % MOD
      prev = s
    }
    val gap2 = n - prev - 1
    ans = ans * invFact(gap2) % MOD
    ans.toInt
  }
}
'''

FILES["2955_number_of_same_end_substrings"] = r'''// LeetCode 2955 - Number of Same-End Substrings
// https://leetcode.com/problems/number-of-same-end-substrings/

object Solution {
  def sameEndSubstringCount(s: String, queries: Array[Array[Int]]): Array[Int] = {
    val n = s.length
    val pref = Array.ofDim[Array[Int]](n + 1)
    pref(0) = Array.ofDim[Int](26)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i).clone()
      pref(i + 1)(s.charAt(i) - 'a') += 1
      i += 1
    }
    val ans = Array.ofDim[Int](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val l = queries(qi)(0)
      val r = queries(qi)(1)
      var total = 0
      var c = 0
      while (c < 26) {
        val cnt = pref(r + 1)(c) - pref(l)(c)
        total += cnt * (cnt + 1) / 2
        c += 1
      }
      ans(qi) = total
      qi += 1
    }
    ans
  }
}
'''

FILES["2956_find_common_elements_between_two_arrays"] = r'''// LeetCode 2956 - Find Common Elements Between Two Arrays
// https://leetcode.com/problems/find-common-elements-between-two-arrays/

object Solution {
  def findIntersectionValues(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
    val s1 = nums1.toSet
    val s2 = nums2.toSet
    var a = 0
    var b = 0
    for (v <- nums1) if (s2.contains(v)) a += 1
    for (v <- nums2) if (s1.contains(v)) b += 1
    Array(a, b)
  }
}
'''

FILES["2957_remove_adjacent_almost_equal_characters"] = r'''// LeetCode 2957 - Remove Adjacent Almost-Equal Characters
// https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

object Solution {
  def removeAlmostEqualCharacters(word: String): Int = {
    var ans = 0
    val n = word.length
    var i = 1
    while (i < n) {
      if (math.abs(word.charAt(i) - word.charAt(i - 1)) <= 1) {
        ans += 1
        i += 2
      } else i += 1
    }
    ans
  }
}
'''

FILES["2958_length_of_longest_subarray_with_at_most_k_frequency"] = r'''// LeetCode 2958 - Length of Longest Subarray With at Most K Frequency
// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

object Solution {
  def maxSubarrayLength(nums: Array[Int], k: Int): Int = {
    val freq = scala.collection.mutable.HashMap[Int, Int]()
    var ans = 0
    var left = 0
    var right = 0
    while (right < nums.length) {
      freq(nums(right)) = freq.getOrElse(nums(right), 0) + 1
      while (freq(nums(right)) > k) {
        freq(nums(left)) = freq(nums(left)) - 1
        left += 1
      }
      if (right - left + 1 > ans) ans = right - left + 1
      right += 1
    }
    ans
  }
}
'''

FILES["2959_number_of_possible_sets_of_closing_branches"] = r'''// LeetCode 2959 - Number of Possible Sets of Closing Branches
// https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

object Solution {
  def numberOfSets(n: Int, maxDistance: Int, roads: Array[Array[Int]]): Int = {
    var ans = 0
    var mask = 0
    while (mask < (1 << n)) {
      val dist = Array.fill(n, n)(1 << 29)
      var i = 0
      while (i < n) { dist(i)(i) = 0; i += 1 }
      for (r <- roads) {
        val u = r(0)
        val v = r(1)
        val w = r(2)
        if ((mask & (1 << u)) != 0 && (mask & (1 << v)) != 0) {
          if (w < dist(u)(v)) {
            dist(u)(v) = w
            dist(v)(u) = w
          }
        }
      }
      var k = 0
      while (k < n) {
        if ((mask & (1 << k)) != 0) {
          i = 0
          while (i < n) {
            if ((mask & (1 << i)) != 0) {
              var j = 0
              while (j < n) {
                if ((mask & (1 << j)) != 0 && dist(i)(k) + dist(k)(j) < dist(i)(j))
                  dist(i)(j) = dist(i)(k) + dist(k)(j)
                j += 1
              }
            }
            i += 1
          }
        }
        k += 1
      }
      var ok = true
      i = 0
      while (i < n && ok) {
        if ((mask & (1 << i)) != 0) {
          var j = 0
          while (j < n) {
            if ((mask & (1 << j)) != 0 && dist(i)(j) > maxDistance) { ok = false }
            j += 1
          }
        }
        i += 1
      }
      if (ok) ans += 1
      mask += 1
    }
    ans
  }
}
'''

FILES["2960_count_tested_devices_after_test_operations"] = r'''// LeetCode 2960 - Count Tested Devices After Test Operations
// https://leetcode.com/problems/count-tested-devices-after-test-operations/

object Solution {
  def countTestedDevices(batteryPercentages: Array[Int]): Int = {
    var ans = 0
    for (b <- batteryPercentages) if (b > ans) ans += 1
    ans
  }
}
'''

FILES["2961_double_modular_exponentiation"] = r'''// LeetCode 2961 - Double Modular Exponentiation
// https://leetcode.com/problems/double-modular-exponentiation/

object Solution {
  private def modPow(a0: Long, b0: Long, mod: Long): Long = {
    var res = 1L % mod
    var a = a0 % mod
    var b = b0
    while (b > 0) {
      if ((b & 1) != 0) res = res * a % mod
      a = a * a % mod
      b >>= 1
    }
    res
  }

  def getGoodIndices(variables: Array[Array[Int]], target: Int): List[Int] = {
    val ans = scala.collection.mutable.ListBuffer.empty[Int]
    var i = 0
    while (i < variables.length) {
      val v = variables(i)
      if (modPow(modPow(v(0).toLong, v(1).toLong, 10), v(2).toLong, v(3).toLong) == target) ans += i
      i += 1
    }
    ans.toList
  }
}
'''

def main():
    n = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "Solution.scala"
        path.write_text(content, encoding="utf-8", newline="\n")
        if content.startswith("\ufeff"):
            raise SystemExit(f"BOM in {folder}")
        n += 1
        print("wrote", folder)
    print("total", n)

if __name__ == "__main__":
    main()
