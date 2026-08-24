#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

TREE = """class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}
"""

FILES["3318_find_x_sum_of_all_k_long_subarrays_i"] = """// LeetCode 3318 - Find X-Sum of All K-Long Subarrays I
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

object Solution {
  def findXSum(nums: Array[Int], k: Int, x: Int): Array[Int] = {
    val n = nums.length
    val ans = new Array[Int](n - k + 1)
    var i = 0
    while (i <= n - k) {
      val freq = scala.collection.mutable.HashMap.empty[Int, Int]
      var j = i
      while (j < i + k) {
        freq(nums(j)) = freq.getOrElse(nums(j), 0) + 1
        j += 1
      }
      val arr = freq.toArray
      var a = 0
      while (a < arr.length) {
        var b = a + 1
        while (b < arr.length) {
          val A = arr(a)
          val B = arr(b)
          if (B._2 > A._2 || (B._2 == A._2 && B._1 > A._1)) {
            arr(a) = B
            arr(b) = A
          }
          b += 1
        }
        a += 1
      }
      val lim = math.min(x, arr.length)
      val keep = scala.collection.mutable.HashSet.empty[Int]
      var t = 0
      while (t < lim) {
        keep += arr(t)._1
        t += 1
      }
      var sum = 0
      j = i
      while (j < i + k) {
        if (keep.contains(nums(j))) sum += nums(j)
        j += 1
      }
      ans(i) = sum
      i += 1
    }
    ans
  }
}
"""

FILES["3319_k_th_largest_perfect_subtree_size_in_binary_tree"] = f"""// LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
// https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

{TREE}
object Solution {{
  def kthLargestPerfectSubtree(root: TreeNode, k: Int): Int = {{
    val sizes = scala.collection.mutable.ArrayBuffer.empty[Int]
    def dfs(node: TreeNode): Array[Int] = {{
      if (node == null) return Array(0, 0, 1)
      val L = dfs(node.left)
      val R = dfs(node.right)
      val sz = L(1) + R(1) + 1
      val perf = L(2) == 1 && R(2) == 1 && L(0) == R(0)
      if (perf) sizes += sz
      Array(math.max(L(0), R(0)) + 1, sz, if (perf) 1 else 0)
    }}
    dfs(root)
    val sorted = sizes.sorted.reverse
    if (k > sorted.length) -1 else sorted(k - 1)
  }}
}}
"""

FILES["3320_count_the_number_of_winning_sequences"] = """// LeetCode 3320 - Count the Number of Winning Sequences
// https://leetcode.com/problems/count-the-number-of-winning-sequences/

object Solution {
  def countWinningSequences(s: String): Int = {
    val mod = 1000000007
    val n = s.length
    val mp = new Array[Int](256)
    mp('F') = 0; mp('W') = 1; mp('E') = 2
    val beat = Array(2, 0, 1)
    val score = Array.ofDim[Int](3, 3)
    var a = 0
    while (a < 3) {
      var b = 0
      while (b < 3) {
        if (a == b) score(a)(b) = 0
        else if (beat(a) == b) score(a)(b) = 1
        else score(a)(b) = -1
        b += 1
      }
      a += 1
    }
    val offset = n
    var dp = Array.fill(3, 2 * n + 1)(0)
    val b0 = mp(s.charAt(0))
    a = 0
    while (a < 3) {
      dp(a)(score(a)(b0) + offset) = 1
      a += 1
    }
    var i = 1
    while (i < n) {
      val ndp = Array.fill(3, 2 * n + 1)(0)
      val b = mp(s.charAt(i))
      var last = 0
      while (last < 3) {
        var d = 0
        while (d <= 2 * n) {
          if (dp(last)(d) != 0) {
            a = 0
            while (a < 3) {
              if (a != last) {
                val nd = d + score(a)(b)
                if (nd >= 0 && nd <= 2 * n) {
                  ndp(a)(nd) = (ndp(a)(nd) + dp(last)(d)) % mod
                }
              }
              a += 1
            }
          }
          d += 1
        }
        last += 1
      }
      dp = ndp
      i += 1
    }
    var ans = 0
    a = 0
    while (a < 3) {
      var d = offset + 1
      while (d <= 2 * n) {
        ans = (ans + dp(a)(d)) % mod
        d += 1
      }
      a += 1
    }
    ans
  }
}
"""

FILES["3321_find_x_sum_of_all_k_long_subarrays_ii"] = """// LeetCode 3321 - Find X-Sum of All K-Long Subarrays II
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

object Solution {
  def findXSum(nums: Array[Int], k: Int, x: Int): Array[Long] = {
    val n = nums.length
    val ans = new Array[Long](n - k + 1)
    var i = 0
    while (i <= n - k) {
      val freq = scala.collection.mutable.HashMap.empty[Int, Int]
      var j = i
      while (j < i + k) {
        freq(nums(j)) = freq.getOrElse(nums(j), 0) + 1
        j += 1
      }
      val arr = freq.toArray
      var a = 0
      while (a < arr.length) {
        var b = a + 1
        while (b < arr.length) {
          val A = arr(a)
          val B = arr(b)
          if (B._2 > A._2 || (B._2 == A._2 && B._1 > A._1)) {
            arr(a) = B
            arr(b) = A
          }
          b += 1
        }
        a += 1
      }
      val lim = math.min(x, arr.length)
      val keep = scala.collection.mutable.HashSet.empty[Int]
      var t = 0
      while (t < lim) {
        keep += arr(t)._1
        t += 1
      }
      var sum = 0L
      j = i
      while (j < i + k) {
        if (keep.contains(nums(j))) sum += nums(j)
        j += 1
      }
      ans(i) = sum
      i += 1
    }
    ans
  }
}
"""

FILES["3323_minimize_connected_groups_by_inserting_interval"] = """// LeetCode 3323 - Minimize Connected Groups by Inserting Interval
// https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

object Solution {
  def minConnectedGroups(intervals: Array[Array[Int]], k: Int): Int = {
    val sorted = intervals.sortBy(_(0))
    val merged = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    for (it <- sorted) {
      if (merged.isEmpty || it(0) > merged.last(1)) merged += Array(it(0), it(1))
      else if (it(1) > merged.last(1)) merged.last(1) = it(1)
    }
    val m = merged.length
    var ans = m
    var i = 0
    while (i < m) {
      val end = merged(i)(1) + k
      var j = i
      while (j < m && merged(j)(0) <= end) j += 1
      val groups = i + 1 + (m - j)
      if (groups < ans) ans = groups
      i += 1
    }
    ans
  }
}
"""

FILES["3324_find_the_sequence_of_strings_appeared_on_the_screen"] = """// LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
// https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

object Solution {
  def stringSequence(target: String): Array[String] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[String]
    val cur = new StringBuilder
    for (ch <- target) {
      cur.append('a')
      ans += cur.toString
      while (cur.charAt(cur.length - 1) != ch) {
        cur.setCharAt(cur.length - 1, (cur.charAt(cur.length - 1) + 1).toChar)
        ans += cur.toString
      }
    }
    ans.toArray
  }
}
"""

FILES["3325_count_substrings_with_k_frequency_characters_i"] = """// LeetCode 3325 - Count Substrings With K-Frequency Characters I
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

object Solution {
  def numberOfSubstrings(s: String, k: Int): Int = {
    val n = s.length
    var ans = 0
    var i = 0
    while (i < n) {
      val freq = new Array[Int](26)
      var j = i
      var done = false
      while (j < n && !done) {
        freq(s.charAt(j) - 'a') += 1
        var ok = false
        var f = 0
        while (f < 26) {
          if (freq(f) >= k) ok = true
          f += 1
        }
        if (ok) {
          ans += n - j
          done = true
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
"""

FILES["3326_minimum_division_operations_to_make_array_non_decreasing"] = """// LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

object Solution {
  private def smallestProperDivisor(x: Int): Int = {
    var d = 2
    while (d.toLong * d <= x) {
      if (x % d == 0) return d
      d += 1
    }
    x
  }

  def minOperations(nums: Array[Int]): Int = {
    var ops = 0
    var i = nums.length - 2
    while (i >= 0) {
      if (nums(i) > nums(i + 1)) {
        while (nums(i) > nums(i + 1)) {
          val d = smallestProperDivisor(nums(i))
          if (d == nums(i)) return -1
          nums(i) /= d
          ops += 1
          if (nums(i) > nums(i + 1) && smallestProperDivisor(nums(i)) == nums(i)) return -1
        }
      }
      i -= 1
    }
    ops
  }
}
"""

FILES["3327_check_if_dfs_strings_are_palindromes"] = """// LeetCode 3327 - Check DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

object Solution {
  def findAnswer(parent: Array[Int], s: String): Array[Boolean] = {
    val n = parent.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 1
    while (i < n) {
      g(parent(i)) += i
      i += 1
    }
    val ans = new Array[Boolean](n)
    def isPal(t: String): Boolean = {
      var a = 0
      var b = t.length - 1
      while (a < b) {
        if (t.charAt(a) != t.charAt(b)) return false
        a += 1
        b -= 1
      }
      true
    }
    def dfsStr(u: Int): String = {
      val out = new StringBuilder
      for (v <- g(u)) out.append(dfsStr(v))
      out.append(s.charAt(u))
      ans(u) = isPal(out.toString)
      out.toString
    }
    dfsStr(0)
    ans
  }
}
"""

FILES["3329_count_substrings_with_k_frequency_characters_ii"] = """// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

object Solution {
  def numberOfSubstrings(s: String, k: Int): Long = {
    val n = s.length
    var ans = 0L
    var i = 0
    while (i < n) {
      val freq = new Array[Int](26)
      var j = i
      var done = false
      while (j < n && !done) {
        freq(s.charAt(j) - 'a') += 1
        var ok = false
        var f = 0
        while (f < 26) {
          if (freq(f) >= k) ok = true
          f += 1
        }
        if (ok) {
          ans += n - j
          done = true
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
"""

FILES["3330_find_the_original_typed_string_i"] = """// LeetCode 3330 - Find the Original Typed String I
// https://leetcode.com/problems/find-the-original-typed-string-i/

object Solution {
  def possibleStringCount(word: String): Int = {
    var ans = 1
    var i = 1
    while (i < word.length) {
      if (word.charAt(i) == word.charAt(i - 1)) ans += 1
      i += 1
    }
    ans
  }
}
"""

FILES["3331_find_subtree_sizes_after_changes"] = """// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

object Solution {
  def findSubtreeSizes(parent: Array[Int], s: String): Array[Int] = {
    val n = parent.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 1
    while (i < n) {
      g(parent(i)) += i
      i += 1
    }
    val newParent = parent.clone()
    val last = Array.fill(26)(-1)
    def dfs1(u: Int): Unit = {
      val c = s.charAt(u) - 'a'
      val prev = last(c)
      if (prev != -1) newParent(u) = prev
      last(c) = u
      for (v <- g(u)) dfs1(v)
      last(c) = prev
    }
    dfs1(0)
    val ng = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    i = 1
    while (i < n) {
      ng(newParent(i)) += i
      i += 1
    }
    val ans = new Array[Int](n)
    def dfs2(u: Int): Int = {
      var sz = 1
      for (v <- ng(u)) sz += dfs2(v)
      ans(u) = sz
      sz
    }
    dfs2(0)
    ans
  }
}
"""

FILES["3332_maximum_points_tourist_can_earn"] = """// LeetCode 3332 - Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/

object Solution {
  def maxScore(n: Int, k: Int, stayScore: Array[Array[Int]], travelScore: Array[Array[Int]]): Int = {
    var dp = new Array[Int](n)
    var day = 0
    while (day < k) {
      val ndp = Array.fill(n)(-(1 << 30))
      var dest = 0
      while (dest < n) {
        var best = -(1 << 30)
        var src = 0
        while (src < n) {
          var value = dp(src)
          if (src == dest) value += stayScore(day)(dest)
          else value += travelScore(src)(dest)
          if (value > best) best = value
          src += 1
        }
        ndp(dest) = best
        dest += 1
      }
      dp = ndp
      day += 1
    }
    var ans = dp(0)
    var i = 1
    while (i < n) {
      if (dp(i) > ans) ans = dp(i)
      i += 1
    }
    ans
  }
}
"""

FILES["3333_find_the_original_typed_string_ii"] = """// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

object Solution {
  def possibleStringCount(word: String, k: Int): Int = {
    val mod = 1000000007
    val groups = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < word.length) {
      var j = i
      while (j < word.length && word.charAt(j) == word.charAt(i)) j += 1
      groups += j - i
      i = j
    }
    var total = 1
    for (g <- groups) total = (total.toLong * g % mod).toInt
    if (k <= groups.length) return total
    val need = k - 1
    var dp = new Array[Int](need)
    dp(0) = 1
    for (g <- groups) {
      val ndp = new Array[Int](need)
      val pref = new Array[Int](need + 1)
      i = 0
      while (i < need) {
        pref(i + 1) = (pref(i) + dp(i)) % mod
        i += 1
      }
      var s = 0
      while (s < need) {
        var lo = s - g
        if (lo < 0) lo = 0
        val hi = s - 1
        if (hi >= 0) ndp(s) = (pref(hi + 1) - pref(lo) + mod) % mod
        s += 1
      }
      dp = ndp
    }
    var bad = 0
    for (v <- dp) bad = (bad + v) % mod
    (total - bad + mod) % mod
  }
}
"""

FILES["3334_find_the_maximum_factor_score_of_array"] = """// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

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

  def maxScore(nums: Array[Int]): Long = {
    val n = nums.length
    var gcdAll = nums(0)
    var lcmAll = nums(0)
    var i = 1
    while (i < n) {
      gcdAll = gcd(gcdAll, nums(i))
      lcmAll = lcm(lcmAll, nums(i))
      i += 1
    }
    var ans = gcdAll.toLong * lcmAll
    var skip = 0
    while (skip < n) {
      var g = 0
      var l = 1
      var first = true
      i = 0
      while (i < n) {
        if (i != skip) {
          if (first) { g = nums(i); l = nums(i); first = false }
          else { g = gcd(g, nums(i)); l = lcm(l, nums(i)) }
        }
        i += 1
      }
      if (!first) {
        val v = g.toLong * l
        if (v > ans) ans = v
      }
      skip += 1
    }
    ans
  }
}
"""

FILES["3335_total_characters_in_string_after_transformations_i"] = """// LeetCode 3335 - Total Characters in String After Transformations I
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

object Solution {
  def lengthAfterTransformations(s: String, t: Int): Int = {
    val mod = 1000000007
    var cnt = new Array[Int](26)
    for (c <- s) cnt(c - 'a') += 1
    var step = 0
    while (step < t) {
      val ncnt = new Array[Int](26)
      var i = 0
      while (i < 25) {
        ncnt(i + 1) = (ncnt(i + 1) + cnt(i)) % mod
        i += 1
      }
      ncnt(0) = (ncnt(0) + cnt(25)) % mod
      ncnt(1) = (ncnt(1) + cnt(25)) % mod
      cnt = ncnt
      step += 1
    }
    var ans = 0
    for (v <- cnt) ans = (ans + v) % mod
    ans
  }
}
"""

FILES["3336_find_the_number_of_subsequences_with_equal_gcd"] = """// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

object Solution {
  private def gcd(a0: Int, b0: Int): Int = {
    if (a0 == 0) return b0
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  def subsequencePairCount(nums: Array[Int]): Int = {
    val mod = 1000000007
    var maxV = 0
    for (x <- nums) if (x > maxV) maxV = x
    var dp = Array.ofDim[Int](maxV + 1, maxV + 1)
    dp(0)(0) = 1
    for (x <- nums) {
      val ndp = Array.ofDim[Int](maxV + 1, maxV + 1)
      var a = 0
      while (a <= maxV) {
        Array.copy(dp(a), 0, ndp(a), 0, maxV + 1)
        a += 1
      }
      a = 0
      while (a <= maxV) {
        var b = 0
        while (b <= maxV) {
          if (dp(a)(b) != 0) {
            val na = if (a == 0) x else gcd(a, x)
            val nb = if (b == 0) x else gcd(b, x)
            ndp(na)(b) = (ndp(na)(b) + dp(a)(b)) % mod
            ndp(a)(nb) = (ndp(a)(nb) + dp(a)(b)) % mod
          }
          b += 1
        }
        a += 1
      }
      dp = ndp
    }
    var ans = 0
    var g = 1
    while (g <= maxV) {
      ans = (ans + dp(g)(g)) % mod
      g += 1
    }
    ans
  }
}
"""

FILES["3337_total_characters_in_string_after_transformations_ii"] = """// LeetCode 3337 - Total Characters in String After Transformations II
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

object Solution {
  private def matMul(a: Array[Array[Int]], b: Array[Array[Int]], mod: Int): Array[Array[Int]] = {
    val n = a.length
    val c = Array.ofDim[Int](n, n)
    var i = 0
    while (i < n) {
      var k = 0
      while (k < n) {
        if (a(i)(k) != 0) {
          var j = 0
          while (j < n) {
            c(i)(j) = (c(i)(j) + (a(i)(k).toLong * b(k)(j) % mod).toInt) % mod
            j += 1
          }
        }
        k += 1
      }
      i += 1
    }
    c
  }

  private def matPow(a0: Array[Array[Int]], e0: Int, mod: Int): Array[Array[Int]] = {
    val n = a0.length
    var a = a0
    var e = e0
    val r = Array.ofDim[Int](n, n)
    var i = 0
    while (i < n) { r(i)(i) = 1; i += 1 }
    while (e > 0) {
      if ((e & 1) != 0) { val nr = matMul(r, a, mod); Array.copy(nr, 0, r, 0, n); var ii = 0; while (ii < n) { r(ii) = nr(ii); ii += 1 } }
      a = matMul(a, a, mod)
      e >>= 1
    }
    r
  }

  def lengthAfterTransformations(s: String, t: Int, nums: Array[Int]): Int = {
    val mod = 1000000007
    var mat = Array.ofDim[Int](26, 26)
    var i = 0
    while (i < 26) {
      var j = 1
      while (j <= nums(i)) {
        mat(i)((i + j) % 26) = 1
        j += 1
      }
      i += 1
    }
    mat = matPow(mat, t, mod)
    val cnt = new Array[Int](26)
    for (c <- s) cnt(c - 'a') += 1
    var ans = 0
    i = 0
    while (i < 26) {
      var j = 0
      while (j < 26) {
        ans = (ans + (cnt(i).toLong * mat(i)(j) % mod).toInt) % mod
        j += 1
      }
      i += 1
    }
    ans
  }
}
"""

FILES["3339_find_the_number_of_k_even_arrays"] = """// LeetCode 3339 - Find the Number of K-Even Arrays
// https://leetcode.com/problems/find-the-number-of-k-even-arrays/

object Solution {
  def countOfArrays(n: Int, m: Int, k: Int): Int = {
    val mod = 1000000007
    val even = m / 2
    val odd = m - even
    val dp = Array.ofDim[Int](n + 1, k + 1, 2)
    dp(1)(0)(0) = odd
    dp(1)(0)(1) = even
    var i = 1
    while (i < n) {
      var j = 0
      while (j <= k) {
        dp(i + 1)(j)(0) = (dp(i + 1)(j)(0) + ((((dp(i)(j)(0).toLong + dp(i)(j)(1)) % mod) * odd % mod).toInt)) % mod
        dp(i + 1)(j)(1) = (dp(i + 1)(j)(1) + (dp(i)(j)(0).toLong * even % mod).toInt) % mod
        if (j < k) {
          dp(i + 1)(j + 1)(1) = (dp(i + 1)(j + 1)(1) + (dp(i)(j)(1).toLong * even % mod).toInt) % mod
        }
        j += 1
      }
      i += 1
    }
    (dp(n)(k)(0) + dp(n)(k)(1)) % mod
  }
}
"""

FILES["3340_check_balanced_string"] = """// LeetCode 3340 - Check Balanced String
// https://leetcode.com/problems/check-balanced-string/

object Solution {
  def isBalanced(num: String): Boolean = {
    var even = 0
    var odd = 0
    var i = 0
    while (i < num.length) {
      if (i % 2 == 0) even += num.charAt(i) - '0'
      else odd += num.charAt(i) - '0'
      i += 1
    }
    even == odd
  }
}
"""

FILES["3341_find_minimum_time_to_reach_last_room_i"] = """// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

object Solution {
  def minTimeToReach(moveTime: Array[Array[Int]]): Int = {
    val m = moveTime.length
    val n = moveTime(0).length
    val dist = Array.fill(m, n)(1 << 30)
    val h = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    h.offer(Array(0, 0, 0))
    dist(0)(0) = 0
    val dirs = Array(Array(0, 1), Array(1, 0), Array(0, -1), Array(-1, 0))
    while (!h.isEmpty) {
      val cur = h.poll()
      val t = cur(0)
      val r = cur(1)
      val c = cur(2)
      if (t == dist(r)(c)) {
        if (r == m - 1 && c == n - 1) return t
        for (d <- dirs) {
          val nr = r + d(0)
          val nc = c + d(1)
          if (nr >= 0 && nc >= 0 && nr < m && nc < n) {
            val start = math.max(t, moveTime(nr)(nc))
            val nt = start + 1
            if (nt < dist(nr)(nc)) {
              dist(nr)(nc) = nt
              h.offer(Array(nt, nr, nc))
            }
          }
        }
      }
    }
    -1
  }
}
"""

FILES["3342_find_minimum_time_to_reach_last_room_ii"] = """// LeetCode 3342 - Find Minimum Time to Reach Last Room II
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

object Solution {
  def minTimeToReach(moveTime: Array[Array[Int]]): Int = {
    val m = moveTime.length
    val n = moveTime(0).length
    val INF = 1 << 30
    val dist = Array.fill(m, n, 2)(INF)
    val pq = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    dist(0)(0)(0) = 0
    pq.offer(Array(0, 0, 0, 0))
    val dirs = Array(Array(0, 1), Array(1, 0), Array(0, -1), Array(-1, 0))
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val t = cur(0)
      val r = cur(1)
      val c = cur(2)
      val parity = cur(3)
      if (t == dist(r)(c)(parity)) {
        if (r == m - 1 && c == n - 1) return t
        val cost = if (parity == 1) 2 else 1
        for (d <- dirs) {
          val nr = r + d(0)
          val nc = c + d(1)
          if (nr >= 0 && nc >= 0 && nr < m && nc < n) {
            val start = math.max(t, moveTime(nr)(nc))
            val nt = start + cost
            val np = 1 - parity
            if (nt < dist(nr)(nc)(np)) {
              dist(nr)(nc)(np) = nt
              pq.offer(Array(nt, nr, nc, np))
            }
          }
        }
      }
    }
    -1
  }
}
"""

FILES["3343_count_number_of_balanced_permutations"] = """// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

object Solution {
  private def modPow(a0: Long, e0: Long, mod: Int): Int = {
    var r = 1L
    var a = a0 % mod
    var e = e0
    while (e > 0) {
      if ((e & 1) != 0) r = r * a % mod
      a = a * a % mod
      e >>= 1
    }
    r.toInt
  }

  private def key(a: Int, b: Int): Long = (a.toLong << 32) | (b.toLong & 0xffffffffL)

  def countBalancedPermutations(num: String): Int = {
    val mod = 1000000007
    val cnt = new Array[Int](10)
    var sum = 0
    for (c <- num) {
      cnt(c - '0') += 1
      sum += c - '0'
    }
    if (sum % 2 == 1) return 0
    val n = num.length
    val halfN = n / 2
    val halfS = sum / 2
    val fact = new Array[Int](n + 1)
    val invF = new Array[Int](n + 1)
    fact(0) = 1
    var i = 1
    while (i <= n) {
      fact(i) = (fact(i - 1).toLong * i % mod).toInt
      i += 1
    }
    invF(n) = modPow(fact(n).toLong, mod - 2, mod)
    i = n
    while (i > 0) {
      invF(i - 1) = (invF(i).toLong * i % mod).toInt
      i -= 1
    }
    var dp = scala.collection.mutable.HashMap[Long, Int](key(0, 0) -> 1)
    var d = 0
    while (d <= 9) {
      val ndp = scala.collection.mutable.HashMap.empty[Long, Int]
      for ((st, ways) <- dp) {
        val used = (st >> 32).toInt
        val s = st.toInt
        var take = 0
        while (take <= cnt(d)) {
          val nu = used + take
          val ns = s + take * d
          if (nu <= halfN && ns <= halfS) {
            val w = (ways.toLong * invF(take) % mod * invF(cnt(d) - take) % mod).toInt
            val nk = key(nu, ns)
            ndp(nk) = (ndp.getOrElse(nk, 0) + w) % mod
          }
          take += 1
        }
      }
      dp = ndp
      d += 1
    }
    var ans = dp.getOrElse(key(halfN, halfS), 0)
    ans = (ans.toLong * fact(halfN) % mod * fact(n - halfN) % mod).toInt
    d = 0
    while (d <= 9) {
      ans = (ans.toLong * fact(cnt(d)) % mod).toInt
      d += 1
    }
    ans
  }
}
"""

def main() -> None:
    written = 0
    for folder, text in FILES.items():
        path = ROOT / folder / "Solution.scala"
        path.write_text(text, encoding="utf-8", newline="\n")
        if text.startswith("\ufeff"):
            raise SystemExit(f"BOM in {folder}")
        written += 1
        print(f"wrote {folder}")
    print(f"batch_b written={written}")

if __name__ == "__main__":
    main()
