#!/usr/bin/env python3
"""Write Solution.scala for batch_03 folders 0930-0979."""
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


write("0930_binary_subarrays_with_sum", r'''// LeetCode 0930 - Binary Subarrays With Sum
// https://leetcode.com/problems/binary-subarrays-with-sum/

object Solution {
  def numSubarraysWithSum(nums: Array[Int], goal: Int): Int = {
    val count = scala.collection.mutable.Map(0 -> 1)
    var prefix = 0
    var ans = 0
    nums.foreach { x =>
      prefix += x
      ans += count.getOrElse(prefix - goal, 0)
      count(prefix) = count.getOrElse(prefix, 0) + 1
    }
    ans
  }
}
''')

write("0931_minimum_falling_path_sum", r'''// LeetCode 0931 - Minimum Falling Path Sum
// https://leetcode.com/problems/minimum-falling-path-sum/

object Solution {
  def minFallingPathSum(matrix: Array[Array[Int]]): Int = {
    var dp = matrix(0).clone()
    var r = 1
    while (r < matrix.length) {
      val ndp = Array.ofDim[Int](dp.length)
      var c = 0
      while (c < dp.length) {
        var best = dp(c)
        if (c > 0) best = math.min(best, dp(c - 1))
        if (c + 1 < dp.length) best = math.min(best, dp(c + 1))
        ndp(c) = matrix(r)(c) + best
        c += 1
      }
      dp = ndp
      r += 1
    }
    dp.min
  }
}
''')

write("0932_beautiful_array", r'''// LeetCode 0932 - Beautiful Array
// https://leetcode.com/problems/beautiful-array/

object Solution {
  def beautifulArray(n: Int): Array[Int] = {
    if (n == 1) return Array(1)
    val left = beautifulArray((n + 1) / 2)
    val right = beautifulArray(n / 2)
    val ans = Array.ofDim[Int](n)
    var k = 0
    left.foreach { x => ans(k) = 2 * x - 1; k += 1 }
    right.foreach { x => ans(k) = 2 * x; k += 1 }
    ans
  }
}
''')

write("0933_number_of_recent_calls", r'''// LeetCode 0933 - Number of Recent Calls
// https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter() {
  private val q = scala.collection.mutable.Queue[Int]()

  def ping(t: Int): Int = {
    q.enqueue(t)
    while (q.front < t - 3000) q.dequeue()
    q.size
  }
}
''')

write("0934_shortest_bridge", r'''// LeetCode 0934 - Shortest Bridge
// https://leetcode.com/problems/shortest-bridge/

object Solution {
  def shortestBridge(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val dirs = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))
    def dfs(r: Int, c: Int): Unit = {
      if (r < 0 || r >= n || c < 0 || c >= n || grid(r)(c) != 1) return
      grid(r)(c) = 2
      dirs.foreach { d => dfs(r + d(0), c + d(1)) }
    }
    var found = false
    var i = 0
    while (i < n && !found) {
      var j = 0
      while (j < n && !found) {
        if (grid(i)(j) == 1) { dfs(i, j); found = true }
        j += 1
      }
      i += 1
    }
    val q = scala.collection.mutable.Queue[Array[Int]]()
    i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 2) q.enqueue(Array(i, j, 0))
        j += 1
      }
      i += 1
    }
    while (q.nonEmpty) {
      val cur = q.dequeue()
      val r = cur(0)
      val c = cur(1)
      val dist = cur(2)
      dirs.foreach { d =>
        val nr = r + d(0)
        val nc = c + d(1)
        if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
          if (grid(nr)(nc) == 1) return dist
          if (grid(nr)(nc) == 0) {
            grid(nr)(nc) = 2
            q.enqueue(Array(nr, nc, dist + 1))
          }
        }
      }
    }
    -1
  }
}
''')

write("0935_knight_dialer", r'''// LeetCode 0935 - Knight Dialer
// https://leetcode.com/problems/knight-dialer/

object Solution {
  def knightDialer(n: Int): Int = {
    val MOD = 1000000007
    val moves = Array(
      Array(4, 6), Array(6, 8), Array(7, 9), Array(4, 8), Array(0, 3, 9),
      Array.empty[Int], Array(0, 1, 7), Array(2, 6), Array(1, 3), Array(2, 4)
    )
    var dp = Array.fill(10)(1L)
    var step = 0
    while (step < n - 1) {
      val ndp = Array.ofDim[Long](10)
      var i = 0
      while (i < 10) {
        moves(i).foreach { j => ndp(j) = (ndp(j) + dp(i)) % MOD }
        i += 1
      }
      dp = ndp
      step += 1
    }
    (dp.sum % MOD).toInt
  }
}
''')

write("0936_stamping_the_sequence", r'''// LeetCode 0936 - Stamping The Sequence
// https://leetcode.com/problems/stamping-the-sequence/

object Solution {
  def movesToStamp(stamp: String, target: String): Array[Int] = {
    val n = target.length
    val m = stamp.length
    val done = Array.ofDim[Boolean](n)
    val ans = scala.collection.mutable.ArrayBuffer[Int]()
    var changed = true
    while (changed) {
      changed = false
      var i = n - m
      var placed = false
      while (i >= 0 && !placed) {
        var ok = true
        var any = false
        var j = 0
        while (j < m && ok) {
          if (!done(i + j) && target.charAt(i + j) != stamp.charAt(j)) ok = false
          if (!done(i + j)) any = true
          j += 1
        }
        if (ok && any) {
          j = 0
          while (j < m) { done(i + j) = true; j += 1 }
          ans += i
          changed = true
          placed = true
        }
        i -= 1
      }
    }
    if (done.exists(!_)) return Array.empty[Int]
    ans.reverse.toArray
  }
}
''')

write("0937_reorder_data_in_log_files", r'''// LeetCode 0937 - Reorder Data in Log Files
// https://leetcode.com/problems/reorder-data-in-log-files/

object Solution {
  def reorderLogFiles(logs: Array[String]): Array[String] = {
    val letter = scala.collection.mutable.ArrayBuffer[String]()
    val digit = scala.collection.mutable.ArrayBuffer[String]()
    logs.foreach { log =>
      val sp = log.indexOf(' ')
      if (log.charAt(sp + 1).isLetter) letter += log
      else digit += log
    }
    val sorted = letter.sortBy { a =>
      val spa = a.indexOf(' ')
      (a.substring(spa + 1), a.substring(0, spa))
    }
    (sorted ++ digit).toArray
  }
}
''')

write("0938_range_sum_of_bst", f'''// LeetCode 0938 - Range Sum of BST
// https://leetcode.com/problems/range-sum-of-bst/

{TREE}
object Solution {{
  def rangeSumBST(root: TreeNode, low: Int, high: Int): Int = {{
    if (root == null) return 0
    if (root.value < low) return rangeSumBST(root.right, low, high)
    if (root.value > high) return rangeSumBST(root.left, low, high)
    root.value + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high)
  }}
}}
''')

write("0939_minimum_area_rectangle", r'''// LeetCode 0939 - Minimum Area Rectangle
// https://leetcode.com/problems/minimum-area-rectangle/

object Solution {
  def minAreaRect(points: Array[Array[Int]]): Int = {
    val byX = scala.collection.mutable.TreeMap.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    points.foreach { p =>
      byX.getOrElseUpdate(p(0), scala.collection.mutable.ArrayBuffer.empty[Int]) += p(1)
    }
    val last = scala.collection.mutable.Map.empty[String, Int]
    var ans = Long.MaxValue
    byX.foreach { case (x, ysBuf) =>
      val ys = ysBuf.sorted
      var i = 0
      while (i < ys.length) {
        var j = i + 1
        while (j < ys.length) {
          val key = ys(i) + "#" + ys(j)
          if (last.contains(key)) {
            ans = math.min(ans, math.abs(x.toLong - last(key)) * (ys(j) - ys(i)))
          }
          last(key) = x
          j += 1
        }
        i += 1
      }
    }
    if (ans == Long.MaxValue) 0 else ans.toInt
  }
}
''')

write("0940_distinct_subsequences_ii", r'''// LeetCode 0940 - Distinct Subsequences II
// https://leetcode.com/problems/distinct-subsequences-ii/

object Solution {
  def distinctSubseqII(s: String): Int = {
    val MOD = 1000000007
    val ends = Array.ofDim[Long](26)
    var total = 1L
    s.foreach { ch =>
      val prev = ends(ch - 'a')
      ends(ch - 'a') = total
      total = (total - prev + ends(ch - 'a') + MOD) % MOD
    }
    ((total - 1 + MOD) % MOD).toInt
  }
}
''')

write("0941_valid_mountain_array", r'''// LeetCode 0941 - Valid Mountain Array
// https://leetcode.com/problems/valid-mountain-array/

object Solution {
  def validMountainArray(arr: Array[Int]): Boolean = {
    val n = arr.length
    if (n < 3) return false
    var i = 0
    while (i + 1 < n && arr(i) < arr(i + 1)) i += 1
    if (i == 0 || i == n - 1) return false
    while (i + 1 < n && arr(i) > arr(i + 1)) i += 1
    i == n - 1
  }
}
''')

write("0942_di_string_match", r'''// LeetCode 0942 - DI String Match
// https://leetcode.com/problems/di-string-match/

object Solution {
  def diStringMatch(s: String): Array[Int] = {
    var lo = 0
    var hi = s.length
    val ans = Array.ofDim[Int](s.length + 1)
    var k = 0
    s.foreach { ch =>
      if (ch == 'I') { ans(k) = lo; lo += 1 }
      else { ans(k) = hi; hi -= 1 }
      k += 1
    }
    ans(k) = lo
    ans
  }
}
''')

write("0943_find_the_shortest_superstring", r'''// LeetCode 0943 - Find the Shortest Superstring
// https://leetcode.com/problems/find-the-shortest-superstring/

object Solution {
  def shortestSuperstring(words: Array[String]): String = {
    val n = words.length
    val overlap = Array.ofDim[Int](n, n)
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (i != j) {
          val a = words(i)
          val b = words(j)
          var k = math.min(a.length, b.length)
          var found = false
          while (k > 0 && !found) {
            if (a.substring(a.length - k) == b.substring(0, k)) {
              overlap(i)(j) = k
              found = true
            }
            k -= 1
          }
        }
        j += 1
      }
      i += 1
    }
    val N = 1 << n
    val dp = Array.ofDim[String](N, n)
    i = 0
    while (i < n) {
      dp(1 << i)(i) = words(i)
      i += 1
    }
    var mask = 0
    while (mask < N) {
      var last = 0
      while (last < n) {
        if ((mask & (1 << last)) != 0 && dp(mask)(last) != null) {
          var nxt = 0
          while (nxt < n) {
            if ((mask & (1 << nxt)) == 0) {
              val cand = dp(mask)(last) + words(nxt).substring(overlap(last)(nxt))
              val nmask = mask | (1 << nxt)
              if (dp(nmask)(nxt) == null || cand.length < dp(nmask)(nxt).length)
                dp(nmask)(nxt) = cand
            }
            nxt += 1
          }
        }
        last += 1
      }
      mask += 1
    }
    val full = N - 1
    var best: String = null
    i = 0
    while (i < n) {
      if (dp(full)(i) != null && (best == null || dp(full)(i).length < best.length))
        best = dp(full)(i)
      i += 1
    }
    best
  }
}
''')

write("0944_delete_columns_to_make_sorted", r'''// LeetCode 0944 - Delete Columns to Make Sorted
// https://leetcode.com/problems/delete-columns-to-make-sorted/

object Solution {
  def minDeletionSize(strs: Array[String]): Int = {
    var ans = 0
    val m = strs(0).length
    val n = strs.length
    var c = 0
    while (c < m) {
      var r = 0
      var bad = false
      while (r + 1 < n && !bad) {
        if (strs(r).charAt(c) > strs(r + 1).charAt(c)) { ans += 1; bad = true }
        r += 1
      }
      c += 1
    }
    ans
  }
}
''')

write("0945_minimum_increment_to_make_array_unique", r'''// LeetCode 0945 - Minimum Increment to Make Array Unique
// https://leetcode.com/problems/minimum-increment-to-make-array-unique/

object Solution {
  def minIncrementForUnique(nums: Array[Int]): Int = {
    val arr = nums.sorted
    var ans = 0
    var i = 1
    while (i < arr.length) {
      if (arr(i) <= arr(i - 1)) {
        val need = arr(i - 1) + 1
        ans += need - arr(i)
        arr(i) = need
      }
      i += 1
    }
    ans
  }
}
''')

write("0946_validate_stack_sequences", r'''// LeetCode 0946 - Validate Stack Sequences
// https://leetcode.com/problems/validate-stack-sequences/

object Solution {
  def validateStackSequences(pushed: Array[Int], popped: Array[Int]): Boolean = {
    val stack = scala.collection.mutable.ArrayBuffer[Int]()
    var j = 0
    pushed.foreach { x =>
      stack += x
      while (stack.nonEmpty && stack.last == popped(j)) {
        stack.remove(stack.length - 1)
        j += 1
      }
    }
    stack.isEmpty
  }
}
''')

write("0947_most_stones_removed_with_same_row_or_column", r'''// LeetCode 0947 - Most Stones Removed with Same Row or Column
// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

object Solution {
  def removeStones(stones: Array[Array[Int]]): Int = {
    val parent = scala.collection.mutable.Map.empty[Int, Int]
    def find(x: Int): Int = {
      if (!parent.contains(x)) parent(x) = x
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }
    def unite(a: Int, b: Int): Unit = { parent(find(a)) = find(b) }
    stones.foreach { s => unite(s(0), ~s(1)) }
    val roots = scala.collection.mutable.Set.empty[Int]
    stones.foreach { s => roots += find(s(0)) }
    stones.length - roots.size
  }
}
''')

write("0948_bag_of_tokens", r'''// LeetCode 0948 - Bag of Tokens
// https://leetcode.com/problems/bag-of-tokens/

object Solution {
  def bagOfTokensScore(tokens: Array[Int], power: Int): Int = {
    val arr = tokens.sorted
    var i = 0
    var j = arr.length - 1
    var score = 0
    var ans = 0
    var p = power
    while (i <= j) {
      if (p >= arr(i)) {
        p -= arr(i)
        i += 1
        score += 1
        ans = math.max(ans, score)
      } else if (score > 0) {
        p += arr(j)
        j -= 1
        score -= 1
      } else return ans
    }
    ans
  }
}
''')

write("0949_largest_time_for_given_digits", r'''// LeetCode 0949 - Largest Time for Given Digits
// https://leetcode.com/problems/largest-time-for-given-digits/

object Solution {
  def largestTimeFromDigits(arr: Array[Int]): String = {
    scala.util.Sorting.quickSort(arr)
    var best = ""
    def nextPermutation(a: Array[Int]): Boolean = {
      var i = a.length - 2
      while (i >= 0 && a(i) >= a(i + 1)) i -= 1
      if (i < 0) return false
      var j = a.length - 1
      while (a(j) <= a(i)) j -= 1
      val tmp = a(i); a(i) = a(j); a(j) = tmp
      var l = i + 1
      var r = a.length - 1
      while (l < r) {
        val t = a(l); a(l) = a(r); a(r) = t
        l += 1; r -= 1
      }
      true
    }
    do {
      val hours = 10 * arr(0) + arr(1)
      val minutes = 10 * arr(2) + arr(3)
      if (hours < 24 && minutes < 60) {
        val cand = f"${hours}%02d:${minutes}%02d"
        if (cand > best) best = cand
      }
    } while (nextPermutation(arr))
    best
  }
}
''')

write("0950_reveal_cards_in_increasing_order", r'''// LeetCode 0950 - Reveal Cards In Increasing Order
// https://leetcode.com/problems/reveal-cards-in-increasing-order/

object Solution {
  def deckRevealedIncreasing(deck: Array[Int]): Array[Int] = {
    val sorted = deck.sorted
    val n = sorted.length
    val idx = scala.collection.mutable.ArrayDeque[Int]()
    var i = 0
    while (i < n) { idx.append(i); i += 1 }
    val ans = Array.ofDim[Int](n)
    sorted.foreach { card =>
      ans(idx.removeHead()) = card
      if (idx.nonEmpty) idx.append(idx.removeHead())
    }
    ans
  }
}
''')

write("0951_flip_equivalent_binary_trees", f'''// LeetCode 0951 - Flip Equivalent Binary Trees
// https://leetcode.com/problems/flip-equivalent-binary-trees/

{TREE}
object Solution {{
  def flipEquiv(root1: TreeNode, root2: TreeNode): Boolean = {{
    if (root1 == null && root2 == null) return true
    if (root1 == null || root2 == null || root1.value != root2.value) return false
    (flipEquiv(root1.left, root2.left) && flipEquiv(root1.right, root2.right)) ||
      (flipEquiv(root1.left, root2.right) && flipEquiv(root1.right, root2.left))
  }}
}}
''')

write("0952_largest_component_size_by_common_factor", r'''// LeetCode 0952 - Largest Component Size by Common Factor
// https://leetcode.com/problems/largest-component-size-by-common-factor/

object Solution {
  def largestComponentSize(nums: Array[Int]): Int = {
    val mx = nums.max
    val parent = Array.tabulate(mx + 1)(identity)
    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }
    def unite(a: Int, b: Int): Unit = { parent(find(a)) = find(b) }
    def factors(x0: Int): List[Int] = {
      val res = scala.collection.mutable.ListBuffer[Int]()
      var x = x0
      var d = 2
      while (d.toLong * d <= x) {
        if (x % d == 0) {
          res += d
          while (x % d == 0) x /= d
        }
        d += 1
      }
      if (x > 1) res += x
      res.toList
    }
    nums.foreach { num => factors(num).foreach(f => unite(num, f)) }
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0
    nums.foreach { num =>
      val r = find(num)
      val c = cnt.getOrElse(r, 0) + 1
      cnt(r) = c
      ans = math.max(ans, c)
    }
    ans
  }
}
''')

write("0953_verifying_an_alien_dictionary", r'''// LeetCode 0953 - Verifying an Alien Dictionary
// https://leetcode.com/problems/verifying-an-alien-dictionary/

object Solution {
  def isAlienSorted(words: Array[String], order: String): Boolean = {
    val rank = Array.ofDim[Int](26)
    var i = 0
    while (i < 26) {
      rank(order.charAt(i) - 'a') = i
      i += 1
    }
    def lessEq(a: String, b: String): Boolean = {
      val n = math.min(a.length, b.length)
      var j = 0
      while (j < n) {
        if (rank(a.charAt(j) - 'a') != rank(b.charAt(j) - 'a'))
          return rank(a.charAt(j) - 'a') < rank(b.charAt(j) - 'a')
        j += 1
      }
      a.length <= b.length
    }
    i = 0
    while (i + 1 < words.length) {
      if (!lessEq(words(i), words(i + 1))) return false
      i += 1
    }
    true
  }
}
''')

write("0954_array_of_doubled_pairs", r'''// LeetCode 0954 - Array of Doubled Pairs
// https://leetcode.com/problems/array-of-doubled-pairs/

object Solution {
  def canReorderDoubled(arr: Array[Int]): Boolean = {
    val count = scala.collection.mutable.Map.empty[Int, Int]
    arr.foreach { x => count(x) = count.getOrElse(x, 0) + 1 }
    val keys = count.keys.toList.sortBy(math.abs)
    keys.foreach { x =>
      val need = count(x)
      if (need != 0) {
        if (count.getOrElse(2 * x, 0) < need) return false
        count(2 * x) = count(2 * x) - need
      }
    }
    true
  }
}
''')

write("0955_delete_columns_to_make_sorted_ii", r'''// LeetCode 0955 - Delete Columns to Make Sorted II
// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

object Solution {
  def minDeletionSize(strs: Array[String]): Int = {
    val n = strs.length
    val m = strs(0).length
    var deleted = 0
    val sortedPair = Array.ofDim[Boolean](n - 1)
    var c = 0
    while (c < m) {
      var bad = false
      var r = 0
      while (r + 1 < n && !bad) {
        if (!sortedPair(r) && strs(r).charAt(c) > strs(r + 1).charAt(c)) bad = true
        r += 1
      }
      if (bad) deleted += 1
      else {
        r = 0
        while (r + 1 < n) {
          if (strs(r).charAt(c) < strs(r + 1).charAt(c)) sortedPair(r) = true
          r += 1
        }
      }
      c += 1
    }
    deleted
  }
}
''')

write("0956_tallest_billboard", r'''// LeetCode 0956 - Tallest Billboard
// https://leetcode.com/problems/tallest-billboard/

object Solution {
  def tallestBillboard(rods: Array[Int]): Int = {
    var dp = scala.collection.mutable.Map(0 -> 0)
    rods.foreach { rod =>
      val cur = dp.toList
      cur.foreach { case (diff, taller) =>
        val key1 = diff + rod
        dp(key1) = math.max(dp.getOrElse(key1, 0), taller + rod)
        val nd = math.abs(diff - rod)
        val nt = if (diff >= rod) taller else taller - diff + rod
        dp(nd) = math.max(dp.getOrElse(nd, 0), nt)
      }
    }
    dp.getOrElse(0, 0)
  }
}
''')

write("0957_prison_cells_after_n_days", r'''// LeetCode 0957 - Prison Cells After N Days
// https://leetcode.com/problems/prison-cells-after-n-days/

object Solution {
  def prisonAfterNDays(cells: Array[Int], n: Int): Array[Int] = {
    val seen = scala.collection.mutable.Map.empty[String, Int]
    var state = cells.clone()
    var remain = n
    while (remain > 0) {
      val key = state.mkString(",")
      if (seen.contains(key)) {
        val cycle = seen(key) - remain
        remain %= cycle
        if (remain == 0) return state
      }
      seen(key) = remain
      val nxt = Array.ofDim[Int](8)
      var i = 1
      while (i <= 6) {
        nxt(i) = if (state(i - 1) == state(i + 1)) 1 else 0
        i += 1
      }
      state = nxt
      remain -= 1
    }
    state
  }
}
''')

write("0958_check_completeness_of_a_binary_tree", f'''// LeetCode 0958 - Check Completeness of a Binary Tree
// https://leetcode.com/problems/check-completeness-of-a-binary-tree/

{TREE}
object Solution {{
  def isCompleteTree(root: TreeNode): Boolean = {{
    val q = scala.collection.mutable.Queue[TreeNode]()
    q.enqueue(root)
    var end = false
    while (q.nonEmpty) {{
      val node = q.dequeue()
      if (node == null) end = true
      else {{
        if (end) return false
        q.enqueue(node.left)
        q.enqueue(node.right)
      }}
    }}
    true
  }}
}}
''')

write("0959_regions_cut_by_slashes", r'''// LeetCode 0959 - Regions Cut By Slashes
// https://leetcode.com/problems/regions-cut-by-slashes/

object Solution {
  def regionsBySlashes(grid: Array[String]): Int = {
    val n = grid.length
    val parent = Array.tabulate(n * n * 4)(identity)
    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }
    def unite(a: Int, b: Int): Unit = { parent(find(a)) = find(b) }
    var r = 0
    while (r < n) {
      var c = 0
      while (c < n) {
        val root = 4 * (r * n + c)
        val ch = grid(r).charAt(c)
        if (ch == '/') {
          unite(root + 0, root + 3)
          unite(root + 1, root + 2)
        } else if (ch == '\\') {
          unite(root + 0, root + 1)
          unite(root + 2, root + 3)
        } else {
          unite(root + 0, root + 1)
          unite(root + 1, root + 2)
          unite(root + 2, root + 3)
        }
        if (r + 1 < n) unite(root + 2, root + 4 * n + 0)
        if (c + 1 < n) unite(root + 1, root + 4 + 3)
        c += 1
      }
      r += 1
    }
    var ans = 0
    var i = 0
    while (i < parent.length) {
      if (find(i) == i) ans += 1
      i += 1
    }
    ans
  }
}
''')

write("0960_delete_columns_to_make_sorted_iii", r'''// LeetCode 0960 - Delete Columns to Make Sorted III
// https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

object Solution {
  def minDeletionSize(strs: Array[String]): Int = {
    val m = strs(0).length
    val dp = Array.fill(m)(1)
    var j = 0
    while (j < m) {
      var i = 0
      while (i < j) {
        var ok = true
        strs.foreach { row => if (row.charAt(i) > row.charAt(j)) ok = false }
        if (ok) dp(j) = math.max(dp(j), dp(i) + 1)
        i += 1
      }
      j += 1
    }
    m - dp.max
  }
}
''')

write("0961_n_repeated_element_in_size_2n_array", r'''// LeetCode 0961 - N-Repeated Element in Size 2N Array
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

object Solution {
  def repeatedNTimes(nums: Array[Int]): Int = {
    val seen = scala.collection.mutable.Set.empty[Int]
    nums.foreach { x =>
      if (seen.contains(x)) return x
      seen += x
    }
    -1
  }
}
''')

write("0962_maximum_width_ramp", r'''// LeetCode 0962 - Maximum Width Ramp
// https://leetcode.com/problems/maximum-width-ramp/

object Solution {
  def maxWidthRamp(nums: Array[Int]): Int = {
    val stack = scala.collection.mutable.ArrayBuffer[Int]()
    var i = 0
    while (i < nums.length) {
      if (stack.isEmpty || nums(stack.last) > nums(i)) stack += i
      i += 1
    }
    var ans = 0
    var j = nums.length - 1
    while (j >= 0) {
      while (stack.nonEmpty && nums(stack.last) <= nums(j)) {
        ans = math.max(ans, j - stack.last)
        stack.remove(stack.length - 1)
      }
      j -= 1
    }
    ans
  }
}
''')

write("0963_minimum_area_rectangle_ii", r'''// LeetCode 0963 - Minimum Area Rectangle II
// https://leetcode.com/problems/minimum-area-rectangle-ii/

object Solution {
  def minAreaFreeRect(points: Array[Array[Int]]): Double = {
    val n = points.length
    val groups = scala.collection.mutable.Map.empty[String, scala.collection.mutable.ArrayBuffer[Array[Int]]]
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        val cx = points(i)(0).toLong + points(j)(0)
        val cy = points(i)(1).toLong + points(j)(1)
        val dx = points(i)(0).toLong - points(j)(0)
        val dy = points(i)(1).toLong - points(j)(1)
        val dist = dx * dx + dy * dy
        val key = cx + "#" + cy + "#" + dist
        groups.getOrElseUpdate(key, scala.collection.mutable.ArrayBuffer.empty[Array[Int]]) += Array(i, j)
        j += 1
      }
      i += 1
    }
    var ans = 1e300
    groups.values.foreach { pairs =>
      var a = 0
      while (a < pairs.length) {
        var b = a + 1
        while (b < pairs.length) {
          val p1 = pairs(a)(0)
          val p2 = pairs(b)(0)
          val q2 = pairs(b)(1)
          val d1 = math.hypot(points(p1)(0) - points(p2)(0), points(p1)(1) - points(p2)(1))
          val d2 = math.hypot(points(p1)(0) - points(q2)(0), points(p1)(1) - points(q2)(1))
          val area = d1 * d2
          if (area > 0) ans = math.min(ans, area)
          b += 1
        }
        a += 1
      }
    }
    if (ans >= 1e299) 0.0 else ans
  }
}
''')

write("0964_least_operators_to_express_number", r'''// LeetCode 0964 - Least Operators to Express Number
// https://leetcode.com/problems/least-operators-to-express-number/

object Solution {
  def leastOpsExpressTarget(x: Int, target: Int): Int = {
    val memo = scala.collection.mutable.Map.empty[Int, Int]
    def dfs(t: Int): Int = {
      if (memo.contains(t)) return memo(t)
      if (x > t) {
        val ans = math.min(2 * t - 1, 2 * (x - t))
        memo(t) = ans
        return ans
      }
      if (x == t) {
        memo(t) = 0
        return 0
      }
      var prod = x.toLong
      var n = 0
      while (prod < t) {
        prod *= x
        n += 1
      }
      if (prod == t) {
        memo(t) = n
        return n
      }
      var ans = dfs(t - (prod / x).toInt) + n
      if (prod < 2L * t) ans = math.min(ans, dfs(prod.toInt - t) + n + 1)
      memo(t) = ans
      ans
    }
    dfs(target)
  }
}
''')

write("0965_univalued_binary_tree", f'''// LeetCode 0965 - Univalued Binary Tree
// https://leetcode.com/problems/univalued-binary-tree/

{TREE}
object Solution {{
  def isUnivalTree(root: TreeNode): Boolean = {{
    if (root == null) return true
    def dfs(node: TreeNode, v: Int): Boolean = {{
      if (node == null) return true
      if (node.value != v) return false
      dfs(node.left, v) && dfs(node.right, v)
    }}
    dfs(root, root.value)
  }}
}}
''')

write("0966_vowel_spellchecker", r'''// LeetCode 0966 - Vowel Spellchecker
// https://leetcode.com/problems/vowel-spellchecker/

object Solution {
  def spellchecker(wordlist: Array[String], queries: Array[String]): Array[String] = {
    val exact = wordlist.toSet
    val lowerMap = scala.collection.mutable.Map.empty[String, String]
    val vowelMap = scala.collection.mutable.Map.empty[String, String]
    def devowel(w: String): String = {
      val chars = w.toLowerCase.toCharArray
      var i = 0
      while (i < chars.length) {
        val c = chars(i)
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') chars(i) = '*'
        i += 1
      }
      new String(chars)
    }
    wordlist.foreach { w =>
      val low = w.toLowerCase
      if (!lowerMap.contains(low)) lowerMap(low) = w
      val dv = devowel(w)
      if (!vowelMap.contains(dv)) vowelMap(dv) = w
    }
    queries.map { q =>
      if (exact.contains(q)) q
      else if (lowerMap.contains(q.toLowerCase)) lowerMap(q.toLowerCase)
      else if (vowelMap.contains(devowel(q))) vowelMap(devowel(q))
      else ""
    }
  }
}
''')

write("0967_numbers_with_same_consecutive_differences", r'''// LeetCode 0967 - Numbers With Same Consecutive Differences
// https://leetcode.com/problems/numbers-with-same-consecutive-differences/

object Solution {
  def numsSameConsecDiff(n: Int, k: Int): Array[Int] = {
    val ans = scala.collection.mutable.ArrayBuffer[Int]()
    def dfs(num: Int, length: Int): Unit = {
      if (length == n) { ans += num; return }
      val last = num % 10
      val nexts = Set(last + k, last - k)
      nexts.foreach { nxt =>
        if (nxt >= 0 && nxt <= 9) dfs(num * 10 + nxt, length + 1)
      }
    }
    var start = 1
    while (start <= 9) {
      dfs(start, 1)
      start += 1
    }
    ans.toArray
  }
}
''')

write("0968_binary_tree_cameras", f'''// LeetCode 0968 - Binary Tree Cameras
// https://leetcode.com/problems/binary-tree-cameras/

{TREE}
object Solution {{
  def minCameraCover(root: TreeNode): Int = {{
    var cameras = 0
    def dfs(node: TreeNode): Int = {{
      if (node == null) return 1
      val left = dfs(node.left)
      val right = dfs(node.right)
      if (left == 0 || right == 0) {{
        cameras += 1
        return 2
      }}
      if (left == 2 || right == 2) return 1
      0
    }}
    val rootState = dfs(root)
    cameras + (if (rootState == 0) 1 else 0)
  }}
}}
''')

write("0969_pancake_sorting", r'''// LeetCode 0969 - Pancake Sorting
// https://leetcode.com/problems/pancake-sorting/

object Solution {
  def pancakeSort(arr: Array[Int]): List[Int] = {
    val a = arr.clone()
    val ans = scala.collection.mutable.ListBuffer[Int]()
    def indexOf(v: Int): Int = {
      var i = 0
      while (i < a.length) {
        if (a(i) == v) return i
        i += 1
      }
      -1
    }
    def reverse(l0: Int, r0: Int): Unit = {
      var l = l0
      var r = r0
      while (l < r) {
        val t = a(l); a(l) = a(r); a(r) = t
        l += 1; r -= 1
      }
    }
    var size = a.length
    while (size > 1) {
      val i = indexOf(size)
      if (i != size - 1) {
        if (i > 0) {
          ans += i + 1
          reverse(0, i)
        }
        ans += size
        reverse(0, size - 1)
      }
      size -= 1
    }
    ans.toList
  }
}
''')

write("0970_powerful_integers", r'''// LeetCode 0970 - Powerful Integers
// https://leetcode.com/problems/powerful-integers/

object Solution {
  def powerfulIntegers(x: Int, y: Int, bound: Int): List[Int] = {
    val ans = scala.collection.mutable.Set.empty[Int]
    var a = 1L
    var stopA = false
    while (a < bound && !stopA) {
      var b = 1L
      var stopB = false
      while (a + b <= bound && !stopB) {
        ans += (a + b).toInt
        if (y == 1) stopB = true
        else b *= y
      }
      if (x == 1) stopA = true
      else a *= x
    }
    ans.toList
  }
}
''')

write("0971_flip_binary_tree_to_match_preorder_traversal", f'''// LeetCode 0971 - Flip Binary Tree To Match Preorder Traversal
// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

{TREE}
object Solution {{
  def flipMatchVoyage(root: TreeNode, voyage: Array[Int]): List[Int] = {{
    var i = 0
    val ans = scala.collection.mutable.ListBuffer[Int]()
    def dfs(node: TreeNode): Boolean = {{
      if (node == null) return true
      if (node.value != voyage(i)) return false
      i += 1
      if (node.left != null && node.left.value != voyage(i)) {{
        ans += node.value
        return dfs(node.right) && dfs(node.left)
      }}
      dfs(node.left) && dfs(node.right)
    }}
    if (dfs(root)) ans.toList else List(-1)
  }}
}}
''')

write("0972_equal_rational_numbers", r'''// LeetCode 0972 - Equal Rational Numbers
// https://leetcode.com/problems/equal-rational-numbers/

object Solution {
  def isRationalEqual(s: String, t: String): Boolean = {
    math.abs(parse(s) - parse(t)) < 1e-12
  }

  private def parse(x: String): Double = {
    if (!x.contains("(")) return if (x.isEmpty) 0.0 else x.toDouble
    val lp = x.indexOf('(')
    var nonRep = x.substring(0, lp)
    val rep = x.substring(lp + 1, x.length - 1)
    if (!nonRep.contains(".")) nonRep += "."
    val dot = nonRep.indexOf('.')
    val integer = nonRep.substring(0, dot)
    val frac = nonRep.substring(dot + 1)
    var bas = if (integer.isEmpty) 0.0 else integer.toDouble
    if (frac.length > 0) {
      var denom = 1.0
      var i = 0
      while (i < frac.length) { denom *= 10; i += 1 }
      bas += frac.toDouble / denom
    }
    if (rep.length > 0) {
      val repVal = rep.toDouble
      var cycle = 1.0
      var i = 0
      while (i < rep.length) { cycle *= 10; i += 1 }
      var denom = cycle - 1
      i = 0
      while (i < frac.length) { denom *= 10; i += 1 }
      bas += repVal / denom
    }
    bas
  }
}
''')

write("0973_k_closest_points_to_origin", r'''// LeetCode 0973 - K Closest Points to Origin
// https://leetcode.com/problems/k-closest-points-to-origin/

object Solution {
  def kClosest(points: Array[Array[Int]], k: Int): Array[Array[Int]] = {
    points.sortBy(p => p(0).toLong * p(0) + p(1).toLong * p(1)).take(k)
  }
}
''')

write("0974_subarray_sums_divisible_by_k", r'''// LeetCode 0974 - Subarray Sums Divisible by K
// https://leetcode.com/problems/subarray-sums-divisible-by-k/

object Solution {
  def subarraysDivByK(nums: Array[Int], k: Int): Int = {
    val count = scala.collection.mutable.Map(0 -> 1)
    var prefix = 0
    var ans = 0
    nums.foreach { x =>
      prefix = ((prefix + x) % k + k) % k
      ans += count.getOrElse(prefix, 0)
      count(prefix) = count.getOrElse(prefix, 0) + 1
    }
    ans
  }
}
''')

write("0975_odd_even_jump", r'''// LeetCode 0975 - Odd Even Jump
// https://leetcode.com/problems/odd-even-jump/

object Solution {
  def oddEvenJumps(arr: Array[Int]): Int = {
    val n = arr.length
    val nextHigher = Array.ofDim[Int](n)
    val nextLower = Array.ofDim[Int](n)
    var order = arr.indices.sortBy(i => (arr(i), i)).toArray
    val stack = scala.collection.mutable.ArrayBuffer[Int]()
    order.foreach { i =>
      while (stack.nonEmpty && stack.last < i) {
        nextHigher(stack.last) = i
        stack.remove(stack.length - 1)
      }
      stack += i
    }
    stack.clear()
    order = arr.indices.sortBy(i => (-arr(i), i)).toArray
    order.foreach { i =>
      while (stack.nonEmpty && stack.last < i) {
        nextLower(stack.last) = i
        stack.remove(stack.length - 1)
      }
      stack += i
    }
    val odd = Array.ofDim[Boolean](n)
    val even = Array.ofDim[Boolean](n)
    odd(n - 1) = true
    even(n - 1) = true
    var i = n - 2
    while (i >= 0) {
      if (nextHigher(i) != 0) odd(i) = even(nextHigher(i))
      if (nextLower(i) != 0) even(i) = odd(nextLower(i))
      i -= 1
    }
    odd.count(identity)
  }
}
''')

write("0976_largest_perimeter_triangle", r'''// LeetCode 0976 - Largest Perimeter Triangle
// https://leetcode.com/problems/largest-perimeter-triangle/

object Solution {
  def largestPerimeter(nums: Array[Int]): Int = {
    val arr = nums.sorted
    var i = arr.length - 1
    while (i >= 2) {
      if (arr(i) < arr(i - 1) + arr(i - 2))
        return arr(i) + arr(i - 1) + arr(i - 2)
      i -= 1
    }
    0
  }
}
''')

write("0977_squares_of_a_sorted_array", r'''// LeetCode 0977 - Squares of a Sorted Array
// https://leetcode.com/problems/squares-of-a-sorted-array/

object Solution {
  def sortedSquares(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val ans = Array.ofDim[Int](n)
    var i = 0
    var j = n - 1
    var k = n - 1
    while (k >= 0) {
      if (math.abs(nums(i)) > math.abs(nums(j))) {
        ans(k) = nums(i) * nums(i)
        i += 1
      } else {
        ans(k) = nums(j) * nums(j)
        j -= 1
      }
      k -= 1
    }
    ans
  }
}
''')

write("0978_longest_turbulent_subarray", r'''// LeetCode 0978 - Longest Turbulent Subarray
// https://leetcode.com/problems/longest-turbulent-subarray/

object Solution {
  def maxTurbulenceSize(arr: Array[Int]): Int = {
    var ans = 1
    var cur = 1
    var i = 1
    while (i < arr.length) {
      if (arr(i) == arr(i - 1)) cur = 1
      else if (i == 1 || (arr(i).toLong - arr(i - 1)) * (arr(i - 1).toLong - arr(i - 2)) < 0) cur += 1
      else cur = 2
      ans = math.max(ans, cur)
      i += 1
    }
    ans
  }
}
''')

write("0979_distribute_coins_in_binary_tree", f'''// LeetCode 0979 - Distribute Coins in Binary Tree
// https://leetcode.com/problems/distribute-coins-in-binary-tree/

{TREE}
object Solution {{
  def distributeCoins(root: TreeNode): Int = {{
    var ans = 0
    def dfs(node: TreeNode): Int = {{
      if (node == null) return 0
      val left = dfs(node.left)
      val right = dfs(node.right)
      ans += math.abs(left) + math.abs(right)
      node.value + left + right - 1
    }}
    dfs(root)
    ans
  }}
}}
''')

print("done part b")
