#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("3144_minimum_substring_partition_of_equal_character_frequency", r'''
// LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
// https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

object Solution {
  def minimumSubstringsInPartition(s: String): Int = {
    val n = s.length
    val memo = Array.fill(n)(-1)

    def dfs(i: Int): Int = {
      if (i >= n) return 0
      if (memo(i) != -1) return memo(i)
      val cnt = new Array[Int](26)
      val freq = scala.collection.mutable.Map.empty[Int, Int]
      memo(i) = n - i
      var j = i
      while (j < n) {
        val k = s.charAt(j) - 'a'
        if (cnt(k) > 0) {
          val c = cnt(k)
          val nv = freq(c) - 1
          if (nv == 0) freq.remove(c)
          else freq(c) = nv
        }
        cnt(k) += 1
        freq(cnt(k)) = freq.getOrElse(cnt(k), 0) + 1
        if (freq.size == 1) memo(i) = math.min(memo(i), 1 + dfs(j + 1))
        j += 1
      }
      memo(i)
    }

    dfs(0)
  }
}
''')

w("3145_find_products_of_elements_of_big_array", r'''
// LeetCode 3145 - Find Products of Elements of Big Array
// https://leetcode.com/problems/find-products-of-elements-of-big-array/

object Solution {
  private val M = 50
  private val cnt: Array[Long] = new Array[Long](M + 1)
  private val s: Array[Long] = new Array[Long](M + 1)

  {
    var p = 1L
    cnt(0) = 0
    s(0) = 0
    var i = 1
    while (i <= M) {
      cnt(i) = cnt(i - 1) * 2 + p
      s(i) = s(i - 1) * 2 + p * (i - 1)
      p *= 2
      i += 1
    }
  }

  def findProductsOfElements(queries: Array[Array[Long]]): Array[Int] = {
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      val left = queries(i)(0)
      val right = queries(i)(1)
      val mod = queries(i)(2)
      val power = f(right + 1) - f(left)
      ans(i) = qpow(2, power, mod).toInt
      i += 1
    }
    ans
  }

  private def numIdxAndSum(x0: Long): Array[Long] = {
    var x = x0
    var idx = 0L
    var totalSum = 0L
    while (x > 0) {
      val i = 63 - java.lang.Long.numberOfLeadingZeros(x)
      idx += cnt(i)
      totalSum += s(i)
      x -= 1L << i
      totalSum += (x + 1) * i
      idx += x + 1
    }
    Array(idx, totalSum)
  }

  private def f(i0: Long): Long = {
    var l = 0L
    var r = 1L << M
    while (l < r) {
      val mid = (l + r + 1) >> 1
      val p = numIdxAndSum(mid)
      if (p(0) < i0) l = mid
      else r = mid - 1
    }
    val p = numIdxAndSum(l)
    var totalSum = p(1)
    var i = i0 - p(0)
    var x = l + 1
    var j = 0L
    while (j < i) {
      val y = x & -x
      totalSum += java.lang.Long.numberOfTrailingZeros(y)
      x -= y
      j += 1
    }
    totalSum
  }

  private def qpow(a0: Long, n0: Long, mod: Long): Long = {
    var ans = 1L % mod
    var a = a0 % mod
    var n = n0
    while (n > 0) {
      if ((n & 1) != 0) ans = ans * a % mod
      a = a * a % mod
      n >>= 1
    }
    ans
  }
}
''')

w("3146_permutation_difference_between_two_strings", r'''
// LeetCode 3146 - Permutation Difference between Two Strings
// https://leetcode.com/problems/permutation-difference-between-two-strings/

object Solution {
  def findPermutationDifference(s: String, t: String): Int = {
    val d = new Array[Int](26)
    var i = 0
    while (i < s.length) {
      d(s.charAt(i) - 'a') = i
      i += 1
    }
    var ans = 0
    i = 0
    while (i < t.length) {
      ans += math.abs(d(t.charAt(i) - 'a') - i)
      i += 1
    }
    ans
  }
}
''')

w("3147_taking_maximum_energy_from_the_mystic_dungeon", r'''
// LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
// https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

object Solution {
  def maximumEnergy(energy: Array[Int], k: Int): Int = {
    var ans = -(1 << 30)
    val n = energy.length
    var i = n - k
    while (i < n) {
      var j = i
      var s = 0
      while (j >= 0) {
        s += energy(j)
        ans = math.max(ans, s)
        j -= k
      }
      i += 1
    }
    ans
  }
}
''')

w("3148_maximum_difference_score_in_a_grid", r'''
// LeetCode 3148 - Maximum Difference Score in a Grid
// https://leetcode.com/problems/maximum-difference-score-in-a-grid/

object Solution {
  def maxScore(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val INF = 1 << 30
    val f = Array.ofDim[Int](m, n)
    var ans = -INF
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val x = grid(i)(j)
        var mi = INF
        if (i > 0) mi = math.min(mi, f(i - 1)(j))
        if (j > 0) mi = math.min(mi, f(i)(j - 1))
        ans = math.max(ans, x - mi)
        f(i)(j) = math.min(x, mi)
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("3149_find_the_minimum_cost_array_permutation", r'''
// LeetCode 3149 - Find the Minimum Cost Array Permutation
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

object Solution {
  def findPermutation(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val memo = Array.fill(1 << n, n)(-1)
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]

    def absv(x: Int): Int = if (x < 0) -x else x

    def dfs(mask: Int, pre: Int): Int = {
      if (mask == (1 << n) - 1) return absv(pre - nums(0))
      if (memo(mask)(pre) != -1) return memo(mask)(pre)
      var res = Int.MaxValue
      var cur = 1
      while (cur < n) {
        if (((mask >> cur) & 1) == 0) {
          res = math.min(res, absv(pre - nums(cur)) + dfs(mask | (1 << cur), cur))
        }
        cur += 1
      }
      memo(mask)(pre) = res
      res
    }

    def g(mask: Int, pre: Int): Unit = {
      ans += pre
      if (mask == (1 << n) - 1) return
      val res = dfs(mask, pre)
      var cur = 1
      var found = false
      while (cur < n && !found) {
        if (((mask >> cur) & 1) == 0) {
          if (absv(pre - nums(cur)) + dfs(mask | (1 << cur), cur) == res) {
            g(mask | (1 << cur), cur)
            found = true
          }
        }
        cur += 1
      }
    }

    g(1, 0)
    ans.toArray
  }
}
''')

w("3151_special_array_i", r'''
// LeetCode 3151 - Special Array I
// https://leetcode.com/problems/special-array-i/

object Solution {
  def isArraySpecial(nums: Array[Int]): Boolean = {
    var i = 1
    while (i < nums.length) {
      if (nums(i) % 2 == nums(i - 1) % 2) return false
      i += 1
    }
    true
  }
}
''')

w("3152_special_array_ii", r'''
// LeetCode 3152 - Special Array II
// https://leetcode.com/problems/special-array-ii/

object Solution {
  def isArraySpecial(nums: Array[Int], queries: Array[Array[Int]]): Array[Boolean] = {
    val n = nums.length
    val d = Array.tabulate(n)(i => i)
    var i = 1
    while (i < n) {
      if (nums(i) % 2 != nums(i - 1) % 2) d(i) = d(i - 1)
      i += 1
    }
    Array.tabulate(queries.length)(i => d(queries(i)(1)) <= queries(i)(0))
  }
}
''')

w("3153_sum_of_digit_differences_of_all_pairs", r'''
// LeetCode 3153 - Sum of Digit Differences of All Pairs
// https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

object Solution {
  def sumDigitDifferences(nums: Array[Int]): Long = {
    val n = nums.length
    val m = math.floor(math.log10(nums(0))).toInt + 1
    var ans = 0L
    val vals = nums.clone()
    var k = 0
    while (k < m) {
      val cnt = new Array[Int](10)
      var i = 0
      while (i < n) {
        cnt(vals(i) % 10) += 1
        vals(i) /= 10
        i += 1
      }
      cnt.foreach(v => ans += v.toLong * (n - v))
      k += 1
    }
    ans / 2
  }
}
''')

w("3154_find_number_of_ways_to_reach_the_k_th_stair", r'''
// LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

object Solution {
  def waysToReachStair(k: Int): Int = {
    val f = scala.collection.mutable.Map.empty[Long, Int]

    def dfs(i: Long, j: Int, jump: Int): Int = {
      if (i > k + 1) return 0
      val key = (i << 32) | (jump.toLong << 1) | j
      f.get(key) match {
        case Some(cached) => cached
        case None =>
          var ans = 0
          if (i == k) ans += 1
          if (i > 0 && j == 0) ans += dfs(i - 1, 1, jump)
          ans += dfs(i + (1L << jump), 0, jump + 1)
          f(key) = ans
          ans
      }
    }

    dfs(1, 0, 0)
  }
}
''')

w("3155_maximum_number_of_upgradable_servers", r'''
// LeetCode 3155 - Maximum Number of Upgradable Servers
// https://leetcode.com/problems/maximum-number-of-upgradable-servers/

object Solution {
  def maxUpgrades(count: Array[Int], upgrade: Array[Int], sell: Array[Int], money: Array[Int]): Array[Int] = {
    val ans = new Array[Int](count.length)
    var i = 0
    while (i < count.length) {
      val cnt = count(i).toLong
      ans(i) = math.min(cnt, (cnt * sell(i) + money(i)) / (upgrade(i) + sell(i))).toInt
      i += 1
    }
    ans
  }
}
''')

w("3157_find_the_level_of_tree_with_minimum_sum", r'''
// LeetCode 3157 - Find the Level of Tree with Minimum Sum
// https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def minimumLevel(root: TreeNode): Int = {
    val q = new java.util.ArrayDeque[TreeNode]()
    q.offer(root)
    var s = Long.MaxValue
    var ans = 0
    var level = 1
    while (!q.isEmpty) {
      var t = 0L
      var m = q.size()
      while (m > 0) {
        val node = q.poll()
        t += node.value
        if (node.left != null) q.offer(node.left)
        if (node.right != null) q.offer(node.right)
        m -= 1
      }
      if (s > t) {
        s = t
        ans = level
      }
      level += 1
    }
    ans
  }
}
''')

w("3158_find_the_xor_of_numbers_which_appear_twice", r'''
// LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
// https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

object Solution {
  def duplicateNumbersXOR(nums: Array[Int]): Int = {
    val cnt = new Array[Int](51)
    var ans = 0
    nums.foreach { x =>
      cnt(x) += 1
      if (cnt(x) == 2) ans ^= x
    }
    ans
  }
}
''')

w("3159_find_occurrences_of_an_element_in_an_array", r'''
// LeetCode 3159 - Find Occurrences of an Element in an Array
// https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

object Solution {
  def occurrencesOfElement(nums: Array[Int], queries: Array[Int], x: Int): Array[Int] = {
    val ids = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < nums.length) {
      if (nums(i) == x) ids += i
      i += 1
    }
    Array.tabulate(queries.length) { qi =>
      val idx = queries(qi)
      if (idx - 1 < ids.size) ids(idx - 1) else -1
    }
  }
}
''')

w("3160_find_the_number_of_distinct_colors_among_the_balls", r'''
// LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
// https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

object Solution {
  def queryResults(limit: Int, queries: Array[Array[Int]]): Array[Int] = {
    val g = scala.collection.mutable.Map.empty[Int, Int]
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    val ans = new Array[Int](queries.length)
    var ai = 0
    queries.foreach { q =>
      val x = q(0)
      val y = q(1)
      cnt(y) = cnt.getOrElse(y, 0) + 1
      g.get(x).foreach { old =>
        val nv = cnt(old) - 1
        if (nv == 0) cnt.remove(old)
        else cnt(old) = nv
      }
      g(x) = y
      ans(ai) = cnt.size
      ai += 1
    }
    ans
  }
}
''')

w("3161_block_placement_queries", r'''
// LeetCode 3161 - Block Placement Queries
// https://leetcode.com/problems/block-placement-queries/

object Solution {
  private class FenwickMax(n: Int) {
    val vals: Array[Int] = new Array[Int](n + 1)

    def maximize(i0: Int, `val`: Int): Unit = {
      var i = i0
      while (i < vals.length) {
        vals(i) = math.max(vals(i), `val`)
        i += i & -i
      }
    }

    def get(i0: Int): Int = {
      var i = i0
      var res = 0
      while (i > 0) {
        res = math.max(res, vals(i))
        i -= i & -i
      }
      res
    }
  }

  private def lowerBound(a: java.util.ArrayList[Integer], x: Int): Int = {
    var lo = 0
    var hi = a.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a.get(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo
  }

  def getResults(queries: Array[Array[Int]]): Array[Boolean] = {
    var n = queries.length * 3
    if (n > 50000) n = 50000
    val tree = new FenwickMax(n + 1)
    val obs = new java.util.ArrayList[Integer]()
    obs.add(0)
    obs.add(n)
    queries.foreach { q =>
      if (q(0) == 1) {
        val x = q(1)
        val idx = lowerBound(obs, x)
        if (idx == obs.size() || obs.get(idx) != x) obs.add(idx, x)
      }
    }
    var i = 0
    while (i + 1 < obs.size()) {
      tree.maximize(obs.get(i + 1), obs.get(i + 1) - obs.get(i))
      i += 1
    }
    val ans = scala.collection.mutable.ArrayBuffer.empty[Boolean]
    i = queries.length - 1
    while (i >= 0) {
      val typ = queries(i)(0)
      val x = queries(i)(1)
      if (typ == 1) {
        val j = lowerBound(obs, x)
        val prev = obs.get(j - 1)
        val next = obs.get(j + 1)
        obs.remove(j)
        tree.maximize(next, next - prev)
      } else {
        val sz = queries(i)(2)
        val j = lowerBound(obs, x + 1) - 1
        val prev = obs.get(j)
        ans += (tree.get(prev) >= sz || x - prev >= sz)
      }
      i -= 1
    }
    ans.reverse.toArray
  }
}
''')

w("3162_find_the_number_of_good_pairs_i", r'''
// LeetCode 3162 - Find the Number of Good Pairs I
// https://leetcode.com/problems/find-the-number-of-good-pairs-i/

object Solution {
  def numberOfPairs(nums1: Array[Int], nums2: Array[Int], k: Int): Int = {
    var ans = 0
    nums1.foreach { x =>
      nums2.foreach { y =>
        if (x % (y * k) == 0) ans += 1
      }
    }
    ans
  }
}
''')

w("3163_string_compression_iii", r'''
// LeetCode 3163 - String Compression III
// https://leetcode.com/problems/string-compression-iii/

object Solution {
  def compressedString(word: String): String = {
    val ans = new StringBuilder
    val n = word.length
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n && word.charAt(j) == word.charAt(i)) j += 1
      var k = j - i
      while (k > 0) {
        val x = math.min(9, k)
        ans.append(('0' + x).toChar)
        ans.append(word.charAt(i))
        k -= x
      }
      i = j
    }
    ans.toString
  }
}
''')

w("3164_find_the_number_of_good_pairs_ii", r'''
// LeetCode 3164 - Find the Number of Good Pairs II
// https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

object Solution {
  def numberOfPairs(nums1: Array[Int], nums2: Array[Int], k: Int): Long = {
    val cnt1 = scala.collection.mutable.Map.empty[Int, Int]
    nums1.foreach { x =>
      if (x % k == 0) cnt1(x / k) = cnt1.getOrElse(x / k, 0) + 1
    }
    if (cnt1.isEmpty) return 0
    val cnt2 = scala.collection.mutable.Map.empty[Int, Int]
    nums2.foreach(x => cnt2(x) = cnt2.getOrElse(x, 0) + 1)
    var mx = 0
    cnt1.keys.foreach(x => mx = math.max(mx, x))
    var ans = 0L
    cnt2.foreach { case (x, v) =>
      var s = 0
      var y = x
      while (y <= mx) {
        cnt1.get(y).foreach(c => s += c)
        y += x
      }
      ans += s.toLong * v
    }
    ans
  }
}
''')

w("3165_maximum_sum_of_subsequence_with_non_adjacent_elements", r'''
// LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
// https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

object Solution {
  private class Node {
    var l = 0
    var r = 0
    var s00 = 0
    var s01 = 0
    var s10 = 0
    var s11 = 0
  }

  def maximumSumSubsequence(nums: Array[Int], queries: Array[Array[Int]]): Int = {
    val n = nums.length
    val tr = Array.fill(n * 4)(new Node())

    def build(u: Int, l: Int, r: Int): Unit = {
      tr(u).l = l
      tr(u).r = r
      if (l == r) return
      val mid = (l + r) >> 1
      build(u << 1, l, mid)
      build(u << 1 | 1, mid + 1, r)
    }

    def pushup(u: Int): Unit = {
      val left = tr(u << 1)
      val right = tr(u << 1 | 1)
      tr(u).s00 = math.max(left.s00 + right.s10, left.s01 + right.s00)
      tr(u).s01 = math.max(left.s00 + right.s11, left.s01 + right.s01)
      tr(u).s10 = math.max(left.s10 + right.s10, left.s11 + right.s00)
      tr(u).s11 = math.max(left.s10 + right.s11, left.s11 + right.s01)
    }

    def modify(u: Int, x: Int, v: Int): Unit = {
      if (tr(u).l == tr(u).r) {
        tr(u).s11 = math.max(0, v)
        return
      }
      val mid = (tr(u).l + tr(u).r) >> 1
      if (x <= mid) modify(u << 1, x, v)
      else modify(u << 1 | 1, x, v)
      pushup(u)
    }

    def query(u: Int, l: Int, r: Int): Int = {
      if (tr(u).l >= l && tr(u).r <= r) return tr(u).s11
      val mid = (tr(u).l + tr(u).r) >> 1
      var ans = 0
      if (r <= mid) ans = query(u << 1, l, r)
      if (l > mid) ans = math.max(ans, query(u << 1 | 1, l, r))
      ans
    }

    build(1, 1, n)
    var i = 0
    while (i < n) {
      modify(1, i + 1, nums(i))
      i += 1
    }
    val MOD = 1000000007
    var ans = 0
    queries.foreach { q =>
      modify(1, q(0) + 1, q(1))
      ans = (ans + query(1, 1, n)) % MOD
    }
    ans
  }
}
''')

w("3167_better_compression_of_string", r'''
// LeetCode 3167 - Better Compression of String
// https://leetcode.com/problems/better-compression-of-string/

object Solution {
  def betterCompression(compressed: String): String = {
    val cnt = new Array[Int](26)
    val n = compressed.length
    var i = 0
    while (i < n) {
      val c = compressed.charAt(i)
      var j = i + 1
      var x = 0
      var stop = false
      while (j < n && !stop) {
        val d = compressed.charAt(j)
        if (d < '0' || d > '9') stop = true
        else {
          x = x * 10 + (d - '0')
          j += 1
        }
      }
      cnt(c - 'a') += x
      i = j
    }
    val ans = new StringBuilder
    var c = 'a'
    while (c <= 'z') {
      if (cnt(c - 'a') > 0) {
        ans.append(c)
        ans.append(cnt(c - 'a'))
      }
      c = (c + 1).toChar
    }
    ans.toString
  }
}
''')

w("3168_minimum_number_of_chairs_in_a_waiting_room", r'''
// LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

object Solution {
  def minimumChairs(s: String): Int = {
    var cnt = 0
    var left = 0
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i)
      if (c == 'E') {
        if (left > 0) left -= 1
        else cnt += 1
      } else left += 1
      i += 1
    }
    cnt
  }
}
''')

w("3169_count_days_without_meetings", r'''
// LeetCode 3169 - Count Days Without Meetings
// https://leetcode.com/problems/count-days-without-meetings/

object Solution {
  def countDays(days: Int, meetings: Array[Array[Int]]): Int = {
    val ms = meetings.sortBy(_(0))
    var last = 0
    var ans = 0
    ms.foreach { e =>
      val st = e(0)
      val ed = e(1)
      if (last < st) ans += st - last - 1
      last = math.max(last, ed)
    }
    ans += days - last
    ans
  }
}
''')

w("3170_lexicographically_minimum_string_after_removing_stars", r'''
// LeetCode 3170 - Lexicographically Minimum String After Removing Stars
// https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

object Solution {
  def clearStars(s: String): String = {
    val g = Array.fill(26)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val n = s.length
    val rem = new Array[Boolean](n)
    var i = 0
    while (i < n) {
      if (s.charAt(i) == '*') {
        rem(i) = true
        var j = 0
        var found = false
        while (j < 26 && !found) {
          if (g(j).nonEmpty) {
            rem(g(j).last) = true
            g(j).remove(g(j).length - 1)
            found = true
          }
          j += 1
        }
      } else {
        g(s.charAt(i) - 'a') += i
      }
      i += 1
    }
    val ans = new StringBuilder
    i = 0
    while (i < n) {
      if (!rem(i)) ans.append(s.charAt(i))
      i += 1
    }
    ans.toString
  }
}
''')
