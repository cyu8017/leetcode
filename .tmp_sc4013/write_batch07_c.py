#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("2361_minimum_costs_using_the_train_line", r'''
// LeetCode 2361 - Minimum Costs Using the Train Line
// https://leetcode.com/problems/minimum-costs-using-the-train-line/

object Solution {
  def minimumCosts(regular: Array[Int], express: Array[Int], expressCost: Int): Array[Long] = {
    val n = regular.length
    val ans = Array.fill(n)(0L)
    var reg = 0L
    var exp = expressCost.toLong
    var i = 0
    while (i < n) {
      val nextReg = math.min(reg + regular(i), exp + express(i))
      val nextExp = math.min(reg + regular(i) + expressCost, exp + express(i))
      reg = nextReg
      exp = nextExp
      ans(i) = math.min(reg, exp)
      i += 1
    }
    ans
  }
}
''')

w("2363_merge_similar_items", r'''
// LeetCode 2363 - Merge Similar Items
// https://leetcode.com/problems/merge-similar-items/

object Solution {
  def mergeSimilarItems(items1: Array[Array[Int]], items2: Array[Array[Int]]): List[List[Int]] = {
    val mp = scala.collection.mutable.TreeMap.empty[Int, Int]
    items1.foreach(it => mp(it(0)) = mp.getOrElse(it(0), 0) + it(1))
    items2.foreach(it => mp(it(0)) = mp.getOrElse(it(0), 0) + it(1))
    mp.toList.map { case (k, v) => List(k, v) }
  }
}
''')

w("2364_count_number_of_bad_pairs", r'''
// LeetCode 2364 - Count Number of Bad Pairs
// https://leetcode.com/problems/count-number-of-bad-pairs/

object Solution {
  def countBadPairs(nums: Array[Int]): Long = {
    val n = nums.length.toLong
    val total = n * (n - 1) / 2
    val freq = scala.collection.mutable.Map.empty[Int, Long]
    var good = 0L
    var i = 0
    while (i < nums.length) {
      val key = nums(i) - i
      good += freq.getOrElse(key, 0L)
      freq(key) = freq.getOrElse(key, 0L) + 1
      i += 1
    }
    total - good
  }
}
''')

w("2365_task_scheduler_ii", r'''
// LeetCode 2365 - Task Scheduler II
// https://leetcode.com/problems/task-scheduler-ii/

object Solution {
  def taskSchedulerII(tasks: Array[Int], space: Int): Long = {
    val next = scala.collection.mutable.Map.empty[Int, Long]
    var day = 0L
    tasks.foreach { t =>
      day = math.max(day, next.getOrElse(t, 0L))
      day += 1
      next(t) = day + space
    }
    day
  }
}
''')

w("2366_minimum_replacements_to_sort_the_array", r'''
// LeetCode 2366 - Minimum Replacements to Sort the Array
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

object Solution {
  def minimumReplacement(nums: Array[Int]): Long = {
    var ans = 0L
    val n = nums.length
    var prev = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      if (nums(i) <= prev) prev = nums(i)
      else {
        val parts = (nums(i) + prev - 1) / prev
        ans += parts - 1
        prev = nums(i) / parts
      }
      i -= 1
    }
    ans
  }
}
''')

w("2367_number_of_arithmetic_triplets", r'''
// LeetCode 2367 - Number of Arithmetic Triplets
// https://leetcode.com/problems/number-of-arithmetic-triplets/

object Solution {
  def arithmeticTriplets(nums: Array[Int], diff: Int): Int = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    nums.foreach(x => seen += x)
    var ans = 0
    nums.foreach { x =>
      if (seen.contains(x + diff) && seen.contains(x + 2 * diff)) ans += 1
    }
    ans
  }
}
''')

w("2368_reachable_nodes_with_restrictions", r'''
// LeetCode 2368 - Reachable Nodes With Restrictions
// https://leetcode.com/problems/reachable-nodes-with-restrictions/

object Solution {
  def reachableNodes(n: Int, edges: Array[Array[Int]], restricted: Array[Int]): Int = {
    val ban = scala.collection.mutable.HashSet.empty[Int]
    restricted.foreach(x => ban += x)
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    var ans = 0
    val vis = Array.fill(n)(false)
    val q = scala.collection.mutable.Queue.empty[Int]
    q.enqueue(0)
    vis(0) = true
    while (q.nonEmpty) {
      val u = q.dequeue()
      ans += 1
      g(u).foreach { v =>
        if (!vis(v) && !ban.contains(v)) {
          vis(v) = true
          q.enqueue(v)
        }
      }
    }
    ans
  }
}
''')

w("2369_check_if_there_is_a_valid_partition_for_the_array", r'''
// LeetCode 2369 - Check if There is a Valid Partition For The Array
// https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

object Solution {
  def validPartition(nums: Array[Int]): Boolean = {
    val n = nums.length
    val dp = Array.fill(n + 1)(false)
    dp(0) = true
    var i = 1
    while (i <= n) {
      if (i >= 2 && nums(i - 1) == nums(i - 2) && dp(i - 2)) dp(i) = true
      if (i >= 3 && nums(i - 1) == nums(i - 2) && nums(i - 2) == nums(i - 3) && dp(i - 3)) dp(i) = true
      if (i >= 3 && nums(i - 1) == nums(i - 2) + 1 && nums(i - 2) == nums(i - 3) + 1 && dp(i - 3)) dp(i) = true
      i += 1
    }
    dp(n)
  }
}
''')

w("2370_longest_ideal_subsequence", r'''
// LeetCode 2370 - Longest Ideal Subsequence
// https://leetcode.com/problems/longest-ideal-subsequence/

object Solution {
  def longestIdealString(s: String, k: Int): Int = {
    val dp = Array.fill(26)(0)
    var ans = 0
    s.foreach { ch =>
      val c = ch - 'a'
      var best = 0
      var p = 0
      while (p < 26) {
        if (math.abs(c - p) <= k && dp(p) > best) best = dp(p)
        p += 1
      }
      dp(c) = best + 1
      ans = math.max(ans, dp(c))
    }
    ans
  }
}
''')

w("2371_minimize_maximum_value_in_a_grid", r'''
// LeetCode 2371 - Minimize Maximum Value in a Grid
// https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

object Solution {
  def minScore(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val arr = Array.ofDim[Int](m * n, 3)
    var idx = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        arr(idx) = Array(grid(i)(j), i, j)
        idx += 1
        j += 1
      }
      i += 1
    }
    scala.util.Sorting.stableSort(arr, (a: Array[Int], b: Array[Int]) => a(0) < b(0))
    val rowMax = Array.fill(m)(0)
    val colMax = Array.fill(n)(0)
    val ans = Array.ofDim[Int](m, n)
    arr.foreach { cel =>
      val v = math.max(rowMax(cel(1)), colMax(cel(2))) + 1
      ans(cel(1))(cel(2)) = v
      rowMax(cel(1)) = v
      colMax(cel(2)) = v
    }
    ans
  }
}
''')

w("2373_largest_local_values_in_a_matrix", r'''
// LeetCode 2373 - Largest Local Values in a Matrix
// https://leetcode.com/problems/largest-local-values-in-a-matrix/

object Solution {
  def largestLocal(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val n = grid.length
    val ans = Array.ofDim[Int](n - 2, n - 2)
    var i = 0
    while (i < n - 2) {
      var j = 0
      while (j < n - 2) {
        var mx = 0
        var r = i
        while (r < i + 3) {
          var c = j
          while (c < j + 3) {
            if (grid(r)(c) > mx) mx = grid(r)(c)
            c += 1
          }
          r += 1
        }
        ans(i)(j) = mx
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("2374_node_with_highest_edge_score", r'''
// LeetCode 2374 - Node With Highest Edge Score
// https://leetcode.com/problems/node-with-highest-edge-score/

object Solution {
  def edgeScore(edges: Array[Int]): Int = {
    val n = edges.length
    val score = Array.fill(n)(0L)
    var i = 0
    while (i < n) {
      score(edges(i)) += i
      i += 1
    }
    var ans = 0
    i = 1
    while (i < n) {
      if (score(i) > score(ans)) ans = i
      i += 1
    }
    ans
  }
}
''')

w("2375_construct_smallest_number_from_di_string", r'''
// LeetCode 2375 - Construct Smallest Number From DI String
// https://leetcode.com/problems/construct-smallest-number-from-di-string/

object Solution {
  def smallestNumber(pattern: String): String = {
    val n = pattern.length
    val ans = Array.tabulate(n + 1)(i => ('1' + i).toChar)
    var i = 0
    while (i < n) {
      if (pattern.charAt(i) == 'I') i += 1
      else {
        var j = i
        while (j < n && pattern.charAt(j) == 'D') j += 1
        reverse(ans, i, j)
        i = j
      }
    }
    new String(ans)
  }

  private def reverse(a: Array[Char], l0: Int, r0: Int): Unit = {
    var l = l0
    var r = r0
    while (l < r) {
      val t = a(l)
      a(l) = a(r)
      a(r) = t
      l += 1
      r -= 1
    }
  }
}
''')

w("2376_count_special_integers", r'''
// LeetCode 2376 - Count Special Integers
// https://leetcode.com/problems/count-special-integers/

object Solution {
  def countSpecialNumbers(n: Int): Int = {
    val s = n.toString
    val m = s.length
    var ans = 0
    var perm = 9
    var i = 1
    while (i < m) {
      ans += perm
      perm *= (10 - i)
      i += 1
    }
    val used = Array.fill(10)(false)
    i = 0
    while (i < m) {
      val start = if (i == 0) 1 else 0
      val digit = s.charAt(i) - '0'
      var d = start
      while (d < digit) {
        if (!used(d)) {
          var rem = 10 - (i + 1)
          var ways = 1
          var j = i + 1
          while (j < m) {
            ways *= rem
            rem -= 1
            j += 1
          }
          ans += ways
        }
        d += 1
      }
      if (used(digit)) return ans
      used(digit) = true
      i += 1
    }
    ans + 1
  }
}
''')

w("2378_choose_edges_to_maximize_score_in_a_tree", r'''
// LeetCode 2378 - Choose Edges to Maximize Score in a Tree
// https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

object Solution {
  def maxScore(edges: Array[Array[Int]]): Long = {
    val n = edges.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    var i = 1
    while (i < n) {
      val p = edges(i)(0)
      val w = edges(i)(1)
      g(p) += ((i, w))
      i += 1
    }

    def dfs(u: Int): (Long, Long) = {
      var base = 0L
      var bestGain = 0L
      g(u).foreach { case (to, w) =>
        val child = dfs(to)
        base += child._1
        val gain = child._2 + w - child._1
        if (gain > bestGain) bestGain = gain
      }
      (base + bestGain, base)
    }

    dfs(0)._1
  }
}
''')

w("2379_minimum_recolors_to_get_k_consecutive_black_blocks", r'''
// LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

object Solution {
  def minimumRecolors(blocks: String, k: Int): Int = {
    var white = 0
    var i = 0
    while (i < k) {
      if (blocks.charAt(i) == 'W') white += 1
      i += 1
    }
    var ans = white
    i = k
    while (i < blocks.length) {
      if (blocks.charAt(i) == 'W') white += 1
      if (blocks.charAt(i - k) == 'W') white -= 1
      ans = math.min(ans, white)
      i += 1
    }
    ans
  }
}
''')

w("2380_time_needed_to_rearrange_a_binary_string", r'''
// LeetCode 2380 - Time Needed to Rearrange a Binary String
// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

object Solution {
  def secondsToRemoveOccurrences(s: String): Int = {
    var ans = 0
    var zeros = 0
    s.foreach { c =>
      if (c == '0') zeros += 1
      else if (zeros > 0) ans = math.max(ans + 1, zeros)
    }
    ans
  }
}
''')

w("2381_shifting_letters_ii", r'''
// LeetCode 2381 - Shifting Letters II
// https://leetcode.com/problems/shifting-letters-ii/

object Solution {
  def shiftingLetters(s: String, shifts: Array[Array[Int]]): String = {
    val n = s.length
    val diff = Array.fill(n + 1)(0)
    shifts.foreach { sh =>
      val d = if (sh(2) == 0) -1 else 1
      diff(sh(0)) += d
      diff(sh(1) + 1) -= d
    }
    val arr = s.toCharArray
    var cur = 0
    var i = 0
    while (i < n) {
      cur = (cur + diff(i)) % 26
      if (cur < 0) cur += 26
      arr(i) = ('a' + (arr(i) - 'a' + cur) % 26).toChar
      i += 1
    }
    new String(arr)
  }
}
''')

w("2382_maximum_segment_sum_after_removals", r'''
// LeetCode 2382 - Maximum Segment Sum After Removals
// https://leetcode.com/problems/maximum-segment-sum-after-removals/

object Solution {
  def maximumSegmentSum(nums: Array[Int], removeQueries: Array[Int]): Array[Long] = {
    val n = nums.length
    val parent = Array.tabulate(n)(identity)
    val sum = Array.fill(n)(0L)
    val active = Array.fill(n)(false)

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
      if (ra == rb) return
      parent(rb) = ra
      sum(ra) += sum(rb)
    }

    val ans = Array.fill(n)(0L)
    var best = 0L
    var i = n - 1
    while (i >= 0) {
      ans(i) = best
      val idx = removeQueries(i)
      active(idx) = true
      sum(idx) = nums(idx)
      if (idx > 0 && active(idx - 1)) unite(idx, idx - 1)
      if (idx + 1 < n && active(idx + 1)) unite(idx, idx + 1)
      best = math.max(best, sum(find(idx)))
      i -= 1
    }
    ans
  }
}
''')

w("2383_minimum_hours_of_training_to_win_a_competition", r'''
// LeetCode 2383 - Minimum Hours of Training to Win a Competition
// https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

object Solution {
  def minNumberOfHours(initialEnergy: Int, initialExperience: Int, energy: Array[Int], experience: Array[Int]): Int = {
    var ans = 0
    var en = initialEnergy
    var ex = initialExperience
    var i = 0
    while (i < energy.length) {
      if (en <= energy(i)) {
        val need = energy(i) - en + 1
        ans += need
        en += need
      }
      if (ex <= experience(i)) {
        val need = experience(i) - ex + 1
        ans += need
        ex += need
      }
      en -= energy(i)
      ex += experience(i)
      i += 1
    }
    ans
  }
}
''')

w("2384_largest_palindromic_number", r'''
// LeetCode 2384 - Largest Palindromic Number
// https://leetcode.com/problems/largest-palindromic-number/

object Solution {
  def largestPalindromic(num: String): String = {
    val freq = Array.fill(10)(0)
    var i = 0
    while (i < num.length) {
      freq(num.charAt(i) - '0') += 1
      i += 1
    }
    val left = new StringBuilder
    var d = 9
    while (d >= 0) {
      val pairs = freq(d) / 2
      var p = 0
      while (p < pairs) {
        left.append(('0' + d).toChar)
        p += 1
      }
      freq(d) %= 2
      d -= 1
    }
    var mid = 0.toChar
    d = 9
    while (d >= 0) {
      if (freq(d) > 0) {
        mid = ('0' + d).toChar
        d = -1
      } else d -= 1
    }
    if (left.length == 0 || left.charAt(0) == '0') {
      return if (mid == 0) "0" else mid.toString
    }
    val ans = new StringBuilder(left.toString)
    if (mid != 0) ans.append(mid)
    ans.append(left.reverse())
    ans.toString
  }
}
''')

w("2385_amount_of_time_for_binary_tree_to_be_infected", r'''
// LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def amountOfTime(root: TreeNode, start: Int): Int = {
    val g = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]

    def build(node: TreeNode, parent: TreeNode): Unit = {
      if (node == null) return
      if (parent != null) {
        g.getOrElseUpdate(node.value, scala.collection.mutable.ArrayBuffer.empty[Int]) += parent.value
        g.getOrElseUpdate(parent.value, scala.collection.mutable.ArrayBuffer.empty[Int]) += node.value
      }
      build(node.left, node)
      build(node.right, node)
    }

    build(root, null)
    var ans = 0
    val vis = scala.collection.mutable.HashSet(start)
    val q = scala.collection.mutable.Queue((start, 0))
    while (q.nonEmpty) {
      val (cur, dist) = q.dequeue()
      ans = math.max(ans, dist)
      g.getOrElse(cur, scala.collection.mutable.ArrayBuffer.empty[Int]).foreach { nxt =>
        if (vis.add(nxt)) q.enqueue((nxt, dist + 1))
      }
    }
    ans
  }
}
''')

w("2386_find_the_k_sum_of_an_array", r'''
// LeetCode 2386 - Find the K-Sum of an Array
// https://leetcode.com/problems/find-the-k-sum-of-an-array/

object Solution {
  def kSum(nums: Array[Int], k: Int): Long = {
    var total = 0L
    val n = nums.length
    val absNums = Array.fill(n)(0)
    var i = 0
    while (i < n) {
      if (nums(i) >= 0) {
        total += nums(i)
        absNums(i) = nums(i)
      } else absNums(i) = -nums(i)
      i += 1
    }
    java.util.Arrays.sort(absNums)
    val h = scala.collection.mutable.PriorityQueue.empty[(Long, Int)]
    h.enqueue((total, 0))
    var t = 0
    while (t < k - 1) {
      val (sum, idx) = h.dequeue()
      if (idx < absNums.length) {
        h.enqueue((sum - absNums(idx), idx + 1))
        if (idx > 0) h.enqueue((sum - absNums(idx) + absNums(idx - 1), idx + 1))
      }
      t += 1
    }
    h.head._1
  }
}
''')

w("2387_median_of_a_row_wise_sorted_matrix", r'''
// LeetCode 2387 - Median of a Row Wise Sorted Matrix
// https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

object Solution {
  def matrixMedian(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var lo = 1
    var hi = 1000000
    val need = (m * n) / 2 + 1
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (countLE(grid, mid, n) >= need) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def countLE(grid: Array[Array[Int]], x: Int, n: Int): Int = {
    var cnt = 0
    grid.foreach { row =>
      var l = 0
      var r = n
      while (l < r) {
        val mid = (l + r) / 2
        if (row(mid) <= x) l = mid + 1
        else r = mid
      }
      cnt += l
    }
    cnt
  }
}
''')

w("2389_longest_subsequence_with_limited_sum", r'''
// LeetCode 2389 - Longest Subsequence With Limited Sum
// https://leetcode.com/problems/longest-subsequence-with-limited-sum/

object Solution {
  def answerQueries(nums: Array[Int], queries: Array[Int]): Array[Int] = {
    java.util.Arrays.sort(nums)
    var i = 1
    while (i < nums.length) {
      nums(i) += nums(i - 1)
      i += 1
    }
    val ans = Array.fill(queries.length)(0)
    i = 0
    while (i < queries.length) {
      var lo = 0
      var hi = nums.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (nums(mid) <= queries(i)) lo = mid + 1
        else hi = mid
      }
      ans(i) = lo
      i += 1
    }
    ans
  }
}
''')

w("2390_removing_stars_from_a_string", r'''
// LeetCode 2390 - Removing Stars From a String
// https://leetcode.com/problems/removing-stars-from-a-string/

object Solution {
  def removeStars(s: String): String = {
    val stack = new StringBuilder
    s.foreach { c =>
      if (c == '*') stack.deleteCharAt(stack.length - 1)
      else stack.append(c)
    }
    stack.toString
  }
}
''')
