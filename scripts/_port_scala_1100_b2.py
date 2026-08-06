# Temporary batch port script for Scala 1136-1185. Delete after use.
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(folder: str, code: str) -> None:
    (ROOT / folder / "Solution.scala").write_text(code.strip() + "\n", encoding="utf-8")
    print(f"wrote {folder}")


SOLUTIONS = {}

SOLUTIONS["1136_parallel_courses"] = r'''
// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

object Solution {
  def minimumSemesters(n: Int, relations: Array[Array[Int]]): Int = {
    val graph = Array.fill(n + 1)(scala.collection.mutable.ListBuffer.empty[Int])
    val indegree = Array.fill(n + 1)(0)
    for (e <- relations) {
      graph(e(0)) += e(1)
      indegree(e(1)) += 1
    }
    val q = scala.collection.mutable.Queue[Int]()
    for (i <- 1 to n if indegree(i) == 0) q.enqueue(i)
    var semesters = 0
    var taken = 0
    while (q.nonEmpty) {
      semesters += 1
      val size = q.size
      for (_ <- 0 until size) {
        val course = q.dequeue()
        taken += 1
        for (nxt <- graph(course)) {
          indegree(nxt) -= 1
          if (indegree(nxt) == 0) q.enqueue(nxt)
        }
      }
    }
    if (taken == n) semesters else -1
  }
}
'''

SOLUTIONS["1137_n_th_tribonacci_number"] = r'''
// LeetCode 1137 - N-th Tribonacci Number
// https://leetcode.com/problems/n-th-tribonacci-number/

object Solution {
  def tribonacci(n: Int): Int = {
    if (n == 0) return 0
    if (n <= 2) return 1
    var a = 0
    var b = 1
    var c = 1
    for (_ <- 3 to n) {
      val next = a + b + c
      a = b
      b = c
      c = next
    }
    c
  }
}
'''

SOLUTIONS["1138_alphabet_board_path"] = r'''
// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

object Solution {
  def alphabetBoardPath(target: String): String = {
    var row = 0
    var col = 0
    val ans = new StringBuilder
    def moveTo(r: Int, c: Int): Unit = {
      while (row < r) { ans += 'D'; row += 1 }
      while (col > c) { ans += 'L'; col -= 1 }
      while (col < c) { ans += 'R'; col += 1 }
      while (row > r) { ans += 'U'; row -= 1 }
    }
    for (ch <- target) {
      val r = (ch - 'a') / 5
      val c = (ch - 'a') % 5
      if (r == 5) {
        while (col > 0) { ans += 'L'; col -= 1 }
        while (row < 5) { ans += 'D'; row += 1 }
      } else {
        moveTo(r, c)
      }
      ans += '!'
    }
    ans.toString
  }
}
'''

SOLUTIONS["1139_largest_1_bordered_square"] = r'''
// LeetCode 1139 - Largest 1-Bordered Square
// https://leetcode.com/problems/largest-1-bordered-square/

object Solution {
  def largest1BorderedSquare(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val left = Array.ofDim[Int](m, n)
    val up = Array.ofDim[Int](m, n)
    for (r <- 0 until m; c <- 0 until n if grid(r)(c) == 1) {
      left(r)(c) = 1 + (if (c > 0) left(r)(c - 1) else 0)
      up(r)(c) = 1 + (if (r > 0) up(r - 1)(c) else 0)
    }
    var best = 0
    for (r <- 0 until m; c <- 0 until n if grid(r)(c) == 1) {
      val limit = math.min(left(r)(c), up(r)(c))
      var size = limit
      var done = false
      while (size > 0 && !done) {
        if (left(r - size + 1)(c) >= size && up(r)(c - size + 1) >= size) {
          best = math.max(best, size)
          done = true
        }
        size -= 1
      }
    }
    best * best
  }
}
'''

SOLUTIONS["1140_stone_game_ii"] = r'''
// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

object Solution {
  def stoneGameII(piles: Array[Int]): Int = {
    val n = piles.length
    val suffix = Array.ofDim[Int](n + 1)
    for (i <- n - 1 to 0 by -1) suffix(i) = suffix(i + 1) + piles(i)
    val memo = scala.collection.mutable.Map.empty[(Int, Int), Int]
    def dfs(i: Int, m: Int): Int = {
      if (i >= n) return 0
      if (i + m >= n) return suffix(i)
      memo.getOrElseUpdate((i, m), {
        var minOpp = Int.MaxValue
        for (x <- 1 to math.min(2 * m, n - i)) {
          minOpp = math.min(minOpp, dfs(i + x, math.max(x, m)))
        }
        suffix(i) - minOpp
      })
    }
    dfs(0, 1)
  }
}
'''

SOLUTIONS["1143_longest_common_subsequence"] = r'''
// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

object Solution {
  def longestCommonSubsequence(text1: String, text2: String): Int = {
    val m = text1.length
    val n = text2.length
    val dp = Array.ofDim[Int](n + 1)
    for (i <- 1 to m) {
      var prev = 0
      for (j <- 1 to n) {
        val cur = dp(j)
        if (text1(i - 1) == text2(j - 1)) dp(j) = prev + 1
        else dp(j) = math.max(dp(j), dp(j - 1))
        prev = cur
      }
    }
    dp(n)
  }
}
'''

SOLUTIONS["1144_decrease_elements_to_make_array_zigzag"] = r'''
// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

object Solution {
  def movesToMakeZigzag(nums: Array[Int]): Int = {
    def cost(start: Int): Int = {
      var ans = 0
      var i = start
      while (i < nums.length) {
        val left = if (i > 0) nums(i - 1) else Int.MaxValue
        val right = if (i + 1 < nums.length) nums(i + 1) else Int.MaxValue
        ans += math.max(0, nums(i) - math.min(left, right) + 1)
        i += 2
      }
      ans
    }
    math.min(cost(0), cost(1))
  }
}
'''

SOLUTIONS["1145_binary_tree_coloring_game"] = r'''
// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def btreeGameWinningMove(root: TreeNode, n: Int, x: Int): Boolean = {
    var leftCount = 0
    var rightCount = 0
    def dfs(node: TreeNode): Int = {
      if (node == null) return 0
      val l = dfs(node.left)
      val r = dfs(node.right)
      if (node.value == x) {
        leftCount = l
        rightCount = r
      }
      l + r + 1
    }
    dfs(root)
    math.max(leftCount, math.max(rightCount, n - leftCount - rightCount - 1)) > n / 2
  }
}
'''

SOLUTIONS["1146_snapshot_array"] = r'''
// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

class SnapshotArray(_length: Int) {
  private var snapId = 0
  private val data = Array.fill(_length)(scala.collection.mutable.ArrayBuffer((0, 0)))

  def set(index: Int, `val`: Int): Unit = {
    val hist = data(index)
    if (hist.last._1 == snapId) hist(hist.length - 1) = (snapId, `val`)
    else hist += ((snapId, `val`))
  }

  def snap(): Int = {
    snapId += 1
    snapId - 1
  }

  def get(index: Int, snap_id: Int): Int = {
    val hist = data(index)
    var lo = 0
    var hi = hist.length - 1
    var ans = 0
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      if (hist(mid)._1 <= snap_id) {
        ans = hist(mid)._2
        lo = mid + 1
      } else hi = mid - 1
    }
    ans
  }
}
'''

SOLUTIONS["1147_longest_chunked_palindrome_decomposition"] = r'''
// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

object Solution {
  def longestDecomposition(text: String): Int = {
    val n = text.length
    var ans = 0
    var i = 0
    while (i < n - i) {
      var found = false
      var length = 1
      val limit = (n - 2 * i) / 2
      while (length <= limit && !found) {
        if (text.substring(i, i + length) == text.substring(n - i - length, n - i)) {
          ans += 2
          i += length
          found = true
        } else length += 1
      }
      if (!found) {
        ans += 1
        return ans
      }
    }
    ans
  }
}
'''

SOLUTIONS["1150_check_if_a_number_is_majority_element_in_a_sorted_array"] = r'''
// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

object Solution {
  def isMajorityElement(nums: Array[Int], target: Int): Boolean = {
    def lowerBound(x: Int): Int = {
      var lo = 0
      var hi = nums.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (nums(mid) < x) lo = mid + 1 else hi = mid
      }
      lo
    }
    def upperBound(x: Int): Int = {
      var lo = 0
      var hi = nums.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (nums(mid) <= x) lo = mid + 1 else hi = mid
      }
      lo
    }
    upperBound(target) - lowerBound(target) > nums.length / 2
  }
}
'''

SOLUTIONS["1151_minimum_swaps_to_group_all_1s_together"] = r'''
// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

object Solution {
  def minSwaps(data: Array[Int]): Int = {
    val ones = data.sum
    if (ones <= 1) return 0
    var cur = data.take(ones).sum
    var best = cur
    for (i <- ones until data.length) {
      cur += data(i) - data(i - ones)
      best = math.max(best, cur)
    }
    ones - best
  }
}
'''

SOLUTIONS["1152_analyze_user_website_visit_pattern"] = r'''
// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

object Solution {
  def mostVisitedPattern(username: Array[String], timestamp: Array[Int], website: Array[String]): List[String] = {
    val visits = scala.collection.mutable.Map.empty[String, scala.collection.mutable.ListBuffer[(Int, String)]]
    for (i <- username.indices) {
      visits.getOrElseUpdate(username(i), scala.collection.mutable.ListBuffer.empty) += ((timestamp(i), website(i)))
    }
    val scores = scala.collection.mutable.Map.empty[(String, String, String), Int]
    for ((_, vs) <- visits) {
      val sites = vs.sortBy(_._1).map(_._2)
      val patterns = scala.collection.mutable.Set.empty[(String, String, String)]
      for (i <- sites.indices; j <- i + 1 until sites.length; k <- j + 1 until sites.length) {
        patterns += ((sites(i), sites(j), sites(k)))
      }
      for (p <- patterns) scores(p) = scores.getOrElse(p, 0) + 1
    }
    val best = scores.minBy { case (p, c) => (-c, p._1, p._2, p._3) }._1
    List(best._1, best._2, best._3)
  }
}
'''

SOLUTIONS["1153_string_transforms_into_another_string"] = r'''
// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

object Solution {
  def canConvert(str1: String, str2: String): Boolean = {
    if (str1 == str2) return true
    val mapping = scala.collection.mutable.Map.empty[Char, Char]
    for (i <- str1.indices) {
      val a = str1(i)
      val b = str2(i)
      if (mapping.contains(a) && mapping(a) != b) return false
      mapping(a) = b
    }
    str2.toSet.size < 26
  }
}
'''

SOLUTIONS["1154_day_of_the_year"] = r'''
// LeetCode 1154 - Day of the Year
// https://leetcode.com/problems/day-of-the-year/

object Solution {
  def dayOfYear(date: String): Int = {
    val parts = date.split("-").map(_.toInt)
    val year = parts(0)
    val month = parts(1)
    val day = parts(2)
    val leap = year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)
    val days = Array(31, if (leap) 29 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days.take(month - 1).sum + day
  }
}
'''

SOLUTIONS["1155_number_of_dice_rolls_with_target_sum"] = r'''
// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

object Solution {
  def numRollsToTarget(n: Int, k: Int, target: Int): Int = {
    val MOD = 1000000007
    var dp = Array.ofDim[Int](target + 1)
    dp(0) = 1
    for (_ <- 0 until n) {
      val neu = Array.ofDim[Int](target + 1)
      for (s <- 0 to target if dp(s) != 0; face <- 1 to k if s + face <= target) {
        neu(s + face) = (neu(s + face) + dp(s)) % MOD
      }
      dp = neu
    }
    dp(target)
  }
}
'''

SOLUTIONS["1156_swap_for_longest_repeated_character_substring"] = r'''
// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

object Solution {
  def maxRepOpt1(text: String): Int = {
    val count = text.groupBy(identity).view.mapValues(_.length).toMap
    val n = text.length
    var ans = 0
    var i = 0
    while (i < n) {
      var j = i
      while (j < n && text(j) == text(i)) j += 1
      val length = j - i
      var k = j + 1
      while (k < n && text(k) == text(i)) k += 1
      val length2 = if (j < n) k - j - 1 else 0
      ans = math.max(ans, math.min(length + length2 + 1, count(text(i))))
      i = j
    }
    ans
  }
}
'''

SOLUTIONS["1157_online_majority_element_in_subarray"] = r'''
// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

class MajorityChecker(arr: Array[Int]) {
  private val pos = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
  for (i <- arr.indices) {
    pos.getOrElseUpdate(arr(i), scala.collection.mutable.ArrayBuffer.empty) += i
  }

  def query(left: Int, right: Int, threshold: Int): Int = {
    var candidate = 0
    var count = 0
    for (i <- left to right) {
      if (count == 0) candidate = arr(i)
      count += (if (arr(i) == candidate) 1 else -1)
    }
    val locs = pos(candidate)
    def lower(x: Int): Int = {
      var lo = 0
      var hi = locs.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (locs(mid) < x) lo = mid + 1 else hi = mid
      }
      lo
    }
    def upper(x: Int): Int = {
      var lo = 0
      var hi = locs.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (locs(mid) <= x) lo = mid + 1 else hi = mid
      }
      lo
    }
    val freq = upper(right) - lower(left)
    if (freq >= threshold) candidate else -1
  }
}
'''

SOLUTIONS["1160_find_words_that_can_be_formed_by_characters"] = r'''
// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

object Solution {
  def countCharacters(words: Array[String], chars: String): Int = {
    val avail = chars.groupBy(identity).view.mapValues(_.length).toMap
    words.filter { word =>
      val need = word.groupBy(identity).view.mapValues(_.length).toMap
      need.forall { case (c, cnt) => avail.getOrElse(c, 0) >= cnt }
    }.map(_.length).sum
  }
}
'''

SOLUTIONS["1161_maximum_level_sum_of_a_binary_tree"] = r'''
// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def maxLevelSum(root: TreeNode): Int = {
    val q = scala.collection.mutable.Queue(root)
    var bestSum = Int.MinValue
    var bestLevel = 1
    var level = 1
    while (q.nonEmpty) {
      var total = 0
      val size = q.size
      for (_ <- 0 until size) {
        val node = q.dequeue()
        total += node.value
        if (node.left != null) q.enqueue(node.left)
        if (node.right != null) q.enqueue(node.right)
      }
      if (total > bestSum) {
        bestSum = total
        bestLevel = level
      }
      level += 1
    }
    bestLevel
  }
}
'''

SOLUTIONS["1162_as_far_from_land_as_possible"] = r'''
// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

object Solution {
  def maxDistance(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val q = scala.collection.mutable.Queue[(Int, Int)]()
    for (r <- 0 until n; c <- 0 until n if grid(r)(c) == 1) q.enqueue((r, c))
    if (q.isEmpty || q.size == n * n) return -1
    var dist = -1
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    while (q.nonEmpty) {
      dist += 1
      val size = q.size
      for (_ <- 0 until size) {
        val (r, c) = q.dequeue()
        for ((dr, dc) <- dirs) {
          val nr = r + dr
          val nc = c + dc
          if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid(nr)(nc) == 0) {
            grid(nr)(nc) = 1
            q.enqueue((nr, nc))
          }
        }
      }
    }
    dist
  }
}
'''

SOLUTIONS["1163_last_substring_in_lexicographical_order"] = r'''
// LeetCode 1163 - Last Substring in Lexicographical Order
// https://leetcode.com/problems/last-substring-in-lexicographical-order/

object Solution {
  def lastSubstring(s: String): String = {
    var i = 0
    var j = 1
    var k = 0
    val n = s.length
    while (j + k < n) {
      if (s(i + k) == s(j + k)) k += 1
      else if (s(i + k) > s(j + k)) {
        j = j + k + 1
        k = 0
      } else {
        i = math.max(i + k + 1, j)
        j = i + 1
        k = 0
      }
    }
    s.substring(i)
  }
}
'''

SOLUTIONS["1165_single_row_keyboard"] = r'''
// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

object Solution {
  def calculateTime(keyboard: String, word: String): Int = {
    val pos = keyboard.zipWithIndex.toMap
    var ans = 0
    var prev = 0
    for (ch <- word) {
      ans += math.abs(pos(ch) - prev)
      prev = pos(ch)
    }
    ans
  }
}
'''

SOLUTIONS["1166_design_file_system"] = r'''
// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

class FileSystem() {
  private val paths = scala.collection.mutable.Map("" -> -1)

  def createPath(path: String, value: Int): Boolean = {
    if (paths.contains(path)) return false
    val parent = path.substring(0, path.lastIndexOf('/'))
    if (!paths.contains(parent)) return false
    paths(path) = value
    true
  }

  def get(path: String): Int = paths.getOrElse(path, -1)
}
'''

SOLUTIONS["1167_minimum_cost_to_connect_sticks"] = r'''
// LeetCode 1167 - Minimum Cost to Connect Sticks
// https://leetcode.com/problems/minimum-cost-to-connect-sticks/

object Solution {
  def connectSticks(sticks: Array[Int]): Int = {
    if (sticks.length <= 1) return 0
    val pq = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
    sticks.foreach(pq.enqueue(_))
    var ans = 0
    while (pq.size > 1) {
      val cost = pq.dequeue() + pq.dequeue()
      ans += cost
      pq.enqueue(cost)
    }
    ans
  }
}
'''

SOLUTIONS["1168_optimize_water_distribution_in_a_village"] = r'''
// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

object Solution {
  def minCostToSupplyWater(n: Int, wells: Array[Int], pipes: Array[Array[Int]]): Int = {
    val parent = Array.tabulate(n + 1)(identity)
    def find(x: Int): Int = {
      var cur = x
      while (parent(cur) != cur) {
        parent(cur) = parent(parent(cur))
        cur = parent(cur)
      }
      cur
    }
    val edges = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    for (i <- wells.indices) edges += Array(0, i + 1, wells(i))
    edges ++= pipes
    val sorted = edges.sortBy(_(2))
    var ans = 0
    for (e <- sorted) {
      val a = find(e(0))
      val b = find(e(1))
      if (a != b) {
        parent(b) = a
        ans += e(2)
      }
    }
    ans
  }
}
'''

SOLUTIONS["1169_invalid_transactions"] = r'''
// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

object Solution {
  def invalidTransactions(transactions: Array[String]): List[String] = {
    val parsed = transactions.map { t =>
      val p = t.split(",")
      (p(0), p(1).toInt, p(2).toInt, p(3), t)
    }
    val invalid = scala.collection.mutable.Set.empty[String]
    for (i <- parsed.indices) {
      val (name, time, amount, city, raw) = parsed(i)
      if (amount > 1000) invalid += raw
      for (j <- parsed.indices if i != j) {
        val (name2, time2, _, city2, raw2) = parsed(j)
        if (name == name2 && city != city2 && math.abs(time - time2) <= 60) {
          invalid += raw
          invalid += raw2
        }
      }
    }
    invalid.toList
  }
}
'''

SOLUTIONS["1170_compare_strings_by_frequency_of_the_smallest_character"] = r'''
// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

object Solution {
  def numSmallerByFrequency(queries: Array[String], words: Array[String]): Array[Int] = {
    def f(s: String): Int = s.count(_ == s.min)
    val freqs = words.map(f).sorted
    queries.map { q =>
      val fq = f(q)
      var lo = 0
      var hi = freqs.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (freqs(mid) <= fq) lo = mid + 1 else hi = mid
      }
      freqs.length - lo
    }
  }
}
'''

SOLUTIONS["1171_remove_zero_sum_consecutive_nodes_from_linked_list"] = r'''
// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def removeZeroSumSublists(head: ListNode): ListNode = {
    val dummy = new ListNode(0)
    dummy.next = head
    var prefix = 0
    val seen = scala.collection.mutable.Map(0 -> dummy)
    var node = dummy
    while (node != null) {
      prefix += node.x
      seen(prefix) = node
      node = node.next
    }
    prefix = 0
    node = dummy
    while (node != null) {
      prefix += node.x
      node.next = seen(prefix).next
      node = node.next
    }
    dummy.next
  }
}
'''

SOLUTIONS["1172_dinner_plate_stacks"] = r'''
// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

class DinnerPlates(_capacity: Int) {
  private val capacity = _capacity
  private val stacks = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.ArrayBuffer[Int]]
  private val available = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)

  def push(`val`: Int): Unit = {
    while (available.nonEmpty && (available.head >= stacks.length || stacks(available.head).length == capacity)) {
      available.dequeue()
    }
    if (available.isEmpty) {
      stacks += scala.collection.mutable.ArrayBuffer.empty[Int]
      available.enqueue(stacks.length - 1)
    }
    val idx = available.head
    stacks(idx) += `val`
    if (stacks(idx).length == capacity) available.dequeue()
  }

  def pop(): Int = {
    while (stacks.nonEmpty && stacks.last.isEmpty) stacks.remove(stacks.length - 1)
    if (stacks.isEmpty) -1 else popAtStack(stacks.length - 1)
  }

  def popAtStack(index: Int): Int = {
    if (index < 0 || index >= stacks.length || stacks(index).isEmpty) return -1
    if (stacks(index).length == capacity) available.enqueue(index)
    stacks(index).remove(stacks(index).length - 1)
  }
}
'''

SOLUTIONS["1175_prime_arrangements"] = r'''
// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

object Solution {
  def numPrimeArrangements(n: Int): Int = {
    val MOD = 1000000007L
    def isPrime(x: Int): Boolean = {
      if (x < 2) return false
      var d = 2
      while (d * d <= x) {
        if (x % d == 0) return false
        d += 1
      }
      true
    }
    def fact(x: Int): Long = {
      var res = 1L
      for (i <- 2 to x) res = res * i % MOD
      res
    }
    val primes = (1 to n).count(isPrime)
    ((fact(primes) * fact(n - primes)) % MOD).toInt
  }
}
'''

SOLUTIONS["1176_diet_plan_performance"] = r'''
// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

object Solution {
  def dietPlanPerformance(calories: Array[Int], k: Int, lower: Int, upper: Int): Int = {
    var window = calories.take(k).sum
    var ans = 0
    if (window < lower) ans -= 1
    else if (window > upper) ans += 1
    for (i <- k until calories.length) {
      window += calories(i) - calories(i - k)
      if (window < lower) ans -= 1
      else if (window > upper) ans += 1
    }
    ans
  }
}
'''

SOLUTIONS["1177_can_make_palindrome_from_substring"] = r'''
// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

object Solution {
  def canMakePaliQueries(s: String, queries: Array[Array[Int]]): Array[Boolean] = {
    val prefix = Array.ofDim[Int](s.length + 1)
    var mask = 0
    for (i <- s.indices) {
      mask ^= 1 << (s(i) - 'a')
      prefix(i + 1) = mask
    }
    queries.map { q =>
      val bits = Integer.bitCount(prefix(q(1) + 1) ^ prefix(q(0)))
      bits / 2 <= q(2)
    }
  }
}
'''

SOLUTIONS["1178_number_of_valid_words_for_each_puzzle"] = r'''
// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

object Solution {
  def findNumOfValidWords(words: Array[String], puzzles: Array[String]): Array[Int] = {
    def maskOf(s: String): Int = {
      var mask = 0
      for (ch <- s) mask |= 1 << (ch - 'a')
      mask
    }
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    for (w <- words) {
      val m = maskOf(w)
      freq(m) = freq.getOrElse(m, 0) + 1
    }
    puzzles.map { puzzle =>
      val first = 1 << (puzzle(0) - 'a')
      val full = maskOf(puzzle)
      var sub = full
      var total = 0
      var done = false
      while (!done) {
        if ((sub & first) != 0) total += freq.getOrElse(sub, 0)
        if (sub == 0) done = true
        else sub = (sub - 1) & full
      }
      total
    }
  }
}
'''

SOLUTIONS["1180_count_substrings_with_only_one_distinct_letter"] = r'''
// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

object Solution {
  def countLetters(s: String): Int = {
    var ans = 1
    var length = 1
    for (i <- 1 until s.length) {
      length = if (s(i) == s(i - 1)) length + 1 else 1
      ans += length
    }
    ans
  }
}
'''

SOLUTIONS["1181_before_and_after_puzzle"] = r'''
// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

object Solution {
  def beforeAndAfterPuzzles(phrases: Array[String]): List[String] = {
    val split = phrases.map(_.split(" ").toSeq)
    val result = scala.collection.mutable.Set.empty[String]
    for (i <- split.indices; j <- split.indices if i != j) {
      if (split(i).last == split(j).head) {
        result += (split(i) ++ split(j).tail).mkString(" ")
      }
    }
    result.toList.sorted
  }
}
'''

SOLUTIONS["1182_shortest_distance_to_target_color"] = r'''
// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

object Solution {
  def shortestDistanceColor(colors: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val pos = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    for (i <- colors.indices) {
      pos.getOrElseUpdate(colors(i), scala.collection.mutable.ArrayBuffer.empty) += i
    }
    queries.map { q =>
      val i = q(0)
      val c = q(1)
      if (!pos.contains(c)) -1
      else {
        val arr = pos(c)
        var lo = 0
        var hi = arr.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (arr(mid) < i) lo = mid + 1 else hi = mid
        }
        var best = Int.MaxValue
        if (lo < arr.length) best = math.min(best, arr(lo) - i)
        if (lo > 0) best = math.min(best, i - arr(lo - 1))
        if (best == Int.MaxValue) -1 else best
      }
    }
  }
}
'''

SOLUTIONS["1183_maximum_number_of_ones"] = r'''
// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

object Solution {
  def maximumNumberOfOnes(width: Int, height: Int, sideLength: Int, maxOnes: Int): Int = {
    val counts = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (r <- 0 until sideLength; c <- 0 until sideLength) {
      val rows = (height - r + sideLength - 1) / sideLength
      val cols = (width - c + sideLength - 1) / sideLength
      counts += rows * cols
    }
    counts.sorted.reverse.take(maxOnes).sum
  }
}
'''

SOLUTIONS["1184_distance_between_bus_stops"] = r'''
// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

object Solution {
  def distanceBetweenBusStops(distance: Array[Int], start: Int, destination: Int): Int = {
    val (a, b) = if (start > destination) (destination, start) else (start, destination)
    val clockwise = distance.slice(a, b).sum
    math.min(clockwise, distance.sum - clockwise)
  }
}
'''

SOLUTIONS["1185_day_of_the_week"] = r'''
// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

object Solution {
  def dayOfTheWeek(day: Int, month: Int, year: Int): String = {
    val names = Array("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    val cal = java.util.Calendar.getInstance()
    cal.set(year, month - 1, day)
    names(cal.get(java.util.Calendar.DAY_OF_WEEK) - 1)
  }
}
'''


def main() -> None:
    for folder, code in SOLUTIONS.items():
        write(folder, code)
    print(f"done {len(SOLUTIONS)}")


if __name__ == "__main__":
    main()
