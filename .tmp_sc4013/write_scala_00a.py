#!/usr/bin/env python3
"""Write Scala Solution.scala files for batch_00 problems 0551-0617."""
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

TREE = """class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}
"""

NARY = """class Node(_value: Int = 0, _children: List[Node] = Nil) {
  var value: Int = _value
  var children: List[Node] = _children
}
"""

QUAD = """class Node(
  _val: Boolean = false,
  _isLeaf: Boolean = false,
  _topLeft: Node = null,
  _topRight: Node = null,
  _bottomLeft: Node = null,
  _bottomRight: Node = null,
) {
  var value: Boolean = _val
  var isLeaf: Boolean = _isLeaf
  var topLeft: Node = _topLeft
  var topRight: Node = _topRight
  var bottomLeft: Node = _bottomLeft
  var bottomRight: Node = _bottomRight
}
"""

FILES = {}

FILES["0551_student_attendance_record_i"] = """// LeetCode 0551 - Student Attendance Record I
// https://leetcode.com/problems/student-attendance-record-i/

object Solution {
  def checkRecord(s: String): Boolean = {
    var absents = 0
    var lateStreak = 0
    for (i <- s.indices) {
      val ch = s.charAt(i)
      if (ch == 'A') {
        absents += 1
        if (absents >= 2) return false
        lateStreak = 0
      } else if (ch == 'L') {
        lateStreak += 1
        if (lateStreak >= 3) return false
      } else {
        lateStreak = 0
      }
    }
    true
  }
}
"""

FILES["0552_student_attendance_record_ii"] = """// LeetCode 0552 - Student Attendance Record II
// https://leetcode.com/problems/student-attendance-record-ii/

object Solution {
  def checkRecord(n: Int): Int = {
    val MOD = 1000000007
    var dp = Array(Array(1L, 0L, 0L), Array(0L, 0L, 0L))
    for (_ <- 0 until n) {
      val nxt = Array.ofDim[Long](2, 3)
      for (absences <- 0 until 2; lates <- 0 until 3) {
        val ways = dp(absences)(lates)
        if (ways != 0) {
          nxt(absences)(0) = (nxt(absences)(0) + ways) % MOD
          if (absences == 0) nxt(1)(0) = (nxt(1)(0) + ways) % MOD
          if (lates < 2) nxt(absences)(lates + 1) = (nxt(absences)(lates + 1) + ways) % MOD
        }
      }
      dp = nxt
    }
    var total = 0L
    for (absences <- 0 until 2; lates <- 0 until 3) {
      total = (total + dp(absences)(lates)) % MOD
    }
    total.toInt
  }
}
"""

FILES["0553_optimal_division"] = """// LeetCode 0553 - Optimal Division
// https://leetcode.com/problems/optimal-division/

object Solution {
  def optimalDivision(nums: Array[Int]): String = {
    if (nums.length == 1) return nums(0).toString
    if (nums.length == 2) return s"${nums(0)}/${nums(1)}"
    val result = new StringBuilder
    result.append(nums(0)).append("/(")
    var i = 1
    while (i < nums.length) {
      if (i > 1) result.append('/')
      result.append(nums(i))
      i += 1
    }
    result.append(')')
    result.toString
  }
}
"""

FILES["0554_brick_wall"] = """// LeetCode 0554 - Brick Wall
// https://leetcode.com/problems/brick-wall/

import scala.collection.mutable

object Solution {
  def leastBricks(wall: List[List[Int]]): Int = {
    val edges = mutable.Map.empty[Int, Int]
    var best = 0
    wall.foreach { row =>
      var width = 0
      var i = 0
      while (i + 1 < row.size) {
        width += row(i)
        val count = edges.getOrElse(width, 0) + 1
        edges(width) = count
        best = math.max(best, count)
        i += 1
      }
    }
    wall.size - best
  }
}
"""

FILES["0555_split_concatenated_strings"] = """// LeetCode 0555 - Split Concatenated Strings
// https://leetcode.com/problems/split-concatenated-strings/

object Solution {
  def splitLoopedString(strs: Array[String]): String = {
    val bestForms = strs.map { s =>
      val rev = s.reverse
      if (s.compareTo(rev) >= 0) s else rev
    }
    var answer = ""
    for (i <- strs.indices) {
      val midBuilder = new StringBuilder
      var j = i + 1
      while (j < strs.length) { midBuilder.append(bestForms(j)); j += 1 }
      j = 0
      while (j < i) { midBuilder.append(bestForms(j)); j += 1 }
      val mid = midBuilder.toString
      val original = strs(i)
      val reversed = original.reverse
      for (candidate <- Array(original, reversed)) {
        var cut = 0
        while (cut < candidate.length) {
          val formed = candidate.substring(cut) + mid + candidate.substring(0, cut)
          if (formed.compareTo(answer) > 0) answer = formed
          cut += 1
        }
      }
    }
    answer
  }
}
"""

FILES["0556_next_greater_element_iii"] = """// LeetCode 0556 - Next Greater Element III
// https://leetcode.com/problems/next-greater-element-iii/

object Solution {
  def nextGreaterElement(n: Int): Int = {
    val digits = n.toString.toCharArray
    var i = digits.length - 2
    while (i >= 0 && digits(i) >= digits(i + 1)) i -= 1
    if (i < 0) return -1
    var j = digits.length - 1
    while (digits(j) <= digits(i)) j -= 1
    val tmp = digits(i)
    digits(i) = digits(j)
    digits(j) = tmp
    reverse(digits, i + 1, digits.length - 1)
    var value = 0L
    digits.foreach(ch => value = value * 10 + (ch - '0'))
    if (value > Int.MaxValue) -1 else value.toInt
  }

  private def reverse(digits: Array[Char], left0: Int, right0: Int): Unit = {
    var left = left0
    var right = right0
    while (left < right) {
      val tmp = digits(left)
      digits(left) = digits(right)
      digits(right) = tmp
      left += 1
      right -= 1
    }
  }
}
"""

FILES["0557_reverse_words_in_a_string_iii"] = """// LeetCode 0557 - Reverse Words in a String III
// https://leetcode.com/problems/reverse-words-in-a-string-iii/

object Solution {
  def reverseWords(s: String): String = {
    val chars = s.toCharArray
    val n = chars.length
    var start = 0
    var i = 0
    while (i <= n) {
      if (i == n || chars(i) == ' ') {
        reverse(chars, start, i - 1)
        start = i + 1
      }
      i += 1
    }
    new String(chars)
  }

  private def reverse(chars: Array[Char], left0: Int, right0: Int): Unit = {
    var left = left0
    var right = right0
    while (left < right) {
      val tmp = chars(left)
      chars(left) = chars(right)
      chars(right) = tmp
      left += 1
      right -= 1
    }
  }
}
"""

FILES["0558_logical_or_of_two_binary_grids_represented_as_quad_trees"] = f"""// LeetCode 0558 - Logical OR of Two Binary Grids Represented as Quad-Trees
// https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

{QUAD}
object Solution {{
  def intersect(quadTree1: Node, quadTree2: Node): Node = {{
    if (quadTree1.isLeaf) {{
      if (quadTree1.value) quadTree1 else quadTree2
    }} else if (quadTree2.isLeaf) {{
      if (quadTree2.value) quadTree2 else quadTree1
    }} else {{
      val topLeft = intersect(quadTree1.topLeft, quadTree2.topLeft)
      val topRight = intersect(quadTree1.topRight, quadTree2.topRight)
      val bottomLeft = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
      val bottomRight = intersect(quadTree1.bottomRight, quadTree2.bottomRight)
      if (topLeft.isLeaf && topRight.isLeaf && bottomLeft.isLeaf && bottomRight.isLeaf
          && topLeft.value == topRight.value && topRight.value == bottomLeft.value
          && bottomLeft.value == bottomRight.value) {{
        new Node(topLeft.value, true)
      }} else {{
        new Node(false, false, topLeft, topRight, bottomLeft, bottomRight)
      }}
    }}
  }}
}}
"""

FILES["0559_maximum_depth_of_n_ary_tree"] = f"""// LeetCode 0559 - Maximum Depth of N-ary Tree
// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

{NARY}
object Solution {{
  def maxDepth(root: Node): Int = {{
    if (root == null) return 0
    if (root.children == null || root.children.isEmpty) return 1
    var best = 0
    root.children.foreach {{ child =>
      best = math.max(best, maxDepth(child))
    }}
    best + 1
  }}
}}
"""

FILES["0560_subarray_sum_equals_k"] = """// LeetCode 0560 - Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/

import scala.collection.mutable

object Solution {
  def subarraySum(nums: Array[Int], k: Int): Int = {
    val counts = mutable.Map[Int, Int](0 -> 1)
    var prefix = 0
    var answer = 0
    nums.foreach { num =>
      prefix += num
      answer += counts.getOrElse(prefix - k, 0)
      counts(prefix) = counts.getOrElse(prefix, 0) + 1
    }
    answer
  }
}
"""

FILES["0561_array_partition"] = """// LeetCode 0561 - Array Partition
// https://leetcode.com/problems/array-partition/

object Solution {
  def arrayPairSum(nums: Array[Int]): Int = {
    val sorted = nums.sorted
    var total = 0
    var i = 0
    while (i < sorted.length) {
      total += sorted(i)
      i += 2
    }
    total
  }
}
"""

FILES["0562_longest_line_of_consecutive_one_in_matrix"] = """// LeetCode 0562 - Longest Line of Consecutive One in Matrix
// https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

object Solution {
  def longestLine(mat: Array[Array[Int]]): Int = {
    if (mat.isEmpty || mat(0).isEmpty) return 0
    val rows = mat.length
    val cols = mat(0).length
    val dp = Array.ofDim[Int](rows, cols, 4)
    var best = 0
    for (r <- 0 until rows; c <- 0 until cols if mat(r)(c) != 0) {
      dp(r)(c)(0) = (if (c > 0) dp(r)(c - 1)(0) else 0) + 1
      dp(r)(c)(1) = (if (r > 0) dp(r - 1)(c)(1) else 0) + 1
      dp(r)(c)(2) = (if (r > 0 && c > 0) dp(r - 1)(c - 1)(2) else 0) + 1
      dp(r)(c)(3) = (if (r > 0 && c + 1 < cols) dp(r - 1)(c + 1)(3) else 0) + 1
      var d = 0
      while (d < 4) {
        best = math.max(best, dp(r)(c)(d))
        d += 1
      }
    }
    best
  }
}
"""

FILES["0563_binary_tree_tilt"] = f"""// LeetCode 0563 - Binary Tree Tilt
// https://leetcode.com/problems/binary-tree-tilt/

{TREE}
object Solution {{
  def findTilt(root: TreeNode): Int = {{
    var total = 0
    def subtreeSum(node: TreeNode): Int = {{
      if (node == null) return 0
      val left = subtreeSum(node.left)
      val right = subtreeSum(node.right)
      total += math.abs(left - right)
      node.value + left + right
    }}
    subtreeSum(root)
    total
  }}
}}
"""

FILES["0564_find_the_closest_palindrome"] = """// LeetCode 0564 - Find the Closest Palindrome
// https://leetcode.com/problems/find-the-closest-palindrome/

import scala.collection.mutable

object Solution {
  def nearestPalindromic(n: String): String = {
    val length = n.length
    val number = n.toLong
    val candidates = mutable.ArrayBuffer[Long]()
    candidates += pow10(length - 1) - 1
    candidates += pow10(length) + 1
    val prefix = n.substring(0, (length + 1) / 2).toLong
    var half = prefix - 1
    while (half <= prefix + 1) {
      candidates += makePalindrome(half, length)
      half += 1
    }
    var best = -1L
    var bestDiff = Long.MaxValue
    candidates.foreach { candidate =>
      if (candidate != number) {
        val diff = math.abs(candidate - number)
        if (diff < bestDiff || (diff == bestDiff && candidate < best)) {
          best = candidate
          bestDiff = diff
        }
      }
    }
    best.toString
  }

  private def makePalindrome(half: Long, length: Int): Long = {
    val text = half.toString
    val pal = new StringBuilder(text)
    if (length % 2 == 0) {
      var i = text.length - 1
      while (i >= 0) { pal.append(text.charAt(i)); i -= 1 }
    } else {
      var i = text.length - 2
      while (i >= 0) { pal.append(text.charAt(i)); i -= 1 }
    }
    pal.toString.toLong
  }

  private def pow10(exp: Int): Long = {
    var value = 1L
    var i = 0
    while (i < exp) { value *= 10; i += 1 }
    value
  }
}
"""

FILES["0565_array_nesting"] = """// LeetCode 0565 - Array Nesting
// https://leetcode.com/problems/array-nesting/

object Solution {
  def arrayNesting(nums: Array[Int]): Int = {
    var best = 0
    var i = 0
    while (i < nums.length) {
      if (nums(i) >= 0) {
        var length = 0
        var j = i
        while (nums(j) >= 0) {
          val nxt = nums(j)
          nums(j) = -1
          j = nxt
          length += 1
        }
        best = math.max(best, length)
      }
      i += 1
    }
    best
  }
}
"""

FILES["0566_reshape_the_matrix"] = """// LeetCode 0566 - Reshape the Matrix
// https://leetcode.com/problems/reshape-the-matrix/

object Solution {
  def matrixReshape(mat: Array[Array[Int]], r: Int, c: Int): Array[Array[Int]] = {
    val rows = mat.length
    val cols = mat(0).length
    if (rows * cols != r * c) return mat
    val result = Array.ofDim[Int](r, c)
    var index = 0
    var i = 0
    while (i < r) {
      var j = 0
      while (j < c) {
        result(i)(j) = mat(index / cols)(index % cols)
        index += 1
        j += 1
      }
      i += 1
    }
    result
  }
}
"""

FILES["0567_permutation_in_string"] = """// LeetCode 0567 - Permutation in String
// https://leetcode.com/problems/permutation-in-string/

object Solution {
  def checkInclusion(s1: String, s2: String): Boolean = {
    val n1 = s1.length
    val n2 = s2.length
    if (n1 > n2) return false
    val need = Array.fill(26)(0)
    val window = Array.fill(26)(0)
    var i = 0
    while (i < n1) {
      need(s1.charAt(i) - 'a') += 1
      window(s2.charAt(i) - 'a') += 1
      i += 1
    }
    var matches = 0
    i = 0
    while (i < 26) {
      if (need(i) == window(i)) matches += 1
      i += 1
    }
    if (matches == 26) return true
    var right = n1
    while (right < n2) {
      val add = s2.charAt(right) - 'a'
      val remove = s2.charAt(right - n1) - 'a'
      if (window(add) == need(add)) matches -= 1
      window(add) += 1
      if (window(add) == need(add)) matches += 1
      if (window(remove) == need(remove)) matches -= 1
      window(remove) -= 1
      if (window(remove) == need(remove)) matches += 1
      if (matches == 26) return true
      right += 1
    }
    false
  }
}
"""

FILES["0568_maximum_vacation_days"] = """// LeetCode 0568 - Maximum Vacation Days
// https://leetcode.com/problems/maximum-vacation-days/

object Solution {
  def maxVacationDays(flights: Array[Array[Int]], days: Array[Array[Int]]): Int = {
    val cities = flights.length
    val weeks = days(0).length
    val NEG = -1000000000
    var dp = Array.fill(cities)(NEG)
    dp(0) = 0
    var week = 0
    while (week < weeks) {
      val nxt = Array.fill(cities)(NEG)
      var city = 0
      while (city < cities) {
        if (dp(city) != NEG) {
          var dest = 0
          while (dest < cities) {
            if (dest == city || flights(city)(dest) == 1) {
              nxt(dest) = math.max(nxt(dest), dp(city) + days(dest)(week))
            }
            dest += 1
          }
        }
        city += 1
      }
      dp = nxt
      week += 1
    }
    var best = NEG
    dp.foreach(v => best = math.max(best, v))
    best
  }
}
"""

FILES["0572_subtree_of_another_tree"] = f"""// LeetCode 0572 - Subtree of Another Tree
// https://leetcode.com/problems/subtree-of-another-tree/

{TREE}
object Solution {{
  def isSubtree(root: TreeNode, subRoot: TreeNode): Boolean = {{
    if (root == null) return false
    same(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
  }}

  private def same(a: TreeNode, b: TreeNode): Boolean = {{
    if (a == null || b == null) return a == b
    a.value == b.value && same(a.left, b.left) && same(a.right, b.right)
  }}
}}
"""

FILES["0573_squirrel_simulation"] = """// LeetCode 0573 - Squirrel Simulation
// https://leetcode.com/problems/squirrel-simulation/

object Solution {
  def minDistance(height: Int, width: Int, tree: Array[Int], squirrel: Array[Int], nuts: Array[Array[Int]]): Int = {
    var total = 0
    var bestSave = Int.MinValue
    nuts.foreach { nut =>
      val treeDist = dist(tree, nut)
      val squirrelDist = dist(squirrel, nut)
      total += 2 * treeDist
      val save = treeDist - squirrelDist
      if (save > bestSave) bestSave = save
    }
    total - bestSave
  }

  private def dist(a: Array[Int], b: Array[Int]): Int =
    math.abs(a(0) - b(0)) + math.abs(a(1) - b(1))
}
"""

FILES["0575_distribute_candies"] = """// LeetCode 0575 - Distribute Candies
// https://leetcode.com/problems/distribute-candies/

object Solution {
  def distributeCandies(candyType: Array[Int]): Int = {
    val unique = candyType.toSet
    math.min(unique.size, candyType.length / 2)
  }
}
"""

FILES["0576_out_of_boundary_paths"] = """// LeetCode 0576 - Out of Boundary Paths
// https://leetcode.com/problems/out-of-boundary-paths/

object Solution {
  def findPaths(m: Int, n: Int, maxMove: Int, startRow: Int, startColumn: Int): Int = {
    val MOD = 1000000007
    var dp = Array.ofDim[Int](m, n)
    dp(startRow)(startColumn) = 1
    var result = 0
    val dirs = Array((0, 1), (0, -1), (1, 0), (-1, 0))
    var move = 0
    while (move < maxMove) {
      val nxt = Array.ofDim[Int](m, n)
      var row = 0
      while (row < m) {
        var col = 0
        while (col < n) {
          val ways = dp(row)(col)
          if (ways != 0) {
            dirs.foreach { case (dr, dc) =>
              val nr = row + dr
              val nc = col + dc
              if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                nxt(nr)(nc) = (nxt(nr)(nc) + ways) % MOD
              } else {
                result = (result + ways) % MOD
              }
            }
          }
          col += 1
        }
        row += 1
      }
      dp = nxt
      move += 1
    }
    result
  }
}
"""

FILES["0581_shortest_unsorted_continuous_subarray"] = """// LeetCode 0581 - Shortest Unsorted Continuous Subarray
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

object Solution {
  def findUnsortedSubarray(nums: Array[Int]): Int = {
    val n = nums.length
    var left = -1
    var right = -2
    var maxSeen = nums(0)
    var minSeen = nums(n - 1)
    var i = 0
    while (i < n) {
      maxSeen = math.max(maxSeen, nums(i))
      if (nums(i) < maxSeen) right = i
      val j = n - 1 - i
      minSeen = math.min(minSeen, nums(j))
      if (nums(j) > minSeen) left = j
      i += 1
    }
    right - left + 1
  }
}
"""

FILES["0582_kill_process"] = """// LeetCode 0582 - Kill Process
// https://leetcode.com/problems/kill-process/

import scala.collection.mutable

object Solution {
  def killProcess(pid: List[Int], ppid: List[Int], kill: Int): List[Int] = {
    val children = mutable.Map.empty[Int, mutable.ArrayBuffer[Int]]
    var i = 0
    while (i < pid.size) {
      children.getOrElseUpdate(ppid(i), mutable.ArrayBuffer.empty[Int]) += pid(i)
      i += 1
    }
    val result = mutable.ArrayBuffer.empty[Int]
    val queue = mutable.Queue[Int](kill)
    while (queue.nonEmpty) {
      val process = queue.dequeue()
      result += process
      children.get(process).foreach(_.foreach(queue.enqueue))
    }
    result.toList
  }
}
"""

FILES["0583_delete_operation_for_two_strings"] = """// LeetCode 0583 - Delete Operation for Two Strings
// https://leetcode.com/problems/delete-operation-for-two-strings/

object Solution {
  def minDistance(word1: String, word2: String): Int = {
    val m = word1.length
    val n = word2.length
    var prev = Array.fill(n + 1)(0)
    var curr = Array.fill(n + 1)(0)
    var i = 1
    while (i <= m) {
      var j = 1
      while (j <= n) {
        if (word1.charAt(i - 1) == word2.charAt(j - 1)) curr(j) = prev(j - 1) + 1
        else curr(j) = math.max(prev(j), curr(j - 1))
        j += 1
      }
      val tmp = prev
      prev = curr
      curr = tmp
      j = 0
      while (j <= n) { curr(j) = 0; j += 1 }
      i += 1
    }
    m + n - 2 * prev(n)
  }
}
"""

FILES["0587_erect_the_fence"] = """// LeetCode 0587 - Erect the Fence
// https://leetcode.com/problems/erect-the-fence/

import scala.collection.mutable

object Solution {
  def outerTrees(trees: Array[Array[Int]]): Array[Array[Int]] = {
    val points = trees.sortBy(p => (p(0), p(1)))
    if (points.length <= 1) return points
    val lower = build(points)
    val reversed = points.reverse
    val upper = build(reversed)
    val seen = mutable.Set.empty[String]
    val unique = mutable.ArrayBuffer.empty[Array[Int]]
    var i = 0
    while (i + 1 < lower.size) { addUnique(unique, seen, lower(i)); i += 1 }
    i = 0
    while (i + 1 < upper.size) { addUnique(unique, seen, upper(i)); i += 1 }
    unique.toArray
  }

  private def build(ordered: Array[Array[Int]]): mutable.ArrayBuffer[Array[Int]] = {
    val hull = mutable.ArrayBuffer.empty[Array[Int]]
    ordered.foreach { point =>
      while (hull.size >= 2 && cross(hull(hull.size - 2), hull(hull.size - 1), point) < 0) {
        hull.remove(hull.size - 1)
      }
      hull += point
    }
    hull
  }

  private def cross(o: Array[Int], a: Array[Int], b: Array[Int]): Long =
    1L * (a(0) - o(0)) * (b(1) - o(1)) - 1L * (a(1) - o(1)) * (b(0) - o(0))

  private def addUnique(unique: mutable.ArrayBuffer[Array[Int]], seen: mutable.Set[String], point: Array[Int]): Unit = {
    val key = s"${point(0)},${point(1)}"
    if (seen.add(key)) unique += point
  }
}
"""

FILES["0588_design_in_memory_file_system"] = """// LeetCode 0588 - Design In-Memory File System
// https://leetcode.com/problems/design-in-memory-file-system/

import scala.collection.mutable

class FileSystem() {
  private class Node {
    var isFile = false
    var content = ""
    val children = mutable.TreeMap.empty[String, Node]
  }

  private val root = new Node()

  def ls(path: String): List[String] = {
    if (path == "/") return root.children.keys.toList
    val parts = split(path)
    var node = root
    parts.foreach(part => node = node.children(part))
    if (node.isFile) List(parts.last)
    else node.children.keys.toList
  }

  def mkdir(path: String): Unit = {
    var node = root
    split(path).foreach { part =>
      if (!node.children.contains(part)) node.children(part) = new Node()
      node = node.children(part)
    }
  }

  def addContentToFile(filePath: String, content: String): Unit = {
    val parts = split(filePath)
    var node = root
    var i = 0
    while (i + 1 < parts.size) {
      if (!node.children.contains(parts(i))) node.children(parts(i)) = new Node()
      node = node.children(parts(i))
      i += 1
    }
    val name = parts.last
    if (!node.children.contains(name)) node.children(name) = new Node()
    val file = node.children(name)
    file.isFile = true
    file.content += content
  }

  def readContentFromFile(filePath: String): String = {
    var node = root
    split(filePath).foreach(part => node = node.children(part))
    node.content
  }

  private def split(path: String): List[String] =
    path.split("/").filter(_.nonEmpty).toList
}
"""

FILES["0589_n_ary_tree_preorder_traversal"] = f"""// LeetCode 0589 - N-ary Tree Preorder Traversal
// https://leetcode.com/problems/n-ary-tree-preorder-traversal/

import scala.collection.mutable

{NARY}
object Solution {{
  def preorder(root: Node): List[Int] = {{
    val result = mutable.ArrayBuffer.empty[Int]
    dfs(root, result)
    result.toList
  }}

  private def dfs(node: Node, result: mutable.ArrayBuffer[Int]): Unit = {{
    if (node == null) return
    result += node.value
    if (node.children != null) node.children.foreach(child => dfs(child, result))
  }}
}}
"""

FILES["0590_n_ary_tree_postorder_traversal"] = f"""// LeetCode 0590 - N-ary Tree Postorder Traversal
// https://leetcode.com/problems/n-ary-tree-postorder-traversal/

import scala.collection.mutable

{NARY}
object Solution {{
  def postorder(root: Node): List[Int] = {{
    val result = mutable.ArrayBuffer.empty[Int]
    dfs(root, result)
    result.toList
  }}

  private def dfs(node: Node, result: mutable.ArrayBuffer[Int]): Unit = {{
    if (node == null) return
    if (node.children != null) node.children.foreach(child => dfs(child, result))
    result += node.value
  }}
}}
"""

FILES["0591_tag_validator"] = """// LeetCode 0591 - Tag Validator
// https://leetcode.com/problems/tag-validator/

import scala.collection.mutable

object Solution {
  def isValid(code: String): Boolean = {
    val stack = mutable.ArrayBuffer.empty[String]
    var i = 0
    val n = code.length
    while (i < n) {
      if (code.startsWith("<![CDATA[", i)) {
        if (stack.isEmpty) return false
        val j = code.indexOf("]]>", i + 9)
        if (j < 0) return false
        i = j + 3
      } else if (code.startsWith("</", i)) {
        val j = code.indexOf('>', i + 2)
        if (j < 0) return false
        val tag = code.substring(i + 2, j)
        if (stack.isEmpty || stack.last != tag) return false
        stack.remove(stack.size - 1)
        i = j + 1
        if (stack.isEmpty && i < n) return false
      } else if (code.charAt(i) == '<') {
        val j = code.indexOf('>', i + 1)
        if (j < 0) return false
        val tag = code.substring(i + 1, j)
        if (tag.isEmpty || tag.length > 9) return false
        var k = 0
        while (k < tag.length) {
          val ch = tag.charAt(k)
          if (ch < 'A' || ch > 'Z') return false
          k += 1
        }
        stack += tag
        i = j + 1
      } else {
        if (stack.isEmpty) return false
        i += 1
      }
    }
    stack.isEmpty
  }
}
"""

FILES["0592_fraction_addition_and_subtraction"] = """// LeetCode 0592 - Fraction Addition and Subtraction
// https://leetcode.com/problems/fraction-addition-and-subtraction/

object Solution {
  def fractionAddition(expression: String): String = {
    var numerator = 0L
    var denominator = 1L
    var i = 0
    val len = expression.length
    while (i < len) {
      var sign = 1
      if (expression.charAt(i) == '+' || expression.charAt(i) == '-') {
        if (expression.charAt(i) == '-') sign = -1
        i += 1
      }
      var a = 0L
      while (i < len && expression.charAt(i) >= '0' && expression.charAt(i) <= '9') {
        a = a * 10 + (expression.charAt(i) - '0')
        i += 1
      }
      a *= sign
      i += 1
      var b = 0L
      while (i < len && expression.charAt(i) >= '0' && expression.charAt(i) <= '9') {
        b = b * 10 + (expression.charAt(i) - '0')
        i += 1
      }
      numerator = numerator * b + a * denominator
      denominator *= b
      val g = gcd(math.abs(numerator), math.abs(denominator))
      numerator /= g
      denominator /= g
    }
    s"$numerator/$denominator"
  }

  private def gcd(a0: Long, b0: Long): Long = {
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

FILES["0593_valid_square"] = """// LeetCode 0593 - Valid Square
// https://leetcode.com/problems/valid-square/

object Solution {
  def validSquare(p1: Array[Int], p2: Array[Int], p3: Array[Int], p4: Array[Int]): Boolean = {
    val points = Array(p1, p2, p3, p4)
    val distances = Array.fill(6)(0)
    var idx = 0
    var i = 0
    while (i < 4) {
      var j = i + 1
      while (j < 4) {
        distances(idx) = distSq(points(i), points(j))
        idx += 1
        j += 1
      }
      i += 1
    }
    scala.util.Sorting.quickSort(distances)
    distances(0) > 0 && distances(0) == distances(1) && distances(1) == distances(2) &&
      distances(2) == distances(3) && distances(4) == distances(5) &&
      distances(4) == 2 * distances(0)
  }

  private def distSq(a: Array[Int], b: Array[Int]): Int = {
    val dx = a(0) - b(0)
    val dy = a(1) - b(1)
    dx * dx + dy * dy
  }
}
"""

FILES["0594_longest_harmonious_subsequence"] = """// LeetCode 0594 - Longest Harmonious Subsequence
// https://leetcode.com/problems/longest-harmonious-subsequence/

import scala.collection.mutable

object Solution {
  def findLHS(nums: Array[Int]): Int = {
    val counts = mutable.Map.empty[Int, Int]
    nums.foreach(num => counts(num) = counts.getOrElse(num, 0) + 1)
    var best = 0
    counts.foreach { case (key, value) =>
      counts.get(key + 1).foreach { nxt =>
        best = math.max(best, value + nxt)
      }
    }
    best
  }
}
"""

FILES["0598_range_addition_ii"] = """// LeetCode 0598 - Range Addition II
// https://leetcode.com/problems/range-addition-ii/

object Solution {
  def maxCount(m0: Int, n0: Int, ops: Array[Array[Int]]): Int = {
    var m = m0
    var n = n0
    ops.foreach { op =>
      m = math.min(m, op(0))
      n = math.min(n, op(1))
    }
    m * n
  }
}
"""

FILES["0599_minimum_index_sum_of_two_lists"] = """// LeetCode 0599 - Minimum Index Sum of Two Lists
// https://leetcode.com/problems/minimum-index-sum-of-two-lists/

import scala.collection.mutable

object Solution {
  def findRestaurant(list1: Array[String], list2: Array[String]): Array[String] = {
    val index1 = mutable.Map.empty[String, Int]
    var i = 0
    while (i < list1.length) { index1(list1(i)) = i; i += 1 }
    var best = Int.MaxValue
    val answer = mutable.ArrayBuffer.empty[String]
    var j = 0
    while (j < list2.length) {
      index1.get(list2(j)).foreach { i1 =>
        val total = i1 + j
        if (total < best) {
          best = total
          answer.clear()
          answer += list2(j)
        } else if (total == best) {
          answer += list2(j)
        }
      }
      j += 1
    }
    answer.toArray
  }
}
"""

FILES["0600_non_negative_integers_without_consecutive_ones"] = """// LeetCode 0600 - Non-negative Integers without Consecutive Ones
// https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

object Solution {
  def findIntegers(n: Int): Int = {
    val fib = Array.fill(32)(0)
    fib(0) = 1
    fib(1) = 2
    var i = 2
    while (i < 32) { fib(i) = fib(i - 1) + fib(i - 2); i += 1 }
    var answer = 0
    var prevBit = 0
    var bit = 30
    while (bit >= 0) {
      if ((n & (1 << bit)) != 0) {
        answer += fib(bit)
        if (prevBit == 1) return answer
        prevBit = 1
      } else {
        prevBit = 0
      }
      bit -= 1
    }
    answer + 1
  }
}
"""

FILES["0604_design_compressed_string_iterator"] = """// LeetCode 0604 - Design Compressed String Iterator
// https://leetcode.com/problems/design-compressed-string-iterator/

import scala.collection.mutable

class StringIterator(compressedString: String) {
  private val chars = mutable.ArrayBuffer.empty[Char]
  private val counts = mutable.ArrayBuffer.empty[Int]
  private var index = 0

  {
    val n = compressedString.length
    var i = 0
    while (i < n) {
      val ch = compressedString.charAt(i)
      i += 1
      var j = i
      while (j < n && compressedString.charAt(j) >= '0' && compressedString.charAt(j) <= '9') j += 1
      chars += ch
      counts += compressedString.substring(i, j).toInt
      i = j
    }
  }

  def next(): Char = {
    if (!hasNext()) return ' '
    val ch = chars(index)
    counts(index) -= 1
    if (counts(index) == 0) index += 1
    ch
  }

  def hasNext(): Boolean = index < chars.size
}
"""

FILES["0605_can_place_flowers"] = """// LeetCode 0605 - Can Place Flowers
// https://leetcode.com/problems/can-place-flowers/

object Solution {
  def canPlaceFlowers(flowerbed: Array[Int], n0: Int): Boolean = {
    var n = n0
    if (n == 0) return true
    var i = 0
    while (i < flowerbed.length) {
      if (flowerbed(i) != 1) {
        val leftEmpty = i == 0 || flowerbed(i - 1) == 0
        val rightEmpty = i == flowerbed.length - 1 || flowerbed(i + 1) == 0
        if (leftEmpty && rightEmpty) {
          flowerbed(i) = 1
          n -= 1
          if (n == 0) return true
        }
      }
      i += 1
    }
    false
  }
}
"""

FILES["0606_construct_string_from_binary_tree"] = f"""// LeetCode 0606 - Construct String from Binary Tree
// https://leetcode.com/problems/construct-string-from-binary-tree/

{TREE}
object Solution {{
  def tree2str(root: TreeNode): String = {{
    if (root == null) return ""
    var result = root.value.toString
    if (root.left != null || root.right != null) result += "(" + tree2str(root.left) + ")"
    if (root.right != null) result += "(" + tree2str(root.right) + ")"
    result
  }}
}}
"""

FILES["0609_find_duplicate_file_in_system"] = """// LeetCode 0609 - Find Duplicate File in System
// https://leetcode.com/problems/find-duplicate-file-in-system/

import scala.collection.mutable

object Solution {
  def findDuplicate(paths: Array[String]): List[List[String]] = {
    val contentToPaths = mutable.Map.empty[String, mutable.ArrayBuffer[String]]
    paths.foreach { entry =>
      val tokens = entry.split(" ")
      val directory = tokens(0)
      var i = 1
      while (i < tokens.length) {
        val fileInfo = tokens(i)
        val open = fileInfo.indexOf('(')
        val name = fileInfo.substring(0, open)
        val content = fileInfo.substring(open + 1, fileInfo.length - 1)
        contentToPaths.getOrElseUpdate(content, mutable.ArrayBuffer.empty[String]) += (directory + "/" + name)
        i += 1
      }
    }
    val result = mutable.ArrayBuffer.empty[List[String]]
    contentToPaths.values.foreach { group =>
      if (group.size > 1) result += group.toList
    }
    result.toList
  }
}
"""

FILES["0611_valid_triangle_number"] = """// LeetCode 0611 - Valid Triangle Number
// https://leetcode.com/problems/valid-triangle-number/

object Solution {
  def triangleNumber(nums: Array[Int]): Int = {
    scala.util.Sorting.quickSort(nums)
    val n = nums.length
    var count = 0
    var k = n - 1
    while (k >= 2) {
      var left = 0
      var right = k - 1
      while (left < right) {
        if (nums(left) + nums(right) > nums(k)) {
          count += right - left
          right -= 1
        } else {
          left += 1
        }
      }
      k -= 1
    }
    count
  }
}
"""

FILES["0616_add_bold_tag_in_string"] = """// LeetCode 0616 - Add Bold Tag in String
// https://leetcode.com/problems/add-bold-tag-in-string/

object Solution {
  def addBoldTag(s: String, words: Array[String]): String = {
    val n = s.length
    val bold = Array.fill(n)(false)
    words.foreach { word =>
      var start = s.indexOf(word)
      while (start >= 0) {
        var i = start
        while (i < start + word.length) { bold(i) = true; i += 1 }
        start = s.indexOf(word, start + 1)
      }
    }
    val parts = new StringBuilder
    var i = 0
    while (i < n) {
      if (bold(i)) {
        parts.append("<b>")
        while (i < n && bold(i)) { parts.append(s.charAt(i)); i += 1 }
        parts.append("</b>")
      } else {
        parts.append(s.charAt(i))
        i += 1
      }
    }
    parts.toString
  }
}
"""

FILES["0617_merge_two_binary_trees"] = f"""// LeetCode 0617 - Merge Two Binary Trees
// https://leetcode.com/problems/merge-two-binary-trees/

{TREE}
object Solution {{
  def mergeTrees(root1: TreeNode, root2: TreeNode): TreeNode = {{
    if (root1 == null) return root2
    if (root2 == null) return root1
    root1.value += root2.value
    root1.left = mergeTrees(root1.left, root2.left)
    root1.right = mergeTrees(root1.right, root2.right)
    root1
  }}
}}
"""


def main() -> None:
    written = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "Solution.scala"
        path.write_text(content.lstrip("\n") if False else content, encoding="utf-8", newline="\n")
        # strip BOM if any
        text = path.read_text(encoding="utf-8-sig")
        if text.startswith("\ufeff"):
            text = text[1:]
        path.write_text(text, encoding="utf-8", newline="\n")
        written += 1
        print("wrote", folder)
    print("TOTAL", written)


if __name__ == "__main__":
    main()
