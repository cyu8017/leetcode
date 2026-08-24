#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("3847_find_the_score_difference_in_a_game", r'''
// LeetCode 3847 - Find The Score Difference In A Game
// https://leetcode.com/problems/find-the-score-difference-in-a-game/

object Solution {
  def scoreDifference(nums: Array[Int]): Int = {
    var ans = 0
    var k = 1
    var i = 0
    while (i < nums.length) {
      if (nums(i) % 2 != 0) k = -k
      if (i % 6 == 5) k = -k
      ans += k * nums(i)
      i += 1
    }
    ans
  }
}
''')

w("3848_check_digitorial_permutation", r'''
// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

object Solution {
  def isDigitorialPermutation(n: Int): Boolean = {
    val f = new Array[Int](10)
    f(0) = 1
    var i = 1
    while (i < 10) {
      f(i) = f(i - 1) * i
      i += 1
    }
    var x = 0
    var y = n
    while (y > 0) {
      x += f(y % 10)
      y /= 10
    }
    val a = x.toString.toCharArray.sorted
    val b = n.toString.toCharArray.sorted
    a.sameElements(b)
  }
}
''')

w("3849_maximum_bitwise_xor_after_rearrangement", r'''
// LeetCode 3849 - Maximum Bitwise Xor After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

object Solution {
  def maximumXor(s: String, t: String): String = {
    val cnt = new Array[Int](2)
    t.foreach { c => cnt(c - '0') += 1 }
    val ans = new Array[Char](s.length)
    var i = 0
    while (i < s.length) {
      val x = s.charAt(i) - '0'
      if (cnt(x ^ 1) > 0) {
        cnt(x ^ 1) -= 1
        ans(i) = '1'
      } else {
        cnt(x) -= 1
        ans(i) = '0'
      }
      i += 1
    }
    new String(ans)
  }
}
''')

w("3850_count_sequences_to_k", r'''
// LeetCode 3850 - Count Sequences To K
// https://leetcode.com/problems/count-sequences-to-k/

object Solution {
  private var nums: Array[Int] = _
  private var k: Long = _
  private val f = scala.collection.mutable.Map.empty[String, Int]

  def countSequences(nums: Array[Int], k: Long): Int = {
    this.nums = nums
    this.k = k
    f.clear()
    dfs(0, 1, 1)
  }

  private def gcd(a0: Long, b0: Long): Long = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  private def dfs(i: Int, p: Long, q: Long): Int = {
    if (i == nums.length) return if (p == k && q == 1) 1 else 0
    val key = i + "," + p + "," + q
    if (f.contains(key)) return f(key)
    var res = dfs(i + 1, p, q)
    val x = nums(i).toLong
    val g1 = gcd(p * x, q)
    res += dfs(i + 1, (p * x) / g1, q / g1)
    val g2 = gcd(p, q * x)
    res += dfs(i + 1, p / g2, (q * x) / g2)
    f(key) = res
    res
  }
}
''')

w("3851_maximum_requests_without_violating_the_limit", r'''
// LeetCode 3851 - Maximum Requests Without Violating The Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

object Solution {
  def maxRequests(requests: Array[Array[Int]], k: Int, window: Int): Int = {
    val g = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    requests.foreach { r =>
      g.getOrElseUpdate(r(0), scala.collection.mutable.ArrayBuffer.empty[Int]) += r(1)
    }
    var ans = requests.length
    g.values.foreach { ts =>
      val sorted = ts.sorted
      val kept = scala.collection.mutable.ArrayBuffer.empty[Int]
      sorted.foreach { t =>
        while (kept.nonEmpty && t - kept(0) > window) kept.remove(0)
        if (kept.length < k) kept += t
        else ans -= 1
      }
    }
    ans
  }
}
''')

w("3852_smallest_pair_with_different_frequencies", r'''
// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

object Solution {
  def minDistinctFreqPair(nums: Array[Int]): Array[Int] = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    nums.foreach { v => cnt(v) = cnt.getOrElse(v, 0) + 1 }
    var x = nums(0)
    nums.foreach { v => x = math.min(x, v) }
    var minY = Int.MaxValue
    cnt.keys.foreach { y =>
      if (y < minY && cnt(x) != cnt(y)) minY = y
    }
    if (minY == Int.MaxValue) Array(-1, -1)
    else Array(x, minY)
  }
}
''')

w("3853_merge_close_characters", r'''
// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

object Solution {
  def mergeCharacters(s: String, k: Int): String = {
    val last = scala.collection.mutable.Map.empty[Char, Int]
    val ans = new StringBuilder
    s.foreach { c =>
      val cur = ans.length
      if (!(last.contains(c) && cur - last(c) <= k)) {
        ans.append(c)
        last(c) = cur
      }
    }
    ans.toString
  }
}
''')

w("3854_minimum_operations_to_make_array_parity_alternating", r'''
// LeetCode 3854 - Minimum Operations To Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

object Solution {
  def makeParityAlternating(nums: Array[Int]): Array[Int] = {
    if (nums.length == 1) return Array(0, 0)
    var mn = nums(0)
    var mx = nums(0)
    nums.foreach { x =>
      mn = math.min(mn, x)
      mx = math.max(mx, x)
    }
    val r0 = f(nums, 0, mn, mx)
    val r1 = f(nums, 1, mn, mx)
    if (r0(0) != r1(0)) {
      if (r0(0) < r1(0)) r0 else r1
    } else if (r0(1) <= r1(1)) r0
    else r1
  }

  private def f(nums: Array[Int], k: Int, mn: Int, mx: Int): Array[Int] = {
    var cnt = 0
    var a = Int.MaxValue
    var b = Int.MinValue
    var i = 0
    while (i < nums.length) {
      var x = nums(i)
      if (((x - i) & 1) != k) {
        cnt += 1
        if (x == mn) x += 1
        else if (x == mx) x -= 1
      }
      a = math.min(a, x)
      b = math.max(b, x)
      i += 1
    }
    Array(cnt, math.max(1, b - a))
  }
}
''')

w("3855_sum_of_k_digit_numbers_in_a_range", r'''
// LeetCode 3855 - Sum Of K Digit Numbers In A Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

object Solution {
  private def qpow(a0: Long, n0: Long, mod: Long): Long = {
    var a = a0 % mod
    var n = n0
    var ans = 1L
    while (n > 0) {
      if ((n & 1) != 0) ans = ans * a % mod
      a = a * a % mod
      n >>= 1
    }
    ans
  }

  def sumOfNumbers(l: Int, r: Int, k: Int): Int = {
    val MOD = 1000000007L
    val n = r.toLong - l + 1
    val sum = (l.toLong + r) * n / 2 % MOD
    val part1 = qpow(n % MOD, k - 1, MOD)
    val part2 = (qpow(10, k, MOD) - 1 + MOD) % MOD
    val inv9 = qpow(9, MOD - 2, MOD)
    var ans = sum
    ans = ans * part1 % MOD
    ans = ans * part2 % MOD
    ans = ans * inv9 % MOD
    ans.toInt
  }
}
''')

w("3856_trim_trailing_vowels", r'''
// LeetCode 3856 - Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/

object Solution {
  def trimTrailingVowels(s: String): String = {
    var i = s.length - 1
    while (i >= 0 && isVowel(s.charAt(i))) i -= 1
    s.substring(0, i + 1)
  }

  private def isVowel(c: Char): Boolean =
    c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}
''')

w("3857_minimum_cost_to_split_into_ones", r'''
// LeetCode 3857 - Minimum Cost To Split Into Ones
// https://leetcode.com/problems/minimum-cost-to-split-into-ones/

object Solution {
  def minCost(n: Int): Int = n * (n - 1) / 2
}
''')

w("3858_minimum_bitwise_or_from_grid", r'''
// LeetCode 3858 - Minimum Bitwise Or From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

object Solution {
  private def bitLen(x0: Int): Int = {
    var x = x0
    if (x == 0) return 0
    var n = 0
    while (x > 0) { n += 1; x >>= 1 }
    n
  }

  def minimumOR(grid: Array[Array[Int]]): Int = {
    var mx = 0
    grid.foreach { row => row.foreach { x => mx = math.max(mx, x) } }
    val m = bitLen(mx)
    var ans = 0
    var i = m - 1
    while (i >= 0) {
      val mask = ans | ((1 << i) - 1)
      var needBit = false
      grid.foreach { row =>
        if (!needBit) {
          var found = false
          row.foreach { x => if ((x | mask) == mask) found = true }
          if (!found) {
            ans |= 1 << i
            needBit = true
          }
        }
      }
      i -= 1
    }
    ans
  }
}
''')

w("3859_count_subarrays_with_k_distinct_integers", r'''
// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

object Solution {
  private var nums: Array[Int] = _
  private var k: Int = _
  private var m: Int = _

  def countSubarrays(nums: Array[Int], k: Int, m: Int): Long = {
    this.nums = nums
    this.k = k
    this.m = m
    f(k) - f(k + 1)
  }

  private def f(lim: Int): Long = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0L
    var l = 0
    var t = 0
    nums.foreach { x =>
      val c = cnt.getOrElse(x, 0) + 1
      cnt(x) = c
      if (c == m) t += 1
      while (cnt.size >= lim && t >= k) {
        val y = nums(l)
        l += 1
        val cy = cnt(y) - 1
        if (cy == m - 1) t -= 1
        if (cy == 0) cnt.remove(y)
        else cnt(y) = cy
      }
      ans += l
    }
    ans
  }
}
''')

w("3860_unique_email_groups", r'''
// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

object Solution {
  def uniqueEmailGroups(emails: Array[String]): Int = {
    val st = scala.collection.mutable.Set.empty[String]
    emails.foreach { email =>
      val at = email.indexOf('@')
      var local = email.substring(0, at)
      val domain = email.substring(at + 1).toLowerCase
      val plus = local.indexOf('+')
      if (plus >= 0) local = local.substring(0, plus)
      val cleaned = new StringBuilder
      local.foreach { c => if (c != '.') cleaned.append(c.toLower) }
      st += cleaned.toString + domain
    }
    st.size
  }
}
''')

w("3861_minimum_capacity_box", r'''
// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

object Solution {
  def minimumIndex(capacity: Array[Int], itemSize: Int): Int = {
    var ans = -1
    var i = 0
    while (i < capacity.length) {
      if (capacity(i) >= itemSize && (ans == -1 || capacity(i) < capacity(ans))) ans = i
      i += 1
    }
    ans
  }
}
''')

w("3862_find_the_smallest_balanced_index", r'''
// LeetCode 3862 - Find The Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/

object Solution {
  def smallestBalancedIndex(nums: Array[Int]): Int = {
    var s = 0L
    var p = 1L
    nums.foreach { x => s += x }
    var i = nums.length - 1
    while (i >= 0) {
      s -= nums(i)
      if (s == p) return i
      p *= nums(i)
      if (p >= s) return {
        i = -1
        -1
      }
      i -= 1
    }
    -1
  }
}
''')

w("3863_minimum_operations_to_sort_a_string", r'''
// LeetCode 3863 - Minimum Operations To Sort A String
// https://leetcode.com/problems/minimum-operations-to-sort-a-string/

object Solution {
  def minOperations(s: String): Int = {
    val n = s.length
    var sorted = true
    var i = 1
    while (i < n) {
      if (s.charAt(i) < s.charAt(i - 1)) { sorted = false; i = n }
      else i += 1
    }
    if (sorted) return 0
    if (n == 2) return -1
    var mn = s.charAt(0)
    var mx = s.charAt(0)
    s.foreach { c =>
      if (c < mn) mn = c
      if (c > mx) mx = c
    }
    if (s.charAt(0) == mn || s.charAt(n - 1) == mx) return 1
    i = 1
    while (i < n - 1) {
      if (s.charAt(i) == mn || s.charAt(i) == mx) return 2
      i += 1
    }
    3
  }
}
''')

w("3864_minimum_cost_to_partition_a_binary_string", r'''
// LeetCode 3864 - Minimum Cost To Partition A Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

object Solution {
  private var pre: Array[Int] = _
  private var encCost: Int = _
  private var flatCost: Int = _

  def minCost(s: String, encCost: Int, flatCost: Int): Long = {
    val n = s.length
    this.encCost = encCost
    this.flatCost = flatCost
    pre = new Array[Int](n + 1)
    var i = 1
    while (i <= n) {
      pre(i) = pre(i - 1) + (s.charAt(i - 1) - '0')
      i += 1
    }
    dfs(0, n)
  }

  private def dfs(l: Int, r: Int): Long = {
    val x = pre(r) - pre(l)
    var res = if (x != 0) (r - l).toLong * x * encCost else flatCost.toLong
    if ((r - l) % 2 == 0) {
      val m = (l + r) / 2
      res = math.min(res, dfs(l, m) + dfs(m, r))
    }
    res
  }
}
''')

w("3865_reverse_k_subarrays", r'''
// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

object Solution {
  def reverseSubarrays(nums: Array[Int], k: Int): Array[Int] = {
    val n = nums.length
    val m = n / k
    var i = 0
    while (i < n) {
      var lo = i
      var hi = i + m - 1
      while (lo < hi) {
        val t = nums(lo)
        nums(lo) = nums(hi)
        nums(hi) = t
        lo += 1
        hi -= 1
      }
      i += m
    }
    nums
  }
}
''')

w("3866_first_unique_even_element", r'''
// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

object Solution {
  def firstUniqueEven(nums: Array[Int]): Int = {
    val cnt = new Array[Int](101)
    nums.foreach { x => cnt(x) += 1 }
    nums.foreach { x =>
      if (x % 2 == 0 && cnt(x) == 1) return x
    }
    -1
  }
}
''')

w("3867_sum_of_gcd_of_formed_pairs", r'''
// LeetCode 3867 - Sum Of Gcd Of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

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

  def gcdSum(nums: Array[Int]): Long = {
    val n = nums.length
    val prefixGcd = new Array[Int](n)
    var mx = 0
    var i = 0
    while (i < n) {
      mx = math.max(mx, nums(i))
      prefixGcd(i) = gcd(nums(i), mx)
      i += 1
    }
    java.util.Arrays.sort(prefixGcd)
    var ans = 0L
    i = 0
    while (i < n / 2) {
      ans += gcd(prefixGcd(i), prefixGcd(n - i - 1))
      i += 1
    }
    ans
  }
}
''')

w("3868_minimum_cost_to_equalize_arrays_using_swaps", r'''
// LeetCode 3868 - Minimum Cost To Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

object Solution {
  def minCost(nums1: Array[Int], nums2: Array[Int]): Int = {
    val cnt2 = scala.collection.mutable.Map.empty[Int, Int]
    nums2.foreach { x => cnt2(x) = cnt2.getOrElse(x, 0) + 1 }
    val cnt1 = scala.collection.mutable.Map.empty[Int, Int]
    nums1.foreach { x =>
      val c = cnt2.getOrElse(x, 0)
      if (c > 0) cnt2(x) = c - 1
      else cnt1(x) = cnt1.getOrElse(x, 0) + 1
    }
    var ans = 0
    cnt1.values.foreach { v =>
      if (v % 2 == 1) return -1
      ans += v / 2
    }
    cnt2.values.foreach { v =>
      if (v % 2 == 1) return -1
    }
    ans
  }
}
''')

w("3869_count_fancy_numbers_in_a_range", r'''
// LeetCode 3869 - Count Fancy Numbers In A Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

object Solution {
  private var num: String = _
  private var f: Array[Array[Array[Array[Long]]]] = _
  private var n: Int = _

  private def check(s: Int): Boolean = {
    if (s < 100) return s % 11 != 0
    val mid = (s / 10) % 10
    val last = s % 10
    mid > 1 && mid < last
  }

  def countFancy(l: Long, r: Long): Long = calc(r) - calc(l - 1)

  private def calc(x: Long): Long = {
    num = x.toString
    n = num.length
    f = Array.ofDim[Long](n, 9 * n + 1, 10, 4)
    var i = 0
    while (i < n) {
      var j = 0
      while (j <= 9 * n) {
        var p = 0
        while (p < 10) {
          java.util.Arrays.fill(f(i)(j)(p), -1L)
          p += 1
        }
        j += 1
      }
      i += 1
    }
    dfs(0, 0, 0, 0, true)
  }

  private def dfs(pos: Int, s: Int, prev: Int, st: Int, lim: Boolean): Long = {
    if (pos >= n) {
      if (st != 3) return 1
      return if (check(s)) 1 else 0
    }
    if (!lim && f(pos)(s)(prev)(st) != -1) return f(pos)(s)(prev)(st)
    val up = if (lim) num.charAt(pos) - '0' else 9
    var res = 0L
    var i = 0
    while (i <= up) {
      var nxtSt = st
      if (st == 0) {
        if (prev == 0) nxtSt = 0
        else if (i > prev) nxtSt = 1
        else if (i < prev) nxtSt = 2
        else nxtSt = 3
      } else if (st == 1) {
        nxtSt = if (i > prev) 1 else 3
      } else if (st == 2) {
        nxtSt = if (i < prev) 2 else 3
      } else {
        nxtSt = 3
      }
      res += dfs(pos + 1, s + i, i, nxtSt, lim && i == up)
      i += 1
    }
    if (!lim) f(pos)(s)(prev)(st) = res
    res
  }
}
''')

w("3870_count_commas_in_range", r'''
// LeetCode 3870 - Count Commas In Range
// https://leetcode.com/problems/count-commas-in-range/

object Solution {
  def countCommas(n: Int): Int = math.max(0, n - 999)
}
''')

w("3871_count_commas_in_range_ii", r'''
// LeetCode 3871 - Count Commas In Range Ii
// https://leetcode.com/problems/count-commas-in-range-ii/

object Solution {
  def countCommas(n: Long): Long = {
    var ans = 0L
    var x = 1000L
    while (x <= n) {
      ans += n - x + 1
      x *= 1000
    }
    ans
  }
}
''')

print("batch B done")
