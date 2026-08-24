#!/usr/bin/env python3
"""Write Scala solutions for batch_12 folders 2912-2936."""
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

FILES = {}

FILES["2912_number_of_ways_to_reach_destination_in_the_grid"] = r'''// LeetCode 2912 - Number of Ways to Reach Destination in the Grid
// https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/

object Solution {
  def numberOfWays(n: Int, m: Int, k: Int, source: Array[Int], dest: Array[Int]): Int = {
    val mod = 1000000007
    val sx = source(0)
    val sy = source(1)
    val tx = dest(0)
    val ty = dest(1)
    var same = 0L
    var row = 0L
    var col = 0L
    var other = 0L
    if (sx == tx && sy == ty) same = 1
    else if (sx == tx) row = 1
    else if (sy == ty) col = 1
    else other = 1
    for (_ <- 0 until k) {
      val ns = (row * (m - 1) + col * (n - 1)) % mod
      val nr = (same + row * (m - 2) % mod + other * (n - 1) % mod) % mod
      val nc = (same + col * (n - 2) % mod + other * (m - 1) % mod) % mod
      val no = (row * (n - 1) + col * (m - 1) + other * (n + m - 4) % mod) % mod
      same = ns
      row = nr
      col = nc
      other = no
    }
    if (sx == tx && sy == ty) same.toInt
    else if (sx == tx) row.toInt
    else if (sy == ty) col.toInt
    else other.toInt
  }
}
'''

FILES["2913_subarrays_distinct_element_sum_of_squares_i"] = r'''// LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

object Solution {
  def sumCounts(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    for (i <- 0 until n) {
      val seen = scala.collection.mutable.Set.empty[Int]
      for (j <- i until n) {
        seen += nums(j)
        val d = seen.size
        ans += d * d
      }
    }
    ans
  }
}
'''

FILES["2914_minimum_number_of_changes_to_make_binary_string_beautiful"] = r'''// LeetCode 2914 - Minimum Number of Changes to Make Binary String Beautiful
// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

object Solution {
  def minChanges(s: String): Int = {
    var ans = 0
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) != s.charAt(i + 1)) ans += 1
      i += 2
    }
    ans
  }
}
'''

FILES["2915_length_of_the_longest_subsequence_that_sums_to_target"] = r'''// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

object Solution {
  def lengthOfLongestSubsequence(nums: Array[Int], target: Int): Int = {
    val dp = Array.fill(target + 1)(-1)
    dp(0) = 0
    nums.foreach { v =>
      var s = target
      while (s >= v) {
        if (dp(s - v) >= 0 && dp(s - v) + 1 > dp(s)) dp(s) = dp(s - v) + 1
        s -= 1
      }
    }
    dp(target)
  }
}
'''

FILES["2916_subarrays_distinct_element_sum_of_squares_ii"] = r'''// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

object Solution {
  private val MOD = 1000000007
  private var tree: Array[Node] = _

  private class Node {
    var sum: Int = 0
    var sumSq: Int = 0
    var lazy: Int = 0
  }

  def sumCounts(nums: Array[Int]): Int = {
    val n = nums.length
    val last = scala.collection.mutable.Map.empty[Int, Int]
    tree = Array.fill(4 * (n + 2))(new Node)
    var ans = 0
    for (i <- 1 to n) {
      val v = nums(i - 1)
      val prev = last.getOrElse(v, 0)
      update(1, 1, n, prev + 1, i, 1)
      ans = (ans + tree(1).sumSq) % MOD
      last(v) = i
    }
    ans
  }

  private def apply(idx: Int, l: Int, r: Int, value: Int): Unit = {
    val length = r - l + 1
    tree(idx).sumSq = ((tree(idx).sumSq + 2L * value % MOD * tree(idx).sum % MOD
      + 1L * value % MOD * value % MOD * length % MOD) % MOD).toInt
    tree(idx).sum = ((tree(idx).sum + 1L * value % MOD * length % MOD) % MOD).toInt
    tree(idx).lazy = (tree(idx).lazy + value) % MOD
  }

  private def update(idx: Int, l: Int, r: Int, ql: Int, qr: Int, value: Int): Unit = {
    if (ql > r || qr < l) return
    if (ql <= l && r <= qr) {
      apply(idx, l, r, value)
      return
    }
    if (tree(idx).lazy != 0 && l != r) {
      val mid = (l + r) / 2
      apply(idx * 2, l, mid, tree(idx).lazy)
      apply(idx * 2 + 1, mid + 1, r, tree(idx).lazy)
      tree(idx).lazy = 0
    }
    val mid = (l + r) / 2
    update(idx * 2, l, mid, ql, qr, value)
    update(idx * 2 + 1, mid + 1, r, ql, qr, value)
    tree(idx).sum = (tree(idx * 2).sum + tree(idx * 2 + 1).sum) % MOD
    tree(idx).sumSq = (tree(idx * 2).sumSq + tree(idx * 2 + 1).sumSq) % MOD
  }
}
'''

FILES["2917_find_the_k_or_of_an_array"] = r'''// LeetCode 2917 - Find the K-or of an Array
// https://leetcode.com/problems/find-the-k-or-of-an-array/

object Solution {
  def findKOr(nums: Array[Int], k: Int): Int = {
    var ans = 0
    for (b <- 0 until 31) {
      var cnt = 0
      nums.foreach { v => if ((v & (1 << b)) != 0) cnt += 1 }
      if (cnt >= k) ans |= 1 << b
    }
    ans
  }
}
'''

FILES["2918_minimum_equal_sum_of_two_arrays_after_replacing_zeros"] = r'''// LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

object Solution {
  def minSum(nums1: Array[Int], nums2: Array[Int]): Long = {
    var s1 = 0L
    var s2 = 0L
    var z1 = 0
    var z2 = 0
    nums1.foreach { v =>
      if (v == 0) {
        z1 += 1
        s1 += 1
      } else s1 += v
    }
    nums2.foreach { v =>
      if (v == 0) {
        z2 += 1
        s2 += 1
      } else s2 += v
    }
    if (z1 == 0 && s1 < s2) return -1
    if (z2 == 0 && s2 < s1) return -1
    if (s1 > s2) s1 else s2
  }
}
'''

FILES["2919_minimum_increment_operations_to_make_array_beautiful"] = r'''// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

object Solution {
  def minIncrementOperations(nums: Array[Int], k: Int): Long = {
    var dp0 = 0L
    var dp1 = 0L
    var dp2 = 0L
    nums.foreach { v =>
      val cost = if (v < k) k - v else 0
      val nd0 = cost + math.min(dp0, math.min(dp1, dp2))
      dp0 = dp1
      dp1 = dp2
      dp2 = nd0
    }
    math.min(dp0, math.min(dp1, dp2))
  }
}
'''

FILES["2920_maximum_points_after_collecting_coins_from_all_nodes"] = r'''// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

object Solution {
  private var g: Array[scala.collection.mutable.ArrayBuffer[Int]] = _
  private var coins: Array[Int] = _
  private var k: Int = _
  private var memo: scala.collection.mutable.Map[Long, Int] = _

  def maximumPoints(edges: Array[Array[Int]], coins: Array[Int], k: Int): Int = {
    val n = coins.length
    this.coins = coins
    this.k = k
    g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    memo = scala.collection.mutable.Map.empty[Long, Int]
    dfs(0, -1, 0)
  }

  private def dfs(u: Int, p: Int, shifts0: Int): Int = {
    var shifts = shifts0
    if (shifts > 14) shifts = 14
    val key = (u.toLong << 5) | shifts
    if (memo.contains(key)) return memo(key)
    val c = coins(u) >> shifts
    var opt1 = c - k
    var opt2 = c / 2
    g(u).foreach { v =>
      if (v != p) {
        opt1 += dfs(v, u, shifts)
        opt2 += dfs(v, u, shifts + 1)
      }
    }
    val best = math.max(opt1, opt2)
    memo(key) = best
    best
  }
}
'''

FILES["2921_maximum_profitable_triplets_with_increasing_prices_ii"] = r'''// LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

object Solution {
  private var bit: Array[Int] = _

  def maxProfit(prices: Array[Int], profits: Array[Int]): Int = {
    val n = prices.length
    var ans = -1
    val maxLeft = Array.fill(n)(0)
    bit = Array.fill(5002)(0)
    for (j <- 0 until n) {
      maxLeft(j) = query(prices(j) - 1)
      update(prices(j), profits(j))
    }
    for (j <- 0 until n) {
      var bestR = -1
      for (k <- j + 1 until n if prices(k) > prices(j) && profits(k) > bestR) bestR = profits(k)
      if (maxLeft(j) >= 0 && bestR >= 0) {
        val cand = maxLeft(j) + profits(j) + bestR
        if (cand > ans) ans = cand
      }
    }
    ans
  }

  private def update(i0: Int, value: Int): Unit = {
    var i = i0
    while (i < bit.length) {
      if (value > bit(i)) bit(i) = value
      i += i & -i
    }
  }

  private def query(i0: Int): Int = {
    var best = -1
    var i = i0
    while (i > 0) {
      if (bit(i) > best) best = bit(i)
      i -= i & -i
    }
    best
  }
}
'''

FILES["2923_find_champion_i"] = r'''// LeetCode 2923 - Find Champion I
// https://leetcode.com/problems/find-champion-i/

object Solution {
  def findChampion(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    for (i <- 0 until n) {
      var win = true
      var j = 0
      while (j < n && win) {
        if (i != j && grid(i)(j) == 0) win = false
        j += 1
      }
      if (win) return i
    }
    -1
  }
}
'''

FILES["2924_find_champion_ii"] = r'''// LeetCode 2924 - Find Champion II
// https://leetcode.com/problems/find-champion-ii/

object Solution {
  def findChampion(n: Int, edges: Array[Array[Int]]): Int = {
    val indeg = Array.fill(n)(0)
    edges.foreach(e => indeg(e(1)) += 1)
    var ans = -1
    for (i <- 0 until n if indeg(i) == 0) {
      if (ans != -1) return -1
      ans = i
    }
    ans
  }
}
'''

FILES["2925_maximum_score_after_applying_operations_on_a_tree"] = r'''// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

object Solution {
  private var g: Array[scala.collection.mutable.ArrayBuffer[Int]] = _
  private var values: Array[Int] = _

  def maximumScoreAfterOperations(edges: Array[Array[Int]], values: Array[Int]): Long = {
    val n = values.length
    this.values = values
    g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    var total = 0L
    values.foreach(v => total += v)
    total - dfs(0, -1)
  }

  private def dfs(u: Int, p: Int): Long = {
    var sumKids = 0L
    var isLeaf = true
    g(u).foreach { v =>
      if (v != p) {
        isLeaf = false
        sumKids += dfs(v, u)
      }
    }
    if (isLeaf) values(u).toLong
    else if (values(u) < sumKids) values(u).toLong else sumKids
  }
}
'''

FILES["2926_maximum_balanced_subsequence_sum"] = r'''// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

object Solution {
  private var bit: Array[Long] = _
  private val NEG_INF = -(1L << 60)

  def maxBalancedSubsequenceSum(nums: Array[Int]): Long = {
    val n = nums.length
    val keys = Array.tabulate(n)(i => nums(i) - i)
    val uniq = keys.sorted.distinct
    bit = Array.fill(uniq.length + 2)(NEG_INF)
    var ans = NEG_INF
    for (i <- 0 until n) {
      val id = idxOf(uniq, keys(i))
      val best = query(id)
      var cur = nums(i).toLong
      if (best > NEG_INF / 2) {
        val cand = best + nums(i)
        if (cand > cur) cur = cand
      }
      update(id, cur)
      if (cur > ans) ans = cur
    }
    ans
  }

  private def idxOf(uniq: Array[Int], v: Int): Int = {
    var lo = 0
    var hi = uniq.length
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (uniq(mid) < v) lo = mid + 1
      else hi = mid
    }
    lo + 1
  }

  private def update(i0: Int, value: Long): Unit = {
    var i = i0
    while (i < bit.length) {
      if (value > bit(i)) bit(i) = value
      i += i & -i
    }
  }

  private def query(i0: Int): Long = {
    var best = NEG_INF
    var i = i0
    while (i > 0) {
      if (bit(i) > best) best = bit(i)
      i -= i & -i
    }
    best
  }
}
'''

FILES["2927_distribute_candies_among_children_iii"] = r'''// LeetCode 2927 - Distribute Candies Among Children III
// https://leetcode.com/problems/distribute-candies-among-children-iii/

object Solution {
  def distributeCandies(n: Int, limit: Int): Long = {
    var ans = comb(n + 2L)
    ans -= 3 * comb((n - limit).toLong + 1)
    ans += 3 * comb((n - 2 * (limit + 1)).toLong + 2)
    ans -= comb((n - 3 * (limit + 1)).toLong + 2)
    if (ans < 0) 0 else ans
  }

  private def comb(x: Long): Long = if (x < 2) 0 else x * (x - 1) / 2
}
'''

FILES["2928_distribute_candies_among_children_i"] = r'''// LeetCode 2928 - Distribute Candies Among Children I
// https://leetcode.com/problems/distribute-candies-among-children-i/

object Solution {
  def distributeCandies(n: Int, limit: Int): Int = {
    var ans = 0
    for (i <- 0 to limit; j <- 0 to limit) {
      val k = n - i - j
      if (k >= 0 && k <= limit) ans += 1
    }
    ans
  }
}
'''

FILES["2929_distribute_candies_among_children_ii"] = r'''// LeetCode 2929 - Distribute Candies Among Children II
// https://leetcode.com/problems/distribute-candies-among-children-ii/

object Solution {
  def distributeCandies(n: Int, limit: Int): Long = {
    var ans = comb2(n)
    ans -= 3 * comb2(n - (limit + 1))
    ans += 3 * comb2(n - 2 * (limit + 1))
    ans -= comb2(n - 3 * (limit + 1))
    ans
  }

  private def comb2(x: Long): Long = if (x < 0) 0 else (x + 1) * (x + 2) / 2
}
'''

FILES["2930_number_of_strings_which_can_be_rearranged_to_contain_substring"] = r'''// LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
// https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

object Solution {
  private val MOD = 1000000007

  def stringCount(n: Int): Int = {
    if (n < 4) return 0
    var ans = modPow(26, n).toLong
    ans = (ans - 3L * modPow(25, n) % MOD + MOD) % MOD
    ans = (ans + 3L * modPow(24, n) % MOD) % MOD
    ans = (ans - modPow(23, n) + MOD) % MOD
    ans = (ans + 1L * (n % MOD) * modPow(25, n - 1) % MOD) % MOD
    ans = (ans - 2L * (n % MOD) % MOD * modPow(24, n - 1) % MOD + MOD) % MOD
    ans = (ans + 1L * (n % MOD) * modPow(23, n - 1) % MOD) % MOD
    ans = (ans - 1L * (n % MOD) * ((n - 1 + MOD) % MOD) % MOD * modPow(24, n - 2) % MOD % MOD + MOD) % MOD
    ans = (ans + 1L * (n % MOD) * ((n - 1 + MOD) % MOD) % MOD * modPow(23, n - 2) % MOD) % MOD
    ans.toInt
  }

  private def modPow(a0: Long, b0: Int): Int = {
    var res = 1L
    var a = a0 % MOD
    var b = b0
    while (b > 0) {
      if ((b & 1) != 0) res = res * a % MOD
      a = a * a % MOD
      b >>= 1
    }
    res.toInt
  }
}
'''

FILES["2931_maximum_spending_after_buying_items"] = r'''// LeetCode 2931 - Maximum Spending After Buying Items
// https://leetcode.com/problems/maximum-spending-after-buying-items/

object Solution {
  def maxSpending(values: Array[Array[Int]]): Long = {
    val m = values.length
    val n = values(0).length
    val idx = Array.fill(m)(n - 1)
    var ans = 0L
    var day = 1L
    val total = m * n
    for (_ <- 0 until total) {
      var bestI = -1
      var bestV = 1L << 60
      for (i <- 0 until m) {
        if (idx(i) >= 0 && values(i)(idx(i)) < bestV) {
          bestV = values(i)(idx(i))
          bestI = i
        }
      }
      ans += bestV * day
      idx(bestI) -= 1
      day += 1
    }
    ans
  }
}
'''

FILES["2932_maximum_strong_pair_xor_i"] = r'''// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/

object Solution {
  def maximumStrongPairXor(nums: Array[Int]): Int = {
    var ans = 0
    for (i <- nums.indices; j <- i until nums.length) {
      val x = nums(i)
      val y = nums(j)
      if (math.abs(x - y) <= math.min(x, y)) {
        val xorr = x ^ y
        if (xorr > ans) ans = xorr
      }
    }
    ans
  }
}
'''

FILES["2933_high_access_employees"] = r'''// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/

object Solution {
  def findHighAccessEmployees(access_times: Array[Array[String]]): Array[String] = {
    val m = scala.collection.mutable.Map.empty[String, scala.collection.mutable.ArrayBuffer[Int]]
    access_times.foreach { a =>
      val name = a(0)
      val t = a(1)
      val hh = (t.charAt(0) - '0') * 10 + (t.charAt(1) - '0')
      val mm = (t.charAt(2) - '0') * 10 + (t.charAt(3) - '0')
      m.getOrElseUpdate(name, scala.collection.mutable.ArrayBuffer.empty[Int]) += hh * 60 + mm
    }
    val ans = scala.collection.mutable.ArrayBuffer.empty[String]
    m.foreach { case (name, times) =>
      val sorted = times.sorted
      var i = 0
      var found = false
      while (i + 2 < sorted.length && !found) {
        if (sorted(i + 2) - sorted(i) < 60) {
          ans += name
          found = true
        }
        i += 1
      }
    }
    ans.sorted.toArray
  }
}
'''

FILES["2934_minimum_operations_to_maximize_last_elements_in_arrays"] = r'''// LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
// https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

object Solution {
  def minOperations(nums1: Array[Int], nums2: Array[Int]): Int = {
    val n = nums1.length
    var ans = calc(nums1, nums2)
    val t = nums1(n - 1)
    nums1(n - 1) = nums2(n - 1)
    nums2(n - 1) = t
    val cand = calc(nums1, nums2) + 1
    if (cand < ans) ans = cand
    if (ans >= (1 << 30)) -1 else ans
  }

  private def calc(a1: Array[Int], a2: Array[Int]): Int = {
    val n = a1.length
    var ops = 0
    val last1 = a1(n - 1)
    val last2 = a2(n - 1)
    for (i <- 0 until n - 1) {
      val x = a1(i)
      val y = a2(i)
      if (x <= last1 && y <= last2) {}
      else if (y <= last1 && x <= last2) ops += 1
      else return 1 << 30
    }
    ops
  }
}
'''

FILES["2935_maximum_strong_pair_xor_ii"] = r'''// LeetCode 2935 - Maximum Strong Pair XOR II
// https://leetcode.com/problems/maximum-strong-pair-xor-ii/

object Solution {
  def maximumStrongPairXor(nums: Array[Int]): Int = {
    val a = nums.sorted
    var ans = 0
    for (i <- a.indices) {
      val x = a(i)
      var j = i
      while (j < a.length && a(j) <= 2 * x) {
        val xorr = x ^ a(j)
        if (xorr > ans) ans = xorr
        j += 1
      }
    }
    ans
  }
}
'''

FILES["2936_number_of_equal_numbers_blocks"] = r'''// LeetCode 2936 - Number of Equal Numbers Blocks
// https://leetcode.com/problems/number-of-equal-numbers-blocks/

object Solution {
  def blockCount(nums: Array[Int]): Int = {
    if (nums.isEmpty) return 0
    var ans = 1
    for (i <- 1 until nums.length if nums(i) != nums(i - 1)) ans += 1
    ans
  }
}
'''

def main() -> None:
    written = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "Solution.scala"
        path.write_text(content, encoding="utf-8", newline="\n")
        if path.read_bytes().startswith(b"\xef\xbb\xbf"):
            raise SystemExit(f"BOM in {path}")
        written += 1
        print(f"wrote {folder}")
    print(f"written={written}")


if __name__ == "__main__":
    main()
