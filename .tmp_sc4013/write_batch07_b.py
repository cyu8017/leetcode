#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("2333_minimum_sum_of_squared_difference", r'''
// LeetCode 2333 - Minimum Sum of Squared Difference
// https://leetcode.com/problems/minimum-sum-of-squared-difference/

object Solution {
  def minSumSquareDiff(nums1: Array[Int], nums2: Array[Int], k1: Int, k2: Int): Long = {
    val n = nums1.length
    val diff = Array.fill(n)(0)
    var maxD = 0
    var i = 0
    while (i < n) {
      val d = math.abs(nums1(i) - nums2(i))
      diff(i) = d
      if (d > maxD) maxD = d
      i += 1
    }
    var k = k1 + k2
    val freq = Array.fill(maxD + 1)(0)
    diff.foreach(d => freq(d) += 1)
    var d = maxD
    while (d > 0 && k > 0) {
      if (freq(d) != 0) {
        var take = freq(d)
        if (take > k) take = k
        freq(d) -= take
        freq(d - 1) += take
        k -= take
      }
      d -= 1
    }
    var ans = 0L
    d = 0
    while (d <= maxD) {
      ans += d.toLong * d * freq(d)
      d += 1
    }
    ans
  }
}
''')

w("2334_subarray_with_elements_greater_than_varying_threshold", r'''
// LeetCode 2334 - Subarray With Elements Greater Than Varying Threshold
// https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

object Solution {
  def validSubarraySize(nums: Array[Int], threshold: Int): Int = {
    val n = nums.length
    val left = Array.fill(n)(0)
    val right = Array.fill(n)(0)
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < n) {
      while (stack.nonEmpty && nums(stack.last) >= nums(i)) stack.remove(stack.length - 1)
      left(i) = if (stack.isEmpty) -1 else stack.last
      stack += i
      i += 1
    }
    stack.clear()
    i = n - 1
    while (i >= 0) {
      while (stack.nonEmpty && nums(stack.last) >= nums(i)) stack.remove(stack.length - 1)
      right(i) = if (stack.isEmpty) n else stack.last
      stack += i
      i -= 1
    }
    i = 0
    while (i < n) {
      val k = right(i) - left(i) - 1
      if (nums(i) > threshold / k) return k
      i += 1
    }
    -1
  }
}
''')

w("2335_minimum_amount_of_time_to_fill_cups", r'''
// LeetCode 2335 - Minimum Amount of Time to Fill Cups
// https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

object Solution {
  def fillCups(amount: Array[Int]): Int = {
    var a = amount(0)
    var b = amount(1)
    var c = amount(2)
    if (a < b) { val t = a; a = b; b = t }
    if (a < c) { val t = a; a = c; c = t }
    if (b < c) { val t = b; b = c; c = t }
    if (a >= b + c) a else (a + b + c + 1) / 2
  }
}
''')

w("2336_smallest_number_in_infinite_set", r'''
// LeetCode 2336 - Smallest Number in Infinite Set
// https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet() {
  private var next = 1
  private val added = scala.collection.mutable.HashSet.empty[Int]
  private val heap = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)

  def popSmallest(): Int = {
    if (heap.nonEmpty) {
      val x = heap.dequeue()
      added.remove(x)
      return x
    }
    val x = next
    next += 1
    x
  }

  def addBack(num: Int): Unit = {
    if (num < next && added.add(num)) heap.enqueue(num)
  }
}
''')

w("2337_move_pieces_to_obtain_a_string", r'''
// LeetCode 2337 - Move Pieces to Obtain a String
// https://leetcode.com/problems/move-pieces-to-obtain-a-string/

object Solution {
  def canChange(start: String, target: String): Boolean = {
    val n = start.length
    var i = 0
    var j = 0
    while (i < n || j < n) {
      while (i < n && start.charAt(i) == '_') i += 1
      while (j < n && target.charAt(j) == '_') j += 1
      if (i == n || j == n) return i == n && j == n
      if (start.charAt(i) != target.charAt(j)) return false
      if (start.charAt(i) == 'L' && i < j) return false
      if (start.charAt(i) == 'R' && i > j) return false
      i += 1
      j += 1
    }
    true
  }
}
''')

w("2338_count_the_number_of_ideal_arrays", r'''
// LeetCode 2338 - Count the Number of Ideal Arrays
// https://leetcode.com/problems/count-the-number-of-ideal-arrays/

object Solution {
  def idealArrays(n: Int, maxValue: Int): Int = {
    val mod = 1000000007
    val maxLen = 14
    val comb = Array.ofDim[Int](n + 1, maxLen + 1)
    var i = 0
    while (i <= n) {
      comb(i)(0) = 1
      var j = 1
      while (j <= maxLen && j <= i) {
        comb(i)(j) = (comb(i - 1)(j) + comb(i - 1)(j - 1)) % mod
        j += 1
      }
      i += 1
    }
    val dp = Array.ofDim[Int](maxValue + 1, maxLen + 1)
    i = 1
    while (i <= maxValue) {
      dp(i)(1) = 1
      i += 1
    }
    var len = 2
    while (len <= maxLen) {
      var v = 1
      while (v <= maxValue) {
        var m = 2 * v
        while (m <= maxValue) {
          dp(m)(len) = (dp(m)(len) + dp(v)(len - 1)) % mod
          m += v
        }
        v += 1
      }
      len += 1
    }
    var ans = 0
    var v = 1
    while (v <= maxValue) {
      len = 1
      while (len <= maxLen && len <= n) {
        ans = (ans + (dp(v)(len).toLong * comb(n - 1)(len - 1) % mod).toInt) % mod
        len += 1
      }
      v += 1
    }
    ans
  }
}
''')

w("2340_minimum_adjacent_swaps_to_make_a_valid_array", r'''
// LeetCode 2340 - Minimum Adjacent Swaps to Make a Valid Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/

object Solution {
  def minimumSwaps(nums: Array[Int]): Int = {
    val n = nums.length
    var minI = 0
    var maxI = 0
    var i = 1
    while (i < n) {
      if (nums(i) < nums(minI)) minI = i
      if (nums(i) >= nums(maxI)) maxI = i
      i += 1
    }
    var ans = minI + (n - 1 - maxI)
    if (minI > maxI) ans -= 1
    ans
  }
}
''')

w("2341_maximum_number_of_pairs_in_array", r'''
// LeetCode 2341 - Maximum Number of Pairs in Array
// https://leetcode.com/problems/maximum-number-of-pairs-in-array/

object Solution {
  def numberOfPairs(nums: Array[Int]): Array[Int] = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    nums.foreach(x => cnt(x) = cnt.getOrElse(x, 0) + 1)
    var pairs = 0
    var left = 0
    cnt.values.foreach { c =>
      pairs += c / 2
      left += c % 2
    }
    Array(pairs, left)
  }
}
''')

w("2342_max_sum_of_a_pair_with_equal_sum_of_digits", r'''
// LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

object Solution {
  def maximumSum(nums: Array[Int]): Int = {
    val best = scala.collection.mutable.Map.empty[Int, Int]
    var ans = -1
    nums.foreach { x =>
      val ds = digitSum(x)
      if (best.contains(ds)) {
        ans = math.max(ans, best(ds) + x)
        if (x > best(ds)) best(ds) = x
      } else {
        best(ds) = x
      }
    }
    ans
  }

  private def digitSum(x0: Int): Int = {
    var x = x0
    var s = 0
    while (x > 0) {
      s += x % 10
      x /= 10
    }
    s
  }
}
''')

w("2343_query_kth_smallest_trimmed_number", r'''
// LeetCode 2343 - Query Kth Smallest Trimmed Number
// https://leetcode.com/problems/query-kth-smallest-trimmed-number/

object Solution {
  def smallestTrimmedNumbers(nums: Array[String], queries: Array[Array[Int]]): Array[Int] = {
    val n = nums.length
    val m = queries.length
    val ans = Array.fill(m)(0)
    var qi = 0
    while (qi < m) {
      val k = queries(qi)(0)
      val trim = queries(qi)(1)
      val arr = Array.tabulate(n) { i =>
        val s = nums(i)
        (s.substring(s.length - trim), i)
      }
      scala.util.Sorting.stableSort(arr, (a: (String, Int), b: (String, Int)) => {
        val c = a._1.compareTo(b._1)
        if (c != 0) c < 0 else a._2 < b._2
      })
      ans(qi) = arr(k - 1)._2
      qi += 1
    }
    ans
  }
}
''')

w("2344_minimum_deletions_to_make_array_divisible", r'''
// LeetCode 2344 - Minimum Deletions to Make Array Divisible
// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

object Solution {
  def minOperations(nums: Array[Int], numsDivide: Array[Int]): Int = {
    var g = numsDivide(0)
    var i = 1
    while (i < numsDivide.length) {
      g = gcd(g, numsDivide(i))
      i += 1
    }
    java.util.Arrays.sort(nums)
    i = 0
    while (i < nums.length) {
      if (g % nums(i) == 0) return i
      i += 1
    }
    -1
  }

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
}
''')

w("2345_finding_the_number_of_visible_mountains", r'''
// LeetCode 2345 - Finding the Number of Visible Mountains
// https://leetcode.com/problems/finding-the-number-of-visible-mountains/

object Solution {
  def visibleMountains(peaks: Array[Array[Int]]): Int = {
    val arr = peaks.map(p => Array(p(0) - p(1), p(0) + p(1)))
    scala.util.Sorting.stableSort(arr, (a: Array[Int], b: Array[Int]) => {
      if (a(0) == b(0)) a(1) > b(1) else a(0) < b(0)
    })
    var ans = 0
    var maxR = Int.MinValue
    var i = 0
    while (i < arr.length) {
      var j = i
      while (j < arr.length && arr(j)(0) == arr(i)(0) && arr(j)(1) == arr(i)(1)) j += 1
      if (arr(i)(1) > maxR) {
        if (j - i == 1) ans += 1
        maxR = arr(i)(1)
      }
      i = j
    }
    ans
  }
}
''')

w("2347_best_poker_hand", r'''
// LeetCode 2347 - Best Poker Hand
// https://leetcode.com/problems/best-poker-hand/

object Solution {
  def bestHand(ranks: Array[Int], suits: Array[Char]): String = {
    if (suits(0) == suits(1) && suits(1) == suits(2) && suits(2) == suits(3) && suits(3) == suits(4)) {
      return "Flush"
    }
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var best = 0
    ranks.foreach { r =>
      val c = cnt.getOrElse(r, 0) + 1
      cnt(r) = c
      best = math.max(best, c)
    }
    if (best >= 3) "Three of a Kind"
    else if (best == 2) "Pair"
    else "High Card"
  }
}
''')

w("2348_number_of_zero_filled_subarrays", r'''
// LeetCode 2348 - Number of Zero-Filled Subarrays
// https://leetcode.com/problems/number-of-zero-filled-subarrays/

object Solution {
  def zeroFilledSubarray(nums: Array[Int]): Long = {
    var ans = 0L
    var streak = 0L
    nums.foreach { x =>
      if (x == 0) {
        streak += 1
        ans += streak
      } else streak = 0
    }
    ans
  }
}
''')

w("2349_design_a_number_container_system", r'''
// LeetCode 2349 - Design a Number Container System
// https://leetcode.com/problems/design-a-number-container-system/

class NumberContainers() {
  private val idx = scala.collection.mutable.Map.empty[Int, Int]
  private val heap = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.TreeSet[Int]]

  def change(index: Int, number: Int): Unit = {
    idx(index) = number
    heap.getOrElseUpdate(number, scala.collection.mutable.TreeSet.empty[Int]) += index
  }

  def find(number: Int): Int = {
    val h = heap.getOrElse(number, return -1)
    while (h.nonEmpty) {
      val i = h.head
      if (idx.get(i).contains(number)) return i
      h -= i
    }
    -1
  }
}
''')

w("2350_shortest_impossible_sequence_of_rolls", r'''
// LeetCode 2350 - Shortest Impossible Sequence of Rolls
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

object Solution {
  def shortestSequence(rolls: Array[Int], k: Int): Int = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var ans = 1
    rolls.foreach { r =>
      seen += r
      if (seen.size == k) {
        ans += 1
        seen.clear()
      }
    }
    ans
  }
}
''')

w("2351_first_letter_to_appear_twice", r'''
// LeetCode 2351 - First Letter to Appear Twice
// https://leetcode.com/problems/first-letter-to-appear-twice/

object Solution {
  def repeatedCharacter(s: String): Char = {
    val seen = Array.fill(26)(false)
    s.foreach { c =>
      val i = c - 'a'
      if (seen(i)) return c
      seen(i) = true
    }
    0.toChar
  }
}
''')

w("2352_equal_row_and_column_pairs", r'''
// LeetCode 2352 - Equal Row and Column Pairs
// https://leetcode.com/problems/equal-row-and-column-pairs/

object Solution {
  def equalPairs(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val freq = scala.collection.mutable.Map.empty[String, Int]
    var i = 0
    while (i < n) {
      val key = grid(i).mkString(",")
      freq(key) = freq.getOrElse(key, 0) + 1
      i += 1
    }
    var ans = 0
    val col = Array.fill(n)(0)
    var j = 0
    while (j < n) {
      i = 0
      while (i < n) {
        col(i) = grid(i)(j)
        i += 1
      }
      ans += freq.getOrElse(col.mkString(","), 0)
      j += 1
    }
    ans
  }
}
''')

w("2353_design_a_food_rating_system", r'''
// LeetCode 2353 - Design a Food Rating System
// https://leetcode.com/problems/design-a-food-rating-system/

class FoodRatings(_foods: Array[String], _cuisines: Array[String], _ratings: Array[Int]) {
  private val cuisineOf = scala.collection.mutable.Map.empty[String, String]
  private val ratingOf = scala.collection.mutable.Map.empty[String, Int]
  private val heaps = scala.collection.mutable.Map.empty[String, scala.collection.mutable.TreeSet[(Int, String)]]

  {
    var i = 0
    while (i < _foods.length) {
      cuisineOf(_foods(i)) = _cuisines(i)
      ratingOf(_foods(i)) = _ratings(i)
      heaps.getOrElseUpdate(_cuisines(i), scala.collection.mutable.TreeSet.empty[(Int, String)]) += ((-_ratings(i), _foods(i)))
      i += 1
    }
  }

  def changeRating(food: String, newRating: Int): Unit = {
    val cuisine = cuisineOf(food)
    val set = heaps(cuisine)
    set -= ((-ratingOf(food), food))
    ratingOf(food) = newRating
    set += ((-newRating, food))
  }

  def highestRated(cuisine: String): String = heaps(cuisine).head._2
}
''')

w("2354_number_of_excellent_pairs", r'''
// LeetCode 2354 - Number of Excellent Pairs
// https://leetcode.com/problems/number-of-excellent-pairs/

object Solution {
  def countExcellentPairs(nums: Array[Int], k: Int): Long = {
    val uniq = scala.collection.mutable.HashSet.empty[Int]
    nums.foreach(x => uniq += x)
    val cnt = Array.fill(32)(0)
    uniq.foreach { x =>
      cnt(Integer.bitCount(x)) += 1
    }
    var ans = 0L
    var i = 0
    while (i < 32) {
      var j = 0
      while (j < 32) {
        if (i + j >= k) ans += cnt(i).toLong * cnt(j)
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("2355_maximum_number_of_books_you_can_take", r'''
// LeetCode 2355 - Maximum Number of Books You Can Take
// https://leetcode.com/problems/maximum-number-of-books-you-can-take/

object Solution {
  def maximumBooks(books: Array[Int]): Long = {
    val n = books.length
    val dp = Array.fill(n)(0L)
    val stack = scala.collection.mutable.ArrayDeque.empty[Int]
    var ans = 0L
    var i = 0
    while (i < n) {
      while (stack.nonEmpty && books(stack.last) >= books(i) - (i - stack.last)) {
        stack.removeLast()
      }
      if (stack.isEmpty) dp(i) = sum(0, i, books(i))
      else {
        val j = stack.last
        dp(i) = dp(j) + sum(j + 1, i, books(i))
      }
      ans = math.max(ans, dp(i))
      stack.append(i)
      i += 1
    }
    ans
  }

  private def sum(l: Int, r: Int, h: Int): Long = {
    val width = r - l + 1
    if (h >= width) width.toLong * (2L * h - width + 1) / 2
    else h.toLong * (h + 1) / 2
  }
}
''')

w("2357_make_array_zero_by_subtracting_equal_amounts", r'''
// LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

object Solution {
  def minimumOperations(nums: Array[Int]): Int = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    nums.foreach(x => if (x > 0) seen += x)
    seen.size
  }
}
''')

w("2358_maximum_number_of_groups_entering_a_competition", r'''
// LeetCode 2358 - Maximum Number of Groups Entering a Competition
// https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

object Solution {
  def maximumGroups(grades: Array[Int]): Int = {
    val n = grades.length
    var k = 0
    while ((k + 1L) * (k + 2) / 2 <= n) k += 1
    k
  }
}
''')

w("2359_find_closest_node_to_given_two_nodes", r'''
// LeetCode 2359 - Find Closest Node to Given Two Nodes
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

object Solution {
  def closestMeetingNode(edges: Array[Int], node1: Int, node2: Int): Int = {
    val n = edges.length

    def dist(start: Int): Array[Int] = {
      val d = Array.fill(n)(-1)
      var cur = start
      var step = 0
      while (cur != -1 && d(cur) == -1) {
        d(cur) = step
        cur = edges(cur)
        step += 1
      }
      d
    }

    val d1 = dist(node1)
    val d2 = dist(node2)
    var ans = -1
    var best = Int.MaxValue
    var i = 0
    while (i < n) {
      if (d1(i) != -1 && d2(i) != -1) {
        val mx = math.max(d1(i), d2(i))
        if (mx < best) {
          best = mx
          ans = i
        }
      }
      i += 1
    }
    ans
  }
}
''')

w("2360_longest_cycle_in_a_graph", r'''
// LeetCode 2360 - Longest Cycle in a Graph
// https://leetcode.com/problems/longest-cycle-in-a-graph/

object Solution {
  def longestCycle(edges: Array[Int]): Int = {
    val n = edges.length
    val vis = Array.fill(n)(false)
    var ans = -1
    var i = 0
    while (i < n) {
      if (!vis(i)) {
        val dist = scala.collection.mutable.Map.empty[Int, Int]
        var cur = i
        var step = 0
        while (cur != -1 && !vis(cur)) {
          vis(cur) = true
          dist(cur) = step
          cur = edges(cur)
          step += 1
        }
        if (cur != -1 && dist.contains(cur)) {
          ans = math.max(ans, step - dist(cur))
        }
      }
      i += 1
    }
    ans
  }
}
''')
