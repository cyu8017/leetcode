#!/usr/bin/env python3
"""Write Scala Solution.scala files for batch_00 problems 0621-0650."""
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

TREE = """class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}
"""

FILES = {}

FILES["0621_task_scheduler"] = """// LeetCode 0621 - Task Scheduler
// https://leetcode.com/problems/task-scheduler/

object Solution {
  def leastInterval(tasks: Array[Char], n: Int): Int = {
    val counts = Array.fill(26)(0)
    tasks.foreach(task => counts(task - 'A') += 1)
    var maxFreq = 0
    counts.foreach(count => maxFreq = math.max(maxFreq, count))
    var maxCount = 0
    counts.foreach(count => if (count == maxFreq) maxCount += 1)
    math.max(tasks.length, (maxFreq - 1) * (n + 1) + maxCount)
  }
}
"""

FILES["0622_design_circular_queue"] = """// LeetCode 0622 - Design Circular Queue
// https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue(_k: Int) {
  private val data = Array.fill(_k)(0)
  private val capacity = _k
  private var head = 0
  private var size = 0

  def enQueue(value: Int): Boolean = {
    if (isFull()) return false
    data((head + size) % capacity) = value
    size += 1
    true
  }

  def deQueue(): Boolean = {
    if (isEmpty()) return false
    head = (head + 1) % capacity
    size -= 1
    true
  }

  def Front(): Int = if (isEmpty()) -1 else data(head)

  def Rear(): Int = {
    if (isEmpty()) return -1
    data((head + size - 1) % capacity)
  }

  def isEmpty(): Boolean = size == 0

  def isFull(): Boolean = size == capacity
}
"""

FILES["0623_add_one_row_to_tree"] = f"""// LeetCode 0623 - Add One Row to Tree
// https://leetcode.com/problems/add-one-row-to-tree/

{TREE}
object Solution {{
  def addOneRow(root: TreeNode, `val`: Int, depth: Int): TreeNode = {{
    if (depth == 1) return new TreeNode(`val`, root, null)
    dfs(root, 1, `val`, depth)
    root
  }}

  private def dfs(node: TreeNode, current: Int, value: Int, depth: Int): Unit = {{
    if (node == null) return
    if (current == depth - 1) {{
      node.left = new TreeNode(value, node.left, null)
      node.right = new TreeNode(value, null, node.right)
      return
    }}
    dfs(node.left, current + 1, value, depth)
    dfs(node.right, current + 1, value, depth)
  }}
}}
"""

FILES["0624_maximum_distance_in_arrays"] = """// LeetCode 0624 - Maximum Distance in Arrays
// https://leetcode.com/problems/maximum-distance-in-arrays/

object Solution {
  def maxDistance(arrays: List[List[Int]]): Int = {
    var minVal = arrays.head.head
    var maxVal = arrays.head.last
    var best = 0
    var i = 1
    while (i < arrays.size) {
      val arr = arrays(i)
      val first = arr.head
      val last = arr.last
      best = math.max(best, math.max(math.abs(last - minVal), math.abs(maxVal - first)))
      minVal = math.min(minVal, first)
      maxVal = math.max(maxVal, last)
      i += 1
    }
    best
  }
}
"""

FILES["0625_minimum_factorization"] = """// LeetCode 0625 - Minimum Factorization
// https://leetcode.com/problems/minimum-factorization/

import scala.collection.mutable

object Solution {
  def smallestFactorization(num0: Int): Int = {
    var num = num0
    if (num < 10) return num
    val digits = mutable.ArrayBuffer.empty[Int]
    var digit = 9
    while (digit >= 2) {
      while (num % digit == 0) {
        digits += digit
        num /= digit
      }
      digit -= 1
    }
    if (num != 1) return 0
    var result = 0L
    var i = digits.size - 1
    while (i >= 0) {
      result = result * 10 + digits(i)
      if (result > Int.MaxValue) return 0
      i -= 1
    }
    result.toInt
  }
}
"""

FILES["0628_maximum_product_of_three_numbers"] = """// LeetCode 0628 - Maximum Product of Three Numbers
// https://leetcode.com/problems/maximum-product-of-three-numbers/

object Solution {
  def maximumProduct(nums: Array[Int]): Int = {
    scala.util.Sorting.quickSort(nums)
    val n = nums.length
    math.max(nums(n - 1) * nums(n - 2) * nums(n - 3), nums(0) * nums(1) * nums(n - 1))
  }
}
"""

FILES["0629_k_inverse_pairs_array"] = """// LeetCode 0629 - K Inverse Pairs Array
// https://leetcode.com/problems/k-inverse-pairs-array/

object Solution {
  def kInversePairs(n: Int, k: Int): Int = {
    val mod = 1000000007
    var dp = Array.fill(k + 1)(0)
    dp(0) = 1
    var size = 1
    while (size <= n) {
      val nxt = Array.fill(k + 1)(0)
      var prefix = 0L
      var pairs = 0
      while (pairs <= k) {
        prefix = (prefix + dp(pairs)) % mod
        if (pairs >= size) prefix = (prefix - dp(pairs - size) + mod) % mod
        nxt(pairs) = prefix.toInt
        pairs += 1
      }
      dp = nxt
      size += 1
    }
    dp(k)
  }
}
"""

FILES["0630_course_schedule_iii"] = """// LeetCode 0630 - Course Schedule III
// https://leetcode.com/problems/course-schedule-iii/

import scala.collection.mutable

object Solution {
  def scheduleCourse(courses: Array[Array[Int]]): Int = {
    val sorted = courses.sortBy(_(1))
    val heap = mutable.PriorityQueue.empty[Int]
    var time = 0
    sorted.foreach { course =>
      val duration = course(0)
      val lastDay = course(1)
      if (time + duration <= lastDay) {
        heap.enqueue(duration)
        time += duration
      } else if (heap.nonEmpty && heap.head > duration) {
        time += duration - heap.dequeue()
        heap.enqueue(duration)
      }
    }
    heap.size
  }
}
"""

FILES["0631_design_excel_sum_formula"] = """// LeetCode 0631 - Design Excel Sum Formula
// https://leetcode.com/problems/design-excel-sum-formula/

import scala.collection.mutable

class Excel(height: Int, width: Char) {
  private val values = Array.ofDim[Int](height + 1, width - 'A' + 1)
  private val formulas = mutable.Map.empty[Long, mutable.ArrayBuffer[Array[Int]]]

  def set(row: Int, column: Char, `val`: Int): Unit = {
    val col = column - 'A'
    formulas.remove(key(row, col))
    values(row)(col) = `val`
  }

  def get(row: Int, column: Char): Int = eval(row, column - 'A')

  def sum(row: Int, column: Char, numbers: Array[String]): Int = {
    val col = column - 'A'
    val cells = mutable.ArrayBuffer.empty[Array[Int]]
    numbers.foreach { token =>
      val colon = token.indexOf(':')
      if (colon >= 0) {
        val p1 = parse(token.substring(0, colon))
        val p2 = parse(token.substring(colon + 1))
        var r = p1(0)
        while (r <= p2(0)) {
          var c = p1(1)
          while (c <= p2(1)) {
            cells += Array(r, c)
            c += 1
          }
          r += 1
        }
      } else {
        cells += parse(token)
      }
    }
    formulas(key(row, col)) = cells
    eval(row, col)
  }

  private def parse(cell: String): Array[Int] =
    Array(cell.substring(1).toInt, cell.charAt(0) - 'A')

  private def eval(row: Int, col: Int): Int = {
    formulas.get(key(row, col)) match {
      case Some(formula) =>
        var total = 0
        formula.foreach(cell => total += eval(cell(0), cell(1)))
        total
      case None => values(row)(col)
    }
  }

  private def key(row: Int, col: Int): Long =
    (row.toLong << 32) | (col.toLong & 0xffffffffL)
}
"""

FILES["0632_smallest_range_covering_elements_from_k_lists"] = """// LeetCode 0632 - Smallest Range Covering Elements from K Lists
// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

import scala.collection.mutable

object Solution {
  def smallestRange(nums: List[List[Int]]): Array[Int] = {
    implicit val ord: Ordering[Array[Int]] = Ordering.by(-_(0))
    val heap = mutable.PriorityQueue.empty[Array[Int]]
    var currentMax = Int.MinValue
    var i = 0
    while (i < nums.size) {
      val value = nums(i).head
      heap.enqueue(Array(value, i, 0))
      currentMax = math.max(currentMax, value)
      i += 1
    }
    var bestLeft = heap.head(0)
    var bestRight = currentMax
    var done = false
    while (!done) {
      val top = heap.dequeue()
      val value = top(0)
      val listIndex = top(1)
      val index = top(2)
      if (currentMax - value < bestRight - bestLeft) {
        bestLeft = value
        bestRight = currentMax
      }
      if (index + 1 == nums(listIndex).size) {
        done = true
      } else {
        val nxt = nums(listIndex)(index + 1)
        heap.enqueue(Array(nxt, listIndex, index + 1))
        currentMax = math.max(currentMax, nxt)
      }
    }
    Array(bestLeft, bestRight)
  }
}
"""

FILES["0633_sum_of_square_numbers"] = """// LeetCode 0633 - Sum of Square Numbers
// https://leetcode.com/problems/sum-of-square-numbers/

object Solution {
  def judgeSquareSum(c: Int): Boolean = {
    var left = 0L
    var right = math.sqrt(c.toDouble).toLong
    while (left <= right) {
      val total = left * left + right * right
      if (total == c) return true
      if (total < c) left += 1 else right -= 1
    }
    false
  }
}
"""

FILES["0634_find_the_derangement_of_an_array"] = """// LeetCode 0634 - Find the Derangement of An Array
// https://leetcode.com/problems/find-the-derangement-of-an-array/

object Solution {
  def findDerangement(n: Int): Int = {
    val mod = 1000000007
    if (n == 1) return 0
    var prev2 = 0L
    var prev1 = 1L
    var size = 3
    while (size <= n) {
      val next = (size - 1) * (prev1 + prev2) % mod
      prev2 = prev1
      prev1 = next
      size += 1
    }
    prev1.toInt
  }
}
"""

FILES["0635_design_log_storage_system"] = """// LeetCode 0635 - Design Log Storage System
// https://leetcode.com/problems/design-log-storage-system/

import scala.collection.mutable

class LogSystem() {
  private val ids = mutable.ArrayBuffer.empty[Int]
  private val timestamps = mutable.ArrayBuffer.empty[String]
  private val granularityIndex = mutable.Map(
    "Year" -> 4,
    "Month" -> 7,
    "Day" -> 10,
    "Hour" -> 13,
    "Minute" -> 16,
    "Second" -> 19,
  )

  def put(id: Int, timestamp: String): Unit = {
    ids += id
    timestamps += timestamp
  }

  def retrieve(start: String, end: String, granularity: String): List[Int] = {
    val index = granularityIndex(granularity)
    val startKey = start.substring(0, index)
    val endKey = end.substring(0, index)
    val matched = mutable.ArrayBuffer.empty[(String, Int)]
    var i = 0
    while (i < timestamps.size) {
      val timestamp = timestamps(i)
      val key = timestamp.substring(0, index)
      if (startKey.compareTo(key) <= 0 && key.compareTo(endKey) <= 0) {
        matched += ((timestamp, ids(i)))
      }
      i += 1
    }
    matched.sortBy(_._1).map(_._2).toList
  }
}
"""

FILES["0636_exclusive_time_of_functions"] = """// LeetCode 0636 - Exclusive Time of Functions
// https://leetcode.com/problems/exclusive-time-of-functions/

import scala.collection.mutable

object Solution {
  def exclusiveTime(n: Int, logs: List[String]): Array[Int] = {
    val result = Array.fill(n)(0)
    val stack = mutable.ArrayBuffer.empty[Int]
    var prevTime = 0
    logs.foreach { log =>
      val parts = log.split(":")
      val funcId = parts(0).toInt
      val event = parts(1)
      val time = parts(2).toInt
      if (event == "start") {
        if (stack.nonEmpty) result(stack.last) += time - prevTime
        stack += funcId
        prevTime = time
      } else {
        result(stack.remove(stack.size - 1)) += time - prevTime + 1
        prevTime = time + 1
      }
    }
    result
  }
}
"""

FILES["0637_average_of_levels_in_binary_tree"] = f"""// LeetCode 0637 - Average of Levels in Binary Tree
// https://leetcode.com/problems/average-of-levels-in-binary-tree/

import scala.collection.mutable

{TREE}
object Solution {{
  def averageOfLevels(root: TreeNode): Array[Double] = {{
    if (root == null) return Array.empty[Double]
    val result = mutable.ArrayBuffer.empty[Double]
    val queue = mutable.Queue[TreeNode](root)
    while (queue.nonEmpty) {{
      val count = queue.size
      var total = 0L
      var i = 0
      while (i < count) {{
        val node = queue.dequeue()
        total += node.value
        if (node.left != null) queue.enqueue(node.left)
        if (node.right != null) queue.enqueue(node.right)
        i += 1
      }}
      result += total.toDouble / count
    }}
    result.toArray
  }}
}}
"""

FILES["0638_shopping_offers"] = """// LeetCode 0638 - Shopping Offers
// https://leetcode.com/problems/shopping-offers/

import scala.collection.mutable

object Solution {
  def shoppingOffers(price: List[Int], special: List[List[Int]], needs: List[Int]): Int = {
    val memo = mutable.Map.empty[List[Int], Int]
    def dfs(state: List[Int]): Int = {
      memo.get(state) match {
        case Some(cached) => cached
        case None =>
          var cost = 0
          var i = 0
          while (i < price.size) {
            cost += state(i) * price(i)
            i += 1
          }
          special.foreach { offer =>
            val nxt = state.toArray
            var valid = true
            i = 0
            while (i < price.size && valid) {
              if (nxt(i) < offer(i)) valid = false
              else nxt(i) -= offer(i)
              i += 1
            }
            if (valid) cost = math.min(cost, offer(price.size) + dfs(nxt.toList))
          }
          memo(state) = cost
          cost
      }
    }
    dfs(needs)
  }
}
"""

FILES["0639_decode_ways_ii"] = """// LeetCode 0639 - Decode Ways II
// https://leetcode.com/problems/decode-ways-ii/

object Solution {
  def numDecodings(s: String): Int = {
    val mod = 1000000007
    var prev2 = 1L
    var prev1 = one(s.charAt(0)).toLong
    var i = 1
    while (i < s.length) {
      val cur = (one(s.charAt(i)) * prev1 + two(s.charAt(i - 1), s.charAt(i)) * prev2) % mod
      prev2 = prev1
      prev1 = cur
      i += 1
    }
    prev1.toInt
  }

  private def one(ch: Char): Int = {
    if (ch == '*') 9
    else if (ch == '0') 0
    else 1
  }

  private def two(a: Char, b: Char): Int = {
    if (a == '*' && b == '*') return 15
    if (a == '*') return if (b <= '6') 2 else 1
    if (b == '*') {
      if (a == '1') return 9
      if (a == '2') return 6
      return 0
    }
    val value = (a - '0') * 10 + (b - '0')
    if (value >= 10 && value <= 26) 1 else 0
  }
}
"""

FILES["0640_solve_the_equation"] = """// LeetCode 0640 - Solve the Equation
// https://leetcode.com/problems/solve-the-equation/

object Solution {
  def solveEquation(equation: String): String = {
    val eq = equation.indexOf('=')
    val left = parse(equation.substring(0, eq))
    val right = parse(equation.substring(eq + 1))
    val coef = left(0) - right(0)
    val constant = right(1) - left(1)
    if (coef == 0) return if (constant == 0) "Infinite solutions" else "No solution"
    "x=" + (constant / coef)
  }

  private def parse(expr: String): Array[Int] = {
    var coef = 0
    var constant = 0
    val n = expr.length
    var i = 0
    while (i < n) {
      var sign = 1
      if (expr.charAt(i) == '+' || expr.charAt(i) == '-') {
        sign = if (expr.charAt(i) == '-') -1 else 1
        i += 1
      }
      var value = 0
      var hasDigit = false
      while (i < n && expr.charAt(i).isDigit) {
        hasDigit = true
        value = value * 10 + (expr.charAt(i) - '0')
        i += 1
      }
      if (i < n && expr.charAt(i) == 'x') {
        coef += sign * (if (hasDigit) value else 1)
        i += 1
      } else {
        constant += sign * value
      }
    }
    Array(coef, constant)
  }
}
"""

FILES["0641_design_circular_deque"] = """// LeetCode 0641 - Design Circular Deque
// https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque(_k: Int) {
  private val data = Array.fill(_k)(0)
  private val capacity = _k
  private var front = 0
  private var size = 0

  def insertFront(value: Int): Boolean = {
    if (isFull()) return false
    front = (front - 1 + capacity) % capacity
    data(front) = value
    size += 1
    true
  }

  def insertLast(value: Int): Boolean = {
    if (isFull()) return false
    data((front + size) % capacity) = value
    size += 1
    true
  }

  def deleteFront(): Boolean = {
    if (isEmpty()) return false
    front = (front + 1) % capacity
    size -= 1
    true
  }

  def deleteLast(): Boolean = {
    if (isEmpty()) return false
    size -= 1
    true
  }

  def getFront(): Int = if (isEmpty()) -1 else data(front)

  def getRear(): Int = {
    if (isEmpty()) return -1
    data((front + size - 1) % capacity)
  }

  def isEmpty(): Boolean = size == 0

  def isFull(): Boolean = size == capacity
}
"""

FILES["0642_design_search_autocomplete_system"] = """// LeetCode 0642 - Design Search Autocomplete System
// https://leetcode.com/problems/design-search-autocomplete-system/

import scala.collection.mutable

class AutocompleteSystem(sentences: Array[String], times: Array[Int]) {
  private val counts = mutable.Map.empty[String, Int]
  private val current = new StringBuilder

  {
    var i = 0
    while (i < sentences.length) {
      counts(sentences(i)) = counts.getOrElse(sentences(i), 0) + times(i)
      i += 1
    }
  }

  def input(c: Char): List[String] = {
    if (c == '#') {
      val sentence = current.toString
      counts(sentence) = counts.getOrElse(sentence, 0) + 1
      current.setLength(0)
      return List.empty
    }
    current.append(c)
    val prefix = current.toString
    val matches = mutable.ArrayBuffer.empty[String]
    counts.keys.foreach { sentence =>
      if (sentence.startsWith(prefix)) matches += sentence
    }
    val sorted = matches.sortWith { (a, b) =>
      val ca = counts(a)
      val cb = counts(b)
      if (ca != cb) ca > cb else a < b
    }
    if (sorted.size > 3) sorted.take(3).toList else sorted.toList
  }
}
"""

FILES["0643_maximum_average_subarray_i"] = """// LeetCode 0643 - Maximum Average Subarray I
// https://leetcode.com/problems/maximum-average-subarray-i/

object Solution {
  def findMaxAverage(nums: Array[Int], k: Int): Double = {
    var window = 0L
    var i = 0
    while (i < k) { window += nums(i); i += 1 }
    var best = window
    i = k
    while (i < nums.length) {
      window += nums(i) - nums(i - k)
      best = math.max(best, window)
      i += 1
    }
    best.toDouble / k
  }
}
"""

FILES["0644_maximum_average_subarray_ii"] = """// LeetCode 0644 - Maximum Average Subarray II
// https://leetcode.com/problems/maximum-average-subarray-ii/

object Solution {
  def findMaxAverage(nums: Array[Int], k: Int): Double = {
    var left = nums(0).toDouble
    var right = nums(0).toDouble
    nums.foreach { num =>
      left = math.min(left, num.toDouble)
      right = math.max(right, num.toDouble)
    }
    var i = 0
    while (i < 80) {
      val mid = (left + right) / 2.0
      if (canReach(nums, k, mid)) left = mid else right = mid
      i += 1
    }
    left
  }

  private def canReach(nums: Array[Int], k: Int, mid: Double): Boolean = {
    var prefix = 0.0
    var i = 0
    while (i < k) { prefix += nums(i) - mid; i += 1 }
    if (prefix >= 0) return true
    var prev = 0.0
    var minPrev = 0.0
    i = k
    while (i < nums.length) {
      prefix += nums(i) - mid
      prev += nums(i - k) - mid
      minPrev = math.min(minPrev, prev)
      if (prefix - minPrev >= 0) return true
      i += 1
    }
    false
  }
}
"""

FILES["0645_set_mismatch"] = """// LeetCode 0645 - Set Mismatch
// https://leetcode.com/problems/set-mismatch/

object Solution {
  def findErrorNums(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val seen = Array.fill(n + 1)(0)
    nums.foreach(value => seen(value) += 1)
    var duplicate = -1
    var missing = -1
    var value = 1
    while (value <= n) {
      if (seen(value) == 2) duplicate = value
      else if (seen(value) == 0) missing = value
      value += 1
    }
    Array(duplicate, missing)
  }
}
"""

FILES["0646_maximum_length_of_pair_chain"] = """// LeetCode 0646 - Maximum Length of Pair Chain
// https://leetcode.com/problems/maximum-length-of-pair-chain/

object Solution {
  def findLongestChain(pairs: Array[Array[Int]]): Int = {
    val sorted = pairs.sortBy(_(1))
    var length = 0
    var currentEnd = Int.MinValue
    sorted.foreach { pair =>
      if (pair(0) > currentEnd) {
        length += 1
        currentEnd = pair(1)
      }
    }
    length
  }
}
"""

FILES["0647_palindromic_substrings"] = """// LeetCode 0647 - Palindromic Substrings
// https://leetcode.com/problems/palindromic-substrings/

object Solution {
  def countSubstrings(s: String): Int = {
    var total = 0
    var i = 0
    while (i < s.length) {
      total += expand(s, i, i)
      total += expand(s, i, i + 1)
      i += 1
    }
    total
  }

  private def expand(s: String, left0: Int, right0: Int): Int = {
    var left = left0
    var right = right0
    var count = 0
    while (left >= 0 && right < s.length && s.charAt(left) == s.charAt(right)) {
      count += 1
      left -= 1
      right += 1
    }
    count
  }
}
"""

FILES["0648_replace_words"] = """// LeetCode 0648 - Replace Words
// https://leetcode.com/problems/replace-words/

object Solution {
  def replaceWords(dictionary: List[String], sentence: String): String = {
    val roots = dictionary.toSet
    val words = sentence.split(" ")
    val result = new StringBuilder
    var w = 0
    while (w < words.length) {
      val word = words(w)
      var replacement = word
      var i = 1
      var found = false
      while (i <= word.length && !found) {
        val prefix = word.substring(0, i)
        if (roots.contains(prefix)) {
          replacement = prefix
          found = true
        }
        i += 1
      }
      if (w > 0) result.append(' ')
      result.append(replacement)
      w += 1
    }
    result.toString
  }
}
"""

FILES["0649_dota2_senate"] = """// LeetCode 0649 - Dota2 Senate
// https://leetcode.com/problems/dota2-senate/

import scala.collection.mutable

object Solution {
  def predictPartyVictory(senate: String): String = {
    val radiant = mutable.Queue.empty[Int]
    val dire = mutable.Queue.empty[Int]
    val n = senate.length
    var i = 0
    while (i < n) {
      if (senate.charAt(i) == 'R') radiant.enqueue(i) else dire.enqueue(i)
      i += 1
    }
    while (radiant.nonEmpty && dire.nonEmpty) {
      val r = radiant.dequeue()
      val d = dire.dequeue()
      if (r < d) radiant.enqueue(r + n) else dire.enqueue(d + n)
    }
    if (radiant.isEmpty) "Dire" else "Radiant"
  }
}
"""

FILES["0650_2_keys_keyboard"] = """// LeetCode 0650 - 2 Keys Keyboard
// https://leetcode.com/problems/2-keys-keyboard/

object Solution {
  def minSteps(n0: Int): Int = {
    var n = n0
    var steps = 0
    var factor = 2
    while (factor * factor <= n) {
      while (n % factor == 0) {
        steps += factor
        n /= factor
      }
      factor += 1
    }
    if (n > 1) steps += n
    steps
  }
}
"""


def main() -> None:
    written = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "Solution.scala"
        path.write_text(content, encoding="utf-8", newline="\n")
        written += 1
        print("wrote", folder)
    print("TOTAL", written)


if __name__ == "__main__":
    main()
