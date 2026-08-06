# Temporary batch port script for Scala 1242-1299. Delete after use.
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(folder: str, code: str) -> None:
    (ROOT / folder / "Solution.scala").write_text(code.strip() + "\n", encoding="utf-8")
    print(f"wrote {folder}")


S = {}

S["1242_web_crawler_multithreaded"] = r'''
// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

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
    var frontier = List(startUrl)
    while (frontier.nonEmpty) {
      val next = scala.collection.mutable.ListBuffer.empty[String]
      for (urls <- frontier.map(htmlParser.getUrls); url <- urls if host(url) == h && !seen.contains(url)) {
        seen += url
        next += url
      }
      frontier = next.toList
    }
    seen.toList.sorted
  }
}
'''

S["1243_array_transformation"] = r'''
// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

object Solution {
  def transformArray(arr: Array[Int]): List[Int] = {
    var cur = arr.clone()
    var changed = true
    while (changed) {
      changed = false
      val nxt = cur.clone()
      for (i <- 1 until cur.length - 1) {
        if (cur(i) < cur(i - 1) && cur(i) < cur(i + 1)) {
          nxt(i) += 1
          changed = true
        } else if (cur(i) > cur(i - 1) && cur(i) > cur(i + 1)) {
          nxt(i) -= 1
          changed = true
        }
      }
      cur = nxt
    }
    cur.toList
  }
}
'''

S["1244_design_a_leaderboard"] = r'''
// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

class Leaderboard() {
  private val scores = scala.collection.mutable.Map.empty[Int, Int].withDefaultValue(0)

  def addScore(playerId: Int, score: Int): Unit = {
    scores(playerId) += score
  }

  def top(K: Int): Int =
    scores.values.toSeq.sorted(Ordering[Int].reverse).take(K).sum

  def reset(playerId: Int): Unit = {
    scores.remove(playerId)
  }
}
'''

S["1245_tree_diameter"] = r'''
// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

object Solution {
  def treeDiameter(edges: Array[Array[Int]]): Int = {
    if (edges.isEmpty) return 0
    val graph = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ListBuffer[Int]]
    for (e <- edges) {
      graph.getOrElseUpdate(e(0), scala.collection.mutable.ListBuffer.empty) += e(1)
      graph.getOrElseUpdate(e(1), scala.collection.mutable.ListBuffer.empty) += e(0)
    }
    def farthest(start: Int): (Int, Int) = {
      val q = scala.collection.mutable.Queue((start, 0))
      val seen = scala.collection.mutable.Set(start)
      var last = (start, 0)
      while (q.nonEmpty) {
        last = q.dequeue()
        for (v <- graph.getOrElse(last._1, Nil) if !seen.contains(v)) {
          seen += v
          q.enqueue((v, last._2 + 1))
        }
      }
      last
    }
    val endpoint = farthest(edges(0)(0))._1
    farthest(endpoint)._2
  }
}
'''

S["1246_palindrome_removal"] = r'''
// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

object Solution {
  def minimumMoves(arr: Array[Int]): Int = {
    val n = arr.length
    val dp = Array.ofDim[Int](n, n)
    for (i <- 0 until n) dp(i)(i) = 1
    for (length <- 2 to n; i <- 0 to n - length) {
      val j = i + length - 1
      dp(i)(j) = 1 + dp(i + 1)(j)
      if (arr(i) == arr(i + 1)) dp(i)(j) = math.min(dp(i)(j), 1 + (if (i + 2 <= j) dp(i + 2)(j) else 0))
      for (k <- i + 2 to j if arr(i) == arr(k)) {
        dp(i)(j) = math.min(dp(i)(j), dp(i + 1)(k - 1) + (if (k < j) dp(k + 1)(j) else 0))
      }
    }
    dp(0)(n - 1)
  }
}
'''

S["1247_minimum_swaps_to_make_strings_equal"] = r'''
// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

object Solution {
  def minimumSwap(s1: String, s2: String): Int = {
    var xy = 0
    var yx = 0
    for (i <- s1.indices) {
      if (s1(i) == 'x' && s2(i) == 'y') xy += 1
      else if (s1(i) == 'y' && s2(i) == 'x') yx += 1
    }
    if ((xy + yx) % 2 != 0) -1 else xy / 2 + yx / 2 + 2 * (xy % 2)
  }
}
'''

S["1248_count_number_of_nice_subarrays"] = r'''
// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

object Solution {
  def numberOfSubarrays(nums: Array[Int], k: Int): Int = {
    val frequency = scala.collection.mutable.Map(0 -> 1).withDefaultValue(0)
    var odd = 0
    var answer = 0
    for (x <- nums) {
      odd += x & 1
      answer += frequency(odd - k)
      frequency(odd) += 1
    }
    answer
  }
}
'''

S["1249_minimum_remove_to_make_valid_parentheses"] = r'''
// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

object Solution {
  def minRemoveToMakeValid(s: String): String = {
    val chars = s.toArray
    val opens = scala.collection.mutable.Stack[Int]()
    for (i <- chars.indices) {
      if (chars(i) == '(') opens.push(i)
      else if (chars(i) == ')') {
        if (opens.nonEmpty) opens.pop()
        else chars(i) = 0
      }
    }
    while (opens.nonEmpty) chars(opens.pop()) = 0
    chars.filter(_ != 0).mkString
  }
}
'''

S["1250_check_if_it_is_a_good_array"] = r'''
// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

object Solution {
  def isGoodArray(nums: Array[Int]): Boolean = {
    def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)
    nums.reduce(gcd) == 1
  }
}
'''

S["1252_cells_with_odd_values_in_a_matrix"] = r'''
// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

object Solution {
  def oddCells(m: Int, n: Int, indices: Array[Array[Int]]): Int = {
    val rows = Array.fill(m)(0)
    val cols = Array.fill(n)(0)
    for (idx <- indices) {
      rows(idx(0)) ^= 1
      cols(idx(1)) ^= 1
    }
    (for (r <- 0 until m; c <- 0 until n if (rows(r) ^ cols(c)) == 1) yield 1).sum
  }
}
'''

S["1253_reconstruct_a_2_row_binary_matrix"] = r'''
// LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

object Solution {
  def reconstructMatrix(upper: Int, lower: Int, colsum: Array[Int]): List[List[Int]] = {
    var u = upper
    var l = lower
    val top = Array.fill(colsum.length)(0)
    val bottom = Array.fill(colsum.length)(0)
    for (i <- colsum.indices if colsum(i) == 2) {
      top(i) = 1
      bottom(i) = 1
      u -= 1
      l -= 1
    }
    if (u < 0 || l < 0) return List.empty
    for (i <- colsum.indices if colsum(i) == 1) {
      if (u > 0) { top(i) = 1; u -= 1 }
      else if (l > 0) { bottom(i) = 1; l -= 1 }
      else return List.empty
    }
    if (u == 0 && l == 0) List(top.toList, bottom.toList) else List.empty
  }
}
'''

S["1254_number_of_closed_islands"] = r'''
// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

object Solution {
  def closedIsland(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    def flood(sr: Int, sc: Int): Boolean = {
      val stack = scala.collection.mutable.Stack((sr, sc))
      grid(sr)(sc) = 1
      var closed = true
      while (stack.nonEmpty) {
        val (r, c) = stack.pop()
        if (r == 0 || r == m - 1 || c == 0 || c == n - 1) closed = false
        for ((dr, dc) <- Seq((1, 0), (-1, 0), (0, 1), (0, -1))) {
          val nr = r + dr
          val nc = c + dc
          if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) == 0) {
            grid(nr)(nc) = 1
            stack.push((nr, nc))
          }
        }
      }
      closed
    }
    var ans = 0
    for (r <- 0 until m; c <- 0 until n if grid(r)(c) == 0) if (flood(r, c)) ans += 1
    ans
  }
}
'''

S["1255_maximum_score_words_formed_by_letters"] = r'''
// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

object Solution {
  def maxScoreWords(words: Array[String], letters: Array[Char], score: Array[Int]): Int = {
    val available = Array.fill(26)(0)
    for (ch <- letters) available(ch - 'a') += 1
    val counts = words.map { w =>
      val c = Array.fill(26)(0)
      for (ch <- w) c(ch - 'a') += 1
      c
    }
    val values = words.map(w => w.map(ch => score(ch - 'a')).sum)
    def canUse(i: Int): Boolean = (0 until 26).forall(j => counts(i)(j) <= available(j))
    def dfs(i: Int): Int = {
      if (i == words.length) return 0
      var best = dfs(i + 1)
      if (canUse(i)) {
        for (j <- 0 until 26) available(j) -= counts(i)(j)
        best = math.max(best, values(i) + dfs(i + 1))
        for (j <- 0 until 26) available(j) += counts(i)(j)
      }
      best
    }
    dfs(0)
  }
}
'''

S["1256_encode_number"] = r'''
// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

object Solution {
  def encode(num: Int): String = {
    val s = Integer.toBinaryString(num + 1)
    if (s.length <= 1) "" else s.substring(1)
  }
}
'''

S["1257_smallest_common_region"] = r'''
// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

object Solution {
  def findSmallestRegion(regions: List[List[String]], region1: String, region2: String): String = {
    val parent = scala.collection.mutable.Map.empty[String, String]
    for (group <- regions; child <- group.tail) parent(child) = group.head
    val ancestors = scala.collection.mutable.Set.empty[String]
    var r1: String = region1
    while (r1 != null) {
      ancestors += r1
      r1 = parent.getOrElse(r1, null)
    }
    var r2 = region2
    while (!ancestors.contains(r2)) r2 = parent(r2)
    r2
  }
}
'''

S["1258_synonymous_sentences"] = r'''
// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

object Solution {
  def generateSentences(synonyms: List[List[String]], text: String): List[String] = {
    val parent = scala.collection.mutable.Map.empty[String, String]
    def find(x: String): String = {
      parent.getOrElseUpdate(x, x)
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }
    for (pair <- synonyms) {
      val ra = find(pair(0))
      val rb = find(pair(1))
      parent(ra) = rb
    }
    val groups = scala.collection.mutable.Map.empty[String, scala.collection.mutable.ListBuffer[String]]
    for (word <- parent.keys) {
      groups.getOrElseUpdate(find(word), scala.collection.mutable.ListBuffer.empty) += word
    }
    val words = text.split(" ")
    val choices = words.map { w =>
      if (parent.contains(w)) groups(find(w)).sorted.toList else List(w)
    }
    def product(idx: Int, cur: List[String], acc: scala.collection.mutable.ListBuffer[String]): Unit = {
      if (idx == choices.length) acc += cur.reverse.mkString(" ")
      else for (w <- choices(idx)) product(idx + 1, w :: cur, acc)
    }
    val acc = scala.collection.mutable.ListBuffer.empty[String]
    product(0, Nil, acc)
    acc.toList.sorted
  }
}
'''

S["1259_handshakes_that_dont_cross"] = r'''
// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

object Solution {
  def numberOfWays(numPeople: Int): Int = {
    val mod = 1000000007
    val dp = Array.ofDim[Long](numPeople + 1)
    dp(0) = 1
    for (people <- 2 to numPeople by 2) {
      var sum = 0L
      for (left <- 0 until people by 2) {
        sum = (sum + dp(left) * dp(people - 2 - left)) % mod
      }
      dp(people) = sum
    }
    dp(numPeople).toInt
  }
}
'''

S["1260_shift_2d_grid"] = r'''
// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

object Solution {
  def shiftGrid(grid: Array[Array[Int]], k: Int): List[List[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val flat = grid.flatten
    val kk = k % flat.length
    val shifted = if (kk == 0) flat else flat.takeRight(kk) ++ flat.dropRight(kk)
    (0 until m).map(i => shifted.slice(i * n, (i + 1) * n).toList).toList
  }
}
'''

S["1261_find_elements_in_a_contaminated_binary_tree"] = r'''
// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

class FindElements(_root: TreeNode) {
  private val values = scala.collection.mutable.Set.empty[Int]
  private def recover(node: TreeNode, value: Int): Unit = {
    if (node == null) return
    node.value = value
    values += value
    recover(node.left, 2 * value + 1)
    recover(node.right, 2 * value + 2)
  }
  recover(_root, 0)

  def find(target: Int): Boolean = values.contains(target)
}
'''

S["1262_greatest_sum_divisible_by_three"] = r'''
// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

object Solution {
  def maxSumDivThree(nums: Array[Int]): Int = {
    val impossible = Long.MinValue / 4
    var dp = Array(0L, impossible, impossible)
    for (value <- nums) {
      val old = dp.clone()
      for (total <- old if total != impossible) {
        val rem = ((total + value) % 3).toInt
        dp(rem) = math.max(dp(rem), total + value)
      }
    }
    dp(0).toInt
  }
}
'''

S["1263_minimum_moves_to_move_a_box_to_their_target_location"] = r'''
// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

object Solution {
  def minPushBox(grid: Array[Array[Char]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var box = (0, 0)
    var player = (0, 0)
    var target = (0, 0)
    for (r <- 0 until m; c <- 0 until n) {
      if (grid(r)(c) == 'B') box = (r, c)
      else if (grid(r)(c) == 'S') player = (r, c)
      else if (grid(r)(c) == 'T') target = (r, c)
    }
    def reachable(start: (Int, Int), blocked: (Int, Int)): Set[(Int, Int)] = {
      val seen = scala.collection.mutable.Set(start)
      val stack = scala.collection.mutable.Stack(start)
      while (stack.nonEmpty) {
        val (r, c) = stack.pop()
        for ((dr, dc) <- Seq((1, 0), (-1, 0), (0, 1), (0, -1))) {
          val nxt = (r + dr, c + dc)
          if (nxt._1 >= 0 && nxt._1 < m && nxt._2 >= 0 && nxt._2 < n &&
              grid(nxt._1)(nxt._2) != '#' && nxt != blocked && !seen.contains(nxt)) {
            seen += nxt
            stack.push(nxt)
          }
        }
      }
      seen.toSet
    }
    val q = scala.collection.mutable.Queue((box, player, 0))
    val seen = scala.collection.mutable.Set((box, player))
    while (q.nonEmpty) {
      val (b, p, pushes) = q.dequeue()
      if (b == target) return pushes
      val canReach = reachable(p, b)
      for ((dr, dc) <- Seq((1, 0), (-1, 0), (0, 1), (0, -1))) {
        val stand = (b._1 - dr, b._2 - dc)
        val nb = (b._1 + dr, b._2 + dc)
        if (canReach.contains(stand) && nb._1 >= 0 && nb._1 < m && nb._2 >= 0 && nb._2 < n &&
            grid(nb._1)(nb._2) != '#') {
          val state = (nb, b)
          if (!seen.contains(state)) {
            seen += state
            q.enqueue((nb, b, pushes + 1))
          }
        }
      }
    }
    -1
  }
}
'''

S["1265_print_immutable_linked_list_in_reverse"] = r'''
// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

trait ImmutableListNode {
  def printValue(): Unit
  def getNext(): ImmutableListNode
}

object Solution {
  def printLinkedListInReverse(head: ImmutableListNode): Unit = {
    if (head == null) return
    printLinkedListInReverse(head.getNext())
    head.printValue()
  }
}
'''

S["1266_minimum_time_visiting_all_points"] = r'''
// LeetCode 1266 - Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/

object Solution {
  def minTimeToVisitAllPoints(points: Array[Array[Int]]): Int =
    points.zip(points.tail).map { case (a, b) => math.max(math.abs(a(0) - b(0)), math.abs(a(1) - b(1))) }.sum
}
'''

S["1267_count_servers_that_communicate"] = r'''
// LeetCode 1267 - Count Servers that Communicate
// https://leetcode.com/problems/count-servers-that-communicate/

object Solution {
  def countServers(grid: Array[Array[Int]]): Int = {
    val rows = grid.map(_.sum)
    val cols = grid(0).indices.map(c => grid.map(_(c)).sum)
    var ans = 0
    for (r <- grid.indices; c <- grid(0).indices if grid(r)(c) == 1 && (rows(r) > 1 || cols(c) > 1)) ans += 1
    ans
  }
}
'''

S["1268_search_suggestions_system"] = r'''
// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

object Solution {
  def suggestedProducts(products: Array[String], searchWord: String): List[List[String]] = {
    val sorted = products.sorted
    val answer = scala.collection.mutable.ListBuffer.empty[List[String]]
    var prefix = ""
    for (ch <- searchWord) {
      prefix += ch
      var lo = 0
      var hi = sorted.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (sorted(mid) < prefix) lo = mid + 1 else hi = mid
      }
      answer += sorted.slice(lo, lo + 3).filter(_.startsWith(prefix)).toList
    }
    answer.toList
  }
}
'''

S["1269_number_of_ways_to_stay_in_the_same_place_after_some_steps"] = r'''
// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

object Solution {
  def numWays(steps: Int, arrLen: Int): Int = {
    val mod = 1000000007
    val width = math.min(arrLen, steps / 2 + 1)
    var dp = Array.fill(width)(0)
    dp(0) = 1
    for (_ <- 0 until steps) {
      dp = Array.tabulate(width) { i =>
        var v = dp(i).toLong
        if (i > 0) v += dp(i - 1)
        if (i + 1 < width) v += dp(i + 1)
        (v % mod).toInt
      }
    }
    dp(0)
  }
}
'''

S["1271_hexspeak"] = r'''
// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

object Solution {
  def toHexspeak(num: String): String = {
    var value = num.toLong
    val digits = "0123456789ABCDEF"
    val out = new StringBuilder
    if (value == 0) return "O"
    while (value > 0) {
      val rem = (value % 16).toInt
      value /= 16
      if (rem >= 2 && rem <= 9) return "ERROR"
      out.insert(0, digits(rem))
    }
    out.toString.replace("0", "O").replace("1", "I")
  }
}
'''

S["1272_remove_interval"] = r'''
// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

object Solution {
  def removeInterval(intervals: Array[Array[Int]], toBeRemoved: Array[Int]): List[List[Int]] = {
    val left = toBeRemoved(0)
    val right = toBeRemoved(1)
    val answer = scala.collection.mutable.ListBuffer.empty[List[Int]]
    for (iv <- intervals) {
      val start = iv(0)
      val end = iv(1)
      if (end <= left || start >= right) answer += List(start, end)
      else {
        if (start < left) answer += List(start, left)
        if (end > right) answer += List(right, end)
      }
    }
    answer.toList
  }
}
'''

S["1273_delete_tree_nodes"] = r'''
// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

object Solution {
  def deleteTreeNodes(nodes: Int, parent: Array[Int], value: Array[Int]): Int = {
    val children = Array.fill(nodes)(scala.collection.mutable.ListBuffer.empty[Int])
    for (node <- 1 until nodes) children(parent(node)) += node
    def dfs(node: Int): (Int, Int) = {
      var total = value(node)
      var count = 1
      for (child <- children(node)) {
        val (childSum, childCount) = dfs(child)
        total += childSum
        count += childCount
      }
      if (total == 0) (0, 0) else (total, count)
    }
    dfs(0)._2
  }
}
'''

S["1274_number_of_ships_in_a_rectangle"] = r'''
// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

class Point(var x: Int, var y: Int)

trait Sea {
  def hasShips(topRight: Point, bottomLeft: Point): Boolean
}

object Solution {
  def countShips(sea: Sea, topRight: Point, bottomLeft: Point): Int = {
    val tx = topRight.x
    val ty = topRight.y
    val bx = bottomLeft.x
    val by = bottomLeft.y
    if (tx < bx || ty < by || !sea.hasShips(topRight, bottomLeft)) return 0
    if (tx == bx && ty == by) return 1
    val mx = (tx + bx) / 2
    val my = (ty + by) / 2
    countShips(sea, new Point(mx, my), new Point(bx, by)) +
      countShips(sea, new Point(tx, my), new Point(mx + 1, by)) +
      countShips(sea, new Point(mx, ty), new Point(bx, my + 1)) +
      countShips(sea, new Point(tx, ty), new Point(mx + 1, my + 1))
  }
}
'''

S["1275_find_winner_on_a_tic_tac_toe_game"] = r'''
// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

object Solution {
  def tictactoe(moves: Array[Array[Int]]): String = {
    val board = Array.fill(3, 3)(0)
    for (i <- moves.indices) {
      board(moves(i)(0))(moves(i)(1)) = if (i % 2 == 0) 1 else -1
    }
    val lines = board.map(_.toSeq).toSeq ++ board(0).indices.map(c => board.map(_(c)).toSeq) ++
      Seq((0 until 3).map(i => board(i)(i)), (0 until 3).map(i => board(i)(2 - i)))
    for (line <- lines) {
      val s = line.sum
      if (math.abs(s) == 3) return if (s == 3) "A" else "B"
    }
    if (moves.length == 9) "Draw" else "Pending"
  }
}
'''

S["1276_number_of_burgers_with_no_waste_of_ingredients"] = r'''
// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

object Solution {
  def numOfBurgers(tomatoSlices: Int, cheeseSlices: Int): List[Int] = {
    val jumbo = tomatoSlices / 2 - cheeseSlices
    val small = cheeseSlices - jumbo
    if (tomatoSlices % 2 == 0 && jumbo >= 0 && small >= 0) List(jumbo, small) else List.empty
  }
}
'''

S["1277_count_square_submatrices_with_all_ones"] = r'''
// LeetCode 1277 - Count Square Submatrices with All Ones
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

object Solution {
  def countSquares(matrix: Array[Array[Int]]): Int = {
    var answer = 0
    for (r <- matrix.indices; c <- matrix(0).indices) {
      if (matrix(r)(c) > 0 && r > 0 && c > 0) {
        matrix(r)(c) += math.min(matrix(r - 1)(c), math.min(matrix(r)(c - 1), matrix(r - 1)(c - 1)))
      }
      answer += matrix(r)(c)
    }
    answer
  }
}
'''

S["1278_palindrome_partitioning_iii"] = r'''
// LeetCode 1278 - Palindrome Partitioning III
// https://leetcode.com/problems/palindrome-partitioning-iii/

object Solution {
  def palindromePartition(s: String, k: Int): Int = {
    val n = s.length
    val cost = Array.ofDim[Int](n, n)
    for (length <- 2 to n; i <- 0 to n - length) {
      val j = i + length - 1
      cost(i)(j) = (if (length > 2) cost(i + 1)(j - 1) else 0) + (if (s(i) != s(j)) 1 else 0)
    }
    val inf = n + 1
    val dp = Array.fill(k + 1, n + 1)(inf)
    dp(0)(0) = 0
    for (parts <- 1 to k; end <- parts to n) {
      dp(parts)(end) = (parts - 1 until end).map(start => dp(parts - 1)(start) + cost(start)(end - 1)).min
    }
    dp(k)(n)
  }
}
'''

S["1279_traffic_light_controlled_intersection"] = r'''
// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

class TrafficLight() {
  private var greenRoad = 1
  private val lock = new Object

  def carArrived(carId: Int, roadId: Int, direction: Int, turnGreen: Runnable, crossCar: Runnable): Unit = {
    lock.synchronized {
      if (roadId != greenRoad) {
        turnGreen.run()
        greenRoad = roadId
      }
      crossCar.run()
    }
  }
}
'''

S["1281_subtract_the_product_and_sum_of_digits_of_an_integer"] = r'''
// LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

object Solution {
  def subtractProductAndSum(n: Int): Int = {
    var product = 1
    var total = 0
    var x = n
    while (x > 0) {
      val digit = x % 10
      x /= 10
      product *= digit
      total += digit
    }
    product - total
  }
}
'''

S["1282_group_the_people_given_the_group_size_they_belong_to"] = r'''
// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

object Solution {
  def groupThePeople(groupSizes: Array[Int]): List[List[Int]] = {
    val pending = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ListBuffer[Int]]
    val answer = scala.collection.mutable.ListBuffer.empty[List[Int]]
    for (person <- groupSizes.indices) {
      val size = groupSizes(person)
      val buf = pending.getOrElseUpdate(size, scala.collection.mutable.ListBuffer.empty)
      buf += person
      if (buf.length == size) {
        answer += buf.toList
        pending(size) = scala.collection.mutable.ListBuffer.empty
      }
    }
    answer.toList
  }
}
'''

S["1283_find_the_smallest_divisor_given_a_threshold"] = r'''
// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

object Solution {
  def smallestDivisor(nums: Array[Int], threshold: Int): Int = {
    var lo = 1
    var hi = nums.max
    while (lo < hi) {
      val mid = (lo + hi) / 2
      val total = nums.map(x => (x + mid - 1) / mid).sum
      if (total <= threshold) hi = mid else lo = mid + 1
    }
    lo
  }
}
'''

S["1284_minimum_number_of_flips_to_convert_binary_matrix_to_zero_matrix"] = r'''
// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

object Solution {
  def minFlips(mat: Array[Array[Int]]): Int = {
    val m = mat.length
    val n = mat(0).length
    var start = 0
    for (r <- 0 until m; c <- 0 until n if mat(r)(c) == 1) start |= 1 << (r * n + c)
    val masks = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (r <- 0 until m; c <- 0 until n) {
      var mask = 0
      for ((dr, dc) <- Seq((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1))) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < m && nc >= 0 && nc < n) mask ^= 1 << (nr * n + nc)
      }
      masks += mask
    }
    val q = scala.collection.mutable.Queue((start, 0))
    val seen = scala.collection.mutable.Set(start)
    while (q.nonEmpty) {
      val (state, distance) = q.dequeue()
      if (state == 0) return distance
      for (mask <- masks) {
        val nxt = state ^ mask
        if (!seen.contains(nxt)) {
          seen += nxt
          q.enqueue((nxt, distance + 1))
        }
      }
    }
    -1
  }
}
'''

S["1286_iterator_for_combination"] = r'''
// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

class CombinationIterator(characters: String, combinationLength: Int) {
  private val items = characters.combinations(combinationLength).toIterator
  private var nextItem: Option[String] = if (items.hasNext) Some(items.next()) else None

  def next(): String = {
    val current = nextItem.get
    nextItem = if (items.hasNext) Some(items.next()) else None
    current
  }

  def hasNext(): Boolean = nextItem.isDefined
}
'''

S["1287_element_appearing_more_than_25_in_sorted_array"] = r'''
// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

object Solution {
  def findSpecialInteger(arr: Array[Int]): Int = {
    val n = arr.length
    for (value <- Seq(arr(n / 4), arr(n / 2), arr(3 * n / 4))) {
      if (arr.count(_ == value) > n / 4) return value
    }
    arr(0)
  }
}
'''

S["1288_remove_covered_intervals"] = r'''
// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

object Solution {
  def removeCoveredIntervals(intervals: Array[Array[Int]]): Int = {
    val sorted = intervals.sortBy(iv => (iv(0), -iv(1)))
    var answer = 0
    var farthest = -1
    for (iv <- sorted) {
      if (iv(1) > farthest) {
        answer += 1
        farthest = iv(1)
      }
    }
    answer
  }
}
'''

S["1289_minimum_falling_path_sum_ii"] = r'''
// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

object Solution {
  def minFallingPathSum(grid: Array[Array[Int]]): Int = {
    var dp = grid(0).clone()
    for (row <- grid.tail) {
      val first = dp.indices.minBy(dp)
      val secondValue = if (dp.length > 1) dp.indices.filter(_ != first).map(dp).min else 0
      dp = row.zipWithIndex.map { case (value, i) =>
        value + (if (i == first) secondValue else dp(first))
      }.toArray
    }
    dp.min
  }
}
'''

S["1290_convert_binary_number_in_a_linked_list_to_integer"] = r'''
// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def getDecimalValue(head: ListNode): Int = {
    var value = 0
    var cur = head
    while (cur != null) {
      value = value * 2 + cur.x
      cur = cur.next
    }
    value
  }
}
'''

S["1291_sequential_digits"] = r'''
// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

object Solution {
  def sequentialDigits(low: Int, high: Int): List[Int] = {
    val digits = "123456789"
    val answer = scala.collection.mutable.ListBuffer.empty[Int]
    for (length <- 2 to 9; start <- 0 to 9 - length) {
      val value = digits.substring(start, start + length).toInt
      if (value >= low && value <= high) answer += value
    }
    answer.toList
  }
}
'''

S["1292_maximum_side_length_of_a_square_with_sum_less_than_or_equal_to_threshold"] = r'''
// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

object Solution {
  def maxSideLength(mat: Array[Array[Int]], threshold: Int): Int = {
    val m = mat.length
    val n = mat(0).length
    val prefix = Array.ofDim[Int](m + 1, n + 1)
    for (r <- 0 until m; c <- 0 until n) {
      prefix(r + 1)(c + 1) = mat(r)(c) + prefix(r)(c + 1) + prefix(r + 1)(c) - prefix(r)(c)
    }
    def possible(size: Int): Boolean = {
      for (r <- size to m; c <- size to n) {
        val sum = prefix(r)(c) - prefix(r - size)(c) - prefix(r)(c - size) + prefix(r - size)(c - size)
        if (sum <= threshold) return true
      }
      false
    }
    var lo = 0
    var hi = math.min(m, n)
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (possible(mid)) lo = mid else hi = mid - 1
    }
    lo
  }
}
'''

S["1293_shortest_path_in_a_grid_with_obstacles_elimination"] = r'''
// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

object Solution {
  def shortestPath(grid: Array[Array[Int]], k: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    if (k >= m + n - 2) return m + n - 2
    val q = scala.collection.mutable.Queue((0, 0, k, 0))
    val best = scala.collection.mutable.Map((0, 0) -> k)
    while (q.nonEmpty) {
      val (r, c, remaining, distance) = q.dequeue()
      if (r == m - 1 && c == n - 1) return distance
      for ((dr, dc) <- Seq((1, 0), (-1, 0), (0, 1), (0, -1))) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
          val nxt = remaining - grid(nr)(nc)
          if (nxt >= 0 && nxt > best.getOrElse((nr, nc), -1)) {
            best((nr, nc)) = nxt
            q.enqueue((nr, nc, nxt, distance + 1))
          }
        }
      }
    }
    -1
  }
}
'''

S["1295_find_numbers_with_even_number_of_digits"] = r'''
// LeetCode 1295 - Find Numbers with Even Number of Digits
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

object Solution {
  def findNumbers(nums: Array[Int]): Int =
    nums.count(value => value.toString.length % 2 == 0)
}
'''

S["1296_divide_array_in_sets_of_k_consecutive_numbers"] = r'''
// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

object Solution {
  def isPossibleDivide(nums: Array[Int], k: Int): Boolean = {
    if (nums.length % k != 0) return false
    val counts = scala.collection.mutable.TreeMap.empty[Int, Int].withDefaultValue(0)
    for (x <- nums) counts(x) += 1
    while (counts.nonEmpty) {
      val start = counts.firstKey
      val amount = counts(start)
      for (value <- start until start + k) {
        if (counts(value) < amount) return false
        counts(value) -= amount
        if (counts(value) == 0) counts.remove(value)
      }
    }
    true
  }
}
'''

S["1297_maximum_number_of_occurrences_of_a_substring"] = r'''
// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

object Solution {
  def maxFreq(s: String, maxLetters: Int, minSize: Int, maxSize: Int): Int = {
    val counts = scala.collection.mutable.Map.empty[String, Int].withDefaultValue(0)
    for (i <- 0 to s.length - minSize) {
      val sub = s.substring(i, i + minSize)
      if (sub.toSet.size <= maxLetters) counts(sub) += 1
    }
    if (counts.isEmpty) 0 else counts.values.max
  }
}
'''

S["1298_maximum_candies_you_can_get_from_boxes"] = r'''
// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

object Solution {
  def maxCandies(
    status: Array[Int],
    candies: Array[Int],
    keys: Array[Array[Int]],
    containedBoxes: Array[Array[Int]],
    initialBoxes: Array[Int]
  ): Int = {
    val owned = scala.collection.mutable.Set(initialBoxes: _*)
    val opened = scala.collection.mutable.Set.empty[Int]
    val q = scala.collection.mutable.Queue[Int]()
    for (box <- initialBoxes if status(box) == 1) q.enqueue(box)
    var total = 0
    while (q.nonEmpty) {
      val box = q.dequeue()
      if (!opened.contains(box) && status(box) == 1) {
        opened += box
        total += candies(box)
        for (key <- keys(box)) {
          status(key) = 1
          if (owned.contains(key) && !opened.contains(key)) q.enqueue(key)
        }
        for (child <- containedBoxes(box)) {
          owned += child
          if (status(child) == 1 && !opened.contains(child)) q.enqueue(child)
        }
      }
    }
    total
  }
}
'''

S["1299_replace_elements_with_greatest_element_on_right_side"] = r'''
// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

object Solution {
  def replaceElements(arr: Array[Int]): Array[Int] = {
    var greatest = -1
    for (i <- arr.length - 1 to 0 by -1) {
      val cur = arr(i)
      arr(i) = greatest
      greatest = math.max(greatest, cur)
    }
    arr
  }
}
'''


def main() -> None:
    for folder, code in S.items():
        write(folder, code)
    print(f"done {len(S)}")


if __name__ == "__main__":
    main()
