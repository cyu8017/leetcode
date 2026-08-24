#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)

w("3049_earliest_second_to_mark_indices_ii", r'''
// LeetCode 3049 - Earliest Second to Mark Indices II
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

object Solution {
  def earliestSecondToMarkIndices(nums: Array[Int], changeIndices: Array[Int]): Int = {
    val secondToIndex = getSecondToIndex(nums, changeIndices)
    var numsSum = 0L
    nums.foreach(v => numsSum += v)
    var l = 0
    var r = changeIndices.length + 1
    while (l < r) {
      val m = (l + r) / 2
      if (canMark(nums, secondToIndex, m, numsSum)) r = m
      else l = m + 1
    }
    if (l <= changeIndices.length) l else -1
  }

  private def getSecondToIndex(nums: Array[Int], changeIndices: Array[Int]): java.util.HashMap[Integer, Integer] = {
    val indexToFirstSecond = new java.util.HashMap[Integer, Integer]()
    var second = 0
    while (second < changeIndices.length) {
      val index = changeIndices(second) - 1
      if (nums(index) > 0 && !indexToFirstSecond.containsKey(index)) {
        indexToFirstSecond.put(index, second)
      }
      second += 1
    }
    val secondToIndex = new java.util.HashMap[Integer, Integer]()
    val it = indexToFirstSecond.entrySet().iterator()
    while (it.hasNext) {
      val e = it.next()
      secondToIndex.put(e.getValue, e.getKey)
    }
    secondToIndex
  }

  private def canMark(
      nums: Array[Int],
      secondToIndex: java.util.HashMap[Integer, Integer],
      maxSecond: Int,
      numsSum: Long
  ): Boolean = {
    val h = new java.util.PriorityQueue[Integer]()
    var marks = 0
    var second = maxSecond - 1
    while (second >= 0) {
      if (secondToIndex.containsKey(second)) {
        h.offer(nums(secondToIndex.get(second)))
        if (marks == 0) {
          h.poll()
          marks += 1
        } else {
          marks -= 1
        }
      } else {
        marks += 1
      }
      second -= 1
    }
    val heapSize = h.size()
    var heapSum = 0L
    while (!h.isEmpty) heapSum += h.poll()
    val decrementAndMarkCost = numsSum - heapSum + (nums.length - heapSize)
    val zeroAndMarkCost = heapSize.toLong + heapSize
    decrementAndMarkCost + zeroAndMarkCost <= maxSecond
  }
}
''')

w("3062_winner_of_the_linked_list_game", r'''
// LeetCode 3062 - Winner of the Linked List Game
// https://leetcode.com/problems/winner-of-the-linked-list-game/

class ListNode(var x: Int = 0) {
  var next: ListNode = null
}

object Solution {
  def gameResult(head: ListNode): String = {
    var odd = 0
    var even = 0
    var cur = head
    while (cur != null) {
      val a = cur.x
      val b = cur.next.x
      if (a < b) odd += 1
      if (a > b) even += 1
      cur = cur.next.next
    }
    if (odd > even) "Odd"
    else if (odd < even) "Even"
    else "Tie"
  }
}
''')

w("3063_linked_list_frequency", r'''
// LeetCode 3063 - Linked List Frequency
// https://leetcode.com/problems/linked-list-frequency/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def frequenciesOfElements(head: ListNode): ListNode = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var cur = head
    while (cur != null) {
      cnt(cur.x) = cnt.getOrElse(cur.x, 0) + 1
      cur = cur.next
    }
    val dummy = new ListNode()
    cnt.values.foreach { v =>
      dummy.next = new ListNode(v, dummy.next)
    }
    dummy.next
  }
}
''')

w("3064_guess_the_number_using_bitwise_questions_i", r'''
// LeetCode 3064 - Guess the Number Using Bitwise Questions I
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

object Solution {
  def commonSetBits(num: Int): Int = throw new NotImplementedError()

  def findNumber(): Int = {
    var n = 0
    var i = 0
    while (i < 32) {
      if (commonSetBits(1 << i) > 0) n |= 1 << i
      i += 1
    }
    n
  }
}
''')

w("3065_minimum_operations_to_exceed_threshold_value_i", r'''
// LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Int = {
    var ans = 0
    nums.foreach { x => if (x < k) ans += 1 }
    ans
  }
}
''')

w("3066_minimum_operations_to_exceed_threshold_value_ii", r'''
// LeetCode 3066 - Minimum Operations to Exceed Threshold Value II
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Int = {
    val pq = new java.util.PriorityQueue[java.lang.Long]()
    nums.foreach(x => pq.offer(x.toLong))
    var ans = 0
    while (pq.size() > 1 && pq.peek() < k) {
      val x = pq.poll()
      val y = pq.poll()
      pq.offer(x * 2 + y)
      ans += 1
    }
    ans
  }
}
''')

w("3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network", r'''
// LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
// https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

object Solution {
  def countPairsOfConnectableServers(edges: Array[Array[Int]], signalSpeed: Int): Array[Int] = {
    val n = edges.length + 1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Array[Int]])
    edges.foreach { e =>
      g(e(0)) += Array(e(1), e(2))
      g(e(1)) += Array(e(0), e(2))
    }

    def dfs(a: Int, fa: Int, ws: Int): Int = {
      var cnt = if (ws % signalSpeed == 0) 1 else 0
      g(a).foreach { e =>
        val b = e(0)
        val w = e(1)
        if (b != fa) cnt += dfs(b, a, ws + w)
      }
      cnt
    }

    val ans = new Array[Int](n)
    var a = 0
    while (a < n) {
      var s = 0
      g(a).foreach { e =>
        val t = dfs(e(0), a, e(1))
        ans(a) += s * t
        s += t
      }
      a += 1
    }
    ans
  }
}
''')

w("3068_find_the_maximum_sum_of_node_values", r'''
// LeetCode 3068 - Find the Maximum Sum of Node Values
// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

object Solution {
  def maximumValueSum(nums: Array[Int], k: Int, edges: Array[Array[Int]]): Long = {
    var f0 = 0L
    var f1 = -0x3f3f3f3fL
    nums.foreach { x =>
      val nf0 = math.max(f0 + x, f1 + (x ^ k))
      val nf1 = math.max(f1 + x, f0 + (x ^ k))
      f0 = nf0
      f1 = nf1
    }
    f0
  }
}
''')

w("3069_distribute_elements_into_two_arrays_i", r'''
// LeetCode 3069 - Distribute Elements Into Two Arrays I
// https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

object Solution {
  def resultArray(nums: Array[Int]): Array[Int] = {
    val arr1 = scala.collection.mutable.ArrayBuffer(nums(0))
    val arr2 = scala.collection.mutable.ArrayBuffer(nums(1))
    var i = 2
    while (i < nums.length) {
      if (arr1.last > arr2.last) arr1 += nums(i)
      else arr2 += nums(i)
      i += 1
    }
    (arr1 ++ arr2).toArray
  }
}
''')

w("3070_count_submatrices_with_top_left_element_and_sum_less_than_k", r'''
// LeetCode 3070 - Count Submatrices with Top-Left Element and Sum Less Than k
// https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

object Solution {
  def countSubmatrices(grid: Array[Array[Int]], k: Int): Int = {
    val n = grid.length
    val m = grid(0).length
    var ans = 0
    val s = Array.fill(n + 1, m + 1)(0)
    var i = 0
    while (i < n) {
      var j = 0
      while (j < m) {
        s(i + 1)(j + 1) = s(i + 1)(j) + s(i)(j + 1) - s(i)(j) + grid(i)(j)
        if (s(i + 1)(j + 1) <= k) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("3071_minimum_operations_to_write_the_letter_y_on_a_grid", r'''
// LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
// https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

object Solution {
  def minimumOperationsToWriteY(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val cnt1 = new Array[Int](3)
    val cnt2 = new Array[Int](3)
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        val x = grid(i)(j)
        val a = i == j && i <= n / 2
        val b = i + j == n - 1 && i <= n / 2
        val c = j == n / 2 && i >= n / 2
        if (a || b || c) cnt1(x) += 1
        else cnt2(x) += 1
        j += 1
      }
      i += 1
    }
    var ans = n * n
    i = 0
    while (i < 3) {
      var j = 0
      while (j < 3) {
        if (i != j) ans = math.min(ans, n * n - cnt1(i) - cnt2(j))
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("3072_distribute_elements_into_two_arrays_ii", r'''
// LeetCode 3072 - Distribute Elements Into Two Arrays II
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

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

  def resultArray(nums: Array[Int]): Array[Int] = {
    val st = nums.sorted
    val n = st.length
    val tree1 = new BIT(n + 1)
    val tree2 = new BIT(n + 1)
    val arr1 = scala.collection.mutable.ArrayBuffer(nums(0))
    val arr2 = scala.collection.mutable.ArrayBuffer(nums(1))
    tree1.update(idx(st, nums(0)), 1)
    tree2.update(idx(st, nums(1)), 1)
    var i = 2
    while (i < nums.length) {
      val x = nums(i)
      val id = idx(st, x)
      val a = arr1.size - tree1.query(id)
      val b = arr2.size - tree2.query(id)
      if (a > b || (a == b && arr1.size <= arr2.size)) {
        arr1 += x
        tree1.update(id, 1)
      } else {
        arr2 += x
        tree2.update(id, 1)
      }
      i += 1
    }
    (arr1 ++ arr2).toArray
  }

  private def idx(st: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = st.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (st(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo + 1
  }
}
''')

w("3073_maximum_increasing_triplet_value", r'''
// LeetCode 3073 - Maximum Increasing Triplet Value
// https://leetcode.com/problems/maximum-increasing-triplet-value/

object Solution {
  def maximumTripletValue(nums: Array[Int]): Int = {
    val n = nums.length
    val right = new Array[Int](n)
    right(n - 1) = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      right(i) = math.max(nums(i), right(i + 1))
      i -= 1
    }
    val ts = new java.util.TreeSet[Integer]()
    ts.add(nums(0))
    var ans = 0
    var j = 1
    while (j < n - 1) {
      if (right(j + 1) > nums(j)) {
        val it = ts.lower(nums(j))
        if (it != null) ans = math.max(ans, it - nums(j) + right(j + 1))
      }
      ts.add(nums(j))
      j += 1
    }
    ans
  }
}
''')

w("3074_apple_redistribution_into_boxes", r'''
// LeetCode 3074 - Apple Redistribution into Boxes
// https://leetcode.com/problems/apple-redistribution-into-boxes/

object Solution {
  def minimumBoxes(apple: Array[Int], capacity: Array[Int]): Int = {
    val cap = capacity.sorted
    var s = 0
    apple.foreach(x => s += x)
    var i = 1
    while (true) {
      s -= cap(cap.length - i)
      if (s <= 0) return i
      i += 1
    }
    0
  }
}
''')

w("3075_maximize_happiness_of_selected_children", r'''
// LeetCode 3075 - Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

object Solution {
  def maximumHappinessSum(happiness: Array[Int], k: Int): Long = {
    val h = happiness.sorted
    var ans = 0L
    var i = 0
    while (i < k) {
      val x = h(h.length - i - 1) - i
      ans += math.max(x, 0)
      i += 1
    }
    ans
  }
}
''')

w("3076_shortest_uncommon_substring_in_an_array", r'''
// LeetCode 3076 - Shortest Uncommon Substring in an Array
// https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

object Solution {
  def shortestSubstrings(arr: Array[String]): Array[String] = {
    val n = arr.length
    val ans = Array.fill(n)("")
    var i = 0
    while (i < n) {
      val s = arr(i)
      val m = s.length
      var j = 1
      while (j <= m && ans(i).isEmpty) {
        var l = 0
        while (l <= m - j) {
          val sub = s.substring(l, l + j)
          if (ans(i).isEmpty || ans(i).compareTo(sub) > 0) {
            var ok = true
            var k = 0
            while (k < n && ok) {
              if (k != i && arr(k).contains(sub)) ok = false
              k += 1
            }
            if (ok) ans(i) = sub
          }
          l += 1
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("3077_maximum_strength_of_k_disjoint_subarrays", r'''
// LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
// https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

object Solution {
  def maximumStrength(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val INF = Long.MinValue / 2
    val f = Array.fill(n + 1, k + 1, 2)(INF)
    f(0)(0)(0) = 0
    var i = 1
    while (i <= n) {
      val x = nums(i - 1).toLong
      var j = 0
      while (j <= k) {
        val sign = if ((j & 1) != 0) 1L else -1L
        val `val` = sign * x * (k - j + 1)
        f(i)(j)(0) = math.max(f(i - 1)(j)(0), f(i - 1)(j)(1))
        f(i)(j)(1) = math.max(f(i)(j)(1), f(i - 1)(j)(1) + `val`)
        if (j > 0) {
          val t = math.max(f(i - 1)(j - 1)(0), f(i - 1)(j - 1)(1)) + `val`
          f(i)(j)(1) = math.max(f(i)(j)(1), t)
        }
        j += 1
      }
      i += 1
    }
    math.max(f(n)(k)(0), f(n)(k)(1))
  }
}
''')

w("3078_match_alphanumerical_pattern_in_matrix_i", r'''
// LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
// https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

object Solution {
  def findPattern(board: Array[Array[Int]], pattern: Array[String]): Array[Int] = {
    val m = board.length
    val n = board(0).length
    val r = pattern.length
    val c = pattern(0).length
    var i = 0
    while (i < m - r + 1) {
      var j = 0
      while (j < n - c + 1) {
        if (check(board, pattern, i, j, r, c)) return Array(i, j)
        j += 1
      }
      i += 1
    }
    Array(-1, -1)
  }

  private def check(board: Array[Array[Int]], pattern: Array[String], i: Int, j: Int, r: Int, c: Int): Boolean = {
    val d1 = new Array[Int](26)
    val d2 = new Array[Int](10)
    var a = 0
    while (a < r) {
      var b = 0
      while (b < c) {
        val x = i + a
        val y = j + b
        val ch = pattern(a).charAt(b)
        if (ch >= '0' && ch <= '9') {
          if (ch - '0' != board(x)(y)) return false
        } else {
          val v = ch - 'a'
          if (d1(v) > 0 && d1(v) - 1 != board(x)(y)) return false
          if (d2(board(x)(y)) > 0 && d2(board(x)(y)) - 1 != v) return false
          d1(v) = board(x)(y) + 1
          d2(board(x)(y)) = v + 1
        }
        b += 1
      }
      a += 1
    }
    true
  }
}
''')

w("3079_find_the_sum_of_encrypted_integers", r'''
// LeetCode 3079 - Find the Sum of Encrypted Integers
// https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

object Solution {
  def sumOfEncryptedInt(nums: Array[Int]): Int = {
    var ans = 0
    nums.foreach(x => ans += encrypt(x))
    ans
  }

  private def encrypt(x0: Int): Int = {
    var x = x0
    var mx = 0
    var p = 0
    while (x > 0) {
      mx = math.max(mx, x % 10)
      p = p * 10 + 1
      x /= 10
    }
    mx * p
  }
}
''')

w("3080_mark_elements_on_array_by_performing_queries", r'''
// LeetCode 3080 - Mark Elements on Array by Performing Queries
// https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

object Solution {
  def unmarkedSumArray(nums: Array[Int], queries: Array[Array[Int]]): Array[Long] = {
    val n = nums.length
    var s = 0L
    nums.foreach(x => s += x)
    val mark = new Array[Boolean](n)
    val arr = Array.tabulate(n)(i => Array(nums(i), i))
    scala.util.Sorting.stableSort(arr, (a: Array[Int], b: Array[Int]) =>
      if (a(0) != b(0)) a(0) < b(0) else a(1) < b(1)
    )
    val ans = new Array[Long](queries.length)
    var j = 0
    var qi = 0
    while (qi < queries.length) {
      val index = queries(qi)(0)
      var k = queries(qi)(1)
      if (!mark(index)) {
        mark(index) = true
        s -= nums(index)
      }
      while (k > 0 && j < n) {
        if (!mark(arr(j)(1))) {
          mark(arr(j)(1)) = true
          s -= arr(j)(0)
          k -= 1
        }
        j += 1
      }
      ans(qi) = s
      qi += 1
    }
    ans
  }
}
''')

w("3081_replace_question_marks_in_string_to_minimize_its_value", r'''
// LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
// https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

object Solution {
  def minimizeStringValue(s: String): String = {
    val cnt = new Array[Int](26)
    var k = 0
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i)
      if (c == '?') k += 1
      else cnt(c - 'a') += 1
      i += 1
    }
    val pq = new java.util.PriorityQueue[Array[Int]](
      (a: Array[Int], b: Array[Int]) => if (a(0) != b(0)) a(0) - b(0) else a(1) - b(1)
    )
    i = 0
    while (i < 26) {
      pq.offer(Array(cnt(i), i))
      i += 1
    }
    val t = new Array[Int](k)
    i = 0
    while (i < k) {
      val p = pq.poll()
      t(i) = p(1)
      p(0) += 1
      pq.offer(p)
      i += 1
    }
    java.util.Arrays.sort(t)
    val arr = s.toCharArray
    var j = 0
    i = 0
    while (i < arr.length) {
      if (arr(i) == '?') {
        arr(i) = (t(j) + 'a').toChar
        j += 1
      }
      i += 1
    }
    new String(arr)
  }
}
''')

w("3082_find_the_sum_of_the_power_of_all_subsequences", r'''
// LeetCode 3082 - Find the Sum of the Power of All Subsequences
// https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

object Solution {
  def sumOfPower(nums: Array[Int], k: Int): Int = {
    val MOD = 1000000007
    val n = nums.length
    val f = Array.ofDim[Int](n + 1, k + 1)
    f(0)(0) = 1
    var i = 1
    while (i <= n) {
      var j = 0
      while (j <= k) {
        f(i)(j) = ((f(i - 1)(j).toLong * 2) % MOD).toInt
        if (j >= nums(i - 1)) f(i)(j) = (f(i)(j) + f(i - 1)(j - nums(i - 1))) % MOD
        j += 1
      }
      i += 1
    }
    f(n)(k)
  }
}
''')

w("3083_existence_of_a_substring_in_a_string_and_its_reverse", r'''
// LeetCode 3083 - Existence of a Substring in a String and Its Reverse
// https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

object Solution {
  def isSubstringPresent(s: String): Boolean = {
    val st = Array.ofDim[Boolean](26, 26)
    var i = 0
    while (i + 1 < s.length) {
      st(s.charAt(i + 1) - 'a')(s.charAt(i) - 'a') = true
      i += 1
    }
    i = 0
    while (i + 1 < s.length) {
      if (st(s.charAt(i) - 'a')(s.charAt(i + 1) - 'a')) return true
      i += 1
    }
    false
  }
}
''')

w("3084_count_substrings_starting_and_ending_with_given_character", r'''
// LeetCode 3084 - Count Substrings Starting and Ending with Given Character
// https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

object Solution {
  def countSubstrings(s: String, c: Char): Long = {
    var cnt = 0L
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == c) cnt += 1
      i += 1
    }
    cnt * (cnt + 1) / 2
  }
}
''')

w("3085_minimum_deletions_to_make_string_k_special", r'''
// LeetCode 3085 - Minimum Deletions to Make String K-Special
// https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

object Solution {
  def minimumDeletions(word: String, k: Int): Int = {
    val freq = new Array[Int](26)
    var i = 0
    while (i < word.length) {
      freq(word.charAt(i) - 'a') += 1
      i += 1
    }
    val nums = freq.filter(_ > 0)
    var ans = word.length
    i = 0
    while (i <= word.length) {
      var cur = 0
      nums.foreach { x =>
        if (x < i) cur += x
        else if (x > i + k) cur += x - i - k
      }
      ans = math.min(ans, cur)
      i += 1
    }
    ans
  }
}
''')
