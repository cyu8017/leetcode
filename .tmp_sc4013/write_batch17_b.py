#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3423_maximum_difference_between_adjacent_elements_in_a_circular_array"] = r'''// LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
// https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

object Solution {
  def maxAdjacentDistance(nums: Array[Int]): Int = {
    var ans = 0
    val n = nums.length
    var i = 0
    while (i < n) {
      val d = math.abs(nums(i) - nums((i + 1) % n))
      if (d > ans) ans = d
      i += 1
    }
    ans
  }
}
'''

FILES["3424_minimum_cost_to_make_arrays_identical"] = r'''// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

object Solution {
  def minCost(arr: Array[Int], brr: Array[Int], k: Long): Long = {
    var noSwap = 0L
    var i = 0
    while (i < arr.length) {
      noSwap += math.abs(arr(i) - brr(i))
      i += 1
    }
    java.util.Arrays.sort(arr)
    java.util.Arrays.sort(brr)
    var withSwap = k
    i = 0
    while (i < arr.length) {
      withSwap += math.abs(arr(i) - brr(i))
      i += 1
    }
    if (noSwap < withSwap) noSwap else withSwap
  }
}
'''

FILES["3425_longest_special_path"] = r'''// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

object Solution {
  private var g: Array[java.util.ArrayList[Array[Int]]] = _
  private var nums: Array[Int] = _
  private var bestLen = 0
  private var bestNodes = 0
  private val last = new java.util.HashMap[Integer, Integer]()

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
    last.clear()
    val path = new java.util.ArrayList[Integer]()
    dfs(0, -1, 0, 0, path)
    Array(bestLen, bestNodes)
  }

  private def dfs(u: Int, p: Int, dist: Int, left: Int, path: java.util.ArrayList[Integer]): Unit = {
    var prevPos = -1
    val seen = last.containsKey(nums(u))
    if (seen) prevPos = last.get(nums(u))
    last.put(nums(u), path.size())
    var newLeft = left
    if (seen && prevPos >= left) newLeft = prevPos + 1
    path.add(dist)
    val length = dist - path.get(newLeft)
    val nodes = path.size() - newLeft
    if (length > bestLen || (length == bestLen && nodes < bestNodes)) {
      bestLen = length
      bestNodes = nodes
    }
    val it = g(u).iterator()
    while (it.hasNext) {
      val e = it.next()
      if (e(0) != p) dfs(e(0), u, dist + e(1), newLeft, path)
    }
    path.remove(path.size() - 1)
    if (seen) last.put(nums(u), prevPos)
    else last.remove(nums(u))
  }
}
'''

FILES["3426_manhattan_distances_of_all_arrangements_of_pieces"] = r'''// LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

object Solution {
  private def modPow(a0: Long, e0: Long, mod: Int): Long = {
    var a = a0 % mod
    var e = e0
    var r = 1L
    while (e > 0) {
      if ((e & 1) != 0) r = r * a % mod
      a = a * a % mod
      e >>= 1
    }
    r
  }

  private def comb(n: Int, k: Int, mod: Int): Int = {
    if (k < 0 || k > n) return 0
    var num = 1L
    var den = 1L
    var i = 0
    while (i < k) {
      num = num * (n - i) % mod
      den = den * (i + 1) % mod
      i += 1
    }
    (num * modPow(den, mod - 2, mod) % mod).toInt
  }

  def distanceSum(m: Int, n: Int, k: Int): Int = {
    val mod = 1000000007
    if (k < 2) return 0
    val totalCells = m * n
    val pairChoose = comb(totalCells - 2, k - 2, mod)
    var sumDist = 0L
    var d = 1
    while (d < m) {
      sumDist += d.toLong * (m - d) * n * n
      d += 1
    }
    d = 1
    while (d < n) {
      sumDist += d.toLong * (n - d) * m * m
      d += 1
    }
    (sumDist % mod * pairChoose % mod).toInt
  }
}
'''

FILES["3427_sum_of_variable_length_subarrays"] = r'''// LeetCode 3427 - Sum of Variable Length Subarrays
// https://leetcode.com/problems/sum-of-variable-length-subarrays/

object Solution {
  def subarraySum(nums: Array[Int]): Int = {
    val n = nums.length
    val pref = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + nums(i)
      i += 1
    }
    var ans = 0
    i = 0
    while (i < n) {
      var start = i - nums(i)
      if (start < 0) start = 0
      ans += pref(i + 1) - pref(start)
      i += 1
    }
    ans
  }
}
'''

FILES["3428_maximum_and_minimum_sums_of_at_most_size_k_subsequences"] = r'''// LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

object Solution {
  def minMaxSums(nums: Array[Int], k: Int): Int = {
    val mod = 1000000007
    java.util.Arrays.sort(nums)
    val n = nums.length
    val C = Array.ofDim[Int](n + 1, k)
    var i = 0
    while (i <= n) {
      C(i)(0) = 1
      var j = 1
      while (j < k && j <= i) {
        C(i)(j) = (C(i - 1)(j) + C(i - 1)(j - 1)) % mod
        j += 1
      }
      i += 1
    }
    var ans = 0
    i = 0
    while (i < n) {
      var waysMax = 0
      var j = 0
      while (j < k && j <= i) {
        waysMax = (waysMax + C(i)(j)) % mod
        j += 1
      }
      var waysMin = 0
      val right = n - i - 1
      j = 0
      while (j < k && j <= right) {
        waysMin = (waysMin + C(right)(j)) % mod
        j += 1
      }
      ans = ((ans + nums(i).toLong * waysMax % mod + nums(i).toLong * waysMin % mod) % mod).toInt
      i += 1
    }
    ans
  }
}
'''

FILES["3429_paint_house_iv"] = r'''// LeetCode 3429 - Paint House IV
// https://leetcode.com/problems/paint-house-iv/

object Solution {
  def minCost(n: Int, cost: Array[Array[Int]]): Long = {
    val inf = 1L << 60
    val m = n / 2
    val dp = Array.ofDim[Long](3, 3)
    var a = 0
    while (a < 3) {
      var b = 0
      while (b < 3) {
        dp(a)(b) = if (a == b) inf else cost(0)(a).toLong + cost(n - 1)(b)
        b += 1
      }
      a += 1
    }
    var i = 1
    while (i < m) {
      val ndp = Array.fill(3, 3)(inf)
      var pa = 0
      while (pa < 3) {
        var pb = 0
        while (pb < 3) {
          if (dp(pa)(pb) < inf) {
            a = 0
            while (a < 3) {
              if (a != pa) {
                var b = 0
                while (b < 3) {
                  if (!(b == pb || a == b)) {
                    val v = dp(pa)(pb) + cost(i)(a) + cost(n - 1 - i)(b)
                    if (v < ndp(a)(b)) ndp(a)(b) = v
                  }
                  b += 1
                }
              }
              a += 1
            }
          }
          pb += 1
        }
        pa += 1
      }
      a = 0
      while (a < 3) {
        var b = 0
        while (b < 3) {
          dp(a)(b) = ndp(a)(b)
          b += 1
        }
        a += 1
      }
      i += 1
    }
    var ans = inf
    a = 0
    while (a < 3) {
      var b = 0
      while (b < 3) {
        if (dp(a)(b) < ans) ans = dp(a)(b)
        b += 1
      }
      a += 1
    }
    ans
  }
}
'''

FILES["3430_maximum_and_minimum_sums_of_at_most_size_k_subarrays"] = r'''// LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

object Solution {
  def minMaxSubarraySum(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    var ans = 0L
    var i = 0
    while (i < n) {
      var mn = nums(i)
      var mx = nums(i)
      var j = i
      while (j < n && j - i + 1 <= k) {
        if (nums(j) < mn) mn = nums(j)
        if (nums(j) > mx) mx = nums(j)
        ans += mn + mx
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3431_minimum_unlocked_indices_to_sort_nums"] = r'''// LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
// https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

object Solution {
  def minUnlockedIndices(nums: Array[Int], locked: Array[Int]): Int = {
    val n = nums.length
    var need = false
    var i = 1
    while (i < n) {
      if (nums(i) < nums(i - 1)) { need = true; i = n }
      else i += 1
    }
    if (!need) return 0
    var left = n
    var right = -1
    i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        if (nums(i) > nums(j)) {
          if (i < left) left = i
          if (j > right) right = j
        }
        j += 1
      }
      i += 1
    }
    if (right < left) return 0
    var ans = 0
    i = left
    while (i <= right) {
      if (locked(i) == 1) ans += 1
      i += 1
    }
    val tmp = nums.clone()
    val lock = locked.clone()
    i = left
    while (i <= right) {
      lock(i) = 0
      i += 1
    }
    var changed = true
    while (changed) {
      changed = false
      i = 0
      while (i + 1 < n) {
        if (lock(i) == 0 && lock(i + 1) == 0 && tmp(i) > tmp(i + 1)) {
          val t = tmp(i); tmp(i) = tmp(i + 1); tmp(i + 1) = t
          changed = true
        }
        i += 1
      }
    }
    i = 1
    while (i < n) {
      if (tmp(i) < tmp(i - 1)) return -1
      i += 1
    }
    ans
  }
}
'''

FILES["3432_count_partitions_with_even_sum_difference"] = r'''// LeetCode 3432 - Count Partitions with Even Sum Difference
// https://leetcode.com/problems/count-partitions-with-even-sum-difference/

object Solution {
  def countPartitions(nums: Array[Int]): Int = {
    var total = 0
    nums.foreach(x => total += x)
    var ans = 0
    var left = 0
    var i = 0
    while (i < nums.length - 1) {
      left += nums(i)
      if ((left - (total - left)) % 2 == 0) ans += 1
      i += 1
    }
    ans
  }
}
'''

FILES["3433_count_mentions_per_user"] = r'''// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

object Solution {
  def countMentions(numberOfUsers: Int, events: List[List[String]]): Array[Int] = {
    val ev = events.sortWith { (a, b) =>
      val ti = a(1).toInt
      val tj = b(1).toInt
      if (ti != tj) ti < tj
      else a(0).compareTo(b(0)) > 0
    }
    val online = Array.fill(numberOfUsers)(true)
    val offlineUntil = new Array[Int](numberOfUsers)
    val ans = new Array[Int](numberOfUsers)
    ev.foreach { e =>
      val t = e(1).toInt
      var i = 0
      while (i < numberOfUsers) {
        if (!online(i) && offlineUntil(i) <= t) online(i) = true
        i += 1
      }
      if (e(0) == "OFFLINE") {
        val id = e(2).toInt
        online(id) = false
        offlineUntil(id) = t + 60
      } else {
        val msg = e(2)
        if (msg == "ALL") {
          i = 0
          while (i < numberOfUsers) { ans(i) += 1; i += 1 }
        } else if (msg == "HERE") {
          i = 0
          while (i < numberOfUsers) { if (online(i)) ans(i) += 1; i += 1 }
        } else {
          msg.split(" ").foreach { part =>
            val id = part.substring(2).toInt
            ans(id) += 1
          }
        }
      }
    }
    ans
  }
}
'''

FILES["3434_maximum_frequency_after_subarray_operation"] = r'''// LeetCode 3434 - Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

object Solution {
  def maxFrequency(nums: Array[Int], k: Int): Int = {
    var base = 0
    nums.foreach { x => if (x == k) base += 1 }
    var ans = base
    val uniq = scala.collection.mutable.Set.empty[Int]
    nums.foreach(x => uniq += x)
    uniq.foreach { v =>
      if (v != k) {
        var best = 0
        var cur = 0
        nums.foreach { x =>
          var delta = 0
          if (x == v) delta = 1
          else if (x == k) delta = -1
          cur += delta
          if (cur < 0) cur = 0
          if (cur > best) best = cur
        }
        if (base + best > ans) ans = base + best
      }
    }
    ans
  }
}
'''

FILES["3435_frequencies_of_shortest_supersequences"] = r'''// LeetCode 3435 - Frequencies of Shortest Supersequences
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/

object Solution {
  private var words: Array[String] = _
  private var letters: Array[Int] = _
  private var m = 0
  private var best = 0
  private val freq = new Array[Int](26)
  private var bestFreqs: java.util.ArrayList[Array[Int]] = _

  def supersequences(words0: Array[String]): List[List[Int]] = {
    words = words0
    val used = Array.fill(26)(false)
    words.foreach { w =>
      used(w.charAt(0) - 'a') = true
      used(w.charAt(1) - 'a') = true
    }
    val lettersList = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < 26) {
      if (used(i)) lettersList += i
      i += 1
    }
    m = lettersList.length
    letters = lettersList.toArray
    best = 1000000000
    bestFreqs = new java.util.ArrayList[Array[Int]]()
    i = 0
    while (i < 26) { freq(i) = 0; i += 1 }
    dfs(0)
    val res = scala.collection.mutable.ListBuffer.empty[List[Int]]
    val it = bestFreqs.iterator()
    while (it.hasNext) {
      val f = it.next()
      res += f.toList
    }
    res.toList
  }

  private def dfs(i: Int): Unit = {
    if (i == m) {
      words.foreach { w =>
        val a = w.charAt(0) - 'a'
        val b = w.charAt(1) - 'a'
        if (a == b) {
          if (freq(a) < 2) return
        } else if (freq(a) < 1 || freq(b) < 1) return
      }
      var sum = 0
      val f = new Array[Int](26)
      var j = 0
      while (j < 26) { f(j) = freq(j); sum += freq(j); j += 1 }
      if (sum < best) {
        best = sum
        bestFreqs = new java.util.ArrayList[Array[Int]]()
        bestFreqs.add(f)
      } else if (sum == best) bestFreqs.add(f)
      return
    }
    val L = letters(i)
    var c = 1
    while (c <= 2) {
      freq(L) = c
      dfs(i + 1)
      c += 1
    }
    freq(L) = 0
  }
}
'''

FILES["3437_permutations_iii"] = r'''// LeetCode 3437 - Permutations III
// https://leetcode.com/problems/permutations-iii/

object Solution {
  def permute(n: Int): Array[Array[Int]] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    val used = new Array[Boolean](n + 1)
    val cur = scala.collection.mutable.ArrayBuffer.empty[Int]
    dfs(n, used, cur, ans)
    ans.toArray
  }

  private def dfs(n: Int, used: Array[Boolean], cur: scala.collection.mutable.ArrayBuffer[Int], ans: scala.collection.mutable.ArrayBuffer[Array[Int]]): Unit = {
    if (cur.length == n) {
      ans += cur.toArray
      return
    }
    var i = 1
    while (i <= n) {
      if (!used(i) && (cur.isEmpty || cur.last % 2 != i % 2)) {
        used(i) = true
        cur += i
        dfs(n, used, cur, ans)
        cur.remove(cur.length - 1)
        used(i) = false
      }
      i += 1
    }
  }
}
'''

FILES["3438_find_valid_pair_of_adjacent_digits_in_string"] = r'''// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

object Solution {
  def findValidPair(s: String): String = {
    val freq = new Array[Int](10)
    s.foreach { c => freq(c - '0') += 1 }
    var i = 0
    while (i + 1 < s.length) {
      val a = s.charAt(i) - '0'
      val b = s.charAt(i + 1) - '0'
      if (a != b && freq(a) == a && freq(b) == b) return s.substring(i, i + 2)
      i += 1
    }
    ""
  }
}
'''

FILES["3439_reschedule_meetings_for_maximum_free_time_i"] = r'''// LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

object Solution {
  def maxFreeTime(eventTime: Int, k: Int, startTime: Array[Int], endTime: Array[Int]): Int = {
    val n = startTime.length
    val gaps = new Array[Int](n + 1)
    gaps(0) = startTime(0)
    var i = 1
    while (i < n) {
      gaps(i) = startTime(i) - endTime(i - 1)
      i += 1
    }
    gaps(n) = eventTime - endTime(n - 1)
    val window = k + 1
    var sum = 0
    i = 0
    while (i < window && i < gaps.length) {
      sum += gaps(i)
      i += 1
    }
    var ans = sum
    i = window
    while (i < gaps.length) {
      sum += gaps(i) - gaps(i - window)
      if (sum > ans) ans = sum
      i += 1
    }
    ans
  }
}
'''

FILES["3440_reschedule_meetings_for_maximum_free_time_ii"] = r'''// LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

object Solution {
  def maxFreeTime(eventTime: Int, startTime: Array[Int], endTime: Array[Int]): Int = {
    val n = startTime.length
    val gaps = new Array[Int](n + 1)
    gaps(0) = startTime(0)
    var i = 1
    while (i < n) {
      gaps(i) = startTime(i) - endTime(i - 1)
      i += 1
    }
    gaps(n) = eventTime - endTime(n - 1)
    var ans = 0
    gaps.foreach { g => if (g > ans) ans = g }
    val leftMax = new Array[Int](n + 1)
    val rightMax = new Array[Int](n + 1)
    i = 0
    while (i <= n) {
      leftMax(i) = gaps(i)
      if (i > 0 && leftMax(i - 1) > leftMax(i)) leftMax(i) = leftMax(i - 1)
      i += 1
    }
    i = n
    while (i >= 0) {
      rightMax(i) = gaps(i)
      if (i < n && rightMax(i + 1) > rightMax(i)) rightMax(i) = rightMax(i + 1)
      i -= 1
    }
    i = 0
    while (i < n) {
      val dur = endTime(i) - startTime(i)
      val merged = gaps(i) + gaps(i + 1)
      var bestOther = 0
      if (i > 0 && leftMax(i - 1) > bestOther) bestOther = leftMax(i - 1)
      if (i + 2 <= n && rightMax(i + 2) > bestOther) bestOther = rightMax(i + 2)
      var cand = merged
      if (bestOther >= dur) cand = merged + dur
      if (cand > ans) ans = cand
      i += 1
    }
    ans
  }
}
'''

FILES["3441_minimum_cost_good_caption"] = r'''// LeetCode 3441 - Minimum Cost Good Caption
// https://leetcode.com/problems/minimum-cost-good-caption/

object Solution {
  def minCostGoodCaption(caption: String): String = {
    val n = caption.length
    if (n < 3) return ""
    val ans = caption.toCharArray
    var i = 0
    while (i < n) {
      var j = i
      while (j < n && ans(j) == ans(i)) j += 1
      if (j - i >= 3) i = j
      else {
        val need = 3 - (j - i)
        if (j + need <= n) {
          var t = 0
          while (t < need) { ans(j + t) = ans(i); t += 1 }
          i = j + need
        } else {
          var ch = 'a'
          if (i > 0) ch = ans(i - 1)
          else if (j < n) ch = caption.charAt(j)
          var t = i
          while (t < n) { ans(t) = ch; t += 1 }
          i = n
        }
      }
    }
    i = 0
    while (i < n) {
      var j = i
      while (j < n && ans(j) == ans(i)) j += 1
      if (j - i < 3) return ""
      i = j
    }
    new String(ans)
  }
}
'''

FILES["3442_maximum_difference_between_even_and_odd_frequency_i"] = r'''// LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

object Solution {
  def maxDifference(s: String): Int = {
    val freq = new Array[Int](26)
    s.foreach { c => freq(c - 'a') += 1 }
    var maxOdd = 0
    var minEven = 1000000000
    freq.foreach { f =>
      if (f != 0) {
        if (f % 2 == 1) {
          if (f > maxOdd) maxOdd = f
        } else if (f < minEven) minEven = f
      }
    }
    maxOdd - minEven
  }
}
'''

FILES["3443_maximum_manhattan_distance_after_k_changes"] = r'''// LeetCode 3443 - Maximum Manhattan Distance After K Changes
// https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

object Solution {
  def maxDistance(s: String, k: Int): Int = {
    var ans = 0
    var lat = 0
    var lon = 0
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i)
      if (c == 'N') lat += 1
      else if (c == 'S') lat -= 1
      else if (c == 'E') lon += 1
      else lon -= 1
      val md = math.abs(lat) + math.abs(lon)
      val steps = i + 1
      var cur = md + 2 * k
      if (cur > steps) cur = steps
      if (cur > ans) ans = cur
      i += 1
    }
    ans
  }
}
'''

FILES["3444_minimum_increments_for_target_multiples_in_an_array"] = r'''// LeetCode 3444 - Minimum Increments for Target Multiples in an Array
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

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
  private def lcm(a: Int, b: Int): Int = a / gcd(a, b) * b

  def minimumIncrements(nums: Array[Int], target: Array[Int]): Int = {
    val m = target.length
    val N = 1 << m
    val inf = 1e18.toLong
    var dp = Array.fill(N)(inf)
    dp(0) = 0
    nums.foreach { x =>
      val ndp = dp.clone()
      var mask = 0
      while (mask < N) {
        var sub = 1
        while (sub < N) {
          var L = 1
          var ok = true
          var i = 0
          while (i < m && ok) {
            if ((sub & (1 << i)) != 0) {
              L = lcm(L, target(i))
              if (L > 1000000000) ok = false
            }
            i += 1
          }
          if (ok) {
            val cost = (L - x % L) % L
            val nmask = mask | sub
            if (dp(mask) + cost < ndp(nmask)) ndp(nmask) = dp(mask) + cost
          }
          sub += 1
        }
        mask += 1
      }
      dp = ndp
    }
    dp(N - 1).toInt
  }
}
'''

FILES["3445_maximum_difference_between_even_and_odd_frequency_ii"] = r'''// LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

object Solution {
  def maxDifference(s: String, k: Int): Int = {
    val n = s.length
    var ans = -1000000000
    var a = 0
    while (a < 5) {
      var b = 0
      while (b < 5) {
        if (a != b) {
          val prefA = new Array[Int](n + 1)
          val prefB = new Array[Int](n + 1)
          var i = 0
          while (i < n) {
            prefA(i + 1) = prefA(i)
            prefB(i + 1) = prefB(i)
            if (s.charAt(i) - '0' == a) prefA(i + 1) += 1
            if (s.charAt(i) - '0' == b) prefB(i + 1) += 1
            i += 1
          }
          i = 0
          while (i < n) {
            var j = i + k - 1
            while (j < n) {
              val fa = prefA(j + 1) - prefA(i)
              val fb = prefB(j + 1) - prefB(i)
              if (fa % 2 == 1 && fb % 2 == 0 && fb > 0) {
                if (fa - fb > ans) ans = fa - fb
              }
              j += 1
            }
            i += 1
          }
        }
        b += 1
      }
      a += 1
    }
    ans
  }
}
'''

FILES["3446_sort_matrix_by_diagonals"] = r'''// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

object Solution {
  def sortMatrix(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val n = grid.length
    val diags = scala.collection.mutable.Map.empty[Int, java.util.ArrayList[Integer]]
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        val list = diags.getOrElseUpdate(i - j, new java.util.ArrayList[Integer]())
        list.add(grid(i)(j))
        j += 1
      }
      i += 1
    }
    diags.foreach { case (key, value) =>
      if (key >= 0) java.util.Collections.sort(value, java.util.Collections.reverseOrder[Integer]())
      else java.util.Collections.sort(value)
    }
    val idx = scala.collection.mutable.Map.empty[Int, Int]
    i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        val k = i - j
        val pos = idx.getOrElse(k, 0)
        grid(i)(j) = diags(k).get(pos)
        idx(k) = pos + 1
        j += 1
      }
      i += 1
    }
    grid
  }
}
'''

FILES["3447_assign_elements_to_groups_with_constraints"] = r'''// LeetCode 3447 - Assign Elements to Groups with Constraints
// https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

object Solution {
  def assignElements(groups: Array[Int], elements: Array[Int]): Array[Int] = {
    val maxV = 100001
    val first = Array.fill(maxV)(-1)
    var i = 0
    while (i < elements.length) {
      val e = elements(i)
      if (e < maxV && first(e) == -1) first(e) = i
      i += 1
    }
    val ans = new Array[Int](groups.length)
    var gi = 0
    while (gi < groups.length) {
      val g = groups(gi)
      var best = -1
      var d = 1
      while (d.toLong * d <= g) {
        if (g % d == 0) {
          if (first(d) != -1 && (best == -1 || first(d) < best)) best = first(d)
          val other = g / d
          if (first(other) != -1 && (best == -1 || first(other) < best)) best = first(other)
        }
        d += 1
      }
      ans(gi) = best
      gi += 1
    }
    ans
  }
}
'''

FILES["3448_count_substrings_divisible_by_last_digit"] = r'''// LeetCode 3448 - Count Substrings Divisible By Last Digit
// https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

object Solution {
  def countSubstrings(s: String): Long = {
    var ans = 0L
    val n = s.length
    var r = 0
    while (r < n) {
      val last = s.charAt(r) - '0'
      if (last != 0) {
        var mod = 0
        var p = 1 % last
        var l = r
        while (l >= 0) {
          mod = (mod + (s.charAt(l) - '0') * p) % last
          p = (p * 10) % last
          if (mod == 0) ans += 1
          l -= 1
        }
      }
      r += 1
    }
    ans
  }
}
'''

FILES["3449_maximize_the_minimum_game_score"] = r'''// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

object Solution {
  def maxScore(points: Array[Int], m: Int): Long = {
    var lo = 0L
    var hi = 1e18.toLong
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(points, m, mid)) lo = mid
      else hi = mid - 1
    }
    lo
  }

  private def ok(points: Array[Int], m: Int, mid: Long): Boolean = {
    var need = 0L
    var extra = 0L
    points.foreach { p =>
      val req = (mid + p - 1) / p
      if (req > extra) {
        val visits = req - extra
        need += 2 * visits - 1
        extra = visits - 1
      } else {
        need += 1
        extra = 0
      }
      if (need > m) return false
    }
    need <= m
  }
}
'''

for folder, text in FILES.items():
    path = ROOT / folder / "Solution.scala"
    path.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", folder)
print("count", len(FILES))
