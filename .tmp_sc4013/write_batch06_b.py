#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)


w("2223_sum_of_scores_of_built_strings", r'''
// LeetCode 2223 - Sum of Scores of Built Strings
// https://leetcode.com/problems/sum-of-scores-of-built-strings/

object Solution {
  def sumScores(s: String): Long = {
    val n = s.length
    val z = new Array[Int](n)
    var l = 0
    var r = 0
    var i = 1
    while (i < n) {
      if (i <= r) z(i) = math.min(r - i + 1, z(i - l))
      while (i + z(i) < n && s.charAt(z(i)) == s.charAt(i + z(i))) z(i) += 1
      if (i + z(i) - 1 > r) {
        l = i
        r = i + z(i) - 1
      }
      i += 1
    }
    var ans = n.toLong
    i = 1
    while (i < n) {
      ans += z(i)
      i += 1
    }
    ans
  }
}
''')

w("2224_minimum_number_of_operations_to_convert_time", r'''
// LeetCode 2224 - Minimum Number of Operations to Convert Time
// https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

object Solution {
  def convertTime(current: String, correct: String): Int = {
    def toMin(t: String): Int =
      (t.charAt(0) - '0') * 600 + (t.charAt(1) - '0') * 60 +
        (t.charAt(3) - '0') * 10 + (t.charAt(4) - '0')
    var diff = toMin(correct) - toMin(current)
    var ans = 0
    for (step <- Array(60, 15, 5, 1)) {
      ans += diff / step
      diff %= step
    }
    ans
  }
}
''')

w("2225_find_players_with_zero_or_one_losses", r'''
// LeetCode 2225 - Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

object Solution {
  def findWinners(matches: Array[Array[Int]]): List[List[Int]] = {
    val lose = scala.collection.mutable.HashMap.empty[Int, Int]
    val seen = scala.collection.mutable.HashSet.empty[Int]
    for (m <- matches) {
      seen += m(0)
      seen += m(1)
      lose(m(1)) = lose.getOrElse(m(1), 0) + 1
    }
    val zero = scala.collection.mutable.ListBuffer.empty[Int]
    val one = scala.collection.mutable.ListBuffer.empty[Int]
    for (p <- seen) {
      val L = lose.getOrElse(p, 0)
      if (L == 0) zero += p
      else if (L == 1) one += p
    }
    List(zero.sorted.toList, one.sorted.toList)
  }
}
''')

w("2226_maximum_candies_allocated_to_k_children", r'''
// LeetCode 2226 - Maximum Candies Allocated to K Children
// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

object Solution {
  def maximumCandies(candies: Array[Int], k: Long): Int = {
    def can(mid: Int): Boolean = {
      if (mid == 0) return true
      var cnt = 0L
      for (c <- candies) {
        cnt += c / mid
        if (cnt >= k) return true
      }
      false
    }
    var mx = 0
    for (c <- candies) mx = math.max(mx, c)
    var lo = 0
    var hi = mx
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (can(mid)) lo = mid else hi = mid - 1
    }
    lo
  }
}
''')

w("2227_encrypt_and_decrypt_strings", r'''
// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

class Encrypter(_keys: Array[Char], _values: Array[String], _dictionary: Array[String]) {
  private val enc = scala.collection.mutable.HashMap.empty[Char, String]
  private val cnt = scala.collection.mutable.HashMap.empty[String, Int]
  {
    var i = 0
    while (i < _keys.length) {
      enc(_keys(i)) = _values(i)
      i += 1
    }
    for (w <- _dictionary) {
      val e = encrypt(w)
      cnt(e) = cnt.getOrElse(e, 0) + 1
    }
  }

  def encrypt(word1: String): String = {
    val b = new StringBuilder
    var i = 0
    while (i < word1.length) {
      val c = word1.charAt(i)
      if (!enc.contains(c)) return ""
      b.append(enc(c))
      i += 1
    }
    b.toString
  }

  def decrypt(word2: String): Int = cnt.getOrElse(word2, 0)
}
''')

w("2229_check_if_an_array_is_consecutive", r'''
// LeetCode 2229 - Check if an Array Is Consecutive
// https://leetcode.com/problems/check-if-an-array-is-consecutive/

object Solution {
  def isConsecutive(nums: Array[Int]): Boolean = {
    var mn = nums(0)
    var mx = nums(0)
    val seen = scala.collection.mutable.HashSet.empty[Int]
    for (x <- nums) {
      if (!seen.add(x)) return false
      mn = math.min(mn, x)
      mx = math.max(mx, x)
    }
    mx - mn + 1 == nums.length
  }
}
''')

w("2230_the_users_that_are_eligible_for_discount", r'''
// LeetCode 2230 - The Users That Are Eligible for Discount
// https://leetcode.com/problems/the-users-that-are-eligible-for-discount/

object Solution {
  final val QUERY: String = """CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
  SELECT DISTINCT user_id
  FROM Purchases
  WHERE time_stamp BETWEEN startDate AND endDate
    AND amount >= minAmount
  ORDER BY user_id;
END
"""
}
''')

w("2231_largest_number_after_digit_swaps_by_parity", r'''
// LeetCode 2231 - Largest Number After Digit Swaps by Parity
// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

object Solution {
  def largestInteger(num: Int): Int = {
    val digits = scala.collection.mutable.ArrayBuffer.empty[Int]
    var x = num
    while (x > 0) {
      digits.prepend(x % 10)
      x /= 10
    }
    val even = scala.collection.mutable.ArrayBuffer.empty[Int]
    val odd = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (d <- digits) {
      if (d % 2 == 0) even += d else odd += d
    }
    val ev = even.sorted(Ordering[Int].reverse)
    val od = odd.sorted(Ordering[Int].reverse)
    var ei = 0
    var oi = 0
    var ans = 0
    for (d <- digits) {
      if (d % 2 == 0) {
        ans = ans * 10 + ev(ei)
        ei += 1
      } else {
        ans = ans * 10 + od(oi)
        oi += 1
      }
    }
    ans
  }
}
''')

w("2232_minimize_result_by_adding_parentheses_to_expression", r'''
// LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
// https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

object Solution {
  def minimizeResult(expression: String): String = {
    val plus = expression.indexOf('+')
    val left = expression.substring(0, plus)
    val right = expression.substring(plus + 1)
    var bestVal = Int.MaxValue
    var best = ""
    var i = 0
    while (i < left.length) {
      var j = 1
      while (j <= right.length) {
        val a = left.substring(0, i)
        val b = left.substring(i)
        val c = right.substring(0, j)
        val d = right.substring(j)
        var value = b.toInt + c.toInt
        if (a.length > 0) value *= a.toInt
        if (d.length > 0) value *= d.toInt
        val cand = a + "(" + b + "+" + c + ")" + d
        if (value < bestVal) {
          bestVal = value
          best = cand
        }
        j += 1
      }
      i += 1
    }
    best
  }
}
''')

w("2233_maximum_product_after_k_increments", r'''
// LeetCode 2233 - Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/

object Solution {
  def maximumProduct(nums: Array[Int], k: Int): Int = {
    val MOD = 1000000007
    val h = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
    for (x <- nums) h.enqueue(x)
    var i = 0
    while (i < k) {
      val x = h.dequeue()
      h.enqueue(x + 1)
      i += 1
    }
    var ans = 1L
    while (h.nonEmpty) ans = ans * h.dequeue() % MOD
    ans.toInt
  }
}
''')

w("2234_maximum_total_beauty_of_the_gardens", r'''
// LeetCode 2234 - Maximum Total Beauty of the Gardens
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

object Solution {
  def maximumBeauty(flowers: Array[Int], newFlowers: Long, target: Int, full: Int, partial: Int): Long = {
    val n = flowers.length
    var i = 0
    while (i < n) {
      if (flowers(i) > target) flowers(i) = target
      i += 1
    }
    java.util.Arrays.sort(flowers)
    var sum = 0L
    for (f <- flowers) sum += f
    if (target.toLong * n - sum <= newFlowers) return n.toLong * full
    val pref = new Array[Long](n + 1)
    i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + flowers(i)
      i += 1
    }
    var ans = 0L
    var j = n - 1
    var remain = newFlowers
    var complete = 0
    while (complete <= n) {
      if (complete > 0) {
        val need = target.toLong - flowers(n - complete)
        if (remain < need) return ans
        remain -= need
      }
      while (j >= n - complete || (j >= 0 && flowers(j).toLong * (j + 1) - pref(j + 1) > remain)) j -= 1
      var partialVal = 0L
      if (j >= 0) {
        val extra = (remain - (flowers(j).toLong * (j + 1) - pref(j + 1))) / (j + 1)
        partialVal = flowers(j) + extra
        if (partialVal >= target) partialVal = target - 1
      }
      ans = math.max(ans, complete.toLong * full + partialVal * partial)
      complete += 1
    }
    ans
  }
}
''')

w("2235_add_two_integers", r'''
// LeetCode 2235 - Add Two Integers
// https://leetcode.com/problems/add-two-integers/

object Solution {
  def sum(num1: Int, num2: Int): Int = num1 + num2
}
''')

w("2236_root_equals_sum_of_children", r'''
// LeetCode 2236 - Root Equals Sum of Children
// https://leetcode.com/problems/root-equals-sum-of-children/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def checkTree(root: TreeNode): Boolean =
    root.value == root.left.value + root.right.value
}
''')

w("2237_count_positions_on_street_with_required_brightness", r'''
// LeetCode 2237 - Count Positions on Street With Required Brightness
// https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

object Solution {
  def meetRequirement(n: Int, lights: Array[Array[Int]], requirement: Array[Int]): Int = {
    val diff = new Array[Int](n + 1)
    for (light <- lights) {
      val pos = light(0)
      val r = light(1)
      val l = math.max(0, pos - r)
      val rr = math.min(n - 1, pos + r)
      diff(l) += 1
      diff(rr + 1) -= 1
    }
    var ans = 0
    var cur = 0
    var i = 0
    while (i < n) {
      cur += diff(i)
      if (cur >= requirement(i)) ans += 1
      i += 1
    }
    ans
  }
}
''')

w("2239_find_closest_number_to_zero", r'''
// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

object Solution {
  def findClosestNumber(nums: Array[Int]): Int = {
    var ans = nums(0)
    for (x <- nums) {
      if (math.abs(x) < math.abs(ans) || (math.abs(x) == math.abs(ans) && x > ans)) ans = x
    }
    ans
  }
}
''')

w("2240_number_of_ways_to_buy_pens_and_pencils", r'''
// LeetCode 2240 - Number of Ways to Buy Pens and Pencils
// https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

object Solution {
  def waysToBuyPensPencils(total: Int, cost1: Int, cost2: Int): Long = {
    var ans = 0L
    var pens = 0
    while (pens.toLong * cost1 <= total) {
      val remain = total - pens * cost1
      ans += remain / cost2 + 1
      pens += 1
    }
    ans
  }
}
''')

w("2241_design_an_atm_machine", r'''
// LeetCode 2241 - Design an ATM Machine
// https://leetcode.com/problems/design-an-atm-machine/

class ATM() {
  private val cnt = Array.fill(5)(0L)
  private val vals = Array(20, 50, 100, 200, 500)

  def deposit(banknotesCount: Array[Int]): Unit = {
    var i = 0
    while (i < 5) {
      cnt(i) += banknotesCount(i)
      i += 1
    }
  }

  def withdraw(amount: Int): Array[Int] = {
    val take = new Array[Int](5)
    var remain = amount.toLong
    val tmp = cnt.clone()
    var i = 4
    while (i >= 0) {
      var need = remain / vals(i)
      if (need > tmp(i)) need = tmp(i)
      take(i) = need.toInt
      remain -= need * vals(i)
      i -= 1
    }
    if (remain != 0) return Array(-1)
    i = 0
    while (i < 5) {
      cnt(i) -= take(i)
      i += 1
    }
    take
  }
}
''')

w("2242_maximum_score_of_a_node_sequence", r'''
// LeetCode 2242 - Maximum Score of a Node Sequence
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/

object Solution {
  def maximumScore(scores: Array[Int], edges: Array[Array[Int]]): Int = {
    val n = scores.length
    val top = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    var i = 0
    while (i < n) {
      for (v <- g(i)) {
        top(i) += v
        var j = top(i).length - 1
        while (j > 0) {
          if (scores(top(i)(j)) > scores(top(i)(j - 1))) {
            val tmp = top(i)(j)
            top(i)(j) = top(i)(j - 1)
            top(i)(j - 1) = tmp
          }
          j -= 1
        }
        if (top(i).length > 3) top(i).remove(3, top(i).length - 3)
      }
      i += 1
    }
    var ans = -1
    for (e <- edges) {
      val a = e(0)
      val b = e(1)
      for (c <- top(a) if c != b) {
        for (d <- top(b) if d != a && d != c) {
          ans = math.max(ans, scores(a) + scores(b) + scores(c) + scores(d))
        }
      }
    }
    ans
  }
}
''')

w("2243_calculate_digit_sum_of_a_string", r'''
// LeetCode 2243 - Calculate Digit Sum of a String
// https://leetcode.com/problems/calculate-digit-sum-of-a-string/

object Solution {
  def digitSum(s0: String, k: Int): String = {
    var s = s0
    while (s.length > k) {
      val next = new StringBuilder
      var i = 0
      while (i < s.length) {
        var sum = 0
        val end = math.min(i + k, s.length)
        var j = i
        while (j < end) {
          sum += s.charAt(j) - '0'
          j += 1
        }
        next.append(sum)
        i += k
      }
      s = next.toString
    }
    s
  }
}
''')

w("2244_minimum_rounds_to_complete_all_tasks", r'''
// LeetCode 2244 - Minimum Rounds to Complete All Tasks
// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

object Solution {
  def minimumRounds(tasks: Array[Int]): Int = {
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (t <- tasks) freq(t) = freq.getOrElse(t, 0) + 1
    var ans = 0
    for (c <- freq.values) {
      if (c == 1) return -1
      ans += (c + 2) / 3
    }
    ans
  }
}
''')

w("2245_maximum_trailing_zeros_in_a_cornered_path", r'''
// LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
// https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

object Solution {
  def maxTrailingZeros(grid: Array[Array[Int]]): Int = {
    def fact(x0: Int): Array[Int] = {
      var x = x0
      var t = 0
      var f = 0
      while (x % 2 == 0) { t += 1; x /= 2 }
      while (x % 5 == 0) { f += 1; x /= 5 }
      Array(t, f)
    }
    val m = grid.length
    val n = grid(0).length
    val left2 = Array.ofDim[Int](m, n)
    val left5 = Array.ofDim[Int](m, n)
    val up2 = Array.ofDim[Int](m, n)
    val up5 = Array.ofDim[Int](m, n)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val p = fact(grid(i)(j))
        left2(i)(j) = p(0)
        up2(i)(j) = p(0)
        left5(i)(j) = p(1)
        up5(i)(j) = p(1)
        if (j > 0) {
          left2(i)(j) += left2(i)(j - 1)
          left5(i)(j) += left5(i)(j - 1)
        }
        if (i > 0) {
          up2(i)(j) += up2(i - 1)(j)
          up5(i)(j) += up5(i - 1)(j)
        }
        j += 1
      }
      i += 1
    }
    var ans = 0
    i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val cell = fact(grid(i)(j))
        val L2 = left2(i)(j)
        val L5 = left5(i)(j)
        val R2 = left2(i)(n - 1) - left2(i)(j) + cell(0)
        val R5 = left5(i)(n - 1) - left5(i)(j) + cell(1)
        val U2 = up2(i)(j)
        val U5 = up5(i)(j)
        val D2 = up2(m - 1)(j) - up2(i)(j) + cell(0)
        val D5 = up5(m - 1)(j) - up5(i)(j) + cell(1)
        val cands = Array(
          Array(L2 + U2 - cell(0), L5 + U5 - cell(1)),
          Array(L2 + D2 - cell(0), L5 + D5 - cell(1)),
          Array(R2 + U2 - cell(0), R5 + U5 - cell(1)),
          Array(R2 + D2 - cell(0), R5 + D5 - cell(1))
        )
        for (c <- cands) ans = math.max(ans, math.min(c(0), c(1)))
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("2246_longest_path_with_different_adjacent_characters", r'''
// LeetCode 2246 - Longest Path With Different Adjacent Characters
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

object Solution {
  def longestPath(parent: Array[Int], s: String): Int = {
    val n = parent.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 1
    while (i < n) {
      g(parent(i)) += i
      i += 1
    }
    var ans = 1
    def dfs(u: Int): Int = {
      var best1 = 0
      var best2 = 0
      for (v <- g(u)) {
        val lenV = dfs(v)
        if (s.charAt(v) != s.charAt(u)) {
          if (lenV > best1) {
            best2 = best1
            best1 = lenV
          } else if (lenV > best2) best2 = lenV
        }
      }
      ans = math.max(ans, 1 + best1 + best2)
      1 + best1
    }
    dfs(0)
    ans
  }
}
''')

w("2247_maximum_cost_of_trip_with_k_highways", r'''
// LeetCode 2247 - Maximum Cost of Trip With K Highways
// https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

object Solution {
  def maximumCost(n: Int, highways: Array[Array[Int]], k: Int): Int = {
    if (k + 1 > n) return -1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    for (h <- highways) {
      g(h(0)) += ((h(1), h(2)))
      g(h(1)) += ((h(0), h(2)))
    }
    val dp = Array.fill(1 << n, n)(-1)
    var i = 0
    while (i < n) {
      dp(1 << i)(i) = 0
      i += 1
    }
    var ans = -1
    var mask = 0
    while (mask < (1 << n)) {
      val cities = Integer.bitCount(mask)
      var u = 0
      while (u < n) {
        if (dp(mask)(u) >= 0) {
          if (cities - 1 == k) ans = math.max(ans, dp(mask)(u))
          for ((v, w) <- g(u) if (mask & (1 << v)) == 0) {
            val nm = mask | (1 << v)
            dp(nm)(v) = math.max(dp(nm)(v), dp(mask)(u) + w)
          }
        }
        u += 1
      }
      mask += 1
    }
    ans
  }
}
''')

w("2248_intersection_of_multiple_arrays", r'''
// LeetCode 2248 - Intersection of Multiple Arrays
// https://leetcode.com/problems/intersection-of-multiple-arrays/

object Solution {
  def intersection(nums: Array[Array[Int]]): List[Int] = {
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (arr <- nums) {
      val seen = scala.collection.mutable.HashSet.empty[Int]
      for (x <- arr if seen.add(x)) freq(x) = freq.getOrElse(x, 0) + 1
    }
    val ans = scala.collection.mutable.ListBuffer.empty[Int]
    for ((k, v) <- freq if v == nums.length) ans += k
    ans.sorted.toList
  }
}
''')

w("2249_count_lattice_points_inside_a_circle", r'''
// LeetCode 2249 - Count Lattice Points Inside a Circle
// https://leetcode.com/problems/count-lattice-points-inside-a-circle/

object Solution {
  def countLatticePoints(circles: Array[Array[Int]]): Int = {
    val seen = scala.collection.mutable.HashSet.empty[Long]
    for (c <- circles) {
      val x = c(0)
      val y = c(1)
      val r = c(2)
      var i = x - r
      while (i <= x + r) {
        var j = y - r
        while (j <= y + r) {
          if ((i - x) * (i - x) + (j - y) * (j - y) <= r * r)
            seen += ((i.toLong << 32) | (j.toLong & 0xffffffffL))
          j += 1
        }
        i += 1
      }
    }
    seen.size
  }
}
''')

w("2250_count_number_of_rectangles_containing_each_point", r'''
// LeetCode 2250 - Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

object Solution {
  def countRectangles(rectangles: Array[Array[Int]], points: Array[Array[Int]]): Array[Int] = {
    val byH = Array.fill(101)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (r <- rectangles) byH(r(1)) += r(0)
    var h = 1
    while (h <= 100) {
      val sorted = byH(h).sorted
      byH(h).clear()
      byH(h) ++= sorted
      h += 1
    }
    val ans = new Array[Int](points.length)
    var i = 0
    while (i < points.length) {
      val x = points(i)(0)
      val y = points(i)(1)
      var cnt = 0
      h = y
      while (h <= 100) {
        val xs = byH(h)
        var lo = 0
        var hi = xs.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (xs(mid) < x) lo = mid + 1 else hi = mid
        }
        cnt += xs.length - lo
        h += 1
      }
      ans(i) = cnt
      i += 1
    }
    ans
  }
}
''')

w("2251_number_of_flowers_in_full_bloom", r'''
// LeetCode 2251 - Number of Flowers in Full Bloom
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/

object Solution {
  def fullBloomFlowers(flowers: Array[Array[Int]], people: Array[Int]): Array[Int] = {
    val start = scala.collection.mutable.ArrayBuffer.empty[Int]
    val end = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (f <- flowers) {
      start += f(0)
      end += f(1)
    }
    val st = start.sorted
    val en = end.sorted
    def upperBound(a: scala.collection.mutable.IndexedSeq[Int], t: Int): Int = {
      var lo = 0
      var hi = a.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (a(mid) <= t) lo = mid + 1 else hi = mid
      }
      lo
    }
    def lowerBound(a: scala.collection.mutable.IndexedSeq[Int], t: Int): Int = {
      var lo = 0
      var hi = a.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (a(mid) < t) lo = mid + 1 else hi = mid
      }
      lo
    }
    val ans = new Array[Int](people.length)
    var i = 0
    while (i < people.length) {
      val t = people(i)
      ans(i) = upperBound(st, t) - lowerBound(en, t)
      i += 1
    }
    ans
  }
}
''')

print("batch b done")
