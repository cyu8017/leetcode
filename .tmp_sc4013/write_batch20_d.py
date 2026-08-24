#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("3774_absolute_difference_between_maximum_and_minimum_k_elements", r'''
// LeetCode 3774 - Absolute Difference Between Maximum And Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

object Solution {
  def absDifference(nums: Array[Int], k: Int): Int = {
    java.util.Arrays.sort(nums)
    var ans = 0
    val n = nums.length
    var i = 0
    while (i < k) {
      ans += nums(n - i - 1) - nums(i)
      i += 1
    }
    ans
  }
}
''')

w("3775_reverse_words_with_same_vowel_count", r'''
// LeetCode 3775 - Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse-words-with-same-vowel-count/

object Solution {
  private def calc(w: String): Int = {
    var cnt = 0
    w.foreach { c =>
      if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') cnt += 1
    }
    cnt
  }

  def reverseWords(s: String): String = {
    val words = s.trim.split("\\s+")
    val cnt = calc(words(0))
    val ans = new StringBuilder
    ans.append(words(0))
    var i = 1
    while (i < words.length) {
      var w = words(i)
      if (calc(w) == cnt) w = new StringBuilder(w).reverse().toString
      ans.append(' ').append(w)
      i += 1
    }
    ans.toString
  }
}
''')

w("3776_minimum_moves_to_balance_circular_array", r'''
// LeetCode 3776 - Minimum Moves To Balance Circular Array
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

object Solution {
  def minMoves(balance: Array[Int]): Long = {
    var sum = 0L
    balance.foreach(b => sum += b)
    if (sum < 0) return -1

    val n = balance.length
    var mn = balance(0)
    var idx = 0
    var i = 1
    while (i < n) {
      if (balance(i) < mn) {
        mn = balance(i)
        idx = i
      }
      i += 1
    }
    if (mn >= 0) return 0

    var need = -mn
    var ans = 0L
    var j = 1
    while (j < n) {
      val a = balance((idx - j + n) % n)
      val b = balance((idx + j) % n)
      val c1 = math.min(a, need)
      need -= c1
      ans += c1.toLong * j
      val c2 = math.min(b, need)
      need -= c2
      ans += c2.toLong * j
      j += 1
    }
    ans
  }
}
''')

w("3777_minimum_deletions_to_make_alternating_substring", r'''
// LeetCode 3777 - Minimum Deletions To Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

object Solution {
  private class BIT(n_ : Int) {
    val n: Int = n_
    val c: Array[Int] = new Array[Int](n_ + 1)
    def update(x0: Int, delta: Int): Unit = {
      var x = x0
      while (x <= n) {
        c(x) += delta
        x += x & -x
      }
    }
    def query(x0: Int): Int = {
      var x = x0
      var s = 0
      while (x > 0) {
        s += c(x)
        x -= x & -x
      }
      s
    }
  }

  def minDeletions(s: String, queries: Array[Array[Int]]): Array[Int] = {
    val n = s.length
    val nums = new Array[Int](n)
    val bit = new BIT(n)
    var i = 1
    while (i < n) {
      if (s.charAt(i) == s.charAt(i - 1)) {
        nums(i) = 1
        bit.update(i + 1, 1)
      }
      i += 1
    }
    val ans = new java.util.ArrayList[Integer]()
    queries.foreach { q =>
      if (q(0) == 1) {
        val j = q(1)
        var delta = (nums(j) ^ 1) - nums(j)
        nums(j) ^= 1
        bit.update(j + 1, delta)
        if (j + 1 < n) {
          delta = (nums(j + 1) ^ 1) - nums(j + 1)
          nums(j + 1) ^= 1
          bit.update(j + 2, delta)
        }
      } else {
        val l = q(1)
        val r = q(2)
        ans.add(bit.query(r + 1) - bit.query(l + 1))
      }
    }
    val out = new Array[Int](ans.size())
    i = 0
    while (i < out.length) {
      out(i) = ans.get(i)
      i += 1
    }
    out
  }
}
''')

w("3778_minimum_distance_excluding_one_maximum_weighted_edge", r'''
// LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
// https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

object Solution {
  def minCostExcludingMax(n: Int, edges: Array[Array[Int]]): Long = {
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    edges.foreach { e =>
      val u = e(0); val v = e(1); val w = e(2)
      g(u).add(Array(v, w))
      g(v).add(Array(u, w))
    }
    val INF = 4e18.toLong
    val dist = Array.fill(n, 2)(INF)
    dist(0)(0) = 0
    val pq = new java.util.PriorityQueue[Array[Long]]((a: Array[Long], b: Array[Long]) => java.lang.Long.compare(a(0), b(0)))
    pq.offer(Array(0L, 0L, 0L))
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val c = cur(0)
      val u = cur(1).toInt
      val used = cur(2).toInt
      if (c <= dist(u)(used)) {
        if (u == n - 1 && used == 1) return c
        val it = g(u).iterator()
        while (it.hasNext) {
          val e = it.next()
          val v = e(0)
          val w = e(1)
          var nxt = c + w
          if (nxt < dist(v)(used)) {
            dist(v)(used) = nxt
            pq.offer(Array(nxt, v.toLong, used.toLong))
          }
          if (used == 0) {
            nxt = c
            if (nxt < dist(v)(1)) {
              dist(v)(1) = nxt
              pq.offer(Array(nxt, v.toLong, 1L))
            }
          }
        }
      }
    }
    dist(n - 1)(1)
  }
}
''')

w("3779_minimum_number_of_operations_to_have_distinct_elements", r'''
// LeetCode 3779 - Minimum Number Of Operations To Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    val st = new java.util.HashSet[Integer]()
    var i = nums.length - 1
    while (i >= 0) {
      if (st.contains(nums(i))) return i / 3 + 1
      st.add(nums(i))
      i -= 1
    }
    0
  }
}
''')

w("3780_maximum_sum_of_three_numbers_divisible_by_three", r'''
// LeetCode 3780 - Maximum Sum Of Three Numbers Divisible By Three
// https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/

object Solution {
  def maximumSum(nums: Array[Int]): Int = {
    java.util.Arrays.sort(nums)
    val g = Array.fill(3)(new java.util.ArrayList[Integer]())
    nums.foreach(x => g(x % 3).add(x))
    var ans = 0
    var a = 0
    while (a < 3) {
      if (!g(a).isEmpty) {
        val x = g(a).remove(g(a).size() - 1)
        var b = 0
        while (b < 3) {
          if (!g(b).isEmpty) {
            val y = g(b).remove(g(b).size() - 1)
            val c = (3 - (a + b) % 3) % 3
            if (!g(c).isEmpty) {
              val z = g(c).get(g(c).size() - 1)
              ans = math.max(ans, x + y + z)
            }
            g(b).add(y)
          }
          b += 1
        }
        g(a).add(x)
      }
      a += 1
    }
    ans
  }
}
''')

w("3781_maximum_score_after_binary_swaps", r'''
// LeetCode 3781 - Maximum Score After Binary Swaps
// https://leetcode.com/problems/maximum-score-after-binary-swaps/

object Solution {
  def maximumScore(nums: Array[Int], s: String): Long = {
    var ans = 0L
    val pq = new java.util.PriorityQueue[Integer]((a: Integer, b: Integer) => Integer.compare(b, a))
    var i = 0
    while (i < nums.length) {
      pq.offer(nums(i))
      if (s.charAt(i) == '1') ans += pq.poll()
      i += 1
    }
    ans
  }
}
''')

w("3782_last_remaining_integer_after_alternating_deletion_operations", r'''
// LeetCode 3782 - Last Remaining Integer After Alternating Deletion Operations
// https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/

object Solution {
  def lastRemaining(n0: Long): Long = {
    var n = n0
    var first = 1L
    var step = 2L
    var left = true
    while (n > 1) {
      if (!left && n % 2 == 0) first += step
      n = (n + 1) / 2
      step *= 2
      left = !left
    }
    first
  }
}
''')

w("3783_mirror_distance_of_an_integer", r'''
// LeetCode 3783 - Mirror Distance Of An Integer
// https://leetcode.com/problems/mirror-distance-of-an-integer/

object Solution {
  def mirrorDistance(n: Int): Int = math.abs(n - reverse(n))

  private def reverse(x0: Int): Int = {
    var x = x0
    var y = 0
    while (x > 0) {
      y = y * 10 + x % 10
      x /= 10
    }
    y
  }
}
''')

w("3784_minimum_deletion_cost_to_make_all_characters_equal", r'''
// LeetCode 3784 - Minimum Deletion Cost To Make All Characters Equal
// https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

object Solution {
  def minCost(s: String, cost: Array[Int]): Long = {
    var tot = 0L
    val g = new java.util.HashMap[Character, java.lang.Long]()
    var i = 0
    while (i < cost.length) {
      tot += cost(i)
      g.merge(s.charAt(i), cost(i).toLong, (a: java.lang.Long, b: java.lang.Long) => java.lang.Long.valueOf(a + b))
      i += 1
    }
    var ans = tot
    val it = g.values().iterator()
    while (it.hasNext) {
      val x = it.next()
      ans = math.min(ans, tot - x)
    }
    ans
  }
}
''')

w("3785_minimum_swaps_to_avoid_forbidden_values", r'''
// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

object Solution {
  def minSwaps(nums: Array[Int], forbidden: Array[Int]): Int = {
    val n = nums.length
    val freq = new java.util.HashMap[Integer, Integer]()
    nums.foreach { x =>
      if (!freq.containsKey(x)) freq.put(x, 0)
      freq.merge(x, 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
    }
    forbidden.foreach { x =>
      if (!freq.containsKey(x)) freq.put(x, 0)
      freq.merge(x, 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
    }
    val it = freq.values().iterator()
    while (it.hasNext) {
      if (it.next() > n) return -1
    }
    val bad = new java.util.HashMap[Integer, Integer]()
    var total = 0
    var largest = 0
    var i = 0
    while (i < n) {
      if (nums(i) == forbidden(i)) {
        if (!bad.containsKey(nums(i))) bad.put(nums(i), 0)
        bad.merge(nums(i), 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
        total += 1
        if (bad.get(nums(i)) > largest) largest = bad.get(nums(i))
      }
      i += 1
    }
    if ((total + 1) / 2 > largest) (total + 1) / 2 else largest
  }
}
''')

w("3786_total_sum_of_interaction_cost_in_tree_groups", r'''
// LeetCode 3786 - Total Sum Of Interaction Cost In Tree Groups
// https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

object Solution {
  def interactionCost(n: Int, edges: Array[Array[Int]], group: Array[Int]): Long = {
    val g = Array.fill(n)(new java.util.ArrayList[Integer]())
    edges.foreach { e =>
      g(e(0)).add(e(1))
      g(e(1)).add(e(0))
    }
    val total = new Array[Int](21)
    group.foreach(x => total(x) += 1)
    val parent = Array.fill(n)(-2)
    parent(0) = -1
    val order = new java.util.ArrayList[Integer]()
    order.add(0)
    var i = 0
    while (i < order.size()) {
      val u = order.get(i)
      val it = g(u).iterator()
      while (it.hasNext) {
        val v = it.next()
        if (parent(v) == -2) {
          parent(v) = u
          order.add(v)
        }
      }
      i += 1
    }
    val count = Array.ofDim[Int](n, 21)
    var ans = 0L
    i = n - 1
    while (i >= 0) {
      val u = order.get(i)
      count(u)(group(u)) += 1
      val it = g(u).iterator()
      while (it.hasNext) {
        val v = it.next()
        if (parent(v) == u) {
          var c = 1
          while (c <= 20) {
            val x = count(v)(c)
            ans += x.toLong * (total(c) - x)
            count(u)(c) += x
            c += 1
          }
        }
      }
      i -= 1
    }
    ans
  }
}
''')

w("3787_find_diameter_endpoints_of_a_tree", r'''
// LeetCode 3787 - Find Diameter Endpoints Of A Tree
// https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/

object Solution {
  def findSpecialNodes(n: Int, edges: Array[Array[Int]]): String = {
    val g = Array.fill(n)(new java.util.ArrayList[Integer]())
    edges.foreach { e =>
      g(e(0)).add(e(1))
      g(e(1)).add(e(0))
    }

    def bfs(start: Int): Array[Int] = {
      val dist = Array.fill(n)(-1)
      dist(start) = 0
      val q = new java.util.ArrayList[Integer]()
      q.add(start)
      var far = start
      var head = 0
      while (head < q.size()) {
        val u = q.get(head)
        if (dist(u) > dist(far)) far = u
        val it = g(u).iterator()
        while (it.hasNext) {
          val v = it.next()
          if (dist(v) == -1) {
            dist(v) = dist(u) + 1
            q.add(v)
          }
        }
        head += 1
      }
      val out = new Array[Int](n + 1)
      out(0) = far
      System.arraycopy(dist, 0, out, 1, n)
      out
    }

    val r0 = bfs(0)
    val a = r0(0)
    val r1 = bfs(a)
    val b = r1(0)
    val dist1 = java.util.Arrays.copyOfRange(r1, 1, n + 1)
    val r2 = bfs(b)
    val dist2 = java.util.Arrays.copyOfRange(r2, 1, n + 1)
    val d = dist1(b)
    val ans = Array.fill(n)('0')
    var i = 0
    while (i < n) {
      if (dist1(i) == d || dist2(i) == d) ans(i) = '1'
      i += 1
    }
    new String(ans)
  }
}
''')

w("3788_maximum_score_of_a_split", r'''
// LeetCode 3788 - Maximum Score Of A Split
// https://leetcode.com/problems/maximum-score-of-a-split/

object Solution {
  def maximumScore(nums: Array[Int]): Long = {
    val n = nums.length
    val suf = new Array[Long](n)
    suf(n - 1) = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      suf(i) = math.min(nums(i), suf(i + 1))
      i -= 1
    }
    var pre = 0L
    var ans = Long.MinValue
    i = 0
    while (i < n - 1) {
      pre += nums(i)
      ans = math.max(ans, pre - suf(i + 1))
      i += 1
    }
    ans
  }
}
''')

w("3789_minimum_cost_to_acquire_required_items", r'''
// LeetCode 3789 - Minimum Cost To Acquire Required Items
// https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

object Solution {
  def minimumCost(cost1: Int, cost2: Int, costBoth: Int, need1: Int, need2: Int): Long = {
    val a = need1.toLong * cost1 + need2.toLong * cost2
    val b = costBoth.toLong * math.max(need1, need2)
    val mn = math.min(need1, need2)
    val c = costBoth.toLong * mn + (need1 - mn).toLong * cost1 + (need2 - mn).toLong * cost2
    math.min(a, math.min(b, c))
  }
}
''')

w("3790_smallest_all_ones_multiple", r'''
// LeetCode 3790 - Smallest All Ones Multiple
// https://leetcode.com/problems/smallest-all-ones-multiple/

object Solution {
  def minAllOneMultiple(k: Int): Int = {
    if ((k & 1) == 0) return -1
    var x = 1 % k
    var ans = 1
    var i = 0
    while (i < k) {
      x = (x * 10 + 1) % k
      ans += 1
      if (x == 0) return ans
      i += 1
    }
    -1
  }
}
''')

w("3791_number_of_balanced_integers_in_a_range", r'''
// LeetCode 3791 - Number Of Balanced Integers In A Range
// https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

object Solution {
  private val BASE = 90

  def countBalanced(low0: Long, high: Long): Long = {
    if (high < 11) return 0
    var low = low0
    if (low < 11) low = 11
    var num = ""
    val f = Array.fill(20, 181)(-1L)

    def dfs(pos: Int, diff: Int, lim: Boolean): Long = {
      if (pos >= num.length) return if (diff == 0) 1 else 0
      if (!lim && f(pos)(diff + BASE) != -1) return f(pos)(diff + BASE)
      val up = if (lim) num.charAt(pos) - '0' else 9
      var res = 0L
      var i = 0
      while (i <= up) {
        if (pos % 2 == 0) res += dfs(pos + 1, diff + i, lim && i == up)
        else res += dfs(pos + 1, diff - i, lim && i == up)
        i += 1
      }
      if (!lim) f(pos)(diff + BASE) = res
      res
    }

    num = java.lang.Long.toString(low - 1)
    var r = 0
    while (r < 20) {
      java.util.Arrays.fill(f(r), -1L)
      r += 1
    }
    val a = dfs(0, 0, lim = true)
    num = java.lang.Long.toString(high)
    r = 0
    while (r < 20) {
      java.util.Arrays.fill(f(r), -1L)
      r += 1
    }
    val b = dfs(0, 0, lim = true)
    b - a
  }
}
''')

w("3792_sum_of_increasing_product_blocks", r'''
// LeetCode 3792 - Sum Of Increasing Product Blocks
// https://leetcode.com/problems/sum-of-increasing-product-blocks/

object Solution {
  def sumOfBlocks(n: Int): Int = {
    val MOD = 1000000007
    var ans = 0
    var k = 1
    var i = 1
    while (i <= n) {
      var x = 1
      var j = k
      while (j < k + i) {
        x = ((x.toLong * j) % MOD).toInt
        j += 1
      }
      ans = (ans + x) % MOD
      k += i
      i += 1
    }
    ans
  }
}
''')

w("3794_reverse_string_prefix", r'''
// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

object Solution {
  def reversePrefix(s: String, k: Int): String = {
    val arr = s.toCharArray
    reverse(arr, 0, 0 + k)
    new String(arr)
  }

  private def reverse(a: Array[Char], l: Int, r: Int): Unit = {
    var i = l
    var j = r - 1
    while (i < j) {
      val t = a(i); a(i) = a(j); a(j) = t
      i += 1
      j -= 1
    }
  }
}
''')
