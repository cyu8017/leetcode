#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

TREE = """class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}
"""

LISTN = """class ListNode(var x: Int = 0) {
  var next: ListNode = null
}
"""


def hdr(num: str, title: str, slug: str) -> str:
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n\n"


FILES = {}

FILES["0780_reaching_points"] = hdr("0780", "Reaching Points", "reaching-points") + """object Solution {
  def reachingPoints(sx: Int, sy: Int, tx: Int, ty: Int): Boolean = {
    var x = tx
    var y = ty
    while (x >= sx && y >= sy) {
      if (x == sx && y == sy) return true
      if (x == y) return false
      if (x > y) {
        if (y > sy) x %= y
        else return (x - sx) % y == 0
      } else {
        if (x > sx) y %= x
        else return (y - sy) % x == 0
      }
    }
    x == sx && y == sy
  }
}
"""

FILES["0781_rabbits_in_forest"] = hdr("0781", "Rabbits in Forest", "rabbits-in-forest") + """object Solution {
  def numRabbits(answers: Array[Int]): Int = {
    val counts = scala.collection.mutable.Map.empty[Int, Int]
    answers.foreach { a => counts(a) = counts.getOrElse(a, 0) + 1 }
    var total = 0
    counts.foreach { case (ans, cnt) =>
      val group = ans + 1
      val groups = (cnt + group - 1) / group
      total += groups * group
    }
    total
  }
}
"""

FILES["0782_transform_to_chessboard"] = hdr("0782", "Transform to Chessboard", "transform-to-chessboard") + """object Solution {
  def movesToChessboard(board: Array[Array[Int]]): Int = {
    val n = board.length
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if ((board(0)(0) ^ board(i)(0) ^ board(0)(j) ^ board(i)(j)) != 0) return -1
        j += 1
      }
      i += 1
    }
    var rowSum = 0
    var colSum = 0
    i = 0
    while (i < n) {
      rowSum += board(0)(i)
      colSum += board(i)(0)
      i += 1
    }
    if (rowSum < n / 2 || rowSum > (n + 1) / 2) return -1
    if (colSum < n / 2 || colSum > (n + 1) / 2) return -1
    var rowSwap = 0
    var colSwap = 0
    i = 0
    while (i < n) {
      if (board(0)(i) != i % 2) rowSwap += 1
      if (board(i)(0) != i % 2) colSwap += 1
      i += 1
    }
    if (n % 2 == 1) {
      if (rowSwap % 2 == 1) rowSwap = n - rowSwap
      if (colSwap % 2 == 1) colSwap = n - colSwap
    } else {
      rowSwap = math.min(rowSwap, n - rowSwap)
      colSwap = math.min(colSwap, n - colSwap)
    }
    (rowSwap + colSwap) / 2
  }
}
"""

FILES["0783_minimum_distance_between_bst_nodes"] = hdr("0783", "Minimum Distance Between BST Nodes", "minimum-distance-between-bst-nodes") + TREE + """
object Solution {
  def minDiffInBST(root: TreeNode): Int = {
    var hasPrev = false
    var prev = 0
    var best = Int.MaxValue
    def inorder(node: TreeNode): Unit = {
      if (node == null) return
      inorder(node.left)
      if (hasPrev) best = math.min(best, node.value - prev)
      prev = node.value
      hasPrev = true
      inorder(node.right)
    }
    inorder(root)
    best
  }
}
"""

FILES["0784_letter_case_permutation"] = hdr("0784", "Letter Case Permutation", "letter-case-permutation") + """object Solution {
  def letterCasePermutation(s: String): List[String] = {
    var result = List("")
    s.foreach { ch =>
      if (ch.isLetter) {
        val lower = ch.toLower
        val upper = ch.toUpper
        result = result.flatMap(p => List(p + lower, p + upper))
      } else {
        result = result.map(_ + ch)
      }
    }
    result
  }
}
"""

FILES["0785_is_graph_bipartite"] = hdr("0785", "Is Graph Bipartite?", "is-graph-bipartite") + """object Solution {
  def isBipartite(graph: Array[Array[Int]]): Boolean = {
    val color = Array.fill(graph.length)(-1)
    def dfs(node: Int, c: Int): Boolean = {
      color(node) = c
      graph(node).foreach { nei =>
        if (color(nei) == -1) {
          if (!dfs(nei, c ^ 1)) return false
        } else if (color(nei) == c) return false
      }
      true
    }
    graph.indices.foreach { node =>
      if (color(node) == -1 && !dfs(node, 0)) return false
    }
    true
  }
}
"""

FILES["0786_k_th_smallest_prime_fraction"] = hdr("0786", "K-th Smallest Prime Fraction", "k-th-smallest-prime-fraction") + """object Solution {
  def kthSmallestPrimeFraction(arr: Array[Int], k: Int): Array[Int] = {
    val n = arr.length
    val heap = scala.collection.mutable.PriorityQueue.empty[(Int, Int)](
      Ordering.by[(Int, Int), Double] { case (i, j) => arr(i).toDouble / arr(j) }.reverse
    )
    var i = 0
    while (i < n - 1) {
      heap.enqueue((i, n - 1))
      i += 1
    }
    var t = 0
    while (t < k - 1) {
      val (ii, jj) = heap.dequeue()
      if (jj - 1 > ii) heap.enqueue((ii, jj - 1))
      t += 1
    }
    val (a, b) = heap.dequeue()
    Array(arr(a), arr(b))
  }
}
"""

FILES["0787_cheapest_flights_within_k_stops"] = hdr("0787", "Cheapest Flights Within K Stops", "cheapest-flights-within-k-stops") + """object Solution {
  def findCheapestPrice(n: Int, flights: Array[Array[Int]], src: Int, dst: Int, k: Int): Int = {
    val INF = Int.MaxValue / 4
    var dist = Array.fill(n)(INF)
    dist(src) = 0
    var i = 0
    while (i <= k) {
      val nxt = dist.clone()
      flights.foreach { f =>
        val u = f(0); val v = f(1); val price = f(2)
        if (dist(u) != INF && dist(u) + price < nxt(v)) nxt(v) = dist(u) + price
      }
      dist = nxt
      i += 1
    }
    if (dist(dst) == INF) -1 else dist(dst)
  }
}
"""

FILES["0788_rotated_digits"] = hdr("0788", "Rotated Digits", "rotated-digits") + """object Solution {
  def rotatedDigits(n: Int): Int = {
    var count = 0
    var num = 1
    while (num <= n) {
      val s = num.toString
      var ok = true
      var changed = false
      s.foreach { ch =>
        if (ch == '3' || ch == '4' || ch == '7') ok = false
        if (ch == '2' || ch == '5' || ch == '6' || ch == '9') changed = true
      }
      if (ok && changed) count += 1
      num += 1
    }
    count
  }
}
"""

FILES["0789_escape_the_ghosts"] = hdr("0789", "Escape The Ghosts", "escape-the-ghosts") + """object Solution {
  def escapeGhosts(ghosts: Array[Array[Int]], target: Array[Int]): Boolean = {
    val targetDist = math.abs(target(0)) + math.abs(target(1))
    !ghosts.exists { g =>
      math.abs(g(0) - target(0)) + math.abs(g(1) - target(1)) <= targetDist
    }
  }
}
"""

FILES["0790_domino_and_tromino_tiling"] = hdr("0790", "Domino and Tromino Tiling", "domino-and-tromino-tiling") + """object Solution {
  def numTilings(n: Int): Int = {
    val MOD = 1000000007
    if (n == 1) return 1
    if (n == 2) return 2
    val dp = Array.ofDim[Long](n + 1)
    dp(1) = 1
    dp(2) = 2
    dp(3) = 5
    var i = 4
    while (i <= n) {
      dp(i) = (2 * dp(i - 1) + dp(i - 3)) % MOD
      i += 1
    }
    dp(n).toInt
  }
}
"""

FILES["0791_custom_sort_string"] = hdr("0791", "Custom Sort String", "custom-sort-string") + """object Solution {
  def customSortString(order: String, s: String): String = {
    val count = Array.ofDim[Int](26)
    s.foreach(ch => count(ch - 'a') += 1)
    val sb = new StringBuilder
    order.foreach { ch =>
      while (count(ch - 'a') > 0) {
        sb.append(ch)
        count(ch - 'a') -= 1
      }
    }
    var i = 0
    while (i < 26) {
      while (count(i) > 0) {
        sb.append(('a' + i).toChar)
        count(i) -= 1
      }
      i += 1
    }
    sb.toString
  }
}
"""

FILES["0792_number_of_matching_subsequences"] = hdr("0792", "Number of Matching Subsequences", "number-of-matching-subsequences") + """object Solution {
  def numMatchingSubseq(s: String, words: Array[String]): Int = {
    val waiting = Array.fill(26)(scala.collection.mutable.ListBuffer.empty[(Int, Int)])
    words.indices.foreach { i =>
      waiting(words(i).charAt(0) - 'a') += ((i, 0))
    }
    var ans = 0
    s.foreach { ch =>
      val cur = waiting(ch - 'a').toList
      waiting(ch - 'a').clear()
      cur.foreach { case (wi, idx0) =>
        val idx = idx0 + 1
        if (idx == words(wi).length) ans += 1
        else waiting(words(wi).charAt(idx) - 'a') += ((wi, idx))
      }
    }
    ans
  }
}
"""

FILES["0793_preimage_size_of_factorial_zeroes_function"] = hdr("0793", "Preimage Size of Factorial Zeroes Function", "preimage-size-of-factorial-zeroes-function") + """object Solution {
  def preimageSizeFZF(k: Int): Int = {
    def zeros(n0: Long): Long = {
      var n = n0
      var z = 0L
      while (n > 0) {
        n /= 5
        z += n
      }
      z
    }
    def firstGe(target: Long): Long = {
      var lo = 0L
      var hi = 5L * target + 5
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (zeros(mid) >= target) hi = mid
        else lo = mid + 1
      }
      lo
    }
    (firstGe(k.toLong + 1) - firstGe(k.toLong)).toInt
  }
}
"""

FILES["0794_valid_tic_tac_toe_state"] = hdr("0794", "Valid Tic-Tac-Toe State", "valid-tic-tac-toe-state") + """object Solution {
  def validTicTacToe(board: Array[String]): Boolean = {
    var x = 0
    var o = 0
    board.foreach { row =>
      row.foreach { ch =>
        if (ch == 'X') x += 1
        else if (ch == 'O') o += 1
      }
    }
    if (o > x || x - o > 1) return false
    def win(player: Char): Boolean = {
      var i = 0
      while (i < 3) {
        if (board(i).charAt(0) == player && board(i).charAt(1) == player && board(i).charAt(2) == player) return true
        if (board(0).charAt(i) == player && board(1).charAt(i) == player && board(2).charAt(i) == player) return true
        i += 1
      }
      if (board(0).charAt(0) == player && board(1).charAt(1) == player && board(2).charAt(2) == player) return true
      board(0).charAt(2) == player && board(1).charAt(1) == player && board(2).charAt(0) == player
    }
    val xWin = win('X')
    val oWin = win('O')
    if (xWin && oWin) return false
    if (xWin && x != o + 1) return false
    if (oWin && x != o) return false
    true
  }
}
"""

FILES["0795_number_of_subarrays_with_bounded_maximum"] = hdr("0795", "Number of Subarrays with Bounded Maximum", "number-of-subarrays-with-bounded-maximum") + """object Solution {
  def numSubarrayBoundedMax(nums: Array[Int], left: Int, right: Int): Int = {
    def countAtMost(bound: Int): Int = {
      var ans = 0
      var cur = 0
      nums.foreach { num =>
        if (num <= bound) {
          cur += 1
          ans += cur
        } else cur = 0
      }
      ans
    }
    countAtMost(right) - countAtMost(left - 1)
  }
}
"""

FILES["0796_rotate_string"] = hdr("0796", "Rotate String", "rotate-string") + """object Solution {
  def rotateString(s: String, goal: String): Boolean = {
    s.length == goal.length && (s + s).contains(goal)
  }
}
"""

FILES["0797_all_paths_from_source_to_target"] = hdr("0797", "All Paths From Source to Target", "all-paths-from-source-to-target") + """object Solution {
  def allPathsSourceTarget(graph: Array[Array[Int]]): List[List[Int]] = {
    val target = graph.length - 1
    val answer = scala.collection.mutable.ListBuffer.empty[List[Int]]
    val path = scala.collection.mutable.ListBuffer(0)
    def dfs(node: Int): Unit = {
      if (node == target) {
        answer += path.toList
        return
      }
      graph(node).foreach { nei =>
        path += nei
        dfs(nei)
        path.remove(path.length - 1)
      }
    }
    dfs(0)
    answer.toList
  }
}
"""

FILES["0798_smallest_rotation_with_highest_score"] = hdr("0798", "Smallest Rotation with Highest Score", "smallest-rotation-with-highest-score") + """object Solution {
  def bestRotation(nums: Array[Int]): Int = {
    val n = nums.length
    val change = Array.fill(n)(1)
    var i = 0
    while (i < n) {
      change((i - nums(i) + 1 + n) % n) -= 1
      i += 1
    }
    i = 1
    while (i < n) {
      change(i) += change(i - 1)
      i += 1
    }
    var best = 0
    i = 1
    while (i < n) {
      if (change(i) > change(best)) best = i
      i += 1
    }
    best
  }
}
"""

FILES["0799_champagne_tower"] = hdr("0799", "Champagne Tower", "champagne-tower") + """object Solution {
  def champagneTower(poured: Int, query_row: Int, query_glass: Int): Double = {
    var row = Array(poured.toDouble)
    var r = 0
    while (r < query_row) {
      val nextRow = Array.ofDim[Double](r + 2)
      var i = 0
      while (i < row.length) {
        val overflow = (row(i) - 1.0) / 2.0
        if (overflow > 0) {
          nextRow(i) += overflow
          nextRow(i + 1) += overflow
        }
        i += 1
      }
      row = nextRow
      r += 1
    }
    math.min(1.0, row(query_glass))
  }
}
"""

FILES["0800_similar_rgb_color"] = hdr("0800", "Similar RGB Color", "similar-rgb-color") + """object Solution {
  def similarRGB(color: String): String = {
    def closest(component: String): String = {
      val value = Integer.parseInt(component, 16)
      val rounded = (value + 8) / 17
      f"$rounded%x$rounded%x"
    }
    "#" + closest(color.substring(1, 3)) + closest(color.substring(3, 5)) + closest(color.substring(5, 7))
  }
}
"""

FILES["0801_minimum_swaps_to_make_sequences_increasing"] = hdr("0801", "Minimum Swaps To Make Sequences Increasing", "minimum-swaps-to-make-sequences-increasing") + """object Solution {
  def minSwap(nums1: Array[Int], nums2: Array[Int]): Int = {
    val n = nums1.length
    val swap = Array.fill(n)(n)
    val keep = Array.fill(n)(n)
    swap(0) = 1
    keep(0) = 0
    var i = 1
    while (i < n) {
      if (nums1(i) > nums1(i - 1) && nums2(i) > nums2(i - 1)) {
        keep(i) = keep(i - 1)
        swap(i) = swap(i - 1) + 1
      }
      if (nums1(i) > nums2(i - 1) && nums2(i) > nums1(i - 1)) {
        keep(i) = math.min(keep(i), swap(i - 1))
        swap(i) = math.min(swap(i), keep(i - 1) + 1)
      }
      i += 1
    }
    math.min(swap(n - 1), keep(n - 1))
  }
}
"""

FILES["0802_find_eventual_safe_states"] = hdr("0802", "Find Eventual Safe States", "find-eventual-safe-states") + """object Solution {
  def eventualSafeNodes(graph: Array[Array[Int]]): List[Int] = {
    val n = graph.length
    val color = Array.ofDim[Int](n)
    def dfs(node: Int): Boolean = {
      if (color(node) != 0) return color(node) == 2
      color(node) = 1
      graph(node).foreach { nei => if (!dfs(nei)) return false }
      color(node) = 2
      true
    }
    (0 until n).filter(dfs).toList
  }
}
"""

FILES["0803_bricks_falling_when_hit"] = hdr("0803", "Bricks Falling When Hit", "bricks-falling-when-hit") + """object Solution {
  def hitBricks(grid: Array[Array[Int]], hits: Array[Array[Int]]): Array[Int] = {
    val m = grid.length
    val n = grid(0).length
    val roof = m * n
    val parent = Array.tabulate(roof + 1)(identity)
    val size = Array.fill(roof + 1)(1)
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
      if (ra == rb) return
      parent(ra) = rb
      size(rb) += size(ra)
    }
    def idx(r: Int, c: Int): Int = r * n + c
    val status = grid.map(_.clone())
    hits.foreach { h => status(h(0))(h(1)) = 0 }
    val dr = Array(-1, 1, 0, 0)
    val dc = Array(0, 0, -1, 1)
    var r = 0
    while (r < m) {
      var c = 0
      while (c < n) {
        if (status(r)(c) != 0) {
          if (r == 0) unite(idx(r, c), roof)
          var k = 0
          while (k < 4) {
            val nr = r + dr(k)
            val nc = c + dc(k)
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && status(nr)(nc) == 1) {
              unite(idx(r, c), idx(nr, nc))
            }
            k += 1
          }
        }
        c += 1
      }
      r += 1
    }
    val answer = Array.ofDim[Int](hits.length)
    var i = hits.length - 1
    while (i >= 0) {
      r = hits(i)(0)
      val c = hits(i)(1)
      if (grid(r)(c) != 0) {
        val prev = size(find(roof))
        status(r)(c) = 1
        if (r == 0) unite(idx(r, c), roof)
        var k = 0
        while (k < 4) {
          val nr = r + dr(k)
          val nc = c + dc(k)
          if (nr >= 0 && nr < m && nc >= 0 && nc < n && status(nr)(nc) == 1) {
            unite(idx(r, c), idx(nr, nc))
          }
          k += 1
        }
        val curr = size(find(roof))
        answer(i) = math.max(0, curr - prev - 1)
      }
      i -= 1
    }
    answer
  }
}
"""

FILES["0804_unique_morse_code_words"] = hdr("0804", "Unique Morse Code Words", "unique-morse-code-words") + """object Solution {
  def uniqueMorseRepresentations(words: Array[String]): Int = {
    val codes = Array(
      ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
      "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
      "..-", "...-", ".--", "-..-", "-.--", "--.."
    )
    words.map(w => w.map(ch => codes(ch - 'a')).mkString).toSet.size
  }
}
"""

FILES["0805_split_array_with_same_average"] = hdr("0805", "Split Array With Same Average", "split-array-with-same-average") + """object Solution {
  def splitArraySameAverage(nums: Array[Int]): Boolean = {
    val n = nums.length
    val total = nums.sum
    scala.util.Sorting.quickSort(nums)
    val memo = scala.collection.mutable.Set.empty[Long]
    def find(target: Int, count: Int, index: Int): Boolean = {
      if (count == 0) return target == 0
      if (index == n || count + index > n || target < 0) return false
      val key = (target.toLong << 20) | (count.toLong << 10) | index
      if (memo.contains(key)) return false
      if (find(target - nums(index), count - 1, index + 1) || find(target, count, index + 1)) return true
      memo += key
      false
    }
    var size = 1
    while (size < n) {
      if ((total * size) % n == 0 && find(total * size / n, size, 0)) return true
      size += 1
    }
    false
  }
}
"""

FILES["0806_number_of_lines_to_write_string"] = hdr("0806", "Number of Lines To Write String", "number-of-lines-to-write-string") + """object Solution {
  def numberOfLines(widths: Array[Int], s: String): Array[Int] = {
    var lines = 1
    var width = 0
    s.foreach { ch =>
      val w = widths(ch - 'a')
      if (width + w > 100) {
        lines += 1
        width = w
      } else width += w
    }
    Array(lines, width)
  }
}
"""

FILES["0807_max_increase_to_keep_city_skyline"] = hdr("0807", "Max Increase to Keep City Skyline", "max-increase-to-keep-city-skyline") + """object Solution {
  def maxIncreaseKeepingSkyline(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val rowMax = Array.ofDim[Int](m)
    val colMax = Array.ofDim[Int](n)
    var r = 0
    while (r < m) {
      var c = 0
      while (c < n) {
        rowMax(r) = math.max(rowMax(r), grid(r)(c))
        colMax(c) = math.max(colMax(c), grid(r)(c))
        c += 1
      }
      r += 1
    }
    var ans = 0
    r = 0
    while (r < m) {
      var c = 0
      while (c < n) {
        ans += math.min(rowMax(r), colMax(c)) - grid(r)(c)
        c += 1
      }
      r += 1
    }
    ans
  }
}
"""

FILES["0808_soup_servings"] = hdr("0808", "Soup Servings", "soup-servings") + """object Solution {
  def soupServings(n: Int): Double = {
    if (n >= 4800) return 1.0
    val units = (n + 24) / 25
    val memo = scala.collection.mutable.Map.empty[Long, Double]
    def dp(a: Int, b: Int): Double = {
      if (a <= 0 && b <= 0) return 0.5
      if (a <= 0) return 1.0
      if (b <= 0) return 0.0
      val key = (a.toLong << 16) | b
      memo.get(key) match {
        case Some(v) => v
        case None =>
          val v = 0.25 * (dp(a - 4, b) + dp(a - 3, b - 1) + dp(a - 2, b - 2) + dp(a - 1, b - 3))
          memo(key) = v
          v
      }
    }
    dp(units, units)
  }
}
"""

FILES["0809_expressive_words"] = hdr("0809", "Expressive Words", "expressive-words") + """object Solution {
  def expressiveWords(s: String, words: Array[String]): Int = {
    def groups(text: String): List[(Int, Int)] = {
      val result = scala.collection.mutable.ListBuffer.empty[(Int, Int)]
      var i = 0
      val n = text.length
      while (i < n) {
        var j = i
        while (j < n && text.charAt(j) == text.charAt(i)) j += 1
        result += ((text.charAt(i), j - i))
        i = j
      }
      result.toList
    }
    val target = groups(s)
    var ans = 0
    words.foreach { word =>
      val source = groups(word)
      if (source.length == target.length) {
        var ok = true
        var i = 0
        while (i < source.length && ok) {
          if (source(i)._1 != target(i)._1) ok = false
          else {
            val c1 = source(i)._2
            val c2 = target(i)._2
            if (c1 > c2 || (c1 != c2 && c2 < 3)) ok = false
          }
          i += 1
        }
        if (ok) ans += 1
      }
    }
    ans
  }
}
"""

FILES["0810_chalkboard_xor_game"] = hdr("0810", "Chalkboard XOR Game", "chalkboard-xor-game") + """object Solution {
  def xorGame(nums: Array[Int]): Boolean = {
    var x = 0
    nums.foreach(num => x ^= num)
    x == 0 || nums.length % 2 == 0
  }
}
"""

FILES["0811_subdomain_visit_count"] = hdr("0811", "Subdomain Visit Count", "subdomain-visit-count") + """object Solution {
  def subdomainVisits(cpdomains: Array[String]): List[String] = {
    val counts = scala.collection.mutable.Map.empty[String, Int]
    cpdomains.foreach { item =>
      val space = item.indexOf(' ')
      val count = item.substring(0, space).toInt
      var domain = item.substring(space + 1)
      var cont = true
      while (cont) {
        counts(domain) = counts.getOrElse(domain, 0) + count
        val dot = domain.indexOf('.')
        if (dot < 0) cont = false
        else domain = domain.substring(dot + 1)
      }
    }
    counts.map { case (k, v) => s"$v $k" }.toList
  }
}
"""

FILES["0812_largest_triangle_area"] = hdr("0812", "Largest Triangle Area", "largest-triangle-area") + """object Solution {
  def largestTriangleArea(points: Array[Array[Int]]): Double = {
    var best = 0.0
    val n = points.length
    var i = 0
    while (i < n) {
      val x1 = points(i)(0); val y1 = points(i)(1)
      var j = i + 1
      while (j < n) {
        val x2 = points(j)(0); val y2 = points(j)(1)
        var k = j + 1
        while (k < n) {
          val x3 = points(k)(0); val y3 = points(k)(1)
          val area = math.abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
          best = math.max(best, area)
          k += 1
        }
        j += 1
      }
      i += 1
    }
    best
  }
}
"""

FILES["0813_largest_sum_of_averages"] = hdr("0813", "Largest Sum of Averages", "largest-sum-of-averages") + """object Solution {
  def largestSumOfAverages(nums: Array[Int], k: Int): Double = {
    val n = nums.length
    val prefix = Array.ofDim[Double](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + nums(i)
      i += 1
    }
    var dp = Array.tabulate(n)(i => (prefix(i + 1) - prefix(0)) / (i + 1))
    var groups = 2
    while (groups <= k) {
      val nxt = Array.ofDim[Double](n)
      i = groups - 1
      while (i < n) {
        var best = 0.0
        var j = groups - 2
        while (j < i) {
          best = math.max(best, dp(j) + (prefix(i + 1) - prefix(j + 1)) / (i - j))
          j += 1
        }
        nxt(i) = best
        i += 1
      }
      dp = nxt
      groups += 1
    }
    dp(n - 1)
  }
}
"""

FILES["0814_binary_tree_pruning"] = hdr("0814", "Binary Tree Pruning", "binary-tree-pruning") + TREE + """
object Solution {
  def pruneTree(root: TreeNode): TreeNode = {
    if (root == null) return null
    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)
    if (root.value == 0 && root.left == null && root.right == null) null else root
  }
}
"""

FILES["0815_bus_routes"] = hdr("0815", "Bus Routes", "bus-routes") + """object Solution {
  def numBusesToDestination(routes: Array[Array[Int]], source: Int, target: Int): Int = {
    if (source == target) return 0
    val stopToBuses = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ListBuffer[Int]]
    routes.indices.foreach { bus =>
      routes(bus).foreach { stop =>
        stopToBuses.getOrElseUpdate(stop, scala.collection.mutable.ListBuffer.empty) += bus
      }
    }
    val queue = scala.collection.mutable.Queue[(Int, Int)]((source, 0))
    val seenStops = scala.collection.mutable.Set(source)
    val seenBuses = scala.collection.mutable.Set.empty[Int]
    while (queue.nonEmpty) {
      val (stop, busesTaken) = queue.dequeue()
      stopToBuses.getOrElse(stop, scala.collection.mutable.ListBuffer.empty[Int]).foreach { bus =>
        if (seenBuses.add(bus)) {
          routes(bus).foreach { nxt =>
            if (nxt == target) return busesTaken + 1
            if (seenStops.add(nxt)) queue.enqueue((nxt, busesTaken + 1))
          }
        }
      }
    }
    -1
  }
}
"""

FILES["0816_ambiguous_coordinates"] = hdr("0816", "Ambiguous Coordinates", "ambiguous-coordinates") + """object Solution {
  def ambiguousCoordinates(s: String): List[String] = {
    val digits = s.substring(1, s.length - 1)
    def candidates(frag: String): List[String] = {
      val options = scala.collection.mutable.ListBuffer.empty[String]
      if (frag.isEmpty || (frag.length > 1 && frag.charAt(0) == '0' && frag.charAt(frag.length - 1) == '0')) {
        return options.toList
      }
      if (frag.charAt(0) == '0' && frag.length > 1) {
        if (frag.charAt(frag.length - 1) != '0') options += ("0." + frag.substring(1))
        return options.toList
      }
      options += frag
      if (frag.charAt(frag.length - 1) == '0') return options.toList
      var i = 1
      while (i < frag.length) {
        options += (frag.substring(0, i) + "." + frag.substring(i))
        i += 1
      }
      options.toList
    }
    val answer = scala.collection.mutable.ListBuffer.empty[String]
    var i = 1
    while (i < digits.length) {
      candidates(digits.substring(0, i)).foreach { left =>
        candidates(digits.substring(i)).foreach { right =>
          answer += s"($left, $right)"
        }
      }
      i += 1
    }
    answer.toList
  }
}
"""

FILES["0817_linked_list_components"] = hdr("0817", "Linked List Components", "linked-list-components") + LISTN + """
object Solution {
  def numComponents(head: ListNode, nums: Array[Int]): Int = {
    val present = nums.toSet
    var count = 0
    var connected = false
    var cur = head
    while (cur != null) {
      if (present.contains(cur.x)) {
        if (!connected) {
          count += 1
          connected = true
        }
      } else connected = false
      cur = cur.next
    }
    count
  }
}
"""

FILES["0818_race_car"] = hdr("0818", "Race Car", "race-car") + """object Solution {
  def racecar(target: Int): Int = {
    def key(pos: Int, speed: Int): Long = (pos.toLong << 20) ^ (speed & 0xfffffL)
    val queue = scala.collection.mutable.Queue[(Int, Int, Int)]((0, 1, 0))
    val seen = scala.collection.mutable.Set(key(0, 1))
    while (queue.nonEmpty) {
      val (pos, speed, steps) = queue.dequeue()
      if (pos == target) return steps
      val nxtPos = pos + speed
      val nxtSpeed = speed * 2
      if (!seen.contains(key(nxtPos, nxtSpeed)) && math.abs(nxtPos) < target * 2) {
        seen += key(nxtPos, nxtSpeed)
        queue.enqueue((nxtPos, nxtSpeed, steps + 1))
      }
      val revSpeed = if (speed > 0) -1 else 1
      if (seen.add(key(pos, revSpeed))) queue.enqueue((pos, revSpeed, steps + 1))
    }
    -1
  }
}
"""

FILES["0819_most_common_word"] = hdr("0819", "Most Common Word", "most-common-word") + """object Solution {
  def mostCommonWord(paragraph: String, banned: Array[String]): String = {
    val bannedSet = banned.toSet
    val counts = scala.collection.mutable.Map.empty[String, Int]
    val word = new StringBuilder
    var best = ""
    var bestCount = 0
    var i = 0
    while (i <= paragraph.length) {
      val ch = if (i < paragraph.length) paragraph.charAt(i) else ' '
      if (ch.isLetter) word.append(ch.toLower)
      else if (word.nonEmpty) {
        val w = word.toString
        word.clear()
        if (!bannedSet.contains(w)) {
          val c = counts.getOrElse(w, 0) + 1
          counts(w) = c
          if (c > bestCount) {
            bestCount = c
            best = w
          }
        }
      }
      i += 1
    }
    best
  }
}
"""

FILES["0820_short_encoding_of_words"] = hdr("0820", "Short Encoding of Words", "short-encoding-of-words") + """object Solution {
  def minimumLengthEncoding(words: Array[String]): Int = {
    val good = scala.collection.mutable.Set(words: _*)
    words.foreach { word =>
      var i = 1
      while (i < word.length) {
        good.remove(word.substring(i))
        i += 1
      }
    }
    good.map(_.length + 1).sum
  }
}
"""

FILES["0821_shortest_distance_to_a_character"] = hdr("0821", "Shortest Distance to a Character", "shortest-distance-to-a-character") + """object Solution {
  def shortestToChar(s: String, c: Char): Array[Int] = {
    val n = s.length
    val ans = Array.ofDim[Int](n)
    var prev = -n
    var i = 0
    while (i < n) {
      if (s.charAt(i) == c) prev = i
      ans(i) = i - prev
      i += 1
    }
    prev = 2 * n
    i = n - 1
    while (i >= 0) {
      if (s.charAt(i) == c) prev = i
      ans(i) = math.min(ans(i), prev - i)
      i -= 1
    }
    ans
  }
}
"""

FILES["0822_card_flipping_game"] = hdr("0822", "Card Flipping Game", "card-flipping-game") + """object Solution {
  def flipgame(fronts: Array[Int], backs: Array[Int]): Int = {
    val same = scala.collection.mutable.Set.empty[Int]
    fronts.indices.foreach { i => if (fronts(i) == backs(i)) same += fronts(i) }
    var best = Int.MaxValue
    fronts.foreach { x => if (!same.contains(x)) best = math.min(best, x) }
    backs.foreach { x => if (!same.contains(x)) best = math.min(best, x) }
    if (best == Int.MaxValue) 0 else best
  }
}
"""

FILES["0823_binary_trees_with_factors"] = hdr("0823", "Binary Trees With Factors", "binary-trees-with-factors") + """object Solution {
  def numFactoredBinaryTrees(arr: Array[Int]): Int = {
    val MOD = 1000000007
    scala.util.Sorting.quickSort(arr)
    val dp = scala.collection.mutable.Map.empty[Int, Long]
    var i = 0
    while (i < arr.length) {
      val x = arr(i)
      var ways = 1L
      var j = 0
      while (j < i) {
        val left = arr(j)
        if (x % left == 0) {
          val right = x / left
          if (dp.contains(right)) ways = (ways + dp(left) * dp(right)) % MOD
        }
        j += 1
      }
      dp(x) = ways
      i += 1
    }
    (dp.values.sum % MOD).toInt
  }
}
"""

FILES["0824_goat_latin"] = hdr("0824", "Goat Latin", "goat-latin") + """object Solution {
  def toGoatLatin(sentence: String): String = {
    val vowels = Set('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    val words = sentence.split(" ")
    words.indices.map { i =>
      val word = words(i)
      val goat = new StringBuilder
      if (vowels.contains(word.charAt(0))) goat.append(word).append("ma")
      else goat.append(word.substring(1)).append(word.charAt(0)).append("ma")
      goat.append("a" * (i + 1))
      goat.toString
    }.mkString(" ")
  }
}
"""

FILES["0825_friends_of_appropriate_ages"] = hdr("0825", "Friends Of Appropriate Ages", "friends-of-appropriate-ages") + """object Solution {
  def numFriendRequests(ages: Array[Int]): Int = {
    val count = Array.ofDim[Int](121)
    ages.foreach(age => count(age) += 1)
    var ans = 0
    var x = 1
    while (x <= 120) {
      if (count(x) != 0) {
        var y = 1
        while (y <= 120) {
          if (count(y) != 0) {
            if (!(y <= 0.5 * x + 7 || y > x || (y > 100 && x < 100))) {
              ans += count(x) * count(y)
              if (x == y) ans -= count(x)
            }
          }
          y += 1
        }
      }
      x += 1
    }
    ans
  }
}
"""

FILES["0826_most_profit_assigning_work"] = hdr("0826", "Most Profit Assigning Work", "most-profit-assigning-work") + """object Solution {
  def maxProfitAssignment(difficulty: Array[Int], profit: Array[Int], worker: Array[Int]): Int = {
    val m = difficulty.length
    val jobs = Array.tabulate(m)(i => (difficulty(i), profit(i)))
    scala.util.Sorting.quickSort(jobs)(Ordering.by(_._1))
    scala.util.Sorting.quickSort(worker)
    var ans = 0
    var best = 0
    var i = 0
    worker.foreach { ability =>
      while (i < m && jobs(i)._1 <= ability) {
        best = math.max(best, jobs(i)._2)
        i += 1
      }
      ans += best
    }
    ans
  }
}
"""

FILES["0827_making_a_large_island"] = hdr("0827", "Making A Large Island", "making-a-large-island") + """object Solution {
  def largestIsland(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val sizes = scala.collection.mutable.Map(0 -> 0)
    def dfs(r: Int, c: Int, iid: Int): Int = {
      if (r < 0 || r >= n || c < 0 || c >= n || grid(r)(c) != 1) return 0
      grid(r)(c) = iid
      1 + dfs(r + 1, c, iid) + dfs(r - 1, c, iid) + dfs(r, c + 1, iid) + dfs(r, c - 1, iid)
    }
    var islandId = 2
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 1) {
          sizes(islandId) = dfs(i, j, islandId)
          islandId += 1
        }
        j += 1
      }
      i += 1
    }
    var ans = sizes.values.foldLeft(0)(math.max)
    val dr = Array(1, -1, 0, 0)
    val dc = Array(0, 0, 1, -1)
    i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 0) {
          val seen = scala.collection.mutable.Set.empty[Int]
          var total = 1
          var k = 0
          while (k < 4) {
            val ni = i + dr(k)
            val nj = j + dc(k)
            if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
              val iid = grid(ni)(nj)
              if (iid > 1 && seen.add(iid)) total += sizes(iid)
            }
            k += 1
          }
          ans = math.max(ans, total)
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
"""

FILES["0828_count_unique_characters_of_all_substrings_of_a_given_string"] = hdr("0828", "Count Unique Characters of All Substrings of a Given String", "count-unique-characters-of-all-substrings-of-a-given-string") + """object Solution {
  def uniqueLetterString(s: String): Int = {
    val n = s.length
    val last = scala.collection.mutable.Map.empty[Char, scala.collection.mutable.ListBuffer[Int]]
    s.foreach { ch => last.getOrElseUpdate(ch, scala.collection.mutable.ListBuffer(-1)) }
    var i = 0
    while (i < n) {
      last(s.charAt(i)) += i
      i += 1
    }
    last.values.foreach(_ += n)
    var ans = 0
    last.values.foreach { indices =>
      var k = 1
      while (k + 1 < indices.length) {
        ans += (indices(k) - indices(k - 1)) * (indices(k + 1) - indices(k))
        k += 1
      }
    }
    ans
  }
}
"""

FILES["0829_consecutive_numbers_sum"] = hdr("0829", "Consecutive Numbers Sum", "consecutive-numbers-sum") + """object Solution {
  def consecutiveNumbersSum(n: Int): Int = {
    var ans = 0
    var k = 1
    while (k.toLong * (k - 1) / 2 < n) {
      if ((n - k * (k - 1) / 2) % k == 0) ans += 1
      k += 1
    }
    ans
  }
}
"""

written = 0
for folder, src in FILES.items():
    path = ROOT / folder / "Solution.scala"
    path.write_text(src, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")
