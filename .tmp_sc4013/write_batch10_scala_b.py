#!/usr/bin/env python3
"""Write Scala Solution.scala files for batch_10 problems 2657-2695."""
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["2657_find_the_prefix_common_array_of_two_arrays"] = """// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

object Solution {
  def findThePrefixCommonArray(A: Array[Int], B: Array[Int]): Array[Int] = {
    val n = A.length
    val seenA = new Array[Boolean](n + 1)
    val seenB = new Array[Boolean](n + 1)
    val ans = new Array[Int](n)
    var common = 0
    var i = 0
    while (i < n) {
      if (seenB(A(i))) common += 1
      seenA(A(i)) = true
      if (seenA(B(i))) common += 1
      seenB(B(i)) = true
      ans(i) = common
      i += 1
    }
    ans
  }
}
"""

FILES["2658_maximum_number_of_fish_in_a_grid"] = """// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

object Solution {
  def findMaxFish(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var best = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) > 0) best = math.max(best, dfs(grid, i, j))
        j += 1
      }
      i += 1
    }
    best
  }

  private def dfs(grid: Array[Array[Int]], r: Int, c: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    if (r < 0 || r >= m || c < 0 || c >= n || grid(r)(c) == 0) return 0
    val fish = grid(r)(c)
    grid(r)(c) = 0
    fish + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1)
  }
}
"""

FILES["2659_make_array_empty"] = """// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

object Solution {
  def countOperationsToEmptyArray(nums: Array[Int]): Long = {
    val n = nums.length
    val idx = Array.tabulate(n)(identity)
    val sorted = idx.sortBy(nums)
    var ans = n.toLong
    var i = 1
    while (i < n) {
      if (sorted(i) < sorted(i - 1)) ans += n - i
      i += 1
    }
    ans
  }
}
"""

FILES["2660_determine_the_winner_of_a_bowling_game"] = """// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

object Solution {
  def isWinner(player1: Array[Int], player2: Array[Int]): Int = {
    val a = score(player1)
    val b = score(player2)
    if (a > b) 1
    else if (b > a) 2
    else 0
  }

  private def score(p: Array[Int]): Int = {
    var s = 0
    var i = 0
    while (i < p.length) {
      var mul = 1
      if ((i > 0 && p(i - 1) == 10) || (i > 1 && p(i - 2) == 10)) mul = 2
      s += mul * p(i)
      i += 1
    }
    s
  }
}
"""

FILES["2661_first_completely_painted_row_or_column"] = """// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

object Solution {
  def firstCompleteIndex(arr: Array[Int], mat: Array[Array[Int]]): Int = {
    val m = mat.length
    val n = mat(0).length
    val posR = new Array[Int](m * n + 1)
    val posC = new Array[Int](m * n + 1)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        posR(mat(i)(j)) = i
        posC(mat(i)(j)) = j
        j += 1
      }
      i += 1
    }
    val rowCnt = new Array[Int](m)
    val colCnt = new Array[Int](n)
    i = 0
    while (i < arr.length) {
      val r = posR(arr(i))
      val c = posC(arr(i))
      rowCnt(r) += 1
      colCnt(c) += 1
      if (rowCnt(r) == n || colCnt(c) == m) return i
      i += 1
    }
    -1
  }
}
"""

FILES["2662_minimum_cost_of_a_path_with_special_roads"] = """// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

import scala.collection.mutable

object Solution {
  def minimumCost(start: Array[Int], target: Array[Int], specialRoads: Array[Array[Int]]): Int = {
    val points = mutable.ArrayBuffer.empty[Array[Int]]
    points += start
    points += target
    var i = 0
    while (i < specialRoads.length) {
      val r = specialRoads(i)
      points += Array(r(0), r(1))
      points += Array(r(2), r(3))
      i += 1
    }
    val N = points.length
    val g = Array.fill(N)(mutable.ArrayBuffer.empty[Array[Int]])
    i = 0
    while (i < N) {
      var j = 0
      while (j < N) {
        if (i != j) g(i) += Array(j, man(points(i), points(j)))
        j += 1
      }
      i += 1
    }
    i = 0
    while (i < specialRoads.length) {
      val r = specialRoads(i)
      var u = -1
      var v = -1
      var k = 0
      while (k < N) {
        val p = points(k)
        if (p(0) == r(0) && p(1) == r(1)) u = k
        if (p(0) == r(2) && p(1) == r(3)) v = k
        k += 1
      }
      if (u >= 0 && v >= 0) g(u) += Array(v, r(4))
      i += 1
    }
    val dist = Array.fill(N)(Int.MaxValue / 4)
    dist(0) = 0
    val pq = mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](_._2).reverse)
    pq.enqueue((0, 0))
    while (pq.nonEmpty) {
      val (id, cost) = pq.dequeue()
      if (cost <= dist(id)) {
        g(id).foreach { e =>
          if (cost + e(1) < dist(e(0))) {
            dist(e(0)) = cost + e(1)
            pq.enqueue((e(0), dist(e(0))))
          }
        }
      }
    }
    dist(1)
  }

  private def man(a: Array[Int], b: Array[Int]): Int =
    math.abs(a(0) - b(0)) + math.abs(a(1) - b(1))
}
"""

FILES["2663_lexicographically_smallest_beautiful_string"] = """// LeetCode 2663 - Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

object Solution {
  def smallestBeautifulString(s: String, k: Int): String = {
    val n = s.length
    val b = s.toCharArray
    var i = n - 1
    while (i >= 0) {
      var c = (b(i) + 1).toChar
      while (c < ('a' + k).toChar) {
        if (!((i > 0 && c == b(i - 1)) || (i > 1 && c == b(i - 2)))) {
          b(i) = c
          var j = i + 1
          while (j < n) {
            var nc = 'a'
            var placed = false
            while (nc < ('a' + k).toChar && !placed) {
              if (!((j > 0 && nc == b(j - 1)) || (j > 1 && nc == b(j - 2)))) {
                b(j) = nc
                placed = true
              }
              nc = (nc + 1).toChar
            }
            j += 1
          }
          return new String(b)
        }
        c = (c + 1).toChar
      }
      i -= 1
    }
    ""
  }
}
"""

FILES["2664_the_knights_tour"] = """// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

object Solution {
  private val DIRS = Array(
    Array(1, 2), Array(1, -2), Array(-1, 2), Array(-1, -2),
    Array(2, 1), Array(2, -1), Array(-2, 1), Array(-2, -1)
  )

  def tourOfKnight(m: Int, n: Int, r: Int, c: Int): Array[Array[Int]] = {
    val ans = Array.fill(m, n)(-1)
    dfs(ans, m, n, r, c, 0)
    ans
  }

  private def dfs(ans: Array[Array[Int]], m: Int, n: Int, x: Int, y: Int, step: Int): Boolean = {
    ans(x)(y) = step
    if (step == m * n - 1) return true
    var i = 0
    while (i < DIRS.length) {
      val nx = x + DIRS(i)(0)
      val ny = y + DIRS(i)(1)
      if (nx >= 0 && nx < m && ny >= 0 && ny < n && ans(nx)(ny) == -1)
        if (dfs(ans, m, n, nx, ny, step + 1)) return true
      i += 1
    }
    ans(x)(y) = -1
    false
  }
}
"""

FILES["2665_counter_ii"] = """// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

class CounterII(_init: Int) {
  private val init = _init
  private var cur = _init

  def increment(): Int = {
    cur += 1
    cur
  }

  def decrement(): Int = {
    cur -= 1
    cur
  }

  def reset(): Int = {
    cur = init
    cur
  }
}

object Solution {
  def createCounter(init: Int): CounterII = new CounterII(init)
}
"""

FILES["2666_allow_one_function_call"] = """// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

object Solution {
  def once(fn: Int => Int): Int => Option[Int] = {
    var called = false
    var res = 0
    (arg: Int) => {
      if (called) None
      else {
        called = true
        res = fn(arg)
        Some(res)
      }
    }
  }
}
"""

FILES["2667_create_hello_world_function"] = """// LeetCode 2667 - Create Hello World Function
// https://leetcode.com/problems/create-hello-world-function/

object Solution {
  def createHelloWorld(): () => String = {
    () => "Hello World"
  }
}
"""

FILES["2670_find_the_distinct_difference_array"] = """// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

object Solution {
  def distinctDifferenceArray(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val suf = new Array[Int](n + 1)
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var i = n - 1
    while (i >= 0) {
      seen += nums(i)
      suf(i) = seen.size
      i -= 1
    }
    seen.clear()
    val ans = new Array[Int](n)
    i = 0
    while (i < n) {
      seen += nums(i)
      ans(i) = seen.size - suf(i + 1)
      i += 1
    }
    ans
  }
}
"""

FILES["2671_frequency_tracker"] = """// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

class FrequencyTracker() {
  private val freq = scala.collection.mutable.HashMap.empty[Int, Int]
  private val count = scala.collection.mutable.HashMap.empty[Int, Int]

  def add(number: Int): Unit = {
    val old = freq.getOrElse(number, 0)
    if (old > 0) count(old) = count.getOrElse(old, 0) - 1
    freq(number) = old + 1
    count(old + 1) = count.getOrElse(old + 1, 0) + 1
  }

  def deleteOne(number: Int): Unit = {
    val old = freq.getOrElse(number, 0)
    if (old == 0) return
    count(old) = count.getOrElse(old, 0) - 1
    freq(number) = old - 1
    if (old - 1 > 0) count(old - 1) = count.getOrElse(old - 1, 0) + 1
  }

  def hasFrequency(frequency: Int): Boolean =
    count.getOrElse(frequency, 0) > 0
}
"""

FILES["2672_number_of_adjacent_elements_with_the_same_color"] = """// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

object Solution {
  def colorTheArray(n: Int, queries: Array[Array[Int]]): Array[Int] = {
    val colors = new Array[Int](n)
    val ans = new Array[Int](queries.length)
    var same = 0
    var i = 0
    while (i < queries.length) {
      val idx = queries(i)(0)
      val color = queries(i)(1)
      if (colors(idx) != 0) {
        if (idx > 0 && colors(idx) == colors(idx - 1)) same -= 1
        if (idx + 1 < n && colors(idx) == colors(idx + 1)) same -= 1
      }
      colors(idx) = color
      if (idx > 0 && colors(idx) == colors(idx - 1)) same += 1
      if (idx + 1 < n && colors(idx) == colors(idx + 1)) same += 1
      ans(i) = same
      i += 1
    }
    ans
  }
}
"""

FILES["2673_make_costs_of_paths_equal_in_a_binary_tree"] = """// LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

object Solution {
  def minIncrements(n: Int, cost: Array[Int]): Int = {
    var ans = 0
    var i = n / 2 - 1
    while (i >= 0) {
      val l = 2 * i + 1
      val r = 2 * i + 2
      ans += math.abs(cost(l) - cost(r))
      cost(i) += math.max(cost(l), cost(r))
      i -= 1
    }
    ans
  }
}
"""

FILES["2674_split_a_circular_linked_list"] = """// LeetCode 2674 - Split a Circular Linked List
// https://leetcode.com/problems/split-a-circular-linked-list/

class ListNode(var x: Int = 0) { var next: ListNode = null }

object Solution {
  def splitCircularLinkedList(list: ListNode): Array[ListNode] = {
    if (list == null) return Array(null, null)
    var slow = list
    var fast = list
    while (fast.next != list && fast.next.next != list) {
      slow = slow.next
      fast = fast.next.next
    }
    if (fast.next.next == list) fast = fast.next
    val head2 = slow.next
    slow.next = list
    fast.next = head2
    Array(list, head2)
  }
}
"""

FILES["2675_array_of_objects_to_matrix"] = """// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/

object Solution {
  def jsonToMatrix(arr: List[scala.collection.mutable.TreeMap[String, String]]): List[List[String]] = {
    val keys = scala.collection.mutable.TreeSet.empty[String]
    arr.foreach(obj => keys ++= obj.keySet)
    val mat = scala.collection.mutable.ArrayBuffer.empty[List[String]]
    mat += keys.toList
    arr.foreach { obj =>
      val row = scala.collection.mutable.ArrayBuffer.empty[String]
      keys.foreach(k => row += obj.getOrElse(k, ""))
      mat += row.toList
    }
    mat.toList
  }
}
"""

FILES["2676_throttle"] = """// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

object Solution {
  def throttle(fn: () => Unit, t: Int): () => Unit = {
    var last = System.nanoTime() - 24L * 3600 * 1000000000L
    () => {
      val now = System.nanoTime()
      if ((now - last) / 1000000L >= t) {
        last = now
        fn()
      }
    }
  }
}
"""

FILES["2677_chunk_array"] = """// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/

object Solution {
  def chunk(arr: Array[Int], size: Int): Array[Array[Int]] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var i = 0
    while (i < arr.length) {
      val end = math.min(arr.length, i + size)
      ans += arr.slice(i, end)
      i += size
    }
    ans.toArray
  }
}
"""

FILES["2678_number_of_senior_citizens"] = """// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/

object Solution {
  def countSeniors(details: Array[String]): Int = {
    var ans = 0
    var i = 0
    while (i < details.length) {
      val d = details(i)
      val age = (d.charAt(11) - '0') * 10 + (d.charAt(12) - '0')
      if (age > 60) ans += 1
      i += 1
    }
    ans
  }
}
"""

FILES["2679_sum_in_a_matrix"] = """// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

object Solution {
  def matrixSum(nums: Array[Array[Int]]): Int = {
    var i = 0
    while (i < nums.length) {
      scala.util.Sorting.quickSort(nums(i))
      i += 1
    }
    var ans = 0
    val n = nums(0).length
    var j = 0
    while (j < n) {
      var mx = 0
      i = 0
      while (i < nums.length) {
        mx = math.max(mx, nums(i)(j))
        i += 1
      }
      ans += mx
      j += 1
    }
    ans
  }
}
"""

FILES["2680_maximum_or"] = """// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

object Solution {
  def maximumOr(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val pref = new Array[Long](n + 1)
    val suf = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) | (nums(i).toLong & 0xffffffffL)
      i += 1
    }
    i = n - 1
    while (i >= 0) {
      suf(i) = suf(i + 1) | (nums(i).toLong & 0xffffffffL)
      i -= 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      val cur = pref(i) | (nums(i).toLong << k) | suf(i + 1)
      if (cur > ans) ans = cur
      i += 1
    }
    ans
  }
}
"""

FILES["2681_power_of_heroes"] = """// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

object Solution {
  def sumOfPower(nums: Array[Int]): Int = {
    val MOD = 1000000007
    scala.util.Sorting.quickSort(nums)
    var ans = 0L
    var s = 0L
    var i = 0
    while (i < nums.length) {
      val x = nums(i).toLong
      ans = (ans + (s + x) % MOD * x % MOD * x) % MOD
      s = (s * 2 + x) % MOD
      i += 1
    }
    ans.toInt
  }
}
"""

FILES["2682_find_the_losers_of_the_circular_game"] = """// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

object Solution {
  def circularGameLosers(n: Int, k: Int): Array[Int] = {
    val seen = new Array[Boolean](n + 1)
    var cur = 1
    var step = 1
    while (!seen(cur)) {
      seen(cur) = true
      cur = (cur - 1 + step * k) % n + 1
      step += 1
    }
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 1
    while (i <= n) {
      if (!seen(i)) ans += i
      i += 1
    }
    ans.toArray
  }
}
"""

FILES["2683_neighboring_bitwise_xor"] = """// LeetCode 2683 - Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

object Solution {
  def doesValidArrayExist(derived: Array[Int]): Boolean = {
    var x = 0
    var i = 0
    while (i < derived.length) {
      x ^= derived(i)
      i += 1
    }
    x == 0
  }
}
"""

FILES["2684_maximum_number_of_moves_in_a_grid"] = """// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

object Solution {
  def maxMoves(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var dp = new Array[Int](m)
    var c = n - 2
    while (c >= 0) {
      val ndp = new Array[Int](m)
      var r = 0
      while (r < m) {
        var best = 0
        var dr = -1
        while (dr <= 1) {
          val nr = r + dr
          if (nr >= 0 && nr < m && grid(nr)(c + 1) > grid(r)(c))
            best = math.max(best, 1 + dp(nr))
          dr += 1
        }
        ndp(r) = best
        r += 1
      }
      dp = ndp
      c -= 1
    }
    var ans = 0
    var i = 0
    while (i < dp.length) {
      ans = math.max(ans, dp(i))
      i += 1
    }
    ans
  }
}
"""

FILES["2685_count_the_number_of_complete_components"] = """// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

import scala.collection.mutable

object Solution {
  def countCompleteComponents(n: Int, edges: Array[Array[Int]]): Int = {
    val g = Array.fill(n)(mutable.ArrayBuffer.empty[Int])
    var i = 0
    while (i < edges.length) {
      val e = edges(i)
      g(e(0)) += e(1)
      g(e(1)) += e(0)
      i += 1
    }
    val vis = new Array[Boolean](n)
    var ans = 0
    i = 0
    while (i < n) {
      if (!vis(i)) {
        val nodes = mutable.ArrayBuffer.empty[Int]
        dfs(g, vis, i, nodes)
        var ecount = 0
        nodes.foreach(u => ecount += g(u).length)
        ecount /= 2
        val sz = nodes.length
        if (ecount == sz * (sz - 1) / 2) ans += 1
      }
      i += 1
    }
    ans
  }

  private def dfs(
    g: Array[mutable.ArrayBuffer[Int]],
    vis: Array[Boolean],
    u: Int,
    nodes: mutable.ArrayBuffer[Int]
  ): Unit = {
    vis(u) = true
    nodes += u
    g(u).foreach { v =>
      if (!vis(v)) dfs(g, vis, v, nodes)
    }
  }
}
"""

FILES["2689_extract_kth_character_from_the_rope_tree"] = """// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

class RopeTreeNode(_len: Int = 0, _value: Char = '\\u0000') {
  var len: Int = _len
  var value: Char = _value
  var left: RopeTreeNode = null
  var right: RopeTreeNode = null
}

object Solution {
  def getKthCharacter(root: RopeTreeNode, k: Int): Char = dfs(root, k)

  private def dfs(node: RopeTreeNode, kk: Int): Char = {
    if (node.left == null && node.right == null) return node.value
    var leftLen = 0
    if (node.left != null) leftLen = if (node.left.len > 0) node.left.len else 1
    if (kk <= leftLen) dfs(node.left, kk)
    else dfs(node.right, kk - leftLen)
  }
}
"""

FILES["2690_infinite_method_object"] = """// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

object Solution {
  def createInfiniteObject(): String => String = {
    (_: String) => "Hello World"
  }
}
"""

FILES["2691_immutability_helper"] = """// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/

object Solution {
  def immutableHelper(
    obj: scala.collection.mutable.TreeMap[String, Int],
    mutators: List[scala.collection.mutable.TreeMap[String, Int] => Unit]
  ): List[scala.collection.mutable.TreeMap[String, Int]] = {
    val out = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.TreeMap[String, Int]]
    mutators.foreach { m =>
      val copy = scala.collection.mutable.TreeMap.empty[String, Int] ++ obj
      m(copy)
      out += copy
    }
    out.toList
  }
}
"""

FILES["2692_make_object_immutable"] = """// LeetCode 2692 - Make Object Immutable
// https://leetcode.com/problems/make-object-immutable/

object Solution {
  def makeImmutable(obj: scala.collection.mutable.TreeMap[String, Int]): scala.collection.mutable.TreeMap[String, Int] =
    scala.collection.mutable.TreeMap.empty[String, Int] ++ obj
}
"""

FILES["2693_call_function_with_custom_context"] = """// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

object Solution {
  def call(fn: (Int, Int) => Int, ctx: Int, arg: Int): Int = fn(ctx, arg)
}
"""

FILES["2694_event_emitter"] = """// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

import scala.collection.mutable

class EventEmitter() {
  private val handlers = mutable.HashMap.empty[String, mutable.ArrayBuffer[Array[Int] => Unit]]

  def subscribe(eventName: String, callback: Array[Int] => Unit): () => Unit = {
    val list = handlers.getOrElseUpdate(eventName, mutable.ArrayBuffer.empty[Array[Int] => Unit])
    list += callback
    var idx = list.length - 1
    () => {
      val v = handlers.get(eventName)
      if (v.isDefined && idx >= 0 && idx < v.get.length) {
        v.get.remove(idx)
        idx = -1
      }
    }
  }

  def emit(eventName: String, args: Array[Int]): Array[Int] = {
    val res = mutable.ArrayBuffer.empty[Int]
    handlers.get(eventName).foreach { list =>
      list.toList.foreach { cb =>
        cb(args)
        res += 0
      }
    }
    res.toArray
  }
}

object Solution {
  def createEmitter(): EventEmitter = new EventEmitter()
}
"""

FILES["2695_array_wrapper"] = """// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

class ArrayWrapper(private val nums: Array[Int]) {
  def valueOf(): Int = {
    var s = 0
    var i = 0
    while (i < nums.length) {
      s += nums(i)
      i += 1
    }
    s
  }

  override def toString: String = {
    val sb = new StringBuilder
    sb.append('[')
    var i = 0
    while (i < nums.length) {
      if (i > 0) sb.append(',')
      sb.append(nums(i))
      i += 1
    }
    sb.append(']')
    sb.toString
  }
}

object Solution {
  def arrayWrapperCreate(nums: Array[Int]): ArrayWrapper = new ArrayWrapper(nums)
}
"""

def main():
    written = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "Solution.scala"
        if not path.parent.exists():
            print(f"MISSING FOLDER {folder}")
            continue
        path.write_text(content, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {folder}")
    print(f"written={written}")

if __name__ == "__main__":
    main()
