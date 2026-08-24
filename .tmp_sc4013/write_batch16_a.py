#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3285_find_indices_of_stable_mountains"] = """// LeetCode 3285 - Find Indices of Stable Mountains
// https://leetcode.com/problems/find-indices-of-stable-mountains/

object Solution {
  def stableMountains(height: Array[Int], threshold: Int): Array[Int] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 1
    while (i < height.length) {
      if (height(i - 1) > threshold) ans += i
      i += 1
    }
    ans.toArray
  }
}
"""

FILES["3286_find_a_safe_walk_through_a_grid"] = """// LeetCode 3286 - Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

object Solution {
  def findSafeWalk(grid: Array[Array[Int]], health: Int): Boolean = {
    val m = grid.length
    val n = grid(0).length
    val vis = Array.fill(m, n)(-1)
    val qh = health - grid(0)(0)
    if (qh <= 0) return false
    val q = scala.collection.mutable.Queue[(Int, Int, Int)]()
    q.enqueue((0, 0, qh))
    vis(0)(0) = qh
    val dirs = Array((0, 1), (1, 0), (0, -1), (-1, 0))
    while (q.nonEmpty) {
      val (r, c, h) = q.dequeue()
      if (r == m - 1 && c == n - 1) return true
      for ((dr, dc) <- dirs) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nc >= 0 && nr < m && nc < n) {
          val nh = h - grid(nr)(nc)
          if (nh > 0 && nh > vis(nr)(nc)) {
            vis(nr)(nc) = nh
            q.enqueue((nr, nc, nh))
          }
        }
      }
    }
    false
  }
}
"""

FILES["3287_find_the_maximum_sequence_value_of_array"] = """// LeetCode 3287 - Find the Maximum Sequence Value of Array
// https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

object Solution {
  def maxValue(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val MAX = 128
    val left = Array.ofDim[Boolean](n + 1, k + 1, MAX)
    left(0)(0)(0) = true
    var i = 0
    while (i < n) {
      var j = 0
      while (j <= k) {
        var v = 0
        while (v < MAX) {
          if (left(i)(j)(v)) {
            left(i + 1)(j)(v) = true
            if (j < k) left(i + 1)(j + 1)(v | nums(i)) = true
          }
          v += 1
        }
        j += 1
      }
      i += 1
    }
    val right = Array.ofDim[Boolean](n + 1, k + 1, MAX)
    right(n)(0)(0) = true
    i = n - 1
    while (i >= 0) {
      var j = 0
      while (j <= k) {
        var v = 0
        while (v < MAX) {
          if (right(i + 1)(j)(v)) {
            right(i)(j)(v) = true
            if (j < k) right(i)(j + 1)(v | nums(i)) = true
          }
          v += 1
        }
        j += 1
      }
      i -= 1
    }
    var ans = 0
    var mid = k
    while (mid + k <= n) {
      var a = 0
      while (a < MAX) {
        if (left(mid)(k)(a)) {
          var b = 0
          while (b < MAX) {
            if (right(mid)(k)(b) && (a ^ b) > ans) ans = a ^ b
            b += 1
          }
        }
        a += 1
      }
      mid += 1
    }
    ans
  }
}
"""

FILES["3288_length_of_the_longest_increasing_path"] = """// LeetCode 3288 - Length of the Longest Increasing Path
// https://leetcode.com/problems/length-of-the-longest-increasing-path/

object Solution {
  private def lis(a: Array[Int]): Int = {
    val tails = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (x <- a) {
      var lo = 0
      var hi = tails.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (tails(mid) < x) lo = mid + 1
        else hi = mid
      }
      if (lo == tails.length) tails += x
      else tails(lo) = x
    }
    tails.length
  }

  def maxPathLength(coordinates: Array[Array[Int]], k: Int): Int = {
    val n = coordinates.length
    val arr = Array.tabulate(n)(i => Array(coordinates(i)(0), coordinates(i)(1), i))
    scala.util.Sorting.stableSort(arr, (a: Array[Int], b: Array[Int]) =>
      if (a(0) == b(0)) a(1) > b(1) else a(0) < b(0)
    )
    val kx = coordinates(k)(0)
    val ky = coordinates(k)(1)
    val left = scala.collection.mutable.ArrayBuffer.empty[Int]
    val right = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (p <- arr) {
      if (p(0) < kx && p(1) < ky) left += p(1)
      if (p(0) > kx && p(1) > ky) right += p(1)
    }
    lis(left.toArray) + 1 + lis(right.toArray)
  }
}
"""

FILES["3289_the_two_sneaky_numbers_of_digitville"] = """// LeetCode 3289 - The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

object Solution {
  def getSneakyNumbers(nums: Array[Int]): Array[Int] = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (x <- nums) {
      if (!seen.add(x)) ans += x
    }
    ans.toArray
  }
}
"""

FILES["3290_maximum_multiplication_score"] = """// LeetCode 3290 - Maximum Multiplication Score
// https://leetcode.com/problems/maximum-multiplication-score/

object Solution {
  def maxScore(a: Array[Int], b: Array[Int]): Long = {
    val neg = -(1L << 62)
    val dp = Array(0L, neg, neg, neg, neg)
    for (x <- b) {
      var k = 4
      while (k >= 1) {
        if (dp(k - 1) != neg) {
          val v = dp(k - 1) + a(k - 1).toLong * x
          if (v > dp(k)) dp(k) = v
        }
        k -= 1
      }
    }
    dp(4)
  }
}
"""

FILES["3291_minimum_number_of_valid_strings_to_form_target_i"] = """// LeetCode 3291 - Minimum Number of Valid Strings to Form Target I
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/

object Solution {
  private class TrieNode {
    val next = new Array[TrieNode](26)
  }

  def minValidStrings(words: Array[String], target: String): Int = {
    val n = target.length
    val inf = 1000000000
    val dp = Array.fill(n + 1)(inf)
    dp(0) = 0
    val root = new TrieNode
    for (w <- words) {
      var cur = root
      for (c <- w) {
        val ci = c - 'a'
        if (cur.next(ci) == null) cur.next(ci) = new TrieNode
        cur = cur.next(ci)
      }
    }
    var i = 0
    while (i < n) {
      if (dp(i) != inf) {
        var cur = root
        var j = i
        while (j < n) {
          val ci = target.charAt(j) - 'a'
          if (cur.next(ci) == null) { j = n }
          else {
            cur = cur.next(ci)
            if (dp(i) + 1 < dp(j + 1)) dp(j + 1) = dp(i) + 1
            j += 1
          }
        }
      }
      i += 1
    }
    if (dp(n) == inf) -1 else dp(n)
  }
}
"""

FILES["3292_minimum_number_of_valid_strings_to_form_target_ii"] = """// LeetCode 3292 - Minimum Number of Valid Strings to Form Target II
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/

object Solution {
  private class TrieNode {
    val next = new Array[TrieNode](26)
  }

  def minValidStrings(words: Array[String], target: String): Int = {
    val n = target.length
    val inf = 1000000000
    val dp = Array.fill(n + 1)(inf)
    dp(0) = 0
    val root = new TrieNode
    for (w <- words) {
      var cur = root
      for (c <- w) {
        val ci = c - 'a'
        if (cur.next(ci) == null) cur.next(ci) = new TrieNode
        cur = cur.next(ci)
      }
    }
    var i = 0
    while (i < n) {
      if (dp(i) != inf) {
        var cur = root
        var j = i
        while (j < n) {
          val ci = target.charAt(j) - 'a'
          if (cur.next(ci) == null) { j = n }
          else {
            cur = cur.next(ci)
            if (dp(i) + 1 < dp(j + 1)) dp(j + 1) = dp(i) + 1
            j += 1
          }
        }
      }
      i += 1
    }
    if (dp(n) == inf) -1 else dp(n)
  }
}
"""

FILES["3294_convert_doubly_linked_list_to_array_ii"] = """// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

class Node(var x: Int = 0, var prev: Node = null, var next: Node = null)

object Solution {
  def toArray(node: Node): Array[Int] = {
    var cur = node
    while (cur != null && cur.prev != null) cur = cur.prev
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    while (cur != null) {
      ans += cur.x
      cur = cur.next
    }
    ans.toArray
  }
}
"""

FILES["3295_report_spam_message"] = """// LeetCode 3295 - Report Spam Message
// https://leetcode.com/problems/report-spam-message/

object Solution {
  def reportSpam(message: Array[String], bannedWords: Array[String]): Boolean = {
    val ban = bannedWords.toSet
    var cnt = 0
    for (w <- message) {
      if (ban.contains(w)) {
        cnt += 1
        if (cnt >= 2) return true
      }
    }
    false
  }
}
"""

FILES["3296_minimum_number_of_seconds_to_make_mountain_height_zero"] = """// LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

object Solution {
  def minNumberOfSeconds(mountainHeight: Int, workerTimes: Array[Int]): Long = {
    var lo = 0L
    var hi = 1000000000000000000L
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(mid, mountainHeight, workerTimes)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(t: Long, mountainHeight: Int, workerTimes: Array[Int]): Boolean = {
    var total = 0L
    for (w <- workerTimes) {
      var l = 0L
      var h = mountainHeight.toLong
      while (l < h) {
        val mid = (l + h + 1) / 2
        if (w.toLong * mid * (mid + 1) / 2 <= t) l = mid
        else h = mid - 1
      }
      total += l
      if (total >= mountainHeight) return true
    }
    total >= mountainHeight
  }
}
"""

FILES["3297_count_substrings_that_can_be_rearranged_to_contain_a_string_i"] = """// LeetCode 3297 - Count Substrings That Can Be Rearranged to Contain a String I
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

object Solution {
  def validSubstringCount(word1: String, word2: String): Long = {
    val need = new Array[Int](26)
    var required = 0
    for (c <- word2) {
      if (need(c - 'a') == 0) required += 1
      need(c - 'a') += 1
    }
    val have = new Array[Int](26)
    var formed = 0
    var ans = 0L
    var l = 0
    var r = 0
    while (r < word1.length) {
      val c = word1.charAt(r) - 'a'
      have(c) += 1
      if (have(c) == need(c) && need(c) > 0) formed += 1
      while (formed == required && l <= r) {
        ans += word1.length - r
        val c2 = word1.charAt(l) - 'a'
        if (have(c2) == need(c2) && need(c2) > 0) formed -= 1
        have(c2) -= 1
        l += 1
      }
      r += 1
    }
    ans
  }
}
"""

FILES["3298_count_substrings_that_can_be_rearranged_to_contain_a_string_ii"] = """// LeetCode 3298 - Count Substrings That Can Be Rearranged to Contain a String II
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/

object Solution {
  def validSubstringCount(word1: String, word2: String): Long = {
    val need = new Array[Int](26)
    var required = 0
    for (c <- word2) {
      if (need(c - 'a') == 0) required += 1
      need(c - 'a') += 1
    }
    val have = new Array[Int](26)
    var formed = 0
    var ans = 0L
    var l = 0
    var r = 0
    while (r < word1.length) {
      val c = word1.charAt(r) - 'a'
      have(c) += 1
      if (have(c) == need(c) && need(c) > 0) formed += 1
      while (formed == required && l <= r) {
        ans += word1.length - r
        val c2 = word1.charAt(l) - 'a'
        if (have(c2) == need(c2) && need(c2) > 0) formed -= 1
        have(c2) -= 1
        l += 1
      }
      r += 1
    }
    ans
  }
}
"""

FILES["3299_sum_of_consecutive_subsequences"] = """// LeetCode 3299 - Sum of Consecutive Subsequences
// https://leetcode.com/problems/sum-of-consecutive-subsequences/

object Solution {
  def rangeSum(nums: Array[Int]): Int = {
    val mod = 1000000007
    val cnt = scala.collection.mutable.HashMap.empty[Int, Int]
    val sum = scala.collection.mutable.HashMap.empty[Int, Int]
    var ans = 0
    for (x <- nums) {
      val cL = cnt.getOrElse(x - 1, 0)
      val sL = sum.getOrElse(x - 1, 0)
      val cR = cnt.getOrElse(x + 1, 0)
      val sR = sum.getOrElse(x + 1, 0)
      var c = (1 + cL + cR) % mod
      var s = ((x.toLong + sL + cL.toLong * x % mod + sR + cR.toLong * x % mod) % mod).toInt
      if (cL > 0 && cR > 0) {
        c = (c + (cL.toLong * cR % mod).toInt) % mod
        s = ((s + sL.toLong * cR % mod + sR.toLong * cL % mod + cL.toLong * cR % mod * x % mod) % mod).toInt
      }
      cnt(x) = (cnt.getOrElse(x, 0) + c) % mod
      sum(x) = (sum.getOrElse(x, 0) + s) % mod
      ans = (ans + s) % mod
    }
    ans
  }
}
"""

FILES["3300_minimum_element_after_replacement_with_digit_sum"] = """// LeetCode 3300 - Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

object Solution {
  def minElement(nums: Array[Int]): Int = {
    var ans = 1000000000
    for (num <- nums) {
      var x = num
      var s = 0
      while (x > 0) {
        s += x % 10
        x /= 10
      }
      if (s < ans) ans = s
    }
    ans
  }
}
"""

FILES["3301_maximize_the_total_height_of_unique_towers"] = """// LeetCode 3301 - Maximize the Total Height of Unique Towers
// https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

object Solution {
  def maximumTotalSum(maximumHeight: Array[Int]): Long = {
    val h = maximumHeight.sorted.reverse
    var ans = 0L
    var prev = 1000000000000000000L
    for (mh <- h) {
      var cur = mh.toLong
      if (cur >= prev) cur = prev - 1
      if (cur <= 0) return -1
      ans += cur
      prev = cur
    }
    ans
  }
}
"""

FILES["3302_find_the_lexicographically_smallest_valid_sequence"] = """// LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

object Solution {
  private def canFinish(w1: String, w2: String, i: Int, j: Int, usedSkip: Boolean, right: Array[Int]): Boolean = {
    val m = w2.length
    if (j >= m) return true
    if (!usedSkip) {
      if (right(j) >= i) return true
      if (j + 1 <= m && right(j + 1) > i) return true
      if (right(j) > i) return true
      return false
    }
    right(j) >= i
  }

  def validSequence(word1: String, word2: String): Array[Int] = {
    val n = word1.length
    val m = word2.length
    val right = new Array[Int](m + 1)
    right(m) = n
    var j = m - 1
    var i = n - 1
    while (i >= 0 && j >= 0) {
      if (word1.charAt(i) == word2.charAt(j)) {
        right(j) = i
        j -= 1
      }
      i -= 1
    }
    while (j >= 0) {
      right(j) = -1
      j -= 1
    }
    val ans = new Array[Int](m)
    var usedSkip = false
    i = 0
    j = 0
    while (j < m) {
      var found = false
      while (i < n && !found) {
        if (word1.charAt(i) == word2.charAt(j)) {
          if (canFinish(word1, word2, i + 1, j + 1, usedSkip, right)) {
            ans(j) = i
            i += 1
            found = true
          } else i += 1
        } else if (!usedSkip) {
          if (canFinish(word1, word2, i + 1, j + 1, true, right)) {
            ans(j) = i
            i += 1
            usedSkip = true
            found = true
          } else i += 1
        } else i += 1
      }
      if (!found) return Array.emptyIntArray
      j += 1
    }
    ans
  }
}
"""

FILES["3303_find_the_occurrence_of_first_almost_equal_substring"] = """// LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

object Solution {
  def minStartingIndex(s: String, pattern: String): Int = {
    val n = s.length
    val m = pattern.length
    var i = 0
    while (i + m <= n) {
      var diff = 0
      var j = 0
      while (j < m) {
        if (s.charAt(i + j) != pattern.charAt(j)) {
          diff += 1
          if (diff > 1) j = m
        }
        if (j < m) j += 1
      }
      if (diff <= 1) return i
      i += 1
    }
    -1
  }
}
"""

FILES["3304_find_the_k_th_character_in_string_game_i"] = """// LeetCode 3304 - Find the K-th Character in String Game I
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

object Solution {
  def kthCharacter(k: Int): Char = {
    val s = new StringBuilder("a")
    while (s.length < k) {
      val n = s.length
      var i = 0
      while (i < n) {
        s.append(('a' + ((s.charAt(i) - 'a' + 1) % 26)).toChar)
        i += 1
      }
    }
    s.charAt(k - 1)
  }
}
"""

FILES["3305_count_of_substrings_containing_every_vowel_and_k_consonants_i"] = """// LeetCode 3305 - Count of Substrings Containing Every Vowel and K Consonants I
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/

object Solution {
  private def isVowel(c: Char): Boolean =
    c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'

  private def atLeast(word: String, k: Int): Int = {
    val cnt = scala.collection.mutable.HashMap.empty[Char, Int]
    var cons = 0
    var l = 0
    var ans = 0
    var r = 0
    while (r < word.length) {
      val c = word.charAt(r)
      if (isVowel(c)) cnt(c) = cnt.getOrElse(c, 0) + 1
      else cons += 1
      while (cnt.size == 5 && cons >= k) {
        ans += word.length - r
        val c2 = word.charAt(l)
        if (isVowel(c2)) {
          val nv = cnt(c2) - 1
          if (nv == 0) cnt.remove(c2)
          else cnt(c2) = nv
        } else cons -= 1
        l += 1
      }
      r += 1
    }
    ans
  }

  def countOfSubstrings(word: String, k: Int): Int = atLeast(word, k) - atLeast(word, k + 1)
}
"""

FILES["3306_count_of_substrings_containing_every_vowel_and_k_consonants_ii"] = """// LeetCode 3306 - Count of Substrings Containing Every Vowel and K Consonants II
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

object Solution {
  private def isVowel(c: Char): Boolean =
    c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'

  private def atLeast(word: String, k: Int): Long = {
    val cnt = scala.collection.mutable.HashMap.empty[Char, Int]
    var cons = 0
    var l = 0
    var ans = 0L
    var r = 0
    while (r < word.length) {
      val c = word.charAt(r)
      if (isVowel(c)) cnt(c) = cnt.getOrElse(c, 0) + 1
      else cons += 1
      while (cnt.size == 5 && cons >= k) {
        ans += word.length - r
        val c2 = word.charAt(l)
        if (isVowel(c2)) {
          val nv = cnt(c2) - 1
          if (nv == 0) cnt.remove(c2)
          else cnt(c2) = nv
        } else cons -= 1
        l += 1
      }
      r += 1
    }
    ans
  }

  def countOfSubstrings(word: String, k: Int): Long = atLeast(word, k) - atLeast(word, k + 1)
}
"""

FILES["3307_find_the_k_th_character_in_string_game_ii"] = """// LeetCode 3307 - Find the K-th Character in String Game II
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

object Solution {
  def kthCharacter(k: Long, operations: Array[Int]): Char = {
    var kk = k
    var shift = 0
    val ops = operations.toBuffer
    while (ops.nonEmpty) {
      val op = ops.remove(ops.length - 1)
      val half = 1L << ops.length
      if (kk > half) {
        kk -= half
        if (op == 1) shift += 1
      }
    }
    ('a' + shift % 26).toChar
  }
}
"""

FILES["3309_maximum_possible_number_by_binary_concatenation"] = """// LeetCode 3309 - Maximum Possible Number by Binary Concatenation
// https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

object Solution {
  private def toBin(x: Int): String = {
    if (x == 0) return "0"
    val s = new StringBuilder
    var y = x
    while (y > 0) {
      s.insert(0, ('0' + (y & 1)).toChar)
      y >>= 1
    }
    s.toString
  }

  def maxGoodNumber(nums: Array[Int]): Int = {
    val bs = Array.tabulate(3)(i => toBin(nums(i)))
    val idx = Array(0, 1, 2)
    val ans = Array(0)
    perm(0, idx, bs, ans)
    ans(0)
  }

  private def perm(i: Int, idx: Array[Int], bs: Array[String], ans: Array[Int]): Unit = {
    if (i == 3) {
      val s = bs(idx(0)) + bs(idx(1)) + bs(idx(2))
      var v = 0
      for (c <- s) v = v * 2 + (c - '0')
      if (v > ans(0)) ans(0) = v
      return
    }
    var j = i
    while (j < 3) {
      val t = idx(i); idx(i) = idx(j); idx(j) = t
      perm(i + 1, idx, bs, ans)
      val t2 = idx(i); idx(i) = idx(j); idx(j) = t2
      j += 1
    }
  }
}
"""

FILES["3310_remove_methods_from_project"] = """// LeetCode 3310 - Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/

object Solution {
  def remainingMethods(n: Int, k: Int, invocations: Array[Array[Int]]): Array[Int] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- invocations) g(e(0)) += e(1)
    val sus = new Array[Boolean](n)
    def dfs(u: Int): Unit = {
      if (sus(u)) return
      sus(u) = true
      for (v <- g(u)) dfs(v)
    }
    dfs(k)
    for (e <- invocations) {
      if (!sus(e(0)) && sus(e(1))) return Array.range(0, n)
    }
    (0 until n).filter(!sus(_)).toArray
  }
}
"""

FILES["3311_construct_2d_grid_matching_graph_layout"] = """// LeetCode 3311 - Construct 2D Grid Matching Graph Layout
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

object Solution {
  def constructGridLayout(n: Int, edges: Array[Array[Int]]): Array[Array[Int]] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val deg = Array.tabulate(n)(i => g(i).length)
    var start = 0
    var i = 0
    while (i < n) {
      if (deg(i) == 1) { start = i; i = n }
      else {
        if (deg(i) == 2) start = i
        i += 1
      }
    }
    val vis = new Array[Boolean](n)
    val row = scala.collection.mutable.ArrayBuffer.empty[Int]
    var cur = start
    var prev = -1
    var done = false
    while (!done) {
      row += cur
      vis(cur) = true
      var next = -1
      for (v <- g(cur)) {
        if (v != prev && !vis(v) && deg(v) <= 3) {
          next = v
          if (deg(v) < 4) { /* prefer */ }
        }
      }
      if (next == -1) done = true
      else {
        prev = cur
        cur = next
      }
    }
    var width = row.length
    var height = if (width != 0) n / width else n
    if (width == 0 || width * height != n) {
      var w = 1
      var found = false
      while (w <= n && !found) {
        if (n % w == 0) {
          width = w
          height = n / w
          found = true
        }
        w += 1
      }
    }
    val grid = Array.ofDim[Int](height, width)
    i = 0
    while (i < n) {
      grid(i / width)(i % width) = i
      i += 1
    }
    grid
  }
}
"""

FILES["3312_sorted_gcd_pair_queries"] = """// LeetCode 3312 - Sorted GCD Pair Queries
// https://leetcode.com/problems/sorted-gcd-pair-queries/

object Solution {
  def gcdValues(nums: Array[Int], queries: Array[Long]): Array[Int] = {
    var maxV = 0
    for (x <- nums) if (x > maxV) maxV = x
    val cnt = new Array[Int](maxV + 1)
    for (x <- nums) cnt(x) += 1
    val divCnt = new Array[Long](maxV + 1)
    var g = 1
    while (g <= maxV) {
      var c = 0L
      var m = g
      while (m <= maxV) {
        c += cnt(m)
        m += g
      }
      divCnt(g) = c * (c - 1) / 2
      g += 1
    }
    val exact = new Array[Long](maxV + 1)
    g = maxV
    while (g >= 1) {
      exact(g) = divCnt(g)
      var m = 2 * g
      while (m <= maxV) {
        exact(g) -= exact(m)
        m += g
      }
      g -= 1
    }
    val pref = new Array[Long](maxV + 1)
    g = 1
    while (g <= maxV) {
      pref(g) = pref(g - 1) + exact(g)
      g += 1
    }
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      val q = queries(i)
      var lo = 1
      var hi = maxV
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (pref(mid) > q) hi = mid
        else lo = mid + 1
      }
      ans(i) = lo
      i += 1
    }
    ans
  }
}
"""

FILES["3313_find_the_last_marked_nodes_in_tree"] = """// LeetCode 3313 - Find the Last Marked Nodes in Tree
// https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

object Solution {
  def lastMarkedNodes(edges: Array[Array[Int]]): Array[Int] = {
    val n = edges.length + 1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    def bfs(start: Int): (Int, Array[Int]) = {
      val dist = Array.fill(n)(-1)
      val q = scala.collection.mutable.Queue[Int]()
      q.enqueue(start)
      dist(start) = 0
      var far = start
      while (q.nonEmpty) {
        val u = q.dequeue()
        if (dist(u) > dist(far)) far = u
        for (v <- g(u)) {
          if (dist(v) == -1) {
            dist(v) = dist(u) + 1
            q.enqueue(v)
          }
        }
      }
      (far, dist)
    }
    val u = bfs(0)._1
    val (v, du) = bfs(u)
    val dv = bfs(v)._2
    Array.tabulate(n)(i => if (du(i) >= dv(i)) u else v)
  }
}
"""

FILES["3314_construct_the_minimum_bitwise_array_i"] = """// LeetCode 3314 - Construct the Minimum Bitwise Array I
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

object Solution {
  def minBitwiseArray(nums: Array[Int]): Array[Int] = {
    val ans = Array.fill(nums.length)(-1)
    var i = 0
    while (i < nums.length) {
      val n = nums(i)
      var x = 0
      var found = false
      while (x < n && !found) {
        if ((x | (x + 1)) == n) {
          ans(i) = x
          found = true
        }
        x += 1
      }
      i += 1
    }
    ans
  }
}
"""

FILES["3315_construct_the_minimum_bitwise_array_ii"] = """// LeetCode 3315 - Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

object Solution {
  def minBitwiseArray(nums: Array[Int]): Array[Int] = {
    val ans = Array.fill(nums.length)(-1)
    var i = 0
    while (i < nums.length) {
      val n = nums(i)
      if (n != 2) {
        var b = 0
        var found = false
        while (b < 31 && !found) {
          if (((n >> b) & 1) != 0) {
            val x = n ^ (1 << b)
            if ((x | (x + 1)) == n) {
              ans(i) = x
              found = true
            }
          }
          b += 1
        }
      }
      i += 1
    }
    ans
  }
}
"""

FILES["3316_find_maximum_removals_from_source_string"] = """// LeetCode 3316 - Find Maximum Removals From Source String
// https://leetcode.com/problems/find-maximum-removals-from-source-string/

object Solution {
  def maxRemovals(source: String, pattern: String, targetIndices: Array[Int]): Int = {
    val n = source.length
    var lo = 0
    var hi = targetIndices.length
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(mid, source, pattern, targetIndices, n)) lo = mid
      else hi = mid - 1
    }
    lo
  }

  private def ok(removeFirst: Int, source: String, pattern: String, targetIndices: Array[Int], n: Int): Boolean = {
    val mark = new Array[Boolean](n)
    var i = 0
    while (i < removeFirst) {
      mark(targetIndices(i)) = true
      i += 1
    }
    var j = 0
    i = 0
    while (i < n && j < pattern.length) {
      if (!mark(i) && source.charAt(i) == pattern.charAt(j)) j += 1
      i += 1
    }
    j == pattern.length
  }
}
"""

FILES["3317_find_the_number_of_possible_ways_for_an_event"] = """// LeetCode 3317 - Find the Number of Possible Ways for an Event
// https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

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

  def numberOfWays(n: Int, x: Int, y: Int): Int = {
    val mod = 1000000007
    val dp = Array.ofDim[Int](n + 1, x + 1)
    dp(0)(0) = 1
    var i = 1
    while (i <= n) {
      var j = 1
      while (j <= x && j <= i) {
        dp(i)(j) = (dp(i - 1)(j - 1) + (j.toLong * dp(i - 1)(j) % mod).toInt) % mod
        j += 1
      }
      i += 1
    }
    val fact = new Array[Int](x + 1)
    fact(0) = 1
    i = 1
    while (i <= x) {
      fact(i) = (fact(i - 1).toLong * i % mod).toInt
      i += 1
    }
    var ans = 0
    var ypow = 1
    var k = 1
    while (k <= x && k <= n) {
      ypow = (ypow.toLong * y % mod).toInt
      val perm = (fact(x).toLong * modPow(fact(x - k).toLong, mod - 2, mod) % mod).toInt
      ans = (ans + (dp(n)(k).toLong * perm % mod * ypow % mod).toInt) % mod
      k += 1
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
    print(f"batch_a written={written}")

if __name__ == "__main__":
    main()
