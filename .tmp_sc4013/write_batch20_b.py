#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("3744_find_kth_character_in_expanded_string", r'''
// LeetCode 3744 - Find Kth Character in Expanded String
// https://leetcode.com/problems/find-kth-character-in-expanded-string/

object Solution {
  def kthCharacter(s: String, k0: Long): Char = {
    var k = k0
    val words = s.trim.split("\\s+")
    words.foreach { w =>
      val m = (1L + w.length) * w.length / 2
      if (k == m) return ' '
      if (k > m) {
        k -= m + 1
      } else {
        var cur = 0L
        var i = 0
        while (true) {
          cur += i + 1
          if (k < cur) return w.charAt(i)
          i += 1
        }
      }
    }
    ' '
  }
}
''')

w("3745_maximize_expression_of_three_elements", r'''
// LeetCode 3745 - Maximize Expression of Three Elements
// https://leetcode.com/problems/maximize-expression-of-three-elements/

object Solution {
  def maximizeExpressionOfThree(nums: Array[Int]): Int = {
    val inf = 1 << 30
    var a = -inf
    var b = -inf
    var c = inf
    nums.foreach { x =>
      if (x < c) c = x
      if (x >= a) { b = a; a = x }
      else if (x > b) b = x
    }
    a + b - c
  }
}
''')

w("3746_minimum_string_length_after_balanced_removals", r'''
// LeetCode 3746 - Minimum String Length After Balanced Removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

object Solution {
  def minLengthAfterRemovals(s: String): Int = {
    var a = 0
    s.foreach(c => if (c == 'a') a += 1)
    val b = s.length - a
    math.abs(a - b)
  }
}
''')

w("3747_count_distinct_integers_after_removing_zeros", r'''
// LeetCode 3747 - Count Distinct Integers After Removing Zeros
// https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

object Solution {
  def countDistinct(n: Long): Long = {
    val s = java.lang.Long.toString(n)
    val m = s.length
    val f = Array.fill(20, 2, 2, 2)(-1L)

    def dfs(i: Int, zero: Int, lead: Int, limit: Int): Long = {
      if (i == m) return if (zero == 0 && lead == 0) 1 else 0
      if (limit == 0 && f(i)(zero)(lead)(limit) != -1) return f(i)(zero)(lead)(limit)
      val up = if (limit == 1) s.charAt(i) - '0' else 9
      var ans = 0L
      var d = 0
      while (d <= up) {
        var nxtZero = zero
        if (d == 0 && lead == 0) nxtZero = 1
        val nxtLead = if (lead == 1 && d == 0) 1 else 0
        val nxtLimit = if (limit == 1 && d == up) 1 else 0
        ans += dfs(i + 1, nxtZero, nxtLead, nxtLimit)
        d += 1
      }
      if (limit == 0) f(i)(zero)(lead)(limit) = ans
      ans
    }

    dfs(0, 0, 1, 1)
  }
}
''')

w("3748_count_stable_subarrays", r'''
// LeetCode 3748 - Count Stable Subarrays
// https://leetcode.com/problems/count-stable-subarrays/

object Solution {
  def countStableSubarrays(nums: Array[Int], queries: Array[Array[Int]]): Array[Long] = {
    val n = nums.length
    val seg = new java.util.ArrayList[Integer]()
    val s = new java.util.ArrayList[java.lang.Long]()
    s.add(0L)
    var l = 0
    var r = 0
    while (r < n) {
      if (r == n - 1 || nums(r) > nums(r + 1)) {
        seg.add(l)
        val k = (r - l + 1).toLong
        s.add(s.get(s.size() - 1) + k * (k + 1) / 2)
        l = r + 1
      }
      r += 1
    }
    val ans = new Array[Long](queries.length)
    var idx = 0
    while (idx < queries.length) {
      val left = queries(idx)(0)
      val right = queries(idx)(1)
      val i = lowerBound(seg, left + 1)
      val j = lowerBound(seg, right + 1) - 1
      if (i > j) {
        val k = (right - left + 1).toLong
        ans(idx) = k * (k + 1) / 2
      } else {
        val a = seg.get(i).toLong - left
        val b = right.toLong - seg.get(j) + 1
        ans(idx) = a * (a + 1) / 2 + s.get(j) - s.get(i) + b * (b + 1) / 2
      }
      idx += 1
    }
    ans
  }

  private def lowerBound(a: java.util.List[Integer], x: Int): Int = {
    var lo = 0
    var hi = a.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a.get(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
''')

w("3749_evaluate_valid_expressions", r'''
// LeetCode 3749 - Evaluate Valid Expressions
// https://leetcode.com/problems/evaluate-valid-expressions/

object Solution {
  def evaluateExpression(expression: String): Long = {
    def parse(i0: Int): Array[Long] = {
      val ch = expression.charAt(i0)
      if (Character.isDigit(ch) || ch == '-') {
        var j = i0
        if (expression.charAt(j) == '-') j += 1
        while (j < expression.length && Character.isDigit(expression.charAt(j))) j += 1
        return Array(java.lang.Long.parseLong(expression.substring(i0, j)), j.toLong)
      }
      var j = i0
      while (expression.charAt(j) != '(') j += 1
      val op = expression.substring(i0, j)
      j += 1
      val p1 = parse(j)
      j = p1(1).toInt + 1
      val p2 = parse(j)
      j = p2(1).toInt + 1
      var res = 0L
      if (op == "add") res = p1(0) + p2(0)
      else if (op == "sub") res = p1(0) - p2(0)
      else if (op == "mul") res = p1(0) * p2(0)
      else if (op == "div") res = p1(0) / p2(0)
      Array(res, j.toLong)
    }
    parse(0)(0)
  }
}
''')

w("3750_minimum_number_of_flips_to_reverse_binary_string", r'''
// LeetCode 3750 - Minimum Number Of Flips To Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

object Solution {
  def minimumFlips(n: Int): Int = {
    var x = n.toLong
    val s = if (x == 0) "0" else {
      val sb = new StringBuilder
      while (x > 0) {
        sb.append(('0' + (x & 1).toInt).toChar)
        x >>= 1
      }
      val arr = sb.toString.toCharArray
      reverse(arr, 0, arr.length)
      new String(arr)
    }
    val m = s.length
    var cnt = 0
    var i = 0
    while (i < m / 2) {
      if (s.charAt(i) != s.charAt(m - i - 1)) cnt += 1
      i += 1
    }
    cnt * 2
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

w("3751_total_waviness_of_numbers_in_range_i", r'''
// LeetCode 3751 - Total Waviness Of Numbers In Range I
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

object Solution {
  private def F(x0: Int): Int = {
    var x = x0
    val nums = new java.util.ArrayList[Integer]()
    while (x > 0) {
      nums.add(x % 10)
      x /= 10
    }
    val m = nums.size()
    if (m < 3) return 0
    var s = 0
    var i = 1
    while (i < m - 1) {
      if ((nums.get(i) > nums.get(i - 1) && nums.get(i) > nums.get(i + 1)) ||
          (nums.get(i) < nums.get(i - 1) && nums.get(i) < nums.get(i + 1))) s += 1
      i += 1
    }
    s
  }

  def totalWaviness(num1: Int, num2: Int): Int = {
    var ans = 0
    var x = num1
    while (x <= num2) {
      ans += F(x)
      x += 1
    }
    ans
  }
}
''')

w("3752_lexicographically_smallest_negated_permutation_that_sums_to_target", r'''
// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

object Solution {
  def lexicographicallySmallest(n: Int, target: Long): Array[Int] = {
    val total = 1L * n * (n + 1) / 2
    if (target < -total || target > total || (total - target) % 2 != 0) return Array.emptyIntArray
    var remaining = (total - target) / 2
    val negative = new Array[Boolean](n + 1)
    var value = n
    while (value >= 1) {
      if (value <= remaining) {
        negative(value) = true
        remaining -= value
      }
      value -= 1
    }
    val answer = new java.util.ArrayList[Integer]()
    value = n
    while (value >= 1) {
      if (negative(value)) answer.add(-value)
      value -= 1
    }
    value = 1
    while (value <= n) {
      if (!negative(value)) answer.add(value)
      value += 1
    }
    val out = new Array[Int](answer.size())
    var i = 0
    while (i < out.length) {
      out(i) = answer.get(i)
      i += 1
    }
    out
  }
}
''')

w("3753_total_waviness_of_numbers_in_range_ii", r'''
// LeetCode 3753 - Total Waviness Of Numbers In Range II
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

object Solution {
  private class Result(var count: Long = 0, var sum: Long = 0)

  private def wavinessUpTo(limit: Long): Long = {
    if (limit < 0) return 0
    val digits = new java.util.ArrayList[Integer]()
    if (limit == 0) digits.add(0)
    else {
      var value = limit
      while (value > 0) {
        digits.add((value % 10).toInt)
        value /= 10
      }
      java.util.Collections.reverse(digits)
    }
    val memo = new java.util.HashMap[String, Result]()
    dfs(0, 10, 10, started = false, tight = true, digits, memo).sum
  }

  private def dfs(
      position: Int,
      secondLast: Int,
      last: Int,
      started: Boolean,
      tight: Boolean,
      digits: java.util.List[Integer],
      memo: java.util.HashMap[String, Result]
  ): Result = {
    if (position == digits.size()) return new Result(1, 0)
    val key = position + "," + secondLast + "," + last + "," + started
    if (!tight && memo.containsKey(key)) return memo.get(key)
    val upper = if (tight) digits.get(position) else 9
    val result = new Result()
    var digit = 0
    while (digit <= upper) {
      val nextTight = tight && digit == upper
      var nextSecondLast = secondLast
      var nextLast = last
      val nextStarted = started || digit != 0
      var add = 0L
      if (!nextStarted) {
        nextSecondLast = 10
        nextLast = 10
      } else if (!started) {
        nextSecondLast = 10
        nextLast = digit
      } else {
        if (secondLast != 10 &&
            ((last > secondLast && last > digit) || (last < secondLast && last < digit))) {
          add = 1
        }
        nextSecondLast = last
        nextLast = digit
      }
      val child = dfs(position + 1, nextSecondLast, nextLast, nextStarted, nextTight, digits, memo)
      result.count += child.count
      result.sum += child.sum + add * child.count
      digit += 1
    }
    if (!tight) memo.put(key, result)
    result
  }

  def totalWaviness(a: Long, b: Long): Long = wavinessUpTo(b) - wavinessUpTo(a - 1)
}
''')

w("3754_concatenate_non_zero_digits_and_multiply_by_sum_i", r'''
// LeetCode 3754 - Concatenate Non Zero Digits And Multiply By Sum I
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

object Solution {
  def sumAndMultiply(n0: Int): Long = {
    var n = n0
    var p = 1
    var x = 0
    var s = 0
    while (n > 0) {
      val v = n % 10
      if (v != 0) {
        s += v
        x += p * v
        p *= 10
      }
      n /= 10
    }
    1L * x * s
  }
}
''')

w("3755_find_maximum_balanced_xor_subarray_length", r'''
// LeetCode 3755 - Find Maximum Balanced Xor Subarray Length
// https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/

object Solution {
  def maxBalancedSubarray(nums: Array[Int]): Int = {
    val d = new java.util.HashMap[java.lang.Long, Integer]()
    var a = 0
    var b = nums.length
    var ans = 0
    d.put(b.toLong, -1)
    var i = 0
    while (i < nums.length) {
      a ^= nums(i)
      if (nums(i) % 2 == 0) b += 1 else b -= 1
      val key = (a.toLong << 32) | (b & 0xffffffffL)
      if (d.containsKey(key)) ans = math.max(ans, i - d.get(key))
      else d.put(key, i)
      i += 1
    }
    ans
  }
}
''')

w("3756_concatenate_non_zero_digits_and_multiply_by_sum_ii", r'''
// LeetCode 3756 - Concatenate Non Zero Digits And Multiply By Sum II
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

object Solution {
  private val MX = 100001
  private val MOD = 1000000007L
  private val PW: Array[Long] = {
    val arr = new Array[Long](MX)
    arr(0) = 1
    var i = 1
    while (i < MX) {
      arr(i) = arr(i - 1) * 10 % MOD
      i += 1
    }
    arr
  }

  def sumAndMultiply(s: String, queries: Array[Array[Int]]): Array[Int] = {
    val n = s.length
    val sumD = new Array[Int](n + 1)
    val cntN0 = new Array[Int](n + 1)
    val p = new Array[Long](n + 1)
    var i = 1
    while (i <= n) {
      val d = (s.charAt(i - 1) - '0').toLong
      sumD(i) = sumD(i - 1) + d.toInt
      cntN0(i) = cntN0(i - 1)
      if (d > 0) {
        cntN0(i) += 1
        p(i) = (p(i - 1) * 10 + d) % MOD
      } else p(i) = p(i - 1)
      i += 1
    }
    val ans = new Array[Int](queries.length)
    i = 0
    while (i < queries.length) {
      val l = queries(i)(0)
      val r = queries(i)(1)
      val n0 = cntN0(r + 1) - cntN0(l)
      val sd = (sumD(r + 1) - sumD(l)).toLong
      val x = (p(r + 1) - p(l) * PW(n0) % MOD + MOD) % MOD
      ans(i) = (x * sd % MOD).toInt
      i += 1
    }
    ans
  }
}
''')

w("3757_number_of_effective_subsequences", r'''
// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

object Solution {
  private def PopCount(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x != 0) { c += x & 1; x >>= 1 }
    c
  }

  def countEffectiveSubsequences(nums: Array[Int]): Int = {
    val mod = 1000000007
    var all = 0
    nums.foreach(x => all |= x)
    val bits = new java.util.ArrayList[Integer]()
    var b = 0
    while (b < 20) {
      if (((all >> b) & 1) != 0) bits.add(b)
      b += 1
    }
    val m = bits.size()
    val freq = new Array[Int](1 << m)
    nums.foreach { x =>
      var mask = 0
      var i = 0
      while (i < m) {
        if (((x >> bits.get(i)) & 1) != 0) mask |= 1 << i
        i += 1
      }
      freq(mask) += 1
    }
    val disjoint = freq.clone()
    b = 0
    while (b < m) {
      var mask = 0
      while (mask < (1 << m)) {
        if (((mask >> b) & 1) != 0) disjoint(mask) += disjoint(mask ^ (1 << b))
        mask += 1
      }
      b += 1
    }
    val pow2 = new Array[Int](nums.length + 1)
    pow2(0) = 1
    var i = 1
    while (i <= nums.length) {
      pow2(i) = pow2(i - 1) * 2 % mod
      i += 1
    }
    var ans = 0
    val full = (1 << m) - 1
    var s = 1
    while (s <= full) {
      val ways = pow2(disjoint(full ^ s))
      val bc = PopCount(s)
      if ((bc & 1) != 0) {
        ans += ways
        if (ans >= mod) ans -= mod
      } else {
        ans -= ways
        if (ans < 0) ans += mod
      }
      s += 1
    }
    ans
  }
}
''')

w("3758_convert_number_words_to_digits", r'''
// LeetCode 3758 - Convert Number Words To Digits
// https://leetcode.com/problems/convert-number-words-to-digits/

object Solution {
  def convertNumber(s: String): String = {
    val d = Array("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    val n = s.length
    val ans = new StringBuilder
    var i = 0
    while (i < n) {
      var j = 0
      var matched = false
      while (j < 10 && !matched) {
        val m = d(j).length
        if (i + m <= n && s.substring(i, i + m) == d(j)) {
          ans.append(('0' + j).toChar)
          i += m - 1
          matched = true
        }
        j += 1
      }
      i += 1
    }
    ans.toString
  }
}
''')

w("3759_count_elements_with_at_least_k_greater_values", r'''
// LeetCode 3759 - Count Elements With At Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

object Solution {
  def countElements(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    if (k == 0) return n
    java.util.Arrays.sort(nums)
    var ans = 0
    var i = 0
    while (i < n - k) {
      if (nums(n - k) > nums(i)) ans += 1
      i += 1
    }
    ans
  }
}
''')
