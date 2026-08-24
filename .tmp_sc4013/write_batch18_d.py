#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3575_maximum_good_subtree_score"] = r'''// LeetCode 3575 - Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/

object Solution {
  val MOD = 1000000007

  def digitMask(x0: Int): Array[Int] = {
    var x = x0
    val v = x0
    var mask = 0
    if (x == 0) return Array(1, 1, 0)
    while (x > 0) {
      val d = x % 10
      if ((mask & (1 << d)) != 0) return Array(0, 0, 0)
      mask |= 1 << d
      x /= 10
    }
    Array(mask, 1, v)
  }

  def goodSubtreeSum(vals: Array[Int], par: Array[Int]): Int = {
    val n = vals.length
    val g = Array.fill(n)(new java.util.ArrayList[Integer]())
    var i = 1
    while (i < n) { g(par(i)).add(i); i += 1 }
    var ans = 0

    def dfs(u: Int): java.util.HashMap[Integer, Integer] = {
      val dp = new java.util.HashMap[Integer, Integer]()
      dp.put(0, 0)
      val dm = digitMask(vals(u))
      if (dm(1) == 1) dp.put(dm(0), dm(2))
      val cit = g(u).iterator()
      while (cit.hasNext) {
        val c = cit.next().intValue()
        val child = dfs(c)
        val ndp = new java.util.HashMap[Integer, Integer]()
        val e1it = dp.entrySet().iterator()
        while (e1it.hasNext) {
          val e1 = e1it.next()
          val e2it = child.entrySet().iterator()
          while (e2it.hasNext) {
            val e2 = e2it.next()
            if ((e1.getKey() & e2.getKey()) == 0) {
              val nm = e1.getKey() | e2.getKey()
              ndp.put(nm, math.max(ndp.getOrDefault(nm, 0), e1.getValue() + e2.getValue()))
            }
          }
        }
        val dit = dp.entrySet().iterator()
        while (dit.hasNext) {
          val e = dit.next()
          ndp.put(e.getKey(), math.max(ndp.getOrDefault(e.getKey(), 0), e.getValue()))
        }
        val chit = child.entrySet().iterator()
        while (chit.hasNext) {
          val e = chit.next()
          ndp.put(e.getKey(), math.max(ndp.getOrDefault(e.getKey(), 0), e.getValue()))
        }
        dp.clear()
        dp.putAll(ndp)
      }
      var best = 0
      val vit = dp.values().iterator()
      while (vit.hasNext) best = math.max(best, vit.next())
      ans = (ans + best) % MOD
      dp
    }

    dfs(0)
    ans
  }
}
'''

FILES["3576_transform_array_to_all_equal_elements"] = r'''// LeetCode 3576 - Transform Array to All Equal Elements
// https://leetcode.com/problems/transform-array-to-all-equal-elements/

object Solution {
  def check(nums: Array[Int], target: Int, kk: Int): Boolean = {
    var cnt = 0
    var sign = 1
    var i = 0
    while (i < nums.length - 1) {
      val x = nums(i) * sign
      if (x == target) sign = 1
      else { sign = -1; cnt += 1 }
      i += 1
    }
    cnt <= kk && nums(nums.length - 1) * sign == target
  }

  def canMakeEqual(nums: Array[Int], k: Int): Boolean =
    check(nums, nums(0), k) || check(nums, -nums(0), k)
}
'''

FILES["3577_count_the_number_of_computer_unlocking_permutations"] = r'''// LeetCode 3577 - Count the Number of Computer Unlocking Permutations
// https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

object Solution {
  def countPermutations(complexity: Array[Int]): Int = {
    val mod = 1000000007L
    var ans = 1L
    var i = 1
    while (i < complexity.length) {
      if (complexity(i) <= complexity(0)) return 0
      ans = ans * i % mod
      i += 1
    }
    ans.toInt
  }
}
'''

FILES["3578_count_partitions_with_max_min_difference_at_most_k"] = r'''// LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
// https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

object Solution {
  def countPartitions(nums: Array[Int], k: Int): Int = {
    val mod = 1000000007
    val sl = new java.util.TreeMap[Integer, Integer]()
    val n = nums.length
    val f = new Array[Int](n + 1)
    val g = new Array[Int](n + 1)
    f(0) = 1
    g(0) = 1
    var l = 1
    var r = 1
    while (r <= n) {
      sl.merge(nums(r - 1), 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
      while (sl.lastKey() - sl.firstKey() > k) {
        val v = nums(l - 1)
        val c = sl.get(v)
        if (c == 1) sl.remove(v)
        else sl.put(v, c - 1)
        l += 1
      }
      f(r) = g(r - 1)
      if (l >= 2) f(r) = (f(r) - g(l - 2) + mod) % mod
      g(r) = (g(r - 1) + f(r)) % mod
      r += 1
    }
    f(n)
  }
}
'''

FILES["3579_minimum_steps_to_convert_string_with_operations"] = r'''// LeetCode 3579 - Minimum Steps to Convert String with Operations
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

object Solution {
  def calc(word1: String, word2: String, l: Int, r: Int, rev: Boolean): Int = {
    val cnt = Array.ofDim[Int](26, 26)
    var res = 0
    var i = l
    while (i <= r) {
      val j = if (rev) r - (i - l) else i
      val a = word1.charAt(j) - 'a'
      val b = word2.charAt(i) - 'a'
      if (a != b) {
        if (cnt(b)(a) > 0) cnt(b)(a) -= 1
        else { cnt(a)(b) += 1; res += 1 }
      }
      i += 1
    }
    res
  }

  def minOperations(word1: String, word2: String): Int = {
    val n = word1.length
    val f = Array.fill(n + 1)(Integer.MAX_VALUE / 2)
    f(0) = 0
    var i = 1
    while (i <= n) {
      var j = 0
      while (j < i) {
        val a = calc(word1, word2, j, i - 1, false)
        val b = 1 + calc(word1, word2, j, i - 1, true)
        f(i) = math.min(f(i), f(j) + math.min(a, b))
        j += 1
      }
      i += 1
    }
    f(n)
  }
}
'''

FILES["3581_count_odd_letters_from_number"] = r'''// LeetCode 3581 - Count Odd Letters from Number
// https://leetcode.com/problems/count-odd-letters-from-number/

object Solution {
  def countOddLetters(n0: Int): Int = {
    val d = Array("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    var n = n0
    var mask = 0
    while (n > 0) {
      for (c <- d(n % 10).toCharArray) mask ^= 1 << (c - 'a')
      n /= 10
    }
    Integer.bitCount(mask)
  }
}
'''

FILES["3582_generate_tag_for_video_caption"] = r'''// LeetCode 3582 - Generate Tag for Video Caption
// https://leetcode.com/problems/generate-tag-for-video-caption/

object Solution {
  def generateTag(caption: String): String = {
    val ans = new StringBuilder("#")
    val words = caption.trim.split("\\s+")
    var i = 0
    var done = false
    for (word <- words if !done) {
      if (word.nonEmpty) {
        val w = new StringBuilder(word.toLowerCase)
        if (i == 0) ans.append(w)
        else {
          if (w.length > 0) w.setCharAt(0, Character.toUpperCase(w.charAt(0)))
          ans.append(w)
        }
        if (ans.length >= 100) done = true
        else i += 1
      }
    }
    if (ans.length > 100) ans.setLength(100)
    ans.toString
  }
}
'''

FILES["3583_count_special_triplets"] = r'''// LeetCode 3583 - Count Special Triplets
// https://leetcode.com/problems/count-special-triplets/

object Solution {
  def specialTriplets(nums: Array[Int]): Int = {
    val left = scala.collection.mutable.HashMap.empty[Int, Int]
    val right = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) right(x) = right.getOrElse(x, 0) + 1
    var ans = 0L
    val mod = 1000000007L
    for (x <- nums) {
      right(x) = right(x) - 1
      val lv = left.getOrElse(x * 2, 0).toLong
      val rv = right.getOrElse(x * 2, 0).toLong
      ans = (ans + lv * rv % mod) % mod
      left(x) = left.getOrElse(x, 0) + 1
    }
    ans.toInt
  }
}
'''

FILES["3584_maximum_product_of_first_and_last_elements_of_a_subsequence"] = r'''// LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
// https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

object Solution {
  def maximumProduct(nums: Array[Int], m: Int): Long = {
    var ans = Long.MinValue
    var mx = Integer.MIN_VALUE
    var mi = Integer.MAX_VALUE
    var i = m - 1
    while (i < nums.length) {
      val x = nums(i)
      val y = nums(i - m + 1)
      mi = math.min(mi, y)
      mx = math.max(mx, y)
      ans = math.max(ans, math.max(1L * x * mi, 1L * x * mx))
      i += 1
    }
    ans
  }
}
'''

FILES["3585_find_weighted_median_node_in_tree"] = r'''// LeetCode 3585 - Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/

object Solution {
  def findMedian(n: Int, edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    for (e <- edges) {
      g(e(0)).add(Array(e(1), e(2)))
      g(e(1)).add(Array(e(0), e(2)))
    }
    val ans = new Array[Int](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val u = queries(qi)(0)
      val v = queries(qi)(1)
      val parent = Array.fill(n)(-2)
      val pw = new Array[Int](n)
      parent(u) = -1
      val q = new java.util.ArrayDeque[Integer]()
      q.add(u)
      while (!q.isEmpty) {
        val x = q.poll()
        if (x == v) { /* found */ }
        else {
          val it = g(x).iterator()
          while (it.hasNext) {
            val e = it.next()
            if (parent(e(0)) == -2) {
              parent(e(0)) = x
              pw(e(0)) = e(1)
              q.add(e(0))
            }
          }
        }
      }
      val nodes = new java.util.ArrayList[Integer]()
      nodes.add(v)
      val weights = new java.util.ArrayList[Integer]()
      var cur = v
      while (cur != u) {
        weights.add(pw(cur))
        cur = parent(cur)
        nodes.add(cur)
      }
      java.util.Collections.reverse(nodes)
      java.util.Collections.reverse(weights)
      var total = 0
      val wit = weights.iterator()
      while (wit.hasNext) total += wit.next()
      val need = (total + 1) / 2
      var sum = 0
      var med = u
      var i = 0
      while (i < weights.size()) {
        sum += weights.get(i)
        med = nodes.get(i + 1)
        if (sum >= need) i = weights.size()
        else i += 1
      }
      ans(qi) = med
      qi += 1
    }
    ans
  }
}
'''

FILES["3587_minimum_adjacent_swaps_to_alternate_parity"] = r'''// LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
// https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

object Solution {
  def calc(pos: Array[java.util.ArrayList[Integer]], n: Int, k: Int): Int = {
    var res = 0
    var i = 0
    while (i < n) {
      res += math.abs(pos(k).get(i / 2) - i)
      i += 2
    }
    res
  }

  def minSwaps(nums: Array[Int]): Int = {
    val pos = Array(new java.util.ArrayList[Integer](), new java.util.ArrayList[Integer]())
    var i = 0
    while (i < nums.length) { pos(nums(i) & 1).add(i); i += 1 }
    if (math.abs(pos(0).size() - pos(1).size()) > 1) return -1
    if (pos(0).size() > pos(1).size()) return calc(pos, nums.length, 0)
    if (pos(0).size() < pos(1).size()) return calc(pos, nums.length, 1)
    math.min(calc(pos, nums.length, 0), calc(pos, nums.length, 1))
  }
}
'''

FILES["3588_find_maximum_area_of_a_triangle"] = r'''// LeetCode 3588 - Find Maximum Area of a Triangle
// https://leetcode.com/problems/find-maximum-area-of-a-triangle/

object Solution {
  def calc(coords: Array[Array[Int]]): Long = {
    var mn = 1000000000
    var mx = 0
    val f = scala.collection.mutable.HashMap.empty[Int, Int]
    val g = scala.collection.mutable.HashMap.empty[Int, Int]
    for (c <- coords) {
      val x = c(0)
      val y = c(1)
      mn = math.min(mn, x)
      mx = math.max(mx, x)
      if (f.contains(x)) {
        f(x) = math.min(f(x), y)
        g(x) = math.max(g(x), y)
      } else {
        f(x) = y
        g(x) = y
      }
    }
    var ans = 0L
    for ((x, y) <- f) {
      val d = g(x) - y
      ans = math.max(ans, 1L * d * math.max(mx - x, x - mn))
    }
    ans
  }

  def maxArea(coords: Array[Array[Int]]): Long = {
    var ans = calc(coords)
    for (c <- coords) {
      val t = c(0)
      c(0) = c(1)
      c(1) = t
    }
    ans = math.max(ans, calc(coords))
    if (ans > 0) ans else -1
  }
}
'''

FILES["3589_count_prime_gap_balanced_subarrays"] = r'''// LeetCode 3589 - Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

object Solution {
  def primeSubarray(nums: Array[Int], k: Int): Int = {
    var mx = 0
    for (v <- nums) mx = math.max(mx, v)
    val isPrime = new Array[Boolean](mx + 1)
    var i = 2
    while (i <= mx) { isPrime(i) = true; i += 1 }
    i = 2
    while (i * i <= mx) {
      if (isPrime(i)) {
        var j = i * i
        while (j <= mx) { isPrime(j) = false; j += i }
      }
      i += 1
    }
    val n = nums.length
    var ans = 0
    var l = 0
    while (l < n) {
      val primes = new java.util.ArrayList[Integer]()
      var r = l
      while (r < n) {
        if (isPrime(nums(r))) primes.add(nums(r))
        if (primes.size() >= 2) {
          var mn = primes.get(0)
          var mxp = primes.get(0)
          val it = primes.iterator()
          while (it.hasNext) {
            val p = it.next()
            mn = math.min(mn, p)
            mxp = math.max(mxp, p)
          }
          if (mxp - mn <= k) ans += 1
        }
        r += 1
      }
      l += 1
    }
    ans
  }
}
'''

FILES["3590_kth_smallest_path_xor_sum"] = r'''// LeetCode 3590 - Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/

object Solution {
  def kthSmallest(par: Array[Int], vals: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = par.length
    val g = Array.fill(n)(new java.util.ArrayList[Integer]())
    var i = 1
    while (i < n) { g(par(i)).add(i); i += 1 }
    val xorPath = new Array[Int](n)

    def dfs(u: Int): Unit = {
      xorPath(u) ^= vals(u)
      val it = g(u).iterator()
      while (it.hasNext) {
        val v = it.next()
        xorPath(v) = xorPath(u)
        dfs(v)
      }
    }

    val inT = new Array[Int](n)
    val outT = new Array[Int](n)
    val order = new java.util.ArrayList[Integer]()

    def dfs2(u: Int): Unit = {
      inT(u) = order.size()
      order.add(xorPath(u))
      val it = g(u).iterator()
      while (it.hasNext) dfs2(it.next())
      outT(u) = order.size()
    }

    dfs(0)
    dfs2(0)
    val ans = new Array[Int](queries.length)
    i = 0
    while (i < queries.length) {
      val u = queries(i)(0)
      val k = queries(i)(1)
      val sub = new java.util.ArrayList[Integer](order.subList(inT(u), outT(u)))
      java.util.Collections.sort(sub)
      val uniq = new java.util.ArrayList[Integer]()
      val it = sub.iterator()
      while (it.hasNext) {
        val x = it.next()
        if (uniq.isEmpty || uniq.get(uniq.size() - 1) != x) uniq.add(x)
      }
      ans(i) = if (k > uniq.size()) -1 else uniq.get(k - 1)
      i += 1
    }
    ans
  }
}
'''

FILES["3591_check_if_any_element_has_prime_frequency"] = r'''// LeetCode 3591 - Check if Any Element Has Prime Frequency
// https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

object Solution {
  def isPrime(x: Int): Boolean = {
    if (x < 2) return false
    var i = 2
    while (i * i <= x) {
      if (x % i == 0) return false
      i += 1
    }
    true
  }

  def checkPrimeFrequency(nums: Array[Int]): Boolean = {
    val cnt = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) cnt(x) = cnt.getOrElse(x, 0) + 1
    for ((_, v) <- cnt) if (isPrime(v)) return true
    false
  }
}
'''

FILES["3592_inverse_coin_change"] = r'''// LeetCode 3592 - Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/

object Solution {
  def findCoins(numWays: Array[Int]): Array[Int] = {
    val n = numWays.length
    val dp = new Array[Int](n + 1)
    val coins = new java.util.ArrayList[Integer]()
    dp(0) = 1
    var amt = 1
    while (amt <= n) {
      val ways = numWays(amt - 1)
      if (dp(amt) != ways) {
        if (dp(amt) + 1 == ways) {
          coins.add(amt)
          var x = amt
          while (x <= n) { dp(x) += dp(x - amt); x += 1 }
          if (dp(amt) != ways) return Array.empty[Int]
        } else return Array.empty[Int]
      }
      amt += 1
    }
    val out = new Array[Int](coins.size())
    var t = 0
    while (t < coins.size()) { out(t) = coins.get(t); t += 1 }
    out
  }
}
'''

n = 0
for folder, content in FILES.items():
    (ROOT / folder / "Solution.scala").write_text(content, encoding="utf-8")
    n += 1
    print("wrote", folder)
print("TOTAL", n)
