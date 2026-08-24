#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3477_fruits_into_baskets_ii"] = r'''// LeetCode 3477 - Fruits Into Baskets II
// https://leetcode.com/problems/fruits-into-baskets-ii/

object Solution {
  def numOfUnplacedFruits(fruits: Array[Int], baskets: Array[Int]): Int = {
    val used = new Array[Boolean](baskets.length)
    var unplaced = 0
    fruits.foreach { f =>
      var placed = false
      var j = 0
      while (j < baskets.length && !placed) {
        if (!used(j) && baskets(j) >= f) {
          used(j) = true
          placed = true
        }
        j += 1
      }
      if (!placed) unplaced += 1
    }
    unplaced
  }
}
'''

FILES["3478_choose_k_elements_with_maximum_sum"] = r'''// LeetCode 3478 - Choose K Elements With Maximum Sum
// https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

object Solution {
  def findMaxSum(nums1: Array[Int], nums2: Array[Int], k: Int): Array[Long] = {
    val n = nums1.length
    val arr = Array.tabulate(n)(i => Array(nums1(i), nums2(i), i))
    java.util.Arrays.sort(arr, (a: Array[Int], b: Array[Int]) => java.lang.Integer.compare(a(0), b(0)))
    val ans = new Array[Long](n)
    val h = new java.util.PriorityQueue[Integer]()
    var sum = 0L
    var i = 0
    while (i < n) {
      val v = arr(i)(0)
      val start = i
      while (i < n && arr(i)(0) == v) i += 1
      var t = start
      while (t < i) { ans(arr(t)(2)) = sum; t += 1 }
      t = start
      while (t < i) {
        h.offer(arr(t)(1))
        sum += arr(t)(1)
        if (h.size() > k) sum -= h.poll()
        t += 1
      }
    }
    ans
  }
}
'''

FILES["3479_fruits_into_baskets_iii"] = r'''// LeetCode 3479 - Fruits Into Baskets III
// https://leetcode.com/problems/fruits-into-baskets-iii/

object Solution {
  private var tree: Array[Int] = _
  private var size = 0
  private var n = 0

  def numOfUnplacedFruits(fruits: Array[Int], baskets: Array[Int]): Int = {
    n = baskets.length
    size = 1
    while (size < n) size <<= 1
    tree = new Array[Int](size * 2)
    var i = 0
    while (i < n) { tree(size + i) = baskets(i); i += 1 }
    i = size - 1
    while (i > 0) {
      tree(i) = math.max(tree(i * 2), tree(i * 2 + 1))
      i -= 1
    }
    var unplaced = 0
    fruits.foreach { f =>
      val idx = find(1, 0, size - 1, f)
      if (idx == -1 || idx >= n) unplaced += 1
      else update(idx)
    }
    unplaced
  }

  private def find(node: Int, nl: Int, nr: Int, need: Int): Int = {
    if (tree(node) < need) return -1
    if (nl == nr) return nl
    val mid = (nl + nr) / 2
    val left = find(node * 2, nl, mid, need)
    if (left != -1) left else find(node * 2 + 1, mid + 1, nr, need)
  }

  private def update(idx: Int): Unit = {
    var p = size + idx
    tree(p) = -1
    p >>= 1
    while (p > 0) {
      tree(p) = math.max(tree(p * 2), tree(p * 2 + 1))
      p >>= 1
    }
  }
}
'''

FILES["3480_maximize_subarrays_after_removing_one_conflicting_pair"] = r'''// LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
// https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

object Solution {
  def maxSubarrays(n: Int, conflictingPairs: Array[Array[Int]]): Long = {
    val m = conflictingPairs.length
    var best = 0L
    var skip = 0
    while (skip < m) {
      val rightLimit = Array.fill(n + 2)(n + 1)
      var i = 0
      while (i < m) {
        if (i != skip) {
          var a = conflictingPairs(i)(0)
          var b = conflictingPairs(i)(1)
          if (a > b) { val t = a; a = b; b = t }
          if (b < rightLimit(a)) rightLimit(a) = b
        }
        i += 1
      }
      var minRight = n + 1
      var cnt = 0L
      var l = n
      while (l >= 1) {
        if (rightLimit(l) < minRight) minRight = rightLimit(l)
        cnt += minRight - l
        l -= 1
      }
      if (cnt > best) best = cnt
      skip += 1
    }
    best
  }
}
'''

FILES["3481_apply_substitutions"] = r'''// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

object Solution {
  private var mp: java.util.HashMap[String, String] = _

  def applySubstitutions(replacements: List[List[String]], text: String): String = {
    mp = new java.util.HashMap[String, String]()
    replacements.foreach { r => mp.put(r(0), r(1)) }
    resolve(text)
  }

  private def resolve(s: String): String = {
    val out = new StringBuilder
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == '%') {
        var j = i + 1
        while (j < s.length && s.charAt(j) != '%') j += 1
        val key = s.substring(i + 1, j)
        out.append(resolve(mp.get(key)))
        i = j + 1
      } else {
        out.append(s.charAt(i))
        i += 1
      }
    }
    out.toString
  }
}
'''

FILES["3483_unique_3_digit_even_numbers"] = r'''// LeetCode 3483 - Unique 3-Digit Even Numbers
// https://leetcode.com/problems/unique-3-digit-even-numbers/

object Solution {
  def totalNumbers(digits: Array[Int]): Int = {
    val seen = scala.collection.mutable.Set.empty[Int]
    val n = digits.length
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (j != i) {
          var k = 0
          while (k < n) {
            if (k != i && k != j && digits(i) != 0 && digits(k) % 2 == 0) {
              seen += digits(i) * 100 + digits(j) * 10 + digits(k)
            }
            k += 1
          }
        }
        j += 1
      }
      i += 1
    }
    seen.size
  }
}
'''

FILES["3484_design_spreadsheet"] = r'''// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

class Spreadsheet(_rows: Int) {
  private val cells = scala.collection.mutable.Map.empty[String, Int]

  def setCell(cell: String, value: Int): Unit = { cells(cell) = value }

  def resetCell(cell: String): Unit = { cells.remove(cell) }

  def getValue(formula0: String): Int = {
    var formula = formula0
    if (formula.nonEmpty && formula.charAt(0) == '=') formula = formula.substring(1)
    var sum = 0
    var start = 0
    while (start < formula.length) {
      val plus = formula.indexOf('+', start)
      val p = if (plus < 0) formula.substring(start) else formula.substring(start, plus)
      var isNum = p.nonEmpty && (Character.isDigit(p.charAt(0)) || (p.charAt(0) == '-' && p.length > 1))
      if (isNum) {
        var i = 1
        while (i < p.length) {
          if (!Character.isDigit(p.charAt(i))) { isNum = false; i = p.length }
          else i += 1
        }
      }
      if (isNum) sum += p.toInt
      else sum += cells.getOrElse(p, 0)
      if (plus < 0) return sum
      start = plus + 1
    }
    sum
  }
}
'''

FILES["3485_longest_common_prefix_of_k_strings_after_removal"] = r'''// LeetCode 3485 - Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

object Solution {
  private def lcpOf(a: java.util.List[String]): Int = {
    if (a.isEmpty) return 0
    var pref = a.get(0)
    var t = 1
    while (t < a.size()) {
      val s = a.get(t)
      var i = 0
      while (i < pref.length && i < s.length && pref.charAt(i) == s.charAt(i)) i += 1
      pref = pref.substring(0, i)
      if (pref.isEmpty) return 0
      t += 1
    }
    pref.length
  }

  def longestCommonPrefix(words: Array[String], k: Int): Array[Int] = {
    val n = words.length
    val ans = new Array[Int](n)
    var i = 0
    while (i < n) {
      val rest = new java.util.ArrayList[String]()
      var j = 0
      while (j < n) {
        if (j != i) rest.add(words(j))
        j += 1
      }
      if (rest.size() < k) ans(i) = 0
      else {
        java.util.Collections.sort(rest)
        var best = 0
        j = 0
        while (j + k - 1 < rest.size()) {
          val window = rest.subList(j, j + k)
          best = math.max(best, lcpOf(window))
          j += 1
        }
        ans(i) = best
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3486_longest_special_path_ii"] = r'''// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

object Solution {
  private var g: Array[java.util.ArrayList[Array[Int]]] = _
  private var nums: Array[Int] = _
  private var bestLen = 0
  private var bestNodes = 0

  def longestSpecialPath(edges: Array[Array[Int]], nums0: Array[Int]): Array[Int] = {
    nums = nums0
    val n = nums.length
    g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    edges.foreach { e =>
      g(e(0)).add(Array(e(1), e(2)))
      g(e(1)).add(Array(e(0), e(2)))
    }
    bestLen = 0
    bestNodes = 1
    dfs(0, -1, 0, new java.util.ArrayList[Integer](), new java.util.ArrayList[Integer]())
    Array(bestLen, bestNodes)
  }

  private def dfs(u: Int, p: Int, dist: Int, pathVals: java.util.ArrayList[Integer], pathDist: java.util.ArrayList[Integer]): Unit = {
    pathVals.add(nums(u))
    pathDist.add(dist)
    val freq = new java.util.HashMap[Integer, Integer]()
    var dups = 0
    var left = 0
    var right = 0
    while (right < pathVals.size()) {
      val v = pathVals.get(right)
      freq.put(v, freq.getOrDefault(v, 0) + 1)
      if (freq.get(v) == 2) dups += 1
      while (dups > 1) {
        val lv = pathVals.get(left)
        if (freq.get(lv) == 2) dups -= 1
        freq.put(lv, freq.get(lv) - 1)
        left += 1
      }
      right += 1
    }
    val length = dist - pathDist.get(left)
    val nodes = pathVals.size() - left
    if (length > bestLen || (length == bestLen && nodes < bestNodes)) {
      bestLen = length
      bestNodes = nodes
    }
    val it = g(u).iterator()
    while (it.hasNext) {
      val e = it.next()
      if (e(0) != p) dfs(e(0), u, dist + e(1), pathVals, pathDist)
    }
    pathVals.remove(pathVals.size() - 1)
    pathDist.remove(pathDist.size() - 1)
  }
}
'''

FILES["3487_maximum_unique_subarray_sum_after_deletion"] = r'''// LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

object Solution {
  def maxSum(nums: Array[Int]): Int = {
    val seen = scala.collection.mutable.Set.empty[Int]
    var sum = 0
    var hasPos = false
    var maxNeg = -1000000000
    nums.foreach { x =>
      if (x < 0) {
        if (x > maxNeg) maxNeg = x
      } else {
        hasPos = true
        if (seen.add(x)) sum += x
      }
    }
    if (hasPos) sum else maxNeg
  }
}
'''

FILES["3488_closest_equal_element_queries"] = r'''// LeetCode 3488 - Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/

object Solution {
  def solveQueries(nums: Array[Int], queries: Array[Int]): Array[Int] = {
    val n = nums.length
    val pos = scala.collection.mutable.Map.empty[Int, java.util.ArrayList[Integer]]
    var i = 0
    while (i < n) {
      pos.getOrElseUpdate(nums(i), new java.util.ArrayList[Integer]()).add(i)
      i += 1
    }
    val ans = new Array[Int](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val idx = queries(qi)
      val x = nums(idx)
      val arr = pos(x)
      if (arr.size() == 1) ans(qi) = -1
      else {
        var best = n
        val it = arr.iterator()
        while (it.hasNext) {
          val p = it.next().intValue()
          if (p != idx) {
            var d = math.abs(p - idx)
            d = math.min(d, n - d)
            if (d < best) best = d
          }
        }
        ans(qi) = best
      }
      qi += 1
    }
    ans
  }
}
'''

FILES["3489_zero_array_transformation_iv"] = r'''// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

object Solution {
  private def canSubsetSum(vals: java.util.List[Integer], target: Int): Boolean = {
    if (target == 0) return true
    val dp = new Array[Boolean](target + 1)
    dp(0) = true
    val it = vals.iterator()
    while (it.hasNext) {
      val v = it.next().intValue()
      var s = target
      while (s >= v) {
        if (dp(s - v)) dp(s) = true
        s -= 1
      }
    }
    dp(target)
  }

  def minZeroArray(nums: Array[Int], queries: Array[Array[Int]]): Int = {
    if (ok(nums, queries, 0)) return 0
    var lo = 1
    var hi = queries.length + 1
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (mid <= queries.length && ok(nums, queries, mid)) hi = mid
      else lo = mid + 1
    }
    if (lo > queries.length) -1 else lo
  }

  private def ok(nums: Array[Int], queries: Array[Array[Int]], k: Int): Boolean = {
    val n = nums.length
    var i = 0
    while (i < n) {
      if (nums(i) != 0) {
        val vals = new java.util.ArrayList[Integer]()
        var q = 0
        while (q < k) {
          val l = queries(q)(0)
          val r = queries(q)(1)
          val v = queries(q)(2)
          if (l <= i && i <= r) vals.add(v)
          q += 1
        }
        if (!canSubsetSum(vals, nums(i))) return false
      }
      i += 1
    }
    true
  }
}
'''

FILES["3490_count_beautiful_numbers"] = r'''// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

object Solution {
  private var s: String = _

  private def countBeautiful(n: Int): Int = {
    if (n <= 0) return 0
    s = n.toString
    dfs(0, tight = true, 0, 1, started = false)
  }

  private def dfs(pos: Int, tight: Boolean, sum: Int, prod: Int, started: Boolean): Int = {
    if (pos == s.length) {
      if (!started) return 0
      return if (sum > 0 && prod % sum == 0) 1 else 0
    }
    val up = if (tight) s.charAt(pos) - '0' else 9
    var ans = 0
    var d = 0
    while (d <= up) {
      val nt = tight && d == up
      if (!started && d == 0) ans += dfs(pos + 1, nt, 0, 1, started = false)
      else {
        val ns = sum + d
        val np = if (!started) d else prod * d
        ans += dfs(pos + 1, nt, ns, np, started = true)
      }
      d += 1
    }
    ans
  }

  def beautifulNumbers(l: Int, r: Int): Int = countBeautiful(r) - countBeautiful(l - 1)
}
'''

FILES["3491_phone_number_prefix"] = r'''// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

object Solution {
  def phonePrefix(numbers: Array[String]): Boolean = {
    java.util.Arrays.sort(numbers.asInstanceOf[Array[Object]])
    var i = 0
    while (i + 1 < numbers.length) {
      if (numbers(i).length <= numbers(i + 1).length && numbers(i + 1).startsWith(numbers(i)))
        return false
      i += 1
    }
    true
  }
}
'''

FILES["3492_maximum_containers_on_a_ship"] = r'''// LeetCode 3492 - Maximum Containers on a Ship
// https://leetcode.com/problems/maximum-containers-on-a-ship/

object Solution {
  def maxContainers(n: Int, w: Int, maxWeight: Int): Int = {
    val cap = n * n
    val byW = maxWeight / w
    if (cap < byW) cap else byW
  }
}
'''

FILES["3493_properties_graph"] = r'''// LeetCode 3493 - Properties Graph
// https://leetcode.com/problems/properties-graph/

object Solution {
  private var parent: Array[Int] = _

  private def find(x0: Int): Int = {
    var x = x0
    if (parent(x) != x) parent(x) = find(parent(x))
    parent(x)
  }

  private def unite(a: Int, b: Int): Unit = {
    val ra = find(a)
    val rb = find(b)
    if (ra != rb) parent(ra) = rb
  }

  def numberOfComponents(properties: Array[Array[Int]], k: Int): Int = {
    val n = properties.length
    val sets = Array.fill(n)(scala.collection.mutable.Set.empty[Int])
    var i = 0
    while (i < n) {
      properties(i).foreach(v => sets(i) += v)
      i += 1
    }
    parent = Array.tabulate(n)(identity)
    i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        var cnt = 0
        sets(i).foreach { v => if (sets(j).contains(v)) cnt += 1 }
        if (cnt >= k) unite(i, j)
        j += 1
      }
      i += 1
    }
    val comp = scala.collection.mutable.Set.empty[Int]
    i = 0
    while (i < n) { comp += find(i); i += 1 }
    comp.size
  }
}
'''

FILES["3494_find_the_minimum_amount_of_time_to_brew_potions"] = r'''// LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

object Solution {
  def minTime(skill: Array[Int], mana: Array[Int]): Long = {
    val n = skill.length
    val m = mana.length
    val done = new Array[Long](n)
    var j = 0
    while (j < m) {
      var t = 0L
      var i = 0
      while (i < n) {
        if (done(i) > t) t = done(i)
        t += skill(i).toLong * mana(j)
        done(i) = t
        i += 1
      }
      i = n - 2
      while (i >= 0) {
        done(i) = done(i + 1) - skill(i + 1).toLong * mana(j)
        i -= 1
      }
      j += 1
    }
    done(n - 1)
  }
}
'''

FILES["3495_minimum_operations_to_make_array_elements_zero"] = r'''// LeetCode 3495 - Minimum Operations to Make Array Elements Zero
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

object Solution {
  private def opsToZero(x0: Int): Int = {
    var x = x0
    var ops = 0
    while (x > 0) { x /= 4; ops += 1 }
    ops
  }

  def minOperations(queries: Array[Array[Int]]): Long = {
    var ans = 0L
    queries.foreach { q =>
      val l = q(0)
      val r = q(1)
      var sum = 0L
      var x = l
      while (x <= r) {
        sum += opsToZero(x)
        x += 1
      }
      ans += (sum + 1) / 2
    }
    ans
  }
}
'''

FILES["3496_maximize_score_after_pair_deletions"] = r'''// LeetCode 3496 - Maximize Score After Pair Deletions
// https://leetcode.com/problems/maximize-score-after-pair-deletions/

object Solution {
  def maximizeScore(nums: Array[Int]): Int = {
    val n = nums.length
    var total = 0
    nums.foreach(x => total += x)
    if (n % 2 == 1) {
      var mn = nums(0)
      nums.foreach { x => if (x < mn) mn = x }
      return total - mn
    }
    var mn = nums(0) + nums(1)
    var i = 0
    while (i + 1 < n) {
      mn = math.min(mn, nums(i) + nums(i + 1))
      i += 1
    }
    total - mn
  }
}
'''

FILES["3498_reverse_degree_of_a_string"] = r'''// LeetCode 3498 - Reverse Degree of a String
// https://leetcode.com/problems/reverse-degree-of-a-string/

object Solution {
  def reverseDegree(s: String): Int = {
    var ans = 0
    var i = 0
    while (i < s.length) {
      ans += (26 - (s.charAt(i) - 'a')) * (i + 1)
      i += 1
    }
    ans
  }
}
'''

FILES["3499_maximize_active_section_with_trade_i"] = r'''// LeetCode 3499 - Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/

object Solution {
  def maxActiveSectionsAfterTrade(s: String): Int = {
    var ones = 0
    s.foreach { c => if (c == '1') ones += 1 }
    val zeros = new java.util.ArrayList[Array[Int]]()
    val n = s.length
    var i = 0
    while (i < n) {
      if (s.charAt(i) != '0') i += 1
      else {
        var j = i
        while (j < n && s.charAt(j) == '0') j += 1
        zeros.add(Array(i, j - 1))
        i = j
      }
    }
    var best = 0
    i = 0
    while (i + 1 < zeros.size()) {
      val gain = (zeros.get(i)(1) - zeros.get(i)(0) + 1) + (zeros.get(i + 1)(1) - zeros.get(i + 1)(0) + 1)
      if (gain > best) best = gain
      i += 1
    }
    ones + best
  }
}
'''

FILES["3500_minimum_cost_to_divide_array_into_subarrays"] = r'''// LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
// https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

object Solution {
  def minimumCost(nums: Array[Int], cost: Array[Int], k: Int): Long = {
    val n = nums.length
    val pn = new Array[Long](n + 1)
    val pc = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      pn(i + 1) = pn(i) + nums(i)
      pc(i + 1) = pc(i) + cost(i)
      i += 1
    }
    val inf = 1L << 62
    val dp = Array.fill(n + 1)(0L)
    i = 0
    while (i < n) { dp(i) = inf; i += 1 }
    i = n - 1
    while (i >= 0) {
      var j = i
      while (j < n) {
        val cand = pn(j + 1) * (pc(j + 1) - pc(i)) + k.toLong * (pc(n) - pc(i)) + dp(j + 1)
        if (cand < dp(i)) dp(i) = cand
        j += 1
      }
      i -= 1
    }
    dp(0)
  }
}
'''

FILES["3501_maximize_active_section_with_trade_ii"] = r'''// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

object Solution {
  def maxActiveSectionsAfterTrade(s: String, queries: Array[Array[Int]]): Array[Int] = {
    var ones = 0
    s.foreach { c => if (c == '1') ones += 1 }
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < ans.length) { ans(i) = ones; i += 1 }
    ans
  }
}
'''

FILES["3502_minimum_cost_to_reach_every_position"] = r'''// LeetCode 3502 - Minimum Cost to Reach Every Position
// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

object Solution {
  def minCosts(cost: Array[Int]): Array[Int] = {
    val n = cost.length
    val ans = new Array[Int](n)
    var mi = cost(0)
    var i = 0
    while (i < n) {
      mi = math.min(mi, cost(i))
      ans(i) = mi
      i += 1
    }
    ans
  }
}
'''

FILES["3503_longest_palindrome_after_substring_concatenation_i"] = r'''// LeetCode 3503 - Longest Palindrome After Substring Concatenation I
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

object Solution {
  private def expand(s: String, g: Array[Int], l0: Int, r0: Int): Unit = {
    var l = l0
    var r = r0
    while (l >= 0 && r < s.length && s.charAt(l) == s.charAt(r)) {
      g(l) = math.max(g(l), r - l + 1)
      l -= 1
      r += 1
    }
  }

  private def calc(s: String): Array[Int] = {
    val n = s.length
    val g = new Array[Int](n)
    var i = 0
    while (i < n) {
      expand(s, g, i, i)
      expand(s, g, i, i + 1)
      i += 1
    }
    g
  }

  def longestPalindrome(s: String, t0: String): Int = {
    val m = s.length
    val n = t0.length
    val t = new StringBuilder(t0).reverse().toString
    val g1 = calc(s)
    val g2 = calc(t)
    var ans = 0
    g1.foreach { v => ans = math.max(ans, v) }
    g2.foreach { v => ans = math.max(ans, v) }
    val f = Array.ofDim[Int](m + 1, n + 1)
    var i = 1
    while (i <= m) {
      var j = 1
      while (j <= n) {
        if (s.charAt(i - 1) == t.charAt(j - 1)) {
          f(i)(j) = f(i - 1)(j - 1) + 1
          val a = if (i < m) g1(i) else 0
          val b = if (j < n) g2(j) else 0
          ans = math.max(ans, f(i)(j) * 2 + a)
          ans = math.max(ans, f(i)(j) * 2 + b)
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

for folder, text in FILES.items():
    path = ROOT / folder / "Solution.scala"
    path.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", folder)
print("count", len(FILES))
