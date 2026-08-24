#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3696_maximum_distance_between_unequal_words_in_array_i"] = r'''// LeetCode 3696 - Maximum Distance Between Unequal Words in Array I
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-i/

object Solution {
  def maxDistance(words: Array[String]): Int = {
    val n = words.length
    var ans = 0
    var i = 0
    while (i < n) {
      if (words(i) != words(0)) ans = math.max(ans, i + 1)
      if (words(i) != words(n - 1)) ans = math.max(ans, n - i)
      i += 1
    }
    ans
  }
}
'''

FILES["3697_compute_decimal_representation"] = r'''// LeetCode 3697 - Compute Decimal Representation
// https://leetcode.com/problems/compute-decimal-representation/

object Solution {
  def decimalRepresentation(n0: Int): Array[Int] = {
    val ans = new java.util.ArrayList[Integer]()
    var p = 1
    var n = n0
    while (n > 0) {
      val v = n % 10
      n /= 10
      if (v != 0) ans.add(p * v)
      p *= 10
    }
    java.util.Collections.reverse(ans)
    val res = new Array[Int](ans.size())
    var i = 0
    while (i < ans.size()) {
      res(i) = ans.get(i)
      i += 1
    }
    res
  }
}
'''

FILES["3698_split_array_with_minimum_difference"] = r'''// LeetCode 3698 - Split Array With Minimum Difference
// https://leetcode.com/problems/split-array-with-minimum-difference/

object Solution {
  def splitArray(nums: Array[Int]): Long = {
    val n = nums.length
    val s = new Array[Long](n)
    val f = Array.fill(n)(true)
    val g = Array.fill(n)(true)
    s(0) = nums(0)
    var i = 1
    while (i < n) {
      s(i) = s(i - 1) + nums(i)
      f(i) = f(i - 1)
      if (nums(i) <= nums(i - 1)) f(i) = false
      i += 1
    }
    i = n - 2
    while (i >= 0) {
      g(i) = g(i + 1)
      if (nums(i) <= nums(i + 1)) g(i) = false
      i -= 1
    }
    val inf = Long.MaxValue / 4
    var ans = inf
    i = 0
    while (i < n - 1) {
      if (f(i) && g(i + 1)) {
        val s1 = s(i)
        val s2 = s(n - 1) - s(i)
        ans = math.min(ans, math.abs(s1 - s2))
      }
      i += 1
    }
    if (ans < inf) ans else -1L
  }
}
'''

FILES["3699_number_of_zigzag_arrays_i"] = r'''// LeetCode 3699 - Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/

object Solution {
  def zigZagArrays(n: Int, l: Int, r: Int): Int = {
    val MOD = 1000000007
    val m = r - l + 1
    if (n == 1) return m % MOD
    var up = Array.fill(m)(1)
    var down = Array.fill(m)(1)
    var len_ = 2
    while (len_ <= n) {
      val prefDown = new Array[Int](m + 1)
      var j = 0
      while (j < m) {
        prefDown(j + 1) = (prefDown(j) + down(j)) % MOD
        j += 1
      }
      val nup = new Array[Int](m)
      j = 0
      while (j < m) {
        nup(j) = prefDown(j)
        j += 1
      }
      val sufUp = new Array[Int](m + 1)
      j = m - 1
      while (j >= 0) {
        sufUp(j) = (sufUp(j + 1) + up(j)) % MOD
        j -= 1
      }
      val ndown = new Array[Int](m)
      j = 0
      while (j < m) {
        ndown(j) = sufUp(j + 1)
        j += 1
      }
      up = nup
      down = ndown
      len_ += 1
    }
    var ans = 0
    var j = 0
    while (j < m) {
      ans = (ans + up(j)) % MOD
      ans = (ans + down(j)) % MOD
      j += 1
    }
    ans
  }
}
'''

FILES["3700_number_of_zigzag_arrays_ii"] = r'''// LeetCode 3700 - Number of ZigZag Arrays II
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/

object Solution {
  def zigZagArrays(n: Int, l: Int, r: Int): Int = {
    val MOD = 1000000007
    val m = r - l + 1
    if (n == 1) return m % MOD
    var up = Array.fill(m)(1)
    var down = Array.fill(m)(1)
    var length = 2
    while (length <= n) {
      val pref = new Array[Int](m + 1)
      var j = 0
      while (j < m) {
        pref(j + 1) = (pref(j) + down(j)) % MOD
        j += 1
      }
      val nup = new Array[Int](m)
      j = 0
      while (j < m) {
        nup(j) = pref(j)
        j += 1
      }
      val suf = new Array[Int](m + 1)
      j = m - 1
      while (j >= 0) {
        suf(j) = (suf(j + 1) + up(j)) % MOD
        j -= 1
      }
      val ndown = new Array[Int](m)
      j = 0
      while (j < m) {
        ndown(j) = suf(j + 1)
        j += 1
      }
      up = nup
      down = ndown
      length += 1
    }
    var ans = 0
    var j = 0
    while (j < m) {
      ans = (ans + up(j)) % MOD
      ans = (ans + down(j)) % MOD
      j += 1
    }
    ans
  }
}
'''

FILES["3701_compute_alternating_sum"] = r'''// LeetCode 3701 - Compute Alternating Sum
// https://leetcode.com/problems/compute-alternating-sum/

object Solution {
  def alternatingSum(nums: Array[Int]): Int = {
    var ans = 0
    var i = 0
    while (i < nums.length) {
      if (i % 2 == 0) ans += nums(i)
      else ans -= nums(i)
      i += 1
    }
    ans
  }
}
'''

FILES["3702_longest_subsequence_with_non_zero_bitwise_xor"] = r'''// LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
// https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

object Solution {
  def longestSubsequence(nums: Array[Int]): Int = {
    var xorv = 0
    var cnt0 = 0
    for (x <- nums) {
      xorv ^= x
      if (x == 0) cnt0 += 1
    }
    val n = nums.length
    if (xorv != 0) n
    else if (cnt0 == n) 0
    else n - 1
  }
}
'''

FILES["3703_remove_k_balanced_substrings"] = r'''// LeetCode 3703 - Remove K-Balanced Substrings
// https://leetcode.com/problems/remove-k-balanced-substrings/

object Solution {
  def removeSubstring(s: String, k: Int): String = {
    val stk = new java.util.ArrayList[Array[Int]]()
    for (c <- s) {
      if (!stk.isEmpty && stk.get(stk.size() - 1)(0) == c.toInt)
        stk.get(stk.size() - 1)(1) += 1
      else stk.add(Array(c.toInt, 1))
      if (c == ')' && stk.size() > 1) {
        val top = stk.get(stk.size() - 1)
        val prev = stk.get(stk.size() - 2)
        if (top(1) == k && prev(1) >= k) {
          stk.remove(stk.size() - 1)
          prev(1) -= k
          if (prev(1) == 0) stk.remove(stk.size() - 1)
        }
      }
    }
    val res = new StringBuilder
    val it = stk.iterator()
    while (it.hasNext) {
      val p = it.next()
      var i = 0
      while (i < p(1)) {
        res.append(p(0).toChar)
        i += 1
      }
    }
    res.toString
  }
}
'''

FILES["3704_count_no_zero_pairs_that_sum_to_n"] = r'''// LeetCode 3704 - Count No-Zero Pairs That Sum to N
// https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

object Solution {
  def countNoZeroPairs(n: Long): Long = {
    val s = java.lang.Long.toString(n)
    val m = s.length
    val digits = new Array[Int](m + 1)
    var i = 0
    while (i < m) {
      digits(i) = s.charAt(m - 1 - i) - '0'
      i += 1
    }
    val dp = Array.ofDim[Long](2, 2, 2)
    dp(0)(1)(1) = 1
    var pos = 0
    while (pos < m + 1) {
      val ndp = Array.ofDim[Long](2, 2, 2)
      val target = digits(pos)
      var carry = 0
      while (carry <= 1) {
        var aliveA = 0
        while (aliveA <= 1) {
          var aliveB = 0
          while (aliveB <= 1) {
            val ways = dp(carry)(aliveA)(aliveB)
            if (ways != 0) {
              val A = Array.ofDim[Int](10, 2)
              var aLen = 0
              if (aliveA == 1) {
                var d = 1
                while (d <= 9) {
                  A(aLen)(0) = d
                  A(aLen)(1) = 1
                  aLen += 1
                  d += 1
                }
                if (pos > 0) {
                  A(aLen)(0) = 0
                  A(aLen)(1) = 0
                  aLen += 1
                }
              } else {
                A(0)(0) = 0
                A(0)(1) = 0
                aLen = 1
              }
              val B = Array.ofDim[Int](10, 2)
              var bLen = 0
              if (aliveB == 1) {
                var d = 1
                while (d <= 9) {
                  B(bLen)(0) = d
                  B(bLen)(1) = 1
                  bLen += 1
                  d += 1
                }
                if (pos > 0) {
                  B(bLen)(0) = 0
                  B(bLen)(1) = 0
                  bLen += 1
                }
              } else {
                B(0)(0) = 0
                B(0)(1) = 0
                bLen = 1
              }
              var ai = 0
              while (ai < aLen) {
                val da = A(ai)(0)
                val na = A(ai)(1)
                var bi = 0
                while (bi < bLen) {
                  val db = B(bi)(0)
                  val nb = B(bi)(1)
                  val sum = da + db + carry
                  if (sum % 10 == target) {
                    val ncarry = sum / 10
                    ndp(ncarry)(na)(nb) += ways
                  }
                  bi += 1
                }
                ai += 1
              }
            }
            aliveB += 1
          }
          aliveA += 1
        }
        carry += 1
      }
      var c = 0
      while (c < 2) {
        var a = 0
        while (a < 2) {
          var b = 0
          while (b < 2) {
            dp(c)(a)(b) = ndp(c)(a)(b)
            b += 1
          }
          a += 1
        }
        c += 1
      }
      pos += 1
    }
    dp(0)(0)(0)
  }
}
'''

FILES["3706_maximum_distance_between_unequal_words_in_array_ii"] = r'''// LeetCode 3706 - Maximum Distance Between Unequal Words in Array II
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/

object Solution {
  def maxDistance(words: Array[String]): Int = {
    val n = words.length
    var ans = 0
    var i = 0
    while (i < n) {
      if (words(i) != words(0)) ans = math.max(ans, i + 1)
      if (words(i) != words(n - 1)) ans = math.max(ans, n - i)
      i += 1
    }
    ans
  }
}
'''

FILES["3707_equal_score_substrings"] = r'''// LeetCode 3707 - Equal Score Substrings
// https://leetcode.com/problems/equal-score-substrings/

object Solution {
  def scoreBalance(s: String): Boolean = {
    var l = 0
    var r = 0
    for (c <- s) r += (c - 'a') + 1
    var i = 0
    while (i + 1 < s.length) {
      val x = (s.charAt(i) - 'a') + 1
      l += x
      r -= x
      if (l == r) return true
      i += 1
    }
    false
  }
}
'''

FILES["3708_longest_fibonacci_subarray"] = r'''// LeetCode 3708 - Longest Fibonacci Subarray
// https://leetcode.com/problems/longest-fibonacci-subarray/

object Solution {
  def longestSubarray(nums: Array[Int]): Int = {
    var f = 2
    var ans = f
    var i = 2
    while (i < nums.length) {
      if (nums(i) == nums(i - 1) + nums(i - 2)) {
        f += 1
        ans = math.max(ans, f)
      } else f = 2
      i += 1
    }
    ans
  }
}
'''

FILES["3709_design_exam_scores_tracker"] = r'''// LeetCode 3709 - Design Exam Scores Tracker
// https://leetcode.com/problems/design-exam-scores-tracker/

class ExamTracker() {
  private val times = new java.util.ArrayList[Integer]()
  private val pre = new java.util.ArrayList[java.lang.Long]()
  times.add(0)
  pre.add(0L)

  def record(time: Int, score: Int): Unit = {
    times.add(time)
    pre.add(pre.get(pre.size() - 1) + score)
  }

  def totalScore(startTime: Int, endTime: Int): Long = {
    val l = ExamTracker.lowerBound(times, startTime) - 1
    val r = ExamTracker.lowerBound(times, endTime + 1) - 1
    pre.get(r) - pre.get(l)
  }
}

object ExamTracker {
  private def lowerBound(a: java.util.List[Integer], target: Int): Int = {
    var lo = 0
    var hi = a.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a.get(mid) < target) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
'''

FILES["3710_maximum_partition_factor"] = r'''// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

object Solution {
  def maxPartitionFactor(points: Array[Array[Int]]): Int = {
    val n = points.length
    if (n == 2) return 0

    def dist(i: Int, j: Int): Int =
      math.abs(points(i)(0) - points(j)(0)) + math.abs(points(i)(1) - points(j)(1))

    def ok(d: Int): Boolean = {
      val g = Array.fill(n)(new java.util.ArrayList[Integer]())
      var i = 0
      while (i < n) {
        var j = i + 1
        while (j < n) {
          if (dist(i, j) < d) {
            g(i).add(j)
            g(j).add(i)
          }
          j += 1
        }
        i += 1
      }
      val color = Array.fill(n)(-1)
      i = 0
      while (i < n) {
        if (color(i) == -1) {
          val q = new java.util.ArrayDeque[Integer]()
          q.offer(i)
          color(i) = 0
          while (!q.isEmpty) {
            val u = q.poll()
            val it = g(u).iterator()
            while (it.hasNext) {
              val v = it.next().intValue()
              if (color(v) == -1) {
                color(v) = color(u) ^ 1
                q.offer(v)
              } else if (color(v) == color(u)) return false
            }
          }
        }
        i += 1
      }
      true
    }

    var lo = 0
    var hi = 0
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        hi = math.max(hi, dist(i, j))
        j += 1
      }
      i += 1
    }
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(mid)) lo = mid
      else hi = mid - 1
    }
    lo
  }
}
'''

FILES["3711_maximum_transactions_without_negative_balance"] = r'''// LeetCode 3711 - Maximum Transactions Without Negative Balance
// https://leetcode.com/problems/maximum-transactions-without-negative-balance/

object Solution {
  def maxTransactions(transactions: Array[Int]): Int = {
    val tm = new java.util.TreeMap[Integer, Integer]()
    var ans = transactions.length
    var s = 0L
    for (x <- transactions) {
      s += x
      tm.merge(x, 1, Integer.sum)
      while (s < 0) {
        val y = tm.firstKey.intValue()
        s -= y
        ans -= 1
        val c = tm.get(y)
        if (c == 1) tm.remove(y)
        else tm.put(y, c - 1)
      }
    }
    ans
  }
}
'''

FILES["3712_sum_of_elements_with_frequency_divisible_by_k"] = r'''// LeetCode 3712 - Sum of Elements With Frequency Divisible by K
// https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

object Solution {
  def sumDivisibleByK(nums: Array[Int], k: Int): Int = {
    val cnt = new java.util.HashMap[Integer, Integer]()
    for (x <- nums) cnt.merge(x, 1, Integer.sum)
    var ans = 0
    val it = cnt.entrySet().iterator()
    while (it.hasNext) {
      val e = it.next()
      if (e.getValue % k == 0) ans += e.getKey * e.getValue
    }
    ans
  }
}
'''

FILES["3713_longest_balanced_substring_i"] = r'''// LeetCode 3713 - Longest Balanced Substring I
// https://leetcode.com/problems/longest-balanced-substring-i/

object Solution {
  def longestBalanced(s: String): Int = {
    val n = s.length
    var ans = 0
    var i = 0
    while (i < n) {
      val cnt = new Array[Int](26)
      var mx = 0
      var v = 0
      var j = i
      while (j < n) {
        val c = s.charAt(j) - 'a'
        cnt(c) += 1
        if (cnt(c) == 1) v += 1
        mx = math.max(mx, cnt(c))
        if (mx * v == j - i + 1) ans = math.max(ans, j - i + 1)
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3714_longest_balanced_substring_ii"] = r'''// LeetCode 3714 - Longest Balanced Substring II
// https://leetcode.com/problems/longest-balanced-substring-ii/

object Solution {
  private def calc1(s: String): Int = {
    var res = 0
    val n = s.length
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n && s.charAt(j) == s.charAt(i)) j += 1
      res = math.max(res, j - i)
      i = j
    }
    res
  }

  private def calc2(s: String, a: Char, b: Char): Int = {
    var res = 0
    val n = s.length
    var i = 0
    while (i < n) {
      while (i < n && s.charAt(i) != a && s.charAt(i) != b) i += 1
      val pos = new java.util.HashMap[Integer, Integer]()
      pos.put(0, i - 1)
      var d = 0
      while (i < n && (s.charAt(i) == a || s.charAt(i) == b)) {
        if (s.charAt(i) == a) d += 1
        else d -= 1
        if (pos.containsKey(d)) res = math.max(res, i - pos.get(d))
        else pos.put(d, i)
        i += 1
      }
    }
    res
  }

  private def calc3(s: String): Int = {
    val pos = new java.util.HashMap[java.lang.Long, Integer]()
    pos.put(0L, -1)
    val cnt = new Array[Int](3)
    var res = 0
    var i = 0
    while (i < s.length) {
      cnt(s.charAt(i) - 'a') += 1
      val x = cnt(0) - cnt(1)
      val y = cnt(1) - cnt(2)
      val k = (x.toLong << 32) ^ (y & 0xffffffffL)
      if (pos.containsKey(k)) res = math.max(res, i - pos.get(k))
      else pos.put(k, i)
      i += 1
    }
    res
  }

  def longestBalanced(s: String): Int = {
    val x = calc1(s)
    val y = math.max(calc2(s, 'a', 'b'), math.max(calc2(s, 'b', 'c'), calc2(s, 'a', 'c')))
    val z = calc3(s)
    math.max(x, math.max(y, z))
  }
}
'''

FILES["3715_sum_of_perfect_square_ancestors"] = r'''// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

object Solution {
  def sumOfAncestors(n: Int, edges: Array[Array[Int]], nums: Array[Int]): Long = {
    val graph = Array.fill(n)(new java.util.ArrayList[Integer]())
    for (e <- edges) {
      graph(e(0)).add(e(1))
      graph(e(1)).add(e(0))
    }

    def kernel(x0: Int): Int = {
      var x = x0
      var res = 1
      var p = 2
      while (p * p <= x) {
        var cnt = 0
        while (x % p == 0) {
          x /= p
          cnt += 1
        }
        if (cnt % 2 == 1) res *= p
        p += 1
      }
      if (x > 1) res *= x
      res
    }

    val ks = new Array[Int](n)
    var i = 0
    while (i < n) {
      ks(i) = kernel(nums(i))
      i += 1
    }
    val freq = new java.util.HashMap[Integer, Integer]()
    var ans = 0L

    def dfs(u: Int, p: Int): Unit = {
      ans += freq.getOrDefault(ks(u), 0)
      freq.merge(ks(u), 1, Integer.sum)
      val it = graph(u).iterator()
      while (it.hasNext) {
        val v = it.next().intValue()
        if (v != p) dfs(v, u)
      }
      freq.merge(ks(u), -1, Integer.sum)
    }

    dfs(0, -1)
    ans
  }
}
'''

FILES["3717_minimum_operations_to_make_the_array_beautiful"] = r'''// LeetCode 3717 - Minimum Operations to Make the Array Beautiful
// https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    var f = new java.util.HashMap[Integer, Integer]()
    f.put(nums(0), 0)
    var i = 1
    while (i < nums.length) {
      val x = nums(i)
      val g = new java.util.HashMap[Integer, Integer]()
      val it = f.entrySet().iterator()
      while (it.hasNext) {
        val e = it.next()
        val pre = e.getKey.intValue()
        val s = e.getValue.intValue()
        var cur = (x + pre - 1) / pre * pre
        while (cur <= 100) {
          val `val` = s + (cur - x)
          val old = g.get(cur)
          if (old == null || old > `val`) g.put(cur, `val`)
          cur += pre
        }
      }
      f = g
      i += 1
    }
    var ans = Int.MaxValue
    val vit = f.values().iterator()
    while (vit.hasNext) ans = math.min(ans, vit.next())
    ans
  }
}
'''

FILES["3718_smallest_missing_multiple_of_k"] = r'''// LeetCode 3718 - Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/

object Solution {
  def missingMultiple(nums: Array[Int], k: Int): Int = {
    val s = new java.util.HashSet[Integer]()
    for (x <- nums) s.add(x)
    var i = 1
    while (true) {
      val x = k * i
      if (!s.contains(x)) return x
      i += 1
    }
    -1
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
