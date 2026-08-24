#!/usr/bin/env python3
"""Write Solution.scala for batch_03 folders 0880-0929."""
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

TREE = """class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}
"""


def write(folder: str, body: str) -> None:
    path = ROOT / folder / "Solution.scala"
    path.write_text(body.rstrip() + "\n", encoding="utf-8")
    print("wrote", folder)


write("0880_decoded_string_at_index", r'''// LeetCode 0880 - Decoded String at Index
// https://leetcode.com/problems/decoded-string-at-index/

object Solution {
  def decodeAtIndex(s: String, k: Int): String = {
    var size = 0L
    s.foreach { ch =>
      if (ch.isDigit) size *= (ch - '0')
      else size += 1
    }
    var kk = k.toLong
    var i = s.length - 1
    while (i >= 0) {
      val ch = s.charAt(i)
      kk %= size
      if (kk == 0 && ch.isLetter) return ch.toString
      if (ch.isDigit) size /= (ch - '0')
      else size -= 1
      i -= 1
    }
    ""
  }
}
''')

write("0881_boats_to_save_people", r'''// LeetCode 0881 - Boats to Save People
// https://leetcode.com/problems/boats-to-save-people/

object Solution {
  def numRescueBoats(people: Array[Int], limit: Int): Int = {
    val arr = people.sorted
    var i = 0
    var j = arr.length - 1
    var boats = 0
    while (i <= j) {
      if (arr(i) + arr(j) <= limit) i += 1
      j -= 1
      boats += 1
    }
    boats
  }
}
''')

write("0882_reachable_nodes_in_subdivided_graph", r'''// LeetCode 0882 - Reachable Nodes In Subdivided Graph
// https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

object Solution {
  def reachableNodes(edges: Array[Array[Int]], maxMoves: Int, n: Int): Int = {
    val graph = Array.fill(n)(scala.collection.mutable.Map.empty[Int, Int])
    edges.foreach { e =>
      graph(e(0))(e(1)) = e(2)
      graph(e(1))(e(0)) = e(2)
    }
    val pq = scala.collection.mutable.PriorityQueue[(Int, Int)]()
    pq.enqueue((maxMoves, 0))
    val seen = scala.collection.mutable.Map.empty[Int, Int]
    while (pq.nonEmpty) {
      val (moves, node) = pq.dequeue()
      if (!seen.contains(node)) {
        seen(node) = moves
        graph(node).foreach { case (nei, cnt) =>
          val remain = moves - cnt - 1
          if (!seen.contains(nei) && remain >= 0) pq.enqueue((remain, nei))
        }
      }
    }
    var ans = seen.size
    edges.foreach { e =>
      val left = seen.getOrElse(e(0), 0)
      val right = seen.getOrElse(e(1), 0)
      ans += math.min(e(2), left + right)
    }
    ans
  }
}
''')

write("0883_projection_area_of_3d_shapes", r'''// LeetCode 0883 - Projection Area of 3D Shapes
// https://leetcode.com/problems/projection-area-of-3d-shapes/

object Solution {
  def projectionArea(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    var top = 0
    var front = 0
    var side = 0
    var i = 0
    while (i < n) {
      var rowMax = 0
      var colMax = 0
      var j = 0
      while (j < n) {
        if (grid(i)(j) != 0) top += 1
        rowMax = math.max(rowMax, grid(i)(j))
        colMax = math.max(colMax, grid(j)(i))
        j += 1
      }
      front += rowMax
      side += colMax
      i += 1
    }
    top + front + side
  }
}
''')

write("0884_uncommon_words_from_two_sentences", r'''// LeetCode 0884 - Uncommon Words from Two Sentences
// https://leetcode.com/problems/uncommon-words-from-two-sentences/

object Solution {
  def uncommonFromSentences(s1: String, s2: String): Array[String] = {
    val count = scala.collection.mutable.Map.empty[String, Int]
    def add(s: String): Unit = {
      s.split(" ").foreach { w =>
        if (w.nonEmpty) count(w) = count.getOrElse(w, 0) + 1
      }
    }
    add(s1)
    add(s2)
    count.collect { case (w, c) if c == 1 => w }.toArray
  }
}
''')

write("0885_spiral_matrix_iii", r'''// LeetCode 0885 - Spiral Matrix III
// https://leetcode.com/problems/spiral-matrix-iii/

object Solution {
  def spiralMatrixIII(rows: Int, cols: Int, rStart: Int, cStart: Int): Array[Array[Int]] = {
    val ans = scala.collection.mutable.ArrayBuffer[Array[Int]]()
    ans += Array(rStart, cStart)
    if (rows * cols == 1) return ans.toArray
    var r = rStart
    var c = cStart
    val dirs = Array(Array(0, 1), Array(1, 0), Array(0, -1), Array(-1, 0))
    var steps = 1
    while (ans.length < rows * cols) {
      var d = 0
      while (d < 4) {
        val dr = dirs(d)(0)
        val dc = dirs(d)(1)
        var i = 0
        while (i < steps) {
          r += dr
          c += dc
          if (r >= 0 && r < rows && c >= 0 && c < cols) {
            ans += Array(r, c)
            if (ans.length == rows * cols) return ans.toArray
          }
          i += 1
        }
        if (d % 2 == 1) steps += 1
        d += 1
      }
    }
    ans.toArray
  }
}
''')

write("0886_possible_bipartition", r'''// LeetCode 0886 - Possible Bipartition
// https://leetcode.com/problems/possible-bipartition/

object Solution {
  def possibleBipartition(n: Int, dislikes: Array[Array[Int]]): Boolean = {
    val graph = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
    dislikes.foreach { e =>
      graph(e(0)) += e(1)
      graph(e(1)) += e(0)
    }
    val color = scala.collection.mutable.Map.empty[Int, Int]
    var start = 1
    while (start <= n) {
      if (!color.contains(start)) {
        val queue = scala.collection.mutable.Queue[Int]()
        queue.enqueue(start)
        color(start) = 0
        while (queue.nonEmpty) {
          val node = queue.dequeue()
          graph(node).foreach { nei =>
            if (!color.contains(nei)) {
              color(nei) = color(node) ^ 1
              queue.enqueue(nei)
            } else if (color(nei) == color(node)) return false
          }
        }
      }
      start += 1
    }
    true
  }
}
''')

write("0887_super_egg_drop", r'''// LeetCode 0887 - Super Egg Drop
// https://leetcode.com/problems/super-egg-drop/

object Solution {
  def superEggDrop(k: Int, n: Int): Int = {
    val dp = Array.fill(k + 1)(0)
    var moves = 0
    while (dp(k) < n) {
      moves += 1
      var eggs = k
      while (eggs >= 1) {
        dp(eggs) = dp(eggs) + dp(eggs - 1) + 1
        eggs -= 1
      }
    }
    moves
  }
}
''')

write("0888_fair_candy_swap", r'''// LeetCode 0888 - Fair Candy Swap
// https://leetcode.com/problems/fair-candy-swap/

object Solution {
  def fairCandySwap(aliceSizes: Array[Int], bobSizes: Array[Int]): Array[Int] = {
    val sumA = aliceSizes.sum
    val sumB = bobSizes.sum
    val diff = (sumA - sumB) / 2
    val bob = bobSizes.toSet
    aliceSizes.foreach { a =>
      if (bob.contains(a - diff)) return Array(a, a - diff)
    }
    Array.empty[Int]
  }
}
''')

write("0889_construct_binary_tree_from_preorder_and_postorder_traversal", f'''// LeetCode 0889 - Construct Binary Tree from Preorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

{TREE}
object Solution {{
  def constructFromPrePost(preorder: Array[Int], postorder: Array[Int]): TreeNode = {{
    val postIndex = postorder.zipWithIndex.toMap
    def build(preLo: Int, preHi: Int, postLo: Int, postHi: Int): TreeNode = {{
      if (preLo > preHi) return null
      val root = new TreeNode(preorder(preLo))
      if (preLo == preHi) return root
      val leftVal = preorder(preLo + 1)
      val leftPost = postIndex(leftVal)
      val leftSize = leftPost - postLo + 1
      root.left = build(preLo + 1, preLo + leftSize, postLo, leftPost)
      root.right = build(preLo + leftSize + 1, preHi, leftPost + 1, postHi - 1)
      root
    }}
    val n = preorder.length
    build(0, n - 1, 0, n - 1)
  }}
}}
''')

write("0890_find_and_replace_pattern", r'''// LeetCode 0890 - Find and Replace Pattern
// https://leetcode.com/problems/find-and-replace-pattern/

object Solution {
  def findAndReplacePattern(words: Array[String], pattern: String): List[String] = {
    def normalize(s: String): Array[Int] = {
      val mapping = scala.collection.mutable.Map.empty[Char, Int]
      val out = Array.ofDim[Int](s.length)
      var i = 0
      while (i < s.length) {
        val ch = s.charAt(i)
        if (!mapping.contains(ch)) mapping(ch) = mapping.size
        out(i) = mapping(ch)
        i += 1
      }
      out
    }
    val target = normalize(pattern)
    words.filter(w => java.util.Arrays.equals(normalize(w), target)).toList
  }
}
''')

write("0891_sum_of_subsequence_widths", r'''// LeetCode 0891 - Sum of Subsequence Widths
// https://leetcode.com/problems/sum-of-subsequence-widths/

object Solution {
  def sumSubseqWidths(nums: Array[Int]): Int = {
    val MOD = 1000000007
    val arr = nums.sorted
    val n = arr.length
    val pow2 = Array.ofDim[Long](n)
    pow2(0) = 1
    var i = 1
    while (i < n) {
      pow2(i) = (pow2(i - 1) * 2) % MOD
      i += 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      ans = (ans + arr(i).toLong * (pow2(i) - pow2(n - 1 - i))) % MOD
      i += 1
    }
    ((ans + MOD) % MOD).toInt
  }
}
''')

write("0892_surface_area_of_3d_shapes", r'''// LeetCode 0892 - Surface Area of 3D Shapes
// https://leetcode.com/problems/surface-area-of-3d-shapes/

object Solution {
  def surfaceArea(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    var area = 0
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) != 0) {
          area += grid(i)(j) * 4 + 2
          if (i > 0) area -= math.min(grid(i)(j), grid(i - 1)(j)) * 2
          if (j > 0) area -= math.min(grid(i)(j), grid(i)(j - 1)) * 2
        }
        j += 1
      }
      i += 1
    }
    area
  }
}
''')

write("0893_groups_of_special_equivalent_strings", r'''// LeetCode 0893 - Groups of Special-Equivalent Strings
// https://leetcode.com/problems/groups-of-special-equivalent-strings/

object Solution {
  def numSpecialEquivGroups(words: Array[String]): Int = {
    val groups = scala.collection.mutable.Set.empty[String]
    words.foreach { w =>
      val even = scala.collection.mutable.ArrayBuffer[Char]()
      val odd = scala.collection.mutable.ArrayBuffer[Char]()
      var i = 0
      while (i < w.length) {
        if (i % 2 == 0) even += w.charAt(i)
        else odd += w.charAt(i)
        i += 1
      }
      groups += even.sorted.mkString + "|" + odd.sorted.mkString
    }
    groups.size
  }
}
''')

write("0894_all_possible_full_binary_trees", f'''// LeetCode 0894 - All Possible Full Binary Trees
// https://leetcode.com/problems/all-possible-full-binary-trees/

{TREE}
object Solution {{
  def allPossibleFBT(n: Int): List[TreeNode] = {{
    val memo = scala.collection.mutable.Map.empty[Int, List[TreeNode]]
    def build(nodes: Int): List[TreeNode] = {{
      if (memo.contains(nodes)) return memo(nodes)
      if (nodes % 2 == 0) {{
        memo(nodes) = Nil
        return Nil
      }}
      if (nodes == 1) {{
        val res = List(new TreeNode(0))
        memo(nodes) = res
        return res
      }}
      val res = scala.collection.mutable.ListBuffer[TreeNode]()
      var left = 1
      while (left < nodes) {{
        val right = nodes - 1 - left
        build(left).foreach {{ L =>
          build(right).foreach {{ R =>
            res += new TreeNode(0, L, R)
          }}
        }}
        left += 2
      }}
      val out = res.toList
      memo(nodes) = out
      out
    }}
    build(n)
  }}
}}
''')

write("0895_maximum_frequency_stack", r'''// LeetCode 0895 - Maximum Frequency Stack
// https://leetcode.com/problems/maximum-frequency-stack/

class FreqStack() {
  private val freq = scala.collection.mutable.Map.empty[Int, Int]
  private val group = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
  private var maxfreq = 0

  def push(`val`: Int): Unit = {
    val f = freq.getOrElse(`val`, 0) + 1
    freq(`val`) = f
    maxfreq = math.max(maxfreq, f)
    group.getOrElseUpdate(f, scala.collection.mutable.ArrayBuffer.empty[Int]) += `val`
  }

  def pop(): Int = {
    val list = group(maxfreq)
    val v = list.remove(list.length - 1)
    freq(v) = freq(v) - 1
    if (list.isEmpty) maxfreq -= 1
    v
  }
}
''')

write("0896_monotonic_array", r'''// LeetCode 0896 - Monotonic Array
// https://leetcode.com/problems/monotonic-array/

object Solution {
  def isMonotonic(nums: Array[Int]): Boolean = {
    var inc = true
    var dec = true
    var i = 1
    while (i < nums.length) {
      if (nums(i) < nums(i - 1)) inc = false
      if (nums(i) > nums(i - 1)) dec = false
      i += 1
    }
    inc || dec
  }
}
''')

write("0897_increasing_order_search_tree", f'''// LeetCode 0897 - Increasing Order Search Tree
// https://leetcode.com/problems/increasing-order-search-tree/

{TREE}
object Solution {{
  def increasingBST(root: TreeNode): TreeNode = {{
    val dummy = new TreeNode(0)
    var cur = dummy
    def inorder(node: TreeNode): Unit = {{
      if (node == null) return
      inorder(node.left)
      node.left = null
      cur.right = node
      cur = node
      inorder(node.right)
    }}
    inorder(root)
    dummy.right
  }}
}}
''')

write("0898_bitwise_ors_of_subarrays", r'''// LeetCode 0898 - Bitwise ORs of Subarrays
// https://leetcode.com/problems/bitwise-ors-of-subarrays/

object Solution {
  def subarrayBitwiseORs(arr: Array[Int]): Int = {
    val ans = scala.collection.mutable.Set.empty[Int]
    var cur = Set.empty[Int]
    arr.foreach { x =>
      val nxt = scala.collection.mutable.Set(x)
      cur.foreach(y => nxt += (x | y))
      cur = nxt.toSet
      ans ++= cur
    }
    ans.size
  }
}
''')

write("0899_orderly_queue", r'''// LeetCode 0899 - Orderly Queue
// https://leetcode.com/problems/orderly-queue/

object Solution {
  def orderlyQueue(s: String, k: Int): String = {
    if (k > 1) return s.sorted
    var best = s
    var i = 1
    while (i < s.length) {
      val cand = s.substring(i) + s.substring(0, i)
      if (cand < best) best = cand
      i += 1
    }
    best
  }
}
''')

write("0900_rle_iterator", r'''// LeetCode 0900 - RLE Iterator
// https://leetcode.com/problems/rle-iterator/

class RLEIterator(_encoding: Array[Int]) {
  private val enc = _encoding.clone()
  private var i = 0

  def next(n: Int): Int = {
    var remain = n
    while (i < enc.length) {
      if (enc(i) >= remain) {
        enc(i) -= remain
        return enc(i + 1)
      }
      remain -= enc(i)
      i += 2
    }
    -1
  }
}
''')

write("0901_online_stock_span", r'''// LeetCode 0901 - Online Stock Span
// https://leetcode.com/problems/online-stock-span/

class StockSpanner() {
  private val stack = scala.collection.mutable.ArrayBuffer[Array[Int]]()

  def next(price: Int): Int = {
    var span = 1
    while (stack.nonEmpty && stack.last(0) <= price) {
      span += stack.last(1)
      stack.remove(stack.length - 1)
    }
    stack += Array(price, span)
    span
  }
}
''')

write("0902_numbers_at_most_n_given_digit_set", r'''// LeetCode 0902 - Numbers At Most N Given Digit Set
// https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

object Solution {
  def atMostNGivenDigitSet(digits: Array[String], n: Int): Int = {
    val k = digits.length
    val s = n.toString
    val m = s.length
    def ipow(bas: Int, exp: Int): Int = {
      var r = 1
      var e = exp
      while (e > 0) { r *= bas; e -= 1 }
      r
    }
    def countUpTo(t: String): Int = {
      if (t.isEmpty) return 0
      var first = 0
      digits.foreach { d => if (d.charAt(0) < t.charAt(0)) first += 1 }
      var ways = first * ipow(k, t.length - 1)
      val found = digits.exists(_.charAt(0) == t.charAt(0))
      if (found) ways += countUpTo(t.substring(1))
      ways
    }
    var ans = 0
    var i = 1
    while (i < m) {
      ans += ipow(k, i)
      i += 1
    }
    ans + countUpTo(s)
  }
}
''')

write("0903_valid_permutations_for_di_sequence", r'''// LeetCode 0903 - Valid Permutations for DI Sequence
// https://leetcode.com/problems/valid-permutations-for-di-sequence/

object Solution {
  def numPermsDISequence(s: String): Int = {
    val MOD = 1000000007
    val n = s.length
    var dp = Array.fill(n + 1)(1)
    var i = 1
    while (i <= n) {
      val newDp = Array.ofDim[Int](n + 1)
      if (s.charAt(i - 1) == 'I') {
        var postfix = 0
        var j = n - i
        while (j >= 0) {
          postfix = (postfix + dp(j + 1)) % MOD
          newDp(j) = postfix
          j -= 1
        }
      } else {
        var prefix = 0
        var j = 0
        while (j <= n - i) {
          prefix = (prefix + dp(j)) % MOD
          newDp(j) = prefix
          j += 1
        }
      }
      dp = newDp
      i += 1
    }
    dp(0)
  }
}
''')

write("0904_fruit_into_baskets", r'''// LeetCode 0904 - Fruit Into Baskets
// https://leetcode.com/problems/fruit-into-baskets/

object Solution {
  def totalFruit(fruits: Array[Int]): Int = {
    val count = scala.collection.mutable.Map.empty[Int, Int]
    var left = 0
    var ans = 0
    var right = 0
    while (right < fruits.length) {
      count(fruits(right)) = count.getOrElse(fruits(right), 0) + 1
      while (count.size > 2) {
        val c = count(fruits(left)) - 1
        if (c == 0) count.remove(fruits(left))
        else count(fruits(left)) = c
        left += 1
      }
      ans = math.max(ans, right - left + 1)
      right += 1
    }
    ans
  }
}
''')

write("0905_sort_array_by_parity", r'''// LeetCode 0905 - Sort Array By Parity
// https://leetcode.com/problems/sort-array-by-parity/

object Solution {
  def sortArrayByParity(nums: Array[Int]): Array[Int] = {
    var i = 0
    var j = 0
    while (j < nums.length) {
      if (nums(j) % 2 == 0) {
        val tmp = nums(i)
        nums(i) = nums(j)
        nums(j) = tmp
        i += 1
      }
      j += 1
    }
    nums
  }
}
''')

write("0906_super_palindromes", r'''// LeetCode 0906 - Super Palindromes
// https://leetcode.com/problems/super-palindromes/

object Solution {
  def superpalindromesInRange(left: String, right: String): Int = {
    val L = left.toLong
    val R = right.toLong
    def isPal(x: Long): Boolean = {
      val s = x.toString
      val n = s.length
      var i = 0
      while (i < n / 2) {
        if (s.charAt(i) != s.charAt(n - 1 - i)) return false
        i += 1
      }
      true
    }
    var ans = 0
    var k = 1L
    var stop = false
    while (k <= 100000 && !stop) {
      val s = k.toString
      val pal = (s + s.reverse).toLong
      val sq = pal * pal
      if (sq > R) stop = true
      else {
        if (sq >= L && isPal(sq)) ans += 1
        k += 1
      }
    }
    k = 1L
    stop = false
    while (k <= 100000 && !stop) {
      val s = k.toString
      val pal = (s + s.substring(0, s.length - 1).reverse).toLong
      val sq = pal * pal
      if (sq > R) stop = true
      else {
        if (sq >= L && isPal(sq)) ans += 1
        k += 1
      }
    }
    ans
  }
}
''')

write("0907_sum_of_subarray_minimums", r'''// LeetCode 0907 - Sum of Subarray Minimums
// https://leetcode.com/problems/sum-of-subarray-minimums/

object Solution {
  def sumSubarrayMins(arr: Array[Int]): Int = {
    val MOD = 1000000007
    val n = arr.length
    val left = Array.fill(n)(-1)
    val right = Array.fill(n)(n)
    val st = scala.collection.mutable.ArrayDeque[Int]()
    var i = 0
    while (i < n) {
      while (st.nonEmpty && arr(st.last) > arr(i)) st.removeLast()
      left(i) = if (st.isEmpty) -1 else st.last
      st.append(i)
      i += 1
    }
    st.clear()
    i = n - 1
    while (i >= 0) {
      while (st.nonEmpty && arr(st.last) >= arr(i)) st.removeLast()
      right(i) = if (st.isEmpty) n else st.last
      st.append(i)
      i -= 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      ans = (ans + arr(i).toLong * (i - left(i)) * (right(i) - i)) % MOD
      i += 1
    }
    ans.toInt
  }
}
''')

write("0908_smallest_range_i", r'''// LeetCode 0908 - Smallest Range I
// https://leetcode.com/problems/smallest-range-i/

object Solution {
  def smallestRangeI(nums: Array[Int], k: Int): Int = {
    var mn = nums(0)
    var mx = nums(0)
    nums.foreach { x =>
      mn = math.min(mn, x)
      mx = math.max(mx, x)
    }
    math.max(0, mx - mn - 2 * k)
  }
}
''')

write("0909_snakes_and_ladders", r'''// LeetCode 0909 - Snakes and Ladders
// https://leetcode.com/problems/snakes-and-ladders/

object Solution {
  def snakesAndLadders(board: Array[Array[Int]]): Int = {
    val n = board.length
    val target = n * n
    def pos(square: Int): (Int, Int) = {
      val s = square - 1
      val row = s / n
      val rem = s % n
      val r = n - 1 - row
      val c = if (row % 2 == 0) rem else n - 1 - rem
      (r, c)
    }
    val q = scala.collection.mutable.Queue[Int]()
    val seen = Array.ofDim[Boolean](target + 1)
    q.enqueue(1)
    seen(1) = true
    var moves = 0
    while (q.nonEmpty) {
      val sz = q.size
      var s = 0
      while (s < sz) {
        val cur = q.dequeue()
        if (cur == target) return moves
        val lim = math.min(cur + 6, target)
        var nxt = cur + 1
        while (nxt <= lim) {
          val (r, c) = pos(nxt)
          val dest = if (board(r)(c) != -1) board(r)(c) else nxt
          if (!seen(dest)) {
            seen(dest) = true
            q.enqueue(dest)
          }
          nxt += 1
        }
        s += 1
      }
      moves += 1
    }
    -1
  }
}
''')

write("0910_smallest_range_ii", r'''// LeetCode 0910 - Smallest Range II
// https://leetcode.com/problems/smallest-range-ii/

object Solution {
  def smallestRangeII(nums: Array[Int], k: Int): Int = {
    val arr = nums.sorted
    var ans = arr.last - arr(0)
    var i = 0
    while (i + 1 < arr.length) {
      val lo = math.min(arr(0) + k, arr(i + 1) - k)
      val hi = math.max(arr.last - k, arr(i) + k)
      ans = math.min(ans, hi - lo)
      i += 1
    }
    ans
  }
}
''')

write("0911_online_election", r'''// LeetCode 0911 - Online Election
// https://leetcode.com/problems/online-election/

class TopVotedCandidate(_persons: Array[Int], _times: Array[Int]) {
  private val times = _times
  private val leaders = Array.ofDim[Int](_persons.length)

  {
    val counts = scala.collection.mutable.Map.empty[Int, Int]
    var leader = -1
    var i = 0
    while (i < _persons.length) {
      counts(_persons(i)) = counts.getOrElse(_persons(i), 0) + 1
      if (leader == -1 || counts(_persons(i)) >= counts(leader)) leader = _persons(i)
      leaders(i) = leader
      i += 1
    }
  }

  def q(t: Int): Int = {
    var lo = 0
    var hi = times.length - 1
    while (lo <= hi) {
      val mid = (lo + hi) >>> 1
      if (times(mid) <= t) lo = mid + 1
      else hi = mid - 1
    }
    leaders(hi)
  }
}
''')

write("0912_sort_an_array", r'''// LeetCode 0912 - Sort an Array
// https://leetcode.com/problems/sort-an-array/

object Solution {
  def sortArray(nums: Array[Int]): Array[Int] = {
    if (nums.length <= 1) return nums
    val mid = nums.length / 2
    val left = sortArray(nums.slice(0, mid))
    val right = sortArray(nums.slice(mid, nums.length))
    val merged = Array.ofDim[Int](nums.length)
    var i = 0
    var j = 0
    var k = 0
    while (i < left.length && j < right.length) {
      if (left(i) <= right(j)) { merged(k) = left(i); i += 1 }
      else { merged(k) = right(j); j += 1 }
      k += 1
    }
    while (i < left.length) { merged(k) = left(i); i += 1; k += 1 }
    while (j < right.length) { merged(k) = right(j); j += 1; k += 1 }
    merged
  }
}
''')

write("0913_cat_and_mouse", r'''// LeetCode 0913 - Cat and Mouse
// https://leetcode.com/problems/cat-and-mouse/

object Solution {
  def catMouseGame(graph: Array[Array[Int]]): Int = {
    val n = graph.length
    val DRAW = 0
    val MOUSE_WIN = 1
    val CAT_WIN = 2
    val states = Array.ofDim[Int](n, n, 2)
    val outDegree = Array.ofDim[Int](n, n, 2)
    val q = scala.collection.mutable.Queue[Array[Int]]()
    var cat = 0
    while (cat < n) {
      var mouse = 0
      while (mouse < n) {
        outDegree(cat)(mouse)(0) = graph(mouse).length
        var deg = 0
        graph(cat).foreach { x => if (x != 0) deg += 1 }
        outDegree(cat)(mouse)(1) = deg
        mouse += 1
      }
      cat += 1
    }
    cat = 1
    while (cat < n) {
      var move = 0
      while (move < 2) {
        states(cat)(0)(move) = MOUSE_WIN
        q.enqueue(Array(cat, 0, move, MOUSE_WIN))
        states(cat)(cat)(move) = CAT_WIN
        q.enqueue(Array(cat, cat, move, CAT_WIN))
        move += 1
      }
      cat += 1
    }
    while (q.nonEmpty) {
      val cur = q.dequeue()
      cat = cur(0)
      val mouse = cur(1)
      val move = cur(2)
      val state = cur(3)
      if (cat == 2 && mouse == 1 && move == 0) return state
      val prevMove = move ^ 1
      graph(if (prevMove == 1) cat else mouse).foreach { prev =>
        val prevCat = if (prevMove == 1) prev else cat
        if (prevCat != 0) {
          val prevMouse = if (prevMove == 1) mouse else prev
          if (states(prevCat)(prevMouse)(prevMove) == 0) {
            if ((prevMove == 0 && state == MOUSE_WIN) ||
                (prevMove == 1 && state == CAT_WIN) ||
                outDegree(prevCat)(prevMouse)(prevMove) == 1) {
              states(prevCat)(prevMouse)(prevMove) = state
              q.enqueue(Array(prevCat, prevMouse, prevMove, state))
            } else {
              outDegree(prevCat)(prevMouse)(prevMove) -= 1
            }
          }
        }
      }
    }
    states(2)(1)(0)
  }
}
''')

write("0914_x_of_a_kind_in_a_deck_of_cards", r'''// LeetCode 0914 - X of a Kind in a Deck of Cards
// https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

object Solution {
  def hasGroupsSizeX(deck: Array[Int]): Boolean = {
    val count = scala.collection.mutable.Map.empty[Int, Int]
    deck.foreach { x => count(x) = count.getOrElse(x, 0) + 1 }
    def gcd(a0: Int, b0: Int): Int = {
      var a = a0
      var b = b0
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    var g = 0
    count.values.foreach { c => g = gcd(g, c) }
    g >= 2
  }
}
''')

write("0915_partition_array_into_disjoint_intervals", r'''// LeetCode 0915 - Partition Array into Disjoint Intervals
// https://leetcode.com/problems/partition-array-into-disjoint-intervals/

object Solution {
  def partitionDisjoint(nums: Array[Int]): Int = {
    val n = nums.length
    val minRight = Array.ofDim[Int](n)
    minRight(n - 1) = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      minRight(i) = math.min(nums(i), minRight(i + 1))
      i -= 1
    }
    var maxLeft = nums(0)
    i = 1
    while (i < n) {
      if (maxLeft <= minRight(i)) return i
      maxLeft = math.max(maxLeft, nums(i))
      i += 1
    }
    n - 1
  }
}
''')

write("0916_word_subsets", r'''// LeetCode 0916 - Word Subsets
// https://leetcode.com/problems/word-subsets/

object Solution {
  def wordSubsets(words1: Array[String], words2: Array[String]): List[String] = {
    val need = Array.ofDim[Int](26)
    words2.foreach { w =>
      val cnt = Array.ofDim[Int](26)
      w.foreach { c => cnt(c - 'a') += 1 }
      var i = 0
      while (i < 26) {
        need(i) = math.max(need(i), cnt(i))
        i += 1
      }
    }
    val ans = scala.collection.mutable.ListBuffer[String]()
    words1.foreach { w =>
      val cnt = Array.ofDim[Int](26)
      w.foreach { c => cnt(c - 'a') += 1 }
      var ok = true
      var i = 0
      while (i < 26) {
        if (cnt(i) < need(i)) ok = false
        i += 1
      }
      if (ok) ans += w
    }
    ans.toList
  }
}
''')

write("0917_reverse_only_letters", r'''// LeetCode 0917 - Reverse Only Letters
// https://leetcode.com/problems/reverse-only-letters/

object Solution {
  def reverseOnlyLetters(s: String): String = {
    val arr = s.toCharArray
    var i = 0
    var j = arr.length - 1
    while (i < j) {
      while (i < j && !arr(i).isLetter) i += 1
      while (i < j && !arr(j).isLetter) j -= 1
      val tmp = arr(i)
      arr(i) = arr(j)
      arr(j) = tmp
      i += 1
      j -= 1
    }
    new String(arr)
  }
}
''')

write("0918_maximum_sum_circular_subarray", r'''// LeetCode 0918 - Maximum Sum Circular Subarray
// https://leetcode.com/problems/maximum-sum-circular-subarray/

object Solution {
  def maxSubarraySumCircular(nums: Array[Int]): Int = {
    var total = 0
    nums.foreach(x => total += x)
    var maxSum = nums(0)
    var minSum = nums(0)
    var curMax = nums(0)
    var curMin = nums(0)
    var i = 1
    while (i < nums.length) {
      curMax = math.max(nums(i), curMax + nums(i))
      curMin = math.min(nums(i), curMin + nums(i))
      maxSum = math.max(maxSum, curMax)
      minSum = math.min(minSum, curMin)
      i += 1
    }
    if (maxSum < 0) maxSum
    else math.max(maxSum, total - minSum)
  }
}
''')

write("0919_complete_binary_tree_inserter", f'''// LeetCode 0919 - Complete Binary Tree Inserter
// https://leetcode.com/problems/complete-binary-tree-inserter/

{TREE}
class CBTInserter(_root: TreeNode) {{
  private val root = _root
  private val parents = scala.collection.mutable.Queue[TreeNode]()

  {{
    val q = scala.collection.mutable.Queue[TreeNode]()
    q.enqueue(root)
    var done = false
    while (q.nonEmpty && !done) {{
      val node = q.dequeue()
      if (node.left != null) q.enqueue(node.left)
      else {{
        parents.enqueue(node)
        done = true
      }}
      if (!done) {{
        if (node.right != null) q.enqueue(node.right)
        else {{
          parents.enqueue(node)
          done = true
        }}
      }}
    }}
    while (q.nonEmpty) parents.enqueue(q.dequeue())
  }}

  def insert(`val`: Int): Int = {{
    val parent = parents.front
    val child = new TreeNode(`val`)
    if (parent.left == null) parent.left = child
    else {{
      parent.right = child
      parents.dequeue()
    }}
    parents.enqueue(child)
    parent.value
  }}

  def get_root(): TreeNode = root
  def getRoot(): TreeNode = root
}}
''')

write("0920_number_of_music_playlists", r'''// LeetCode 0920 - Number of Music Playlists
// https://leetcode.com/problems/number-of-music-playlists/

object Solution {
  def numMusicPlaylists(n: Int, goal: Int, k: Int): Int = {
    val MOD = 1000000007
    val dp = Array.ofDim[Long](goal + 1, n + 1)
    dp(0)(0) = 1
    var i = 1
    while (i <= goal) {
      var j = 1
      while (j <= i && j <= n) {
        dp(i)(j) = dp(i - 1)(j - 1) * (n - j + 1) % MOD
        if (j > k) dp(i)(j) = (dp(i)(j) + dp(i - 1)(j) * (j - k)) % MOD
        j += 1
      }
      i += 1
    }
    dp(goal)(n).toInt
  }
}
''')

write("0921_minimum_add_to_make_parentheses_valid", r'''// LeetCode 0921 - Minimum Add to Make Parentheses Valid
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

object Solution {
  def minAddToMakeValid(s: String): Int = {
    var openNeed = 0
    var closeNeed = 0
    s.foreach { ch =>
      if (ch == '(') closeNeed += 1
      else if (closeNeed > 0) closeNeed -= 1
      else openNeed += 1
    }
    openNeed + closeNeed
  }
}
''')

write("0922_sort_array_by_parity_ii", r'''// LeetCode 0922 - Sort Array By Parity II
// https://leetcode.com/problems/sort-array-by-parity-ii/

object Solution {
  def sortArrayByParityII(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val ans = Array.ofDim[Int](n)
    var even = 0
    var odd = 1
    nums.foreach { x =>
      if (x % 2 == 0) { ans(even) = x; even += 2 }
      else { ans(odd) = x; odd += 2 }
    }
    ans
  }
}
''')

write("0923_3sum_with_multiplicity", r'''// LeetCode 0923 - 3Sum With Multiplicity
// https://leetcode.com/problems/3sum-with-multiplicity/

object Solution {
  def threeSumMulti(arr: Array[Int], target: Int): Int = {
    val MOD = 1000000007
    val count = Array.ofDim[Long](101)
    arr.foreach { x => count(x) += 1 }
    var ans = 0L
    var a = 0
    while (a <= 100) {
      if (count(a) > 0) {
        var b = a
        while (b <= 100) {
          if (count(b) > 0) {
            val c = target - a - b
            if (c >= b && c <= 100 && count(c) != 0) {
              if (a == b && b == c) ans += count(a) * (count(a) - 1) * (count(a) - 2) / 6
              else if (a == b) ans += count(a) * (count(a) - 1) / 2 * count(c)
              else if (b == c) ans += count(a) * count(b) * (count(b) - 1) / 2
              else ans += count(a) * count(b) * count(c)
            }
          }
          b += 1
        }
      }
      a += 1
    }
    (ans % MOD).toInt
  }
}
''')

write("0924_minimize_malware_spread", r'''// LeetCode 0924 - Minimize Malware Spread
// https://leetcode.com/problems/minimize-malware-spread/

object Solution {
  def minMalwareSpread(graph: Array[Array[Int]], initial: Array[Int]): Int = {
    val n = graph.length
    val parent = Array.tabulate(n)(identity)
    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        if (graph(i)(j) == 1) parent(find(i)) = find(j)
        j += 1
      }
      i += 1
    }
    val compSize = Array.ofDim[Int](n)
    val malCount = Array.ofDim[Int](n)
    val isInit = Array.ofDim[Boolean](n)
    initial.foreach { m => isInit(m) = true }
    i = 0
    while (i < n) {
      val r = find(i)
      compSize(r) += 1
      if (isInit(i)) malCount(r) += 1
      i += 1
    }
    var best = initial.min
    var bestSave = -1
    initial.foreach { m =>
      val r = find(m)
      if (malCount(r) == 1) {
        val save = compSize(r) - 1
        if (save > bestSave || (save == bestSave && m < best)) {
          bestSave = save
          best = m
        }
      }
    }
    best
  }
}
''')

write("0925_long_pressed_name", r'''// LeetCode 0925 - Long Pressed Name
// https://leetcode.com/problems/long-pressed-name/

object Solution {
  def isLongPressedName(name: String, typed: String): Boolean = {
    var i = 0
    var j = 0
    while (j < typed.length) {
      if (i < name.length && name.charAt(i) == typed.charAt(j)) { i += 1; j += 1 }
      else if (j > 0 && typed.charAt(j) == typed.charAt(j - 1)) j += 1
      else return false
    }
    i == name.length
  }
}
''')

write("0926_flip_string_to_monotone_increasing", r'''// LeetCode 0926 - Flip String to Monotone Increasing
// https://leetcode.com/problems/flip-string-to-monotone-increasing/

object Solution {
  def minFlipsMonoIncr(s: String): Int = {
    var ones = 0
    var ans = 0
    s.foreach { ch =>
      if (ch == '1') ones += 1
      else ans = math.min(ans + 1, ones)
    }
    ans
  }
}
''')

write("0927_three_equal_parts", r'''// LeetCode 0927 - Three Equal Parts
// https://leetcode.com/problems/three-equal-parts/

object Solution {
  def threeEqualParts(arr: Array[Int]): Array[Int] = {
    val ones = scala.collection.mutable.ArrayBuffer[Int]()
    var i = 0
    while (i < arr.length) {
      if (arr(i) != 0) ones += i
      i += 1
    }
    val n = ones.length
    if (n % 3 != 0) return Array(-1, -1)
    if (n == 0) return Array(0, arr.length - 1)
    val third = n / 3
    val length = ones.last - ones(2 * third) + 1
    val a = ones(0)
    val b = ones(third)
    val c = ones(2 * third)
    if (a + length > arr.length || b + length > arr.length || c + length > arr.length)
      return Array(-1, -1)
    i = 0
    while (i < length) {
      if (arr(a + i) != arr(b + i) || arr(a + i) != arr(c + i)) return Array(-1, -1)
      i += 1
    }
    Array(a + length - 1, b + length)
  }
}
''')

write("0928_minimize_malware_spread_ii", r'''// LeetCode 0928 - Minimize Malware Spread II
// https://leetcode.com/problems/minimize-malware-spread-ii/

object Solution {
  def minMalwareSpread(graph: Array[Array[Int]], initial: Array[Int]): Int = {
    val n = graph.length
    val initSet = initial.toSet
    val clean = (0 until n).filter(!initSet.contains(_)).toArray
    val parent = Array.tabulate(n)(identity)
    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }
    clean.foreach { i =>
      clean.foreach { j =>
        if (i < j && graph(i)(j) == 1) parent(find(i)) = find(j)
      }
    }
    val compSize = scala.collection.mutable.Map.empty[Int, Int]
    clean.foreach { node =>
      val r = find(node)
      compSize(r) = compSize.getOrElse(r, 0) + 1
    }
    val touch = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.Set[Int]]
    initial.foreach { m =>
      clean.foreach { node =>
        if (graph(m)(node) == 1) {
          val r = find(node)
          touch.getOrElseUpdate(r, scala.collection.mutable.Set.empty[Int]) += m
        }
      }
    }
    var best = initial.min
    var bestSave = -1
    initial.foreach { m =>
      var save = 0
      touch.foreach { case (r, ms) =>
        if (ms.size == 1 && ms.contains(m)) save += compSize(r)
      }
      if (save > bestSave || (save == bestSave && m < best)) {
        bestSave = save
        best = m
      }
    }
    best
  }
}
''')

write("0929_unique_email_addresses", r'''// LeetCode 0929 - Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/

object Solution {
  def numUniqueEmails(emails: Array[String]): Int = {
    val normalized = scala.collection.mutable.Set.empty[String]
    emails.foreach { email =>
      val at = email.indexOf('@')
      var local = email.substring(0, at)
      val domain = email.substring(at)
      val plus = local.indexOf('+')
      if (plus >= 0) local = local.substring(0, plus)
      val cleaned = new StringBuilder
      local.foreach { c => if (c != '.') cleaned.append(c) }
      normalized += cleaned.toString + domain
    }
    normalized.size
  }
}
''')

print("done part a")
