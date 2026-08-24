#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("3760_maximum_substrings_with_distinct_start", r'''
// LeetCode 3760 - Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/

object Solution {
  def maxDistinct(s: String): Int = {
    val cnt = new Array[Int](26)
    var ans = 0
    s.foreach { c =>
      cnt(c - 'a') += 1
      if (cnt(c - 'a') == 1) ans += 1
    }
    ans
  }
}
''')

w("3761_minimum_absolute_distance_between_mirror_pairs", r'''
// LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
// https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

object Solution {
  def minMirrorPairDistance(nums: Array[Int]): Int = {
    val n = nums.length
    val pos = new java.util.HashMap[Integer, Integer]()
    var ans = n + 1
    var i = 0
    while (i < n) {
      if (pos.containsKey(nums(i))) ans = math.min(ans, i - pos.get(nums(i)))
      pos.put(reverse(nums(i)), i)
      i += 1
    }
    if (ans > n) -1 else ans
  }

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

w("3762_minimum_operations_to_equalize_subarrays", r'''
// LeetCode 3762 - Minimum Operations To Equalize Subarrays
// https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

object Solution {
  private class Node {
    var left: Int = 0
    var right: Int = 0
    var count: Int = 0
    var sum: Long = 0
    def this(o: Node) = {
      this()
      left = o.left; right = o.right; count = o.count; sum = o.sum
    }
  }

  def minOperations(nums: Array[Int], k: Int, queries: Array[Array[Int]]): Array[Long] = {
    val n = nums.length
    val quotient = new Array[Int](n)
    val remainder = new Array[Int](n)
    var values = new Array[Int](n)
    var i = 0
    while (i < n) {
      quotient(i) = nums(i) / k
      remainder(i) = nums(i) % k
      values(i) = quotient(i)
      i += 1
    }
    java.util.Arrays.sort(values)
    var vu = 1
    i = 1
    while (i < n) {
      if (values(i) != values(vu - 1)) {
        values(vu) = values(i)
        vu += 1
      }
      i += 1
    }
    values = java.util.Arrays.copyOf(values, vu)

    val nodes = new java.util.ArrayList[Node]()
    nodes.add(new Node())
    val roots = new Array[Int](n + 1)
    val umax = values.length - 1

    def update(previous: Int, lo: Int, hi: Int, position: Int, value: Int): Int = {
      val current = nodes.size()
      nodes.add(new Node(nodes.get(previous)))
      nodes.get(current).count += 1
      nodes.get(current).sum += value
      if (lo < hi) {
        val mid = (lo + hi) / 2
        if (position <= mid) nodes.get(current).left = update(nodes.get(previous).left, lo, mid, position, value)
        else nodes.get(current).right = update(nodes.get(previous).right, mid + 1, hi, position, value)
      }
      current
    }

    def kth(rightRoot: Int, leftRoot: Int, lo: Int, hi: Int, rank: Int): Int = {
      if (lo == hi) return lo
      val leftCount = nodes.get(nodes.get(rightRoot).left).count - nodes.get(nodes.get(leftRoot).left).count
      val mid = (lo + hi) / 2
      if (rank <= leftCount) kth(nodes.get(rightRoot).left, nodes.get(leftRoot).left, lo, mid, rank)
      else kth(nodes.get(rightRoot).right, nodes.get(leftRoot).right, mid + 1, hi, rank - leftCount)
    }

    def prefixStats(rightRoot: Int, leftRoot: Int, lo: Int, hi: Int, end: Int): Array[Long] = {
      if (end < lo) return Array(0L, 0L)
      if (hi <= end) return Array(
        (nodes.get(rightRoot).count - nodes.get(leftRoot).count).toLong,
        nodes.get(rightRoot).sum - nodes.get(leftRoot).sum
      )
      val mid = (lo + hi) / 2
      val left = prefixStats(nodes.get(rightRoot).left, nodes.get(leftRoot).left, lo, mid, end)
      var count = left(0)
      var sum = left(1)
      if (end > mid) {
        val right = prefixStats(nodes.get(rightRoot).right, nodes.get(leftRoot).right, mid + 1, hi, end)
        count += right(0)
        sum += right(1)
      }
      Array(count, sum)
    }

    def lowerBound(a: Array[Int], x: Int): Int = {
      var lo = 0
      var hi = a.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (a(mid) < x) lo = mid + 1
        else hi = mid
      }
      lo
    }

    i = 0
    while (i < n) {
      val position = lowerBound(values, quotient(i))
      roots(i + 1) = update(roots(i), 0, umax, position, quotient(i))
      i += 1
    }

    val logv = new Array[Int](n + 1)
    i = 2
    while (i <= n) {
      logv(i) = logv(i / 2) + 1
      i += 1
    }
    val levels = logv(n) + 1
    val minTable = new Array[Array[Int]](levels)
    val maxTable = new Array[Array[Int]](levels)
    minTable(0) = remainder.clone()
    maxTable(0) = remainder.clone()
    var level = 1
    while (level < levels) {
      val length = n - (1 << level) + 1
      minTable(level) = new Array[Int](length)
      maxTable(level) = new Array[Int](length)
      val half = 1 << (level - 1)
      i = 0
      while (i < length) {
        minTable(level)(i) = math.min(minTable(level - 1)(i), minTable(level - 1)(i + half))
        maxTable(level)(i) = math.max(maxTable(level - 1)(i), maxTable(level - 1)(i + half))
        i += 1
      }
      level += 1
    }

    val answer = new Array[Long](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val left = queries(qi)(0)
      val right = queries(qi)(1)
      val length = right - left + 1
      val lv = logv(length)
      val offset = right - (1 << lv) + 1
      val minR = math.min(minTable(lv)(left), minTable(lv)(offset))
      val maxR = math.max(maxTable(lv)(left), maxTable(lv)(offset))
      if (minR != maxR) {
        answer(qi) = -1
      } else {
        val medianIndex = kth(roots(right + 1), roots(left), 0, umax, (length + 1) / 2)
        val median = values(medianIndex)
        val stats = prefixStats(roots(right + 1), roots(left), 0, umax, medianIndex)
        val leftCount = stats(0).toInt
        val leftSum = stats(1)
        val totalSum = nodes.get(roots(right + 1)).sum - nodes.get(roots(left)).sum
        answer(qi) = 1L * median * leftCount - leftSum + (totalSum - leftSum) - 1L * median * (length - leftCount)
      }
      qi += 1
    }
    answer
  }
}
''')

w("3763_maximum_total_sum_with_threshold_constraints", r'''
// LeetCode 3763 - Maximum Total Sum With Threshold Constraints
// https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

object Solution {
  def maxSum(nums: Array[Int], threshold: Array[Int]): Long = {
    val n = nums.length
    val idx = Array.tabulate(n)(i => i)
    java.util.Arrays.sort(idx, (a: Integer, b: Integer) => Integer.compare(threshold(a), threshold(b)))
    val tree = new java.util.PriorityQueue[Integer]((a: Integer, b: Integer) => Integer.compare(b, a))
    var ans = 0L
    var i = 0
    var step = 1
    var done = false
    while (!done) {
      while (i < n && threshold(idx(i)) <= step) {
        tree.offer(nums(idx(i)))
        i += 1
      }
      if (tree.isEmpty) done = true
      else {
        ans += tree.poll()
        step += 1
      }
    }
    ans
  }
}
''')

w("3765_complete_prime_number", r'''
// LeetCode 3765 - Complete Prime Number
// https://leetcode.com/problems/complete-prime-number/

object Solution {
  private def isPrime(x: Int): Boolean = {
    if (x < 2) return false
    var i = 2
    while (i * i <= x) {
      if (x % i == 0) return false
      i += 1
    }
    true
  }

  def completePrime(num: Int): Boolean = {
    val s = Integer.toString(num)
    var x = 0
    s.foreach { c =>
      x = x * 10 + (c - '0')
      if (!isPrime(x)) return false
    }
    x = 0
    var p = 1
    var i = s.length - 1
    while (i >= 0) {
      x = p * (s.charAt(i) - '0') + x
      p *= 10
      if (!isPrime(x)) return false
      i -= 1
    }
    true
  }
}
''')

w("3766_minimum_operations_to_make_binary_palindrome", r'''
// LeetCode 3766 - Minimum Operations To Make Binary Palindrome
// https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

object Solution {
  private val PALS: java.util.List[Integer] = {
    val list = new java.util.ArrayList[Integer]()
    val N = 1 << 14
    var i = 0
    while (i < N) {
      val sb = new StringBuilder
      var x = i
      if (x == 0) sb.append('0')
      else {
        while (x > 0) {
          sb.append(('0' + (x & 1)).toChar)
          x >>= 1
        }
        sb.reverse()
      }
      if (isPalindrome(sb)) list.add(i)
      i += 1
    }
    list
  }

  private def isPalindrome(s: StringBuilder): Boolean = {
    val m = s.length
    var i = 0
    while (i < m / 2) {
      if (s.charAt(i) != s.charAt(m - 1 - i)) return false
      i += 1
    }
    true
  }

  def minOperations(nums: Array[Int]): Array[Int] = {
    val ans = new Array[Int](nums.length)
    var k = 0
    while (k < nums.length) {
      val x = nums(k)
      val it = lowerBound(x)
      var t = Integer.MAX_VALUE
      if (it < PALS.size()) t = PALS.get(it) - x
      if (it > 0) t = math.min(t, x - PALS.get(it - 1))
      ans(k) = t
      k += 1
    }
    ans
  }

  private def lowerBound(x: Int): Int = {
    var lo = 0
    var hi = PALS.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (PALS.get(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
''')

w("3767_maximize_points_after_choosing_k_tasks", r'''
// LeetCode 3767 - Maximize Points After Choosing K Tasks
// https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

object Solution {
  def maxPoints(technique1: Array[Int], technique2: Array[Int], k: Int): Long = {
    val n = technique1.length
    val idx = Array.tabulate(n)(i => i)
    java.util.Arrays.sort(idx, (i: Integer, j: Integer) =>
      Integer.compare(technique1(j) - technique2(j), technique1(i) - technique2(i)))
    var ans = 0L
    technique2.foreach(x => ans += x)
    var i = 0
    while (i < k) {
      val index = idx(i)
      ans -= technique2(index)
      ans += technique1(index)
      i += 1
    }
    i = k
    while (i < n) {
      val index = idx(i)
      if (technique1(index) >= technique2(index)) {
        ans -= technique2(index)
        ans += technique1(index)
      }
      i += 1
    }
    ans
  }
}
''')

w("3768_minimum_inversion_count_in_subarrays_of_fixed_length", r'''
// LeetCode 3768 - Minimum Inversion Count In Subarrays Of Fixed Length
// https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

object Solution {
  def minInversionCount(nums: Array[Int], k: Int): Long = {
    var vals = nums.clone()
    java.util.Arrays.sort(vals)
    val u = unique(vals)
    vals = java.util.Arrays.copyOf(vals, u)
    val bit = new Array[Int](vals.length + 1)

    def add(i0: Int, delta: Int): Unit = {
      var i = i0
      while (i < bit.length) {
        bit(i) += delta
        i += i & -i
      }
    }

    def sum(i0: Int): Int = {
      var i = i0
      var res = 0
      while (i > 0) {
        res += bit(i)
        i -= i & -i
      }
      res
    }

    val rank = new Array[Int](nums.length)
    var inv = 0L
    var i = 0
    while (i < nums.length) {
      rank(i) = lowerBound(vals, nums(i)) + 1
      if (i < k) {
        inv += i - sum(rank(i))
        add(rank(i), 1)
      }
      i += 1
    }
    var best = inv
    var r = k
    while (r < nums.length) {
      val left = rank(r - k)
      inv -= sum(left - 1)
      add(left, -1)
      inv += k - 1 - sum(rank(r))
      add(rank(r), 1)
      if (inv < best) best = inv
      r += 1
    }
    best
  }

  private def unique(a: Array[Int]): Int = {
    var n = 0
    var i = 0
    while (i < a.length) {
      if (n == 0 || a(i) != a(n - 1)) {
        a(n) = a(i)
        n += 1
      }
      i += 1
    }
    n
  }

  private def lowerBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
''')

w("3769_sort_integers_by_binary_reflection", r'''
// LeetCode 3769 - Sort Integers By Binary Reflection
// https://leetcode.com/problems/sort-integers-by-binary-reflection/

object Solution {
  def sortByReflection(nums: Array[Int]): Array[Int] = {
    val arr = Array.tabulate(nums.length)(i => nums(i))
    java.util.Arrays.sort(arr, (a: Integer, b: Integer) => {
      val fa = f(a)
      val fb = f(b)
      if (fa != fb) Integer.compare(fa, fb)
      else Integer.compare(a, b)
    })
    var i = 0
    while (i < nums.length) {
      nums(i) = arr(i)
      i += 1
    }
    nums
  }

  private def f(x0: Int): Int = {
    var x = x0
    var y = 0
    while (x != 0) {
      y = (y << 1) | (x & 1)
      x >>= 1
    }
    y
  }
}
''')

w("3770_largest_prime_from_consecutive_prime_sum", r'''
// LeetCode 3770 - Largest Prime From Consecutive Prime Sum
// https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/

object Solution {
  private val MX = 500000
  private val S: java.util.List[Integer] = {
    val list = new java.util.ArrayList[Integer]()
    val isPrime = Array.fill(MX + 1)(true)
    isPrime(0) = false
    isPrime(1) = false
    val primes = new java.util.ArrayList[Integer]()
    var i = 2
    while (i <= MX) {
      if (isPrime(i)) {
        primes.add(i)
        if (i.toLong * i <= MX) {
          var j = i * i
          while (j <= MX) {
            isPrime(j) = false
            j += i
          }
        }
      }
      i += 1
    }
    list.add(0)
    var t = 0
    val it = primes.iterator()
    var stop = false
    while (it.hasNext && !stop) {
      val x = it.next()
      t += x
      if (t > MX) stop = true
      else if (isPrime(t)) list.add(t)
    }
    list
  }

  def largestPrime(n: Int): Int = {
    var lo = 0
    var hi = S.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (S.get(mid) <= n) lo = mid + 1
      else hi = mid
    }
    S.get(lo - 1)
  }
}
''')

w("3771_total_score_of_dungeon_runs", r'''
// LeetCode 3771 - Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/

object Solution {
  def totalScore(hp: Int, damage: Array[Int], requirement: Array[Int]): Long = {
    val n = damage.length
    val prefix = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + damage(i)
      i += 1
    }
    var answer = 1L * n * (n + 1) / 2
    var j = 1
    while (j <= n) {
      val threshold = prefix(j) + (requirement(j - 1) - hp)
      var lo = 0
      var hi = j
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (prefix(mid) < threshold) lo = mid + 1
        else hi = mid
      }
      answer -= lo
      j += 1
    }
    answer
  }
}
''')

w("3772_maximum_subgraph_score_in_a_tree", r'''
// LeetCode 3772 - Maximum Subgraph Score In A Tree
// https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

object Solution {
  def maxSubgraphScore(n: Int, edges: Array[Array[Int]], good: Array[Int]): Array[Int] = {
    val g = Array.fill(n)(new java.util.ArrayList[Integer]())
    edges.foreach { e =>
      g(e(0)).add(e(1))
      g(e(1)).add(e(0))
    }
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
    val down = new Array[Int](n)
    i = n - 1
    while (i >= 0) {
      val u = order.get(i)
      down(u) = 2 * good(u) - 1
      val it = g(u).iterator()
      while (it.hasNext) {
        val v = it.next()
        if (parent(v) == u && down(v) > 0) down(u) += down(v)
      }
      i -= 1
    }
    val ans = down.clone()
    i = 0
    while (i < order.size()) {
      val u = order.get(i)
      val it = g(u).iterator()
      while (it.hasNext) {
        val v = it.next()
        if (parent(v) == u) {
          var outside = ans(u)
          if (down(v) > 0) outside -= down(v)
          ans(v) = down(v)
          if (outside > 0) ans(v) += outside
        }
      }
      i += 1
    }
    ans
  }
}
''')

w("3773_maximum_number_of_equal_length_runs", r'''
// LeetCode 3773 - Maximum Number Of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

object Solution {
  def maxSameLengthRuns(s: String): Int = {
    val cnt = new java.util.HashMap[Integer, Integer]()
    val n = s.length
    var ans = 0
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n && s.charAt(j) == s.charAt(i)) j += 1
      val m = j - i
      if (!cnt.containsKey(m)) cnt.put(m, 0)
      cnt.merge(m, 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
      ans = math.max(ans, cnt.get(m))
      i = j
    }
    ans
  }
}
''')
