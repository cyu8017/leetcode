#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("3795_minimum_subarray_length_with_distinct_sum_at_least_k", r'''
// LeetCode 3795 - Minimum Subarray Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/

object Solution {
  def minLength(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    var ans = n + 1
    var l = 0
    val cnt = new java.util.HashMap[Integer, Integer]()
    var s = 0L
    var r = 0
    while (r < n) {
      val c = cnt.merge(nums(r), 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
      if (c == 1) s += nums(r)
      while (s >= k) {
        if (r - l + 1 < ans) ans = r - l + 1
        val left = nums(l)
        val nc = cnt.merge(left, -1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
        if (nc == 0) {
          cnt.remove(left)
          s -= left
        }
        l += 1
      }
      r += 1
    }
    if (ans > n) -1 else ans
  }
}
''')

w("3796_find_maximum_value_in_a_constrained_sequence", r'''
// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

object Solution {
  def maxValue(n: Int, restrictions: Array[Array[Int]], diff: Array[Int]): Int = {
    val INF = Integer.MAX_VALUE / 4
    val bound = Array.fill(n)(INF)
    bound(0) = 0
    restrictions.foreach(r => bound(r(0)) = r(1))
    var i = 1
    while (i < n) {
      bound(i) = math.min(bound(i), bound(i - 1) + diff(i - 1))
      i += 1
    }
    i = n - 2
    while (i >= 0) {
      bound(i) = math.min(bound(i), bound(i + 1) + diff(i))
      i -= 1
    }
    var ans = bound(0)
    i = 1
    while (i < n) {
      ans = math.max(ans, bound(i))
      i += 1
    }
    ans
  }
}
''')

w("3797_count_routes_to_climb_a_rectangular_grid", r'''
// LeetCode 3797 - Count Routes To Climb A Rectangular Grid
// https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

object Solution {
  def countRoutes(grid: Array[String], d: Int): Int = {
    val MOD = 1000000007
    val n = grid.length
    val m = grid(0).length
    var upRadius = 0
    while ((upRadius + 1L) * (upRadius + 1) + 1 <= d.toLong * d) upRadius += 1
    var arrived = new Array[Int](m)
    var c = 0
    while (c < m) {
      if (grid(n - 1).charAt(c) == '.') arrived(c) = 1
      c += 1
    }
    var r = n - 1
    while (r >= 0) {
      val pref = new Array[Int](m + 1)
      var i = 0
      while (i < m) {
        pref(i + 1) = (pref(i) + arrived(i)) % MOD
        i += 1
      }
      val horizontal = new Array[Int](m)
      c = 0
      while (c < m) {
        if (grid(r).charAt(c) != '#') {
          val l = math.max(0, c - d)
          val rr = math.min(m - 1, c + d)
          horizontal(c) = (pref(rr + 1) - pref(l) - arrived(c)) % MOD
          if (horizontal(c) < 0) horizontal(c) += MOD
        }
        c += 1
      }
      if (r == 0) {
        var ans = 0
        c = 0
        while (c < m) {
          ans = (ans + arrived(c) + horizontal(c)) % MOD
          c += 1
        }
        return ans
      }
      val pref2 = new Array[Int](m + 1)
      c = 0
      while (c < m) {
        pref2(c + 1) = (pref2(c) + arrived(c) + horizontal(c)) % MOD
        c += 1
      }
      val next = new Array[Int](m)
      c = 0
      while (c < m) {
        if (grid(r - 1).charAt(c) != '#') {
          val l = math.max(0, c - upRadius)
          val rr = math.min(m - 1, c + upRadius)
          next(c) = pref2(rr + 1) - pref2(l)
          if (next(c) < 0) next(c) += MOD
        }
        c += 1
      }
      arrived = next
      r -= 1
    }
    0
  }
}
''')

w("3798_largest_even_number", r'''
// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

object Solution {
  def largestEven(s0: String): String = {
    var s = s0
    while (s.length > 0 && s.charAt(s.length - 1) == '1') s = s.substring(0, s.length - 1)
    s
  }
}
''')

w("3799_word_squares_ii", r'''
// LeetCode 3799 - Word Squares II
// https://leetcode.com/problems/word-squares-ii/

object Solution {
  def wordSquares(words: Array[String]): List[List[String]] = {
    java.util.Arrays.sort(words)
    val n = words.length
    val ans = new java.util.ArrayList[java.util.List[String]]()
    var i = 0
    while (i < n) {
      val top = words(i)
      var j = 0
      while (j < n) {
        if (j != i) {
          val left = words(j)
          var k = 0
          while (k < n) {
            if (k != j && k != i) {
              val right = words(k)
              var h = 0
              while (h < n) {
                if (h != k && h != j && h != i) {
                  val bottom = words(h)
                  if (top.charAt(0) == left.charAt(0) && top.charAt(3) == right.charAt(0) &&
                      bottom.charAt(0) == left.charAt(3) && bottom.charAt(3) == right.charAt(3)) {
                    ans.add(java.util.Arrays.asList(top, left, right, bottom))
                  }
                }
                h += 1
              }
            }
            k += 1
          }
        }
        j += 1
      }
      i += 1
    }
    val out = new scala.collection.mutable.ListBuffer[List[String]]()
    val it = ans.iterator()
    while (it.hasNext) {
      val row = it.next()
      out += List(row.get(0), row.get(1), row.get(2), row.get(3))
    }
    out.toList
  }
}
''')

w("3800_minimum_cost_to_make_two_binary_strings_equal", r'''
// LeetCode 3800 - Minimum Cost To Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

object Solution {
  def minimumCost(s: String, t: String, flipCost: Int, swapCost: Int, crossCost: Int): Long = {
    val diff = Array(0L, 0L)
    val n = s.length
    var i = 0
    while (i < n) {
      if (s.charAt(i) != t.charAt(i)) diff(s.charAt(i) - '0') += 1
      i += 1
    }
    var ans = (diff(0) + diff(1)) * flipCost
    val mx = math.max(diff(0), diff(1))
    val mn = math.min(diff(0), diff(1))
    ans = math.min(ans, mn * swapCost + (mx - mn) * flipCost)
    val avg = (mx + mn) / 2
    ans = math.min(ans, (avg - mn) * crossCost + avg * swapCost + (mx + mn - avg * 2) * flipCost)
    ans
  }
}
''')

w("3801_minimum_cost_to_merge_sorted_lists", r'''
// LeetCode 3801 - Minimum Cost To Merge Sorted Lists
// https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

object Solution {
  def minMergeCost(lists: Array[Array[Int]]): Long = {
    val m = lists.length
    val totalMasks = 1 << m
    val merged = Array.fill(totalMasks)(new java.util.ArrayList[Integer]())
    val length = new Array[Int](totalMasks)
    val median = new Array[Int](totalMasks)
    var mask = 1
    while (mask < totalMasks) {
      val bit = mask & -mask
      val index = Integer.numberOfTrailingZeros(bit)
      val previous = merged(mask ^ bit)
      val current = lists(index)
      val out = new java.util.ArrayList[Integer](previous.size() + current.length)
      var i = 0
      var j = 0
      while (i < previous.size() || j < current.length) {
        if (j == current.length || (i < previous.size() && previous.get(i) <= current(j))) {
          out.add(previous.get(i))
          i += 1
        } else {
          out.add(current(j))
          j += 1
        }
      }
      merged(mask) = out
      length(mask) = out.size()
      median(mask) = out.get((out.size() - 1) / 2)
      mask += 1
    }
    val INF = 1L << 62
    val dp = new Array[Long](totalMasks)
    mask = 1
    while (mask < totalMasks) {
      if ((mask & (mask - 1)) != 0) {
        dp(mask) = INF
        val firstBit = mask & -mask
        var left = (mask - 1) & mask
        while (left > 0) {
          if ((left & firstBit) != 0) {
            val right = mask ^ left
            if (right != 0) {
              var diff = median(left) - median(right)
              if (diff < 0) diff = -diff
              val candidate = dp(left) + dp(right) + length(mask) + diff
              if (candidate < dp(mask)) dp(mask) = candidate
            }
          }
          left = (left - 1) & mask
        }
      }
      mask += 1
    }
    dp(totalMasks - 1)
  }
}
''')

w("3802_number_of_ways_to_paint_sheets", r'''
// LeetCode 3802 - Number Of Ways To Paint Sheets
// https://leetcode.com/problems/number-of-ways-to-paint-sheets/

object Solution {
  def numberOfWays(n: Int, limit: Array[Int]): Int = {
    val MOD = 1000000007L
    java.util.Arrays.sort(limit)
    val points = new java.util.ArrayList[Integer]()
    points.add(1)
    points.add(n)
    limit.foreach { x =>
      if (x + 1 > 1 && x + 1 < n) points.add(x + 1)
      if (n - x > 1 && n - x < n) points.add(n - x)
    }
    java.util.Collections.sort(points)
    var u = 0
    var i = 0
    while (i < points.size()) {
      if (u == 0 || !points.get(i).equals(points.get(u - 1))) {
        points.set(u, points.get(i))
        u += 1
      }
      i += 1
    }
    val pts = points.subList(0, u)
    var ans = 0L
    i = 0
    while (i + 1 < pts.size()) {
      val x = pts.get(i)
      val a = countGE(limit, x)
      val b = countGE(limit, n - x)
      val same = countGE(limit, math.max(x, n - x))
      val ways = (a * b - same) % MOD
      val length = pts.get(i + 1).toLong - x
      ans = (ans + ways * length) % MOD
      i += 1
    }
    if (ans < 0) ans += MOD
    ans.toInt
  }

  private def countGE(limit: Array[Int], x: Int): Long = {
    var lo = 0
    var hi = limit.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (limit(mid) < x) lo = mid + 1
      else hi = mid
    }
    limit.length - lo
  }
}
''')

w("3803_count_residue_prefixes", r'''
// LeetCode 3803 - Count Residue Prefixes
// https://leetcode.com/problems/count-residue-prefixes/

object Solution {
  def residuePrefixes(s: String): Int = {
    val st = new java.util.HashSet[Character]()
    var ans = 0
    var i = 0
    while (i < s.length) {
      st.add(s.charAt(i))
      if (st.size() == (i + 1) % 3) ans += 1
      i += 1
    }
    ans
  }
}
''')

w("3804_number_of_centered_subarrays", r'''
// LeetCode 3804 - Number Of Centered Subarrays
// https://leetcode.com/problems/number-of-centered-subarrays/

object Solution {
  def centeredSubarrays(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      val st = new java.util.HashSet[Integer]()
      var s = 0
      var j = i
      while (j < n) {
        s += nums(j)
        st.add(nums(j))
        if (st.contains(s)) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("3805_count_caesar_cipher_pairs", r'''
// LeetCode 3805 - Count Caesar Cipher Pairs
// https://leetcode.com/problems/count-caesar-cipher-pairs/

object Solution {
  def countPairs(words: Array[String]): Long = {
    val cnt = new java.util.HashMap[String, Integer]()
    words.foreach { word =>
      val s = word.toCharArray
      val k = 'z' - s(0)
      var i = 1
      while (i < s.length) {
        s(i) = ('a' + (s(i) - 'a' + k) % 26).toChar
        i += 1
      }
      s(0) = 'z'
      val key = new String(s)
      if (!cnt.containsKey(key)) cnt.put(key, 0)
      cnt.merge(key, 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
    }
    var ans = 0L
    val it = cnt.values().iterator()
    while (it.hasNext) {
      val v = it.next()
      ans += v.toLong * (v - 1) / 2
    }
    ans
  }
}
''')

w("3806_maximum_bitwise_and_after_increment_operations", r'''
// LeetCode 3806 - Maximum Bitwise And After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

object Solution {
  private def BitLen(x0: Int): Int = {
    var x = x0
    if (x == 0) return 0
    var n = 0
    while (x > 0) { n += 1; x >>= 1 }
    n
  }

  def maximumAND(nums: Array[Int], k: Int, m: Int): Int = {
    var mxVal = nums(0)
    nums.foreach(v => if (v > mxVal) mxVal = v)
    mxVal += k
    val mx = BitLen(mxVal)
    var ans = 0
    val cost = new Array[Int](nums.length)
    var bit = mx - 1
    while (bit >= 0) {
      val target = ans | (1 << bit)
      var i = 0
      while (i < nums.length) {
        val x = nums(i)
        val j = BitLen(target & ~x)
        val mask = (1 << j) - 1
        cost(i) = (target & mask) - (x & mask)
        i += 1
      }
      java.util.Arrays.sort(cost)
      var sum = 0
      i = 0
      while (i < m) {
        sum += cost(i)
        i += 1
      }
      if (sum <= k) ans = target
      bit -= 1
    }
    ans
  }
}
''')

w("3807_minimum_cost_to_repair_edges_to_traverse_a_graph", r'''
// LeetCode 3807 - Minimum Cost To Repair Edges To Traverse A Graph
// https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

object Solution {
  def minCost(n: Int, edges: Array[Array[Int]], k: Int): Int = {
    java.util.Arrays.sort(edges, (a: Array[Int], b: Array[Int]) => Integer.compare(a(2), b(2)))
    val m = edges.length
    if (m == 0) return -1

    def check(idx: Int): Boolean = {
      val g = Array.fill(n)(new java.util.ArrayList[Integer]())
      var i = 0
      while (i <= idx) {
        g(edges(i)(0)).add(edges(i)(1))
        g(edges(i)(1)).add(edges(i)(0))
        i += 1
      }
      var q = new java.util.ArrayList[Integer]()
      q.add(0)
      val vis = new Array[Boolean](n)
      vis(0) = true
      var dist = 0
      while (!q.isEmpty) {
        val nq = new java.util.ArrayList[Integer]()
        val it = q.iterator()
        while (it.hasNext) {
          val u = it.next()
          if (u == n - 1) return dist <= k
          val it2 = g(u).iterator()
          while (it2.hasNext) {
            val v = it2.next()
            if (!vis(v)) {
              vis(v) = true
              nq.add(v)
            }
          }
        }
        q = nq
        dist += 1
      }
      false
    }

    var l = 0
    var r = m - 1
    while (l < r) {
      val mid = (l + r) >> 1
      if (check(mid)) r = mid
      else l = mid + 1
    }
    if (check(l)) edges(l)(2) else -1
  }
}
''')

w("3809_best_reachable_tower", r'''
// LeetCode 3809 - Best Reachable Tower
// https://leetcode.com/problems/best-reachable-tower/

object Solution {
  def bestTower(towers: Array[Array[Int]], center: Array[Int], radius: Int): Array[Int] = {
    val cx = center(0)
    val cy = center(1)
    var idx = -1
    var i = 0
    while (i < towers.length) {
      val x = towers(i)(0)
      val y = towers(i)(1)
      val q = towers(i)(2)
      val dist = math.abs(x - cx) + math.abs(y - cy)
      if (dist <= radius) {
        if (idx == -1 || towers(idx)(2) < q ||
            (towers(idx)(2) == q &&
             (x < towers(idx)(0) || (x == towers(idx)(0) && y < towers(idx)(1))))) {
          idx = i
        }
      }
      i += 1
    }
    if (idx == -1) Array(-1, -1) else Array(towers(idx)(0), towers(idx)(1))
  }
}
''')

w("3810_minimum_operations_to_reach_target_array", r'''
// LeetCode 3810 - Minimum Operations To Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

object Solution {
  def minOperations(nums: Array[Int], target: Array[Int]): Int = {
    val s = new java.util.HashSet[Integer]()
    var i = 0
    while (i < nums.length) {
      if (nums(i) != target(i)) s.add(nums(i))
      i += 1
    }
    s.size()
  }
}
''')

w("3811_number_of_alternating_xor_partitions", r'''
// LeetCode 3811 - Number Of Alternating Xor Partitions
// https://leetcode.com/problems/number-of-alternating-xor-partitions/

object Solution {
  def alternatingXOR(nums: Array[Int], target1: Int, target2: Int): Int = {
    val MOD = 1000000007
    val cnt1 = new java.util.HashMap[Integer, Integer]()
    val cnt2 = new java.util.HashMap[Integer, Integer]()
    cnt2.put(0, 1)
    var pre = 0
    var ans = 0
    nums.foreach { x =>
      pre ^= x
      val a = cnt2.getOrDefault(pre ^ target1, 0)
      val b = cnt1.getOrDefault(pre ^ target2, 0)
      ans = (a + b) % MOD
      cnt1.merge(pre, a, (x1: Integer, y1: Integer) => Integer.valueOf((x1 + y1) % MOD))
      cnt2.merge(pre, b, (x1: Integer, y1: Integer) => Integer.valueOf((x1 + y1) % MOD))
    }
    ans
  }
}
''')

w("3812_minimum_edge_toggles_on_a_tree", r'''
// LeetCode 3812 - Minimum Edge Toggles On A Tree
// https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/

object Solution {
  def minimumFlips(n: Int, edges: Array[Array[Int]], start: String, target: String): Array[Int] = {
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    var i = 0
    while (i < n - 1) {
      val a = edges(i)(0)
      val b = edges(i)(1)
      g(a).add(Array(b, i))
      g(b).add(Array(a, i))
      i += 1
    }
    val ans = new java.util.ArrayList[Integer]()

    def dfs(a: Int, fa: Int): Boolean = {
      var rev = start.charAt(a) != target.charAt(a)
      val it = g(a).iterator()
      while (it.hasNext) {
        val e = it.next()
        val b = e(0)
        val ei = e(1)
        if (b != fa && dfs(b, a)) {
          ans.add(ei)
          rev = !rev
        }
      }
      rev
    }

    if (dfs(0, -1)) return Array(-1)
    java.util.Collections.sort(ans)
    val out = new Array[Int](ans.size())
    i = 0
    while (i < out.length) {
      out(i) = ans.get(i)
      i += 1
    }
    out
  }
}
''')

w("3813_vowel_consonant_score", r'''
// LeetCode 3813 - Vowel Consonant Score
// https://leetcode.com/problems/vowel-consonant-score/

object Solution {
  def vowelConsonantScore(s: String): Int = {
    var v = 0
    var c = 0
    s.foreach { ch =>
      if (Character.isLetter(ch)) {
        c += 1
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') v += 1
      }
    }
    c -= v
    if (c == 0) 0 else v / c
  }
}
''')

w("3814_maximum_capacity_within_budget", r'''
// LeetCode 3814 - Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum-capacity-within-budget/

object Solution {
  def maxCapacity(costs: Array[Int], capacity: Array[Int], budget: Int): Int = {
    val arr = new java.util.ArrayList[Array[Int]]()
    var k = 0
    while (k < costs.length) {
      if (costs(k) < budget) arr.add(Array(costs(k), capacity(k)))
      k += 1
    }
    if (arr.isEmpty) return 0
    arr.sort((a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    val m = arr.size()
    val alive = Array.fill(m)(true)
    val h = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) => {
      if (a(0) != b(0)) Integer.compare(b(0), a(0))
      else Integer.compare(b(1), a(1))
    })
    var i = 0
    while (i < m) {
      h.offer(Array(arr.get(i)(1), i))
      i += 1
    }
    while (!h.isEmpty && !alive(h.peek()(1))) h.poll()
    var ans = h.peek()(0)
    i = 0
    var j = m - 1
    while (i < j) {
      alive(i) = false
      while (i < j && arr.get(i)(0) + arr.get(j)(0) >= budget) {
        alive(j) = false
        j -= 1
      }
      while (!h.isEmpty && !alive(h.peek()(1))) h.poll()
      if (!h.isEmpty) ans = math.max(ans, arr.get(i)(1) + h.peek()(0))
      i += 1
    }
    ans
  }
}
''')

w("3815_design_auction_system", r'''
// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design-auction-system/

class AuctionSystem() {
  private class Bid(val amount: Int, val userId: Int)

  private val bids = new java.util.HashMap[Integer, java.util.Map[Integer, Integer]]()
  private val heaps = new java.util.HashMap[Integer, java.util.PriorityQueue[Bid]]()

  def addBid(userId: Int, itemId: Int, bidAmount: Int): Unit = {
    bids.computeIfAbsent(itemId, _ => new java.util.HashMap[Integer, Integer]()).put(userId, bidAmount)
    heaps.computeIfAbsent(itemId, _ => new java.util.PriorityQueue[Bid]((a: Bid, b: Bid) => {
      if (a.amount != b.amount) Integer.compare(b.amount, a.amount)
      else Integer.compare(b.userId, a.userId)
    })).offer(new Bid(bidAmount, userId))
  }

  def updateBid(userId: Int, itemId: Int, newAmount: Int): Unit = {
    addBid(userId, itemId, newAmount)
  }

  def removeBid(userId: Int, itemId: Int): Unit = {
    val m = bids.get(itemId)
    if (m != null) m.remove(userId)
  }

  def getHighestBidder(itemId: Int): Int = {
    val h = heaps.get(itemId)
    if (h == null) return -1
    val m = bids.getOrDefault(itemId, java.util.Collections.emptyMap[Integer, Integer]())
    while (!h.isEmpty) {
      val top = h.peek()
      val cur = m.get(top.userId)
      if (cur != null && cur == top.amount) return top.userId
      h.poll()
    }
    -1
  }
}
''')

w("3816_lexicographically_smallest_string_after_deleting_duplicate_characters", r'''
// LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

object Solution {
  def lexSmallestAfterDeletion(s: String): String = {
    val cnt = new Array[Int](26)
    s.foreach(c => cnt(c - 'a') += 1)
    val stk = new StringBuilder
    s.foreach { c =>
      while (stk.length > 0 && stk.charAt(stk.length - 1) > c
          && cnt(stk.charAt(stk.length - 1) - 'a') > 1) {
        cnt(stk.charAt(stk.length - 1) - 'a') -= 1
        stk.deleteCharAt(stk.length - 1)
      }
      stk.append(c)
    }
    while (cnt(stk.charAt(stk.length - 1) - 'a') > 1) {
      cnt(stk.charAt(stk.length - 1) - 'a') -= 1
      stk.deleteCharAt(stk.length - 1)
    }
    stk.toString
  }
}
''')

w("3817_good_indices_in_a_digit_string", r'''
// LeetCode 3817 - Good Indices In A Digit String
// https://leetcode.com/problems/good-indices-in-a-digit-string/

object Solution {
  def goodIndices(s: String): Array[Int] = {
    val ans = new java.util.ArrayList[Integer]()
    var i = 0
    while (i < s.length) {
      val t = String.valueOf(i)
      val k = t.length
      if (i + 1 - k >= 0 && s.substring(i + 1 - k, k) == t) ans.add(i)
      i += 1
    }
    val out = new Array[Int](ans.size())
    i = 0
    while (i < out.length) {
      out(i) = ans.get(i)
      i += 1
    }
    out
  }
}
''')

w("3818_minimum_prefix_removal_to_make_array_strictly_increasing", r'''
// LeetCode 3818 - Minimum Prefix Removal To Make Array Strictly Increasing
// https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

object Solution {
  def minimumPrefixLength(nums: Array[Int]): Int = {
    var i = nums.length - 1
    while (i > 0) {
      if (nums(i - 1) >= nums(i)) return i
      i -= 1
    }
    0
  }
}
''')

w("3819_rotate_non_negative_elements", r'''
// LeetCode 3819 - Rotate Non Negative Elements
// https://leetcode.com/problems/rotate-non-negative-elements/

object Solution {
  def rotateElements(nums: Array[Int], k: Int): Array[Int] = {
    val t = new java.util.ArrayList[Integer]()
    nums.foreach(x => if (x >= 0) t.add(x))
    val m = t.size()
    if (m == 0) return nums
    val d = new Array[Int](m)
    var i = 0
    while (i < m) {
      d(((i - k) % m + m) % m) = t.get(i)
      i += 1
    }
    var j = 0
    i = 0
    while (i < nums.length) {
      if (nums(i) >= 0) {
        nums(i) = d(j)
        j += 1
      }
      i += 1
    }
    nums
  }
}
''')

w("3820_pythagorean_distance_nodes_in_a_tree", r'''
// LeetCode 3820 - Pythagorean Distance Nodes In A Tree
// https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

object Solution {
  def specialNodes(n: Int, edges: Array[Array[Int]], x: Int, y: Int, z: Int): Int = {
    val g = Array.fill(n)(new java.util.ArrayList[Integer]())
    edges.foreach { e =>
      g(e(0)).add(e(1))
      g(e(1)).add(e(0))
    }

    def bfs(start: Int): Array[Int] = {
      val dist = Array.fill(n)(1000000000)
      val q = new java.util.ArrayDeque[Integer]()
      dist(start) = 0
      q.offer(start)
      while (!q.isEmpty) {
        val u = q.poll()
        val it = g(u).iterator()
        while (it.hasNext) {
          val v = it.next()
          if (dist(v) > dist(u) + 1) {
            dist(v) = dist(u) + 1
            q.offer(v)
          }
        }
      }
      dist
    }

    val d1 = bfs(x)
    val d2 = bfs(y)
    val d3 = bfs(z)
    var ans = 0
    var i = 0
    while (i < n) {
      val a = Array(d1(i), d2(i), d3(i))
      java.util.Arrays.sort(a)
      val x0 = a(0).toLong
      val x1 = a(1).toLong
      val x2 = a(2).toLong
      if (x0 * x0 + x1 * x1 == x2 * x2) ans += 1
      i += 1
    }
    ans
  }
}
''')

w("3821_find_nth_smallest_integer_with_k_one_bits", r'''
// LeetCode 3821 - Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/

object Solution {
  private val MX = 50
  private val C: Array[Array[Long]] = {
    val arr = Array.ofDim[Long](MX, MX + 1)
    var i = 0
    while (i < MX) {
      arr(i)(0) = 1
      var j = 1
      while (j <= i) {
        arr(i)(j) = arr(i - 1)(j - 1) + arr(i - 1)(j)
        j += 1
      }
      i += 1
    }
    arr
  }

  def nthSmallest(n0: Long, k0: Int): Long = {
    var n = n0
    var k = k0
    var ans = 0L
    var i = 49
    while (i >= 0) {
      if (n > C(i)(k)) {
        n -= C(i)(k)
        ans |= 1L << i
        k -= 1
        if (k == 0) return ans
      }
      i -= 1
    }
    ans
  }
}
''')
