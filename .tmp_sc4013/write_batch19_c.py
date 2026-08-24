#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3674_minimum_operations_to_equalize_array"] = r'''// LeetCode 3674 - Minimum Operations to Equalize Array
// https://leetcode.com/problems/minimum-operations-to-equalize-array/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    for (x <- nums) if (x != nums(0)) return 1
    0
  }
}
'''

FILES["3675_minimum_operations_to_transform_string"] = r'''// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

object Solution {
  def minOperations(s: String): Int = {
    var ans = 0
    for (c <- s) {
      if (c != 'a') ans = math.max(ans, 26 - (c - 'a'))
    }
    ans
  }
}
'''

FILES["3676_count_bowl_subarrays"] = r'''// LeetCode 3676 - Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/

object Solution {
  def bowlSubarrays(nums: Array[Int]): Long = {
    val n = nums.length
    var ans = 0L
    val ngr = Array.fill(n)(-1)
    val ngl = Array.fill(n)(-1)
    val stack = new java.util.ArrayList[Integer]()
    var i = n - 1
    while (i >= 0) {
      while (!stack.isEmpty && nums(stack.get(stack.size() - 1)) < nums(i))
        stack.remove(stack.size() - 1)
      if (!stack.isEmpty) ngr(i) = stack.get(stack.size() - 1)
      stack.add(i)
      i -= 1
    }
    stack.clear()
    i = 0
    while (i < n) {
      while (!stack.isEmpty && nums(stack.get(stack.size() - 1)) < nums(i))
        stack.remove(stack.size() - 1)
      if (!stack.isEmpty) ngl(i) = stack.get(stack.size() - 1)
      stack.add(i)
      i += 1
    }
    i = 0
    while (i < n) {
      if (ngr(i) != -1 && ngr(i) - i >= 2) ans += 1
      if (ngl(i) != -1 && i - ngl(i) >= 2) ans += 1
      i += 1
    }
    ans
  }
}
'''

FILES["3677_count_binary_palindromic_numbers"] = r'''// LeetCode 3677 - Count Binary Palindromic Numbers
// https://leetcode.com/problems/count-binary-palindromic-numbers/

object Solution {
  def countBinaryPalindromes(n: Long): Int = {
    if (n == 0) return 1
    var ans = 1
    val sb = new StringBuilder
    var x = n
    while (x > 0) {
      sb.append(('0' + (x & 1).toInt).toChar)
      x >>= 1
    }
    val s = sb.reverse().toString
    val L = s.length
    var len = 1
    while (len < L) {
      val half = (len + 1) / 2
      ans += 1 << (half - 1)
      len += 1
    }
    val half = (L + 1) / 2
    val prefix = s.substring(0, half)
    val start = 1 << (half - 1)
    var prefVal = 0L
    for (c <- prefix) prefVal = (prefVal << 1) | (c - '0')
    ans += (prefVal - start).toInt
    val pal = new StringBuilder(prefix)
    var i = half - 1 - (L % 2)
    while (i >= 0) {
      pal.append(prefix.charAt(i))
      i -= 1
    }
    var pval = 0L
    for (c <- pal.toString) pval = (pval << 1) | (c - '0')
    if (pval <= n) ans += 1
    ans
  }
}
'''

FILES["3678_smallest_absent_positive_greater_than_average"] = r'''// LeetCode 3678 - Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

object Solution {
  def smallestAbsent(nums: Array[Int]): Int = {
    val s = new java.util.HashSet[Integer]()
    var sum = 0
    for (x <- nums) {
      s.add(x)
      sum += x
    }
    var ans = math.max(1, sum / nums.length + 1)
    while (s.contains(ans)) ans += 1
    ans
  }
}
'''

FILES["3679_minimum_discards_to_balance_inventory"] = r'''// LeetCode 3679 - Minimum Discards to Balance Inventory
// https://leetcode.com/problems/minimum-discards-to-balance-inventory/

object Solution {
  def minArrivalsToDiscard(arrivals: Array[Int], w: Int, m: Int): Int = {
    val cnt = new java.util.HashMap[Integer, Integer]()
    val n = arrivals.length
    val marked = new Array[Int](n)
    var ans = 0
    var i = 0
    while (i < n) {
      val x = arrivals(i)
      if (i >= w) cnt.merge(arrivals(i - w), -marked(i - w), Integer.sum)
      if (cnt.getOrDefault(x, 0) >= m) ans += 1
      else {
        marked(i) = 1
        cnt.merge(x, 1, Integer.sum)
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3680_generate_schedule"] = r'''// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

object Solution {
  def generateSchedule(n: Int): Array[Array[Int]] = {
    if (n < 5) return Array.empty[Array[Int]]
    val matches = new java.util.ArrayList[Array[Int]]()
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (i != j) matches.add(Array(i, j))
        j += 1
      }
      i += 1
    }
    val used = Array.fill(matches.size())(false)
    val sched = new java.util.ArrayList[Array[Int]]()
    var last0 = -1
    var last1 = -1

    def dfs(): Boolean = {
      if (sched.size() == matches.size()) return true
      var ii = 0
      while (ii < matches.size()) {
        if (!used(ii)) {
          val m = matches.get(ii)
          if (!(m(0) == last0 || m(0) == last1 || m(1) == last0 || m(1) == last1)) {
            used(ii) = true
            sched.add(m)
            val p0 = last0
            val p1 = last1
            last0 = m(0)
            last1 = m(1)
            if (dfs()) return true
            last0 = p0
            last1 = p1
            sched.remove(sched.size() - 1)
            used(ii) = false
          }
        }
        ii += 1
      }
      false
    }

    if (dfs()) {
      val res = new Array[Array[Int]](sched.size())
      i = 0
      while (i < sched.size()) {
        res(i) = sched.get(i)
        i += 1
      }
      res
    } else Array.empty[Array[Int]]
  }
}
'''

FILES["3681_maximum_xor_of_subsequences"] = r'''// LeetCode 3681 - Maximum XOR of Subsequences
// https://leetcode.com/problems/maximum-xor-of-subsequences/

object Solution {
  def maxXorSubsequences(nums: Array[Int]): Int = {
    val basis = new Array[Int](32)
    for (x <- nums) {
      var cur = x
      var b = 31
      var placed = false
      while (b >= 0 && !placed) {
        if ((cur & (1 << b)) != 0) {
          if (basis(b) == 0) {
            basis(b) = cur
            placed = true
          } else cur ^= basis(b)
        }
        if (!placed) b -= 1
      }
    }
    var ans = 0
    var b = 31
    while (b >= 0) {
      if ((ans ^ basis(b)) > ans) ans ^= basis(b)
      b -= 1
    }
    ans
  }
}
'''

FILES["3682_minimum_index_sum_of_common_elements"] = r'''// LeetCode 3682 - Minimum Index Sum of Common Elements
// https://leetcode.com/problems/minimum-index-sum-of-common-elements/

object Solution {
  def minimumSum(nums1: Array[Int], nums2: Array[Int]): Int = {
    val inf = 1 << 30
    val d = new java.util.HashMap[Integer, Integer]()
    var i = 0
    while (i < nums2.length) {
      d.putIfAbsent(nums2(i), i)
      i += 1
    }
    var ans = inf
    i = 0
    while (i < nums1.length) {
      val j = d.get(nums1(i))
      if (j != null) ans = math.min(ans, i + j.intValue())
      i += 1
    }
    if (ans == inf) -1 else ans
  }
}
'''

FILES["3683_earliest_time_to_finish_one_task"] = r'''// LeetCode 3683 - Earliest Time to Finish One Task
// https://leetcode.com/problems/earliest-time-to-finish-one-task/

object Solution {
  def earliestTime(tasks: Array[Array[Int]]): Int = {
    var ans = 200
    for (task <- tasks) ans = math.min(ans, task(0) + task(1))
    ans
  }
}
'''

FILES["3684_maximize_sum_of_at_most_k_distinct_elements"] = r'''// LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
// https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

object Solution {
  def maxKDistinct(nums: Array[Int], k0: Int): Array[Int] = {
    java.util.Arrays.sort(nums)
    val n = nums.length
    val ans = new java.util.ArrayList[Integer]()
    var k = k0
    var i = n - 1
    var stop = false
    while (i >= 0 && !stop) {
      if (!(i + 1 < n && nums(i) == nums(i + 1))) {
        ans.add(nums(i))
        k -= 1
        if (k == 0) stop = true
      }
      i -= 1
    }
    val res = new Array[Int](ans.size())
    i = 0
    while (i < ans.size()) {
      res(i) = ans.get(i)
      i += 1
    }
    res
  }
}
'''

FILES["3685_subsequence_sum_after_capping_elements"] = r'''// LeetCode 3685 - Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/

object Solution {
  def subsequenceSumAfterCapping(nums: Array[Int], k: Int): Array[Boolean] = {
    val n = nums.length
    val sorted = nums.clone()
    java.util.Arrays.sort(sorted)
    val ans = new Array[Boolean](n)
    val reach = new Array[Boolean](k + 1)
    reach(0) = true
    var idx = 0
    var x = 1
    while (x <= n) {
      while (idx < n && sorted(idx) <= x) {
        val v = sorted(idx)
        var s = k
        while (s >= v) {
          if (reach(s - v)) reach(s) = true
          s -= 1
        }
        idx += 1
      }
      val tmp = reach.clone()
      val rem = n - idx
      var s = 0
      while (s <= k) {
        if (reach(s)) {
          var t = 1
          while (t <= rem && s + t * x <= k) {
            tmp(s + t * x) = true
            t += 1
          }
        }
        s += 1
      }
      ans(x - 1) = tmp(k)
      x += 1
    }
    ans
  }
}
'''

FILES["3686_number_of_stable_subsequences"] = r'''// LeetCode 3686 - Number of Stable Subsequences
// https://leetcode.com/problems/number-of-stable-subsequences/

object Solution {
  def countStableSubsequences(nums: Array[Int]): Int = {
    val MOD = 1000000007
    var a1 = 0
    var a2 = 0
    var b1 = 0
    var b2 = 0
    for (x <- nums) {
      if (x % 2 == 1) {
        val na1 = (1 + b1 + b2) % MOD
        val na2 = a1
        a1 = (a1 + na1) % MOD
        a2 = (a2 + na2) % MOD
      } else {
        val nb1 = (1 + a1 + a2) % MOD
        val nb2 = b1
        b1 = (b1 + nb1) % MOD
        b2 = (b2 + nb2) % MOD
      }
    }
    (((a1 + a2) % MOD + b1) % MOD + b2) % MOD
  }
}
'''

FILES["3687_library_late_fee_calculator"] = r'''// LeetCode 3687 - Library Late Fee Calculator
// https://leetcode.com/problems/library-late-fee-calculator/

object Solution {
  private def fee(x: Int): Int = {
    if (x == 1) 1
    else if (x > 5) 3 * x
    else 2 * x
  }

  def lateFee(daysLate: Array[Int]): Int = {
    var ans = 0
    for (x <- daysLate) ans += fee(x)
    ans
  }
}
'''

FILES["3688_bitwise_or_of_even_numbers_in_an_array"] = r'''// LeetCode 3688 - Bitwise OR of Even Numbers in an Array
// https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

object Solution {
  def evenNumberBitwiseORs(nums: Array[Int]): Int = {
    var ans = 0
    for (x <- nums) if (x % 2 == 0) ans |= x
    ans
  }
}
'''

FILES["3689_maximum_total_subarray_value_i"] = r'''// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

object Solution {
  def maxTotalValue(nums: Array[Int], k: Int): Long = {
    var mn = nums(0)
    var mx = nums(0)
    for (x <- nums) {
      mn = math.min(mn, x)
      mx = math.max(mx, x)
    }
    1L * k * (mx - mn)
  }
}
'''

FILES["3690_split_and_merge_array_transformation"] = r'''// LeetCode 3690 - Split and Merge Array Transformation
// https://leetcode.com/problems/split-and-merge-array-transformation/

object Solution {
  def minSplitMerge(nums1: Array[Int], nums2: Array[Int]): Int = {
    val n = nums1.length

    def toArr(nums: java.util.List[Integer]): Array[Int] = {
      val t = new Array[Int](6)
      var i = 0
      while (i < n) {
        t(i) = nums.get(i)
        i += 1
      }
      t
    }

    def key(a: Array[Int]): String = java.util.Arrays.toString(a)

    val startL = new java.util.ArrayList[Integer]()
    val targetL = new java.util.ArrayList[Integer]()
    var i = 0
    while (i < n) {
      startL.add(nums1(i))
      targetL.add(nums2(i))
      i += 1
    }
    val start = toArr(startL)
    val target = toArr(targetL)
    val vis = new java.util.HashSet[String]()
    vis.add(key(start))
    var q = new java.util.ArrayList[Array[Int]]()
    q.add(start)
    var ans = 0
    while (true) {
      val nq = new java.util.ArrayList[Array[Int]]()
      val qit = q.iterator()
      while (qit.hasNext) {
        val cur = qit.next()
        if (java.util.Arrays.equals(cur, target)) return ans
        var l = 0
        while (l < n) {
          var r = l
          while (r < n) {
            val remain = new java.util.ArrayList[Integer]()
            val sub = new java.util.ArrayList[Integer]()
            i = 0
            while (i < l) {
              remain.add(cur(i))
              i += 1
            }
            i = r + 1
            while (i < n) {
              remain.add(cur(i))
              i += 1
            }
            i = l
            while (i <= r) {
              sub.add(cur(i))
              i += 1
            }
            var pos = 0
            while (pos <= remain.size()) {
              val nxtSlice = new java.util.ArrayList[Integer]()
              nxtSlice.addAll(remain.subList(0, pos))
              nxtSlice.addAll(sub)
              nxtSlice.addAll(remain.subList(pos, remain.size()))
              val nxt = toArr(nxtSlice)
              val kk = key(nxt)
              if (!vis.contains(kk)) {
                vis.add(kk)
                nq.add(nxt)
              }
              pos += 1
            }
            r += 1
          }
          l += 1
        }
      }
      q = nq
      ans += 1
    }
    -1
  }
}
'''

FILES["3691_maximum_total_subarray_value_ii"] = r'''// LeetCode 3691 - Maximum Total Subarray Value II
// https://leetcode.com/problems/maximum-total-subarray-value-ii/

object Solution {
  private class SparseTableRMQ(data: Array[Int]) {
    val n = data.length
    var maxLog = 0
    while ((1 << maxLog) <= n) maxLog += 1
    maxLog += 1
    val fMax = Array.ofDim[Int](n, maxLog)
    val fMin = Array.ofDim[Int](n, maxLog)
    val lg = new Array[Int](n + 1)
    var i = 2
    while (i <= n) {
      lg(i) = lg(i >> 1) + 1
      i += 1
    }
    i = 0
    while (i < n) {
      fMax(i)(0) = data(i)
      fMin(i)(0) = data(i)
      i += 1
    }
    var j = 1
    while (j < maxLog) {
      i = 0
      while (i <= n - (1 << j)) {
        fMax(i)(j) = math.max(fMax(i)(j - 1), fMax(i + (1 << (j - 1)))(j - 1))
        fMin(i)(j) = math.min(fMin(i)(j - 1), fMin(i + (1 << (j - 1)))(j - 1))
        i += 1
      }
      j += 1
    }

    def queryMax(l: Int, r: Int): Int = {
      val k = lg(r - l + 1)
      math.max(fMax(l)(k), fMax(r - (1 << k) + 1)(k))
    }

    def queryMin(l: Int, r: Int): Int = {
      val k = lg(r - l + 1)
      math.min(fMin(l)(k), fMin(r - (1 << k) + 1)(k))
    }
  }

  def maxTotalValue(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val st = new SparseTableRMQ(nums)
    val pq = new java.util.PriorityQueue[Array[Long]]((a: Array[Long], b: Array[Long]) => java.lang.Long.compare(b(0), a(0)))
    var l = 0
    while (l < n) {
      val `val` = st.queryMax(l, n - 1).toLong - st.queryMin(l, n - 1)
      pq.offer(Array(`val`, l.toLong, (n - 1).toLong))
      l += 1
    }
    var ans = 0L
    var i = 0
    while (i < k) {
      val top = pq.poll()
      val v = top(0)
      val ll = top(1).toInt
      val r = top(2).toInt
      ans += v
      if (r > ll) {
        val nextVal = st.queryMax(ll, r - 1).toLong - st.queryMin(ll, r - 1)
        pq.offer(Array(nextVal, ll.toLong, (r - 1).toLong))
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3692_majority_frequency_characters"] = r'''// LeetCode 3692 - Majority Frequency Characters
// https://leetcode.com/problems/majority-frequency-characters/

object Solution {
  def majorityFrequencyGroup(s: String): String = {
    val cnt = new Array[Int](26)
    for (c <- s) cnt(c - 'a') += 1
    val f = new java.util.HashMap[Integer, StringBuilder]()
    var i = 0
    while (i < 26) {
      if (cnt(i) > 0)
        f.computeIfAbsent(cnt(i), _ => new StringBuilder).append(('a' + i).toChar)
      i += 1
    }
    var mx = 0
    var mv = 0
    var ans = ""
    val it = f.entrySet().iterator()
    while (it.hasNext) {
      val e = it.next()
      val v = e.getKey.intValue()
      val cs = e.getValue.toString
      if (cs.length > mx || (cs.length == mx && v > mv)) {
        mx = cs.length
        mv = v
        ans = cs
      }
    }
    ans
  }
}
'''

FILES["3693_climbing_stairs_ii"] = r'''// LeetCode 3693 - Climbing Stairs II
// https://leetcode.com/problems/climbing-stairs-ii/

object Solution {
  def climbStairs(n: Int, costs: Array[Int]): Int = {
    val inf = 1000000000
    val f = Array.fill(n + 1)(inf)
    f(0) = 0
    var i = 1
    while (i <= n) {
      val x = costs(i - 1)
      var j = math.max(0, i - 3)
      while (j < i) {
        f(i) = math.min(f(i), f(j) + x + (i - j) * (i - j))
        j += 1
      }
      i += 1
    }
    f(n)
  }
}
'''

FILES["3694_distinct_points_reachable_after_substring_removal"] = r'''// LeetCode 3694 - Distinct Points Reachable After Substring Removal
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

object Solution {
  def distinctPoints(s: String, k: Int): Int = {
    val n = s.length
    val f = new Array[Int](n + 1)
    val g = new Array[Int](n + 1)
    var x = 0
    var y = 0
    var i = 1
    while (i <= n) {
      val c = s.charAt(i - 1)
      if (c == 'U') y += 1
      else if (c == 'D') y -= 1
      else if (c == 'L') x -= 1
      else x += 1
      f(i) = x
      g(i) = y
      i += 1
    }
    val st = new java.util.HashSet[java.lang.Long]()
    i = k
    while (i <= n) {
      val a = f(n) - (f(i) - f(i - k))
      val b = g(n) - (g(i) - g(i - k))
      val key = a.toLong * n + b
      st.add(key)
      i += 1
    }
    st.size()
  }
}
'''

FILES["3695_maximize_alternating_sum_using_swaps"] = r'''// LeetCode 3695 - Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

object Solution {
  def maxAlternatingSum(nums: Array[Int], swaps: Array[Array[Int]]): Long = {
    val n = nums.length
    val parent = Array.tabulate(n)(i => i)

    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }

    for (s <- swaps) {
      val a = find(s(0))
      val b = find(s(1))
      if (a != b) parent(a) = b
    }
    val compVals = new java.util.HashMap[Integer, java.util.List[Integer]]()
    val compIdx = new java.util.HashMap[Integer, java.util.List[Integer]]()
    var i = 0
    while (i < n) {
      val r = find(i)
      compVals.computeIfAbsent(r, _ => new java.util.ArrayList[Integer]()).add(nums(i))
      compIdx.computeIfAbsent(r, _ => new java.util.ArrayList[Integer]()).add(i)
      i += 1
    }
    val arr = new Array[Int](n)
    val it = compVals.entrySet().iterator()
    while (it.hasNext) {
      val e = it.next()
      val r = e.getKey
      val vals = e.getValue
      val idxs = compIdx.get(r)
      vals.sort(java.util.Collections.reverseOrder())
      val even = new java.util.ArrayList[Integer]()
      val odd = new java.util.ArrayList[Integer]()
      val iit = idxs.iterator()
      while (iit.hasNext) {
        val ii = iit.next().intValue()
        if (ii % 2 == 0) even.add(ii)
        else odd.add(ii)
      }
      java.util.Collections.sort(even)
      java.util.Collections.sort(odd)
      var ei = 0
      val vit = vals.iterator()
      while (vit.hasNext) {
        val v = vit.next().intValue()
        if (ei < even.size()) {
          arr(even.get(ei)) = v
          ei += 1
        } else {
          arr(odd.get(ei - even.size())) = v
          ei += 1
        }
      }
    }
    var ans = 0L
    i = 0
    while (i < n) {
      if (i % 2 == 0) ans += arr(i)
      else ans -= arr(i)
      i += 1
    }
    ans
  }
}
'''

def main():
    written = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "Solution.scala"
        path.write_text(content, encoding="utf-8", newline="\n")
        if path.read_bytes().startswith(b"\xef\xbb\xbf"):
            raise SystemExit(f"BOM in {folder}")
        written += 1
        print(f"wrote {folder}")
    print(f"total {written}")

if __name__ == "__main__":
    main()
