#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("2466_count_ways_to_build_good_strings", r'''
// LeetCode 2466 - Count Ways To Build Good Strings
// https://leetcode.com/problems/count-ways-to-build-good-strings/

object Solution {
  def countGoodStrings(low: Int, high: Int, zero: Int, one: Int): Int = {
    val mod = 1000000007
    val dp = new Array[Int](high + 1)
    dp(0) = 1
    var ans = 0
    var i = 1
    while (i <= high) {
      if (i >= zero) dp(i) = (dp(i) + dp(i - zero)) % mod
      if (i >= one) dp(i) = (dp(i) + dp(i - one)) % mod
      if (i >= low) ans = (ans + dp(i)) % mod
      i += 1
    }
    ans
  }
}
''')

w("2467_most_profitable_path_in_a_tree", r'''
// LeetCode 2467 - Most Profitable Path in a Tree
// https://leetcode.com/problems/most-profitable-path-in-a-tree/

object Solution {
  def mostProfitablePath(edges: Array[Array[Int]], bob: Int, amount: Array[Int]): Int = {
    val n = amount.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val bobTime = Array.fill(n)(n)

    def findBob(u: Int, p: Int, t: Int): Boolean = {
      if (u == 0) {
        bobTime(u) = t
        return true
      }
      g(u).foreach { v =>
        if (v != p && findBob(v, u, t + 1)) {
          bobTime(u) = t
          return true
        }
      }
      false
    }

    findBob(bob, -1, 0)
    var ans = Int.MinValue

    def dfs(u: Int, p: Int, t: Int, income0: Int): Unit = {
      var cur = amount(u)
      if (t > bobTime(u)) cur = 0
      else if (t == bobTime(u)) cur /= 2
      val income = income0 + cur
      var isLeaf = true
      g(u).foreach { v =>
        if (v != p) {
          isLeaf = false
          dfs(v, u, t + 1, income)
        }
      }
      if (isLeaf && income > ans) ans = income
    }

    dfs(0, -1, 0, 0)
    ans
  }
}
''')

w("2468_split_message_based_on_limit", r'''
// LeetCode 2468 - Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/

object Solution {
  def splitMessage(message: String, limit: Int): Array[String] = {
    val n = message.length
    var parts = 1
    while (parts <= n) {
      val sbDigits = parts.toString.length
      var ok = true
      var idx = 0
      val res = scala.collection.mutable.ArrayBuffer.empty[String]
      var i = 1
      while (i <= parts && ok) {
        val tail = 3 + i.toString.length + sbDigits
        val cap = limit - tail
        if (cap <= 0 || idx >= n) ok = false
        else {
          var take = cap
          if (take > n - idx) take = n - idx
          res += message.substring(idx, idx + take) + "<" + i + "/" + parts + ">"
          idx += take
        }
        i += 1
      }
      if (ok && idx == n) return res.toArray
      parts += 1
    }
    Array.empty[String]
  }
}
''')

w("2469_convert_the_temperature", r'''
// LeetCode 2469 - Convert the Temperature
// https://leetcode.com/problems/convert-the-temperature/

object Solution {
  def convertTemperature(celsius: Double): Array[Double] = {
    Array(celsius + 273.15, celsius * 1.80 + 32.00)
  }
}
''')

w("2470_number_of_subarrays_with_lcm_equal_to_k", r'''
// LeetCode 2470 - Number of Subarrays With LCM Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

object Solution {
  def subarrayLCM(nums: Array[Int], k: Int): Int = {
    def gcd(x: Int, y: Int): Int = {
      var a = x
      var b = y
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    var ans = 0
    val n = nums.length
    var i = 0
    while (i < n) {
      var cur = 1L
      var j = i
      var cont = true
      while (j < n && cont) {
        cur = cur / gcd(cur.toInt, nums(j)) * nums(j)
        if (cur > k) cont = false
        else {
          if (cur == k) ans += 1
          j += 1
        }
      }
      i += 1
    }
    ans
  }
}
''')

w("2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level", r'''
// LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def minimumOperations(root: TreeNode): Int = {
    if (root == null) return 0
    var ans = 0
    val q = scala.collection.mutable.Queue[TreeNode](root)
    while (q.nonEmpty) {
      val sz = q.size
      val vals = new Array[Int](sz)
      var i = 0
      while (i < sz) {
        val node = q.dequeue()
        vals(i) = node.value
        if (node.left != null) q.enqueue(node.left)
        if (node.right != null) q.enqueue(node.right)
        i += 1
      }
      val sorted = vals.clone()
      scala.util.Sorting.quickSort(sorted)
      val pos = scala.collection.mutable.Map.empty[Int, Int]
      i = 0
      while (i < sz) {
        pos(vals(i)) = i
        i += 1
      }
      i = 0
      while (i < sz) {
        if (vals(i) != sorted(i)) {
          val j = pos(sorted(i))
          val tmp = vals(i)
          vals(i) = vals(j)
          vals(j) = tmp
          pos(vals(j)) = j
          pos(vals(i)) = i
          ans += 1
        }
        i += 1
      }
    }
    ans
  }
}
''')

w("2472_maximum_number_of_non_overlapping_palindrome_substrings", r'''
// LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

object Solution {
  def maxPalindromes(s: String, k: Int): Int = {
    val n = s.length
    val isPal = Array.ofDim[Boolean](n, n)
    var i = 0
    while (i < n) {
      isPal(i)(i) = true
      i += 1
    }
    i = 0
    while (i + 1 < n) {
      isPal(i)(i + 1) = s.charAt(i) == s.charAt(i + 1)
      i += 1
    }
    var length = 3
    while (length <= n) {
      i = 0
      while (i + length - 1 < n) {
        val j = i + length - 1
        isPal(i)(j) = s.charAt(i) == s.charAt(j) && isPal(i + 1)(j - 1)
        i += 1
      }
      length += 1
    }
    val dp = new Array[Int](n + 1)
    i = n - 1
    while (i >= 0) {
      dp(i) = dp(i + 1)
      var j = i + k - 1
      while (j < n) {
        if (isPal(i)(j) && 1 + dp(j + 1) > dp(i)) dp(i) = 1 + dp(j + 1)
        j += 1
      }
      i -= 1
    }
    dp(0)
  }
}
''')

w("2473_minimum_cost_to_buy_apples", r'''
// LeetCode 2473 - Minimum Cost to Buy Apples
// https://leetcode.com/problems/minimum-cost-to-buy-apples/

object Solution {
  def minCost(n: Int, roads: Array[Array[Int]], appleCost: Array[Int], k: Int): Array[Long] = {
    val g = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    roads.foreach { r =>
      g(r(0)) += ((r(1), r(2)))
      g(r(1)) += ((r(0), r(2)))
    }
    val ans = new Array[Long](n)
    val INF = 1L << 60
    implicit val ord: Ordering[(Long, Int)] = Ordering.by[(Long, Int), Long](_._1).reverse
    var start = 1
    while (start <= n) {
      val dist = Array.fill(n + 1)(INF)
      dist(start) = 0
      val pq = scala.collection.mutable.PriorityQueue.empty[(Long, Int)]
      pq.enqueue((0L, start))
      while (pq.nonEmpty) {
        val (d, u) = pq.dequeue()
        if (d == dist(u)) {
          g(u).foreach { case (v, w) =>
            val nd = d + w
            if (nd < dist(v)) {
              dist(v) = nd
              pq.enqueue((nd, v))
            }
          }
        }
      }
      var best = INF
      var city = 1
      while (city <= n) {
        val cost = dist(city) * (k + 1) + appleCost(city - 1)
        if (cost < best) best = cost
        city += 1
      }
      ans(start - 1) = best
      start += 1
    }
    ans
  }
}
''')

w("2475_number_of_unequal_triplets_in_array", r'''
// LeetCode 2475 - Number of Unequal Triplets in Array
// https://leetcode.com/problems/number-of-unequal-triplets-in-array/

object Solution {
  def unequalTriplets(nums: Array[Int]): Int = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var i = 0
    while (i < nums.length) {
      cnt(nums(i)) = cnt.getOrElse(nums(i), 0) + 1
      i += 1
    }
    var ans = 0
    val n = nums.length
    var left = 0
    cnt.values.foreach { c =>
      val right = n - left - c
      ans += left * c * right
      left += c
    }
    ans
  }
}
''')

w("2476_closest_nodes_queries_in_a_binary_search_tree", r'''
// LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def closestNodes(root: TreeNode, queries: List[Int]): List[List[Int]] = {
    val vals = scala.collection.mutable.ArrayBuffer.empty[Int]
    def inorder(node: TreeNode): Unit = {
      if (node == null) return
      inorder(node.left)
      vals += node.value
      inorder(node.right)
    }
    inorder(root)

    def lowerBound(q: Int): Int = {
      var lo = 0
      var hi = vals.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (vals(mid) < q) lo = mid + 1
        else hi = mid
      }
      lo
    }

    queries.map { q =>
      val j = lowerBound(q)
      val mx = if (j < vals.length) vals(j) else -1
      val mn =
        if (j < vals.length && vals(j) == q) q
        else if (j > 0) vals(j - 1)
        else -1
      List(mn, mx)
    }
  }
}
''')

w("2477_minimum_fuel_cost_to_report_to_the_capital", r'''
// LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

object Solution {
  def minimumFuelCost(roads: Array[Array[Int]], seats: Int): Long = {
    val n = roads.length + 1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    roads.foreach { r =>
      g(r(0)) += r(1)
      g(r(1)) += r(0)
    }
    var ans = 0L

    def dfs(u: Int, p: Int): Int = {
      var people = 1
      g(u).foreach { v =>
        if (v != p) people += dfs(v, u)
      }
      if (u != 0) ans += (people + seats - 1) / seats
      people
    }

    dfs(0, -1)
    ans
  }
}
''')

w("2478_number_of_beautiful_partitions", r'''
// LeetCode 2478 - Number of Beautiful Partitions
// https://leetcode.com/problems/number-of-beautiful-partitions/

object Solution {
  def beautifulPartitions(s: String, k: Int, minLength: Int): Int = {
    def isPrime(c: Char): Boolean = c == '2' || c == '3' || c == '5' || c == '7'
    val mod = 1000000007
    val n = s.length
    if (!isPrime(s.charAt(0)) || isPrime(s.charAt(n - 1))) return 0
    val dp = Array.ofDim[Int](k + 1, n + 1)
    dp(0)(0) = 1
    var p = 1
    while (p <= k) {
      var pref = 0
      var j = 0
      var i = 1
      while (i <= n) {
        while (j <= i - minLength) {
          if (j == 0 || (isPrime(s.charAt(j)) && !isPrime(s.charAt(j - 1)))) {
            pref = (pref + dp(p - 1)(j)) % mod
          }
          j += 1
        }
        if (!isPrime(s.charAt(i - 1))) dp(p)(i) = pref
        i += 1
      }
      p += 1
    }
    dp(k)(n)
  }
}
''')

w("2479_maximum_xor_of_two_non_overlapping_subtrees", r'''
// LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
// https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

object Solution {
  private class Trie {
    val child = Array.fill[Trie](2)(null)
  }

  def maxXor(n: Int, edges: Array[Array[Int]], values: Array[Int]): Long = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val sum = new Array[Long](n)

    def dfsSum(u: Int, p: Int): Long = {
      var s = values(u).toLong
      g(u).foreach { v => if (v != p) s += dfsSum(v, u) }
      sum(u) = s
      s
    }

    val root = new Trie()
    var ans = 0L

    def insert(x: Long): Unit = {
      var cur = root
      var b = 46
      while (b >= 0) {
        val bit = ((x >> b) & 1).toInt
        if (cur.child(bit) == null) cur.child(bit) = new Trie()
        cur = cur.child(bit)
        b -= 1
      }
    }

    def query(x: Long): Long = {
      var cur = root
      if (cur.child(0) == null && cur.child(1) == null) return 0L
      var res = 0L
      var b = 46
      while (b >= 0) {
        val bit = ((x >> b) & 1).toInt
        val want = bit ^ 1
        if (cur.child(want) != null) {
          res |= 1L << b
          cur = cur.child(want)
        } else if (cur.child(bit) != null) {
          cur = cur.child(bit)
        } else {
          return res
        }
        b -= 1
      }
      res
    }

    def dfs(u: Int, p: Int): Unit = {
      g(u).foreach { v =>
        if (v != p) {
          val xorv = query(sum(v))
          if (xorv > ans) ans = xorv
          dfs(v, u)
          insert(sum(v))
        }
      }
    }

    dfsSum(0, -1)
    dfs(0, -1)
    ans
  }
}
''')

w("2481_minimum_cuts_to_divide_a_circle", r'''
// LeetCode 2481 - Minimum Cuts to Divide a Circle
// https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

object Solution {
  def numberOfCuts(n: Int): Int = {
    if (n == 1) 0
    else if (n % 2 == 0) n / 2
    else n
  }
}
''')

w("2482_difference_between_ones_and_zeros_in_row_and_column", r'''
// LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

object Solution {
  def onesMinusZeros(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val row = new Array[Int](m)
    val col = new Array[Int](n)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        row(i) += grid(i)(j)
        col(j) += grid(i)(j)
        j += 1
      }
      i += 1
    }
    val ans = Array.ofDim[Int](m, n)
    i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        ans(i)(j) = row(i) + col(j) - (m - row(i)) - (n - col(j))
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("2483_minimum_penalty_for_a_shop", r'''
// LeetCode 2483 - Minimum Penalty for a Shop
// https://leetcode.com/problems/minimum-penalty-for-a-shop/

object Solution {
  def bestClosingTime(customers: String): Int = {
    val n = customers.length
    var penalty = 0
    var i = 0
    while (i < n) {
      if (customers.charAt(i) == 'Y') penalty += 1
      i += 1
    }
    var best = penalty
    var ans = 0
    i = 0
    while (i < n) {
      if (customers.charAt(i) == 'Y') penalty -= 1
      else penalty += 1
      if (penalty < best) {
        best = penalty
        ans = i + 1
      }
      i += 1
    }
    ans
  }
}
''')

w("2484_count_palindromic_subsequences", r'''
// LeetCode 2484 - Count Palindromic Subsequences
// https://leetcode.com/problems/count-palindromic-subsequences/

object Solution {
  def countPalindromes(s: String): Int = {
    val mod = 1000000007
    val n = s.length
    val pref = Array.ofDim[Int](n, 10, 10)
    val suf = Array.ofDim[Int](n, 10, 10)
    val cnt = new Array[Int](10)
    var i = 0
    while (i < n) {
      if (i > 0) {
        var a = 0
        while (a < 10) {
          var b = 0
          while (b < 10) {
            pref(i)(a)(b) = pref(i - 1)(a)(b)
            b += 1
          }
          a += 1
        }
      }
      val d = s.charAt(i) - '0'
      var a = 0
      while (a < 10) {
        pref(i)(a)(d) += cnt(a)
        a += 1
      }
      cnt(d) += 1
      i += 1
    }
    java.util.Arrays.fill(cnt, 0)
    i = n - 1
    while (i >= 0) {
      if (i + 1 < n) {
        var a = 0
        while (a < 10) {
          var b = 0
          while (b < 10) {
            suf(i)(a)(b) = suf(i + 1)(a)(b)
            b += 1
          }
          a += 1
        }
      }
      val d = s.charAt(i) - '0'
      var a = 0
      while (a < 10) {
        suf(i)(a)(d) += cnt(a)
        a += 1
      }
      cnt(d) += 1
      i -= 1
    }
    var ans = 0
    i = 2
    while (i < n - 2) {
      var a = 0
      while (a < 10) {
        var b = 0
        while (b < 10) {
          ans = ((ans + pref(i - 1)(a)(b).toLong * suf(i + 1)(a)(b)) % mod).toInt
          b += 1
        }
        a += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("2485_find_the_pivot_integer", r'''
// LeetCode 2485 - Find the Pivot Integer
// https://leetcode.com/problems/find-the-pivot-integer/

object Solution {
  def pivotInteger(n: Int): Int = {
    val total = n * (n + 1) / 2
    var sum = 0
    var x = 1
    while (x <= n) {
      sum += x
      if (sum == total - sum + x) return x
      x += 1
    }
    -1
  }
}
''')

w("2486_append_characters_to_string_to_make_subsequence", r'''
// LeetCode 2486 - Append Characters to String to Make Subsequence
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

object Solution {
  def appendCharacters(s: String, t: String): Int = {
    var j = 0
    var i = 0
    while (i < s.length && j < t.length) {
      if (s.charAt(i) == t.charAt(j)) j += 1
      i += 1
    }
    t.length - j
  }
}
''')

w("2487_remove_nodes_from_linked_list", r'''
// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def removeNodes(head0: ListNode): ListNode = {
    def rev(node0: ListNode): ListNode = {
      var prev: ListNode = null
      var node = node0
      while (node != null) {
        val nxt = node.next
        node.next = prev
        prev = node
        node = nxt
      }
      prev
    }
    var head = rev(head0)
    var mx = 0
    val dummy = new ListNode(0, head)
    var prev = dummy
    while (prev.next != null) {
      if (prev.next.x >= mx) {
        mx = prev.next.x
        prev = prev.next
      } else {
        prev.next = prev.next.next
      }
    }
    rev(dummy.next)
  }
}
''')
