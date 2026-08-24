#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3025_find_the_number_of_ways_to_place_people_i"] = r'''// LeetCode 3025 - Find the Number of Ways to Place People I
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

object Solution {
  def numberOfPairs(points: Array[Array[Int]]): Int = {
    scala.util.Sorting.stableSort(points, (a: Array[Int], b: Array[Int]) =>
      if (a(0) != b(0)) a(0) < b(0) else a(1) > b(1)
    )
    var ans = 0
    var i = 0
    while (i < points.length) {
      val y1 = points(i)(1)
      var maxY = Int.MinValue
      var j = i + 1
      while (j < points.length) {
        val y2 = points(j)(1)
        if (maxY < y2 && y2 <= y1) {
          maxY = y2
          ans += 1
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3026_maximum_good_subarray_sum"] = r'''// LeetCode 3026 - Maximum Good Subarray Sum
// https://leetcode.com/problems/maximum-good-subarray-sum/

object Solution {
  def maximumSubarraySum(nums: Array[Int], k: Int): Long = {
    val p = scala.collection.mutable.HashMap[Int, Long]()
    p(nums(0)) = 0L
    var s = 0L
    val n = nums.length
    var ans = Long.MinValue
    var i = 0
    while (i < n) {
      s += nums(i)
      if (p.contains(nums(i) - k)) ans = math.max(ans, s - p(nums(i) - k))
      if (p.contains(nums(i) + k)) ans = math.max(ans, s - p(nums(i) + k))
      if (i + 1 < n) {
        val old = p.get(nums(i + 1))
        if (old.isEmpty || s < old.get) p(nums(i + 1)) = s
      }
      i += 1
    }
    if (ans == Long.MinValue) 0 else ans
  }
}
'''

FILES["3027_find_the_number_of_ways_to_place_people_ii"] = r'''// LeetCode 3027 - Find the Number of Ways to Place People II
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

object Solution {
  def numberOfPairs(points: Array[Array[Int]]): Int = {
    scala.util.Sorting.stableSort(points, (a: Array[Int], b: Array[Int]) =>
      if (a(0) != b(0)) a(0) < b(0) else a(1) > b(1)
    )
    var ans = 0
    var i = 0
    while (i < points.length) {
      val y1 = points(i)(1)
      var maxY = Int.MinValue
      var j = i + 1
      while (j < points.length) {
        val y2 = points(j)(1)
        if (maxY < y2 && y2 <= y1) {
          maxY = y2
          ans += 1
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3028_ant_on_the_boundary"] = r'''// LeetCode 3028 - Ant on the Boundary
// https://leetcode.com/problems/ant-on-the-boundary/

object Solution {
  def returnToBoundaryCount(nums: Array[Int]): Int = {
    var s = 0
    var ans = 0
    for (x <- nums) {
      s += x
      if (s == 0) ans += 1
    }
    ans
  }
}
'''

FILES["3029_minimum_time_to_revert_word_to_initial_state_i"] = r'''// LeetCode 3029 - Minimum Time to Revert Word to Initial State I
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

object Solution {
  def minimumTimeToInitialState(word: String, k: Int): Int = {
    val n = word.length
    var i = k
    while (i < n) {
      if (word.substring(i) == word.substring(0, n - i)) return i / k
      i += k
    }
    (n + k - 1) / k
  }
}
'''

FILES["3030_find_the_grid_of_region_average"] = r'''// LeetCode 3030 - Find the Grid of Region Average
// https://leetcode.com/problems/find-the-grid-of-region-average/

object Solution {
  def resultGrid(image: Array[Array[Int]], threshold: Int): Array[Array[Int]] = {
    val n = image.length
    val m = image(0).length
    val ans = Array.ofDim[Int](n, m)
    val ct = Array.ofDim[Int](n, m)
    var i = 0
    while (i + 2 < n) {
      var j = 0
      while (j + 2 < m) {
        var region = true
        var k = 0
        while (k < 3) {
          var l = 0
          while (l < 2) {
            region = region && math.abs(image(i + k)(j + l) - image(i + k)(j + l + 1)) <= threshold
            l += 1
          }
          k += 1
        }
        k = 0
        while (k < 2) {
          var l = 0
          while (l < 3) {
            region = region && math.abs(image(i + k)(j + l) - image(i + k + 1)(j + l)) <= threshold
            l += 1
          }
          k += 1
        }
        if (region) {
          var tot = 0
          k = 0
          while (k < 3) {
            var l = 0
            while (l < 3) { tot += image(i + k)(j + l); l += 1 }
            k += 1
          }
          k = 0
          while (k < 3) {
            var l = 0
            while (l < 3) {
              ct(i + k)(j + l) += 1
              ans(i + k)(j + l) += tot / 9
              l += 1
            }
            k += 1
          }
        }
        j += 1
      }
      i += 1
    }
    i = 0
    while (i < n) {
      var j = 0
      while (j < m) {
        if (ct(i)(j) == 0) ans(i)(j) = image(i)(j)
        else ans(i)(j) /= ct(i)(j)
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3031_minimum_time_to_revert_word_to_initial_state_ii"] = r'''// LeetCode 3031 - Minimum Time to Revert Word to Initial State II
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/

object Solution {
  private class Hashing(word: String, bas: Long, mod: Long) {
    val n = word.length
    val p = Array.ofDim[Long](n + 1)
    val h = Array.ofDim[Long](n + 1)
    p(0) = 1
    var i = 1
    while (i <= n) {
      p(i) = p(i - 1) * bas % mod
      h(i) = (h(i - 1) * bas + (word.charAt(i - 1) - 'a')) % mod
      i += 1
    }
    def query(l: Int, r: Int): Long =
      (h(r) - h(l - 1) * p(r - l + 1) % mod + mod) % mod
  }

  def minimumTimeToInitialState(word: String, k: Int): Int = {
    val hashing = new Hashing(word, 13331, 998244353)
    val n = word.length
    var i = k
    while (i < n) {
      if (hashing.query(1, n - i) == hashing.query(i + 1, n)) return i / k
      i += k
    }
    (n + k - 1) / k
  }
}
'''

FILES["3032_count_numbers_with_unique_digits_ii"] = r'''// LeetCode 3032 - Count Numbers With Unique Digits II
// https://leetcode.com/problems/count-numbers-with-unique-digits-ii/

object Solution {
  def numberCount(a: Int, b: Int): Int = {
    var num = ""
    var f: Array[Array[Int]] = null
    def reset(): Unit = {
      f = Array.fill(num.length, 1 << 10)(-1)
    }
    def dfs(pos: Int, mask: Int, limit: Boolean): Int = {
      if (pos >= num.length) return if (mask != 0) 1 else 0
      if (!limit && f(pos)(mask) != -1) return f(pos)(mask)
      val up = if (limit) num.charAt(pos) - '0' else 9
      var ans = 0
      var i = 0
      while (i <= up) {
        if (((mask >> i) & 1) == 0) {
          var nxt = mask | (1 << i)
          if (mask == 0 && i == 0) nxt = 0
          ans += dfs(pos + 1, nxt, limit && i == up)
        }
        i += 1
      }
      if (!limit) f(pos)(mask) = ans
      ans
    }
    num = b.toString
    reset()
    val y = dfs(0, 0, true)
    num = (a - 1).toString
    reset()
    val x = dfs(0, 0, true)
    y - x
  }
}
'''

FILES["3033_modify_the_matrix"] = r'''// LeetCode 3033 - Modify the Matrix
// https://leetcode.com/problems/modify-the-matrix/

object Solution {
  def modifiedMatrix(matrix: Array[Array[Int]]): Array[Array[Int]] = {
    val m = matrix.length
    val n = matrix(0).length
    var j = 0
    while (j < n) {
      var mx = -1
      var i = 0
      while (i < m) { mx = math.max(mx, matrix(i)(j)); i += 1 }
      i = 0
      while (i < m) {
        if (matrix(i)(j) == -1) matrix(i)(j) = mx
        i += 1
      }
      j += 1
    }
    matrix
  }
}
'''

FILES["3034_number_of_subarrays_that_match_a_pattern_i"] = r'''// LeetCode 3034 - Number of Subarrays That Match a Pattern I
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

object Solution {
  private def f(a: Int, b: Int): Int = {
    if (a == b) 0 else if (a < b) 1 else -1
  }

  def countMatchingSubarrays(nums: Array[Int], pattern: Array[Int]): Int = {
    val n = nums.length
    val m = pattern.length
    var ans = 0
    var i = 0
    while (i < n - m) {
      var ok = 1
      var k = 0
      while (k < m && ok != 0) {
        if (f(nums(i + k), nums(i + k + 1)) != pattern(k)) ok = 0
        k += 1
      }
      ans += ok
      i += 1
    }
    ans
  }
}
'''

FILES["3035_maximum_palindromes_after_operations"] = r'''// LeetCode 3035 - Maximum Palindromes After Operations
// https://leetcode.com/problems/maximum-palindromes-after-operations/

object Solution {
  private def popcount(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x != 0) { c += x & 1; x >>= 1 }
    c
  }

  def maxPalindromesAfterOperations(words: Array[String]): Int = {
    var s = 0
    var mask = 0
    for (w <- words) {
      s += w.length
      var i = 0
      while (i < w.length) { mask ^= 1 << (w.charAt(i) - 'a'); i += 1 }
    }
    s -= popcount(mask)
    val sorted = words.sortBy(_.length)
    var ans = 0
    for (w <- sorted) {
      s -= w.length / 2 * 2
      if (s < 0) return ans
      ans += 1
    }
    ans
  }
}
'''

FILES["3036_number_of_subarrays_that_match_a_pattern_ii"] = r'''// LeetCode 3036 - Number of Subarrays That Match a Pattern II
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/

object Solution {
  def countMatchingSubarrays(nums: Array[Int], pattern: Array[Int]): Int = {
    val N = pattern.length
    val ps = Array.ofDim[Int](N + 1)
    ps(0) = -1
    ps(1) = 0
    var i = 2
    var p = 0
    while (i <= N) {
      val x = pattern(i - 1)
      while (p >= 0 && pattern(p) != x) p = ps(p)
      p += 1
      ps(i) = p
      i += 1
    }
    var res = 0
    val M = nums.length
    i = 1
    p = 0
    while (i < M) {
      var t = nums(i) - nums(i - 1)
      if (t > 0) t = 1
      else if (t < 0) t = -1
      while (p >= 0 && pattern(p) != t) p = ps(p)
      p += 1
      if (p == N) {
        res += 1
        p = ps(p)
      }
      i += 1
    }
    res
  }
}
'''

FILES["3037_find_pattern_in_infinite_stream_ii"] = r'''// LeetCode 3037 - Find Pattern in Infinite Stream II
// https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

class InfiniteStream(_bits: Array[Int]) {
  private val bits = _bits
  private var i = 0
  def next(): Int = { val v = bits(i); i += 1; v }
}

object Solution {
  private def getLPS(pattern: Array[Int]): Array[Int] = {
    val n = pattern.length
    val lps = Array.ofDim[Int](n)
    var j = 0
    var i = 1
    while (i < n) {
      while (j > 0 && pattern(j) != pattern(i)) j = lps(j - 1)
      if (pattern(i) == pattern(j)) {
        j += 1
        lps(i) = j
      }
      i += 1
    }
    lps
  }

  def findPattern(stream: InfiniteStream, pattern: Array[Int]): Int = {
    val lps = getLPS(pattern)
    var i = 0
    var j = 0
    var bit = 0
    var readNext = false
    while (true) {
      if (!readNext) {
        bit = stream.next()
        readNext = true
      }
      if (bit == pattern(j)) {
        i += 1
        readNext = false
        j += 1
        if (j == pattern.length) return i - j
      } else if (j > 0) {
        j = lps(j - 1)
      } else {
        i += 1
        readNext = false
      }
    }
    -1
  }
}
'''

FILES["3038_maximum_number_of_operations_with_the_same_score_i"] = r'''// LeetCode 3038 - Maximum Number of Operations With the Same Score I
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

object Solution {
  def maxOperations(nums: Array[Int]): Int = {
    val s = nums(0) + nums(1)
    val n = nums.length
    var ans = 0
    var i = 0
    while (i + 1 < n && nums(i) + nums(i + 1) == s) {
      ans += 1
      i += 2
    }
    ans
  }
}
'''

FILES["3039_apply_operations_to_make_string_empty"] = r'''// LeetCode 3039 - Apply Operations to Make String Empty
// https://leetcode.com/problems/apply-operations-to-make-string-empty/

object Solution {
  def lastNonEmptyString(s: String): String = {
    val cnt = Array.ofDim[Int](26)
    val last = Array.ofDim[Int](26)
    var mx = 0
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i) - 'a'
      cnt(c) += 1
      last(c) = i
      mx = math.max(mx, cnt(c))
      i += 1
    }
    val ans = new StringBuilder
    i = 0
    while (i < s.length) {
      val c = s.charAt(i) - 'a'
      if (cnt(c) == mx && last(c) == i) ans.append(s.charAt(i))
      i += 1
    }
    ans.toString
  }
}
'''

FILES["3040_maximum_number_of_operations_with_the_same_score_ii"] = r'''// LeetCode 3040 - Maximum Number of Operations With the Same Score II
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

object Solution {
  def maxOperations(nums: Array[Int]): Int = {
    val n = nums.length
    var f: Array[Array[Int]] = null
    var s = 0
    def dfs(i: Int, j: Int): Int = {
      if (j - i < 1) return 0
      if (f(i)(j) != -1) return f(i)(j)
      var ans = 0
      if (nums(i) + nums(i + 1) == s) ans = math.max(ans, 1 + dfs(i + 2, j))
      if (nums(i) + nums(j) == s) ans = math.max(ans, 1 + dfs(i + 1, j - 1))
      if (nums(j - 1) + nums(j) == s) ans = math.max(ans, 1 + dfs(i, j - 2))
      f(i)(j) = ans
      ans
    }
    def g(i0: Int, j0: Int, score: Int): Int = {
      f = Array.fill(n, n)(-1)
      s = score
      dfs(i0, j0)
    }
    val a = g(2, n - 1, nums(0) + nums(1))
    val b = g(0, n - 3, nums(n - 1) + nums(n - 2))
    val c = g(1, n - 2, nums(0) + nums(n - 1))
    1 + math.max(a, math.max(b, c))
  }
}
'''

FILES["3041_maximize_consecutive_elements_in_an_array_after_modification"] = r'''// LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
// https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

object Solution {
  def maxSelectedElements(nums: Array[Int]): Int = {
    scala.util.Sorting.quickSort(nums)
    val dp = scala.collection.mutable.HashMap[Int, Int]()
    var ans = 0
    for (num <- nums) {
      val dn = dp.getOrElse(num, 0)
      val dnm1 = dp.getOrElse(num - 1, 0)
      dp(num + 1) = dn + 1
      dp(num) = dnm1 + 1
      ans = math.max(ans, math.max(dp(num), dp(num + 1)))
    }
    ans
  }
}
'''

FILES["3042_count_prefix_and_suffix_pairs_i"] = r'''// LeetCode 3042 - Count Prefix and Suffix Pairs I
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

object Solution {
  def countPrefixSuffixPairs(words: Array[String]): Int = {
    var ans = 0
    var i = 0
    while (i < words.length) {
      val s = words(i)
      var j = i + 1
      while (j < words.length) {
        val t = words(j)
        if (t.length >= s.length && t.startsWith(s) && t.endsWith(s)) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3043_find_the_length_of_the_longest_common_prefix"] = r'''// LeetCode 3043 - Find the Length of the Longest Common Prefix
// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

object Solution {
  def longestCommonPrefix(arr1: Array[Int], arr2: Array[Int]): Int = {
    val s = scala.collection.mutable.HashSet[Int]()
    for (x0 <- arr1) {
      var x = x0
      while (x > 0) { s += x; x /= 10 }
    }
    var mx = 0
    for (x0 <- arr2) {
      var x = x0
      var done = false
      while (x > 0 && !done) {
        if (s.contains(x)) { mx = math.max(mx, x); done = true }
        x /= 10
      }
    }
    if (mx > 0) mx.toString.length else 0
  }
}
'''

FILES["3044_most_frequent_prime"] = r'''// LeetCode 3044 - Most Frequent Prime
// https://leetcode.com/problems/most-frequent-prime/

object Solution {
  private def isPrime(n: Int): Boolean = {
    if (n < 2) return false
    var i = 2
    while (i <= n / i) {
      if (n % i == 0) return false
      i += 1
    }
    true
  }

  def mostFrequentPrime(mat: Array[Array[Int]]): Int = {
    val m = mat.length
    val n = mat(0).length
    val cnt = scala.collection.mutable.HashMap[Int, Int]()
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        var a = -1
        while (a <= 1) {
          var b = -1
          while (b <= 1) {
            if (!(a == 0 && b == 0)) {
              var x = i + a
              var y = j + b
              var v = mat(i)(j)
              while (x >= 0 && x < m && y >= 0 && y < n) {
                v = v * 10 + mat(x)(y)
                if (isPrime(v)) cnt(v) = cnt.getOrElse(v, 0) + 1
                x += a
                y += b
              }
            }
            b += 1
          }
          a += 1
        }
        j += 1
      }
      i += 1
    }
    var ans = -1
    var mx = 0
    for ((key, value) <- cnt) {
      if (mx < value || (mx == value && ans < key)) {
        mx = value
        ans = key
      }
    }
    ans
  }
}
'''

FILES["3045_count_prefix_and_suffix_pairs_ii"] = r'''// LeetCode 3045 - Count Prefix and Suffix Pairs II
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

object Solution {
  private class Node {
    val children = scala.collection.mutable.HashMap[Int, Node]()
    var cnt = 0
  }

  def countPrefixSuffixPairs(words: Array[String]): Long = {
    val trie = new Node
    var ans = 0L
    for (s <- words) {
      var node = trie
      val m = s.length
      var i = 0
      while (i < m) {
        val p = s.charAt(i) * 32 + s.charAt(m - i - 1)
        node = node.children.getOrElseUpdate(p, new Node)
        ans += node.cnt
        i += 1
      }
      node.cnt += 1
    }
    ans
  }
}
'''

FILES["3046_split_the_array"] = r'''// LeetCode 3046 - Split the Array
// https://leetcode.com/problems/split-the-array/

object Solution {
  def isPossibleToSplit(nums: Array[Int]): Boolean = {
    val cnt = Array.ofDim[Int](101)
    for (x <- nums) {
      cnt(x) += 1
      if (cnt(x) >= 3) return false
    }
    true
  }
}
'''

FILES["3047_find_the_largest_area_of_square_inside_two_rectangles"] = r'''// LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
// https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

object Solution {
  def largestSquareArea(bottomLeft: Array[Array[Int]], topRight: Array[Array[Int]]): Long = {
    var ans = 0L
    val n = bottomLeft.length
    var i = 0
    while (i < n) {
      val x1 = bottomLeft(i)(0)
      val y1 = bottomLeft(i)(1)
      val x2 = topRight(i)(0)
      val y2 = topRight(i)(1)
      var j = i + 1
      while (j < n) {
        val x3 = bottomLeft(j)(0)
        val y3 = bottomLeft(j)(1)
        val x4 = topRight(j)(0)
        val y4 = topRight(j)(1)
        val ww = math.min(x2, x4) - math.max(x1, x3)
        val h = math.min(y2, y4) - math.max(y1, y3)
        val e = math.min(ww, h)
        if (e > 0) ans = math.max(ans, e.toLong * e)
        j += 1
      }
      i += 1
    }
    ans
  }
}
'''

FILES["3048_earliest_second_to_mark_indices_i"] = r'''// LeetCode 3048 - Earliest Second to Mark Indices I
// https://leetcode.com/problems/earliest-second-to-mark-indices-i/

object Solution {
  def earliestSecondToMarkIndices(nums: Array[Int], changeIndices: Array[Int]): Int = {
    val n = nums.length
    def ok(t: Int): Boolean = {
      val last = Array.ofDim[Int](n + 1)
      var s = 0
      while (s < t) { last(changeIndices(s)) = s; s += 1 }
      var decrement = 0
      var marked = 0
      s = 0
      while (s < t) {
        val i = changeIndices(s)
        if (last(i) == s) {
          if (decrement < nums(i - 1)) return false
          decrement -= nums(i - 1)
          marked += 1
        } else decrement += 1
        s += 1
      }
      marked == n
    }
    val m = changeIndices.length
    var l = 0
    var r = m + 1
    while (l < r) {
      val mid = (l + r) / 2
      if (ok(mid)) r = mid else l = mid + 1
    }
    if (l > m) -1 else l
  }
}
'''

def main():
    n = 0
    for folder, content in FILES.items():
        (ROOT / folder / "Solution.scala").write_text(content, encoding="utf-8", newline="\n")
        n += 1
        print("wrote", folder)
    print("total", n)

if __name__ == "__main__":
    main()
