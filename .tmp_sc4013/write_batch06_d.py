#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)


w("2274_maximum_consecutive_floors_without_special_floors", r'''
// LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

object Solution {
  def maxConsecutive(bottom: Int, top: Int, special: Array[Int]): Int = {
    java.util.Arrays.sort(special)
    var ans = special(0) - bottom
    var i = 1
    while (i < special.length) {
      ans = math.max(ans, special(i) - special(i - 1) - 1)
      i += 1
    }
    math.max(ans, top - special(special.length - 1))
  }
}
''')

w("2275_largest_combination_with_bitwise_and_greater_than_zero", r'''
// LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

object Solution {
  def largestCombination(candidates: Array[Int]): Int = {
    var ans = 0
    var bit = 0
    while (bit < 24) {
      var cnt = 0
      for (x <- candidates) if (((x >> bit) & 1) != 0) cnt += 1
      ans = math.max(ans, cnt)
      bit += 1
    }
    ans
  }
}
''')

w("2276_count_integers_in_intervals", r'''
// LeetCode 2276 - Count Integers in Intervals
// https://leetcode.com/problems/count-integers-in-intervals/

class CountIntervals() {
  private class SegNode {
    var left: SegNode = null
    var right: SegNode = null
    var covered: Boolean = false
  }

  private var root: SegNode = null
  private var cnt: Int = 0

  private def addRange(L: Int, R: Int, l: Int, r: Int, node0: SegNode): (Int, SegNode) = {
    var node = node0
    if (node == null) node = new SegNode
    if (node.covered) return (0, node)
    if (l <= L && R <= r) {
      node.covered = true
      node.left = null
      node.right = null
      return (R - L + 1, node)
    }
    val mid = (L + R) / 2
    var added = 0
    if (l <= mid) {
      val res = addRange(L, mid, l, r, node.left)
      added += res._1
      node.left = res._2
    }
    if (r > mid) {
      val res = addRange(mid + 1, R, l, r, node.right)
      added += res._1
      node.right = res._2
    }
    if (node.left != null && node.right != null && node.left.covered && node.right.covered) {
      node.covered = true
      node.left = null
      node.right = null
    }
    (added, node)
  }

  def add(left: Int, right: Int): Unit = {
    val res = addRange(1, 1000000000, left, right, root)
    cnt += res._1
    root = res._2
  }

  def count(): Int = cnt
}
''')

w("2277_closest_node_to_path_in_tree", r'''
// LeetCode 2277 - Closest Node to Path in Tree
// https://leetcode.com/problems/closest-node-to-path-in-tree/

object Solution {
  def closestNode(n: Int, edges: Array[Array[Int]], query: Array[Array[Int]]): Array[Int] = {
    val LOG = 17
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val up = Array.ofDim[Int](LOG, n)
    val depth = new Array[Int](n)
    def dfs(u: Int, p: Int): Unit = {
      up(0)(u) = p
      for (v <- g(u) if v != p) {
        depth(v) = depth(u) + 1
        dfs(v, u)
      }
    }
    dfs(0, 0)
    var k = 1
    while (k < LOG) {
      var v = 0
      while (v < n) {
        up(k)(v) = up(k - 1)(up(k - 1)(v))
        v += 1
      }
      k += 1
    }
    def lift(v0: Int, d: Int): Int = {
      var v = v0
      var kk = 0
      while (kk < LOG) {
        if (((d >> kk) & 1) != 0) v = up(kk)(v)
        kk += 1
      }
      v
    }
    def lca(a0: Int, b0: Int): Int = {
      var a = a0
      var b = b0
      if (depth(a) < depth(b)) {
        val t = a
        a = b
        b = t
      }
      a = lift(a, depth(a) - depth(b))
      if (a == b) return a
      k = LOG - 1
      while (k >= 0) {
        if (up(k)(a) != up(k)(b)) {
          a = up(k)(a)
          b = up(k)(b)
        }
        k -= 1
      }
      up(0)(a)
    }
    def dist(a: Int, b: Int): Int = {
      val c = lca(a, b)
      depth(a) + depth(b) - 2 * depth(c)
    }
    val ans = new Array[Int](query.length)
    var i = 0
    while (i < query.length) {
      val a = query(i)(0)
      val b = query(i)(1)
      val x = query(i)(2)
      val cands = Array(lca(a, b), lca(a, x), lca(b, x))
      var best = cands(0)
      var bestD = dist(cands(0), x)
      var t = 1
      while (t < 3) {
        val d = dist(cands(t), x)
        if (d < bestD) {
          bestD = d
          best = cands(t)
        }
        t += 1
      }
      ans(i) = best
      i += 1
    }
    ans
  }
}
''')

w("2278_percentage_of_letter_in_string", r'''
// LeetCode 2278 - Percentage of Letter in String
// https://leetcode.com/problems/percentage-of-letter-in-string/

object Solution {
  def percentageLetter(s: String, letter: Char): Int = {
    var cnt = 0
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == letter) cnt += 1
      i += 1
    }
    cnt * 100 / s.length
  }
}
''')

w("2279_maximum_bags_with_full_capacity_of_rocks", r'''
// LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

object Solution {
  def maximumBags(capacity: Array[Int], rocks: Array[Int], additionalRocks0: Int): Int = {
    val need = new Array[Int](capacity.length)
    var i = 0
    while (i < capacity.length) {
      need(i) = capacity(i) - rocks(i)
      i += 1
    }
    java.util.Arrays.sort(need)
    var additionalRocks = additionalRocks0
    var ans = 0
    for (n <- need) {
      if (additionalRocks < n) return ans
      additionalRocks -= n
      ans += 1
    }
    ans
  }
}
''')

w("2280_minimum_lines_to_represent_a_line_chart", r'''
// LeetCode 2280 - Minimum Lines to Represent a Line Chart
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

object Solution {
  def minimumLines(stockPrices: Array[Array[Int]]): Int = {
    if (stockPrices.length <= 1) return 0
    java.util.Arrays.sort(stockPrices, (a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    var ans = 1
    var i = 2
    while (i < stockPrices.length) {
      val x0 = stockPrices(i - 2)(0).toLong
      val y0 = stockPrices(i - 2)(1).toLong
      val x1 = stockPrices(i - 1)(0).toLong
      val y1 = stockPrices(i - 1)(1).toLong
      val x2 = stockPrices(i)(0).toLong
      val y2 = stockPrices(i)(1).toLong
      if ((y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0)) ans += 1
      i += 1
    }
    ans
  }
}
''')

w("2281_sum_of_total_strength_of_wizards", r'''
// LeetCode 2281 - Sum of Total Strength of Wizards
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/

object Solution {
  def totalStrength(strength: Array[Int]): Int = {
    val mod = 1000000007
    val n = strength.length
    val left = new Array[Int](n)
    val right = new Array[Int](n)
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < n) {
      while (stack.nonEmpty && strength(stack.last) >= strength(i)) stack.remove(stack.length - 1)
      left(i) = if (stack.isEmpty) -1 else stack.last
      stack += i
      i += 1
    }
    stack.clear()
    i = n - 1
    while (i >= 0) {
      while (stack.nonEmpty && strength(stack.last) > strength(i)) stack.remove(stack.length - 1)
      right(i) = if (stack.isEmpty) n else stack.last
      stack += i
      i -= 1
    }
    val pref = new Array[Long](n + 1)
    val prefPref = new Array[Long](n + 2)
    i = 0
    while (i < n) {
      pref(i + 1) = (pref(i) + strength(i)) % mod
      i += 1
    }
    i = 0
    while (i <= n) {
      prefPref(i + 1) = (prefPref(i) + pref(i)) % mod
      i += 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      val l = left(i) + 1
      val r = right(i) - 1
      val leftSum = (prefPref(i + 1) - prefPref(l) + mod) % mod
      val rightSum = (prefPref(r + 2) - prefPref(i + 1) + mod) % mod
      val leftCnt = i - l + 1L
      val rightCnt = r - i + 1L
      val contrib = (rightCnt * leftSum % mod - leftCnt * rightSum % mod + mod) % mod
      ans = (ans + contrib * strength(i) % mod) % mod
      i += 1
    }
    ans.toInt
  }
}
''')

w("2282_number_of_people_that_can_be_seen_in_a_grid", r'''
// LeetCode 2282 - Number of People That Can Be Seen in a Grid
// https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

object Solution {
  def seePeople(heights: Array[Array[Int]]): Array[Array[Int]] = {
    val m = heights.length
    val n = heights(0).length
    val ans = Array.ofDim[Int](m, n)
    var i = 0
    while (i < m) {
      val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
      var j = n - 1
      while (j >= 0) {
        var cnt = 0
        while (stack.nonEmpty && heights(i)(stack.last) < heights(i)(j)) {
          stack.remove(stack.length - 1)
          cnt += 1
        }
        if (stack.nonEmpty) cnt += 1
        ans(i)(j) += cnt
        while (stack.nonEmpty && heights(i)(stack.last) == heights(i)(j)) stack.remove(stack.length - 1)
        stack += j
        j -= 1
      }
      i += 1
    }
    var j = 0
    while (j < n) {
      val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
      i = m - 1
      while (i >= 0) {
        var cnt = 0
        while (stack.nonEmpty && heights(stack.last)(j) < heights(i)(j)) {
          stack.remove(stack.length - 1)
          cnt += 1
        }
        if (stack.nonEmpty) cnt += 1
        ans(i)(j) += cnt
        while (stack.nonEmpty && heights(stack.last)(j) == heights(i)(j)) stack.remove(stack.length - 1)
        stack += i
        i -= 1
      }
      j += 1
    }
    ans
  }
}
''')

w("2283_check_if_number_has_equal_digit_count_and_digit_value", r'''
// LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

object Solution {
  def digitCount(num: String): Boolean = {
    val cnt = new Array[Int](10)
    var i = 0
    while (i < num.length) {
      cnt(num.charAt(i) - '0') += 1
      i += 1
    }
    i = 0
    while (i < num.length) {
      if (cnt(i) != num.charAt(i) - '0') return false
      i += 1
    }
    true
  }
}
''')

w("2284_sender_with_largest_word_count", r'''
// LeetCode 2284 - Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/

object Solution {
  def largestWordCount(messages: Array[String], senders: Array[String]): String = {
    val count = scala.collection.mutable.HashMap.empty[String, Int]
    var best = ""
    var bestCnt = -1
    var i = 0
    while (i < messages.length) {
      var words = 1
      var j = 0
      while (j < messages(i).length) {
        if (messages(i).charAt(j) == ' ') words += 1
        j += 1
      }
      val prev = count.getOrElse(senders(i), 0)
      count(senders(i)) = prev + words
      val c2 = count(senders(i))
      if (c2 > bestCnt || (c2 == bestCnt && senders(i).compareTo(best) > 0)) {
        bestCnt = c2
        best = senders(i)
      }
      i += 1
    }
    best
  }
}
''')

w("2285_maximum_total_importance_of_roads", r'''
// LeetCode 2285 - Maximum Total Importance of Roads
// https://leetcode.com/problems/maximum-total-importance-of-roads/

object Solution {
  def maximumImportance(n: Int, roads: Array[Array[Int]]): Long = {
    val deg = new Array[Int](n)
    for (r <- roads) {
      deg(r(0)) += 1
      deg(r(1)) += 1
    }
    java.util.Arrays.sort(deg)
    var ans = 0L
    var i = 0
    while (i < n) {
      ans += deg(i).toLong * (i + 1)
      i += 1
    }
    ans
  }
}
''')

w("2286_booking_concert_tickets_in_groups", r'''
// LeetCode 2286 - Booking Concert Tickets in Groups
// https://leetcode.com/problems/booking-concert-tickets-in-groups/

class BookMyShow(_n: Int, _m: Int) {
  private val n = _n
  private val m = _m
  private val sum = new Array[Long](4 * n)
  private val mx = new Array[Long](4 * n)

  private def pull(idx: Int): Unit = {
    sum(idx) = sum(idx * 2) + sum(idx * 2 + 1)
    mx(idx) = math.max(mx(idx * 2), mx(idx * 2 + 1))
  }

  private def build(idx: Int, l: Int, r: Int): Unit = {
    if (l == r) {
      sum(idx) = m
      mx(idx) = m
      return
    }
    val mid = (l + r) / 2
    build(idx * 2, l, mid)
    build(idx * 2 + 1, mid + 1, r)
    pull(idx)
  }

  private def update(idx: Int, l: Int, r: Int, pos: Int, value: Long): Unit = {
    if (l == r) {
      sum(idx) = value
      mx(idx) = value
      return
    }
    val mid = (l + r) / 2
    if (pos <= mid) update(idx * 2, l, mid, pos, value)
    else update(idx * 2 + 1, mid + 1, r, pos, value)
    pull(idx)
  }

  private def querySum(idx: Int, l: Int, r: Int, ql: Int, qr: Int): Long = {
    if (qr < l || r < ql) return 0L
    if (ql <= l && r <= qr) return sum(idx)
    val mid = (l + r) / 2
    querySum(idx * 2, l, mid, ql, qr) + querySum(idx * 2 + 1, mid + 1, r, ql, qr)
  }

  private def findFirst(idx: Int, l: Int, r: Int, maxRow: Int, k: Long): Int = {
    if (l > maxRow || mx(idx) < k) return -1
    if (l == r) return l
    val mid = (l + r) / 2
    val left = findFirst(idx * 2, l, mid, maxRow, k)
    if (left != -1) left else findFirst(idx * 2 + 1, mid + 1, r, maxRow, k)
  }

  build(1, 0, n - 1)

  def gather(k: Int, maxRow: Int): Array[Int] = {
    val row = findFirst(1, 0, n - 1, maxRow, k)
    if (row == -1) return Array.empty[Int]
    val remain = querySum(1, 0, n - 1, row, row)
    val seat = (m - remain).toInt
    update(1, 0, n - 1, row, remain - k)
    Array(row, seat)
  }

  def scatter(k: Int, maxRow: Int): Boolean = {
    if (querySum(1, 0, n - 1, 0, maxRow) < k) return false
    var need = k.toLong
    var row = 0
    while (row <= maxRow && need > 0) {
      val remain = querySum(1, 0, n - 1, row, row)
      if (remain != 0) {
        val take = math.min(remain, need)
        update(1, 0, n - 1, row, remain - take)
        need -= take
      }
      row += 1
    }
    true
  }
}
''')

w("2287_rearrange_characters_to_make_target_string", r'''
// LeetCode 2287 - Rearrange Characters to Make Target String
// https://leetcode.com/problems/rearrange-characters-to-make-target-string/

object Solution {
  def rearrangeCharacters(s: String, target: String): Int = {
    val sc = new Array[Int](26)
    val tc = new Array[Int](26)
    var i = 0
    while (i < s.length) {
      sc(s.charAt(i) - 'a') += 1
      i += 1
    }
    i = 0
    while (i < target.length) {
      tc(target.charAt(i) - 'a') += 1
      i += 1
    }
    var ans = Int.MaxValue
    i = 0
    while (i < 26) {
      if (tc(i) != 0) ans = math.min(ans, sc(i) / tc(i))
      i += 1
    }
    ans
  }
}
''')

w("2288_apply_discount_to_prices", r'''
// LeetCode 2288 - Apply Discount to Prices
// https://leetcode.com/problems/apply-discount-to-prices/

object Solution {
  def discountPrices(sentence: String, discount: Int): String = {
    val parts = sentence.split(" ")
    var i = 0
    while (i < parts.length) {
      val part = parts(i)
      if (part.length >= 2 && part.charAt(0) == '$') {
        var ok = true
        var j = 1
        while (j < part.length) {
          val ch = part.charAt(j)
          if (ch < '0' || ch > '9') ok = false
          j += 1
        }
        if (ok) {
          val value = part.substring(1).toLong
          val price = value * (100.0 - discount) / 100.0
          parts(i) = f"$$$price%.2f"
        }
      }
      i += 1
    }
    parts.mkString(" ")
  }
}
''')

w("2289_steps_to_make_array_non_decreasing", r'''
// LeetCode 2289 - Steps to Make Array Non-decreasing
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/

object Solution {
  def totalSteps(nums: Array[Int]): Int = {
    val stack = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var ans = 0
    var i = nums.length - 1
    while (i >= 0) {
      var steps = 0
      while (stack.nonEmpty && nums(i) > stack.last(0)) {
        steps = math.max(steps, stack.last(1))
        stack.remove(stack.length - 1)
        steps += 1
      }
      ans = math.max(ans, steps)
      stack += Array(nums(i), steps)
      i -= 1
    }
    ans
  }
}
''')

w("2290_minimum_obstacle_removal_to_reach_corner", r'''
// LeetCode 2290 - Minimum Obstacle Removal to Reach Corner
// https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

object Solution {
  def minimumObstacles(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val dist = Array.fill(m, n)(Int.MaxValue / 2)
    dist(0)(0) = 0
    val dq = scala.collection.mutable.ArrayDeque.empty[(Int, Int)]
    dq.append((0, 0))
    val dirs = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))
    while (dq.nonEmpty) {
      val (r, c) = dq.removeHead()
      for (d <- dirs) {
        val nr = r + d(0)
        val nc = c + d(1)
        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
          val nd = dist(r)(c) + grid(nr)(nc)
          if (nd < dist(nr)(nc)) {
            dist(nr)(nc) = nd
            if (grid(nr)(nc) == 0) dq.prepend((nr, nc))
            else dq.append((nr, nc))
          }
        }
      }
    }
    dist(m - 1)(n - 1)
  }
}
''')

w("2291_maximum_profit_from_trading_stocks", r'''
// LeetCode 2291 - Maximum Profit From Trading Stocks
// https://leetcode.com/problems/maximum-profit-from-trading-stocks/

object Solution {
  def maximumProfit(present: Array[Int], future: Array[Int], budget: Int): Int = {
    val n = present.length
    val dp = new Array[Int](budget + 1)
    var i = 0
    while (i < n) {
      val profit = future(i) - present(i)
      if (profit > 0) {
        val cost = present(i)
        var b = budget
        while (b >= cost) {
          dp(b) = math.max(dp(b), dp(b - cost) + profit)
          b -= 1
        }
      }
      i += 1
    }
    dp(budget)
  }
}
''')

w("2293_min_max_game", r'''
// LeetCode 2293 - Min Max Game
// https://leetcode.com/problems/min-max-game/

object Solution {
  def minMaxGame(nums: Array[Int]): Int = {
    var cur = nums
    while (cur.length > 1) {
      val next = new Array[Int](cur.length / 2)
      var i = 0
      while (i < next.length) {
        if (i % 2 == 0) next(i) = math.min(cur(2 * i), cur(2 * i + 1))
        else next(i) = math.max(cur(2 * i), cur(2 * i + 1))
        i += 1
      }
      cur = next
    }
    cur(0)
  }
}
''')

w("2294_partition_array_such_that_maximum_difference_is_k", r'''
// LeetCode 2294 - Partition Array Such That Maximum Difference Is K
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

object Solution {
  def partitionArray(nums: Array[Int], k: Int): Int = {
    java.util.Arrays.sort(nums)
    var ans = 1
    var start = nums(0)
    var i = 1
    while (i < nums.length) {
      if (nums(i) - start > k) {
        ans += 1
        start = nums(i)
      }
      i += 1
    }
    ans
  }
}
''')

w("2295_replace_elements_in_an_array", r'''
// LeetCode 2295 - Replace Elements in an Array
// https://leetcode.com/problems/replace-elements-in-an-array/

object Solution {
  def arrayChange(nums: Array[Int], operations: Array[Array[Int]]): Array[Int] = {
    val pos = scala.collection.mutable.HashMap.empty[Int, Int]
    var i = 0
    while (i < nums.length) {
      pos(nums(i)) = i
      i += 1
    }
    for (op <- operations) {
      val idx = pos(op(0))
      nums(idx) = op(1)
      pos.remove(op(0))
      pos(op(1)) = idx
    }
    nums
  }
}
''')

w("2296_design_a_text_editor", r'''
// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

class TextEditor() {
  private val left = scala.collection.mutable.ArrayBuffer.empty[Char]
  private val right = scala.collection.mutable.ArrayBuffer.empty[Char]

  private def suffix(): String = {
    val start = math.max(0, left.length - 10)
    val sb = new StringBuilder
    var i = start
    while (i < left.length) {
      sb.append(left(i))
      i += 1
    }
    sb.toString
  }

  def addText(text: String): Unit = {
    var i = 0
    while (i < text.length) {
      left += text.charAt(i)
      i += 1
    }
  }

  def deleteText(k0: Int): Int = {
    var k = k0
    var deleted = 0
    while (k > 0 && left.nonEmpty) {
      left.remove(left.length - 1)
      k -= 1
      deleted += 1
    }
    deleted
  }

  def cursorLeft(k0: Int): String = {
    var k = k0
    while (k > 0 && left.nonEmpty) {
      right += left.remove(left.length - 1)
      k -= 1
    }
    suffix()
  }

  def cursorRight(k0: Int): String = {
    var k = k0
    while (k > 0 && right.nonEmpty) {
      left += right.remove(right.length - 1)
      k -= 1
    }
    suffix()
  }
}
''')

w("2297_jump_game_viii", r'''
// LeetCode 2297 - Jump Game VIII
// https://leetcode.com/problems/jump-game-viii/

object Solution {
  def minCost(nums: Array[Int], costs: Array[Int]): Long = {
    val n = nums.length
    val dp = Array.fill(n)(Long.MaxValue / 4)
    dp(0) = 0L
    val stack1 = scala.collection.mutable.ArrayBuffer.empty[Int]
    val stack2 = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < n) {
      while (stack1.nonEmpty && nums(stack1.last) <= nums(i)) {
        val j = stack1.last
        stack1.remove(stack1.length - 1)
        dp(i) = math.min(dp(i), dp(j) + costs(i))
      }
      while (stack2.nonEmpty && nums(stack2.last) > nums(i)) {
        val j = stack2.last
        stack2.remove(stack2.length - 1)
        dp(i) = math.min(dp(i), dp(j) + costs(i))
      }
      if (stack1.nonEmpty) dp(i) = math.min(dp(i), dp(stack1.last) + costs(i))
      if (stack2.nonEmpty) dp(i) = math.min(dp(i), dp(stack2.last) + costs(i))
      stack1 += i
      stack2 += i
      i += 1
    }
    dp(n - 1)
  }
}
''')

w("2299_strong_password_checker_ii", r'''
// LeetCode 2299 - Strong Password Checker II
// https://leetcode.com/problems/strong-password-checker-ii/

object Solution {
  def strongPasswordCheckerII(password: String): Boolean = {
    if (password.length < 8) return false
    val special = "!@#$%^&*()-+"
    var hasLower = false
    var hasUpper = false
    var hasDigit = false
    var hasSpecial = false
    var i = 0
    while (i < password.length) {
      val c = password.charAt(i)
      if (i > 0 && c == password.charAt(i - 1)) return false
      if (c >= 'a' && c <= 'z') hasLower = true
      else if (c >= 'A' && c <= 'Z') hasUpper = true
      else if (c >= '0' && c <= '9') hasDigit = true
      else if (special.indexOf(c) >= 0) hasSpecial = true
      i += 1
    }
    hasLower && hasUpper && hasDigit && hasSpecial
  }
}
''')

w("2300_successful_pairs_of_spells_and_potions", r'''
// LeetCode 2300 - Successful Pairs of Spells and Potions
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

object Solution {
  def successfulPairs(spells: Array[Int], potions: Array[Int], success: Long): Array[Int] = {
    java.util.Arrays.sort(potions)
    val m = potions.length
    val ans = new Array[Int](spells.length)
    var i = 0
    while (i < spells.length) {
      var lo = 0
      var hi = m
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (spells(i).toLong * potions(mid) >= success) hi = mid
        else lo = mid + 1
      }
      ans(i) = m - lo
      i += 1
    }
    ans
  }
}
''')

w("2301_match_substring_after_replacement", r'''
// LeetCode 2301 - Match Substring After Replacement
// https://leetcode.com/problems/match-substring-after-replacement/

object Solution {
  def matchReplacement(s: String, sub: String, mappings: Array[Array[Char]]): Boolean = {
    val allow = scala.collection.mutable.HashSet.empty[Int]
    for (m <- mappings) allow += ((m(0).toInt << 8) | m(1).toInt)
    val n = s.length
    val mlen = sub.length
    var i = 0
    while (i + mlen <= n) {
      var ok = true
      var j = 0
      while (j < mlen && ok) {
        val a = s.charAt(i + j)
        val b = sub.charAt(j)
        if (a != b && !allow.contains((b.toInt << 8) | a.toInt)) ok = false
        j += 1
      }
      if (ok) return true
      i += 1
    }
    false
  }
}
''')

w("2302_count_subarrays_with_score_less_than_k", r'''
// LeetCode 2302 - Count Subarrays With Score Less Than K
// https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

object Solution {
  def countSubarrays(nums: Array[Int], k: Long): Long = {
    var ans = 0L
    var sum = 0L
    var left = 0
    var right = 0
    while (right < nums.length) {
      sum += nums(right)
      while (sum * (right - left + 1) >= k) {
        sum -= nums(left)
        left += 1
      }
      ans += right - left + 1
      right += 1
    }
    ans
  }
}
''')

w("2303_calculate_amount_paid_in_taxes", r'''
// LeetCode 2303 - Calculate Amount Paid in Taxes
// https://leetcode.com/problems/calculate-amount-paid-in-taxes/

object Solution {
  def calculateTax(brackets: Array[Array[Int]], income: Int): Double = {
    var ans = 0.0
    var prev = 0
    for (b <- brackets) {
      val upper = b(0)
      val percent = b(1)
      if (income <= prev) return ans
      val taxable = if (income < upper) income - prev else upper - prev
      ans += taxable * percent / 100.0
      prev = upper
    }
    ans
  }
}
''')

print("batch d done")
