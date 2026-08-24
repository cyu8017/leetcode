#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("2488_count_subarrays_with_median_k", r'''
// LeetCode 2488 - Count Subarrays With Median K
// https://leetcode.com/problems/count-subarrays-with-median-k/

object Solution {
  def countSubarrays(nums: Array[Int], k: Int): Int = {
    var pos = 0
    var i = 0
    while (i < nums.length) {
      if (nums(i) == k) { pos = i; i = nums.length }
      else i += 1
    }
    val bal = scala.collection.mutable.Map[Int, Int](0 -> 1)
    var cur = 0
    i = pos - 1
    while (i >= 0) {
      cur += (if (nums(i) < k) -1 else 1)
      bal(cur) = bal.getOrElse(cur, 0) + 1
      i -= 1
    }
    var ans = bal.getOrElse(0, 0) + bal.getOrElse(1, 0)
    cur = 0
    i = pos + 1
    while (i < nums.length) {
      cur += (if (nums(i) < k) -1 else 1)
      ans += bal.getOrElse(-cur, 0) + bal.getOrElse(1 - cur, 0)
      i += 1
    }
    ans
  }
}
''')

w("2489_number_of_substrings_with_fixed_ratio", r'''
// LeetCode 2489 - Number of Substrings With Fixed Ratio
// https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

object Solution {
  def fixedRatio(s: String, num1: Int, num2: Int): Long = {
    val pref = scala.collection.mutable.Map[Long, Int](0L -> 1)
    var zeros = 0
    var ones = 0
    var ans = 0L
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == '0') zeros += 1 else ones += 1
      val key = zeros.toLong * num2 - ones.toLong * num1
      ans += pref.getOrElse(key, 0)
      pref(key) = pref.getOrElse(key, 0) + 1
      i += 1
    }
    ans
  }
}
''')

w("2490_circular_sentence", r'''
// LeetCode 2490 - Circular Sentence
// https://leetcode.com/problems/circular-sentence/

object Solution {
  def isCircularSentence(sentence: String): Boolean = {
    val n = sentence.length
    if (sentence.charAt(0) != sentence.charAt(n - 1)) return false
    var i = 0
    while (i < n) {
      if (sentence.charAt(i) == ' ' && sentence.charAt(i - 1) != sentence.charAt(i + 1)) return false
      i += 1
    }
    true
  }
}
''')

w("2491_divide_players_into_teams_of_equal_skill", r'''
// LeetCode 2491 - Divide Players Into Teams of Equal Skill
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

object Solution {
  def dividePlayers(skill: Array[Int]): Long = {
    scala.util.Sorting.quickSort(skill)
    val n = skill.length
    val target = skill(0) + skill(n - 1)
    var chem = 0L
    var i = 0
    while (i < n / 2) {
      if (skill(i) + skill(n - 1 - i) != target) return -1
      chem += skill(i).toLong * skill(n - 1 - i)
      i += 1
    }
    chem
  }
}
''')

w("2492_minimum_score_of_a_path_between_two_cities", r'''
// LeetCode 2492 - Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

object Solution {
  def minScore(n: Int, roads: Array[Array[Int]]): Int = {
    val g = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    roads.foreach { r =>
      g(r(0)) += ((r(1), r(2)))
      g(r(1)) += ((r(0), r(2)))
    }
    val vis = new Array[Boolean](n + 1)
    var ans = 1 << 30
    val q = scala.collection.mutable.Queue[Int]()
    q.enqueue(1)
    vis(1) = true
    while (q.nonEmpty) {
      val u = q.dequeue()
      g(u).foreach { case (v, w) =>
        if (w < ans) ans = w
        if (!vis(v)) {
          vis(v) = true
          q.enqueue(v)
        }
      }
    }
    ans
  }
}
''')

w("2493_divide_nodes_into_the_maximum_number_of_groups", r'''
// LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

object Solution {
  def magnificentSets(n: Int, edges: Array[Array[Int]]): Int = {
    val g = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }

    def bfsDepth(start: Int): Int = {
      val dist = Array.fill(n + 1)(-1)
      val q = scala.collection.mutable.Queue[Int]()
      q.enqueue(start)
      dist(start) = 1
      var best = 1
      while (q.nonEmpty) {
        val u = q.dequeue()
        if (dist(u) > best) best = dist(u)
        g(u).foreach { v =>
          if (dist(v) == -1) {
            dist(v) = dist(u) + 1
            q.enqueue(v)
          }
        }
      }
      best
    }

    val color = Array.fill(n + 1)(-1)
    val components = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.ArrayBuffer[Int]]
    var i = 1
    while (i <= n) {
      if (color(i) == -1) {
        val comp = scala.collection.mutable.ArrayBuffer.empty[Int]
        val q = scala.collection.mutable.Queue[Int]()
        q.enqueue(i)
        color(i) = 0
        var bipartite = true
        while (q.nonEmpty) {
          val u = q.dequeue()
          comp += u
          g(u).foreach { v =>
            if (color(v) == -1) {
              color(v) = color(u) ^ 1
              q.enqueue(v)
            } else if (color(v) == color(u)) {
              bipartite = false
            }
          }
        }
        if (!bipartite) return -1
        components += comp
      }
      i += 1
    }
    var ans = 0
    components.foreach { comp =>
      var best = 0
      comp.foreach { u =>
        val d = bfsDepth(u)
        if (d > best) best = d
      }
      ans += best
    }
    ans
  }
}
''')

w("2495_number_of_subarrays_having_even_product", r'''
// LeetCode 2495 - Number of Subarrays Having Even Product
// https://leetcode.com/problems/number-of-subarrays-having-even-product/

object Solution {
  def evenProduct(nums: Array[Int]): Long = {
    val n = nums.length.toLong
    val total = n * (n + 1) / 2
    var oddLen = 0L
    var odd = 0L
    var i = 0
    while (i < nums.length) {
      if (nums(i) % 2 == 1) {
        odd += 1
        oddLen += odd
      } else {
        odd = 0
      }
      i += 1
    }
    total - oddLen
  }
}
''')

w("2496_maximum_value_of_a_string_in_an_array", r'''
// LeetCode 2496 - Maximum Value of a String in an Array
// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

object Solution {
  def maximumValue(strs: Array[String]): Int = {
    var ans = 0
    var si = 0
    while (si < strs.length) {
      val s = strs(si)
      var allDigit = true
      var value = 0
      var i = 0
      while (i < s.length && allDigit) {
        val c = s.charAt(i)
        if (c < '0' || c > '9') allDigit = false
        else value = value * 10 + (c - '0')
        i += 1
      }
      if (!allDigit) value = s.length
      if (value > ans) ans = value
      si += 1
    }
    ans
  }
}
''')

w("2497_maximum_star_sum_of_a_graph", r'''
// LeetCode 2497 - Maximum Star Sum of a Graph
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

object Solution {
  def maxStarSum(vals: Array[Int], edges: Array[Array[Int]], k: Int): Int = {
    val n = vals.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    var ans = vals(0)
    var i = 0
    while (i < n) {
      val neigh = scala.collection.mutable.ArrayBuffer.empty[Int]
      g(i).foreach { v => if (vals(v) > 0) neigh += vals(v) }
      val arr = neigh.toArray
      scala.util.Sorting.quickSort(arr)
      var sum = vals(i)
      var j = arr.length - 1
      var taken = 0
      while (j >= 0 && taken < k) {
        sum += arr(j)
        taken += 1
        j -= 1
      }
      if (sum > ans) ans = sum
      i += 1
    }
    ans
  }
}
''')

w("2498_frog_jump_ii", r'''
// LeetCode 2498 - Frog Jump II
// https://leetcode.com/problems/frog-jump-ii/

object Solution {
  def maxJump(stones: Array[Int]): Int = {
    var ans = stones(1) - stones(0)
    var i = 2
    while (i < stones.length) {
      val diff = stones(i) - stones(i - 2)
      if (diff > ans) ans = diff
      i += 1
    }
    ans
  }
}
''')

w("2499_minimum_total_cost_to_make_arrays_unequal", r'''
// LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

object Solution {
  def minimumTotalCost(nums1: Array[Int], nums2: Array[Int]): Long = {
    val n = nums1.length
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0L
    var same = 0
    var i = 0
    while (i < n) {
      if (nums1(i) == nums2(i)) {
        same += 1
        freq(nums1(i)) = freq.getOrElse(nums1(i), 0) + 1
        ans += i
      }
      i += 1
    }
    var maxFreq = 0
    var maxVal = 0
    freq.foreach { case (k, v) =>
      if (v > maxFreq) {
        maxFreq = v
        maxVal = k
      }
    }
    var need = maxFreq * 2 - same
    if (need <= 0) return ans
    i = 0
    while (i < n && need > 0) {
      if (nums1(i) != nums2(i) && nums1(i) != maxVal && nums2(i) != maxVal) {
        ans += i
        need -= 1
      }
      i += 1
    }
    if (need > 0) -1 else ans
  }
}
''')

w("2500_delete_greatest_value_in_each_row", r'''
// LeetCode 2500 - Delete Greatest Value in Each Row
// https://leetcode.com/problems/delete-greatest-value-in-each-row/

object Solution {
  def deleteGreatestValue(grid: Array[Array[Int]]): Int = {
    grid.foreach(row => scala.util.Sorting.quickSort(row))
    var ans = 0
    val n = grid(0).length
    var c = 0
    while (c < n) {
      var mx = 0
      var r = 0
      while (r < grid.length) {
        if (grid(r)(c) > mx) mx = grid(r)(c)
        r += 1
      }
      ans += mx
      c += 1
    }
    ans
  }
}
''')

w("2501_longest_square_streak_in_an_array", r'''
// LeetCode 2501 - Longest Square Streak in an Array
// https://leetcode.com/problems/longest-square-streak-in-an-array/

object Solution {
  def longestSquareStreak(nums: Array[Int]): Int = {
    val set = scala.collection.mutable.HashSet.empty[Long]
    var i = 0
    while (i < nums.length) {
      set += nums(i).toLong
      i += 1
    }
    var best = -1
    i = 0
    while (i < nums.length) {
      var cur = nums(i).toLong
      if (set.contains(cur)) {
        var length = 0
        var cont = true
        while (cont && set.contains(cur)) {
          length += 1
          set -= cur
          if (cur > 100000) cont = false
          else cur = cur * cur
        }
        if (length >= 2 && length > best) best = length
      }
      i += 1
    }
    best
  }
}
''')

w("2502_design_memory_allocator", r'''
// LeetCode 2502 - Design Memory Allocator
// https://leetcode.com/problems/design-memory-allocator/

class Allocator(_n: Int) {
  private val mem = new Array[Int](_n)

  def allocate(size: Int, mID: Int): Int = {
    var freeCnt = 0
    var i = 0
    while (i < mem.length) {
      if (mem(i) == 0) {
        freeCnt += 1
        if (freeCnt == size) {
          val start = i - size + 1
          var j = start
          while (j <= i) {
            mem(j) = mID
            j += 1
          }
          return start
        }
      } else {
        freeCnt = 0
      }
      i += 1
    }
    -1
  }

  def freeMemory(mID: Int): Int = {
    var cnt = 0
    var i = 0
    while (i < mem.length) {
      if (mem(i) == mID) {
        mem(i) = 0
        cnt += 1
      }
      i += 1
    }
    cnt
  }
}
''')

w("2503_maximum_number_of_points_from_grid_queries", r'''
// LeetCode 2503 - Maximum Number of Points From Grid Queries
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

object Solution {
  def maxPoints(grid: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
    val m = grid.length
    val n = grid(0).length
    val order = Array.tabulate(queries.length)(identity)
    scala.util.Sorting.stableSort(order, (a: Int, b: Int) => queries(a) < queries(b) || (queries(a) == queries(b) && a < b))
    val ans = new Array[Int](queries.length)
    val visited = Array.ofDim[Boolean](m, n)
    implicit val ord: Ordering[(Int, Int, Int)] = Ordering.by[(Int, Int, Int), Int](_._1).reverse
    val pq = scala.collection.mutable.PriorityQueue.empty[(Int, Int, Int)]
    pq.enqueue((grid(0)(0), 0, 0))
    visited(0)(0) = true
    var points = 0
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    var oi = 0
    while (oi < order.length) {
      val qi = order(oi)
      val q = queries(qi)
      while (pq.nonEmpty && pq.head._1 < q) {
        val (_, r, c) = pq.dequeue()
        points += 1
        var d = 0
        while (d < 4) {
          val nr = r + dirs(d)._1
          val nc = c + dirs(d)._2
          if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited(nr)(nc)) {
            visited(nr)(nc) = true
            pq.enqueue((grid(nr)(nc), nr, nc))
          }
          d += 1
        }
      }
      ans(qi) = points
      oi += 1
    }
    ans
  }
}
''')

w("2505_bitwise_or_of_all_subsequence_sums", r'''
// LeetCode 2505 - Bitwise OR of All Subsequence Sums
// https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

object Solution {
  def subsequenceSumOr(nums: Array[Int]): Long = {
    var ans = 0L
    var prefix = 0L
    var i = 0
    while (i < nums.length) {
      prefix += nums(i)
      ans |= nums(i).toLong | prefix
      i += 1
    }
    ans
  }
}
''')

w("2506_count_pairs_of_similar_strings", r'''
// LeetCode 2506 - Count Pairs Of Similar Strings
// https://leetcode.com/problems/count-pairs-of-similar-strings/

object Solution {
  def similarPairs(words: Array[String]): Int = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0
    var wi = 0
    while (wi < words.length) {
      var mask = 0
      val w = words(wi)
      var i = 0
      while (i < w.length) {
        mask |= 1 << (w.charAt(i) - 'a')
        i += 1
      }
      ans += freq.getOrElse(mask, 0)
      freq(mask) = freq.getOrElse(mask, 0) + 1
      wi += 1
    }
    ans
  }
}
''')

w("2507_smallest_value_after_replacing_with_sum_of_prime_factors", r'''
// LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
// https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

object Solution {
  def smallestValue(n0: Int): Int = {
    def sumPrimeFactors(x0: Int): Int = {
      var x = x0
      var s = 0
      var i = 2
      while (i.toLong * i <= x) {
        while (x % i == 0) {
          s += i
          x /= i
        }
        i += 1
      }
      if (x > 1) s += x
      s
    }
    var n = n0
    while (true) {
      val s = sumPrimeFactors(n)
      if (s == n) return n
      n = s
    }
    n
  }
}
''')

w("2508_add_edges_to_make_degrees_of_all_nodes_even", r'''
// LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

object Solution {
  def isPossible(n: Int, edges: List[List[Int]]): Boolean = {
    val deg = new Array[Int](n + 1)
    val adj = Array.fill(n + 1)(scala.collection.mutable.HashSet.empty[Int])
    edges.foreach { e =>
      val u = e(0)
      val v = e(1)
      deg(u) += 1
      deg(v) += 1
      adj(u) += v
      adj(v) += u
    }
    val odd = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 1
    while (i <= n) {
      if (deg(i) % 2 == 1) odd += i
      i += 1
    }
    if (odd.isEmpty) return true
    if (odd.length == 2) {
      val a = odd(0)
      val b = odd(1)
      if (!adj(a).contains(b)) return true
      i = 1
      while (i <= n) {
        if (i != a && i != b && !adj(a).contains(i) && !adj(b).contains(i)) return true
        i += 1
      }
      return false
    }
    if (odd.length == 4) {
      val a = odd(0)
      val b = odd(1)
      val c = odd(2)
      val d = odd(3)
      return (!adj(a).contains(b) && !adj(c).contains(d)) ||
        (!adj(a).contains(c) && !adj(b).contains(d)) ||
        (!adj(a).contains(d) && !adj(b).contains(c))
    }
    false
  }
}
''')

w("2509_cycle_length_queries_in_a_tree", r'''
// LeetCode 2509 - Cycle Length Queries in a Tree
// https://leetcode.com/problems/cycle-length-queries-in-a-tree/

object Solution {
  def cycleLengthQueries(n: Int, queries: Array[Array[Int]]): Array[Int] = {
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      var a = queries(i)(0)
      var b = queries(i)(1)
      var steps = 0
      while (a != b) {
        if (a > b) a /= 2 else b /= 2
        steps += 1
      }
      ans(i) = steps + 1
      i += 1
    }
    ans
  }
}
''')

w("2510_check_if_there_is_a_path_with_equal_number_of_0s_and_1s", r'''
// LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
// https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

object Solution {
  def isThereAPath(grid: Array[Array[Int]]): Boolean = {
    val m = grid.length
    val n = grid(0).length
    if ((m + n - 1) % 2 != 0) return false
    val target = (m + n - 1) / 2
    val memo = scala.collection.mutable.Map.empty[Long, Boolean]

    def key(r: Int, c: Int, bal: Int): Long = {
      (r.toLong << 40) | (c.toLong << 20) | (bal & 0xfffffL)
    }

    def dfs(r: Int, c: Int, bal0: Int): Boolean = {
      if (r >= m || c >= n) return false
      val bal = bal0 + grid(r)(c)
      if (bal > target || bal + (m - 1 - r) + (n - 1 - c) < target) return false
      if (r == m - 1 && c == n - 1) return bal == target
      val k = key(r, c, bal)
      memo.get(k) match {
        case Some(cached) => cached
        case None =>
          val ok = dfs(r + 1, c, bal) || dfs(r, c + 1, bal)
          memo(k) = ok
          ok
      }
    }

    dfs(0, 0, 0)
  }
}
''')

w("2511_maximum_enemy_forts_that_can_be_captured", r'''
// LeetCode 2511 - Maximum Enemy Forts That Can Be Captured
// https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

object Solution {
  def captureForts(forts: Array[Int]): Int = {
    var ans = 0
    var prev = -1
    var i = 0
    while (i < forts.length) {
      if (forts(i) != 0) {
        if (prev >= 0 && forts(prev) == -forts(i)) {
          if (i - prev - 1 > ans) ans = i - prev - 1
        }
        prev = i
      }
      i += 1
    }
    ans
  }
}
''')

w("2512_reward_top_k_students", r'''
// LeetCode 2512 - Reward Top K Students
// https://leetcode.com/problems/reward-top-k-students/

object Solution {
  def topStudents(positive_feedback: Array[String], negative_feedback: Array[String], report: Array[String], student_id: Array[Int], k: Int): Array[Int] = {
    val pos = positive_feedback.toSet
    val neg = negative_feedback.toSet
    val arr = Array.ofDim[Int](report.length, 2)
    var i = 0
    while (i < report.length) {
      var score = 0
      report(i).split(" ").foreach { w =>
        if (w.nonEmpty) {
          if (pos.contains(w)) score += 3
          else if (neg.contains(w)) score -= 1
        }
      }
      arr(i)(0) = student_id(i)
      arr(i)(1) = score
      i += 1
    }
    scala.util.Sorting.stableSort(arr, (a: Array[Int], b: Array[Int]) =>
      if (a(1) != b(1)) a(1) > b(1) else a(0) < b(0)
    )
    val ans = new Array[Int](k)
    i = 0
    while (i < k) {
      ans(i) = arr(i)(0)
      i += 1
    }
    ans
  }
}
''')

w("2513_minimize_the_maximum_of_two_arrays", r'''
// LeetCode 2513 - Minimize the Maximum of Two Arrays
// https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

object Solution {
  def minimizeSet(divisor1: Int, divisor2: Int, uniqueCnt1: Int, uniqueCnt2: Int): Int = {
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
    val lcm = divisor1.toLong / gcd(divisor1, divisor2) * divisor2
    def ok(x: Long): Boolean = {
      val a = x - x / divisor1
      val b = x - x / divisor2
      val both = x - x / lcm
      a >= uniqueCnt1 && b >= uniqueCnt2 && both >= uniqueCnt1.toLong + uniqueCnt2
    }
    var lo = 1L
    var hi = 1L << 62
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(mid)) hi = mid else lo = mid + 1
    }
    lo.toInt
  }
}
''')

w("2514_count_anagrams", r'''
// LeetCode 2514 - Count Anagrams
// https://leetcode.com/problems/count-anagrams/

object Solution {
  def countAnagrams(s: String): Int = {
    val MOD = 1000000007
    def modPow(a0: Long, e0: Long): Long = {
      var res = 1L
      var a = a0 % MOD
      var e = e0
      while (e > 0) {
        if ((e & 1) != 0) res = res * a % MOD
        a = a * a % MOD
        e >>= 1
      }
      res
    }
    val trimmed = s.trim
    val words = if (trimmed.isEmpty) Array.empty[String] else trimmed.split("\\s+")
    var maxN = 0
    words.foreach { w => if (w.length > maxN) maxN = w.length }
    val fact = new Array[Long](maxN + 1)
    val invFact = new Array[Long](maxN + 1)
    fact(0) = 1
    var i = 1
    while (i <= maxN) {
      fact(i) = fact(i - 1) * i % MOD
      i += 1
    }
    if (maxN >= 0) invFact(maxN) = modPow(fact(maxN), MOD - 2)
    i = maxN
    while (i > 0) {
      invFact(i - 1) = invFact(i) * i % MOD
      i -= 1
    }
    var ans = 1L
    words.foreach { word =>
      val cnt = new Array[Int](26)
      var j = 0
      while (j < word.length) {
        cnt(word.charAt(j) - 'a') += 1
        j += 1
      }
      var cur = fact(word.length)
      j = 0
      while (j < 26) {
        cur = cur * invFact(cnt(j)) % MOD
        j += 1
      }
      ans = ans * cur % MOD
    }
    ans.toInt
  }
}
''')

w("2515_shortest_distance_to_target_string_in_a_circular_array", r'''
// LeetCode 2515 - Shortest Distance to Target String in a Circular Array
// https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

object Solution {
  def closestTarget(words: Array[String], target: String, startIndex: Int): Int = {
    val n = words.length
    var best = -1
    var i = 0
    while (i < n) {
      if (words(i) == target) {
        var d = i - startIndex
        if (d < 0) d = -d
        if (n - d < d) d = n - d
        if (best < 0 || d < best) best = d
      }
      i += 1
    }
    best
  }
}
''')

w("2516_take_k_of_each_character_from_left_and_right", r'''
// LeetCode 2516 - Take K of Each Character From Left and Right
// https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

object Solution {
  def takeCharacters(s: String, k: Int): Int = {
    val n = s.length
    val cnt = new Array[Int](3)
    var i = 0
    while (i < n) {
      cnt(s.charAt(i) - 'a') += 1
      i += 1
    }
    if (cnt(0) < k || cnt(1) < k || cnt(2) < k) return -1
    val need = Array(cnt(0) - k, cnt(1) - k, cnt(2) - k)
    val window = new Array[Int](3)
    var left = 0
    var maxMid = 0
    var right = 0
    while (right < n) {
      window(s.charAt(right) - 'a') += 1
      while (window(0) > need(0) || window(1) > need(1) || window(2) > need(2)) {
        window(s.charAt(left) - 'a') -= 1
        left += 1
      }
      if (right - left + 1 > maxMid) maxMid = right - left + 1
      right += 1
    }
    n - maxMid
  }
}
''')

w("2517_maximum_tastiness_of_candy_basket", r'''
// LeetCode 2517 - Maximum Tastiness of Candy Basket
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

object Solution {
  def maximumTastiness(price: Array[Int], k: Int): Int = {
    scala.util.Sorting.quickSort(price)
    def ok(d: Int): Boolean = {
      var cnt = 1
      var last = price(0)
      var i = 1
      while (i < price.length) {
        if (price(i) - last >= d) {
          cnt += 1
          last = price(i)
          if (cnt >= k) return true
        }
        i += 1
      }
      false
    }
    var lo = 0
    var hi = price(price.length - 1) - price(0)
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(mid)) lo = mid else hi = mid - 1
    }
    lo
  }
}
''')

w("2518_number_of_great_partitions", r'''
// LeetCode 2518 - Number of Great Partitions
// https://leetcode.com/problems/number-of-great-partitions/

object Solution {
  def countPartitions(nums: Array[Int], k: Int): Int = {
    val MOD = 1000000007
    var sum = 0L
    var i = 0
    while (i < nums.length) {
      sum += nums(i)
      i += 1
    }
    if (sum < 2L * k) return 0
    val dp = new Array[Int](k)
    dp(0) = 1
    i = 0
    while (i < nums.length) {
      val x = nums(i)
      var s = k - 1
      while (s >= x) {
        dp(s) = (dp(s) + dp(s - x)) % MOD
        s -= 1
      }
      i += 1
    }
    var bad = 0
    i = 0
    while (i < k) {
      bad = (bad + dp(i)) % MOD
      i += 1
    }
    var total = 1
    i = 0
    while (i < nums.length) {
      total = total * 2 % MOD
      i += 1
    }
    ((total - 2L * bad % MOD + MOD) % MOD).toInt
  }
}
''')

w("2519_count_the_number_of_k_big_indices", r'''
// LeetCode 2519 - Count the Number of K-Big Indices
// https://leetcode.com/problems/count-the-number-of-k-big-indices/

object Solution {
  private class Fenwick(n: Int) {
    private val bit = new Array[Int](n + 2)
    def add(i0: Int, v: Int): Unit = {
      var i = i0
      while (i < bit.length) {
        bit(i) += v
        i += i & -i
      }
    }
    def sum(i0: Int): Int = {
      var i = i0
      var s = 0
      while (i > 0) {
        s += bit(i)
        i -= i & -i
      }
      s
    }
  }

  def kBigIndices(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val uniq = nums.sorted
    var m = 0
    var i = 0
    while (i < uniq.length) {
      if (i == 0 || uniq(i) != uniq(i - 1)) {
        uniq(m) = uniq(i)
        m += 1
      }
      i += 1
    }
    val rank = scala.collection.mutable.Map.empty[Int, Int]
    i = 0
    while (i < m) {
      rank(uniq(i)) = i + 1
      i += 1
    }
    val left = new Array[Int](n)
    val right = new Array[Int](n)
    var ft = new Fenwick(m)
    i = 0
    while (i < n) {
      val r = rank(nums(i))
      left(i) = ft.sum(r - 1)
      ft.add(r, 1)
      i += 1
    }
    ft = new Fenwick(m)
    i = n - 1
    while (i >= 0) {
      val r = rank(nums(i))
      right(i) = ft.sum(r - 1)
      ft.add(r, 1)
      i -= 1
    }
    var ans = 0
    i = 0
    while (i < n) {
      if (left(i) >= k && right(i) >= k) ans += 1
      i += 1
    }
    ans
  }
}
''')
