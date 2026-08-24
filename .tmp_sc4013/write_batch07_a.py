#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("2304_minimum_path_cost_in_a_grid", r'''
// LeetCode 2304 - Minimum Path Cost in a Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-grid/

object Solution {
  def minPathCost(grid: Array[Array[Int]], moveCost: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var dp = grid(0).clone()
    var r = 0
    while (r < m - 1) {
      val next = Array.fill(n)(Int.MaxValue / 2)
      var c = 0
      while (c < n) {
        val from = grid(r)(c)
        var nc = 0
        while (nc < n) {
          next(nc) = math.min(next(nc), dp(c) + moveCost(from)(nc) + grid(r + 1)(nc))
          nc += 1
        }
        c += 1
      }
      dp = next
      r += 1
    }
    var ans = dp(0)
    var i = 1
    while (i < n) {
      ans = math.min(ans, dp(i))
      i += 1
    }
    ans
  }
}
''')

w("2305_fair_distribution_of_cookies", r'''
// LeetCode 2305 - Fair Distribution of Cookies
// https://leetcode.com/problems/fair-distribution-of-cookies/

object Solution {
  def distributeCookies(cookies: Array[Int], k: Int): Int = {
    val bags = Array.fill(k)(0)
    var ans = Int.MaxValue

    def dfs(i: Int): Unit = {
      if (i == cookies.length) {
        var mx = 0
        bags.foreach(b => mx = math.max(mx, b))
        ans = math.min(ans, mx)
        return
      }
      val seen = scala.collection.mutable.HashSet.empty[Int]
      var j = 0
      while (j < bags.length) {
        if (seen.add(bags(j))) {
          bags(j) += cookies(i)
          if (bags(j) < ans) dfs(i + 1)
          bags(j) -= cookies(i)
          if (bags(j) == 0) return
        }
        j += 1
      }
    }

    dfs(0)
    ans
  }
}
''')

w("2306_naming_a_company", r'''
// LeetCode 2306 - Naming a Company
// https://leetcode.com/problems/naming-a-company/

object Solution {
  def distinctNames(ideas: Array[String]): Long = {
    val groups = Array.fill(26)(scala.collection.mutable.HashSet.empty[String])
    ideas.foreach { idea =>
      groups(idea.charAt(0) - 'a') += idea.substring(1)
    }
    var ans = 0L
    var i = 0
    while (i < 26) {
      var j = i + 1
      while (j < 26) {
        var overlap = 0
        groups(i).foreach { s =>
          if (groups(j).contains(s)) overlap += 1
        }
        ans += (groups(i).size - overlap).toLong * (groups(j).size - overlap) * 2
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("2307_check_for_contradictions_in_equations", r'''
// LeetCode 2307 - Check for Contradictions in Equations
// https://leetcode.com/problems/check-for-contradictions-in-equations/

object Solution {
  def checkContradictions(equations: List[List[String]], values: Array[Double]): Boolean = {
    val parent = scala.collection.mutable.Map.empty[String, String]
    val weight = scala.collection.mutable.Map.empty[String, Double]

    def find(x: String): String = {
      if (!parent.contains(x)) {
        parent(x) = x
        weight(x) = 1.0
        return x
      }
      if (parent(x) != x) {
        val old = parent(x)
        val p = find(old)
        weight(x) = weight(x) * weight(old)
        parent(x) = p
      }
      parent(x)
    }

    var i = 0
    while (i < equations.length) {
      val a = equations(i)(0)
      val b = equations(i)(1)
      val ra = find(a)
      val rb = find(b)
      if (ra == rb) {
        if (math.abs(weight(a) / weight(b) - values(i)) > 1e-5) return true
      } else {
        parent(ra) = rb
        weight(ra) = values(i) * weight(b) / weight(a)
      }
      i += 1
    }
    false
  }
}
''')

w("2309_greatest_english_letter_in_upper_and_lower_case", r'''
// LeetCode 2309 - Greatest English Letter in Upper and Lower Case
// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

object Solution {
  def greatestLetter(s: String): String = {
    val lower = Array.fill(26)(false)
    val upper = Array.fill(26)(false)
    s.foreach { c =>
      if (c >= 'a' && c <= 'z') lower(c - 'a') = true
      else upper(c - 'A') = true
    }
    var i = 25
    while (i >= 0) {
      if (lower(i) && upper(i)) return ('A' + i).toChar.toString
      i -= 1
    }
    ""
  }
}
''')

w("2310_sum_of_numbers_with_units_digit_k", r'''
// LeetCode 2310 - Sum of Numbers With Units Digit K
// https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

object Solution {
  def minimumNumbers(num: Int, k: Int): Int = {
    if (num == 0) return 0
    var count = 1
    while (count <= 10) {
      if (count * k % 10 == num % 10 && count * k <= num) return count
      count += 1
    }
    -1
  }
}
''')

w("2311_longest_binary_subsequence_less_than_or_equal_to_k", r'''
// LeetCode 2311 - Longest Binary Subsequence Less Than or Equal to K
// https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

object Solution {
  def longestSubsequence(s: String, k: Int): Int = {
    var zeros = 0
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == '0') zeros += 1
      i += 1
    }
    var value = 0L
    var ones = 0
    var pow = 1L
    i = s.length - 1
    while (i >= 0) {
      if (s.charAt(i) == '1') {
        if (!(pow > k || value + pow > k)) {
          value += pow
          ones += 1
        }
      }
      if (pow <= k) {
        if (pow > (1L << 60)) pow = k + 1L
        else pow <<= 1
      }
      i -= 1
    }
    zeros + ones
  }
}
''')

w("2312_selling_pieces_of_wood", r'''
// LeetCode 2312 - Selling Pieces of Wood
// https://leetcode.com/problems/selling-pieces-of-wood/

object Solution {
  def sellingWood(m: Int, n: Int, prices: Array[Array[Int]]): Long = {
    val price = Array.ofDim[Long](m + 1, n + 1)
    val dp = Array.ofDim[Long](m + 1, n + 1)
    prices.foreach { p => price(p(0))(p(1)) = p(2) }
    var h = 1
    while (h <= m) {
      var w = 1
      while (w <= n) {
        var best = price(h)(w)
        var i = 1
        while (i < h) {
          best = math.max(best, dp(i)(w) + dp(h - i)(w))
          i += 1
        }
        var j = 1
        while (j < w) {
          best = math.max(best, dp(h)(j) + dp(h)(w - j))
          j += 1
        }
        dp(h)(w) = best
        w += 1
      }
      h += 1
    }
    dp(m)(n)
  }
}
''')

w("2313_minimum_flips_in_binary_tree_to_get_result", r'''
// LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
// https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def minimumFlips(root: TreeNode, result: Boolean): Int = {
    val res = dfs(root)
    if (result) res(1) else res(0)
  }

  private def dfs(node: TreeNode): Array[Int] = {
    if (node.left == null && node.right == null) {
      return if (node.value == 0) Array(0, 1) else Array(1, 0)
    }
    if (node.value == 5) {
      val x = dfs(node.left)
      return Array(x(1), x(0))
    }
    val L = dfs(node.left)
    val R = dfs(node.right)
    val lf = L(0)
    val lt = L(1)
    val rf = R(0)
    val rt = R(1)
    if (node.value == 2) {
      return Array(lf + rf, math.min(lt + rt, math.min(lt + rf, lf + rt)))
    }
    if (node.value == 3) {
      return Array(math.min(lf + rf, math.min(lf + rt, lt + rf)), lt + rt)
    }
    if (node.value == 4) {
      return Array(math.min(lf + rf, lt + rt), math.min(lf + rt, lt + rf))
    }
    Array(0, 0)
  }
}
''')

w("2315_count_asterisks", r'''
// LeetCode 2315 - Count Asterisks
// https://leetcode.com/problems/count-asterisks/

object Solution {
  def countAsterisks(s: String): Int = {
    var ans = 0
    var inside = false
    s.foreach { c =>
      if (c == '|') inside = !inside
      else if (c == '*' && !inside) ans += 1
    }
    ans
  }
}
''')

w("2316_count_unreachable_pairs_of_nodes_in_an_undirected_graph", r'''
// LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

object Solution {
  def countPairs(n: Int, edges: Array[Array[Int]]): Long = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val vis = Array.fill(n)(false)

    def dfs(u: Int): Int = {
      vis(u) = true
      var size = 1
      g(u).foreach { v =>
        if (!vis(v)) size += dfs(v)
      }
      size
    }

    var ans = 0L
    var seen = 0L
    var i = 0
    while (i < n) {
      if (!vis(i)) {
        val sz = dfs(i).toLong
        ans += sz * seen
        seen += sz
      }
      i += 1
    }
    ans
  }
}
''')

w("2317_maximum_xor_after_operations", r'''
// LeetCode 2317 - Maximum XOR After Operations
// https://leetcode.com/problems/maximum-xor-after-operations/

object Solution {
  def maximumXOR(nums: Array[Int]): Int = {
    var ans = 0
    nums.foreach(x => ans |= x)
    ans
  }
}
''')

w("2318_number_of_distinct_roll_sequences", r'''
// LeetCode 2318 - Number of Distinct Roll Sequences
// https://leetcode.com/problems/number-of-distinct-roll-sequences/

object Solution {
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

  def distinctSequences(n: Int): Int = {
    val mod = 1000000007
    val dp = Array.ofDim[Int](n + 1, 7, 7)
    var a = 1
    while (a <= 6) {
      dp(1)(a)(0) = 1
      a += 1
    }
    var i = 2
    while (i <= n) {
      var prev = 1
      while (prev <= 6) {
        var pprev = 0
        while (pprev <= 6) {
          if (dp(i - 1)(prev)(pprev) != 0) {
            var cur = 1
            while (cur <= 6) {
              if (!(cur == prev || cur == pprev || gcd(cur, prev) != 1)) {
                dp(i)(cur)(prev) = (dp(i)(cur)(prev) + dp(i - 1)(prev)(pprev)) % mod
              }
              cur += 1
            }
          }
          pprev += 1
        }
        prev += 1
      }
      i += 1
    }
    var ans = 0
    a = 1
    while (a <= 6) {
      var b = 0
      while (b <= 6) {
        ans = (ans + dp(n)(a)(b)) % mod
        b += 1
      }
      a += 1
    }
    ans
  }
}
''')

w("2319_check_if_matrix_is_x_matrix", r'''
// LeetCode 2319 - Check if Matrix Is X-Matrix
// https://leetcode.com/problems/check-if-matrix-is-x-matrix/

object Solution {
  def checkXMatrix(grid: Array[Array[Int]]): Boolean = {
    val n = grid.length
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        val diag = i == j || i + j == n - 1
        if (diag) {
          if (grid(i)(j) == 0) return false
        } else if (grid(i)(j) != 0) return false
        j += 1
      }
      i += 1
    }
    true
  }
}
''')

w("2320_count_number_of_ways_to_place_houses", r'''
// LeetCode 2320 - Count Number of Ways to Place Houses
// https://leetcode.com/problems/count-number-of-ways-to-place-houses/

object Solution {
  def countHousePlacements(n: Int): Int = {
    val mod = 1000000007
    var a = 1L
    var b = 1L
    var i = 1
    while (i <= n) {
      val na = (a + b) % mod
      b = a
      a = na
      i += 1
    }
    val ways = (a + b) % mod
    (ways * ways % mod).toInt
  }
}
''')

w("2321_maximum_score_of_spliced_array", r'''
// LeetCode 2321 - Maximum Score Of Spliced Array
// https://leetcode.com/problems/maximum-score-of-spliced-array/

object Solution {
  def maximumsSplicedArray(nums1: Array[Int], nums2: Array[Int]): Int = {
    math.max(kadane(nums1, nums2), kadane(nums2, nums1))
  }

  private def kadane(a: Array[Int], b: Array[Int]): Int = {
    var best = 0
    var cur = 0
    var sum = 0
    var i = 0
    while (i < a.length) {
      sum += a(i)
      cur += b(i) - a(i)
      if (cur < 0) cur = 0
      best = math.max(best, cur)
      i += 1
    }
    sum + best
  }
}
''')

w("2322_minimum_score_after_removals_on_a_tree", r'''
// LeetCode 2322 - Minimum Score After Removals on a Tree
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

object Solution {
  def minimumScore(nums: Array[Int], edges: Array[Array[Int]]): Int = {
    val n = nums.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val xorv = Array.fill(n)(0)
    val inT = Array.fill(n)(0)
    val outT = Array.fill(n)(0)
    var time = 0

    def dfs(u: Int, p: Int): Unit = {
      inT(u) = time
      time += 1
      xorv(u) = nums(u)
      g(u).foreach { v =>
        if (v != p) {
          dfs(v, u)
          xorv(u) ^= xorv(v)
        }
      }
      outT(u) = time
    }

    def isAncestor(a: Int, b: Int): Boolean = inT(a) <= inT(b) && outT(b) <= outT(a)

    dfs(0, -1)
    val total = xorv(0)
    var ans = Int.MaxValue
    var i = 1
    while (i < n) {
      var j = i + 1
      while (j < n) {
        val (a, b, c) =
          if (isAncestor(i, j)) (xorv(j), xorv(i) ^ xorv(j), total ^ xorv(i))
          else if (isAncestor(j, i)) (xorv(i), xorv(j) ^ xorv(i), total ^ xorv(j))
          else (xorv(i), xorv(j), total ^ xorv(i) ^ xorv(j))
        val mx = math.max(a, math.max(b, c))
        val mn = math.min(a, math.min(b, c))
        ans = math.min(ans, mx - mn)
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("2323_find_minimum_time_to_finish_all_jobs_ii", r'''
// LeetCode 2323 - Find Minimum Time to Finish All Jobs II
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

object Solution {
  def minimumTime(jobs: Array[Int], workers: Array[Int]): Int = {
    java.util.Arrays.sort(jobs)
    java.util.Arrays.sort(workers)
    var ans = 0
    var i = 0
    while (i < jobs.length) {
      ans = math.max(ans, (jobs(i) + workers(i) - 1) / workers(i))
      i += 1
    }
    ans
  }
}
''')

w("2325_decode_the_message", r'''
// LeetCode 2325 - Decode the Message
// https://leetcode.com/problems/decode-the-message/

object Solution {
  def decodeMessage(key: String, message: String): String = {
    val mp = Array.fill(26)(0.toChar)
    var next = 'a'
    key.foreach { c =>
      if (c != ' ' && mp(c - 'a') == 0) {
        mp(c - 'a') = next
        next = (next + 1).toChar
      }
    }
    val outc = message.toCharArray
    var i = 0
    while (i < outc.length) {
      if (outc(i) != ' ') outc(i) = mp(outc(i) - 'a')
      i += 1
    }
    new String(outc)
  }
}
''')

w("2326_spiral_matrix_iv", r'''
// LeetCode 2326 - Spiral Matrix IV
// https://leetcode.com/problems/spiral-matrix-iv/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def spiralMatrix(m: Int, n: Int, head0: ListNode): Array[Array[Int]] = {
    val ans = Array.fill(m, n)(-1)
    val dirs = Array(Array(0, 1), Array(1, 0), Array(0, -1), Array(-1, 0))
    var r = 0
    var c = 0
    var d = 0
    var head = head0
    while (head != null) {
      ans(r)(c) = head.x
      head = head.next
      var nr = r + dirs(d)(0)
      var nc = c + dirs(d)(1)
      if (nr < 0 || nr >= m || nc < 0 || nc >= n || ans(nr)(nc) != -1) {
        d = (d + 1) % 4
        nr = r + dirs(d)(0)
        nc = c + dirs(d)(1)
      }
      r = nr
      c = nc
    }
    ans
  }
}
''')

w("2327_number_of_people_aware_of_a_secret", r'''
// LeetCode 2327 - Number of People Aware of a Secret
// https://leetcode.com/problems/number-of-people-aware-of-a-secret/

object Solution {
  def peopleAwareOfSecret(n: Int, delay: Int, forget: Int): Int = {
    val mod = 1000000007
    val dp = Array.fill(n + 1)(0)
    dp(1) = 1
    var share = 0
    var day = 2
    while (day <= n) {
      if (day - delay >= 1) share = (share + dp(day - delay)) % mod
      if (day - forget >= 1) share = (share - dp(day - forget) + mod) % mod
      dp(day) = share
      day += 1
    }
    var ans = 0
    day = n - forget + 1
    while (day <= n) {
      if (day >= 1) ans = (ans + dp(day)) % mod
      day += 1
    }
    ans
  }
}
''')

w("2328_number_of_increasing_paths_in_a_grid", r'''
// LeetCode 2328 - Number of Increasing Paths in a Grid
// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

object Solution {
  def countPaths(grid: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val m = grid.length
    val n = grid(0).length
    val dp = Array.ofDim[Int](m, n)
    val dirs = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))

    def dfs(r: Int, c: Int): Int = {
      if (dp(r)(c) != 0) return dp(r)(c)
      var res = 1
      dirs.foreach { d =>
        val nr = r + d(0)
        val nc = c + d(1)
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) > grid(r)(c)) {
          res = (res + dfs(nr, nc)) % MOD
        }
      }
      dp(r)(c) = res
      res
    }

    var ans = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        ans = (ans + dfs(i, j)) % MOD
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("2330_valid_palindrome_iv", r'''
// LeetCode 2330 - Valid Palindrome IV
// https://leetcode.com/problems/valid-palindrome-iv/

object Solution {
  def makePalindrome(s: String): Boolean = {
    var diff = 0
    var i = 0
    var j = s.length - 1
    while (i < j) {
      if (s.charAt(i) != s.charAt(j)) {
        diff += 1
        if (diff > 2) return false
      }
      i += 1
      j -= 1
    }
    true
  }
}
''')

w("2331_evaluate_boolean_binary_tree", r'''
// LeetCode 2331 - Evaluate Boolean Binary Tree
// https://leetcode.com/problems/evaluate-boolean-binary-tree/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def evaluateTree(root: TreeNode): Boolean = {
    if (root.left == null && root.right == null) return root.value == 1
    val l = evaluateTree(root.left)
    val r = evaluateTree(root.right)
    if (root.value == 2) l || r else l && r
  }
}
''')

w("2332_the_latest_time_to_catch_a_bus", r'''
// LeetCode 2332 - The Latest Time to Catch a Bus
// https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

object Solution {
  def latestTimeCatchTheBus(buses: Array[Int], passengers: Array[Int], capacity: Int): Int = {
    java.util.Arrays.sort(buses)
    java.util.Arrays.sort(passengers)
    var pos = 0
    var bi = 0
    while (bi < buses.length) {
      val bus = buses(bi)
      var cap = capacity
      while (cap > 0 && pos < passengers.length && passengers(pos) <= bus) {
        pos += 1
        cap -= 1
      }
      if (bi == buses.length - 1) {
        var cand = if (cap == 0) passengers(pos - 1) else bus
        val taken = scala.collection.mutable.HashSet.empty[Int]
        passengers.foreach(p => taken += p)
        while (taken.contains(cand)) cand -= 1
        return cand
      }
      bi += 1
    }
    -1
  }
}
''')
