#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("2441_largest_positive_integer_that_exists_with_its_negative", r'''
// LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

object Solution {
  def findMaxK(nums: Array[Int]): Int = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var ans = -1
    var i = 0
    while (i < nums.length) {
      val x = nums(i)
      seen += x
      if (x > 0 && seen.contains(-x) && x > ans) ans = x
      if (x < 0 && seen.contains(-x) && -x > ans) ans = -x
      i += 1
    }
    ans
  }
}
''')

w("2442_count_number_of_distinct_integers_after_reverse_operations", r'''
// LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

object Solution {
  def countDistinctIntegers(nums: Array[Int]): Int = {
    def rev(x0: Int): Int = {
      var x = x0
      var r = 0
      while (x > 0) {
        r = r * 10 + x % 10
        x /= 10
      }
      r
    }
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var i = 0
    while (i < nums.length) {
      seen += nums(i)
      seen += rev(nums(i))
      i += 1
    }
    seen.size
  }
}
''')

w("2443_sum_of_number_and_its_reverse", r'''
// LeetCode 2443 - Sum of Number and Its Reverse
// https://leetcode.com/problems/sum-of-number-and-its-reverse/

object Solution {
  def sumOfNumberAndReverse(num: Int): Boolean = {
    def rev(x0: Int): Int = {
      var x = x0
      var r = 0
      while (x > 0) {
        r = r * 10 + x % 10
        x /= 10
      }
      r
    }
    var i = 0
    while (i <= num) {
      if (i + rev(i) == num) return true
      i += 1
    }
    false
  }
}
''')

w("2444_count_subarrays_with_fixed_bounds", r'''
// LeetCode 2444 - Count Subarrays With Fixed Bounds
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

object Solution {
  def countSubarrays(nums: Array[Int], minK: Int, maxK: Int): Long = {
    var ans = 0L
    var imin = -1
    var imax = -1
    var ibad = -1
    var i = 0
    while (i < nums.length) {
      val x = nums(i)
      if (x < minK || x > maxK) ibad = i
      if (x == minK) imin = i
      if (x == maxK) imax = i
      val bound = if (imin < imax) imin else imax
      if (bound > ibad) ans += bound - ibad
      i += 1
    }
    ans
  }
}
''')

w("2445_number_of_nodes_with_value_one", r'''
// LeetCode 2445 - Number of Nodes With Value One
// https://leetcode.com/problems/number-of-nodes-with-value-one/

object Solution {
  def numberOfNodes(n: Int, queries: Array[Int]): Int = {
    val flip = new Array[Int](n + 1)
    val value = new Array[Int](n + 1)
    var i = 0
    while (i < queries.length) {
      flip(queries(i)) ^= 1
      i += 1
    }
    var ans = 0
    i = 1
    while (i <= n) {
      value(i) = flip(i)
      if (i > 1) value(i) ^= value(i / 2)
      ans += value(i)
      i += 1
    }
    ans
  }
}
''')

w("2446_determine_if_two_events_have_conflict", r'''
// LeetCode 2446 - Determine if Two Events Have Conflict
// https://leetcode.com/problems/determine-if-two-events-have-conflict/

object Solution {
  def haveConflict(event1: Array[String], event2: Array[String]): Boolean = {
    event1(0) <= event2(1) && event2(0) <= event1(1)
  }
}
''')

w("2447_number_of_subarrays_with_gcd_equal_to_k", r'''
// LeetCode 2447 - Number of Subarrays With GCD Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

object Solution {
  def subarrayGCD(nums: Array[Int], k: Int): Int = {
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
    var ans = 0
    val n = nums.length
    var i = 0
    while (i < n) {
      var g = 0
      var j = i
      while (j < n) {
        g = gcd(g, nums(j))
        if (g < k) j = n
        else {
          if (g == k) ans += 1
          j += 1
        }
      }
      i += 1
    }
    ans
  }
}
''')

w("2448_minimum_cost_to_make_array_equal", r'''
// LeetCode 2448 - Minimum Cost to Make Array Equal
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/

object Solution {
  def minCost(nums: Array[Int], cost: Array[Int]): Long = {
    val n = nums.length
    val idx = Array.tabulate(n)(identity)
    scala.util.Sorting.stableSort(idx, (a: Int, b: Int) => nums(a) < nums(b) || (nums(a) == nums(b) && a < b))
    var totalCost = 0L
    var i = 0
    while (i < n) { totalCost += cost(i); i += 1 }
    var pref = 0L
    var median = 0
    i = 0
    var found = false
    while (i < n && !found) {
      pref += cost(idx(i))
      if (pref * 2 >= totalCost) {
        median = nums(idx(i))
        found = true
      }
      i += 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      var diff = nums(i).toLong - median
      if (diff < 0) diff = -diff
      ans += diff * cost(i)
      i += 1
    }
    ans
  }
}
''')

w("2449_minimum_number_of_operations_to_make_arrays_similar", r'''
// LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

object Solution {
  def makeSimilar(nums: Array[Int], target: Array[Int]): Long = {
    scala.util.Sorting.quickSort(nums)
    scala.util.Sorting.quickSort(target)
    val oddN = scala.collection.mutable.ArrayBuffer.empty[Int]
    val evenN = scala.collection.mutable.ArrayBuffer.empty[Int]
    val oddT = scala.collection.mutable.ArrayBuffer.empty[Int]
    val evenT = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < nums.length) {
      if (nums(i) % 2 == 0) evenN += nums(i) else oddN += nums(i)
      i += 1
    }
    i = 0
    while (i < target.length) {
      if (target(i) % 2 == 0) evenT += target(i) else oddT += target(i)
      i += 1
    }
    var ans = 0L
    i = 0
    while (i < oddN.length) {
      val diff = oddN(i) - oddT(i)
      if (diff > 0) ans += diff / 2
      i += 1
    }
    i = 0
    while (i < evenN.length) {
      val diff = evenN(i) - evenT(i)
      if (diff > 0) ans += diff / 2
      i += 1
    }
    ans
  }
}
''')

w("2450_number_of_distinct_binary_strings_after_applying_operations", r'''
// LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
// https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

object Solution {
  def countDistinctStrings(s: String, k: Int): Int = {
    val mod = 1000000007
    val n = s.length
    var ans = 1
    var i = 0
    while (i < n - k + 1) {
      ans = (ans * 2L % mod).toInt
      i += 1
    }
    ans
  }
}
''')

w("2451_odd_string_difference", r'''
// LeetCode 2451 - Odd String Difference
// https://leetcode.com/problems/odd-string-difference/

object Solution {
  def oddString(words: Array[String]): String = {
    def diff(w: String): String = {
      val b = new StringBuilder()
      var i = 1
      while (i < w.length) {
        val d = w.charAt(i) - w.charAt(i - 1)
        b.append((d + 128).toChar)
        b.append(',')
        i += 1
      }
      b.toString
    }
    val d0 = diff(words(0))
    val d1 = diff(words(1))
    if (d0 == d1) {
      var i = 2
      while (i < words.length) {
        if (diff(words(i)) != d0) return words(i)
        i += 1
      }
    }
    if (diff(words(2)) == d0) words(1) else words(0)
  }
}
''')

w("2452_words_within_two_edits_of_dictionary", r'''
// LeetCode 2452 - Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

object Solution {
  def twoEditWords(queries: Array[String], dictionary: Array[String]): List[String] = {
    val ans = scala.collection.mutable.ListBuffer.empty[String]
    var qi = 0
    while (qi < queries.length) {
      val q = queries(qi)
      var ok = false
      var di = 0
      while (di < dictionary.length && !ok) {
        val d = dictionary(di)
        var df = 0
        var i = 0
        while (i < q.length) {
          if (q.charAt(i) != d.charAt(i)) {
            df += 1
            if (df > 2) i = q.length
          }
          i += 1
        }
        if (df <= 2) ok = true
        di += 1
      }
      if (ok) ans += q
      qi += 1
    }
    ans.toList
  }
}
''')

w("2453_destroy_sequential_targets", r'''
// LeetCode 2453 - Destroy Sequential Targets
// https://leetcode.com/problems/destroy-sequential-targets/

object Solution {
  def destroyTargets(nums: Array[Int], space: Int): Int = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var i = 0
    while (i < nums.length) {
      val m = nums(i) % space
      cnt(m) = cnt.getOrElse(m, 0) + 1
      i += 1
    }
    var bestCnt = 0
    cnt.values.foreach { c => if (c > bestCnt) bestCnt = c }
    var ans = 1000000000
    cnt.foreach { case (key, value) =>
      if (value == bestCnt) {
        var j = 0
        while (j < nums.length) {
          if (nums(j) % space == key && nums(j) < ans) ans = nums(j)
          j += 1
        }
      }
    }
    ans
  }
}
''')

w("2454_next_greater_element_iv", r'''
// LeetCode 2454 - Next Greater Element IV
// https://leetcode.com/problems/next-greater-element-iv/

object Solution {
  def secondGreaterElement(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val ans = Array.fill(n)(-1)
    val stack1 = scala.collection.mutable.ArrayBuffer.empty[Int]
    val stack2 = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < n) {
      val x = nums(i)
      while (stack2.nonEmpty && nums(stack2.last) < x) {
        ans(stack2.last) = x
        stack2.remove(stack2.length - 1)
      }
      val tmp = scala.collection.mutable.ArrayBuffer.empty[Int]
      while (stack1.nonEmpty && nums(stack1.last) < x) {
        tmp += stack1.last
        stack1.remove(stack1.length - 1)
      }
      var j = tmp.length - 1
      while (j >= 0) {
        stack2 += tmp(j)
        j -= 1
      }
      stack1 += i
      i += 1
    }
    ans
  }
}
''')

w("2455_average_value_of_even_numbers_that_are_divisible_by_three", r'''
// LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

object Solution {
  def averageValue(nums: Array[Int]): Int = {
    var sum = 0
    var cnt = 0
    var i = 0
    while (i < nums.length) {
      if (nums(i) % 6 == 0) {
        sum += nums(i)
        cnt += 1
      }
      i += 1
    }
    if (cnt == 0) 0 else sum / cnt
  }
}
''')

w("2456_most_popular_video_creator", r'''
// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

object Solution {
  private class Info(var total: Long, var bestID: String, var bestViews: Int)

  def mostPopularCreator(creators: Array[String], ids: Array[String], views: Array[Int]): List[List[String]] = {
    val mp = scala.collection.mutable.LinkedHashMap.empty[String, Info]
    var maxTotal = 0L
    var i = 0
    while (i < creators.length) {
      mp.get(creators(i)) match {
        case None =>
          mp(creators(i)) = new Info(views(i).toLong, ids(i), views(i))
        case Some(info) =>
          info.total += views(i)
          if (views(i) > info.bestViews || (views(i) == info.bestViews && ids(i) < info.bestID)) {
            info.bestViews = views(i)
            info.bestID = ids(i)
          }
      }
      val t = mp(creators(i)).total
      if (t > maxTotal) maxTotal = t
      i += 1
    }
    val ans = scala.collection.mutable.ListBuffer.empty[List[String]]
    mp.foreach { case (name, info) =>
      if (info.total == maxTotal) ans += List(name, info.bestID)
    }
    ans.toList
  }
}
''')

w("2457_minimum_addition_to_make_integer_beautiful", r'''
// LeetCode 2457 - Minimum Addition to Make Integer Beautiful
// https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

object Solution {
  def makeIntegerBeautiful(n: Long, target: Int): Long = {
    def digitSum(x0: Long): Int = {
      var x = x0
      var s = 0
      while (x > 0) {
        s += (x % 10).toInt
        x /= 10
      }
      s
    }
    val orig = n
    var cur = n
    var pow10 = 1L
    while (digitSum(cur) > target) {
      cur = cur / 10 + 1
      pow10 *= 10
    }
    cur * pow10 - orig
  }
}
''')

w("2458_height_of_binary_tree_after_subtree_removal_queries", r'''
// LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def treeQueries(root: TreeNode, queries: Array[Int]): Array[Int] = {
    val height = scala.collection.mutable.Map.empty[Int, Int]
    val level = scala.collection.mutable.Map.empty[Int, Int]
    val levelMax = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]

    def dfs(node: TreeNode, d: Int): Int = {
      if (node == null) return -1
      level(node.value) = d
      val h = 1 + math.max(dfs(node.left, d + 1), dfs(node.right, d + 1))
      height(node.value) = h
      val arr = levelMax.getOrElseUpdate(d, scala.collection.mutable.ArrayBuffer.empty[Int])
      if (arr.isEmpty) arr += h
      else if (h >= arr(0)) {
        if (arr.length == 1) arr += arr(0)
        else arr(1) = arr(0)
        arr(0) = h
      } else if (arr.length == 1 || h > arr(1)) {
        if (arr.length == 1) arr += h
        else arr(1) = h
      }
      h
    }

    dfs(root, 0)
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      val q = queries(i)
      val d = level(q)
      val h = height(q)
      val top = levelMax(d)
      if (top(0) == h) {
        if (top.length > 1) ans(i) = d + top(1)
        else ans(i) = d - 1
      } else {
        ans(i) = d + top(0)
      }
      i += 1
    }
    ans
  }
}
''')

w("2459_sort_array_by_moving_items_to_empty_space", r'''
// LeetCode 2459 - Sort Array by Moving Items to Empty Space
// https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

object Solution {
  def sortArray(nums: Array[Int]): Int = {
    math.min(solveOne(nums, startZero = true), solveOne(nums, startZero = false))
  }

  private def solveOne(nums: Array[Int], startZero: Boolean): Int = {
    val n = nums.length
    val arr = nums.clone()
    val pos = scala.collection.mutable.Map.empty[Int, Int]
    var i = 0
    while (i < n) {
      pos(arr(i)) = i
      i += 1
    }
    var ops = 0
    while (true) {
      val empty = pos(0)
      val should = if (startZero) empty else if (empty == n - 1) 0 else empty + 1
      if (arr(empty) == should) {
        var found = -1
        i = 0
        while (i < n && found == -1) {
          val want = if (startZero) i else if (i == n - 1) 0 else i + 1
          if (arr(i) != want) found = i
          i += 1
        }
        if (found == -1) return ops
        val v = arr(found)
        arr(empty) = arr(found)
        arr(found) = 0
        pos(0) = found
        pos(v) = empty
        ops += 1
      } else {
        val j = pos(should)
        val vv = arr(j)
        arr(empty) = arr(j)
        arr(j) = 0
        pos(0) = j
        pos(vv) = empty
        ops += 1
      }
    }
    0
  }
}
''')

w("2460_apply_operations_to_an_array", r'''
// LeetCode 2460 - Apply Operations to an Array
// https://leetcode.com/problems/apply-operations-to-an-array/

object Solution {
  def applyOperations(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    var i = 0
    while (i + 1 < n) {
      if (nums(i) == nums(i + 1)) {
        nums(i) *= 2
        nums(i + 1) = 0
      }
      i += 1
    }
    val ans = new Array[Int](n)
    var j = 0
    i = 0
    while (i < n) {
      if (nums(i) != 0) {
        ans(j) = nums(i)
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("2461_maximum_sum_of_distinct_subarrays_with_length_k", r'''
// LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

object Solution {
  def maximumSubarraySum(nums: Array[Int], k: Int): Long = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var sum = 0L
    var ans = 0L
    var i = 0
    while (i < nums.length) {
      sum += nums(i)
      cnt(nums(i)) = cnt.getOrElse(nums(i), 0) + 1
      if (i >= k) {
        val y = nums(i - k)
        sum -= y
        val c = cnt(y) - 1
        if (c == 0) cnt.remove(y) else cnt(y) = c
      }
      if (i >= k - 1 && cnt.size == k && sum > ans) ans = sum
      i += 1
    }
    ans
  }
}
''')

w("2462_total_cost_to_hire_k_workers", r'''
// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

object Solution {
  def totalCost(costs: Array[Int], k: Int, candidates: Int): Long = {
    implicit val ord: Ordering[(Int, Int)] = Ordering.Tuple2[Int, Int]
    val leftH = scala.collection.mutable.PriorityQueue.empty[(Int, Int)](ord.reverse)
    val rightH = scala.collection.mutable.PriorityQueue.empty[(Int, Int)](ord.reverse)
    val n = costs.length
    var l = 0
    var r = n - 1
    while (l <= r && leftH.size < candidates) {
      leftH.enqueue((costs(l), l))
      l += 1
    }
    while (r >= l && rightH.size < candidates) {
      rightH.enqueue((costs(r), r))
      r -= 1
    }
    var ans = 0L
    var t = 0
    while (t < k) {
      var useLeft = false
      if (leftH.nonEmpty && rightH.nonEmpty) {
        val lt = leftH.head
        val rt = rightH.head
        if (lt._1 < rt._1 || (lt._1 == rt._1 && lt._2 <= rt._2)) useLeft = true
      } else if (leftH.nonEmpty) {
        useLeft = true
      }
      if (useLeft) {
        ans += leftH.dequeue()._1
        if (l <= r) {
          leftH.enqueue((costs(l), l))
          l += 1
        }
      } else {
        ans += rightH.dequeue()._1
        if (l <= r) {
          rightH.enqueue((costs(r), r))
          r -= 1
        }
      }
      t += 1
    }
    ans
  }
}
''')

w("2463_minimum_total_distance_traveled", r'''
// LeetCode 2463 - Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/

object Solution {
  def minimumTotalDistance(robot: List[Int], factory: Array[Array[Int]]): Long = {
    val robots = robot.sorted
    val fac = factory.sortBy(_(0))
    val m = robots.length
    val pos = scala.collection.mutable.ArrayBuffer.empty[Int]
    fac.foreach { f =>
      var c = 0
      while (c < f(1)) {
        pos += f(0)
        c += 1
      }
    }
    val n = pos.length
    val INF = 1L << 60
    val dp = Array.fill(m + 1, n + 1)(INF)
    var j = 0
    while (j <= n) {
      dp(0)(j) = 0
      j += 1
    }
    var i = 1
    while (i <= m) {
      j = i
      while (j <= n) {
        dp(i)(j) = dp(i)(j - 1)
        var diff = robots(i - 1).toLong - pos(j - 1)
        if (diff < 0) diff = -diff
        if (dp(i - 1)(j - 1) + diff < dp(i)(j)) dp(i)(j) = dp(i - 1)(j - 1) + diff
        j += 1
      }
      i += 1
    }
    dp(m)(n)
  }
}
''')

w("2464_minimum_subarrays_in_a_valid_split", r'''
// LeetCode 2464 - Minimum Subarrays in a Valid Split
// https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

object Solution {
  def validSubarraySplit(nums: Array[Int]): Int = {
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
    val n = nums.length
    val INF = 1 << 30
    val dp = Array.fill(n + 1)(INF)
    dp(0) = 0
    var i = 0
    while (i < n) {
      if (dp(i) < INF) {
        var j = i
        while (j < n) {
          if (gcd(nums(i), nums(j)) > 1) {
            if (dp(i) + 1 < dp(j + 1)) dp(j + 1) = dp(i) + 1
          }
          j += 1
        }
      }
      i += 1
    }
    if (dp(n) >= INF) -1 else dp(n)
  }
}
''')

w("2465_number_of_distinct_averages", r'''
// LeetCode 2465 - Number of Distinct Averages
// https://leetcode.com/problems/number-of-distinct-averages/

object Solution {
  def distinctAverages(nums: Array[Int]): Int = {
    scala.util.Sorting.quickSort(nums)
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var l = 0
    var r = nums.length - 1
    while (l < r) {
      seen += nums(l) + nums(r)
      l += 1
      r -= 1
    }
    seen.size
  }
}
''')
