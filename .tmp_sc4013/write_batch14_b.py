#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("3086_minimum_moves_to_pick_k_ones", r'''
// LeetCode 3086 - Minimum Moves to Pick K Ones
// https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

object Solution {
  def minimumMoves(nums: Array[Int], k: Int, maxChanges: Int): Long = {
    val n = nums.length
    val cnt = new Array[Int](n + 1)
    val s = new Array[Int](n + 1)
    var i = 1
    while (i <= n) {
      cnt(i) = cnt(i - 1) + nums(i - 1)
      s(i) = s(i - 1) + i * nums(i - 1)
      i += 1
    }
    var ans = Long.MaxValue
    i = 1
    while (i <= n) {
      var t = 0L
      var need = k - nums(i - 1)
      Array(i - 1, i + 1).foreach { j =>
        if (need > 0 && 1 <= j && j <= n && nums(j - 1) == 1) {
          need -= 1
          t += 1
        }
      }
      val c = math.min(need, maxChanges)
      need -= c
      t += c * 2L
      if (need <= 0) {
        ans = math.min(ans, t)
      } else {
        var l = 2
        var r = math.max(i - 1, n - i)
        while (l <= r) {
          val mid = (l + r) >> 1
          val l1 = math.max(1, i - mid)
          val r1 = math.max(0, i - 2)
          val l2 = math.min(n + 1, i + 2)
          val r2 = math.min(n, i + mid)
          val c1 = cnt(r1) - cnt(l1 - 1)
          val c2 = cnt(r2) - cnt(l2 - 1)
          if (c1 + c2 >= need) {
            val t1 = c1.toLong * i - (s(r1) - s(l1 - 1))
            val t2 = s(r2) - s(l2 - 1) - c2.toLong * i
            ans = math.min(ans, t + t1 + t2)
            r = mid - 1
          } else {
            l = mid + 1
          }
        }
      }
      i += 1
    }
    ans
  }
}
''')

w("3088_make_string_anti_palindrome", r'''
// LeetCode 3088 - Make String Anti-palindrome
// https://leetcode.com/problems/make-string-anti-palindrome/

object Solution {
  def makeAntiPalindrome(s: String): String = {
    val arr = s.toCharArray.sorted
    val n = arr.length
    val m = n / 2
    if (arr(m) == arr(m - 1)) {
      var i = m
      while (i < n && arr(i) == arr(i - 1)) i += 1
      var j = m
      while (j < n && arr(j) == arr(n - j - 1)) {
        if (i >= n) return "-1"
        val tmp = arr(i)
        arr(i) = arr(j)
        arr(j) = tmp
        i += 1
        j += 1
      }
    }
    new String(arr)
  }
}
''')

w("3090_maximum_length_substring_with_two_occurrences", r'''
// LeetCode 3090 - Maximum Length Substring With Two Occurrences
// https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

object Solution {
  def maximumLengthSubstring(s: String): Int = {
    var l = 0
    var ans = 0
    val cnt = new Array[Int](26)
    var r = 0
    while (r < s.length) {
      val idx = s.charAt(r) - 'a'
      cnt(idx) += 1
      while (cnt(idx) > 2) {
        cnt(s.charAt(l) - 'a') -= 1
        l += 1
      }
      ans = math.max(ans, r - l + 1)
      r += 1
    }
    ans
  }
}
''')

w("3091_apply_operations_to_make_sum_of_array_greater_than_or_equal_to_k", r'''
// LeetCode 3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
// https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

object Solution {
  def minOperations(k: Int): Int = {
    var ans = k
    var a = 0
    while (a < k) {
      val x = a + 1
      val b = (k + x - 1) / x - 1
      ans = math.min(ans, a + b)
      a += 1
    }
    ans
  }
}
''')

w("3092_most_frequent_ids", r'''
// LeetCode 3092 - Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/

object Solution {
  def mostFrequentIDs(nums: Array[Int], freq: Array[Int]): Array[Long] = {
    val n = nums.length
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    val lazyMap = scala.collection.mutable.Map.empty[Int, Int]
    val ans = new Array[Long](n)
    val pq = new java.util.PriorityQueue[Integer]((a: Integer, b: Integer) => b - a)
    var i = 0
    while (i < n) {
      val x = nums(i)
      val f = freq(i)
      val old = cnt.getOrElse(x, 0)
      lazyMap(old) = lazyMap.getOrElse(old, 0) + 1
      val neu = old + f
      cnt(x) = neu
      pq.offer(neu)
      while (!pq.isEmpty && lazyMap.getOrElse(pq.peek(), 0) > 0) {
        val top = pq.poll()
        lazyMap(top) = lazyMap(top) - 1
      }
      if (!pq.isEmpty) ans(i) = pq.peek().toLong
      i += 1
    }
    ans
  }
}
''')

w("3093_longest_common_suffix_queries", r'''
// LeetCode 3093 - Longest Common Suffix Queries
// https://leetcode.com/problems/longest-common-suffix-queries/

object Solution {
  private val INF = 1 << 30

  private class Trie {
    val children: Array[Trie] = new Array[Trie](26)
    var length: Int = INF
    var idx: Int = INF
  }

  def stringIndices(wordsContainer: Array[String], wordsQuery: Array[String]): Array[Int] = {
    val trie = new Trie()
    var i = 0
    while (i < wordsContainer.length) {
      insert(trie, wordsContainer(i), i)
      i += 1
    }
    val ans = new Array[Int](wordsQuery.length)
    i = 0
    while (i < wordsQuery.length) {
      ans(i) = query(trie, wordsQuery(i))
      i += 1
    }
    ans
  }

  private def insert(t: Trie, w: String, i: Int): Unit = {
    var node = t
    if (node.length > w.length) {
      node.length = w.length
      node.idx = i
    }
    var k = w.length - 1
    while (k >= 0) {
      val id = w.charAt(k) - 'a'
      if (node.children(id) == null) node.children(id) = new Trie()
      node = node.children(id)
      if (node.length > w.length) {
        node.length = w.length
        node.idx = i
      }
      k -= 1
    }
  }

  private def query(t: Trie, w: String): Int = {
    var node = t
    var k = w.length - 1
    while (k >= 0) {
      val id = w.charAt(k) - 'a'
      if (node.children(id) == null) return node.idx
      node = node.children(id)
      k -= 1
    }
    node.idx
  }
}
''')

w("3094_guess_the_number_using_bitwise_questions_ii", r'''
// LeetCode 3094 - Guess the Number Using Bitwise Questions II
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

object Solution {
  def commonBits(num: Int): Int = throw new NotImplementedError()

  def findNumber(): Int = {
    var n = 0
    var i = 0
    while (i < 32) {
      val count1 = commonBits(1 << i)
      val count2 = commonBits(1 << i)
      if (count1 > count2) n |= 1 << i
      i += 1
    }
    n
  }
}
''')

w("3095_shortest_subarray_with_or_at_least_k_i", r'''
// LeetCode 3095 - Shortest Subarray With OR at Least K I
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/

object Solution {
  def minimumSubarrayLength(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val cnt = new Array[Int](32)
    var ans = n + 1
    var s = 0
    var i = 0
    var j = 0
    while (j < n) {
      val x = nums(j)
      s |= x
      var h = 0
      while (h < 32) {
        if (((x >> h) & 1) != 0) cnt(h) += 1
        h += 1
      }
      while (s >= k && i <= j) {
        ans = math.min(ans, j - i + 1)
        h = 0
        while (h < 32) {
          if (((nums(i) >> h) & 1) != 0) {
            cnt(h) -= 1
            if (cnt(h) == 0) s ^= 1 << h
          }
          h += 1
        }
        i += 1
      }
      j += 1
    }
    if (ans == n + 1) -1 else ans
  }
}
''')

w("3096_minimum_levels_to_gain_more_points", r'''
// LeetCode 3096 - Minimum Levels to Gain More Points
// https://leetcode.com/problems/minimum-levels-to-gain-more-points/

object Solution {
  def minimumLevels(possible: Array[Int]): Int = {
    var s = 0
    possible.foreach(x => s += (if (x == 0) -1 else x))
    var t = 0
    var i = 0
    while (i + 1 < possible.length) {
      val x = if (possible(i) == 0) -1 else possible(i)
      t += x
      if (t > s - t) return i + 1
      i += 1
    }
    -1
  }
}
''')

w("3097_shortest_subarray_with_or_at_least_k_ii", r'''
// LeetCode 3097 - Shortest Subarray With OR at Least K II
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

object Solution {
  def minimumSubarrayLength(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val cnt = new Array[Int](32)
    var ans = n + 1
    var s = 0
    var i = 0
    var j = 0
    while (j < n) {
      val x = nums(j)
      s |= x
      var h = 0
      while (h < 32) {
        if (((x >> h) & 1) != 0) cnt(h) += 1
        h += 1
      }
      while (s >= k && i <= j) {
        ans = math.min(ans, j - i + 1)
        h = 0
        while (h < 32) {
          if (((nums(i) >> h) & 1) != 0) {
            cnt(h) -= 1
            if (cnt(h) == 0) s ^= 1 << h
          }
          h += 1
        }
        i += 1
      }
      j += 1
    }
    if (ans == n + 1) -1 else ans
  }
}
''')

w("3098_find_the_sum_of_subsequence_powers", r'''
// LeetCode 3098 - Find the Sum of Subsequence Powers
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

object Solution {
  private val MOD = 1000000007

  def sumOfPowers(nums0: Array[Int], k: Int): Int = {
    val nums = nums0.sorted
    val n = nums.length
    val f = scala.collection.mutable.Map.empty[Long, Int]

    def dfs(i: Int, j: Int, kk: Int, mi: Int): Int = {
      if (i >= n) return if (kk == 0) mi else 0
      if (n - i < kk) return 0
      val key = (mi.toLong << 18) | (i.toLong << 12) | (j.toLong << 6) | kk
      f.get(key) match {
        case Some(cached) => cached
        case None =>
          var ans = dfs(i + 1, j, kk, mi)
          if (j == n) ans = (ans + dfs(i + 1, i, kk - 1, mi)) % MOD
          else ans = (ans + dfs(i + 1, i, kk - 1, math.min(mi, nums(i) - nums(j)))) % MOD
          f(key) = ans
          ans
      }
    }

    dfs(0, n, k, Int.MaxValue)
  }
}
''')

w("3099_harshad_number", r'''
// LeetCode 3099 - Harshad Number
// https://leetcode.com/problems/harshad-number/

object Solution {
  def sumOfTheDigitsOfHarshadNumber(x: Int): Int = {
    var s = 0
    var y = x
    while (y > 0) {
      s += y % 10
      y /= 10
    }
    if (x % s == 0) s else -1
  }
}
''')

w("3100_water_bottles_ii", r'''
// LeetCode 3100 - Water Bottles II
// https://leetcode.com/problems/water-bottles-ii/

object Solution {
  def maxBottlesDrunk(numBottles0: Int, numExchange0: Int): Int = {
    var numBottles = numBottles0
    var numExchange = numExchange0
    var ans = numBottles
    while (numBottles >= numExchange) {
      numBottles -= numExchange
      numExchange += 1
      ans += 1
      numBottles += 1
    }
    ans
  }
}
''')

w("3101_count_alternating_subarrays", r'''
// LeetCode 3101 - Count Alternating Subarrays
// https://leetcode.com/problems/count-alternating-subarrays/

object Solution {
  def countAlternatingSubarrays(nums: Array[Int]): Long = {
    var ans = 1L
    var s = 1L
    var i = 1
    while (i < nums.length) {
      if (nums(i) != nums(i - 1)) s += 1
      else s = 1
      ans += s
      i += 1
    }
    ans
  }
}
''')

w("3102_minimize_manhattan_distances", r'''
// LeetCode 3102 - Minimize Manhattan Distances
// https://leetcode.com/problems/minimize-manhattan-distances/

object Solution {
  def minimumDistance(points: Array[Array[Int]]): Int = {
    val st1 = new java.util.TreeMap[Integer, Integer]()
    val st2 = new java.util.TreeMap[Integer, Integer]()

    def merge(st: java.util.TreeMap[Integer, Integer], x: Int, v: Int): Unit = {
      val nv = st.getOrDefault(x, 0) + v
      if (nv == 0) st.remove(x)
      else st.put(x, nv)
    }

    points.foreach { p =>
      merge(st1, p(0) + p(1), 1)
      merge(st2, p(0) - p(1), 1)
    }
    var ans = Int.MaxValue
    points.foreach { p =>
      val x = p(0)
      val y = p(1)
      merge(st1, x + y, -1)
      merge(st2, x - y, -1)
      ans = math.min(ans, math.max(st1.lastKey() - st1.firstKey(), st2.lastKey() - st2.firstKey()))
      merge(st1, x + y, 1)
      merge(st2, x - y, 1)
    }
    ans
  }
}
''')

w("3104_find_longest_self_contained_substring", r'''
// LeetCode 3104 - Find Longest Self-Contained Substring
// https://leetcode.com/problems/find-longest-self-contained-substring/

object Solution {
  def maxSubstringLength(s: String): Int = {
    val first = Array.fill(26)(-1)
    val last = new Array[Int](26)
    val n = s.length
    var i = 0
    while (i < n) {
      val j = s.charAt(i) - 'a'
      if (first(j) == -1) first(j) = i
      last(j) = i
      i += 1
    }
    var ans = -1
    var k = 0
    while (k < 26) {
      i = first(k)
      if (i != -1) {
        var mx = last(k)
        var j = i
        var broken = false
        while (j < n && !broken) {
          val a = first(s.charAt(j) - 'a')
          val b = last(s.charAt(j) - 'a')
          if (a < i) broken = true
          else {
            mx = math.max(mx, b)
            if (mx == j && j - i + 1 < n) ans = math.max(ans, j - i + 1)
            j += 1
          }
        }
      }
      k += 1
    }
    ans
  }
}
''')

w("3105_longest_strictly_increasing_or_strictly_decreasing_subarray", r'''
// LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

object Solution {
  def longestMonotonicSubarray(nums: Array[Int]): Int = {
    var ans = 1
    var t = 1
    var i = 1
    while (i < nums.length) {
      if (nums(i - 1) < nums(i)) {
        t += 1
        ans = math.max(ans, t)
      } else t = 1
      i += 1
    }
    t = 1
    i = 1
    while (i < nums.length) {
      if (nums(i - 1) > nums(i)) {
        t += 1
        ans = math.max(ans, t)
      } else t = 1
      i += 1
    }
    ans
  }
}
''')

w("3106_lexicographically_smallest_string_after_operations_with_constraint", r'''
// LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
// https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

object Solution {
  def getSmallestString(s: String, k0: Int): String = {
    var k = k0
    val arr = s.toCharArray
    var i = 0
    while (i < arr.length) {
      val c1 = arr(i)
      var c2 = 'a'
      var found = false
      while (c2 < c1 && !found) {
        val d = math.min(c1 - c2, 26 - (c1 - c2))
        if (d <= k) {
          arr(i) = c2
          k -= d
          found = true
        }
        c2 = (c2 + 1).toChar
      }
      i += 1
    }
    new String(arr)
  }
}
''')

w("3107_minimum_operations_to_make_median_of_array_equal_to_k", r'''
// LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

object Solution {
  def minOperationsToMakeMedianK(nums: Array[Int], k: Int): Long = {
    val a = nums.sorted
    val n = a.length
    val m = n >> 1
    var ans = math.abs(a(m) - k).toLong
    if (a(m) > k) {
      var i = m - 1
      while (i >= 0 && a(i) > k) {
        ans += a(i) - k
        i -= 1
      }
    } else {
      var i = m + 1
      while (i < n && a(i) < k) {
        ans += k - a(i)
        i += 1
      }
    }
    ans
  }
}
''')

w("3108_minimum_cost_walk_in_weighted_graph", r'''
// LeetCode 3108 - Minimum Cost Walk in Weighted Graph
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

object Solution {
  private class UnionFind(n: Int) {
    val p: Array[Int] = Array.tabulate(n)(i => i)
    val size: Array[Int] = Array.fill(n)(1)

    def find(x: Int): Int = {
      if (p(x) != x) p(x) = find(p(x))
      p(x)
    }

    def unite(a: Int, b: Int): Unit = {
      val pa = find(a)
      val pb = find(b)
      if (pa == pb) return
      if (size(pa) > size(pb)) {
        p(pb) = pa
        size(pa) += size(pb)
      } else {
        p(pa) = pb
        size(pb) += size(pa)
      }
    }
  }

  def minimumCost(n: Int, edges: Array[Array[Int]], query: Array[Array[Int]]): Array[Int] = {
    val uf = new UnionFind(n)
    val g = Array.fill(n)(-1)
    edges.foreach(e => uf.unite(e(0), e(1)))
    edges.foreach { e =>
      val root = uf.find(e(0))
      g(root) &= e(2)
    }
    val ans = new Array[Int](query.length)
    var i = 0
    while (i < query.length) {
      val u = query(i)(0)
      val v = query(i)(1)
      if (u == v) ans(i) = 0
      else {
        val a = uf.find(u)
        val b = uf.find(v)
        ans(i) = if (a == b) g(a) else -1
      }
      i += 1
    }
    ans
  }
}
''')

w("3109_find_the_index_of_permutation", r'''
// LeetCode 3109 - Find the Index of Permutation
// https://leetcode.com/problems/find-the-index-of-permutation/

object Solution {
  private class BIT(n_ : Int) {
    val n: Int = n_
    val c: Array[Int] = new Array[Int](n_ + 1)
    def update(x0: Int, delta: Int): Unit = {
      var x = x0
      while (x <= n) {
        c(x) += delta
        x += x & -x
      }
    }
    def query(x0: Int): Int = {
      var x = x0
      var s = 0
      while (x > 0) {
        s += c(x)
        x -= x & -x
      }
      s
    }
  }

  def getPermutationIndex(perm: Array[Int]): Int = {
    val MOD = 1000000007
    val n = perm.length
    val tree = new BIT(n + 1)
    val f = new Array[Int](n)
    f(0) = 1
    var i = 1
    while (i < n) {
      f(i) = ((f(i - 1).toLong * i) % MOD).toInt
      i += 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      val x = perm(i)
      val cnt = x - 1 - tree.query(x)
      ans = (ans + cnt.toLong * f(n - 1 - i)) % MOD
      tree.update(x, 1)
      i += 1
    }
    ans.toInt
  }
}
''')

w("3110_score_of_a_string", r'''
// LeetCode 3110 - Score of a String
// https://leetcode.com/problems/score-of-a-string/

object Solution {
  def scoreOfString(s: String): Int = {
    var ans = 0
    var i = 1
    while (i < s.length) {
      ans += math.abs(s.charAt(i - 1) - s.charAt(i))
      i += 1
    }
    ans
  }
}
''')

w("3111_minimum_rectangles_to_cover_points", r'''
// LeetCode 3111 - Minimum Rectangles to Cover Points
// https://leetcode.com/problems/minimum-rectangles-to-cover-points/

object Solution {
  def minRectanglesToCoverPoints(points: Array[Array[Int]], w: Int): Int = {
    val pts = points.sortBy(_(0))
    var ans = 0
    var x1 = -1
    pts.foreach { p =>
      if (p(0) > x1) {
        ans += 1
        x1 = p(0) + w
      }
    }
    ans
  }
}
''')

w("3112_minimum_time_to_visit_disappearing_nodes", r'''
// LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
// https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

object Solution {
  def minimumTime(n: Int, edges: Array[Array[Int]], disappear: Array[Int]): Array[Int] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Array[Int]])
    edges.foreach { e =>
      g(e(0)) += Array(e(1), e(2))
      g(e(1)) += Array(e(0), e(2))
    }
    val INF = 1 << 30
    val dist = Array.fill(n)(INF)
    dist(0) = 0
    val pq = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) => a(0) - b(0))
    pq.offer(Array(0, 0))
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val du = cur(0)
      val u = cur(1)
      if (du <= dist(u)) {
        g(u).foreach { e =>
          val v = e(0)
          val w = e(1)
          if (dist(v) > dist(u) + w && dist(u) + w < disappear(v)) {
            dist(v) = dist(u) + w
            pq.offer(Array(dist(v), v))
          }
        }
      }
    }
    Array.tabulate(n)(i => if (dist(i) < disappear(i)) dist(i) else -1)
  }
}
''')

w("3113_find_the_number_of_subarrays_where_boundary_elements_are_maximum", r'''
// LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
// https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

object Solution {
  def numberOfSubarrays(nums: Array[Int]): Long = {
    val stk = new java.util.ArrayDeque[Array[Int]]()
    var ans = 0L
    nums.foreach { x =>
      while (!stk.isEmpty && stk.peekLast()(0) < x) stk.pollLast()
      if (stk.isEmpty || stk.peekLast()(0) > x) stk.addLast(Array(x, 1))
      else stk.peekLast()(1) += 1
      ans += stk.peekLast()(1)
    }
    ans
  }
}
''')
