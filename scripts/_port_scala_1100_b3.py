# Temporary batch port script for Scala 1186-1240. Delete after use.
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(folder: str, code: str) -> None:
    (ROOT / folder / "Solution.scala").write_text(code.strip() + "\n", encoding="utf-8")
    print(f"wrote {folder}")


S = {}

S["1186_maximum_subarray_sum_with_one_deletion"] = r'''
// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

object Solution {
  def maximumSum(arr: Array[Int]): Int = {
    var keep = arr(0)
    var delete = arr(0)
    var ans = arr(0)
    for (i <- 1 until arr.length) {
      val x = arr(i)
      delete = math.max(keep, delete + x)
      keep = math.max(keep + x, x)
      ans = math.max(ans, math.max(keep, delete))
    }
    ans
  }
}
'''

S["1187_make_array_strictly_increasing"] = r'''
// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

object Solution {
  def makeArrayIncreasing(arr1: Array[Int], arr2: Array[Int]): Int = {
    val sorted2 = arr2.distinct.sorted
    var dp = Map(-1 -> 0)
    for (num <- arr1) {
      val newDp = scala.collection.mutable.Map.empty[Int, Int]
      for ((prev, ops) <- dp) {
        if (num > prev) newDp(num) = math.min(newDp.getOrElse(num, Int.MaxValue), ops)
        var lo = 0
        var hi = sorted2.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (sorted2(mid) <= prev) lo = mid + 1 else hi = mid
        }
        if (lo < sorted2.length) {
          val chosen = sorted2(lo)
          newDp(chosen) = math.min(newDp.getOrElse(chosen, Int.MaxValue), ops + 1)
        }
      }
      dp = newDp.toMap
      if (dp.isEmpty) return -1
    }
    dp.values.min
  }
}
'''

S["1188_design_bounded_blocking_queue"] = r'''
// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

class BoundedBlockingQueue(capacity: Int) {
  private val queue = new java.util.ArrayDeque[Int]()
  private val notFull = new java.util.concurrent.Semaphore(capacity)
  private val notEmpty = new java.util.concurrent.Semaphore(0)
  private val lock = new Object

  def enqueue(element: Int): Unit = {
    notFull.acquire()
    lock.synchronized { queue.addLast(element) }
    notEmpty.release()
  }

  def dequeue(): Int = {
    notEmpty.acquire()
    val value = lock.synchronized { queue.removeFirst() }
    notFull.release()
    value
  }

  def size(): Int = lock.synchronized { queue.size() }
}
'''

S["1189_maximum_number_of_balloons"] = r'''
// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

object Solution {
  def maxNumberOfBalloons(text: String): Int = {
    val count = text.groupBy(identity).view.mapValues(_.length).toMap.withDefaultValue(0)
    math.min(count('b'), math.min(count('a'), math.min(count('l') / 2, math.min(count('o') / 2, count('n')))))
  }
}
'''

S["1190_reverse_substrings_between_each_pair_of_parentheses"] = r'''
// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

object Solution {
  def reverseParentheses(s: String): String = {
    val stack = scala.collection.mutable.ArrayBuffer.empty[Char]
    for (ch <- s) {
      if (ch == ')') {
        val chunk = scala.collection.mutable.ArrayBuffer.empty[Char]
        while (stack.nonEmpty && stack.last != '(') chunk += stack.remove(stack.length - 1)
        stack.remove(stack.length - 1)
        stack ++= chunk
      } else stack += ch
    }
    stack.mkString
  }
}
'''

S["1191_k_concatenation_maximum_sum"] = r'''
// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

object Solution {
  def kConcatenationMaxSum(arr: Array[Int], k: Int): Int = {
    val MOD = 1000000007
    def kadane(nums: Array[Int]): Long = {
      var best = 0L
      var cur = 0L
      for (x <- nums) {
        cur = math.max(0L, cur + x)
        best = math.max(best, cur)
      }
      best
    }
    val one = kadane(arr)
    if (k == 1) return (one % MOD).toInt
    val two = kadane(arr ++ arr)
    val total = arr.map(_.toLong).sum
    val ans = if (total > 0) math.max(one, two + total * (k - 2)) else math.max(one, two)
    (ans % MOD).toInt
  }
}
'''

S["1192_critical_connections_in_a_network"] = r'''
// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

object Solution {
  def criticalConnections(n: Int, connections: List[List[Int]]): List[List[Int]] = {
    val graph = Array.fill(n)(scala.collection.mutable.ListBuffer.empty[Int])
    for (e <- connections) {
      graph(e(0)) += e(1)
      graph(e(1)) += e(0)
    }
    val disc = Array.fill(n)(-1)
    val low = Array.fill(n)(-1)
    var time = 0
    val bridges = scala.collection.mutable.ListBuffer.empty[List[Int]]
    def dfs(node: Int, parent: Int): Unit = {
      disc(node) = time
      low(node) = time
      time += 1
      for (nxt <- graph(node) if nxt != parent) {
        if (disc(nxt) == -1) {
          dfs(nxt, node)
          low(node) = math.min(low(node), low(nxt))
          if (low(nxt) > disc(node)) bridges += List(math.min(node, nxt), math.max(node, nxt))
        } else low(node) = math.min(low(node), disc(nxt))
      }
    }
    dfs(0, -1)
    bridges.toList
  }
}
'''

S["1195_fizz_buzz_multithreaded"] = r'''
// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

class FizzBuzz(n: Int) {
  private var current = 1
  private val lock = new Object

  private def run(predicate: Int => Boolean, action: => Unit): Unit = {
    lock.synchronized {
      while (current <= n) {
        if (predicate(current)) {
          action
          current += 1
          lock.notifyAll()
        } else lock.wait()
      }
    }
  }

  def fizz(printFizz: Runnable): Unit =
    run(x => x % 3 == 0 && x % 5 != 0, printFizz.run())

  def buzz(printBuzz: Runnable): Unit =
    run(x => x % 5 == 0 && x % 3 != 0, printBuzz.run())

  def fizzbuzz(printFizzBuzz: Runnable): Unit =
    run(x => x % 15 == 0, printFizzBuzz.run())

  def number(printNumber: Int => Unit): Unit =
    run(x => x % 3 != 0 && x % 5 != 0, printNumber(current))
}
'''

S["1196_how_many_apples_can_you_put_into_the_basket"] = r'''
// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

object Solution {
  def maxNumberOfApples(weight: Array[Int]): Int = {
    val sorted = weight.sorted
    var total = 0
    for (i <- sorted.indices) {
      total += sorted(i)
      if (total > 5000) return i
    }
    sorted.length
  }
}
'''

S["1197_minimum_knight_moves"] = r'''
// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

object Solution {
  def minKnightMoves(x: Int, y: Int): Int = {
    val ax = math.abs(x)
    val ay = math.abs(y)
    val memo = scala.collection.mutable.Map.empty[(Int, Int), Int]
    def dfs(a: Int, b: Int): Int = {
      val (aa, bb) = if (a < b) (b, a) else (a, b)
      if (aa + bb == 0) return 0
      if (aa + bb == 2) return 2
      memo.getOrElseUpdate((aa, bb), {
        math.min(dfs(math.abs(aa - 1), math.abs(bb - 2)), dfs(math.abs(aa - 2), math.abs(bb - 1))) + 1
      })
    }
    dfs(ax, ay)
  }
}
'''

S["1198_find_smallest_common_element_in_all_rows"] = r'''
// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

object Solution {
  def smallestCommonElement(mat: Array[Array[Int]]): Int = {
    var common = mat(0).toSet
    for (row <- mat.tail) {
      common = common.intersect(row.toSet)
      if (common.isEmpty) return -1
    }
    common.min
  }
}
'''

S["1199_minimum_time_to_build_blocks"] = r'''
// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

object Solution {
  def minBuildTime(blocks: Array[Int], split: Int): Int = {
    val pq = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
    blocks.foreach(pq.enqueue(_))
    while (pq.size > 1) {
      pq.dequeue()
      pq.enqueue(pq.dequeue() + split)
    }
    pq.dequeue()
  }
}
'''

S["1200_minimum_absolute_difference"] = r'''
// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

object Solution {
  def minimumAbsDifference(arr: Array[Int]): List[List[Int]] = {
    val sorted = arr.sorted
    val best = (0 until sorted.length - 1).map(i => sorted(i + 1) - sorted(i)).min
    (0 until sorted.length - 1).collect {
      case i if sorted(i + 1) - sorted(i) == best => List(sorted(i), sorted(i + 1))
    }.toList
  }
}
'''

S["1201_ugly_number_iii"] = r'''
// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

object Solution {
  def nthUglyNumber(n: Int, a: Int, b: Int, c: Int): Int = {
    def gcd(x: Long, y: Long): Long = if (y == 0) x else gcd(y, x % y)
    def lcm(x: Long, y: Long): Long = x / gcd(x, y) * y
    val aa = a.toLong
    val bb = b.toLong
    val cc = c.toLong
    val ab = lcm(aa, bb)
    val ac = lcm(aa, cc)
    val bc = lcm(bb, cc)
    val abc = lcm(ab, cc)
    def count(x: Long): Long =
      x / aa + x / bb + x / cc - x / ab - x / ac - x / bc + x / abc
    var lo = 1L
    var hi = 2000000000L
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (count(mid) >= n) hi = mid else lo = mid + 1
    }
    lo.toInt
  }
}
'''

S["1202_smallest_string_with_swaps"] = r'''
// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

object Solution {
  def smallestStringWithSwaps(s: String, pairs: List[List[Int]]): String = {
    val parent = Array.tabulate(s.length)(identity)
    def find(x: Int): Int = {
      var cur = x
      while (parent(cur) != cur) {
        parent(cur) = parent(parent(cur))
        cur = parent(cur)
      }
      cur
    }
    for (p <- pairs) parent(find(p(0))) = find(p(1))
    val groups = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ListBuffer[Char]]
    for (i <- s.indices) {
      groups.getOrElseUpdate(find(i), scala.collection.mutable.ListBuffer.empty) += s(i)
    }
    for (chars <- groups.values) {
      val sorted = chars.sorted(Ordering[Char].reverse)
      chars.clear()
      chars ++= sorted
    }
    val sb = new StringBuilder
    for (i <- s.indices) sb += groups(find(i)).remove(groups(find(i)).length - 1)
    sb.toString
  }
}
'''

S["1203_sort_items_by_groups_respecting_dependencies"] = r'''
// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

object Solution {
  def sortItems(n: Int, m: Int, group: Array[Int], beforeItems: Array[List[Int]]): Array[Int] = {
    val grp = group.clone()
    var gm = m
    for (i <- 0 until n if grp(i) == -1) {
      grp(i) = gm
      gm += 1
    }
    val itemGraph = Array.fill(n)(scala.collection.mutable.ListBuffer.empty[Int])
    val itemIndeg = Array.fill(n)(0)
    val groupGraph = Array.fill(gm)(scala.collection.mutable.Set.empty[Int])
    val groupIndeg = Array.fill(gm)(0)
    for (v <- 0 until n; u <- beforeItems(v)) {
      itemGraph(u) += v
      itemIndeg(v) += 1
      if (grp(u) != grp(v) && !groupGraph(grp(u)).contains(grp(v))) {
        groupGraph(grp(u)) += grp(v)
        groupIndeg(grp(v)) += 1
      }
    }
    def topo(graph: Array[_ <: Iterable[Int]], indeg: Array[Int]): Array[Int] = {
      val q = scala.collection.mutable.Queue[Int]()
      for (i <- indeg.indices if indeg(i) == 0) q.enqueue(i)
      val order = scala.collection.mutable.ArrayBuffer.empty[Int]
      while (q.nonEmpty) {
        val u = q.dequeue()
        order += u
        for (v <- graph(u)) {
          indeg(v) -= 1
          if (indeg(v) == 0) q.enqueue(v)
        }
      }
      if (order.length == graph.length) order.toArray else Array.empty
    }
    val items = topo(itemGraph, itemIndeg)
    val groups = topo(groupGraph.map(_.toSeq), groupIndeg)
    if (items.isEmpty || groups.isEmpty) return Array.empty
    val buckets = Array.fill(gm)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (item <- items) buckets(grp(item)) += item
    groups.flatMap(g => buckets(g))
  }
}
'''

S["1206_design_skiplist"] = r'''
// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

class Skiplist() {
  private val values = scala.collection.mutable.ArrayBuffer.empty[Int]

  def search(target: Int): Boolean = {
    val i = lowerBound(target)
    i < values.length && values(i) == target
  }

  def add(num: Int): Unit = {
    val i = lowerBound(num)
    values.insert(i, num)
  }

  def erase(num: Int): Boolean = {
    val i = lowerBound(num)
    if (i == values.length || values(i) != num) false
    else {
      values.remove(i)
      true
    }
  }

  private def lowerBound(x: Int): Int = {
    var lo = 0
    var hi = values.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (values(mid) < x) lo = mid + 1 else hi = mid
    }
    lo
  }
}
'''

S["1207_unique_number_of_occurrences"] = r'''
// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

object Solution {
  def uniqueOccurrences(arr: Array[Int]): Boolean = {
    val counts = arr.groupBy(identity).values.map(_.length).toSeq
    counts.size == counts.toSet.size
  }
}
'''

S["1208_get_equal_substrings_within_budget"] = r'''
// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

object Solution {
  def equalSubstring(s: String, t: String, maxCost: Int): Int = {
    var left = 0
    var cost = 0
    var answer = 0
    for (right <- s.indices) {
      cost += math.abs(s(right) - t(right))
      while (cost > maxCost) {
        cost -= math.abs(s(left) - t(left))
        left += 1
      }
      answer = math.max(answer, right - left + 1)
    }
    answer
  }
}
'''

S["1209_remove_all_adjacent_duplicates_in_string_ii"] = r'''
// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

object Solution {
  def removeDuplicates(s: String, k: Int): String = {
    val stack = scala.collection.mutable.ArrayBuffer.empty[(Char, Int)]
    for (ch <- s) {
      if (stack.nonEmpty && stack.last._1 == ch) {
        val (c, cnt) = stack.remove(stack.length - 1)
        val neu = cnt + 1
        if (neu < k) stack += ((c, neu))
      } else stack += ((ch, 1))
    }
    stack.map { case (c, cnt) => c.toString * cnt }.mkString
  }
}
'''

S["1210_minimum_moves_to_reach_target_with_rotations"] = r'''
// LeetCode 1210 - Minimum Moves to Reach Target with Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

object Solution {
  def minimumMoves(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val start = (0, 0, 0)
    val target = (n - 1, n - 2, 0)
    val q = scala.collection.mutable.Queue((start, 0))
    val seen = scala.collection.mutable.Set(start)
    while (q.nonEmpty) {
      val ((r, c, orient), moves) = q.dequeue()
      if ((r, c, orient) == target) return moves
      val nxt = scala.collection.mutable.ListBuffer.empty[(Int, Int, Int)]
      if (orient == 0) {
        if (c + 2 < n && grid(r)(c + 2) == 0) nxt += ((r, c + 1, 0))
        if (r + 1 < n && grid(r + 1)(c) == 0 && grid(r + 1)(c + 1) == 0) {
          nxt += ((r + 1, c, 0))
          nxt += ((r, c, 1))
        }
      } else {
        if (r + 2 < n && grid(r + 2)(c) == 0) nxt += ((r + 1, c, 1))
        if (c + 1 < n && grid(r)(c + 1) == 0 && grid(r + 1)(c + 1) == 0) {
          nxt += ((r, c + 1, 1))
          nxt += ((r, c, 0))
        }
      }
      for (state <- nxt if !seen.contains(state)) {
        seen += state
        q.enqueue((state, moves + 1))
      }
    }
    -1
  }
}
'''

S["1213_intersection_of_three_sorted_arrays"] = r'''
// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

object Solution {
  def arraysIntersection(arr1: Array[Int], arr2: Array[Int], arr3: Array[Int]): List[Int] =
    (arr1.toSet & arr2.toSet & arr3.toSet).toList.sorted
}
'''

S["1214_two_sum_bsts"] = r'''
// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def twoSumBSTs(root1: TreeNode, root2: TreeNode, target: Int): Boolean = {
    val values = scala.collection.mutable.Set.empty[Int]
    val stack = scala.collection.mutable.Stack[TreeNode]()
    if (root1 != null) stack.push(root1)
    while (stack.nonEmpty) {
      val node = stack.pop()
      values += node.value
      if (node.left != null) stack.push(node.left)
      if (node.right != null) stack.push(node.right)
    }
    if (root2 != null) stack.push(root2)
    while (stack.nonEmpty) {
      val node = stack.pop()
      if (values.contains(target - node.value)) return true
      if (node.left != null) stack.push(node.left)
      if (node.right != null) stack.push(node.right)
    }
    false
  }
}
'''

S["1215_stepping_numbers"] = r'''
// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

object Solution {
  def countSteppingNumbers(low: Int, high: Int): List[Int] = {
    val answer = scala.collection.mutable.ListBuffer.empty[Int]
    if (low == 0) answer += 0
    val q = scala.collection.mutable.Queue((1 to 9): _*)
    while (q.nonEmpty) {
      val x = q.dequeue()
      if (x <= high) {
        if (x >= low) answer += x
        val last = x % 10
        if (last > 0) {
          val next = x * 10L + last - 1
          if (next <= high) q.enqueue(next.toInt)
        }
        if (last < 9) {
          val next = x * 10L + last + 1
          if (next <= high) q.enqueue(next.toInt)
        }
      }
    }
    answer.toList.sorted
  }
}
'''

S["1216_valid_palindrome_iii"] = r'''
// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

object Solution {
  def isValidPalindrome(s: String, k: Int): Boolean = {
    if (s.isEmpty) return true
    val dp = Array.ofDim[Int](s.length)
    for (i <- s.length - 1 to 0 by -1) {
      var previous = 0
      for (j <- i + 1 until s.length) {
        val old = dp(j)
        if (s(i) == s(j)) dp(j) = previous
        else dp(j) = 1 + math.min(dp(j), dp(j - 1))
        previous = old
      }
    }
    dp.last <= k
  }
}
'''

S["1217_minimum_cost_to_move_chips_to_the_same_position"] = r'''
// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

object Solution {
  def minCostToMoveChips(position: Array[Int]): Int = {
    val odd = position.count(x => (x & 1) == 1)
    math.min(odd, position.length - odd)
  }
}
'''

S["1218_longest_arithmetic_subsequence_of_given_difference"] = r'''
// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

object Solution {
  def longestSubsequence(arr: Array[Int], difference: Int): Int = {
    val dp = scala.collection.mutable.Map.empty[Int, Int]
    for (x <- arr) dp(x) = dp.getOrElse(x - difference, 0) + 1
    dp.values.max
  }
}
'''

S["1219_path_with_maximum_gold"] = r'''
// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

object Solution {
  def getMaximumGold(grid: Array[Array[Int]]): Int = {
    val rows = grid.length
    val cols = grid(0).length
    def dfs(r: Int, c: Int): Int = {
      val gold = grid(r)(c)
      grid(r)(c) = 0
      var best = 0
      for ((dr, dc) <- Seq((1, 0), (-1, 0), (0, 1), (0, -1))) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid(nr)(nc) > 0) {
          best = math.max(best, dfs(nr, nc))
        }
      }
      grid(r)(c) = gold
      gold + best
    }
    var ans = 0
    for (r <- 0 until rows; c <- 0 until cols if grid(r)(c) > 0) ans = math.max(ans, dfs(r, c))
    ans
  }
}
'''

S["1220_count_vowels_permutation"] = r'''
// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

object Solution {
  def countVowelPermutation(n: Int): Int = {
    val mod = 1000000007
    var a, e, i, o, u = 1L
    for (_ <- 1 until n) {
      val na = (e + i + u) % mod
      val ne = (a + i) % mod
      val ni = (e + o) % mod
      val no = i
      val nu = (i + o) % mod
      a = na; e = ne; i = ni; o = no; u = nu
    }
    ((a + e + i + o + u) % mod).toInt
  }
}
'''

S["1221_split_a_string_in_balanced_strings"] = r'''
// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

object Solution {
  def balancedStringSplit(s: String): Int = {
    var balance = 0
    var answer = 0
    for (ch <- s) {
      balance += (if (ch == 'L') 1 else -1)
      if (balance == 0) answer += 1
    }
    answer
  }
}
'''

S["1222_queens_that_can_attack_the_king"] = r'''
// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

object Solution {
  def queensAttacktheKing(queens: Array[Array[Int]], king: Array[Int]): List[List[Int]] = {
    val occupied = queens.map(q => (q(0), q(1))).toSet
    val answer = scala.collection.mutable.ListBuffer.empty[List[Int]]
    for (dr <- -1 to 1; dc <- -1 to 1 if !(dr == 0 && dc == 0)) {
      var r = king(0) + dr
      var c = king(1) + dc
      var found = false
      while (r >= 0 && r < 8 && c >= 0 && c < 8 && !found) {
        if (occupied.contains((r, c))) {
          answer += List(r, c)
          found = true
        } else {
          r += dr
          c += dc
        }
      }
    }
    answer.toList
  }
}
'''

S["1223_dice_roll_simulation"] = r'''
// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

object Solution {
  def dieSimulator(n: Int, rollMax: Array[Int]): Int = {
    val mod = 1000000007
    var dp = Array.tabulate(6)(j => Array.fill(rollMax(j) + 1)(0))
    for (j <- 0 until 6) dp(j)(1) = 1
    for (_ <- 1 until n) {
      val totals = dp.map(_.sum % mod)
      val totalSum = totals.sum % mod
      val nxt = Array.tabulate(6)(j => Array.fill(dp(j).length)(0))
      for (j <- 0 until 6) {
        nxt(j)(1) = ((totalSum - totals(j)) % mod + mod) % mod
        for (run <- 2 until dp(j).length) nxt(j)(run) = dp(j)(run - 1)
      }
      dp = nxt
    }
    (dp.map(_.sum.toLong).sum % mod).toInt
  }
}
'''

S["1224_maximum_equal_frequency"] = r'''
// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

object Solution {
  def maxEqualFreq(nums: Array[Int]): Int = {
    val count = scala.collection.mutable.Map.empty[Int, Int].withDefaultValue(0)
    val frequencies = scala.collection.mutable.Map.empty[Int, Int].withDefaultValue(0)
    var answer = 0
    for (i <- 1 to nums.length) {
      val x = nums(i - 1)
      val old = count(x)
      if (old > 0) frequencies(old) -= 1
      count(x) = old + 1
      frequencies(old + 1) += 1
      val high = frequencies.keys.filter(frequencies(_) > 0).max
      if (high == 1 || frequencies(high) * high + 1 == i ||
          (frequencies(high) == 1 && frequencies(high - 1) * (high - 1) + high == i)) {
        answer = i
      }
    }
    answer
  }
}
'''

S["1226_the_dining_philosophers"] = r'''
// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

class DiningPhilosophers() {
  private val forks = Array.fill(5)(new Object)

  def wantsToEat(
    philosopher: Int,
    pickLeftFork: Runnable,
    pickRightFork: Runnable,
    eat: Runnable,
    putLeftFork: Runnable,
    putRightFork: Runnable
  ): Unit = {
    val left = philosopher
    val right = (philosopher + 1) % 5
    val (first, second) = if (philosopher % 2 == 0) (left, right) else (right, left)
    forks(first).synchronized {
      forks(second).synchronized {
        pickLeftFork.run()
        pickRightFork.run()
        eat.run()
        putLeftFork.run()
        putRightFork.run()
      }
    }
  }
}
'''

S["1227_airplane_seat_assignment_probability"] = r'''
// LeetCode 1227 - Airplane Seat Assignment Probability
// https://leetcode.com/problems/airplane-seat-assignment-probability/

object Solution {
  def nthPersonGetsNthSeat(n: Int): Double = if (n == 1) 1.0 else 0.5
}
'''

S["1228_missing_number_in_arithmetic_progression"] = r'''
// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

object Solution {
  def missingNumber(arr: Array[Int]): Int = {
    val difference = (arr.last - arr.head) / arr.length
    for (i <- 1 until arr.length) {
      val expected = arr(0) + i * difference
      if (arr(i) != expected) return expected
    }
    arr(0)
  }
}
'''

S["1229_meeting_scheduler"] = r'''
// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

object Solution {
  def minAvailableDuration(slots1: Array[Array[Int]], slots2: Array[Array[Int]], duration: Int): List[Int] = {
    val a = slots1.sortBy(_(0))
    val b = slots2.sortBy(_(0))
    var i = 0
    var j = 0
    while (i < a.length && j < b.length) {
      val start = math.max(a(i)(0), b(j)(0))
      val end = math.min(a(i)(1), b(j)(1))
      if (end - start >= duration) return List(start, start + duration)
      if (a(i)(1) < b(j)(1)) i += 1 else j += 1
    }
    List.empty
  }
}
'''

S["1230_toss_strange_coins"] = r'''
// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

object Solution {
  def probabilityOfHeads(prob: Array[Double], target: Int): Double = {
    val dp = Array.fill(target + 1)(0.0)
    dp(0) = 1.0
    for (p <- prob) {
      for (heads <- target to 0 by -1) {
        dp(heads) = dp(heads) * (1 - p) + (if (heads > 0) dp(heads - 1) * p else 0.0)
      }
    }
    dp(target)
  }
}
'''

S["1231_divide_chocolate"] = r'''
// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

object Solution {
  def maximizeSweetness(sweetness: Array[Int], k: Int): Int = {
    var lo = 1
    var hi = sweetness.sum / (k + 1)
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      var pieces = 0
      var current = 0
      for (value <- sweetness) {
        current += value
        if (current >= mid) {
          pieces += 1
          current = 0
        }
      }
      if (pieces >= k + 1) lo = mid + 1 else hi = mid - 1
    }
    hi
  }
}
'''

S["1232_check_if_it_is_a_straight_line"] = r'''
// LeetCode 1232 - Check If It Is a Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

object Solution {
  def checkStraightLine(coordinates: Array[Array[Int]]): Boolean = {
    val x0 = coordinates(0)(0)
    val y0 = coordinates(0)(1)
    val dx = coordinates(1)(0) - x0
    val dy = coordinates(1)(1) - y0
    coordinates.drop(2).forall { p =>
      (p(0) - x0).toLong * dy == (p(1) - y0).toLong * dx
    }
  }
}
'''

S["1233_remove_sub_folders_from_the_filesystem"] = r'''
// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

object Solution {
  def removeSubfolders(folder: Array[String]): List[String] = {
    val answer = scala.collection.mutable.ListBuffer.empty[String]
    for (path <- folder.sorted) {
      if (answer.isEmpty || !path.startsWith(answer.last + "/")) answer += path
    }
    answer.toList
  }
}
'''

S["1234_replace_the_substring_for_balanced_string"] = r'''
// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

object Solution {
  def balancedString(s: String): Int = {
    val count = scala.collection.mutable.Map('Q' -> 0, 'W' -> 0, 'E' -> 0, 'R' -> 0)
    for (ch <- s) count(ch) += 1
    val limit = s.length / 4
    val n = s.length
    var left = 0
    var answer = n
    for (right <- s.indices) {
      count(s(right)) -= 1
      while (left < n && "QWER".forall(c => count(c) <= limit)) {
        answer = math.min(answer, right - left + 1)
        count(s(left)) += 1
        left += 1
      }
    }
    answer
  }
}
'''

S["1235_maximum_profit_in_job_scheduling"] = r'''
// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

object Solution {
  def jobScheduling(startTime: Array[Int], endTime: Array[Int], profit: Array[Int]): Int = {
    val jobs = endTime.indices.map(i => (endTime(i), startTime(i), profit(i))).sortBy(_._1)
    val ends = scala.collection.mutable.ArrayBuffer(0)
    val dp = scala.collection.mutable.ArrayBuffer(0)
    for ((end, start, gain) <- jobs) {
      var lo = 0
      var hi = ends.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (ends(mid) <= start) lo = mid + 1 else hi = mid
      }
      val i = lo - 1
      ends += end
      dp += math.max(dp.last, dp(i) + gain)
    }
    dp.last
  }
}
'''

S["1236_web_crawler"] = r'''
// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

trait HtmlParser {
  def getUrls(url: String): List[String]
}

object Solution {
  def crawl(startUrl: String, htmlParser: HtmlParser): List[String] = {
    def host(url: String): String = {
      val without = url.stripPrefix("http://")
      without.takeWhile(_ != '/')
    }
    val h = host(startUrl)
    val seen = scala.collection.mutable.Set(startUrl)
    val stack = scala.collection.mutable.Stack(startUrl)
    while (stack.nonEmpty) {
      for (url <- htmlParser.getUrls(stack.pop()) if host(url) == h && !seen.contains(url)) {
        seen += url
        stack.push(url)
      }
    }
    seen.toList.sorted
  }
}
'''

S["1237_find_positive_integer_solution_for_a_given_equation"] = r'''
// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

trait CustomFunction {
  def f(x: Int, y: Int): Int
}

object Solution {
  def findSolution(customfunction: CustomFunction, z: Int): List[List[Int]] = {
    val answer = scala.collection.mutable.ListBuffer.empty[List[Int]]
    var x = 1
    var y = 1000
    while (x <= 1000 && y >= 1) {
      val value = customfunction.f(x, y)
      if (value == z) {
        answer += List(x, y)
        x += 1
        y -= 1
      } else if (value < z) x += 1
      else y -= 1
    }
    answer.toList
  }
}
'''

S["1238_circular_permutation_in_binary_representation"] = r'''
// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

object Solution {
  def circularPermutation(n: Int, start: Int): List[Int] =
    (0 until (1 << n)).map(i => start ^ i ^ (i >> 1)).toList
}
'''

S["1239_maximum_length_of_a_concatenated_string_with_unique_characters"] = r'''
// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

object Solution {
  def maxLength(arr: List[String]): Int = {
    var masks = List((0, 0))
    for (word <- arr) {
      var mask = 0
      var ok = true
      for (ch <- word) {
        val bit = 1 << (ch - 'a')
        if ((mask & bit) != 0) ok = false
        mask |= bit
      }
      if (ok && Integer.bitCount(mask) == word.length) {
        masks = masks ++ masks.collect { case (used, length) if (used & mask) == 0 => (used | mask, length + word.length) }
      }
    }
    masks.map(_._2).max
  }
}
'''

S["1240_tiling_a_rectangle_with_the_fewest_squares"] = r'''
// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

object Solution {
  def tilingRectangle(n: Int, m: Int): Int = {
    var nn = n
    var mm = m
    if (nn > mm) { val t = nn; nn = mm; mm = t }
    val heights = Array.fill(mm)(0)
    var best = nn * mm
    def search(used: Int): Unit = {
      if (used >= best) return
      val low = heights.min
      if (low == nn) {
        best = used
        return
      }
      val left = heights.indexOf(low)
      var right = left
      while (right < mm && heights(right) == low) right += 1
      val maxSize = math.min(nn - low, right - left)
      for (size <- maxSize to 1 by -1) {
        for (i <- left until left + size) heights(i) = low + size
        search(used + 1)
        for (i <- left until left + size) heights(i) = low
      }
    }
    search(0)
    best
  }
}
'''


def main() -> None:
    for folder, code in S.items():
        write(folder, code)
    print(f"done {len(S)}")


if __name__ == "__main__":
    main()
