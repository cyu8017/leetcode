#!/usr/bin/env python3
"""Write Scala Solution.scala files for batch_00 problems 0651-0679."""
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

TREE = """class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}
"""

FILES = {}

FILES["0651_4_keys_keyboard"] = """// LeetCode 0651 - 4 Keys Keyboard
// https://leetcode.com/problems/4-keys-keyboard/

object Solution {
  def maxA(n: Int): Int = {
    val dp = Array.tabulate(n + 1)(identity)
    var i = 1
    while (i <= n) {
      var j = 0
      while (j < i - 2) {
        dp(i) = math.max(dp(i), dp(j) * (i - j - 1))
        j += 1
      }
      i += 1
    }
    dp(n)
  }
}
"""

FILES["0652_find_duplicate_subtrees"] = f"""// LeetCode 0652 - Find Duplicate Subtrees
// https://leetcode.com/problems/find-duplicate-subtrees/

import scala.collection.mutable

{TREE}
object Solution {{
  def findDuplicateSubtrees(root: TreeNode): List[TreeNode] = {{
    val counts = mutable.Map.empty[String, Int]
    val result = mutable.ArrayBuffer.empty[TreeNode]
    def serialize(node: TreeNode): String = {{
      if (node == null) return "#"
      val key = node.value + "," + serialize(node.left) + "," + serialize(node.right)
      val count = counts.getOrElse(key, 0) + 1
      counts(key) = count
      if (count == 2) result += node
      key
    }}
    serialize(root)
    result.toList
  }}
}}
"""

FILES["0653_two_sum_iv_input_is_a_bst"] = f"""// LeetCode 0653 - Two Sum IV - Input is a BST
// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

import scala.collection.mutable

{TREE}
object Solution {{
  def findTarget(root: TreeNode, k: Int): Boolean = {{
    val seen = mutable.Set.empty[Int]
    def dfs(node: TreeNode): Boolean = {{
      if (node == null) return false
      if (seen.contains(k - node.value)) return true
      seen += node.value
      dfs(node.left) || dfs(node.right)
    }}
    dfs(root)
  }}
}}
"""

FILES["0654_maximum_binary_tree"] = f"""// LeetCode 0654 - Maximum Binary Tree
// https://leetcode.com/problems/maximum-binary-tree/

{TREE}
object Solution {{
  def constructMaximumBinaryTree(nums: Array[Int]): TreeNode = {{
    def build(left: Int, right: Int): TreeNode = {{
      if (left > right) return null
      var mid = left
      var i = left
      while (i <= right) {{
        if (nums(i) > nums(mid)) mid = i
        i += 1
      }}
      new TreeNode(nums(mid), build(left, mid - 1), build(mid + 1, right))
    }}
    build(0, nums.length - 1)
  }}
}}
"""

FILES["0655_print_binary_tree"] = f"""// LeetCode 0655 - Print Binary Tree
// https://leetcode.com/problems/print-binary-tree/

import scala.collection.mutable

{TREE}
object Solution {{
  def printTree(root: TreeNode): List[List[String]] = {{
    val h = height(root)
    val rows = h + 1
    val cols = (1 << (h + 1)) - 1
    val res = mutable.ArrayBuffer.fill(rows)(mutable.ArrayBuffer.fill(cols)(""))
    place(root, 0, (cols - 1) / 2, h, res)
    res.map(_.toList).toList
  }}

  private def height(node: TreeNode): Int = {{
    if (node == null) return -1
    1 + math.max(height(node.left), height(node.right))
  }}

  private def place(
    node: TreeNode,
    r: Int,
    c: Int,
    h: Int,
    res: mutable.ArrayBuffer[mutable.ArrayBuffer[String]],
  ): Unit = {{
    if (node == null) return
    res(r)(c) = node.value.toString
    if (r == h) return
    val offset = 1 << (h - r - 1)
    place(node.left, r + 1, c - offset, h, res)
    place(node.right, r + 1, c + offset, h, res)
  }}
}}
"""

FILES["0656_coin_path"] = """// LeetCode 0656 - Coin Path
// https://leetcode.com/problems/coin-path/

import scala.collection.mutable

object Solution {
  def cheapestJump(coins: Array[Int], maxJump: Int): List[Int] = {
    val n = coins.length
    if (coins(n - 1) == -1) return List.empty
    val inf = Long.MaxValue / 4
    val cost = Array.fill(n)(inf)
    val nxt = Array.fill(n)(-1)
    cost(n - 1) = coins(n - 1)
    var i = n - 2
    while (i >= 0) {
      if (coins(i) != -1) {
        var jump = 1
        while (jump <= maxJump) {
          val j = i + jump
          if (j >= n) jump = maxJump + 1
          else {
            if (cost(j) != inf) {
              val candidate = coins(i) + cost(j)
              if (candidate < cost(i) || (candidate == cost(i) && (nxt(i) == -1 || j < nxt(i)))) {
                cost(i) = candidate
                nxt(i) = j
              }
            }
            jump += 1
          }
        }
      }
      i -= 1
    }
    if (cost(0) == inf) return List.empty
    val path = mutable.ArrayBuffer(1)
    i = 0
    while (i != n - 1) {
      i = nxt(i)
      path += i + 1
    }
    path.toList
  }
}
"""

FILES["0657_robot_return_to_origin"] = """// LeetCode 0657 - Robot Return to Origin
// https://leetcode.com/problems/robot-return-to-origin/

object Solution {
  def judgeCircle(moves: String): Boolean = {
    var x = 0
    var y = 0
    var i = 0
    while (i < moves.length) {
      val move = moves.charAt(i)
      if (move == 'U') y += 1
      else if (move == 'D') y -= 1
      else if (move == 'L') x -= 1
      else if (move == 'R') x += 1
      i += 1
    }
    x == 0 && y == 0
  }
}
"""

FILES["0658_find_k_closest_elements"] = """// LeetCode 0658 - Find K Closest Elements
// https://leetcode.com/problems/find-k-closest-elements/

object Solution {
  def findClosestElements(arr: Array[Int], k: Int, x: Int): List[Int] = {
    var left = 0
    var right = arr.length - k
    while (left < right) {
      val mid = left + (right - left) / 2
      if (x - arr(mid) > arr(mid + k) - x) left = mid + 1
      else right = mid
    }
    arr.slice(left, left + k).toList
  }
}
"""

FILES["0659_split_array_into_consecutive_subsequences"] = """// LeetCode 0659 - Split Array into Consecutive Subsequences
// https://leetcode.com/problems/split-array-into-consecutive-subsequences/

import scala.collection.mutable

object Solution {
  def isPossible(nums: Array[Int]): Boolean = {
    val freq = mutable.Map.empty[Int, Int]
    val tails = mutable.Map.empty[Int, Int]
    nums.foreach(num => freq(num) = freq.getOrElse(num, 0) + 1)
    nums.foreach { num =>
      if (freq.getOrElse(num, 0) != 0) {
        freq(num) = freq(num) - 1
        if (tails.getOrElse(num - 1, 0) > 0) {
          tails(num - 1) = tails(num - 1) - 1
          tails(num) = tails.getOrElse(num, 0) + 1
        } else if (freq.getOrElse(num + 1, 0) > 0 && freq.getOrElse(num + 2, 0) > 0) {
          freq(num + 1) = freq(num + 1) - 1
          freq(num + 2) = freq(num + 2) - 1
          tails(num + 2) = tails.getOrElse(num + 2, 0) + 1
        } else {
          return false
        }
      }
    }
    true
  }
}
"""

FILES["0660_remove_9"] = """// LeetCode 0660 - Remove 9
// https://leetcode.com/problems/remove-9/

object Solution {
  def newInteger(n0: Int): Int = {
    var n = n0
    var result = 0
    var base = 1
    while (n > 0) {
      result += (n % 9) * base
      n /= 9
      base *= 10
    }
    result
  }
}
"""

FILES["0661_image_smoother"] = """// LeetCode 0661 - Image Smoother
// https://leetcode.com/problems/image-smoother/

object Solution {
  def imageSmoother(img: Array[Array[Int]]): Array[Array[Int]] = {
    val m = img.length
    val n = img(0).length
    val out = Array.ofDim[Int](m, n)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        var total = 0
        var count = 0
        var di = -1
        while (di <= 1) {
          var dj = -1
          while (dj <= 1) {
            val ni = i + di
            val nj = j + dj
            if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
              total += img(ni)(nj)
              count += 1
            }
            dj += 1
          }
          di += 1
        }
        out(i)(j) = total / count
        j += 1
      }
      i += 1
    }
    out
  }
}
"""

FILES["0662_maximum_width_of_binary_tree"] = f"""// LeetCode 0662 - Maximum Width of Binary Tree
// https://leetcode.com/problems/maximum-width-of-binary-tree/

import scala.collection.mutable

{TREE}
object Solution {{
  def widthOfBinaryTree(root: TreeNode): Int = {{
    if (root == null) return 0
    val queue = mutable.Queue[(TreeNode, Long)]((root, 0L))
    var best = 0
    while (queue.nonEmpty) {{
      val left = queue.head._2
      val size = queue.size
      var i = 0
      while (i < size) {{
        val (node, idx) = queue.dequeue()
        best = math.max(best, (idx - left + 1).toInt)
        if (node.left != null) queue.enqueue((node.left, idx * 2))
        if (node.right != null) queue.enqueue((node.right, idx * 2 + 1))
        i += 1
      }}
    }}
    best
  }}
}}
"""

FILES["0663_equal_tree_partition"] = f"""// LeetCode 0663 - Equal Tree Partition
// https://leetcode.com/problems/equal-tree-partition/

import scala.collection.mutable

{TREE}
object Solution {{
  def checkEqualTree(root: TreeNode): Boolean = {{
    val subtreeSums = mutable.ArrayBuffer.empty[Int]
    def dfs(node: TreeNode): Int = {{
      if (node == null) return 0
      val total = node.value + dfs(node.left) + dfs(node.right)
      subtreeSums += total
      total
    }}
    val total = dfs(root)
    if (subtreeSums.nonEmpty) subtreeSums.remove(subtreeSums.size - 1)
    if (total % 2 != 0) return false
    val half = total / 2
    subtreeSums.exists(_ == half)
  }}
}}
"""

FILES["0664_strange_printer"] = """// LeetCode 0664 - Strange Printer
// https://leetcode.com/problems/strange-printer/

object Solution {
  def strangePrinter(s: String): Int = {
    val n = s.length
    if (n == 0) return 0
    val dp = Array.ofDim[Int](n, n)
    var i = n - 1
    while (i >= 0) {
      dp(i)(i) = 1
      var j = i + 1
      while (j < n) {
        dp(i)(j) = dp(i + 1)(j) + 1
        var k = i + 1
        while (k <= j) {
          if (s.charAt(k) == s.charAt(i)) {
            dp(i)(j) = math.min(dp(i)(j), dp(i)(k - 1) + (if (k + 1 <= j) dp(k + 1)(j) else 0))
          }
          k += 1
        }
        j += 1
      }
      i -= 1
    }
    dp(0)(n - 1)
  }
}
"""

FILES["0665_non_decreasing_array"] = """// LeetCode 0665 - Non-decreasing Array
// https://leetcode.com/problems/non-decreasing-array/

object Solution {
  def checkPossibility(nums: Array[Int]): Boolean = {
    var changed = false
    var i = 1
    while (i < nums.length) {
      if (nums(i) < nums(i - 1)) {
        if (changed) return false
        changed = true
        if (i >= 2 && nums(i) < nums(i - 2)) nums(i) = nums(i - 1)
        else nums(i - 1) = nums(i)
      }
      i += 1
    }
    true
  }
}
"""

FILES["0666_path_sum_iv"] = """// LeetCode 0666 - Path Sum IV
// https://leetcode.com/problems/path-sum-iv/

import scala.collection.mutable

object Solution {
  def pathSum(nums: Array[Int]): Int = {
    val tree = mutable.Map.empty[Long, Int]
    var total = 0
    nums.foreach(num => tree(key(num / 100, (num / 10) % 10)) = num % 10)
    def dfs(depth: Int, pos: Int, path0: Int): Unit = {
      val k = key(depth, pos)
      if (!tree.contains(k)) return
      val path = path0 + tree(k)
      val left = key(depth + 1, pos * 2 - 1)
      val right = key(depth + 1, pos * 2)
      if (!tree.contains(left) && !tree.contains(right)) {
        total += path
        return
      }
      dfs(depth + 1, pos * 2 - 1, path)
      dfs(depth + 1, pos * 2, path)
    }
    dfs(1, 1, 0)
    total
  }

  private def key(depth: Int, pos: Int): Long =
    (depth.toLong << 32) | (pos.toLong & 0xffffffffL)
}
"""

FILES["0667_beautiful_arrangement_ii"] = """// LeetCode 0667 - Beautiful Arrangement II
// https://leetcode.com/problems/beautiful-arrangement-ii/

object Solution {
  def constructArray(n: Int, k: Int): Array[Int] = {
    val res = Array.fill(n)(0)
    var idx = 0
    var i = 1
    while (i <= n - k) {
      res(idx) = i
      idx += 1
      i += 1
    }
    var left = n - k + 1
    var right = n
    var takeHigh = true
    while (left <= right) {
      if (takeHigh) {
        res(idx) = right
        right -= 1
      } else {
        res(idx) = left
        left += 1
      }
      idx += 1
      takeHigh = !takeHigh
    }
    res
  }
}
"""

FILES["0668_kth_smallest_number_in_multiplication_table"] = """// LeetCode 0668 - Kth Smallest Number in Multiplication Table
// https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

object Solution {
  def findKthNumber(m: Int, n: Int, k: Int): Int = {
    var lo = 1
    var hi = m * n
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (countLe(m, n, mid) >= k) hi = mid else lo = mid + 1
    }
    lo
  }

  private def countLe(m: Int, n: Int, x: Int): Int = {
    var count = 0
    var row = 1
    while (row <= m) {
      count += math.min(x / row, n)
      row += 1
    }
    count
  }
}
"""

FILES["0669_trim_a_binary_search_tree"] = f"""// LeetCode 0669 - Trim a Binary Search Tree
// https://leetcode.com/problems/trim-a-binary-search-tree/

{TREE}
object Solution {{
  def trimBST(root: TreeNode, low: Int, high: Int): TreeNode = {{
    if (root == null) return null
    if (root.value < low) return trimBST(root.right, low, high)
    if (root.value > high) return trimBST(root.left, low, high)
    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)
    root
  }}
}}
"""

FILES["0670_maximum_swap"] = """// LeetCode 0670 - Maximum Swap
// https://leetcode.com/problems/maximum-swap/

object Solution {
  def maximumSwap(num: Int): Int = {
    val digits = num.toString.toCharArray
    val last = Array.fill(10)(-1)
    var i = 0
    while (i < digits.length) {
      last(digits(i) - '0') = i
      i += 1
    }
    i = 0
    while (i < digits.length) {
      var candidate = 9
      while (candidate > digits(i) - '0') {
        if (last(candidate) > i) {
          val tmp = digits(i)
          digits(i) = digits(last(candidate))
          digits(last(candidate)) = tmp
          return new String(digits).toInt
        }
        candidate -= 1
      }
      i += 1
    }
    num
  }
}
"""

FILES["0671_second_minimum_node_in_a_binary_tree"] = f"""// LeetCode 0671 - Second Minimum Node In a Binary Tree
// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

{TREE}
object Solution {{
  def findSecondMinimumValue(root: TreeNode): Int = {{
    if (root == null) return -1
    var ans = -1
    val rootVal = root.value
    def dfs(node: TreeNode): Unit = {{
      if (node == null) return
      if (node.value > rootVal) {{
        if (ans == -1 || node.value < ans) ans = node.value
        return
      }}
      dfs(node.left)
      dfs(node.right)
    }}
    dfs(root)
    ans
  }}
}}
"""

FILES["0672_bulb_switcher_ii"] = """// LeetCode 0672 - Bulb Switcher II
// https://leetcode.com/problems/bulb-switcher-ii/

object Solution {
  def flipLights(n0: Int, presses: Int): Int = {
    val n = math.min(n0, 3)
    if (presses == 0) return 1
    val onePress = Array(2, 3, 4)
    val twoPress = Array(2, 4, 7)
    val manyPress = Array(2, 4, 8)
    if (presses == 1) return onePress(n - 1)
    if (presses == 2) return twoPress(n - 1)
    manyPress(n - 1)
  }
}
"""

FILES["0673_number_of_longest_increasing_subsequence"] = """// LeetCode 0673 - Number of Longest Increasing Subsequence
// https://leetcode.com/problems/number-of-longest-increasing-subsequence/

object Solution {
  def findNumberOfLIS(nums: Array[Int]): Int = {
    val n = nums.length
    val lengths = Array.fill(n)(1)
    val counts = Array.fill(n)(1)
    var i = 0
    while (i < n) {
      var j = 0
      while (j < i) {
        if (nums(j) < nums(i)) {
          if (lengths(j) + 1 > lengths(i)) {
            lengths(i) = lengths(j) + 1
            counts(i) = counts(j)
          } else if (lengths(j) + 1 == lengths(i)) {
            counts(i) += counts(j)
          }
        }
        j += 1
      }
      i += 1
    }
    var longest = 0
    lengths.foreach(length => longest = math.max(longest, length))
    var answer = 0
    i = 0
    while (i < n) {
      if (lengths(i) == longest) answer += counts(i)
      i += 1
    }
    answer
  }
}
"""

FILES["0674_longest_continuous_increasing_subsequence"] = """// LeetCode 0674 - Longest Continuous Increasing Subsequence
// https://leetcode.com/problems/longest-continuous-increasing-subsequence/

object Solution {
  def findLengthOfLCIS(nums: Array[Int]): Int = {
    var best = 1
    var cur = 1
    var i = 1
    while (i < nums.length) {
      if (nums(i) > nums(i - 1)) {
        cur += 1
        best = math.max(best, cur)
      } else {
        cur = 1
      }
      i += 1
    }
    best
  }
}
"""

FILES["0675_cut_off_trees_for_golf_event"] = """// LeetCode 0675 - Cut Off Trees for Golf Event
// https://leetcode.com/problems/cut-off-trees-for-golf-event/

import scala.collection.mutable

object Solution {
  def cutOffTree(forest: List[List[Int]]): Int = {
    val trees = mutable.ArrayBuffer.empty[Array[Int]]
    var i = 0
    while (i < forest.size) {
      var j = 0
      while (j < forest.head.size) {
        if (forest(i)(j) > 1) trees += Array(forest(i)(j), i, j)
        j += 1
      }
      i += 1
    }
    val sorted = trees.sortBy(_(0))
    var sr = 0
    var sc = 0
    var steps = 0
    sorted.foreach { tree =>
      val dist = bfs(forest, sr, sc, tree(1), tree(2))
      if (dist < 0) return -1
      steps += dist
      sr = tree(1)
      sc = tree(2)
    }
    steps
  }

  private def bfs(forest: List[List[Int]], sr: Int, sc: Int, tr: Int, tc: Int): Int = {
    if (sr == tr && sc == tc) return 0
    val m = forest.size
    val n = forest.head.size
    val seen = Array.ofDim[Boolean](m, n)
    val queue = mutable.Queue(Array(sr, sc, 0))
    seen(sr)(sc) = true
    val dirs = Array(Array(-1, 0), Array(1, 0), Array(0, -1), Array(0, 1))
    while (queue.nonEmpty) {
      val cur = queue.dequeue()
      val r = cur(0)
      val c = cur(1)
      val dist = cur(2)
      dirs.foreach { dir =>
        val nr = r + dir(0)
        val nc = c + dir(1)
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen(nr)(nc) && forest(nr)(nc) != 0) {
          if (nr == tr && nc == tc) return dist + 1
          seen(nr)(nc) = true
          queue.enqueue(Array(nr, nc, dist + 1))
        }
      }
    }
    -1
  }
}
"""

FILES["0676_implement_magic_dictionary"] = """// LeetCode 0676 - Implement Magic Dictionary
// https://leetcode.com/problems/implement-magic-dictionary/

class MagicDictionary() {
  private var words: Array[String] = Array.empty

  def buildDict(dictionary: Array[String]): Unit = {
    words = dictionary
  }

  def search(searchWord: String): Boolean = {
    words.exists { word =>
      if (word.length != searchWord.length) false
      else {
        var diff = 0
        var i = 0
        while (i < word.length) {
          if (word.charAt(i) != searchWord.charAt(i)) diff += 1
          i += 1
        }
        diff == 1
      }
    }
  }
}
"""

FILES["0677_map_sum_pairs"] = """// LeetCode 0677 - Map Sum Pairs
// https://leetcode.com/problems/map-sum-pairs/

import scala.collection.mutable

class MapSum() {
  private val values = mutable.Map.empty[String, Int]
  private val prefixSums = mutable.Map.empty[String, Int]

  def insert(key: String, `val`: Int): Unit = {
    val delta = `val` - values.getOrElse(key, 0)
    values(key) = `val`
    var i = 1
    while (i <= key.length) {
      val prefix = key.substring(0, i)
      prefixSums(prefix) = prefixSums.getOrElse(prefix, 0) + delta
      i += 1
    }
  }

  def sum(prefix: String): Int = prefixSums.getOrElse(prefix, 0)
}
"""

FILES["0678_valid_parenthesis_string"] = """// LeetCode 0678 - Valid Parenthesis String
// https://leetcode.com/problems/valid-parenthesis-string/

object Solution {
  def checkValidString(s: String): Boolean = {
    var lo = 0
    var hi = 0
    var i = 0
    while (i < s.length) {
      val ch = s.charAt(i)
      if (ch == '(') {
        lo += 1
        hi += 1
      } else if (ch == ')') {
        lo = math.max(lo - 1, 0)
        hi -= 1
        if (hi < 0) return false
      } else {
        lo = math.max(lo - 1, 0)
        hi += 1
      }
      i += 1
    }
    lo == 0
  }
}
"""

FILES["0679_24_game"] = """// LeetCode 0679 - 24 Game
// https://leetcode.com/problems/24-game/

import scala.collection.mutable

object Solution {
  private val EPS = 1e-6

  def judgePoint24(cards: Array[Int]): Boolean = {
    val nums = mutable.ArrayBuffer.from(cards.map(_.toDouble))
    dfs(nums)
  }

  private def dfs(nums: mutable.ArrayBuffer[Double]): Boolean = {
    if (nums.size == 1) return math.abs(nums(0) - 24.0) < EPS
    var i = 0
    while (i < nums.size) {
      var j = 0
      while (j < nums.size) {
        if (i != j) {
          val rest = mutable.ArrayBuffer.empty[Double]
          var k = 0
          while (k < nums.size) {
            if (k != i && k != j) rest += nums(k)
            k += 1
          }
          val a = nums(i)
          val b = nums(j)
          val candidates = mutable.ArrayBuffer(a + b, a - b, a * b)
          if (math.abs(b) > EPS) candidates += a / b
          candidates.foreach { value =>
            rest += value
            if (dfs(rest)) return true
            rest.remove(rest.size - 1)
          }
        }
        j += 1
      }
      i += 1
    }
    false
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
