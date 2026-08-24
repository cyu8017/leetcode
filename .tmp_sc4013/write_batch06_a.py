#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)


w("2197_replace_non_coprime_numbers_in_array", r'''
// LeetCode 2197 - Replace Non-Coprime Numbers in Array
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

object Solution {
  def replaceNonCoprimes(nums: Array[Int]): Array[Int] = {
    def gcd(a0: Int, b0: Int): Int = {
      var a = a0
      var b = b0
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (x0 <- nums) {
      var x = x0
      var merged = true
      while (merged && stack.nonEmpty) {
        val g = gcd(stack.last, x)
        if (g == 1) merged = false
        else {
          x = stack.last / g * x
          stack.remove(stack.length - 1)
        }
      }
      stack += x
    }
    stack.toArray
  }
}
''')

w("2198_number_of_single_divisor_triplets", r'''
// LeetCode 2198 - Number of Single Divisor Triplets
// https://leetcode.com/problems/number-of-single-divisor-triplets/

object Solution {
  def singleDivisorTriplet(nums: Array[Int]): Long = {
    val freq = Array.fill(101)(0L)
    for (x <- nums) freq(x) += 1
    var ans = 0L
    var a = 1
    while (a <= 100) {
      if (freq(a) != 0) {
        var b = a
        while (b <= 100) {
          if (freq(b) != 0) {
            var c = b
            while (c <= 100) {
              if (freq(c) != 0) {
                val s = a + b + c
                var cnt = 0
                if (s % a == 0) cnt += 1
                if (s % b == 0) cnt += 1
                if (s % c == 0) cnt += 1
                if (cnt == 1) {
                  if (a == b && b == c) ans += freq(a) * (freq(a) - 1) * (freq(a) - 2)
                  else if (a == b) ans += freq(a) * (freq(a) - 1) * freq(c) * 3
                  else if (b == c) ans += freq(b) * (freq(b) - 1) * freq(a) * 3
                  else if (a == c) ans += freq(a) * (freq(a) - 1) * freq(b) * 3
                  else ans += freq(a) * freq(b) * freq(c) * 6
                }
              }
              c += 1
            }
          }
          b += 1
        }
      }
      a += 1
    }
    ans
  }
}
''')

w("2200_find_all_k_distant_indices_in_an_array", r'''
// LeetCode 2200 - Find All K-Distant Indices in an Array
// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

object Solution {
  def findKDistantIndices(nums: Array[Int], key: Int, k: Int): List[Int] = {
    val n = nums.length
    val mark = Array.fill(n)(false)
    var i = 0
    while (i < n) {
      if (nums(i) == key) {
        val l = math.max(0, i - k)
        val r = math.min(n - 1, i + k)
        var j = l
        while (j <= r) {
          mark(j) = true
          j += 1
        }
      }
      i += 1
    }
    val ans = scala.collection.mutable.ListBuffer.empty[Int]
    i = 0
    while (i < n) {
      if (mark(i)) ans += i
      i += 1
    }
    ans.toList
  }
}
''')

w("2201_count_artifacts_that_can_be_extracted", r'''
// LeetCode 2201 - Count Artifacts That Can Be Extracted
// https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

object Solution {
  def digArtifacts(n: Int, artifacts: Array[Array[Int]], dig: Array[Array[Int]]): Int = {
    val dug = scala.collection.mutable.HashSet.empty[Long]
    for (d <- dig) dug += ((d(0).toLong << 32) | (d(1).toLong & 0xffffffffL))
    var ans = 0
    for (a <- artifacts) {
      var ok = true
      var r = a(0)
      while (r <= a(2) && ok) {
        var c = a(1)
        while (c <= a(3) && ok) {
          if (!dug.contains((r.toLong << 32) | (c.toLong & 0xffffffffL))) ok = false
          c += 1
        }
        r += 1
      }
      if (ok) ans += 1
    }
    ans
  }
}
''')

w("2202_maximize_the_topmost_element_after_k_moves", r'''
// LeetCode 2202 - Maximize the Topmost Element After K Moves
// https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

object Solution {
  def maximumTop(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    if (n == 1) return if (k % 2 != 0) -1 else nums(0)
    if (k == 0) return nums(0)
    var ans = -1
    val limit = math.min(k - 1, n)
    var i = 0
    while (i < limit) {
      ans = math.max(ans, nums(i))
      i += 1
    }
    if (k < n) ans = math.max(ans, nums(k))
    ans
  }
}
''')

w("2203_minimum_weighted_subgraph_with_the_required_paths", r'''
// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

object Solution {
  def minimumWeight(n: Int, edges: Array[Array[Int]], src1: Int, src2: Int, dest: Int): Long = {
    val INF = 1L << 62
    def dijkstra(g: Array[List[(Int, Int)]], src: Int): Array[Long] = {
      val dist = Array.fill(n)(INF)
      dist(src) = 0L
      val pq = scala.collection.mutable.PriorityQueue.empty[(Long, Int)](
        Ordering.by[(Long, Int), Long](_._1).reverse
      )
      pq.enqueue((0L, src))
      while (pq.nonEmpty) {
        val (d, u) = pq.dequeue()
        if (d == dist(u)) {
          for ((v, w) <- g(u)) {
            if (d + w < dist(v)) {
              dist(v) = d + w
              pq.enqueue((dist(v), v))
            }
          }
        }
      }
      dist
    }
    val g = Array.fill(n)(List.empty[(Int, Int)])
    val rg = Array.fill(n)(List.empty[(Int, Int)])
    for (e <- edges) {
      g(e(0)) = (e(1), e(2)) :: g(e(0))
      rg(e(1)) = (e(0), e(2)) :: rg(e(1))
    }
    val d1 = dijkstra(g, src1)
    val d2 = dijkstra(g, src2)
    val dd = dijkstra(rg, dest)
    var ans = INF
    var i = 0
    while (i < n) {
      if (d1(i) < INF && d2(i) < INF && dd(i) < INF) {
        ans = math.min(ans, d1(i) + d2(i) + dd(i))
      }
      i += 1
    }
    if (ans >= INF) -1L else ans
  }
}
''')

w("2204_distance_to_a_cycle_in_undirected_graph", r'''
// LeetCode 2204 - Distance to a Cycle in Undirected Graph
// https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

object Solution {
  def distanceToCycle(n: Int, edges: Array[Array[Int]]): Array[Int] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val deg = Array.fill(n)(0)
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
      deg(e(0)) += 1
      deg(e(1)) += 1
    }
    val q = scala.collection.mutable.Queue.empty[Int]
    var i = 0
    while (i < n) {
      if (deg(i) == 1) q.enqueue(i)
      i += 1
    }
    val onCycle = Array.fill(n)(true)
    while (q.nonEmpty) {
      val u = q.dequeue()
      onCycle(u) = false
      for (v <- g(u)) {
        deg(v) -= 1
        if (deg(v) == 1) q.enqueue(v)
      }
    }
    val ans = Array.fill(n)(-1)
    val qq = scala.collection.mutable.Queue.empty[Int]
    i = 0
    while (i < n) {
      if (onCycle(i)) {
        ans(i) = 0
        qq.enqueue(i)
      }
      i += 1
    }
    while (qq.nonEmpty) {
      val u = qq.dequeue()
      for (v <- g(u) if ans(v) == -1) {
        ans(v) = ans(u) + 1
        qq.enqueue(v)
      }
    }
    ans
  }
}
''')

w("2205_the_number_of_users_that_are_eligible_for_discount", r'''
// LeetCode 2205 - The Number of Users That Are Eligible for Discount
// https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/

object Solution {
  final val QUERY: String = """CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
READS SQL DATA
BEGIN
  RETURN (
    SELECT COUNT(DISTINCT user_id) AS user_cnt
    FROM Purchases
    WHERE time_stamp BETWEEN startDate AND endDate
      AND amount >= minAmount
  );
END
"""
}
''')

w("2206_divide_array_into_equal_pairs", r'''
// LeetCode 2206 - Divide Array Into Equal Pairs
// https://leetcode.com/problems/divide-array-into-equal-pairs/

object Solution {
  def divideArray(nums: Array[Int]): Boolean = {
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) freq(x) = freq.getOrElse(x, 0) + 1
    freq.values.forall(_ % 2 == 0)
  }
}
''')

w("2207_maximize_number_of_subsequences_in_a_string", r'''
// LeetCode 2207 - Maximize Number of Subsequences in a String
// https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

object Solution {
  def maximumSubsequenceCount(text: String, pattern: String): Long = {
    val a = pattern.charAt(0)
    val b = pattern.charAt(1)
    def count(s: String): Long = {
      var ca = 0L
      var ans = 0L
      var i = 0
      while (i < s.length) {
        val c = s.charAt(i)
        if (c == b) ans += ca
        if (c == a) ca += 1
        i += 1
      }
      ans
    }
    math.max(count(a.toString + text), count(text + b.toString))
  }
}
''')

w("2208_minimum_operations_to_halve_array_sum", r'''
// LeetCode 2208 - Minimum Operations to Halve Array Sum
// https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

object Solution {
  def halveArray(nums: Array[Int]): Int = {
    val h = scala.collection.mutable.PriorityQueue.empty[Double]
    var sum = 0.0
    for (x <- nums) {
      h.enqueue(x.toDouble)
      sum += x
    }
    val target = sum / 2.0
    var ans = 0
    while (sum > target) {
      val top = h.dequeue()
      val x = top / 2.0
      sum -= x
      h.enqueue(x)
      ans += 1
    }
    ans
  }
}
''')

w("2209_minimum_white_tiles_after_covering_with_carpets", r'''
// LeetCode 2209 - Minimum White Tiles After Covering With Carpets
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

object Solution {
  def minimumWhiteTiles(floor: String, numCarpets: Int, carpetLen: Int): Int = {
    val n = floor.length
    val dp = Array.fill(numCarpets + 1, n + 1)(1 << 30)
    dp(0)(0) = 0
    var j = 1
    while (j <= n) {
      dp(0)(j) = dp(0)(j - 1) + (if (floor.charAt(j - 1) == '1') 1 else 0)
      j += 1
    }
    var c = 1
    while (c <= numCarpets) {
      dp(c)(0) = 0
      j = 1
      while (j <= n) {
        dp(c)(j) = dp(c)(j - 1) + (if (floor.charAt(j - 1) == '1') 1 else 0)
        val start = math.max(0, j - carpetLen)
        dp(c)(j) = math.min(dp(c)(j), dp(c - 1)(start))
        j += 1
      }
      c += 1
    }
    dp(numCarpets)(n)
  }
}
''')

w("2210_count_hills_and_valleys_in_an_array", r'''
// LeetCode 2210 - Count Hills and Valleys in an Array
// https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

object Solution {
  def countHillValley(nums: Array[Int]): Int = {
    val compact = scala.collection.mutable.ArrayBuffer(nums(0))
    var i = 1
    while (i < nums.length) {
      if (nums(i) != compact.last) compact += nums(i)
      i += 1
    }
    var ans = 0
    i = 1
    while (i + 1 < compact.length) {
      if ((compact(i) > compact(i - 1) && compact(i) > compact(i + 1)) ||
          (compact(i) < compact(i - 1) && compact(i) < compact(i + 1)))
        ans += 1
      i += 1
    }
    ans
  }
}
''')

w("2211_count_collisions_on_a_road", r'''
// LeetCode 2211 - Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/

object Solution {
  def countCollisions(directions: String): Int = {
    var i = 0
    var j = directions.length - 1
    while (i < directions.length && directions.charAt(i) == 'L') i += 1
    while (j >= 0 && directions.charAt(j) == 'R') j -= 1
    var ans = 0
    var k = i
    while (k <= j) {
      if (directions.charAt(k) != 'S') ans += 1
      k += 1
    }
    ans
  }
}
''')

w("2212_maximum_points_in_an_archery_competition", r'''
// LeetCode 2212 - Maximum Points in an Archery Competition
// https://leetcode.com/problems/maximum-points-in-an-archery-competition/

object Solution {
  def maximumBobPoints(numArrows: Int, aliceArrows: Array[Int]): Array[Int] = {
    var bestScore = -1
    var best = Array.fill(12)(0)
    def dfs(i: Int, remain: Int, score: Int, bob: Array[Int]): Unit = {
      if (i == 12) {
        if (score > bestScore) {
          bestScore = score
          best = bob.clone()
          if (remain > 0) best(0) += remain
        }
        return
      }
      dfs(i + 1, remain, score, bob)
      val need = aliceArrows(i) + 1
      if (remain >= need) {
        bob(i) = need
        dfs(i + 1, remain - need, score + i, bob)
        bob(i) = 0
      }
    }
    dfs(0, numArrows, 0, Array.fill(12)(0))
    best
  }
}
''')

w("2213_longest_substring_of_one_repeating_character", r'''
// LeetCode 2213 - Longest Substring of One Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/

object Solution {
  private class Seg {
    var lChar: Char = 0
    var rChar: Char = 0
    var lLen: Int = 0
    var rLen: Int = 0
    var best: Int = 0
    var size: Int = 0
  }

  def longestRepeating(s_ : String, queryCharacters: String, queryIndices: Array[Int]): Array[Int] = {
    def merge(a: Seg, b: Seg): Seg = {
      if (a.size == 0) return b
      if (b.size == 0) return a
      val res = new Seg
      res.lChar = a.lChar
      res.rChar = b.rChar
      res.size = a.size + b.size
      res.best = math.max(a.best, b.best)
      res.lLen = a.lLen
      res.rLen = b.rLen
      if (a.rChar == b.lChar) {
        val mid = a.rLen + b.lLen
        res.best = math.max(res.best, mid)
        if (a.lLen == a.size) res.lLen = a.size + b.lLen
        if (b.rLen == b.size) res.rLen = b.size + a.rLen
      }
      res
    }
    val s = s_.toCharArray
    val n = s.length
    val tree = new Array[Seg](4 * n + 5)
    def build(idx: Int, l: Int, r: Int): Unit = {
      if (l == r) {
        tree(idx) = new Seg
        tree(idx).lChar = s(l)
        tree(idx).rChar = s(l)
        tree(idx).lLen = 1
        tree(idx).rLen = 1
        tree(idx).best = 1
        tree(idx).size = 1
        return
      }
      val mid = (l + r) / 2
      build(idx * 2, l, mid)
      build(idx * 2 + 1, mid + 1, r)
      tree(idx) = merge(tree(idx * 2), tree(idx * 2 + 1))
    }
    def update(idx: Int, l: Int, r: Int, pos: Int, ch: Char): Unit = {
      if (l == r) {
        s(pos) = ch
        tree(idx) = new Seg
        tree(idx).lChar = ch
        tree(idx).rChar = ch
        tree(idx).lLen = 1
        tree(idx).rLen = 1
        tree(idx).best = 1
        tree(idx).size = 1
        return
      }
      val mid = (l + r) / 2
      if (pos <= mid) update(idx * 2, l, mid, pos, ch)
      else update(idx * 2 + 1, mid + 1, r, pos, ch)
      tree(idx) = merge(tree(idx * 2), tree(idx * 2 + 1))
    }
    build(1, 0, n - 1)
    val ans = new Array[Int](queryIndices.length)
    var i = 0
    while (i < queryIndices.length) {
      update(1, 0, n - 1, queryIndices(i), queryCharacters.charAt(i))
      ans(i) = tree(1).best
      i += 1
    }
    ans
  }
}
''')

w("2214_minimum_health_to_beat_game", r'''
// LeetCode 2214 - Minimum Health to Beat Game
// https://leetcode.com/problems/minimum-health-to-beat-game/

object Solution {
  def minimumHealth(damage: Array[Int], armor: Int): Long = {
    var sum = 0L
    var mx = 0
    for (d <- damage) {
      sum += d
      mx = math.max(mx, d)
    }
    sum - math.min(armor, mx) + 1
  }
}
''')

w("2215_find_the_difference_of_two_arrays", r'''
// LeetCode 2215 - Find the Difference of Two Arrays
// https://leetcode.com/problems/find-the-difference-of-two-arrays/

object Solution {
  def findDifference(nums1: Array[Int], nums2: Array[Int]): List[List[Int]] = {
    val s1 = scala.collection.mutable.HashSet.empty[Int]
    val s2 = scala.collection.mutable.HashSet.empty[Int]
    for (x <- nums1) s1 += x
    for (x <- nums2) s2 += x
    val a = scala.collection.mutable.ListBuffer.empty[Int]
    val b = scala.collection.mutable.ListBuffer.empty[Int]
    for (x <- s1 if !s2.contains(x)) a += x
    for (x <- s2 if !s1.contains(x)) b += x
    List(a.toList, b.toList)
  }
}
''')

w("2216_minimum_deletions_to_make_array_beautiful", r'''
// LeetCode 2216 - Minimum Deletions to Make Array Beautiful
// https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

object Solution {
  def minDeletion(nums: Array[Int]): Int = {
    var ans = 0
    var i = 0
    val n = nums.length
    while (i + 1 < n) {
      if (nums(i) == nums(i + 1)) {
        ans += 1
        i += 1
      } else i += 2
    }
    if ((n - ans) % 2 != 0) ans += 1
    ans
  }
}
''')

w("2217_find_palindrome_with_fixed_length", r'''
// LeetCode 2217 - Find Palindrome With Fixed Length
// https://leetcode.com/problems/find-palindrome-with-fixed-length/

object Solution {
  def kthPalindrome(queries: Array[Int], intLength: Int): Array[Long] = {
    val half = (intLength + 1) / 2
    var start = 1
    var i = 1
    while (i < half) {
      start *= 10
      i += 1
    }
    val total = start * 9
    val ans = new Array[Long](queries.length)
    i = 0
    while (i < queries.length) {
      val q = queries(i)
      if (q > total) ans(i) = -1L
      else {
        val left = start + q - 1
        var pal = left.toLong
        var x = left
        if (intLength % 2 != 0) x /= 10
        while (x > 0) {
          pal = pal * 10 + x % 10
          x /= 10
        }
        ans(i) = pal
      }
      i += 1
    }
    ans
  }
}
''')

w("2218_maximum_value_of_k_coins_from_piles", r'''
// LeetCode 2218 - Maximum Value of K Coins From Piles
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

object Solution {
  def maxValueOfCoins(piles: List[List[Int]], k: Int): Int = {
    var dp = Array.fill(k + 1)(0)
    for (pile <- piles) {
      val ndp = dp.clone()
      var sum = 0
      var take = 1
      while (take <= pile.size && take <= k) {
        sum += pile(take - 1)
        var j = take
        while (j <= k) {
          ndp(j) = math.max(ndp(j), dp(j - take) + sum)
          j += 1
        }
        take += 1
      }
      dp = ndp
    }
    dp(k)
  }
}
''')

w("2219_maximum_sum_score_of_array", r'''
// LeetCode 2219 - Maximum Sum Score of Array
// https://leetcode.com/problems/maximum-sum-score-of-array/

object Solution {
  def maximumSumScore(nums: Array[Int]): Long = {
    var total = 0L
    for (x <- nums) total += x
    var pref = 0L
    var ans = Long.MinValue
    for (x <- nums) {
      pref += x
      ans = math.max(ans, math.max(pref, total - pref + x))
    }
    ans
  }
}
''')

w("2220_minimum_bit_flips_to_convert_number", r'''
// LeetCode 2220 - Minimum Bit Flips to Convert Number
// https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

object Solution {
  def minBitFlips(start: Int, goal: Int): Int = {
    var x = start ^ goal
    var ans = 0
    while (x > 0) {
      ans += x & 1
      x >>= 1
    }
    ans
  }
}
''')

w("2221_find_triangular_sum_of_an_array", r'''
// LeetCode 2221 - Find Triangular Sum of an Array
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

object Solution {
  def triangularSum(nums: Array[Int]): Int = {
    var cur = nums
    while (cur.length > 1) {
      val next = new Array[Int](cur.length - 1)
      var i = 0
      while (i < next.length) {
        next(i) = (cur(i) + cur(i + 1)) % 10
        i += 1
      }
      cur = next
    }
    cur(0)
  }
}
''')

w("2222_number_of_ways_to_select_buildings", r'''
// LeetCode 2222 - Number of Ways to Select Buildings
// https://leetcode.com/problems/number-of-ways-to-select-buildings/

object Solution {
  def numberOfWays(s: String): Long = {
    var total0 = 0
    var total1 = 0
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == '0') total0 += 1 else total1 += 1
      i += 1
    }
    var left0 = 0
    var left1 = 0
    var ans = 0L
    i = 0
    while (i < s.length) {
      if (s.charAt(i) == '0') {
        ans += left1.toLong * (total1 - left1)
        left0 += 1
      } else {
        ans += left0.toLong * (total0 - left0)
        left1 += 1
      }
      i += 1
    }
    ans
  }
}
''')

print("batch a done")
