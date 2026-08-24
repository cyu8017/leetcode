#!/usr/bin/env python3
"""Write Scala Solution.scala files for batch_16 problems 3359-3394."""
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3359_find_sorted_submatrices_with_maximum_element_at_most_k"] = """// LeetCode 3359 - Find Sorted Submatrices With Maximum Element at Most K
// https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/

object Solution {
  def countSortedMatrices(grid: Array[Array[Int]], k: Int): Long = {
    val m = grid.length
    val n = grid(0).length
    var ans = 0L
    var r1 = 0
    while (r1 < m) {
      var r2 = r1
      while (r2 < m) {
        var c1 = 0
        while (c1 < n) {
          var c2 = c1
          while (c2 < n) {
            var ok = true
            var i = r1
            while (i <= r2 && ok) {
              var j = c1
              while (j <= c2 && ok) {
                if (grid(i)(j) > k) ok = false
                else if (j > c1 && grid(i)(j) < grid(i)(j - 1)) ok = false
                else if (i > r1 && grid(i)(j) < grid(i - 1)(j)) ok = false
                j += 1
              }
              i += 1
            }
            if (ok) ans += 1
            c2 += 1
          }
          c1 += 1
        }
        r2 += 1
      }
      r1 += 1
    }
    ans
  }
}
"""

FILES["3360_stone_removal_game"] = """// LeetCode 3360 - Stone Removal Game
// https://leetcode.com/problems/stone-removal-game/

object Solution {
  def canAliceWin(n0: Int): Boolean = {
    var n = n0
    var take = 10
    var alice = true
    while (n >= take && take > 0) {
      n -= take
      take -= 1
      alice = !alice
    }
    !alice
  }
}
"""

FILES["3361_shift_distance_between_two_strings"] = """// LeetCode 3361 - Shift Distance Between Two Strings
// https://leetcode.com/problems/shift-distance-between-two-strings/

object Solution {
  def shiftDistance(s: String, t: String, nextCost: Array[Int], previousCost: Array[Int]): Long = {
    var ans = 0L
    var i = 0
    while (i < s.length) {
      val a = s.charAt(i) - 'a'
      val b = t.charAt(i) - 'a'
      if (a != b) {
        var fwd = 0L
        var x = a
        while (x != b) {
          fwd += nextCost(x)
          x = (x + 1) % 26
        }
        var bwd = 0L
        x = a
        while (x != b) {
          bwd += previousCost(x)
          x = (x + 25) % 26
        }
        ans += (if (fwd < bwd) fwd else bwd)
      }
      i += 1
    }
    ans
  }
}
"""

FILES["3362_zero_array_transformation_iii"] = """// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

object Solution {
  def maxRemoval(nums: Array[Int], queries: Array[Array[Int]]): Int = {
    val qs = queries.sortBy(_(0))
    val h = new java.util.PriorityQueue[Int]((a, b) => Integer.compare(b, a))
    val n = nums.length
    val diff = new Array[Int](n + 1)
    var j = 0
    var used = 0
    var cur = 0
    var i = 0
    while (i < n) {
      cur += diff(i)
      while (j < qs.length && qs(j)(0) == i) {
        h.offer(qs(j)(1))
        j += 1
      }
      while (cur < nums(i)) {
        if (h.isEmpty || h.peek() < i) return -1
        val r = h.poll()
        cur += 1
        diff(r + 1) -= 1
        used += 1
      }
      i += 1
    }
    qs.length - used
  }
}
"""

FILES["3363_find_the_maximum_number_of_fruits_collected"] = """// LeetCode 3363 - Find the Maximum Number of Fruits Collected
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

object Solution {
  def maxCollectedFruits(fruits: Array[Array[Int]]): Int = {
    val n = fruits.length
    var ans = 0
    var i = 0
    while (i < n) {
      ans += fruits(i)(i)
      fruits(i)(i) = 0
      i += 1
    }
    val neg = -(1 << 30)
    val dp2 = Array.fill(n, n)(neg)
    val dp3 = Array.fill(n, n)(neg)
    dp2(0)(n - 1) = fruits(0)(n - 1)
    i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (dp2(i)(j) != neg) {
          for (dj <- Array(-1, 0, 1)) {
            val ni = i + 1
            val nj = j + dj
            if (ni < n && nj >= 0 && nj < n && nj > ni) {
              val v = dp2(i)(j) + fruits(ni)(nj)
              if (v > dp2(ni)(nj)) dp2(ni)(nj) = v
            }
          }
        }
        j += 1
      }
      i += 1
    }
    dp3(n - 1)(0) = fruits(n - 1)(0)
    var j = 0
    while (j < n) {
      i = 0
      while (i < n) {
        if (dp3(i)(j) != neg) {
          for (di <- Array(-1, 0, 1)) {
            val ni = i + di
            val nj = j + 1
            if (ni >= 0 && ni < n && nj < n && ni > nj) {
              val v = dp3(i)(j) + fruits(ni)(nj)
              if (v > dp3(ni)(nj)) dp3(ni)(nj) = v
            }
          }
        }
        i += 1
      }
      j += 1
    }
    ans += dp2(n - 1)(n - 1) + dp3(n - 1)(n - 1)
    ans
  }
}
"""

FILES["3364_minimum_positive_sum_subarray"] = """// LeetCode 3364 - Minimum Positive Sum Subarray
// https://leetcode.com/problems/minimum-positive-sum-subarray/

object Solution {
  def minimumSumSubarray(nums: Array[Int], l: Int, r: Int): Int = {
    val n = nums.length
    val pref = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + nums(i)
      i += 1
    }
    var ans = Int.MaxValue
    var found = false
    i = 0
    while (i < n) {
      var length = l
      while (length <= r && i + length <= n) {
        val s = pref(i + length) - pref(i)
        if (s > 0 && s < ans) {
          ans = s
          found = true
        }
        length += 1
      }
      i += 1
    }
    if (found) ans else -1
  }
}
"""

FILES["3365_rearrange_k_substrings_to_form_target_string"] = """// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

object Solution {
  def isPossibleToRearrange(s: String, t: String, k: Int): Boolean = {
    val n = s.length
    val sz = n / k
    val cnt = scala.collection.mutable.HashMap.empty[String, Int]
    var i = 0
    while (i < n) {
      val a = s.substring(i, i + sz)
      val b = t.substring(i, i + sz)
      cnt(a) = cnt.getOrElse(a, 0) + 1
      cnt(b) = cnt.getOrElse(b, 0) - 1
      i += sz
    }
    cnt.values.forall(_ == 0)
  }
}
"""

FILES["3366_minimum_array_sum"] = """// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

object Solution {
  def minArraySum(nums: Array[Int], k: Int, op1: Int, op2: Int): Int = {
    val inf = 1000000000000000000L
    var dp = Array.fill(op1 + 1, op2 + 1)(inf)
    dp(0)(0) = 0
    for (x <- nums) {
      val ndp = Array.fill(op1 + 1, op2 + 1)(inf)
      var a = 0
      while (a <= op1) {
        var b = 0
        while (b <= op2) {
          if (dp(a)(b) != inf) {
            tryCand(ndp, dp(a)(b), a, b, x)
            if (a < op1) tryCand(ndp, dp(a)(b), a + 1, b, (x + 1) / 2)
            if (b < op2 && x >= k) tryCand(ndp, dp(a)(b), a, b + 1, x - k)
            if (a < op1 && b < op2) {
              val v1 = (x + 1) / 2
              if (v1 >= k) tryCand(ndp, dp(a)(b), a + 1, b + 1, v1 - k)
              if (x >= k) tryCand(ndp, dp(a)(b), a + 1, b + 1, (x - k + 1) / 2)
            }
          }
          b += 1
        }
        a += 1
      }
      dp = ndp
    }
    var ans = inf
    var a = 0
    while (a <= op1) {
      var b = 0
      while (b <= op2) {
        if (dp(a)(b) < ans) ans = dp(a)(b)
        b += 1
      }
      a += 1
    }
    ans.toInt
  }

  private def tryCand(ndp: Array[Array[Long]], base: Long, na: Int, nb: Int, v: Int): Unit = {
    if (base + v < ndp(na)(nb)) ndp(na)(nb) = base + v
  }
}
"""

FILES["3367_maximize_sum_of_weights_after_edge_removals"] = """// LeetCode 3367 - Maximize Sum of Weights after Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

object Solution {
  def maximizeSumOfWeights(edges: Array[Array[Int]], k: Int): Long = {
    val n = edges.length + 1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Array[Int]])
    for (e <- edges) {
      g(e(0)) += Array(e(1), e(2))
      g(e(1)) += Array(e(0), e(2))
    }
    def dfs(u: Int, p: Int): Array[Long] = {
      var base = 0L
      val gains = scala.collection.mutable.ArrayBuffer.empty[Long]
      for (e <- g(u)) {
        val to = e(0)
        val w = e(1)
        if (to != p) {
          val child = dfs(to, u)
          base += child(1)
          val gain = child(0) + w - child(1)
          if (gain > 0) gains += gain
        }
      }
      val sorted = gains.sorted(Ordering[Long].reverse)
      var withP = base
      var without = base
      var i = 0
      while (i < sorted.length && i < k - 1) {
        withP += sorted(i)
        i += 1
      }
      i = 0
      while (i < sorted.length && i < k) {
        without += sorted(i)
        i += 1
      }
      Array(withP, without)
    }
    dfs(0, -1)(1)
  }
}
"""

FILES["3369_design_an_array_statistics_tracker"] = """// LeetCode 3369 - Design an Array Statistics Tracker
// https://leetcode.com/problems/design-an-array-statistics-tracker/

class StatisticsTracker() {
  private val arr = scala.collection.mutable.ArrayBuffer.empty[Int]
  private var sum = 0L
  private val freq = scala.collection.mutable.HashMap.empty[Int, Int]
  private var modeFreq = 0
  private val modes = scala.collection.mutable.HashSet.empty[Int]

  def addNumber(num: Int): Unit = {
    arr += num
    sum += num
    val f = freq.getOrElse(num, 0) + 1
    freq(num) = f
    if (f > modeFreq) {
      modeFreq = f
      modes.clear()
      modes += num
    } else if (f == modeFreq) {
      modes += num
    }
  }

  def removeFirst(): Unit = {
    if (arr.isEmpty) return
    val num = arr.remove(0)
    sum -= num
    val f = freq(num) - 1
    if (f == 0) freq.remove(num)
    else freq(num) = f
    modeFreq = 0
    modes.clear()
    for ((v, ff) <- freq) {
      if (ff > modeFreq) {
        modeFreq = ff
        modes.clear()
        modes += v
      } else if (ff == modeFreq) {
        modes += v
      }
    }
  }

  def getMean(): Int = {
    if (arr.isEmpty) 0 else (sum / arr.length).toInt
  }

  def getMedian(): Int = {
    val n = arr.length
    val tmp = arr.sorted
    if (n % 2 == 1) tmp(n / 2) else tmp(n / 2 - 1)
  }

  def getMode(): Int = {
    var best = Long.MaxValue
    for (v <- modes) if (v < best) best = v
    if (best == Long.MaxValue) 0 else best.toInt
  }
}
"""

FILES["3370_smallest_number_with_all_set_bits"] = """// LeetCode 3370 - Smallest Number With All Set Bits
// https://leetcode.com/problems/smallest-number-with-all-set-bits/

object Solution {
  def smallestNumber(n: Int): Int = {
    var x = 1
    while (x < n) x = x * 2 + 1
    x
  }
}
"""

FILES["3371_identify_the_largest_outlier_in_an_array"] = """// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

object Solution {
  def getLargestOutlier(nums: Array[Int]): Int = {
    var sum = 0
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) {
      sum += x
      freq(x) = freq.getOrElse(x, 0) + 1
    }
    var ans = Int.MinValue
    for (x <- nums) {
      freq(x) = freq(x) - 1
      val rem = sum - x
      if (rem % 2 == 0) {
        val cand = rem / 2
        if (freq.getOrElse(cand, 0) > 0 && x > ans) ans = x
      }
      freq(x) = freq(x) + 1
    }
    ans
  }
}
"""

FILES["3372_maximize_the_number_of_target_nodes_after_connecting_trees_i"] = """// LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

object Solution {
  private def buildTree(n: Int, edges: Array[Array[Int]]): Array[scala.collection.mutable.ArrayBuffer[Int]] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    g
  }

  private def countWithin(g: Array[scala.collection.mutable.ArrayBuffer[Int]], start: Int, k: Int): Int = {
    if (k < 0) return 0
    val n = g.length
    val vis = new Array[Boolean](n)
    val q = scala.collection.mutable.Queue[(Int, Int)]()
    q.enqueue((start, 0))
    vis(start) = true
    var cnt = 0
    while (q.nonEmpty) {
      val (u, d) = q.dequeue()
      cnt += 1
      if (d != k) {
        for (v <- g(u) if !vis(v)) {
          vis(v) = true
          q.enqueue((v, d + 1))
        }
      }
    }
    cnt
  }

  def maxTargetNodes(edges1: Array[Array[Int]], edges2: Array[Array[Int]], k: Int): Array[Int] = {
    val n = edges1.length + 1
    val m = edges2.length + 1
    val g1 = buildTree(n, edges1)
    val g2 = buildTree(m, edges2)
    val cnt1 = Array.tabulate(n)(i => countWithin(g1, i, k))
    var best2 = 0
    if (k > 0) {
      var i = 0
      while (i < m) {
        val c = countWithin(g2, i, k - 1)
        if (c > best2) best2 = c
        i += 1
      }
    }
    Array.tabulate(n)(i => cnt1(i) + best2)
  }
}
"""

FILES["3373_maximize_the_number_of_target_nodes_after_connecting_trees_ii"] = """// LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

object Solution {
  private def buildTree(n: Int, edges: Array[Array[Int]]): Array[scala.collection.mutable.ArrayBuffer[Int]] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    g
  }

  private def bipartiteCount(g: Array[scala.collection.mutable.ArrayBuffer[Int]], color: Array[Int]): Array[Int] = {
    java.util.Arrays.fill(color, -1)
    val q = scala.collection.mutable.Queue[Int]()
    q.enqueue(0)
    color(0) = 0
    val cnt = Array(1, 0)
    while (q.nonEmpty) {
      val u = q.dequeue()
      for (v <- g(u) if color(v) == -1) {
        color(v) = color(u) ^ 1
        cnt(color(v)) += 1
        q.enqueue(v)
      }
    }
    cnt
  }

  def maxTargetNodes(edges1: Array[Array[Int]], edges2: Array[Array[Int]]): Array[Int] = {
    val n = edges1.length + 1
    val m = edges2.length + 1
    val g1 = buildTree(n, edges1)
    val g2 = buildTree(m, edges2)
    val color1 = new Array[Int](n)
    val color2 = new Array[Int](m)
    val c1 = bipartiteCount(g1, color1)
    val c2 = bipartiteCount(g2, color2)
    val best2 = math.max(c2(0), c2(1))
    Array.tabulate(n)(i => c1(color1(i)) + best2)
  }
}
"""

FILES["3375_minimum_operations_to_make_array_values_equal_to_k"] = """// LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Int = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    for (x <- nums) {
      if (x < k) return -1
      if (x > k) seen += x
    }
    seen.size
  }
}
"""

FILES["3376_minimum_time_to_break_locks_i"] = """// LeetCode 3376 - Minimum Time to Break Locks I
// https://leetcode.com/problems/minimum-time-to-break-locks-i/

object Solution {
  private def bitsOnes(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x > 0) {
      c += x & 1
      x >>= 1
    }
    c
  }

  def findMinimumTime(strength: Array[Int], k: Int): Int = {
    val n = strength.length
    val inf = 1000000000
    val N = 1 << n
    val dp = Array.fill(N)(inf)
    dp(0) = 0
    var mask = 0
    while (mask < N) {
      if (dp(mask) != inf) {
        val opened = bitsOnes(mask)
        val x = 1 + opened * k
        var i = 0
        while (i < n) {
          if ((mask & (1 << i)) == 0) {
            val t = (strength(i) + x - 1) / x
            val nmask = mask | (1 << i)
            if (dp(mask) + t < dp(nmask)) dp(nmask) = dp(mask) + t
          }
          i += 1
        }
      }
      mask += 1
    }
    dp(N - 1)
  }
}
"""

FILES["3377_digit_operations_to_make_two_integers_equal"] = """// LeetCode 3377 - Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

object Solution {
  private def sieve(n: Int): Array[Boolean] = {
    val isP = new Array[Boolean](n)
    var i = 2
    while (i < n) { isP(i) = true; i += 1 }
    i = 2
    while (i * i < n) {
      if (isP(i)) {
        var j = i * i
        while (j < n) {
          isP(j) = false
          j += i
        }
      }
      i += 1
    }
    isP
  }

  def minOperations(n: Int, m: Int): Int = {
    val isPrime = sieve(100000)
    if (isPrime(n)) return -1
    val dist = Array.fill(100000)(-1)
    val pq = new java.util.PriorityQueue[Array[Int]]((a, b) => Integer.compare(a(0), b(0)))
    pq.offer(Array(n, n))
    dist(n) = n
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val cost = cur(0)
      val `val` = cur(1)
      if (cost == dist(`val`)) {
        if (`val` == m) return cost
        val s = `val`.toString.toCharArray
        var i = 0
        while (i < s.length) {
          val orig = s(i)
          for (d <- Array(-1, 1)) {
            val nd = (orig - '0') + d
            if (nd >= 0 && nd <= 9 && !(i == 0 && nd == 0 && s.length > 1)) {
              s(i) = ('0' + nd).toChar
              val nv = new String(s).toInt
              s(i) = orig
              if (!isPrime(nv)) {
                val nc = cost + nv
                if (dist(nv) == -1 || nc < dist(nv)) {
                  dist(nv) = nc
                  pq.offer(Array(nc, nv))
                }
              }
            }
          }
          i += 1
        }
      }
    }
    -1
  }
}
"""

FILES["3378_count_connected_components_in_lcm_graph"] = """// LeetCode 3378 - Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/

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

  def countComponents(nums: Array[Int], threshold: Int): Int = {
    val n = nums.length
    val parent = Array.tabulate(n)(i => i)
    def find(x0: Int): Int = {
      var x = x0
      while (parent(x) != x) {
        parent(x) = parent(parent(x))
        x = parent(x)
      }
      x
    }
    def unite(a: Int, b: Int): Unit = {
      val ra = find(a)
      val rb = find(b)
      if (ra != rb) parent(ra) = rb
    }
    val idx = scala.collection.mutable.HashMap.empty[Int, Int]
    var i = 0
    while (i < n) {
      idx(nums(i)) = i
      i += 1
    }
    var d = 1
    while (d <= threshold) {
      var first = -1
      var m = d
      while (m <= threshold) {
        idx.get(m) match {
          case Some(ii) =>
            if (first == -1) first = ii
            else if (nums(first).toLong * nums(ii) / gcd(nums(first), nums(ii)) <= threshold)
              unite(first, ii)
          case None =>
        }
        m += d
      }
      d += 1
    }
    i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        val a = nums(i)
        val b = nums(j)
        val g = gcd(a, b)
        if (a.toLong / g * b <= threshold) unite(i, j)
        j += 1
      }
      i += 1
    }
    val comp = scala.collection.mutable.HashSet.empty[Int]
    i = 0
    while (i < n) {
      comp += find(i)
      i += 1
    }
    comp.size
  }
}
"""

FILES["3379_transformed_array"] = """// LeetCode 3379 - Transformed Array
// https://leetcode.com/problems/transformed-array/

object Solution {
  def constructTransformedArray(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val ans = new Array[Int](n)
    var i = 0
    while (i < n) {
      val j = ((i + nums(i)) % n + n) % n
      ans(i) = nums(j)
      i += 1
    }
    ans
  }
}
"""

FILES["3380_maximum_area_rectangle_with_point_constraints_i"] = """// LeetCode 3380 - Maximum Area Rectangle With Point Constraints I
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/

object Solution {
  private def pack(x: Int, y: Int): Long = (x.toLong << 32) ^ (y & 0xffffffffL)

  def maxRectangleArea(points: Array[Array[Int]]): Int = {
    val set = scala.collection.mutable.HashSet.empty[Long]
    for (p <- points) set += pack(p(0), p(1))
    var ans = -1
    val n = points.length
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        val x1 = points(i)(0)
        val y1 = points(i)(1)
        val x2 = points(j)(0)
        val y2 = points(j)(1)
        if (x1 != x2 && y1 != y2 && set.contains(pack(x1, y2)) && set.contains(pack(x2, y1))) {
          val minX = math.min(x1, x2)
          val maxX = math.max(x1, x2)
          val minY = math.min(y1, y2)
          val maxY = math.max(y1, y2)
          var ok = true
          for (p <- points if ok) {
            val x = p(0)
            val y = p(1)
            if (x > minX && x < maxX && y > minY && y < maxY) ok = false
            else {
              val onBorder =
                ((x == minX || x == maxX) && y >= minY && y <= maxY) ||
                  ((y == minY || y == maxY) && x >= minX && x <= maxX)
              if (onBorder) {
                val isCorner = (x == minX || x == maxX) && (y == minY || y == maxY)
                if (!isCorner) ok = false
              }
            }
          }
          if (ok) {
            val area = (maxX - minX) * (maxY - minY)
            if (area > ans) ans = area
          }
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
"""

FILES["3381_maximum_subarray_sum_with_length_divisible_by_k"] = """// LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

object Solution {
  def maxSubarraySum(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val pref = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + nums(i)
      i += 1
    }
    val INF = 1L << 62
    val best = Array.fill(k)(INF)
    best(0) = 0
    var ans = -(1L << 62)
    i = 1
    while (i <= n) {
      val r = i % k
      if (best(r) != INF) {
        val cand = pref(i) - best(r)
        if (cand > ans) ans = cand
      }
      if (pref(i) < best(r)) best(r) = pref(i)
      i += 1
    }
    ans
  }
}
"""

FILES["3382_maximum_area_rectangle_with_point_constraints_ii"] = """// LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

object Solution {
  private def pack(x: Int, y: Int): Long = (x.toLong << 32) ^ (y & 0xffffffffL)

  def maxRectangleArea(xCoord: Array[Int], yCoord: Array[Int]): Long = {
    val n = xCoord.length
    val points = Array.tabulate(n)(i => Array(xCoord(i), yCoord(i)))
    val set = scala.collection.mutable.HashSet.empty[Long]
    for (p <- points) set += pack(p(0), p(1))
    var ans = -1L
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        val x1 = points(i)(0)
        val y1 = points(i)(1)
        val x2 = points(j)(0)
        val y2 = points(j)(1)
        if (x1 != x2 && y1 != y2 && set.contains(pack(x1, y2)) && set.contains(pack(x2, y1))) {
          val minX = math.min(x1, x2)
          val maxX = math.max(x1, x2)
          val minY = math.min(y1, y2)
          val maxY = math.max(y1, y2)
          var ok = true
          for (p <- points if ok) {
            val x = p(0)
            val y = p(1)
            if (x > minX && x < maxX && y > minY && y < maxY) ok = false
            else {
              val onBorder =
                ((x == minX || x == maxX) && y >= minY && y <= maxY) ||
                  ((y == minY || y == maxY) && x >= minX && x <= maxX)
              if (onBorder) {
                val isCorner = (x == minX || x == maxX) && (y == minY || y == maxY)
                if (!isCorner) ok = false
              }
            }
          }
          if (ok) {
            val area = (maxX - minX).toLong * (maxY - minY)
            if (area > ans) ans = area
          }
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
"""

FILES["3383_minimum_runes_to_add_to_cast_spell"] = """// LeetCode 3383 - Minimum Runes to Add to Cast Spell
// https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

object Solution {
  def minRunesToAdd(n: Int, crystals: Array[Int], flowFrom: Array[Int], flowTo: Array[Int]): Int = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val rg = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 0
    while (i < flowFrom.length) {
      val a = flowFrom(i)
      val b = flowTo(i)
      g(a) += b
      rg(b) += a
      i += 1
    }
    val vis = new Array[Boolean](n)
    val order = scala.collection.mutable.ArrayBuffer.empty[Int]
    def dfs1(u: Int): Unit = {
      vis(u) = true
      for (v <- g(u) if !vis(v)) dfs1(v)
      order += u
    }
    i = 0
    while (i < n) {
      if (!vis(i)) dfs1(i)
      i += 1
    }
    val comp = Array.fill(n)(-1)
    var cid = 0
    def dfs2(u: Int): Unit = {
      comp(u) = cid
      for (v <- rg(u) if comp(v) == -1) dfs2(v)
    }
    i = n - 1
    while (i >= 0) {
      val u = order(i)
      if (comp(u) == -1) {
        dfs2(u)
        cid += 1
      }
      i -= 1
    }
    val hasCrystal = new Array[Boolean](cid)
    for (c <- crystals) hasCrystal(comp(c)) = true
    val indeg = new Array[Int](cid)
    var u = 0
    while (u < n) {
      for (v <- g(u) if comp(u) != comp(v)) indeg(comp(v)) += 1
      u += 1
    }
    var ans = 0
    i = 0
    while (i < cid) {
      if (indeg(i) == 0 && !hasCrystal(i)) ans += 1
      i += 1
    }
    ans
  }
}
"""

FILES["3385_minimum_time_to_break_locks_ii"] = """// LeetCode 3385 - Minimum Time to Break Locks II
// https://leetcode.com/problems/minimum-time-to-break-locks-ii/

object Solution {
  private def bitsOnes(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x > 0) {
      c += x & 1
      x >>= 1
    }
    c
  }

  def findMinimumTime(strength: Array[Int]): Int = {
    val n = strength.length
    val N = 1 << n
    val inf = 1000000000000000000L
    val dp = Array.fill(N)(inf)
    dp(0) = 0
    val k = 1
    var mask = 0
    while (mask < N) {
      if (dp(mask) != inf) {
        val opened = bitsOnes(mask)
        val x = 1 + opened * k
        var i = 0
        while (i < n) {
          if ((mask & (1 << i)) == 0) {
            val t = (strength(i) + x - 1) / x
            val nmask = mask | (1 << i)
            if (dp(mask) + t < dp(nmask)) dp(nmask) = dp(mask) + t
          }
          i += 1
        }
      }
      mask += 1
    }
    dp(N - 1).toInt
  }
}
"""

FILES["3386_button_with_longest_push_time"] = """// LeetCode 3386 - Button with Longest Push Time
// https://leetcode.com/problems/button-with-longest-push-time/

object Solution {
  def buttonWithLongestTime(events: Array[Array[Int]]): Int = {
    var bestT = events(0)(1)
    var bestI = events(0)(0)
    var i = 1
    while (i < events.length) {
      val t = events(i)(1) - events(i - 1)(1)
      if (t > bestT || (t == bestT && events(i)(0) < bestI)) {
        bestT = t
        bestI = events(i)(0)
      }
      i += 1
    }
    bestI
  }
}
"""

FILES["3387_maximize_amount_after_two_days_of_conversions"] = """// LeetCode 3387 - Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

object Solution {
  private def buildRateGraph(pairs: Array[Array[String]], rates: Array[Double]): scala.collection.mutable.HashMap[String, scala.collection.mutable.HashMap[String, Double]] = {
    val g = scala.collection.mutable.HashMap.empty[String, scala.collection.mutable.HashMap[String, Double]]
    var i = 0
    while (i < pairs.length) {
      val a = pairs(i)(0)
      val b = pairs(i)(1)
      if (!g.contains(a)) g(a) = scala.collection.mutable.HashMap.empty[String, Double]
      if (!g.contains(b)) g(b) = scala.collection.mutable.HashMap.empty[String, Double]
      g(a)(b) = rates(i)
      g(b)(a) = 1.0 / rates(i)
      i += 1
    }
    g
  }

  private def bellman(start: String, pairs: Array[Array[String]], rates: Array[Double]): scala.collection.mutable.HashMap[String, Double] = {
    val g = buildRateGraph(pairs, rates)
    val dist = scala.collection.mutable.HashMap[String, Double](start -> 1.0)
    var it = 0
    var loop = true
    while (it < 100 && loop) {
      var updated = false
      for ((from, tos) <- g if dist.contains(from) && dist(from) != 0) {
        for ((to, rate) <- tos) {
          val nv = dist(from) * rate
          if (!dist.contains(to) || nv > dist(to)) {
            dist(to) = nv
            updated = true
          }
        }
      }
      if (!updated) loop = false
      it += 1
    }
    dist
  }

  def maxAmount(initialCurrency: String, pairs1: Array[Array[String]], rates1: Array[Double],
                pairs2: Array[Array[String]], rates2: Array[Double]): Double = {
    val amt1 = bellman(initialCurrency, pairs1, rates1)
    var ans = 1.0
    val g2 = buildRateGraph(pairs2, rates2)
    for ((c, a) <- amt1 if a > 0) {
      val dist = scala.collection.mutable.HashMap[String, Double](c -> a)
      var updated = true
      var it = 0
      while (it < 100 && updated) {
        updated = false
        for ((from, tos) <- g2 if dist.contains(from) && dist(from) != 0) {
          for ((to, rate) <- tos) {
            val nv = dist(from) * rate
            if (!dist.contains(to) || nv > dist(to)) {
              dist(to) = nv
              updated = true
            }
          }
        }
        it += 1
      }
      if (dist.contains(initialCurrency) && dist(initialCurrency) > ans) ans = dist(initialCurrency)
    }
    ans
  }
}
"""

FILES["3388_count_beautiful_splits_in_an_array"] = """// LeetCode 3388 - Count Beautiful Splits in an Array
// https://leetcode.com/problems/count-beautiful-splits-in-an-array/

object Solution {
  private def equal(a: Array[Int], as: Int, ae: Int, b: Array[Int], bs: Int, be: Int): Boolean = {
    if (ae - as != be - bs) return false
    var i = 0
    while (i < ae - as) {
      if (a(as + i) != b(bs + i)) return false
      i += 1
    }
    true
  }

  def beautifulSplits(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var i = 1
    while (i < n - 1) {
      var j = i + 1
      while (j < n) {
        var ok = false
        if (i <= j - i && equal(nums, 0, i, nums, i, i + i)) ok = true
        if (!ok && j - i <= n - j && equal(nums, i, j, nums, j, j + (j - i))) ok = true
        if (ok) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
"""

FILES["3389_minimum_operations_to_make_character_frequencies_equal"] = """// LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

object Solution {
  def makeStringGood(s: String): Int = {
    val freq = new Array[Int](26)
    for (c <- s) freq(c - 'a') += 1
    var ans = s.length
    var t = 1
    while (t <= s.length) {
      var pool = 0
      var i = 0
      while (i < 26) {
        if (freq(i) > t) pool += freq(i) - t
        i += 1
      }
      var deficit = 0
      i = 0
      while (i < 26) {
        if (freq(i) < t) deficit += t - freq(i)
        i += 1
      }
      val ops = math.max(pool, deficit)
      if (ops < ans) ans = ops
      t += 1
    }
    if (s.length < ans) ans = s.length
    ans
  }
}
"""

FILES["3391_design_a_3d_binary_matrix_with_efficient_layer_tracking"] = """// LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
// https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

class Matrix3D(_n: Int) {
  private val n = _n
  private val m = Array.ofDim[Int](n, n, n)
  private val ones = new Array[Int](n)

  def setCell(x: Int, y: Int, z: Int): Unit = {
    if (m(x)(y)(z) == 0) {
      m(x)(y)(z) = 1
      ones(x) += 1
    }
  }

  def unsetCell(x: Int, y: Int, z: Int): Unit = {
    if (m(x)(y)(z) == 1) {
      m(x)(y)(z) = 0
      ones(x) -= 1
    }
  }

  def largestMatrix(): Int = {
    var best = -1
    var idx = 0
    var i = 0
    while (i < n) {
      if (ones(i) >= best) {
        best = ones(i)
        idx = i
      }
      i += 1
    }
    idx
  }
}
"""

FILES["3392_count_subarrays_of_length_three_with_a_condition"] = """// LeetCode 3392 - Count Subarrays of Length Three With a Condition
// https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

object Solution {
  def countSubarrays(nums: Array[Int]): Int = {
    var ans = 0
    var i = 0
    while (i + 2 < nums.length) {
      if (nums(i) * 2 + nums(i + 2) * 2 == nums(i + 1)) ans += 1
      i += 1
    }
    ans
  }
}
"""

FILES["3393_count_paths_with_the_given_xor_value"] = """// LeetCode 3393 - Count Paths With the Given XOR Value
// https://leetcode.com/problems/count-paths-with-the-given-xor-value/

object Solution {
  def countPathsWithXorValue(grid: Array[Array[Int]], k: Int): Int = {
    val mod = 1000000007
    val m = grid.length
    val n = grid(0).length
    val dp = Array.ofDim[Int](m, n, 16)
    dp(0)(0)(grid(0)(0)) = 1
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        var x = 0
        while (x < 16) {
          if (dp(i)(j)(x) != 0) {
            if (i + 1 < m) {
              val nx = x ^ grid(i + 1)(j)
              dp(i + 1)(j)(nx) = (dp(i + 1)(j)(nx) + dp(i)(j)(x)) % mod
            }
            if (j + 1 < n) {
              val nx = x ^ grid(i)(j + 1)
              dp(i)(j + 1)(nx) = (dp(i)(j + 1)(nx) + dp(i)(j)(x)) % mod
            }
          }
          x += 1
        }
        j += 1
      }
      i += 1
    }
    dp(m - 1)(n - 1)(k)
  }
}
"""

FILES["3394_check_if_grid_can_be_cut_into_sections"] = """// LeetCode 3394 - Check if Grid can be Cut into Sections
// https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

object Solution {
  private def checkCut(rects: Array[Array[Int]], axis: Int): Boolean = {
    val arr = Array.tabulate(rects.length) { i =>
      if (axis == 0) Array(rects(i)(0), rects(i)(2))
      else Array(rects(i)(1), rects(i)(3))
    }
    scala.util.Sorting.stableSort(arr, (x: Array[Int], y: Array[Int]) =>
      if (x(0) == y(0)) x(1) < y(1) else x(0) < y(0)
    )
    var cuts = 0
    var end = arr(0)(1)
    var i = 1
    while (i < arr.length) {
      if (arr(i)(0) >= end) {
        cuts += 1
        end = arr(i)(1)
        if (cuts >= 2) return true
      } else if (arr(i)(1) > end) {
        end = arr(i)(1)
      }
      i += 1
    }
    false
  }

  def checkValidCuts(n: Int, rectangles: Array[Array[Int]]): Boolean =
    checkCut(rectangles, 0) || checkCut(rectangles, 1)
}
"""

def main() -> None:
    written = 0
    for folder, text in FILES.items():
        path = ROOT / folder / "Solution.scala"
        path.write_text(text, encoding="utf-8")
        if path.read_bytes().startswith(b"\xef\xbb\xbf"):
            raise SystemExit(f"BOM in {folder}")
        written += 1
        print(f"wrote {folder}")
    print(f"batch C written={written}")

if __name__ == "__main__":
    main()
