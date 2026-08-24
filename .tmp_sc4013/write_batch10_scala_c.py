#!/usr/bin/env python3
"""Write Scala Solution.scala files for batch_10 problems 2696-2726."""
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["2696_minimum_string_length_after_removing_substrings"] = """// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

object Solution {
  def minLength(s: String): Int = {
    val st = new StringBuilder
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i)
      val len = st.length
      if (len > 0 && ((st.charAt(len - 1) == 'A' && c == 'B') || (st.charAt(len - 1) == 'C' && c == 'D')))
        st.setLength(len - 1)
      else st.append(c)
      i += 1
    }
    st.length
  }
}
"""

FILES["2697_lexicographically_smallest_palindrome"] = """// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

object Solution {
  def makeSmallestPalindrome(s: String): String = {
    val arr = s.toCharArray
    val n = arr.length
    var i = 0
    while (i < n / 2) {
      val c = if (arr(i) < arr(n - 1 - i)) arr(i) else arr(n - 1 - i)
      arr(i) = c
      arr(n - 1 - i) = c
      i += 1
    }
    new String(arr)
  }
}
"""

FILES["2698_find_the_punishment_number_of_an_integer"] = """// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

object Solution {
  def punishmentNumber(n: Int): Int = {
    var ans = 0
    var i = 1
    while (i <= n) {
      val sq = i * i
      if (can(sq, i)) ans += sq
      i += 1
    }
    ans
  }

  private def can(sq: Int, target: Int): Boolean = {
    val s = sq.toString
    dfs(s, 0, 0, target)
  }

  private def dfs(s: String, i: Int, sum: Int, target: Int): Boolean = {
    val m = s.length
    if (i == m) return sum == target
    var cur = 0
    var j = i
    while (j < m) {
      cur = cur * 10 + (s.charAt(j) - '0')
      if (sum + cur > target) return false
      if (dfs(s, j + 1, sum + cur, target)) return true
      j += 1
    }
    false
  }
}
"""

FILES["2699_modify_graph_edge_weights"] = """// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/

import scala.collection.mutable

object Solution {
  private val INF = 2000000000

  def modifiedGraphEdges(
    n: Int,
    edges: Array[Array[Int]],
    source: Int,
    destination: Int,
    target: Int
  ): Array[Array[Int]] = {
    var d = dijkstra(n, edges, source, ignoreNeg = true)
    if (d(destination) < target) return Array.empty[Array[Int]]
    var matched = d(destination) == target
    var i = 0
    while (i < edges.length) {
      if (edges(i)(2) == -1) {
        if (matched) {
          edges(i)(2) = INF
        } else {
          edges(i)(2) = 1
          d = dijkstra(n, edges, source, ignoreNeg = false)
          if (d(destination) <= target) {
            edges(i)(2) += target - d(destination)
            matched = true
          }
        }
      }
      i += 1
    }
    d = dijkstra(n, edges, source, ignoreNeg = false)
    if (d(destination) != target) Array.empty[Array[Int]] else edges
  }

  private def dijkstra(n: Int, edges: Array[Array[Int]], source: Int, ignoreNeg: Boolean): Array[Int] = {
    val dist = Array.fill(n)(INF)
    dist(source) = 0
    val pq = mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](_._2).reverse)
    pq.enqueue((source, 0))
    while (pq.nonEmpty) {
      val (u, d) = pq.dequeue()
      if (d == dist(u)) {
        var i = 0
        while (i < edges.length) {
          val e = edges(i)
          val a = e(0)
          val b = e(1)
          var w = e(2)
          if (a == u || b == u) {
            val to = if (a == u) b else a
            var skip = false
            if (w == -1) {
              if (ignoreNeg) skip = true
              else w = 1
            }
            if (!skip && d + w < dist(to)) {
              dist(to) = d + w
              pq.enqueue((to, dist(to)))
            }
          }
          i += 1
        }
      }
    }
    dist
  }
}
"""

FILES["2700_differences_between_two_objects"] = """// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/

object Solution {
  def objDiff(
    obj1: scala.collection.mutable.TreeMap[String, Int],
    obj2: scala.collection.mutable.TreeMap[String, Int]
  ): scala.collection.mutable.TreeMap[String, Array[Int]] = {
    val diff = scala.collection.mutable.TreeMap.empty[String, Array[Int]]
    obj1.foreach { case (k, v) =>
      obj2.get(k) match {
        case Some(v2) if v2 != v => diff(k) = Array(v, v2)
        case _ =>
      }
    }
    diff
  }
}
"""

FILES["2702_minimum_operations_to_make_numbers_non_positive"] = """// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

object Solution {
  def minOperations(nums: Array[Int], x: Int, y: Int): Int = {
    var lo = 0
    var hi = 0
    var i = 0
    while (i < nums.length) {
      val v = nums(i)
      hi = math.max(hi, (v + y - 1) / y)
      hi = math.max(hi, (v + x - 1) / x)
      i += 1
    }
    hi += nums.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(nums, x, y, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(nums: Array[Int], x: Int, y: Int, ops: Int): Boolean = {
    var extra = 0L
    var i = 0
    while (i < nums.length) {
      val remain = nums(i).toLong - ops.toLong * y
      if (remain > 0) extra += (remain + (x - y) - 1) / (x - y)
      i += 1
    }
    extra <= ops
  }
}
"""

FILES["2703_return_length_of_arguments_passed"] = """// LeetCode 2703 - Return Length of Arguments Passed
// https://leetcode.com/problems/return-length-of-arguments-passed/

object Solution {
  def argumentsLength(args: Array[Int]): Int = args.length
}
"""

FILES["2704_to_be_or_not_to_be"] = """// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

class Expect(private val value: Int) {
  def toBe(other: Int): Boolean = {
    if (value == other) true
    else throw new RuntimeException("Not Equal")
  }

  def notToBe(other: Int): Boolean = {
    if (value != other) true
    else throw new RuntimeException("Equal")
  }
}

object Solution {
  def expect(`val`: Int): Expect = new Expect(`val`)
}
"""

FILES["2705_compact_object"] = """// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/

object Solution {
  def compactObject(obj: Array[Int]): Array[Int] = {
    val out = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < obj.length) {
      if (obj(i) != 0) out += obj(i)
      i += 1
    }
    out.toArray
  }
}
"""

FILES["2706_buy_two_chocolates"] = """// LeetCode 2706 - Buy Two Chocolates
// https://leetcode.com/problems/buy-two-chocolates/

object Solution {
  def buyChoco(prices: Array[Int], money: Int): Int = {
    scala.util.Sorting.quickSort(prices)
    val cost = prices(0) + prices(1)
    if (cost <= money) money - cost else money
  }
}
"""

FILES["2707_extra_characters_in_a_string"] = """// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/

object Solution {
  def minExtraChar(s: String, dictionary: Array[String]): Int = {
    val dict = dictionary.toSet
    val n = s.length
    val dp = Array.fill(n + 1)(n)
    dp(0) = 0
    var i = 0
    while (i < n) {
      dp(i + 1) = math.min(dp(i + 1), dp(i) + 1)
      var j = i + 1
      while (j <= n) {
        if (dict.contains(s.substring(i, j)))
          dp(j) = math.min(dp(j), dp(i))
        j += 1
      }
      i += 1
    }
    dp(n)
  }
}
"""

FILES["2708_maximum_strength_of_a_group"] = """// LeetCode 2708 - Maximum Strength of a Group
// https://leetcode.com/problems/maximum-strength-of-a-group/

object Solution {
  def maxStrength(nums: Array[Int]): Long = {
    scala.util.Sorting.quickSort(nums)
    val n = nums.length
    if (n == 1) return nums(0).toLong
    var prod = 1L
    var used = false
    var i = 0
    while (i + 1 < n && nums(i) < 0 && nums(i + 1) < 0) {
      prod *= nums(i).toLong * nums(i + 1)
      used = true
      i += 2
    }
    val negLeft = i < n && nums(i) < 0
    while (i < n) {
      if (nums(i) > 0) {
        prod *= nums(i)
        used = true
      }
      i += 1
    }
    if (!used) {
      if (negLeft) {
        var j = 0
        while (j < n) {
          if (nums(j) == 0) return 0
          j += 1
        }
        return nums(n - 1).toLong
      }
      return 0
    }
    prod
  }
}
"""

FILES["2709_greatest_common_divisor_traversal"] = """// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

object Solution {
  def canTraverseAllPairs(nums: Array[Int]): Boolean = {
    val n = nums.length
    if (n == 1) return true
    var mx = nums(0)
    var i = 0
    while (i < n) {
      if (nums(i) > mx) mx = nums(i)
      i += 1
    }
    val parent = Array.tabulate(mx + 1)(identity)
    val has = new Array[Boolean](mx + 1)
    i = 0
    while (i < n) {
      if (nums(i) == 1) return false
      has(nums(i)) = true
      i += 1
    }

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
      if (ra != rb) parent(ra) = rb
    }

    val sieve = new Array[Int](mx + 1)
    i = 2
    while (i <= mx) {
      if (sieve(i) == 0) {
        var j = i
        while (j <= mx) {
          if (sieve(j) == 0) sieve(j) = i
          if (has(j)) unite(i, j)
          j += i
        }
      }
      i += 1
    }
    val root = find(nums(0))
    i = 0
    while (i < n) {
      if (find(nums(i)) != root) return false
      i += 1
    }
    true
  }
}
"""

FILES["2710_remove_trailing_zeros_from_a_string"] = """// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

object Solution {
  def removeTrailingZeros(num: String): String = {
    var end = num.length
    while (end > 0 && num.charAt(end - 1) == '0') end -= 1
    num.substring(0, end)
  }
}
"""

FILES["2711_difference_of_number_of_distinct_values_on_diagonals"] = """// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

object Solution {
  def differenceOfDistinctValues(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val ans = Array.ofDim[Int](m, n)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val top = scala.collection.mutable.HashSet.empty[Int]
        val bot = scala.collection.mutable.HashSet.empty[Int]
        var r = i - 1
        var c = j - 1
        while (r >= 0 && c >= 0) {
          top += grid(r)(c)
          r -= 1
          c -= 1
        }
        r = i + 1
        c = j + 1
        while (r < m && c < n) {
          bot += grid(r)(c)
          r += 1
          c += 1
        }
        ans(i)(j) = math.abs(top.size - bot.size)
        j += 1
      }
      i += 1
    }
    ans
  }
}
"""

FILES["2712_minimum_cost_to_make_all_characters_equal"] = """// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

object Solution {
  def minimumCost(s: String): Long = {
    val n = s.length
    var ans = 0L
    var i = 1
    while (i < n) {
      if (s.charAt(i) != s.charAt(i - 1)) ans += math.min(i, n - i)
      i += 1
    }
    ans
  }
}
"""

FILES["2713_maximum_strictly_increasing_cells_in_a_matrix"] = """// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

object Solution {
  def maxIncreasingCells(mat: Array[Array[Int]]): Int = {
    val m = mat.length
    val n = mat(0).length
    val cells = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        cells += Array(mat(i)(j), i, j)
        j += 1
      }
      i += 1
    }
    val sorted = cells.sortBy(_(0))
    val rowMax = new Array[Int](m)
    val colMax = new Array[Int](n)
    val dp = Array.ofDim[Int](m, n)
    var ans = 0
    i = 0
    while (i < sorted.length) {
      var j = i
      while (j < sorted.length && sorted(j)(0) == sorted(i)(0)) j += 1
      val buf = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
      var k = i
      while (k < j) {
        val r = sorted(k)(1)
        val c = sorted(k)(2)
        val best = math.max(rowMax(r), colMax(c))
        dp(r)(c) = best + 1
        ans = math.max(ans, dp(r)(c))
        buf += Array(r, c, dp(r)(c))
        k += 1
      }
      buf.foreach { b =>
        rowMax(b(0)) = math.max(rowMax(b(0)), b(2))
        colMax(b(1)) = math.max(colMax(b(1)), b(2))
      }
      i = j
    }
    ans
  }
}
"""

FILES["2714_find_shortest_path_with_k_hops"] = """// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/

import scala.collection.mutable

object Solution {
  def shortestPathWithHops(n: Int, edges: Array[Array[Int]], s: Int, d: Int, k: Int): Int = {
    val g = Array.fill(n)(mutable.ArrayBuffer.empty[Array[Int]])
    var i = 0
    while (i < edges.length) {
      val e = edges(i)
      g(e(0)) += Array(e(1), e(2))
      g(e(1)) += Array(e(0), e(2))
      i += 1
    }
    val dist = Array.fill(n, k + 1)(Int.MaxValue / 4)
    dist(s)(0) = 0
    val pq = mutable.PriorityQueue.empty[(Int, Int, Int)](Ordering.by[(Int, Int, Int), Int](_._3).reverse)
    pq.enqueue((s, 0, 0))
    while (pq.nonEmpty) {
      val (u, hops, cd) = pq.dequeue()
      if (u == d) return cd
      if (cd <= dist(u)(hops)) {
        g(u).foreach { e =>
          val to = e(0)
          val w = e(1)
          if (cd + w < dist(to)(hops)) {
            dist(to)(hops) = cd + w
            pq.enqueue((to, hops, dist(to)(hops)))
          }
          if (hops < k && cd < dist(to)(hops + 1)) {
            dist(to)(hops + 1) = cd
            pq.enqueue((to, hops + 1, cd))
          }
        }
      }
    }
    -1
  }
}
"""

FILES["2715_timeout_cancellation"] = """// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

object Solution {
  def cancellable(fn: () => Int, t: Int): Array[Any] = {
    var cancelled = false
    val cancel: () => Unit = () => { cancelled = true }
    val result: () => Option[Int] = () => {
      if (cancelled) None
      else Some(fn())
    }
    Array(cancel, result)
  }
}
"""

FILES["2716_minimize_string_length"] = """// LeetCode 2716 - Minimize String Length
// https://leetcode.com/problems/minimize-string-length/

object Solution {
  def minimizedStringLength(s: String): Int = {
    val set = scala.collection.mutable.HashSet.empty[Char]
    var i = 0
    while (i < s.length) {
      set += s.charAt(i)
      i += 1
    }
    set.size
  }
}
"""

FILES["2717_semi_ordered_permutation"] = """// LeetCode 2717 - Semi-Ordered Permutation
// https://leetcode.com/problems/semi-ordered-permutation/

object Solution {
  def semiOrderedPermutation(nums: Array[Int]): Int = {
    val n = nums.length
    var p1 = 0
    var pn = 0
    var i = 0
    while (i < n) {
      if (nums(i) == 1) p1 = i
      if (nums(i) == n) pn = i
      i += 1
    }
    var ans = p1 + (n - 1 - pn)
    if (p1 > pn) ans -= 1
    ans
  }
}
"""

FILES["2718_sum_of_matrix_after_queries"] = """// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/

object Solution {
  def matrixSumQueries(n: Int, queries: Array[Array[Int]]): Long = {
    val rowDone = new Array[Boolean](n)
    val colDone = new Array[Boolean](n)
    var rowsLeft = n
    var colsLeft = n
    var ans = 0L
    var i = queries.length - 1
    while (i >= 0) {
      val typ = queries(i)(0)
      val idx = queries(i)(1)
      val v = queries(i)(2)
      if (typ == 0) {
        if (!rowDone(idx)) {
          ans += v.toLong * colsLeft
          rowDone(idx) = true
          rowsLeft -= 1
        }
      } else if (!colDone(idx)) {
        ans += v.toLong * rowsLeft
        colDone(idx) = true
        colsLeft -= 1
      }
      i -= 1
    }
    ans
  }
}
"""

FILES["2719_count_of_integers"] = """// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

object Solution {
  private val MOD = 1000000007
  private var minSum = 0
  private var maxSum = 0

  def count(num1: String, num2: String, min_sum: Int, max_sum: Int): Int = {
    minSum = min_sum
    maxSum = max_sum
    (dp(num2) - dp(dec(num1)) + MOD) % MOD
  }

  private def dec(s: String): String = {
    val arr = s.toCharArray
    var i = arr.length - 1
    while (i >= 0 && arr(i) == '0') {
      arr(i) = '9'
      i -= 1
    }
    if (i >= 0) arr(i) = (arr(i) - 1).toChar
    var j = 0
    while (j < arr.length - 1 && arr(j) == '0') j += 1
    new String(arr, j, arr.length - j)
  }

  private def dp(s: String): Int = {
    val memo = scala.collection.mutable.HashMap.empty[String, Int]
    dfs(s, 0, 0, tight = true, memo)
  }

  private def dfs(
    s: String,
    pos: Int,
    sum: Int,
    tight: Boolean,
    memo: scala.collection.mutable.HashMap[String, Int]
  ): Int = {
    if (sum > maxSum) return 0
    if (pos == s.length) return if (sum >= minSum) 1 else 0
    val key = pos + "," + sum + "," + (if (tight) 1 else 0)
    memo.get(key) match {
      case Some(cached) => cached
      case None =>
        val up = if (tight) s.charAt(pos) - '0' else 9
        var res = 0
        var d = 0
        while (d <= up) {
          res = (res + dfs(s, pos + 1, sum + d, tight && d == up, memo)) % MOD
          d += 1
        }
        memo(key) = res
        res
    }
  }
}
"""

FILES["2721_execute_asynchronous_functions_in_parallel"] = """// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

object Solution {
  def promiseAll(functions: List[() => Int]): Array[Int] = {
    val out = new Array[Int](functions.length)
    var i = 0
    while (i < functions.length) {
      out(i) = functions(i)()
      i += 1
    }
    out
  }
}
"""

FILES["2722_join_two_arrays_by_id"] = """// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/

object Solution {
  def join(
    arr1: List[scala.collection.mutable.TreeMap[String, Int]],
    arr2: List[scala.collection.mutable.TreeMap[String, Int]]
  ): List[scala.collection.mutable.TreeMap[String, Int]] = {
    val byId = scala.collection.mutable.TreeMap.empty[Int, scala.collection.mutable.TreeMap[String, Int]]
    merge(byId, arr1)
    merge(byId, arr2)
    byId.values.toList
  }

  private def merge(
    byId: scala.collection.mutable.TreeMap[Int, scala.collection.mutable.TreeMap[String, Int]],
    arr: List[scala.collection.mutable.TreeMap[String, Int]]
  ): Unit = {
    arr.foreach { obj =>
      val id = obj("id")
      val dest = byId.getOrElseUpdate(id, scala.collection.mutable.TreeMap.empty[String, Int])
      dest ++= obj
    }
  }
}
"""

FILES["2723_add_two_promises"] = """// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

object Solution {
  def addTwoPromises(promise1: () => Int, promise2: () => Int): Int =
    promise1() + promise2()
}
"""

FILES["2724_sort_by"] = """// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

object Solution {
  def sortBy(arr: Array[Int], fn: Int => Double): Array[Int] = {
    arr.sortBy(fn)
  }
}
"""

FILES["2725_interval_cancellation"] = """// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

object Solution {
  def cancellable(fn: () => Int, t: Int, times: Int): Array[Any] = {
    var cancelled = false
    val results = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < times && !cancelled) {
      results += fn()
      i += 1
    }
    val cancel: () => Unit = () => { cancelled = true }
    Array(cancel, results.toArray)
  }
}
"""

FILES["2726_calculator_with_method_chaining"] = """// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/

class Calculator(private var value: Double) {
  def add(v: Double): Calculator = {
    value += v
    this
  }

  def subtract(v: Double): Calculator = {
    value -= v
    this
  }

  def multiply(v: Double): Calculator = {
    value *= v
    this
  }

  def divide(v: Double): Calculator = {
    if (v != 0) value /= v
    this
  }

  def power(v: Double): Calculator = {
    value = math.pow(value, v)
    this
  }

  def getResult(): Double = value
}

object Solution {
  def calculatorCreate(v: Double): Calculator = new Calculator(v)
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
