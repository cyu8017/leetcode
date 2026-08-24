#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("2391_minimum_amount_of_time_to_collect_garbage", r'''
// LeetCode 2391 - Minimum Amount of Time to Collect Garbage
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

object Solution {
  def garbageCollection(garbage: Array[String], travel: Array[Int]): Int = {
    var ans = 0
    var lastM = 0
    var lastP = 0
    var lastG = 0
    var i = 0
    while (i < garbage.length) {
      ans += garbage(i).length
      var j = 0
      while (j < garbage(i).length) {
        val c = garbage(i).charAt(j)
        if (c == 'M') lastM = i
        else if (c == 'P') lastP = i
        else lastG = i
        j += 1
      }
      i += 1
    }
    val pref = Array.fill(travel.length + 1)(0)
    i = 0
    while (i < travel.length) {
      pref(i + 1) = pref(i) + travel(i)
      i += 1
    }
    ans + pref(lastM) + pref(lastP) + pref(lastG)
  }
}
''')

w("2392_build_a_matrix_with_conditions", r'''
// LeetCode 2392 - Build a Matrix With Conditions
// https://leetcode.com/problems/build-a-matrix-with-conditions/

object Solution {
  def buildMatrix(k: Int, rowConditions: Array[Array[Int]], colConditions: Array[Array[Int]]): Array[Array[Int]] = {
    val rowOrder = topo(k, rowConditions)
    val colOrder = topo(k, colConditions)
    if (rowOrder == null || colOrder == null) return Array.empty[Array[Int]]
    val rowPos = Array.fill(k + 1)(0)
    val colPos = Array.fill(k + 1)(0)
    var i = 0
    while (i < k) {
      rowPos(rowOrder(i)) = i
      colPos(colOrder(i)) = i
      i += 1
    }
    val ans = Array.ofDim[Int](k, k)
    var v = 1
    while (v <= k) {
      ans(rowPos(v))(colPos(v)) = v
      v += 1
    }
    ans
  }

  private def topo(k: Int, conds: Array[Array[Int]]): Array[Int] = {
    val g = Array.fill(k + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val indeg = Array.fill(k + 1)(0)
    conds.foreach { c =>
      g(c(0)) += c(1)
      indeg(c(1)) += 1
    }
    val q = scala.collection.mutable.Queue.empty[Int]
    var i = 1
    while (i <= k) {
      if (indeg(i) == 0) q.enqueue(i)
      i += 1
    }
    val order = Array.fill(k)(0)
    var idx = 0
    while (q.nonEmpty) {
      val u = q.dequeue()
      order(idx) = u
      idx += 1
      g(u).foreach { v =>
        indeg(v) -= 1
        if (indeg(v) == 0) q.enqueue(v)
      }
    }
    if (idx != k) null else order
  }
}
''')

w("2393_count_strictly_increasing_subarrays", r'''
// LeetCode 2393 - Count Strictly Increasing Subarrays
// https://leetcode.com/problems/count-strictly-increasing-subarrays/

object Solution {
  def countSubarrays(nums: Array[Int]): Long = {
    var ans = 0L
    var len = 0L
    var i = 0
    while (i < nums.length) {
      if (i > 0 && nums(i) > nums(i - 1)) len += 1
      else len = 1
      ans += len
      i += 1
    }
    ans
  }
}
''')

w("2395_find_subarrays_with_equal_sum", r'''
// LeetCode 2395 - Find Subarrays With Equal Sum
// https://leetcode.com/problems/find-subarrays-with-equal-sum/

object Solution {
  def findSubarrays(nums: Array[Int]): Boolean = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var i = 0
    while (i + 1 < nums.length) {
      val s = nums(i) + nums(i + 1)
      if (seen.contains(s)) return true
      seen += s
      i += 1
    }
    false
  }
}
''')

w("2396_strictly_palindromic_number", r'''
// LeetCode 2396 - Strictly Palindromic Number
// https://leetcode.com/problems/strictly-palindromic-number/

object Solution {
  def isStrictlyPalindromic(n: Int): Boolean = false
}
''')

w("2397_maximum_rows_covered_by_columns", r'''
// LeetCode 2397 - Maximum Rows Covered by Columns
// https://leetcode.com/problems/maximum-rows-covered-by-columns/

object Solution {
  def maximumRows(matrix: Array[Array[Int]], numSelect: Int): Int = {
    val m = matrix.length
    val n = matrix(0).length
    var ans = 0

    def dfs(col: Int, chosen: Int, mask: Int): Unit = {
      if (chosen == numSelect) {
        var covered = 0
        var i = 0
        while (i < m) {
          var ok = true
          var j = 0
          while (j < n && ok) {
            if (matrix(i)(j) == 1 && ((mask >> j) & 1) == 0) ok = false
            j += 1
          }
          if (ok) covered += 1
          i += 1
        }
        ans = math.max(ans, covered)
        return
      }
      if (col == n) return
      dfs(col + 1, chosen + 1, mask | (1 << col))
      dfs(col + 1, chosen, mask)
    }

    dfs(0, 0, 0)
    ans
  }
}
''')

w("2398_maximum_number_of_robots_within_budget", r'''
// LeetCode 2398 - Maximum Number of Robots Within Budget
// https://leetcode.com/problems/maximum-number-of-robots-within-budget/

object Solution {
  def maximumRobots(chargeTimes: Array[Int], runningCosts: Array[Int], budget: Long): Int = {
    val n = chargeTimes.length
    var left = 0
    var sum = 0L
    val dq = scala.collection.mutable.ArrayDeque.empty[Int]
    var ans = 0
    var right = 0
    while (right < n) {
      while (dq.nonEmpty && chargeTimes(dq.last) <= chargeTimes(right)) dq.removeLast()
      dq.append(right)
      sum += runningCosts(right)
      while (left <= right && chargeTimes(dq.head).toLong + (right - left + 1).toLong * sum > budget) {
        if (dq.head == left) dq.removeHead()
        sum -= runningCosts(left)
        left += 1
      }
      ans = math.max(ans, right - left + 1)
      right += 1
    }
    ans
  }
}
''')

w("2399_check_distances_between_same_letters", r'''
// LeetCode 2399 - Check Distances Between Same Letters
// https://leetcode.com/problems/check-distances-between-same-letters/

object Solution {
  def checkDistances(s: String, distance: Array[Int]): Boolean = {
    val first = Array.fill(26)(-1)
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i) - 'a'
      if (first(c) == -1) first(c) = i
      else if (i - first(c) - 1 != distance(c)) return false
      i += 1
    }
    true
  }
}
''')

w("2400_number_of_ways_to_reach_a_position_after_exactly_k_steps", r'''
// LeetCode 2400 - Number of Ways to Reach a Position After Exactly k Steps
// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

object Solution {
  def numberOfWays(startPos: Int, endPos: Int, k: Int): Int = {
    val mod = 1000000007
    val diff = math.abs(endPos - startPos)
    if (diff > k || (k - diff) % 2 != 0) return 0
    val r = (k + diff) / 2
    comb(k, r, mod)
  }

  private def comb(n: Int, r: Int, mod: Int): Int = {
    if (r < 0 || r > n) return 0
    var num = 1L
    var den = 1L
    var i = 0
    while (i < r) {
      num = num * (n - i) % mod
      den = den * (i + 1) % mod
      i += 1
    }
    (num * modInverse(den.toInt, mod) % mod).toInt
  }

  private def modInverse(a: Int, mod: Int): Int = modPow(a, mod - 2, mod)

  private def modPow(a: Int, e0: Int, mod: Int): Int = {
    var res = 1L
    var base = a % mod
    var e = e0
    while (e > 0) {
      if ((e & 1) != 0) res = res * base % mod
      base = base * base % mod
      e >>= 1
    }
    res.toInt
  }
}
''')

w("2401_longest_nice_subarray", r'''
// LeetCode 2401 - Longest Nice Subarray
// https://leetcode.com/problems/longest-nice-subarray/

object Solution {
  def longestNiceSubarray(nums: Array[Int]): Int = {
    var used = 0
    var left = 0
    var ans = 0
    var right = 0
    while (right < nums.length) {
      while ((used & nums(right)) != 0) {
        used ^= nums(left)
        left += 1
      }
      used |= nums(right)
      ans = math.max(ans, right - left + 1)
      right += 1
    }
    ans
  }
}
''')

w("2402_meeting_rooms_iii", r'''
// LeetCode 2402 - Meeting Rooms III
// https://leetcode.com/problems/meeting-rooms-iii/

object Solution {
  def mostBooked(n: Int, meetings: Array[Array[Int]]): Int = {
    scala.util.Sorting.stableSort(meetings, (a: Array[Int], b: Array[Int]) => a(0) < b(0))
    val free = scala.collection.mutable.PriorityQueue.empty[Long](Ordering[Long].reverse)
    var i = 0
    while (i < n) {
      free.enqueue(i.toLong)
      i += 1
    }
    val busy = scala.collection.mutable.PriorityQueue.empty[(Long, Long)](
      Ordering.Tuple2[Long, Long].reverse
    )
    val cnt = Array.fill(n)(0)
    meetings.foreach { m =>
      val start = m(0).toLong
      val end = m(1).toLong
      while (busy.nonEmpty && busy.head._1 <= start) {
        free.enqueue(busy.dequeue()._2)
      }
      val dur = end - start
      val (begin, room) =
        if (free.nonEmpty) (start, free.dequeue())
        else {
          val top = busy.dequeue()
          (top._1, top._2)
        }
      busy.enqueue((begin + dur, room))
      cnt(room.toInt) += 1
    }
    var ans = 0
    i = 1
    while (i < n) {
      if (cnt(i) > cnt(ans)) ans = i
      i += 1
    }
    ans
  }
}
''')

w("2403_minimum_time_to_kill_all_monsters", r'''
// LeetCode 2403 - Minimum Time to Kill All Monsters
// https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

object Solution {
  def minimumTime(power: Array[Int]): Long = {
    val n = power.length
    val N = 1 << n
    val dp = Array.fill(N)(Long.MaxValue / 4)
    dp(0) = 0
    var mask = 0
    while (mask < N) {
      val killed = Integer.bitCount(mask)
      val gain = killed + 1L
      var i = 0
      while (i < n) {
        if ((mask & (1 << i)) == 0) {
          val need = (power(i) + gain - 1) / gain
          val nm = mask | (1 << i)
          dp(nm) = math.min(dp(nm), dp(mask) + need)
        }
        i += 1
      }
      mask += 1
    }
    dp(N - 1)
  }
}
''')

w("2404_most_frequent_even_element", r'''
// LeetCode 2404 - Most Frequent Even Element
// https://leetcode.com/problems/most-frequent-even-element/

object Solution {
  def mostFrequentEven(nums: Array[Int]): Int = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var ans = -1
    var best = 0
    nums.foreach { x =>
      if (x % 2 == 0) {
        val c = cnt.getOrElse(x, 0) + 1
        cnt(x) = c
        if (c > best || (c == best && (ans == -1 || x < ans))) {
          best = c
          ans = x
        }
      }
    }
    ans
  }
}
''')

w("2405_optimal_partition_of_string", r'''
// LeetCode 2405 - Optimal Partition of String
// https://leetcode.com/problems/optimal-partition-of-string/

object Solution {
  def partitionString(s: String): Int = {
    var ans = 1
    var seen = 0
    s.foreach { c =>
      val bit = 1 << (c - 'a')
      if ((seen & bit) != 0) {
        ans += 1
        seen = 0
      }
      seen |= bit
    }
    ans
  }
}
''')

w("2406_divide_intervals_into_minimum_number_of_groups", r'''
// LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

object Solution {
  def minGroups(intervals: Array[Array[Int]]): Int = {
    val events = Array.ofDim[Int](intervals.length * 2, 2)
    var idx = 0
    intervals.foreach { it =>
      events(idx) = Array(it(0), 1)
      idx += 1
      events(idx) = Array(it(1) + 1, -1)
      idx += 1
    }
    scala.util.Sorting.stableSort(events, (a: Array[Int], b: Array[Int]) => {
      if (a(0) != b(0)) a(0) < b(0) else a(1) < b(1)
    })
    var cur = 0
    var ans = 0
    events.foreach { e =>
      cur += e(1)
      ans = math.max(ans, cur)
    }
    ans
  }
}
''')

w("2407_longest_increasing_subsequence_ii", r'''
// LeetCode 2407 - Longest Increasing Subsequence II
// https://leetcode.com/problems/longest-increasing-subsequence-ii/

object Solution {
  def lengthOfLIS(nums: Array[Int], k: Int): Int = {
    var maxV = 0
    nums.foreach(x => maxV = math.max(maxV, x))
    val st = new SegTree(maxV + 1)
    var ans = 0
    nums.foreach { x =>
      val lo = math.max(1, x - k)
      var best = 1
      if (lo <= x - 1) best = st.query(1, 1, maxV, lo, x - 1) + 1
      st.update(1, 1, maxV, x, best)
      ans = math.max(ans, best)
    }
    ans
  }

  private class SegTree(n: Int) {
    private val tree = Array.fill(4 * n)(0)

    def update(idx: Int, l: Int, r: Int, pos: Int, value: Int): Unit = {
      if (l == r) {
        tree(idx) = math.max(tree(idx), value)
        return
      }
      val mid = (l + r) / 2
      if (pos <= mid) update(idx * 2, l, mid, pos, value)
      else update(idx * 2 + 1, mid + 1, r, pos, value)
      tree(idx) = math.max(tree(idx * 2), tree(idx * 2 + 1))
    }

    def query(idx: Int, l: Int, r: Int, ql: Int, qr: Int): Int = {
      if (qr < l || r < ql) return 0
      if (ql <= l && r <= qr) return tree(idx)
      val mid = (l + r) / 2
      math.max(query(idx * 2, l, mid, ql, qr), query(idx * 2 + 1, mid + 1, r, ql, qr))
    }
  }
}
''')

w("2408_design_sql", r'''
// LeetCode 2408 - Design SQL
// https://leetcode.com/problems/design-sql/

class SQL(_names: Array[String], _columns: Array[Int]) {
  private val tables = scala.collection.mutable.Map.empty[String, scala.collection.mutable.ArrayBuffer[List[String]]]
  private val nextID = scala.collection.mutable.Map.empty[String, Int]

  _names.foreach { name =>
    tables(name) = scala.collection.mutable.ArrayBuffer.empty[List[String]]
    nextID(name) = 1
  }

  def ins(name: String, row: List[String]): Boolean = {
    if (!tables.contains(name)) return false
    val id = nextID(name)
    nextID(name) = id + 1
    tables(name) += (id.toString :: row)
    true
  }

  def rmv(name: String, rowId: Int): Unit = {
    val rows = tables(name)
    var i = 0
    while (i < rows.length) {
      if (rows(i).head.toInt == rowId) {
        rows.remove(i)
        return
      }
      i += 1
    }
  }

  def sel(name: String, rowId: Int, columnId: Int): String = {
    tables(name).foreach { r =>
      if (r.head.toInt == rowId) {
        if (columnId < 1 || columnId >= r.length) return "<null>"
        return r(columnId)
      }
    }
    "<null>"
  }

  def exp(name: String): List[String] = {
    tables(name).map(_.mkString(",")).toList
  }
}
''')

w("2409_count_days_spent_together", r'''
// LeetCode 2409 - Count Days Spent Together
// https://leetcode.com/problems/count-days-spent-together/

object Solution {
  private val DAYS = Array(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

  def countDaysTogether(arriveAlice: String, leaveAlice: String, arriveBob: String, leaveBob: String): Int = {
    val a1 = toDay(arriveAlice)
    val a2 = toDay(leaveAlice)
    val b1 = toDay(arriveBob)
    val b2 = toDay(leaveBob)
    val start = math.max(a1, b1)
    val end = math.min(a2, b2)
    if (end < start) 0 else end - start + 1
  }

  private def toDay(s: String): Int = {
    val m = (s.charAt(0) - '0') * 10 + (s.charAt(1) - '0')
    val d = (s.charAt(3) - '0') * 10 + (s.charAt(4) - '0')
    var res = d
    var i = 0
    while (i < m - 1) {
      res += DAYS(i)
      i += 1
    }
    res
  }
}
''')

w("2410_maximum_matching_of_players_with_trainers", r'''
// LeetCode 2410 - Maximum Matching of Players With Trainers
// https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

object Solution {
  def matchPlayersAndTrainers(players: Array[Int], trainers: Array[Int]): Int = {
    java.util.Arrays.sort(players)
    java.util.Arrays.sort(trainers)
    var i = 0
    var j = 0
    var ans = 0
    while (i < players.length && j < trainers.length) {
      if (players(i) <= trainers(j)) {
        ans += 1
        i += 1
        j += 1
      } else j += 1
    }
    ans
  }
}
''')

w("2411_smallest_subarrays_with_maximum_bitwise_or", r'''
// LeetCode 2411 - Smallest Subarrays With Maximum Bitwise OR
// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

object Solution {
  def smallestSubarrays(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val ans = Array.fill(n)(0)
    val last = Array.fill(32)(-1)
    var i = n - 1
    while (i >= 0) {
      var b = 0
      while (b < 32) {
        if (((nums(i) >> b) & 1) != 0) last(b) = i
        b += 1
      }
      var far = i
      b = 0
      while (b < 32) {
        far = math.max(far, last(b))
        b += 1
      }
      ans(i) = far - i + 1
      i -= 1
    }
    ans
  }
}
''')

w("2412_minimum_money_required_before_transactions", r'''
// LeetCode 2412 - Minimum Money Required Before Transactions
// https://leetcode.com/problems/minimum-money-required-before-transactions/

object Solution {
  def minimumMoney(transactions: Array[Array[Int]]): Long = {
    var totalLoss = 0L
    var maxCashback = 0L
    var maxCost = 0L
    transactions.foreach { t =>
      val cost = t(0).toLong
      val cashback = t(1).toLong
      if (cost > cashback) {
        totalLoss += cost - cashback
        maxCashback = math.max(maxCashback, cashback)
      } else maxCost = math.max(maxCost, cost)
    }
    math.max(totalLoss + maxCashback, totalLoss + maxCost)
  }
}
''')

w("2413_smallest_even_multiple", r'''
// LeetCode 2413 - Smallest Even Multiple
// https://leetcode.com/problems/smallest-even-multiple/

object Solution {
  def smallestEvenMultiple(n: Int): Int = if (n % 2 == 0) n else n * 2
}
''')

w("2414_length_of_the_longest_alphabetical_continuous_substring", r'''
// LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

object Solution {
  def longestContinuousSubstring(s: String): Int = {
    var ans = 1
    var cur = 1
    var i = 1
    while (i < s.length) {
      if (s.charAt(i) == s.charAt(i - 1) + 1) {
        cur += 1
        ans = math.max(ans, cur)
      } else cur = 1
      i += 1
    }
    ans
  }
}
''')

w("2415_reverse_odd_levels_of_binary_tree", r'''
// LeetCode 2415 - Reverse Odd Levels of Binary Tree
// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def reverseOddLevels(root: TreeNode): TreeNode = {
    if (root != null) dfs(root.left, root.right, 1)
    root
  }

  private def dfs(a: TreeNode, b: TreeNode, level: Int): Unit = {
    if (a == null || b == null) return
    if (level % 2 == 1) {
      val tmp = a.value
      a.value = b.value
      b.value = tmp
    }
    dfs(a.left, b.right, level + 1)
    dfs(a.right, b.left, level + 1)
  }
}
''')
