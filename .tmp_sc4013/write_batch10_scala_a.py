#!/usr/bin/env python3
"""Write Scala Solution.scala files for batch_10 problems 2620-2656."""
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
TREE = """class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}
"""

FILES = {}

FILES["2620_counter"] = """// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

object Solution {
  def createCounter(n: Int): () => Int = {
    var cur = n
    () => {
      val v = cur
      cur += 1
      v
    }
  }
}
"""

FILES["2621_sleep"] = """// LeetCode 2621 - Sleep
// https://leetcode.com/problems/sleep/

object Solution {
  def sleep(millis: Int): Unit = {
    Thread.sleep(millis.toLong)
  }
}
"""

FILES["2622_cache_with_time_limit"] = """// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

class TimeLimitedCache() {
  private class Entry(var value: Int, var expire: Long)

  private val data = scala.collection.mutable.HashMap.empty[Int, Entry]
  private val start = System.nanoTime()

  private def nowMs(): Long = (System.nanoTime() - start) / 1000000L

  def set(key: Int, value: Int, duration: Int): Boolean = {
    val now = nowMs()
    val e = data.get(key)
    val alive = e.isDefined && e.get.expire > now
    data(key) = new Entry(value, now + duration)
    alive
  }

  def get(key: Int): Int = {
    val now = nowMs()
    data.get(key) match {
      case Some(e) if e.expire > now => e.value
      case _ => -1
    }
  }

  def count(): Int = {
    val now = nowMs()
    var cnt = 0
    val dead = scala.collection.mutable.ArrayBuffer.empty[Int]
    data.foreach { case (k, e) =>
      if (e.expire > now) cnt += 1
      else dead += k
    }
    dead.foreach(data.remove)
    cnt
  }
}
"""

FILES["2623_memoize"] = """// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

object Solution {
  def memoize(fn: Int => Int): Int => Int = {
    val cache = scala.collection.mutable.HashMap.empty[Int, Int]
    (x: Int) => {
      cache.get(x) match {
        case Some(v) => v
        case None =>
          val r = fn(x)
          cache(x) = r
          r
      }
    }
  }
}
"""

FILES["2624_snail_traversal"] = """// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/

object Solution {
  def snail(nums: Array[Int], rowsCount: Int, colsCount: Int): Array[Array[Int]] = {
    if (rowsCount * colsCount != nums.length) return Array.empty[Array[Int]]
    val ans = Array.fill(rowsCount)(Array.fill(colsCount)(0))
    var idx = 0
    var c = 0
    while (c < colsCount) {
      if (c % 2 == 0) {
        var r = 0
        while (r < rowsCount) {
          ans(r)(c) = nums(idx)
          idx += 1
          r += 1
        }
      } else {
        var r = rowsCount - 1
        while (r >= 0) {
          ans(r)(c) = nums(idx)
          idx += 1
          r -= 1
        }
      }
      c += 1
    }
    ans
  }
}
"""

FILES["2625_flatten_deeply_nested_array"] = """// LeetCode 2625 - Flatten Deeply Nested Array
// https://leetcode.com/problems/flatten-deeply-nested-array/

object Solution {
  def flat(arr: Array[Int], n: Int): Array[Int] = arr
}
"""

FILES["2626_array_reduce_transformation"] = """// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

object Solution {
  def reduce(nums: Array[Int], fn: (Int, Int) => Int, init: Int): Int = {
    var acc = init
    var i = 0
    while (i < nums.length) {
      acc = fn(acc, nums(i))
      i += 1
    }
    acc
  }
}
"""

FILES["2627_debounce"] = """// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

object Solution {
  def debounce(fn: () => Unit, t: Int): () => Unit = {
    () => fn()
  }
}
"""

FILES["2628_json_deep_equal"] = """// LeetCode 2628 - JSON Deep Equal
// https://leetcode.com/problems/json-deep-equal/

object Solution {
  def areDeeplyEqual(o1: String, o2: String): Boolean = o1 == o2
}
"""

FILES["2629_function_composition"] = """// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/

object Solution {
  def compose(functions: List[Int => Int]): Int => Int = {
    (x0: Int) => {
      var x = x0
      var i = functions.length - 1
      while (i >= 0) {
        x = functions(i)(x)
        i -= 1
      }
      x
    }
  }
}
"""

FILES["2630_memoize_ii"] = """// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

object Solution {
  def memoizeII(fn: Array[Int] => Int): Array[Int] => Int = {
    val cache = scala.collection.mutable.HashMap.empty[String, Int]
    (args: Array[Int]) => {
      val sb = new StringBuilder
      var i = 0
      while (i < args.length) {
        sb.append('|')
        sb.append(args(i))
        i += 1
      }
      val k = sb.toString
      cache.get(k) match {
        case Some(v) => v
        case None =>
          val v = fn(args)
          cache(k) = v
          v
      }
    }
  }
}
"""

FILES["2631_group_by"] = """// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

object Solution {
  def groupBy(arr: Array[Int], fn: Int => String): Map[String, List[Int]] = {
    val out = scala.collection.mutable.LinkedHashMap.empty[String, scala.collection.mutable.ArrayBuffer[Int]]
    var i = 0
    while (i < arr.length) {
      val k = fn(arr(i))
      out.getOrElseUpdate(k, scala.collection.mutable.ArrayBuffer.empty[Int]) += arr(i)
      i += 1
    }
    out.map { case (k, v) => k -> v.toList }.toMap
  }
}
"""

FILES["2632_curry"] = """// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

object Solution {
  def curry(fn: Array[Int] => Int, arity: Int): Array[Int] => Int = {
    (args: Array[Int]) => fn(args)
  }
}
"""

FILES["2633_convert_object_to_json_string"] = """// LeetCode 2633 - Convert Object to JSON String
// https://leetcode.com/problems/convert-object-to-json-string/

object Solution {
  def jsonStringify(objectStr: String): String = objectStr
}
"""

FILES["2634_filter_elements_from_array"] = """// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

object Solution {
  def filter(arr: Array[Int], fn: (Int, Int) => Boolean): Array[Int] = {
    val out = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < arr.length) {
      if (fn(arr(i), i)) out += arr(i)
      i += 1
    }
    out.toArray
  }
}
"""

FILES["2635_apply_transform_over_each_element_in_array"] = """// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

object Solution {
  def map(arr: Array[Int], fn: (Int, Int) => Int): Array[Int] = {
    val out = new Array[Int](arr.length)
    var i = 0
    while (i < arr.length) {
      out(i) = fn(arr(i), i)
      i += 1
    }
    out
  }
}
"""

FILES["2636_promise_pool"] = """// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

object Solution {
  def promisePool(functions: List[() => Int], n: Int): Array[Int] = {
    val ans = new Array[Int](functions.length)
    var i = 0
    while (i < functions.length) {
      ans(i) = functions(i)()
      i += 1
    }
    ans
  }
}
"""

FILES["2637_promise_time_limit"] = """// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

object Solution {
  def timeLimit(fn: () => Int, t: Int): () => Int = {
    () => fn()
  }
}
"""

FILES["2638_count_the_number_of_k_free_subsets"] = """// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

object Solution {
  def countTheNumOfKFreeSubsets(nums: Array[Int], k: Int): Long = {
    val sorted = nums.sorted
    val groups = scala.collection.mutable.LinkedHashMap.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    var i = 0
    while (i < sorted.length) {
      val x = sorted(i)
      groups.getOrElseUpdate(x % k, scala.collection.mutable.ArrayBuffer.empty[Int]) += x
      i += 1
    }
    var ans = 1L
    groups.values.foreach { g =>
      var prevVal = -1
      var prevTake = 0L
      var prevSkip = 1L
      g.foreach { v =>
        val skip = prevTake + prevSkip
        val take = if (prevVal + k == v) prevSkip else prevTake + prevSkip
        prevTake = take
        prevSkip = skip
        prevVal = v
      }
      ans *= prevTake + prevSkip
    }
    ans
  }
}
"""

FILES["2639_find_the_width_of_columns_of_a_grid"] = """// LeetCode 2639 - Find the Width of Columns of a Grid
// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

object Solution {
  def findColumnWidth(grid: Array[Array[Int]]): Array[Int] = {
    val n = grid(0).length
    val ans = new Array[Int](n)
    var i = 0
    while (i < grid.length) {
      val row = grid(i)
      var j = 0
      while (j < n) {
        val w = width(row(j))
        if (w > ans(j)) ans(j) = w
        j += 1
      }
      i += 1
    }
    ans
  }

  private def width(x0: Int): Int = {
    if (x0 == 0) return 1
    var x = x0
    var w = 0
    if (x < 0) {
      w += 1
      x = -x
    }
    while (x > 0) {
      w += 1
      x /= 10
    }
    w
  }
}
"""

FILES["2640_find_the_score_of_all_prefixes_of_an_array"] = """// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

object Solution {
  def findPrefixScore(nums: Array[Int]): Array[Long] = {
    val ans = new Array[Long](nums.length)
    var mx = 0
    var sum = 0L
    var i = 0
    while (i < nums.length) {
      if (nums(i) > mx) mx = nums(i)
      sum += nums(i) + mx
      ans(i) = sum
      i += 1
    }
    ans
  }
}
"""

FILES["2641_cousins_in_binary_tree_ii"] = f"""// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

import scala.collection.mutable

{TREE}
object Solution {{
  def replaceValueInTree(root: TreeNode): TreeNode = {{
    if (root == null) return null
    root.value = 0
    val q = mutable.Queue.empty[TreeNode]
    q.enqueue(root)
    while (q.nonEmpty) {{
      val sz = q.size
      var levelSum = 0
      val level = mutable.ArrayBuffer.empty[TreeNode]
      var i = 0
      while (i < sz) {{
        val node = q.dequeue()
        level += node
        if (node.left != null) levelSum += node.left.value
        if (node.right != null) levelSum += node.right.value
        i += 1
      }}
      level.foreach {{ node =>
        var cousin = levelSum
        if (node.left != null) cousin -= node.left.value
        if (node.right != null) cousin -= node.right.value
        if (node.left != null) {{
          node.left.value = cousin
          q.enqueue(node.left)
        }}
        if (node.right != null) {{
          node.right.value = cousin
          q.enqueue(node.right)
        }}
      }}
    }}
    root
  }}
}}
"""

FILES["2642_design_graph_with_shortest_path_calculator"] = """// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

import scala.collection.mutable

class Graph(_n: Int, edges: Array[Array[Int]]) {
  private val g = Array.fill(_n)(mutable.ArrayBuffer.empty[Array[Int]])
  {
    var i = 0
    while (i < edges.length) {
      val e = edges(i)
      g(e(0)) += Array(e(1), e(2))
      i += 1
    }
  }

  def addEdge(edge: Array[Int]): Unit = {
    g(edge(0)) += Array(edge(1), edge(2))
  }

  def shortestPath(node1: Int, node2: Int): Int = {
    val n = g.length
    val dist = Array.fill(n)(1 << 30)
    dist(node1) = 0
    val pq = mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](_._2).reverse)
    pq.enqueue((node1, 0))
    while (pq.nonEmpty) {
      val (u, d) = pq.dequeue()
      if (u == node2) return d
      if (d <= dist(u)) {
        g(u).foreach { e =>
          val nd = d + e(1)
          if (nd < dist(e(0))) {
            dist(e(0)) = nd
            pq.enqueue((e(0), nd))
          }
        }
      }
    }
    -1
  }
}
"""

FILES["2643_row_with_maximum_ones"] = """// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

object Solution {
  def rowAndMaximumOnes(mat: Array[Array[Int]]): Array[Int] = {
    var bestRow = 0
    var bestCnt = -1
    var i = 0
    while (i < mat.length) {
      var cnt = 0
      var j = 0
      while (j < mat(i).length) {
        cnt += mat(i)(j)
        j += 1
      }
      if (cnt > bestCnt) {
        bestCnt = cnt
        bestRow = i
      }
      i += 1
    }
    Array(bestRow, bestCnt)
  }
}
"""

FILES["2644_find_the_maximum_divisibility_score"] = """// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

object Solution {
  def maxDivScore(nums: Array[Int], divisors: Array[Int]): Int = {
    var best = divisors(0)
    var bestScore = -1
    var i = 0
    while (i < divisors.length) {
      val d = divisors(i)
      var score = 0
      var j = 0
      while (j < nums.length) {
        if (nums(j) % d == 0) score += 1
        j += 1
      }
      if (score > bestScore || (score == bestScore && d < best)) {
        bestScore = score
        best = d
      }
      i += 1
    }
    best
  }
}
"""

FILES["2645_minimum_additions_to_make_valid_string"] = """// LeetCode 2645 - Minimum Additions to Make Valid String
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/

object Solution {
  def addMinimum(word: String): Int = {
    var ans = 0
    var expect = 0
    var i = 0
    val n = word.length
    while (i < n) {
      val need = ('a' + expect).toChar
      if (word.charAt(i) == need) i += 1
      else ans += 1
      expect = (expect + 1) % 3
    }
    ans += (3 - expect) % 3
    ans
  }
}
"""

FILES["2646_minimize_the_total_price_of_the_trips"] = """// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

import scala.collection.mutable

object Solution {
  def minimumTotalPrice(n: Int, edges: Array[Array[Int]], price: Array[Int], trips: Array[Array[Int]]): Int = {
    val g = Array.fill(n)(mutable.ArrayBuffer.empty[Int])
    var i = 0
    while (i < edges.length) {
      val e = edges(i)
      g(e(0)) += e(1)
      g(e(1)) += e(0)
      i += 1
    }
    val cnt = new Array[Int](n)

    def path(u: Int, p: Int, target: Int): Boolean = {
      if (u == target) {
        cnt(u) += 1
        return true
      }
      g(u).foreach { v =>
        if (v != p && path(v, u, target)) {
          cnt(u) += 1
          return true
        }
      }
      false
    }

    def dfs(u: Int, p: Int): Array[Int] = {
      var full = price(u) * cnt(u)
      var half = full / 2
      g(u).foreach { v =>
        if (v != p) {
          val child = dfs(v, u)
          full += math.min(child(0), child(1))
          half += child(0)
        }
      }
      Array(full, half)
    }

    i = 0
    while (i < trips.length) {
      path(trips(i)(0), -1, trips(i)(1))
      i += 1
    }
    val res = dfs(0, -1)
    math.min(res(0), res(1))
  }
}
"""

FILES["2647_color_the_triangle_red"] = """// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

object Solution {
  def colorRed(n: Int): Array[Array[Int]] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var i = 1
    while (i <= n) {
      ans += Array(i, 1)
      i += 1
    }
    i = n % 2 + 2
    while (i <= n) {
      var j = 2
      while (j <= 2 * (n - i) + 2) {
        ans += Array(i, j)
        j += 1
      }
      i += 2
    }
    ans.toArray
  }
}
"""

FILES["2648_generate_fibonacci_sequence"] = """// LeetCode 2648 - Generate Fibonacci Sequence
// https://leetcode.com/problems/generate-fibonacci-sequence/

object Solution {
  def fibGenerator(): () => Int = {
    val ab = Array(0, 1)
    () => {
      val v = ab(0)
      val na = ab(1)
      ab(1) = ab(0) + ab(1)
      ab(0) = na
      v
    }
  }
}
"""

FILES["2649_nested_array_generator"] = """// LeetCode 2649 - Nested Array Generator
// https://leetcode.com/problems/nested-array-generator/

object Solution {
  def inorderTraversal(arr: Array[Int]): Array[Int] = arr
}
"""

FILES["2650_design_cancellable_function"] = """// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

object Solution {
  def cancellable(generator: () => Int): Array[Any] = {
    var cancelled = false
    var done = false
    var result = 0
    val cancel: () => Unit = () => { cancelled = true }
    val run: () => Int = () => {
      if (!done) {
        result = generator()
        done = true
      }
      result
    }
    Array(cancel, run, cancelled)
  }
}
"""

FILES["2651_calculate_delayed_arrival_time"] = """// LeetCode 2651 - Calculate Delayed Arrival Time
// https://leetcode.com/problems/calculate-delayed-arrival-time/

object Solution {
  def findDelayedArrivalTime(arrivalTime: Int, delayedTime: Int): Int =
    (arrivalTime + delayedTime) % 24
}
"""

FILES["2652_sum_multiples"] = """// LeetCode 2652 - Sum Multiples
// https://leetcode.com/problems/sum-multiples/

object Solution {
  def sumOfMultiples(n: Int): Int = {
    var ans = 0
    var i = 1
    while (i <= n) {
      if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) ans += i
      i += 1
    }
    ans
  }
}
"""

FILES["2653_sliding_subarray_beauty"] = """// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/

object Solution {
  def getSubarrayBeauty(nums: Array[Int], k: Int, x: Int): Array[Int] = {
    val freq = new Array[Int](101)
    val ans = new Array[Int](nums.length - k + 1)
    var i = 0
    while (i < nums.length) {
      freq(nums(i) + 50) += 1
      if (i >= k) freq(nums(i - k) + 50) -= 1
      if (i >= k - 1) {
        var need = x
        var `val` = 0
        var j = 0
        var found = false
        while (j < 50 && !found) {
          need -= freq(j)
          if (need <= 0) {
            `val` = j - 50
            found = true
          }
          j += 1
        }
        ans(i - k + 1) = `val`
      }
      i += 1
    }
    ans
  }
}
"""

FILES["2654_minimum_number_of_operations_to_make_all_array_elements_equal_to_1"] = """// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    val n = nums.length
    var ones = 0
    var i = 0
    while (i < n) {
      if (nums(i) == 1) ones += 1
      i += 1
    }
    if (ones > 0) return n - ones
    var best = n + 1
    i = 0
    while (i < n) {
      var g = 0
      var j = i
      var done = false
      while (j < n && !done) {
        g = gcd(g, nums(j))
        if (g == 1) {
          best = math.min(best, j - i)
          done = true
        }
        j += 1
      }
      i += 1
    }
    if (best == n + 1) -1 else best + n - 1
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
"""

FILES["2655_find_maximal_uncovered_ranges"] = """// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

object Solution {
  def findMaximalUncoveredRanges(n: Int, ranges: Array[Array[Int]]): Array[Array[Int]] = {
    val sorted = ranges.sortBy(_(0))
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var cur = 0
    var i = 0
    while (i < sorted.length) {
      val r = sorted(i)
      if (r(0) > cur) ans += Array(cur, r(0) - 1)
      if (r(1) + 1 > cur) cur = r(1) + 1
      i += 1
    }
    if (cur < n) ans += Array(cur, n - 1)
    ans.toArray
  }
}
"""

FILES["2656_maximum_sum_with_exactly_k_elements"] = """// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

object Solution {
  def maximizeSum(nums: Array[Int], k: Int): Int = {
    var mx = nums(0)
    var i = 0
    while (i < nums.length) {
      if (nums(i) > mx) mx = nums(i)
      i += 1
    }
    k * mx + k * (k - 1) / 2
  }
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
