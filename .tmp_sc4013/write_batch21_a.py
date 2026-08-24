#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("3822_design_order_management_system", r'''
// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design_order_management_system/

class OrderManagementSystem() {
  private case class Key(orderType: String, price: Int)
  private val orderTypeMap = scala.collection.mutable.Map.empty[Int, String]
  private val priceMap = scala.collection.mutable.Map.empty[Int, Int]
  private val t = scala.collection.mutable.Map.empty[Key, scala.collection.mutable.ArrayBuffer[Int]]

  def addOrder(orderId: Int, orderType: String, price: Int): Unit = {
    orderTypeMap(orderId) = orderType
    priceMap(orderId) = price
    val key = Key(orderType, price)
    t.getOrElseUpdate(key, scala.collection.mutable.ArrayBuffer.empty[Int]) += orderId
  }

  def modifyOrder(orderId: Int, newPrice: Int): Unit = {
    val orderType = orderTypeMap(orderId)
    val oldPrice = priceMap(orderId)
    priceMap(orderId) = newPrice
    val oldList = t(Key(orderType, oldPrice))
    var i = 0
    while (i < oldList.length) {
      if (oldList(i) == orderId) {
        oldList.remove(i)
        i = oldList.length
      } else i += 1
    }
    t.getOrElseUpdate(Key(orderType, newPrice), scala.collection.mutable.ArrayBuffer.empty[Int]) += orderId
  }

  def cancelOrder(orderId: Int): Unit = {
    val orderType = orderTypeMap(orderId)
    val price = priceMap(orderId)
    orderTypeMap.remove(orderId)
    priceMap.remove(orderId)
    val list = t(Key(orderType, price))
    var i = 0
    while (i < list.length) {
      if (list(i) == orderId) {
        list.remove(i)
        i = list.length
      } else i += 1
    }
  }

  def getOrdersAtPrice(orderType: String, price: Int): Array[Int] = {
    t.get(Key(orderType, price)) match {
      case None => Array.emptyIntArray
      case Some(list) => list.toArray
    }
  }
}
''')

w("3823_reverse_letters_then_special_characters_in_a_string", r'''
// LeetCode 3823 - Reverse Letters Then Special Characters In A String
// https://leetcode.com/problems/reverse_letters_then_special_characters_in_a_string/

object Solution {
  def reverseByType(s: String): String = {
    val a = scala.collection.mutable.ArrayBuffer.empty[Char]
    val b = scala.collection.mutable.ArrayBuffer.empty[Char]
    s.foreach { c =>
      if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) a += c
      else b += c
    }
    var j = a.length
    var k = b.length
    val arr = s.toCharArray
    var i = 0
    while (i < arr.length) {
      if ((arr(i) >= 'A' && arr(i) <= 'Z') || (arr(i) >= 'a' && arr(i) <= 'z')) {
        j -= 1
        arr(i) = a(j)
      } else {
        k -= 1
        arr(i) = b(k)
      }
      i += 1
    }
    new String(arr)
  }
}
''')

w("3824_minimum_k_to_reduce_array_within_limit", r'''
// LeetCode 3824 - Minimum K To Reduce Array Within Limit
// https://leetcode.com/problems/minimum_k_to_reduce_array_within_limit/

object Solution {
  def minimumK(nums: Array[Int]): Int = {
    var lo = 1
    var hi = 100000
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (check(nums, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def check(nums: Array[Int], k: Int): Boolean = {
    var t = 0L
    nums.foreach { x => t += (x + k - 1L) / k }
    t <= 1L * k * k
  }
}
''')

w("3825_longest_strictly_increasing_subsequence_with_non_zero_bitwise_and", r'''
// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non Zero Bitwise And
// https://leetcode.com/problems/longest_strictly_increasing_subsequence_with_non_zero_bitwise_and/

object Solution {
  private def bitLen(x0: Int): Int = {
    var x = x0
    if (x == 0) return 0
    var n = 0
    while (x > 0) { n += 1; x >>= 1 }
    n
  }

  private def lis(arr: scala.collection.mutable.ArrayBuffer[Int]): Int = {
    val g = scala.collection.mutable.ArrayBuffer.empty[Int]
    arr.foreach { x =>
      var lo = 0
      var hi = g.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (g(mid) < x) lo = mid + 1
        else hi = mid
      }
      if (lo == g.length) g += x
      else g(lo) = x
    }
    g.length
  }

  def longestSubsequence(nums: Array[Int]): Int = {
    var ans = 0
    var mx = 0
    nums.foreach { x => mx = math.max(mx, x) }
    val m = bitLen(mx)
    var i = 0
    while (i < m) {
      val arr = scala.collection.mutable.ArrayBuffer.empty[Int]
      nums.foreach { x => if (((x >> i) & 1) != 0) arr += x }
      ans = math.max(ans, lis(arr))
      i += 1
    }
    ans
  }
}
''')

w("3826_minimum_partition_score", r'''
// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum_partition_score/

object Solution {
  private var prefix: Array[Long] = _
  private var previous: Array[Long] = _
  private var current: Array[Long] = _
  private val INF = 1L << 62

  def minPartitionScore(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    prefix = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + nums(i)
      i += 1
    }
    previous = Array.fill(n + 1)(INF)
    previous(0) = 0
    var parts = 1
    while (parts <= k) {
      current = Array.fill(n + 1)(INF)
      compute(parts, n, parts - 1, n - 1)
      previous = current
      parts += 1
    }
    previous(n)
  }

  private def value(left: Int, right: Int): Long = {
    val sum = prefix(right) - prefix(left)
    sum * (sum + 1) / 2
  }

  private def compute(lo: Int, hi: Int, optLo: Int, optHi: Int): Unit = {
    if (lo > hi) return
    val mid = (lo + hi) / 2
    var bestIndex = -1
    val end = math.min(optHi, mid - 1)
    var split = optLo
    while (split <= end) {
      if (previous(split) != INF) {
        val candidate = previous(split) + value(split, mid)
        if (candidate < current(mid)) {
          current(mid) = candidate
          bestIndex = split
        }
      }
      split += 1
    }
    if (bestIndex == -1) bestIndex = optLo
    compute(lo, mid - 1, optLo, bestIndex)
    compute(mid + 1, hi, bestIndex, optHi)
  }
}
''')

w("3827_count_monobit_integers", r'''
// LeetCode 3827 - Count Monobit Integers
// https://leetcode.com/problems/count-monobit-integers/

object Solution {
  def countMonobit(n: Int): Int = {
    var ans = 1
    var i = 1
    var x = 1
    while (x <= n) {
      ans += 1
      x += (1 << i)
      i += 1
    }
    ans
  }
}
''')

w("3828_final_element_after_subarray_deletions", r'''
// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

object Solution {
  def finalElement(nums: Array[Int]): Int = math.max(nums(0), nums(nums.length - 1))
}
''')

w("3829_design_ride_sharing_system", r'''
// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design_ride_sharing_system/

class RideSharingSystem() {
  private var t = 0
  private val riders = scala.collection.mutable.TreeMap.empty[Int, Int]
  private val drivers = scala.collection.mutable.TreeMap.empty[Int, Int]
  private val d = scala.collection.mutable.Map.empty[Int, Int]

  def addRider(riderId: Int): Unit = {
    d(riderId) = t
    riders(t) = riderId
    t += 1
  }

  def addDriver(driverId: Int): Unit = {
    drivers(t) = driverId
    t += 1
  }

  def matchDriverWithRider(): Array[Int] = {
    if (riders.isEmpty || drivers.isEmpty) return Array(-1, -1)
    val dKey = drivers.firstKey
    val rKey = riders.firstKey
    val driverId = drivers(dKey)
    val riderId = riders(rKey)
    drivers.remove(dKey)
    riders.remove(rKey)
    Array(driverId, riderId)
  }

  def cancelRider(riderId: Int): Unit = {
    if (!d.contains(riderId)) return
    riders.remove(d(riderId))
  }
}
''')

w("3830_longest_alternating_subarray_after_removing_at_most_one_element", r'''
// LeetCode 3830 - Longest Alternating Subarray After Removing At Most One Element
// https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/

object Solution {
  def longestAlternating(nums: Array[Int]): Int = {
    val n = nums.length
    val l1 = Array.fill(n)(1)
    val l2 = Array.fill(n)(1)
    val r1 = Array.fill(n)(1)
    val r2 = Array.fill(n)(1)
    var ans = 0
    var i = 1
    while (i < n) {
      if (nums(i - 1) < nums(i)) l1(i) = l2(i - 1) + 1
      else if (nums(i - 1) > nums(i)) l2(i) = l1(i - 1) + 1
      ans = math.max(ans, math.max(l1(i), l2(i)))
      i += 1
    }
    i = n - 2
    while (i >= 0) {
      if (nums(i + 1) > nums(i)) r1(i) = r2(i + 1) + 1
      else if (nums(i + 1) < nums(i)) r2(i) = r1(i + 1) + 1
      i -= 1
    }
    i = 1
    while (i < n - 1) {
      if (nums(i - 1) < nums(i + 1)) ans = math.max(ans, l2(i - 1) + r2(i + 1))
      else if (nums(i - 1) > nums(i + 1)) ans = math.max(ans, l1(i - 1) + r1(i + 1))
      i += 1
    }
    ans
  }
}
''')

w("3831_median_of_a_binary_search_tree_level", r'''
// LeetCode 3831 - Median Of A Binary Search Tree Level
// https://leetcode.com/problems/median_of_a_binary_search_tree_level/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  private var nums: scala.collection.mutable.ArrayBuffer[Int] = _

  def levelMedian(root: TreeNode, level: Int): Int = {
    nums = scala.collection.mutable.ArrayBuffer.empty[Int]
    dfs(root, 0, level)
    if (nums.isEmpty) return -1
    nums(nums.length / 2)
  }

  private def dfs(node: TreeNode, i: Int, level: Int): Unit = {
    if (node == null) return
    dfs(node.left, i + 1, level)
    if (i == level) nums += node.value
    dfs(node.right, i + 1, level)
  }
}
''')

w("3833_count_dominant_indices", r'''
// LeetCode 3833 - Count Dominant Indices
// https://leetcode.com/problems/count-dominant-indices/

object Solution {
  def dominantIndices(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var suf = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      if (nums(i).toLong * (n - i - 1) > suf) ans += 1
      suf += nums(i)
      i -= 1
    }
    ans
  }
}
''')

w("3834_merge_adjacent_equal_elements", r'''
// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge_adjacent_equal_elements/

object Solution {
  def mergeAdjacent(nums: Array[Int]): Array[Long] = {
    val stk = scala.collection.mutable.ArrayBuffer.empty[Long]
    nums.foreach { x =>
      stk += x.toLong
      while (stk.length > 1 && stk(stk.length - 1) == stk(stk.length - 2)) {
        val a = stk.remove(stk.length - 1)
        val b = stk.remove(stk.length - 1)
        stk += a + b
      }
    }
    stk.toArray
  }
}
''')

w("3835_count_subarrays_with_cost_less_than_or_equal_to_k", r'''
// LeetCode 3835 - Count Subarrays With Cost Less Than Or Equal To K
// https://leetcode.com/problems/count_subarrays_with_cost_less_than_or_equal_to_k/

object Solution {
  def countSubarrays(nums: Array[Int], k: Long): Long = {
    var ans = 0L
    val q1 = scala.collection.mutable.ArrayDeque.empty[Int]
    val q2 = scala.collection.mutable.ArrayDeque.empty[Int]
    var l = 0
    var r = 0
    while (r < nums.length) {
      val x = nums(r)
      while (q1.nonEmpty && nums(q1.last) <= x) q1.removeLast()
      while (q2.nonEmpty && nums(q2.last) >= x) q2.removeLast()
      q1.append(r)
      q2.append(r)
      while (l < r && (nums(q1.head).toLong - nums(q2.head)) * (r - l + 1) > k) {
        l += 1
        if (q1.head < l) q1.removeHead()
        if (q2.head < l) q2.removeHead()
      }
      ans += r - l + 1
      r += 1
    }
    ans
  }
}
''')

w("3836_maximum_score_using_exactly_k_pairs", r'''
// LeetCode 3836 - Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum_score_using_exactly_k_pairs/

object Solution {
  def maxScore(nums1: Array[Int], nums2: Array[Int], K: Int): Long = {
    val n = nums1.length
    val m = nums2.length
    val NEG = Long.MinValue / 4
    val f = Array.ofDim[Long](n + 1, m + 1, K + 1)
    var i = 0
    while (i <= n) {
      var j = 0
      while (j <= m) {
        java.util.Arrays.fill(f(i)(j), NEG)
        j += 1
      }
      i += 1
    }
    f(0)(0)(0) = 0
    i = 0
    while (i <= n) {
      var j = 0
      while (j <= m) {
        var k = 0
        while (k <= K) {
          if (i > 0) f(i)(j)(k) = math.max(f(i)(j)(k), f(i - 1)(j)(k))
          if (j > 0) f(i)(j)(k) = math.max(f(i)(j)(k), f(i)(j - 1)(k))
          if (i > 0 && j > 0 && k > 0) {
            f(i)(j)(k) = math.max(f(i)(j)(k), f(i - 1)(j - 1)(k - 1) + nums1(i - 1).toLong * nums2(j - 1))
          }
          k += 1
        }
        j += 1
      }
      i += 1
    }
    f(n)(m)(K)
  }
}
''')

w("3837_delayed_count_of_equal_elements", r'''
// LeetCode 3837 - Delayed Count Of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

object Solution {
  def delayedCount(nums: Array[Int], k: Int): Array[Int] = {
    val n = nums.length
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    val ans = new Array[Int](n)
    var i = n - k - 2
    while (i >= 0) {
      val key = nums(i + k + 1)
      cnt(key) = cnt.getOrElse(key, 0) + 1
      ans(i) = cnt.getOrElse(nums(i), 0)
      i -= 1
    }
    ans
  }
}
''')

w("3838_weighted_word_mapping", r'''
// LeetCode 3838 - Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/

object Solution {
  def mapWordWeights(words: Array[String], weights: Array[Int]): String = {
    val ans = new StringBuilder
    words.foreach { w =>
      var s = 0
      w.foreach { c => s = (s + weights(c - 'a')) % 26 }
      ans.append(('a' + (25 - s)).toChar)
    }
    ans.toString
  }
}
''')

w("3839_number_of_prefix_connected_groups", r'''
// LeetCode 3839 - Number Of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

object Solution {
  def prefixConnected(words: Array[String], k: Int): Int = {
    val cnt = scala.collection.mutable.Map.empty[String, Int]
    words.foreach { w =>
      if (w.length >= k) {
        val p = w.substring(0, k)
        cnt(p) = cnt.getOrElse(p, 0) + 1
      }
    }
    var ans = 0
    cnt.values.foreach { v => if (v > 1) ans += 1 }
    ans
  }
}
''')

w("3840_house_robber_v", r'''
// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

object Solution {
  def rob(nums: Array[Int], colors: Array[Int]): Long = {
    val n = nums.length
    var f = 0L
    var g = nums(0).toLong
    var i = 1
    while (i < n) {
      if (colors(i - 1) == colors(i)) {
        val nf = math.max(f, g)
        g = f + nums(i)
        f = nf
      } else {
        val nf = math.max(f, g)
        g = nf + nums(i)
        f = nf
      }
      i += 1
    }
    math.max(f, g)
  }
}
''')

w("3841_palindromic_path_queries_in_a_tree", r'''
// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

object Solution {
  private var bit: Array[Int] = _
  private var n: Int = _
  private var parent: Array[Int] = _
  private var depth: Array[Int] = _
  private var size: Array[Int] = _
  private var heavy: Array[Int] = _
  private var head: Array[Int] = _
  private var position: Array[Int] = _
  private var graph: Array[scala.collection.mutable.ArrayBuffer[Int]] = _

  def palindromicPathQueries(n: Int, edges: Array[Array[Int]], s: String, queries: Array[String]): Array[Boolean] = {
    this.n = n
    graph = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { edge =>
      graph(edge(0)) += edge(1)
      graph(edge(1)) += edge(0)
    }
    parent = Array.fill(n)(-2)
    depth = new Array[Int](n)
    parent(0) = -1
    val order = scala.collection.mutable.ArrayBuffer[Int](0)
    var i = 0
    while (i < order.length) {
      val u = order(i)
      graph(u).foreach { v =>
        if (parent(v) == -2) {
          parent(v) = u
          depth(v) = depth(u) + 1
          order += v
        }
      }
      i += 1
    }
    size = new Array[Int](n)
    heavy = Array.fill(n)(-1)
    i = n - 1
    while (i >= 0) {
      val u = order(i)
      size(u) = 1
      graph(u).foreach { v =>
        if (parent(v) == u) {
          size(u) += size(v)
          if (heavy(u) == -1 || size(v) > size(heavy(u))) heavy(u) = v
        }
      }
      i -= 1
    }
    head = new Array[Int](n)
    position = new Array[Int](n)
    val stack = scala.collection.mutable.ArrayBuffer[Array[Int]](Array(0, 0))
    var nextPosition = 0
    while (stack.nonEmpty) {
      val chain = stack.remove(stack.length - 1)
      var u = chain(0)
      while (u != -1) {
        head(u) = chain(1)
        position(u) = nextPosition
        nextPosition += 1
        graph(u).foreach { v =>
          if (parent(v) == u && v != heavy(u)) stack += Array(v, v)
        }
        u = heavy(u)
      }
    }
    bit = new Array[Int](n + 1)
    val current = s.toCharArray
    var node = 0
    while (node < n) {
      update(position(node), 1 << (current(node) - 'a'))
      node += 1
    }
    val answer = scala.collection.mutable.ArrayBuffer.empty[Boolean]
    queries.foreach { query =>
      val parts = query.split(" ")
      val op = parts(0)
      val nd = parts(1).toInt
      if (op == "update") {
        val newCharacter = parts(2).charAt(0)
        val delta = (1 << (current(nd) - 'a')) ^ (1 << (newCharacter - 'a'))
        update(position(nd), delta)
        current(nd) = newCharacter
      } else {
        val other = parts(2).toInt
        val mask = pathMask(nd, other)
        answer += ((mask & (mask - 1)) == 0)
      }
    }
    answer.toArray
  }

  private def update(index0: Int, value: Int): Unit = {
    var index = index0 + 1
    while (index <= n) {
      bit(index) ^= value
      index += index & -index
    }
  }

  private def prefix(index0: Int): Int = {
    var result = 0
    var index = index0
    while (index > 0) {
      result ^= bit(index)
      index -= index & -index
    }
    result
  }

  private def pathMask(u0: Int, v0: Int): Int = {
    var u = u0
    var v = v0
    var result = 0
    while (head(u) != head(v)) {
      if (depth(head(u)) < depth(head(v))) {
        val tmp = u; u = v; v = tmp
      }
      result ^= prefix(position(u) + 1) ^ prefix(position(head(u)))
      u = parent(head(u))
    }
    if (position(u) > position(v)) {
      val tmp = u; u = v; v = tmp
    }
    result ^ prefix(position(v) + 1) ^ prefix(position(u))
  }
}
''')

w("3842_toggle_light_bulbs", r'''
// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

object Solution {
  def toggleLightBulbs(bulbs: Array[Int]): Array[Int] = {
    val st = new Array[Int](101)
    bulbs.foreach { x => st(x) ^= 1 }
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < 101) {
      if (st(i) == 1) ans += i
      i += 1
    }
    ans.toArray
  }
}
''')

w("3843_first_element_with_unique_frequency", r'''
// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

object Solution {
  def firstUniqueFreq(nums: Array[Int]): Int = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    nums.foreach { x => cnt(x) = cnt.getOrElse(x, 0) + 1 }
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    cnt.values.foreach { v => freq(v) = freq.getOrElse(v, 0) + 1 }
    nums.foreach { x =>
      if (freq(cnt(x)) == 1) return x
    }
    -1
  }
}
''')

w("3844_longest_almost_palindromic_substring", r'''
// LeetCode 3844 - Longest Almost Palindromic Substring
// https://leetcode.com/problems/longest-almost-palindromic-substring/

object Solution {
  def almostPalindromic(s: String): Int = {
    val n = s.length
    var ans = 0
    var i = 0
    while (i < n) {
      ans = math.max(ans, math.max(expand(s, i, i), expand(s, i, i + 1)))
      i += 1
    }
    ans
  }

  private def expand(s: String, l0: Int, r0: Int): Int = {
    val n = s.length
    var l = l0
    var r = r0
    while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) { l -= 1; r += 1 }
    var l1 = l - 1
    var r1 = r
    var l2 = l
    var r2 = r + 1
    while (l1 >= 0 && r1 < n && s.charAt(l1) == s.charAt(r1)) { l1 -= 1; r1 += 1 }
    while (l2 >= 0 && r2 < n && s.charAt(l2) == s.charAt(r2)) { l2 -= 1; r2 += 1 }
    math.min(n, math.max(r1 - l1 - 1, r2 - l2 - 1))
  }
}
''')

w("3845_maximum_subarray_xor_with_bounded_range", r'''
// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

object Solution {
  private class Node {
    val next = new Array[Int](2)
    var count = 0
  }

  private var nodes: scala.collection.mutable.ArrayBuffer[Node] = _

  private def add(x: Int, delta: Int): Unit = {
    var u = 0
    nodes(u).count += delta
    var b = 15
    while (b >= 0) {
      val bit = (x >> b) & 1
      if (nodes(u).next(bit) == 0) {
        nodes(u).next(bit) = nodes.length
        nodes += new Node
      }
      u = nodes(u).next(bit)
      nodes(u).count += delta
      b -= 1
    }
  }

  private def query(x: Int): Int = {
    var u = 0
    var res = 0
    var b = 15
    while (b >= 0) {
      val bit = (x >> b) & 1
      val want = bit ^ 1
      val v = nodes(u).next(want)
      if (v != 0 && nodes(v).count > 0) {
        res |= 1 << b
        u = v
      } else {
        u = nodes(u).next(bit)
      }
      b -= 1
    }
    res
  }

  def maxSubarrayXor(nums: Array[Int], k: Int): Int = {
    nodes = scala.collection.mutable.ArrayBuffer[Node](new Node)
    val n = nums.length
    val pref = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) ^ nums(i)
      i += 1
    }
    val maxQ = scala.collection.mutable.ArrayBuffer.empty[Int]
    val minQ = scala.collection.mutable.ArrayBuffer.empty[Int]
    var left = 0
    var trieLeft = 0
    var ans = 0
    var r = 0
    while (r < n) {
      val x = nums(r)
      while (maxQ.nonEmpty && nums(maxQ.last) <= x) maxQ.remove(maxQ.length - 1)
      maxQ += r
      while (minQ.nonEmpty && nums(minQ.last) >= x) minQ.remove(minQ.length - 1)
      minQ += r
      while (nums(maxQ(0)) - nums(minQ(0)) > k) {
        if (maxQ(0) == left) maxQ.remove(0)
        if (minQ(0) == left) minQ.remove(0)
        left += 1
      }
      add(pref(r), 1)
      while (trieLeft < left) {
        add(pref(trieLeft), -1)
        trieLeft += 1
      }
      val cur = query(pref(r + 1))
      if (cur > ans) ans = cur
      r += 1
    }
    ans
  }
}
''')

w("3846_total_distance_to_type_a_string_using_one_finger", r'''
// LeetCode 3846 - Total Distance To Type A String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

object Solution {
  private val POS: Map[Char, Array[Int]] = {
    val pos = scala.collection.mutable.Map.empty[Char, Array[Int]]
    val keys = Array("qwertyuiop", "asdfghjkl", "zxcvbnm")
    var i = 0
    while (i < 3) {
      var j = 0
      while (j < keys(i).length) {
        pos(keys(i).charAt(j)) = Array(i, j)
        j += 1
      }
      i += 1
    }
    pos.toMap
  }

  def totalDistance(s: String): Int = {
    var pre = 'a'
    var ans = 0
    s.foreach { cur =>
      val p1 = POS(pre)
      val p2 = POS(cur)
      ans += math.abs(p1(0) - p2(0)) + math.abs(p1(1) - p2(1))
      pre = cur
    }
    ans
  }
}
''')

print("batch A done")
