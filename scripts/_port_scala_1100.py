# Temporary batch port script for Scala 1100-1299. Delete after use.
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(folder: str, code: str) -> None:
    path = ROOT / folder / "Solution.scala"
    path.write_text(code.strip() + "\n", encoding="utf-8")
    print(f"wrote {folder}")


SOLUTIONS = {}

SOLUTIONS["1111_maximum_nesting_depth_of_two_valid_parentheses_strings"] = r'''
// LeetCode 1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

object Solution {
  def maxDepthAfterSplit(seq: String): Array[Int] = {
    var depth = 0
    val ans = Array.ofDim[Int](seq.length)
    for (i <- seq.indices) {
      if (seq(i) == '(') {
        ans(i) = depth % 2
        depth += 1
      } else {
        depth -= 1
        ans(i) = depth % 2
      }
    }
    ans
  }
}
'''

SOLUTIONS["1114_print_in_order"] = r'''
// LeetCode 1114 - Print in Order
// https://leetcode.com/problems/print-in-order/

class Foo {
  private val second = new java.util.concurrent.Semaphore(0)
  private val third = new java.util.concurrent.Semaphore(0)

  def first(printFirst: Runnable): Unit = {
    printFirst.run()
    second.release()
  }

  def second(printSecond: Runnable): Unit = {
    second.acquire()
    printSecond.run()
    third.release()
  }

  def third(printThird: Runnable): Unit = {
    third.acquire()
    printThird.run()
  }
}
'''

SOLUTIONS["1115_print_foobar_alternately"] = r'''
// LeetCode 1115 - Print FooBar Alternately
// https://leetcode.com/problems/print-foobar-alternately/

class FooBar(n: Int) {
  private val fooSem = new java.util.concurrent.Semaphore(1)
  private val barSem = new java.util.concurrent.Semaphore(0)

  def foo(printFoo: Runnable): Unit = {
    for (_ <- 0 until n) {
      fooSem.acquire()
      printFoo.run()
      barSem.release()
    }
  }

  def bar(printBar: Runnable): Unit = {
    for (_ <- 0 until n) {
      barSem.acquire()
      printBar.run()
      fooSem.release()
    }
  }
}
'''

SOLUTIONS["1116_print_zero_even_odd"] = r'''
// LeetCode 1116 - Print Zero Even Odd
// https://leetcode.com/problems/print-zero-even-odd/

class ZeroEvenOdd(n: Int) {
  private val zeroSem = new java.util.concurrent.Semaphore(1)
  private val evenSem = new java.util.concurrent.Semaphore(0)
  private val oddSem = new java.util.concurrent.Semaphore(0)

  def zero(printNumber: Int => Unit): Unit = {
    for (i <- 0 until n) {
      zeroSem.acquire()
      printNumber(0)
      if (i % 2 == 0) oddSem.release() else evenSem.release()
    }
  }

  def even(printNumber: Int => Unit): Unit = {
    var num = 2
    while (num <= n) {
      evenSem.acquire()
      printNumber(num)
      zeroSem.release()
      num += 2
    }
  }

  def odd(printNumber: Int => Unit): Unit = {
    var num = 1
    while (num <= n) {
      oddSem.acquire()
      printNumber(num)
      zeroSem.release()
      num += 2
    }
  }
}
'''

SOLUTIONS["1117_building_h2o"] = r'''
// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

class H2O {
  private val hydrogen = new java.util.concurrent.Semaphore(2)
  private val oxygen = new java.util.concurrent.Semaphore(0)
  private val lock = new Object
  private var count = 0

  def hydrogen(releaseHydrogen: Runnable): Unit = {
    hydrogen.acquire()
    lock.synchronized {
      count += 1
      if (count == 2) oxygen.release()
    }
    releaseHydrogen.run()
  }

  def oxygen(releaseOxygen: Runnable): Unit = {
    oxygen.acquire()
    releaseOxygen.run()
    lock.synchronized {
      count = 0
      hydrogen.release()
      hydrogen.release()
    }
  }
}
'''

SOLUTIONS["1118_number_of_days_in_a_month"] = r'''
// LeetCode 1118 - Number of Days in a Month
// https://leetcode.com/problems/number-of-days-in-a-month/

object Solution {
  def numberOfDays(year: Int, month: Int): Int = {
    val days = Array(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if (month == 2 && ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)) 29
    else days(month - 1)
  }
}
'''

SOLUTIONS["1119_remove_vowels_from_a_string"] = r'''
// LeetCode 1119 - Remove Vowels from a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

object Solution {
  def removeVowels(s: String): String =
    s.filter(ch => !"aeiou".contains(ch))
}
'''

SOLUTIONS["1120_maximum_average_subtree"] = r'''
// LeetCode 1120 - Maximum Average Subtree
// https://leetcode.com/problems/maximum-average-subtree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def maximumAverageSubtree(root: TreeNode): Double = {
    var ans = Double.NegativeInfinity
    def dfs(node: TreeNode): (Int, Int) = {
      if (node == null) return (0, 0)
      val (ls, lc) = dfs(node.left)
      val (rs, rc) = dfs(node.right)
      val sum = ls + rs + node.value
      val count = lc + rc + 1
      ans = math.max(ans, sum.toDouble / count)
      (sum, count)
    }
    dfs(root)
    ans
  }
}
'''

SOLUTIONS["1121_divide_array_into_increasing_sequences"] = r'''
// LeetCode 1121 - Divide Array Into Increasing Sequences
// https://leetcode.com/problems/divide-array-into-increasing-sequences/

object Solution {
  def canDivideIntoSubsequences(nums: Array[Int], k: Int): Boolean = {
    var maxFreq = 1
    var cur = 1
    for (i <- 1 until nums.length) {
      if (nums(i) == nums(i - 1)) {
        cur += 1
        maxFreq = math.max(maxFreq, cur)
      } else cur = 1
    }
    maxFreq.toLong * k <= nums.length
  }
}
'''

SOLUTIONS["1122_relative_sort_array"] = r'''
// LeetCode 1122 - Relative Sort Array
// https://leetcode.com/problems/relative-sort-array/

object Solution {
  def relativeSortArray(arr1: Array[Int], arr2: Array[Int]): Array[Int] = {
    val order = arr2.zipWithIndex.toMap
    arr1.sortBy(x => (order.getOrElse(x, 1000 + x), x))
  }
}
'''

SOLUTIONS["1123_lowest_common_ancestor_of_deepest_leaves"] = r'''
// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def lcaDeepestLeaves(root: TreeNode): TreeNode = {
    def dfs(node: TreeNode): (TreeNode, Int) = {
      if (node == null) return (null, 0)
      val (lNode, lDepth) = dfs(node.left)
      val (rNode, rDepth) = dfs(node.right)
      if (lDepth > rDepth) (lNode, lDepth + 1)
      else if (rDepth > lDepth) (rNode, rDepth + 1)
      else (node, lDepth + 1)
    }
    dfs(root)._1
  }
}
'''

SOLUTIONS["1124_longest_well_performing_interval"] = r'''
// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

object Solution {
  def longestWPI(hours: Array[Int]): Int = {
    val seen = scala.collection.mutable.Map.empty[Int, Int]
    var score = 0
    var ans = 0
    for (i <- hours.indices) {
      score += (if (hours(i) > 8) 1 else -1)
      if (score > 0) ans = i + 1
      else {
        if (!seen.contains(score)) seen(score) = i
        if (seen.contains(score - 1)) ans = math.max(ans, i - seen(score - 1))
      }
    }
    ans
  }
}
'''

SOLUTIONS["1125_smallest_sufficient_team"] = r'''
// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

object Solution {
  def smallestSufficientTeam(req_skills: Array[String], people: List[List[String]]): Array[Int] = {
    val n = req_skills.length
    val skillIndex = req_skills.zipWithIndex.toMap
    val peopleMask = people.map(p => p.map(skillIndex).foldLeft(0)((acc, i) => acc | (1 << i))).toArray
    val dp = Array.fill[Array[Int]](1 << n)(null)
    dp(0) = Array.empty[Int]
    for (mask <- 0 until (1 << n) if dp(mask) != null; i <- peopleMask.indices) {
      val next = mask | peopleMask(i)
      if (dp(next) == null || dp(next).length > dp(mask).length + 1) {
        dp(next) = dp(mask) :+ i
      }
    }
    dp((1 << n) - 1)
  }
}
'''

SOLUTIONS["1128_number_of_equivalent_domino_pairs"] = r'''
// LeetCode 1128 - Number of Equivalent Domino Pairs
// https://leetcode.com/problems/number-of-equivalent-domino-pairs/

object Solution {
  def numEquivDominoPairs(dominoes: Array[Array[Int]]): Int = {
    val count = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0
    for (d <- dominoes) {
      val a = math.min(d(0), d(1))
      val b = math.max(d(0), d(1))
      val key = a * 10 + b
      ans += count.getOrElse(key, 0)
      count(key) = count.getOrElse(key, 0) + 1
    }
    ans
  }
}
'''

SOLUTIONS["1129_shortest_path_with_alternating_colors"] = r'''
// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

object Solution {
  def shortestAlternatingPaths(n: Int, redEdges: Array[Array[Int]], blueEdges: Array[Array[Int]]): Array[Int] = {
    val red = Array.fill(n)(scala.collection.mutable.ListBuffer.empty[Int])
    val blue = Array.fill(n)(scala.collection.mutable.ListBuffer.empty[Int])
    for (e <- redEdges) red(e(0)) += e(1)
    for (e <- blueEdges) blue(e(0)) += e(1)
    val ans = Array.fill(n)(-1)
    val seen = Array.fill(n, 2)(false)
    val q = scala.collection.mutable.Queue[(Int, Int, Int)]()
    q.enqueue((0, 0, -1))
    seen(0)(0) = true
    seen(0)(1) = true
    ans(0) = 0
    while (q.nonEmpty) {
      val (node, dist, color) = q.dequeue()
      if (color != 0) {
        for (nei <- red(node) if !seen(nei)(0)) {
          seen(nei)(0) = true
          if (ans(nei) == -1) ans(nei) = dist + 1
          q.enqueue((nei, dist + 1, 0))
        }
      }
      if (color != 1) {
        for (nei <- blue(node) if !seen(nei)(1)) {
          seen(nei)(1) = true
          if (ans(nei) == -1) ans(nei) = dist + 1
          q.enqueue((nei, dist + 1, 1))
        }
      }
    }
    ans
  }
}
'''

SOLUTIONS["1130_minimum_cost_tree_from_leaf_values"] = r'''
// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

object Solution {
  def mctFromLeafValues(arr: Array[Int]): Int = {
    val stack = scala.collection.mutable.ArrayBuffer(Int.MaxValue)
    var ans = 0
    for (a <- arr) {
      while (stack.last <= a) {
        val mid = stack.remove(stack.length - 1)
        ans += mid * math.min(stack.last, a)
      }
      stack += a
    }
    while (stack.length > 2) {
      val mid = stack.remove(stack.length - 1)
      ans += mid * stack.last
    }
    ans
  }
}
'''

SOLUTIONS["1131_maximum_of_absolute_value_expression"] = r'''
// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

object Solution {
  def maxAbsValExpr(arr1: Array[Int], arr2: Array[Int]): Int = {
    val n = arr1.length
    var ans = 0
    for ((s1, s2) <- Seq((1, 1), (1, -1), (-1, 1), (-1, -1))) {
      var maxv = Int.MinValue
      var minv = Int.MaxValue
      for (i <- 0 until n) {
        val v = s1 * arr1(i) + s2 * arr2(i) + i
        maxv = math.max(maxv, v)
        minv = math.min(minv, v)
      }
      ans = math.max(ans, maxv - minv)
    }
    ans
  }
}
'''

SOLUTIONS["1133_largest_unique_number"] = r'''
// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

object Solution {
  def largestUniqueNumber(nums: Array[Int]): Int = {
    val count = nums.groupBy(identity).view.mapValues(_.length).toMap
    nums.filter(x => count(x) == 1).foldLeft(-1)(math.max)
  }
}
'''

SOLUTIONS["1134_armstrong_number"] = r'''
// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

object Solution {
  def isArmstrong(n: Int): Boolean = {
    val s = n.toString
    val k = s.length
    s.map(c => math.pow(c - '0', k).toInt).sum == n
  }
}
'''

SOLUTIONS["1135_connecting_cities_with_minimum_cost"] = r'''
// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

object Solution {
  def minimumCost(n: Int, connections: Array[Array[Int]]): Int = {
    val parent = Array.tabulate(n + 1)(identity)
    def find(x: Int): Int = {
      var cur = x
      while (parent(cur) != cur) {
        parent(cur) = parent(parent(cur))
        cur = parent(cur)
      }
      cur
    }
    val edges = connections.sortBy(_(2))
    var cost = 0
    var used = 0
    for (e <- edges) {
      val a = find(e(0))
      val b = find(e(1))
      if (a != b) {
        parent(b) = a
        cost += e(2)
        used += 1
        if (used == n - 1) return cost
      }
    }
    -1
  }
}
'''


def main() -> None:
    for folder, code in SOLUTIONS.items():
        write(folder, code)
    print(f"done {len(SOLUTIONS)}")


if __name__ == "__main__":
    main()
