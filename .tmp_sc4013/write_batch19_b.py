#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3643_flip_square_submatrix_vertically"] = r'''// LeetCode 3643 - Flip Square Submatrix Vertically
// https://leetcode.com/problems/flip-square-submatrix-vertically/

object Solution {
  def reverseSubmatrix(grid: Array[Array[Int]], x: Int, y: Int, k: Int): Array[Array[Int]] = {
    var i = x
    while (i < x + k / 2) {
      val i2 = x + k - 1 - (i - x)
      var j = y
      while (j < y + k) {
        val tmp = grid(i)(j)
        grid(i)(j) = grid(i2)(j)
        grid(i2)(j) = tmp
        j += 1
      }
      i += 1
    }
    grid
  }
}
'''

FILES["3644_maximum_k_to_sort_a_permutation"] = r'''// LeetCode 3644 - Maximum K to Sort a Permutation
// https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

object Solution {
  def sortPermutation(nums: Array[Int]): Int = {
    var ans = -1
    var i = 0
    while (i < nums.length) {
      if (i != nums(i)) ans &= nums(i)
      i += 1
    }
    math.max(ans, 0)
  }
}
'''

FILES["3645_maximum_total_from_optimal_activation_order"] = r'''// LeetCode 3645 - Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

object Solution {
  def maxTotal(value: Array[Int], limit: Array[Int]): Long = {
    val g = new java.util.HashMap[Integer, java.util.List[Integer]]()
    var i = 0
    while (i < value.length) {
      g.computeIfAbsent(limit(i), _ => new java.util.ArrayList[Integer]()).add(value(i))
      i += 1
    }
    var ans = 0L
    val it = g.entrySet().iterator()
    while (it.hasNext) {
      val e = it.next()
      val lim = e.getKey.intValue()
      val vs = e.getValue
      vs.sort(java.util.Collections.reverseOrder())
      i = 0
      while (i < math.min(lim, vs.size())) {
        ans += vs.get(i)
        i += 1
      }
    }
    ans
  }
}
'''

FILES["3646_next_special_palindrome_number"] = r'''// LeetCode 3646 - Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/

object Solution {
  def specialPalindrome(n: Long): Long = {
    val cands = new java.util.ArrayList[java.lang.Long]()
    var halfCnt = new Array[Int](10)
    var mid = 0
    var halfLen = 0

    def dfs(pos: Int, cur: java.util.List[Integer]): Unit = {
      if (pos == halfLen) {
        val left = new StringBuilder
        val it = cur.iterator()
        while (it.hasNext) left.append(it.next().intValue())
        val s = new StringBuilder(left)
        if (mid > 0) s.append(mid)
        var i = left.length - 1
        while (i >= 0) {
          s.append(left.charAt(i))
          i -= 1
        }
        cands.add(java.lang.Long.parseLong(s.toString))
        return
      }
      var d = 1
      while (d <= 9) {
        if (halfCnt(d) != 0) {
          halfCnt(d) -= 1
          cur.add(d)
          dfs(pos + 1, cur)
          cur.remove(cur.size() - 1)
          halfCnt(d) += 1
        }
        d += 1
      }
    }

    def gen(mask: Int): Unit = {
      var total = 0
      var odd = 0
      var d = 1
      while (d <= 9) {
        if (((mask >> d) & 1) != 0) {
          total += d
          if (d % 2 == 1) odd += 1
        }
        d += 1
      }
      if (total == 0 || total > 18 || odd > 1) return
      halfCnt = new Array[Int](10)
      mid = 0
      d = 1
      while (d <= 9) {
        if (((mask >> d) & 1) != 0) {
          halfCnt(d) = d / 2
          if (d % 2 == 1) mid = d
        }
        d += 1
      }
      halfLen = total / 2
      dfs(0, new java.util.ArrayList[Integer]())
    }

    var mask = 1
    while (mask < (1 << 10)) {
      if ((mask & 1) == 0) gen(mask)
      mask += 1
    }
    java.util.Collections.sort(cands)
    val it = cands.iterator()
    while (it.hasNext) {
      val v = it.next().longValue()
      if (v > n) return v
    }
    -1L
  }
}
'''

FILES["3647_maximum_weight_in_two_bags"] = r'''// LeetCode 3647 - Maximum Weight in Two Bags
// https://leetcode.com/problems/maximum-weight-in-two-bags/

object Solution {
  def maxWeight(weights: Array[Int], w1: Int, w2: Int): Int = {
    val f = Array.ofDim[Int](w1 + 1, w2 + 1)
    for (x <- weights) {
      var j = w1
      while (j >= 0) {
        var k = w2
        while (k >= 0) {
          if (x <= j) f(j)(k) = math.max(f(j)(k), f(j - x)(k) + x)
          if (x <= k) f(j)(k) = math.max(f(j)(k), f(j)(k - x) + x)
          k -= 1
        }
        j -= 1
      }
    }
    f(w1)(w2)
  }
}
'''

FILES["3648_minimum_sensors_to_cover_grid"] = r'''// LeetCode 3648 - Minimum Sensors to Cover Grid
// https://leetcode.com/problems/minimum-sensors-to-cover-grid/

object Solution {
  def minSensors(n: Int, m: Int, k: Int): Int = {
    val cover = 2 * k + 1
    ((n + cover - 1) / cover) * ((m + cover - 1) / cover)
  }
}
'''

FILES["3649_number_of_perfect_pairs"] = r'''// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

object Solution {
  def perfectPairs(nums: Array[Int]): Long = {
    val n = nums.length
    val absNums = new Array[Int](n)
    var i = 0
    while (i < n) {
      absNums(i) = math.abs(nums(i))
      i += 1
    }
    java.util.Arrays.sort(absNums)
    var ans = 0L
    var j = 0
    i = 0
    while (i < n) {
      if (j < i + 1) j = i + 1
      while (j < n && absNums(j) <= 2 * absNums(i)) j += 1
      ans += j - i - 1
      i += 1
    }
    ans
  }
}
'''

FILES["3650_minimum_cost_path_with_edge_reversals"] = r'''// LeetCode 3650 - Minimum Cost Path with Edge Reversals
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

object Solution {
  def minCost(n: Int, edges: Array[Array[Int]]): Int = {
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      val w = e(2)
      g(u).add(Array(v, w))
      g(v).add(Array(u, w * 2))
    }
    val inf = Int.MaxValue / 2
    val dist = Array.fill(n)(inf)
    dist(0) = 0
    val pq = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    pq.offer(Array(0, 0))
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val d = cur(0)
      val u = cur(1)
      if (d <= dist(u)) {
        if (u == n - 1) return d
        val it = g(u).iterator()
        while (it.hasNext) {
          val e = it.next()
          val v = e(0)
          val w = e(1)
          val nd = d + w
          if (nd < dist(v)) {
            dist(v) = nd
            pq.offer(Array(nd, v))
          }
        }
      }
    }
    -1
  }
}
'''

FILES["3651_minimum_cost_path_with_teleportations"] = r'''// LeetCode 3651 - Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

object Solution {
  def minCost(grid: Array[Array[Int]], k: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    val inf = Int.MaxValue / 4
    val f = Array.ofDim[Int](k + 1, m, n)
    var t = 0
    while (t <= k) {
      var i = 0
      while (i < m) {
        java.util.Arrays.fill(f(t)(i), inf)
        i += 1
      }
      t += 1
    }
    f(0)(0)(0) = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (i > 0) f(0)(i)(j) = math.min(f(0)(i)(j), f(0)(i - 1)(j) + grid(i)(j))
        if (j > 0) f(0)(i)(j) = math.min(f(0)(i)(j), f(0)(i)(j - 1) + grid(i)(j))
        j += 1
      }
      i += 1
    }
    val g = new java.util.TreeMap[Integer, java.util.List[Array[Int]]]((a: Integer, b: Integer) => Integer.compare(b, a))
    i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        g.computeIfAbsent(grid(i)(j), _ => new java.util.ArrayList[Array[Int]]()).add(Array(i, j))
        j += 1
      }
      i += 1
    }
    t = 1
    while (t <= k) {
      var mn = inf
      val vit = g.values().iterator()
      while (vit.hasNext) {
        val pos = vit.next()
        val pit = pos.iterator()
        while (pit.hasNext) {
          val p = pit.next()
          mn = math.min(mn, f(t - 1)(p(0))(p(1)))
        }
        val pit2 = pos.iterator()
        while (pit2.hasNext) {
          val p = pit2.next()
          f(t)(p(0))(p(1)) = mn
        }
      }
      i = 0
      while (i < m) {
        var j = 0
        while (j < n) {
          if (i > 0) f(t)(i)(j) = math.min(f(t)(i)(j), f(t)(i - 1)(j) + grid(i)(j))
          if (j > 0) f(t)(i)(j) = math.min(f(t)(i)(j), f(t)(i)(j - 1) + grid(i)(j))
          j += 1
        }
        i += 1
      }
      t += 1
    }
    var ans = inf
    t = 0
    while (t <= k) {
      ans = math.min(ans, f(t)(m - 1)(n - 1))
      t += 1
    }
    ans
  }
}
'''

FILES["3652_best_time_to_buy_and_sell_stock_using_strategy"] = r'''// LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

object Solution {
  def maxProfit(prices: Array[Int], strategy: Array[Int], k: Int): Long = {
    val n = prices.length
    val s = new Array[Long](n + 1)
    val t = new Array[Long](n + 1)
    var i = 1
    while (i <= n) {
      s(i) = s(i - 1) + 1L * prices(i - 1) * strategy(i - 1)
      t(i) = t(i - 1) + prices(i - 1)
      i += 1
    }
    var ans = s(n)
    i = k
    while (i <= n) {
      ans = math.max(ans, s(n) - (s(i) - s(i - k)) + (t(i) - t(i - k / 2)))
      i += 1
    }
    ans
  }
}
'''

FILES["3653_xor_after_range_multiplication_queries_i"] = r'''// LeetCode 3653 - XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

object Solution {
  def xorAfterQueries(nums: Array[Int], queries: Array[Array[Int]]): Int = {
    val mod = 1000000007
    for (q <- queries) {
      val l = q(0)
      val r = q(1)
      val k = q(2)
      val v = q(3)
      var idx = l
      while (idx <= r) {
        nums(idx) = ((1L * nums(idx) * v) % mod).toInt
        idx += k
      }
    }
    var ans = 0
    for (x <- nums) ans ^= x
    ans
  }
}
'''

FILES["3654_minimum_sum_after_divisible_sum_deletions"] = r'''// LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

object Solution {
  def minArraySum(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val prefix = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = (prefix(i) + nums(i)) % k
      i += 1
    }
    val inf = 1L << 62
    val dp = new Array[Long](n + 1)
    val best = Array.fill(k)(inf)
    best(0) = 0
    i = 1
    while (i <= n) {
      dp(i) = dp(i - 1) + nums(i - 1)
      if (best(prefix(i)) < dp(i)) dp(i) = best(prefix(i))
      if (dp(i) < best(prefix(i))) best(prefix(i)) = dp(i)
      i += 1
    }
    dp(n)
  }
}
'''

FILES["3655_xor_after_range_multiplication_queries_ii"] = r'''// LeetCode 3655 - XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

object Solution {
  def xorAfterQueries(nums: Array[Int], queries: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val n = nums.length
    val byK = new java.util.HashMap[Integer, java.util.List[Array[Int]]]()
    for (q <- queries)
      byK.computeIfAbsent(q(2), _ => new java.util.ArrayList[Array[Int]]()).add(Array(q(0), q(1), q(2), q(3)))
    val res = nums.clone()
    val it = byK.entrySet().iterator()
    while (it.hasNext) {
      val e = it.next()
      val fac = new Array[Int](n)
      java.util.Arrays.fill(fac, 1)
      val uit = e.getValue.iterator()
      while (uit.hasNext) {
        val u = uit.next()
        var i = u(0)
        while (i <= u(1)) {
          fac(i) = ((1L * fac(i) * u(3)) % MOD).toInt
          i += u(2)
        }
      }
      var i = 0
      while (i < n) {
        res(i) = ((1L * res(i) * fac(i)) % MOD).toInt
        i += 1
      }
    }
    var ans = 0
    for (v <- res) ans ^= v
    ans
  }
}
'''

FILES["3656_determine_if_a_simple_graph_exists"] = r'''// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

object Solution {
  def simpleGraphExists(degrees: Array[Int]): Boolean = {
    val n = degrees.length
    val d = degrees.clone()
    java.util.Arrays.sort(d)
    var i = 0
    var j = n - 1
    while (i < j) {
      val tmp = d(i)
      d(i) = d(j)
      d(j) = tmp
      i += 1
      j -= 1
    }
    var sum = 0L
    for (x <- d) {
      if (x < 0 || x >= n) return false
      sum += x
    }
    if (sum % 2 == 1) return false
    val prefix = new Array[Long](n + 1)
    i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + d(i)
      i += 1
    }
    var k = 1
    while (k <= n) {
      var right = 0L
      i = k
      while (i < n) {
        right += (if (d(i) < k) d(i) else k)
        i += 1
      }
      if (prefix(k) > 1L * k * (k - 1) + right) return false
      k += 1
    }
    true
  }
}
'''

FILES["3658_gcd_of_odd_and_even_sums"] = r'''// LeetCode 3658 - GCD of Odd and Even Sums
// https://leetcode.com/problems/gcd-of-odd-and-even-sums/

object Solution {
  def gcdOfOddEvenSums(n: Int): Int = n
}
'''

FILES["3659_partition_array_into_k_distinct_groups"] = r'''// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

object Solution {
  def partitionArray(nums: Array[Int], k: Int): Boolean = {
    val n = nums.length
    if (n % k != 0) return false
    val m = n / k
    var mx = 0
    for (x <- nums) mx = math.max(mx, x)
    val cnt = new Array[Int](mx + 1)
    for (x <- nums) {
      cnt(x) += 1
      if (cnt(x) > m) return false
    }
    true
  }
}
'''

FILES["3660_jump_game_ix"] = r'''// LeetCode 3660 - Jump Game IX
// https://leetcode.com/problems/jump-game-ix/

object Solution {
  def maxValue(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val ans = new Array[Int](n)
    val preMax = new Array[Int](n)
    preMax(0) = nums(0)
    var i = 1
    while (i < n) {
      preMax(i) = math.max(preMax(i - 1), nums(i))
      i += 1
    }
    var sufMin = Int.MaxValue / 2
    i = n - 1
    while (i >= 0) {
      if (preMax(i) > sufMin) ans(i) = ans(i + 1)
      else ans(i) = preMax(i)
      sufMin = math.min(sufMin, nums(i))
      i -= 1
    }
    ans
  }
}
'''

FILES["3661_maximum_walls_destroyed_by_robots"] = r'''// LeetCode 3661 - Maximum Walls Destroyed by Robots
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

object Solution {
  def maxWalls(robots: Array[Int], distance: Array[Int], walls: Array[Int]): Int = {
    val n = robots.length
    val arr = Array.ofDim[Int](n, 2)
    var i = 0
    while (i < n) {
      arr(i)(0) = robots(i)
      arr(i)(1) = distance(i)
      i += 1
    }
    java.util.Arrays.sort(arr, (a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    java.util.Arrays.sort(walls)
    val memo = new java.util.HashMap[java.lang.Long, Integer]()

    def lowerBound(a: Array[Int], target: Int): Int = {
      var lo = 0
      var hi = a.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (a(mid) < target) lo = mid + 1
        else hi = mid
      }
      lo
    }

    def dfs(ii: Int, j: Int): Int = {
      if (ii < 0) return 0
      val key = (ii.toLong << 1) | j
      if (memo.containsKey(key)) return memo.get(key)
      var left = arr(ii)(0) - arr(ii)(1)
      if (ii > 0) left = math.max(left, arr(ii - 1)(0) + 1)
      var l = lowerBound(walls, left)
      var r = lowerBound(walls, arr(ii)(0) + 1)
      var ans = dfs(ii - 1, 0) + (r - l)
      var right = arr(ii)(0) + arr(ii)(1)
      if (ii + 1 < arr.length) {
        if (j == 0) right = math.min(right, arr(ii + 1)(0) - arr(ii + 1)(1) - 1)
        else right = math.min(right, arr(ii + 1)(0) - 1)
      }
      l = lowerBound(walls, arr(ii)(0))
      r = lowerBound(walls, right + 1)
      ans = math.max(ans, dfs(ii - 1, 1) + (r - l))
      memo.put(key, ans)
      ans
    }
    dfs(n - 1, 1)
  }
}
'''

FILES["3662_filter_characters_by_frequency"] = r'''// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

object Solution {
  def filterCharacters(s: String, k: Int): String = {
    val cnt = new Array[Int](26)
    for (c <- s) cnt(c - 'a') += 1
    val ans = new StringBuilder
    for (c <- s) if (cnt(c - 'a') < k) ans.append(c)
    ans.toString
  }
}
'''

FILES["3663_find_the_least_frequent_digit"] = r'''// LeetCode 3663 - Find The Least Frequent Digit
// https://leetcode.com/problems/find-the-least-frequent-digit/

object Solution {
  def getLeastFrequentDigit(n: Int): Int = {
    val cnt = new Array[Int](10)
    var ans = 0
    var f = 1 << 30
    var x = n
    while (x > 0) {
      cnt(x % 10) += 1
      x /= 10
    }
    var d = 0
    while (d < 10) {
      if (cnt(d) > 0 && cnt(d) < f) {
        f = cnt(d)
        ans = d
      }
      d += 1
    }
    ans
  }
}
'''

FILES["3664_two_letter_card_game"] = r'''// LeetCode 3664 - Two-Letter Card Game
// https://leetcode.com/problems/two-letter-card-game/

object Solution {
  private def pairGroup(arr: Array[Int]): Array[Int] = {
    var total = 0
    var mx = 0
    var i = 0
    while (i < 26) {
      total += arr(i)
      mx = math.max(mx, arr(i))
      i += 1
    }
    var pairs = total / 2
    if (total - mx < pairs) pairs = total - mx
    Array(pairs, total - 2 * pairs)
  }

  def score(cards: Array[String], x: Char): Int = {
    var xx = 0
    val left = new Array[Int](26)
    val right = new Array[Int](26)
    for (c <- cards) {
      val a = c.charAt(0)
      val b = c.charAt(1)
      if (a == x && b == x) xx += 1
      else if (a == x) left(b - 'a') += 1
      else if (b == x) right(a - 'a') += 1
    }
    val lp = pairGroup(left)
    val rp = pairGroup(right)
    var ans = lp(0) + rp(0)
    val rem = lp(1) + rp(1)
    val use = math.min(xx, rem)
    ans += use
    xx -= use
    ans += xx / 2
    ans
  }
}
'''

FILES["3665_twisted_mirror_path_count"] = r'''// LeetCode 3665 - Twisted Mirror Path Count
// https://leetcode.com/problems/twisted-mirror-path-count/

object Solution {
  def uniquePaths(grid: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val m = grid.length
    val n = grid(0).length

    def nextCell(i: Int, j: Int, di0: Int, dj0: Int): Array[Int] = {
      var di = di0
      var dj = dj0
      var ni = i + di
      var nj = j + dj
      while (ni >= 0 && nj >= 0 && ni < m && nj < n && grid(ni)(nj) == 1) {
        if (dj == 1) {
          di = 1
          dj = 0
        } else {
          di = 0
          dj = 1
        }
        ni += di
        nj += dj
      }
      if (ni < 0 || nj < 0 || ni >= m || nj >= n) null
      else Array(ni, nj)
    }

    val dp = Array.ofDim[Int](m, n)
    if (grid(0)(0) == 1) return 0
    dp(0)(0) = 1
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (!(grid(i)(j) == 1 || dp(i)(j) == 0)) {
          val a = nextCell(i, j, 0, 1)
          if (a != null) dp(a(0))(a(1)) = (dp(a(0))(a(1)) + dp(i)(j)) % MOD
          val b = nextCell(i, j, 1, 0)
          if (b != null) dp(b(0))(b(1)) = (dp(b(0))(b(1)) + dp(i)(j)) % MOD
        }
        j += 1
      }
      i += 1
    }
    dp(m - 1)(n - 1)
  }
}
'''

FILES["3666_minimum_operations_to_equalize_binary_string"] = r'''// LeetCode 3666 - Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

object Solution {
  def minOperations(s: String, k: Int): Int = {
    val n = s.length
    val ts = Array.fill(2)(new java.util.TreeSet[Integer]())
    var i = 0
    while (i <= n) {
      ts(i % 2).add(i)
      i += 1
    }
    var cnt0 = 0
    for (c <- s) if (c == '0') cnt0 += 1
    ts(cnt0 % 2).remove(cnt0)
    var q = new java.util.ArrayList[Integer]()
    q.add(cnt0)
    var ans = 0
    while (!q.isEmpty) {
      val nq = new java.util.ArrayList[Integer]()
      val qit = q.iterator()
      while (qit.hasNext) {
        val cur = qit.next().intValue()
        if (cur == 0) return ans
        val l = cur + k - 2 * math.min(cur, k)
        val r = cur + k - 2 * math.max(k - n + cur, 0)
        val t = ts(l % 2)
        var it = t.ceiling(l)
        while (it != null && it <= r) {
          nq.add(it)
          t.remove(it)
          it = t.ceiling(l)
        }
      }
      q = nq
      ans += 1
    }
    -1
  }
}
'''

FILES["3667_sort_array_by_absolute_value"] = r'''// LeetCode 3667 - Sort Array By Absolute Value
// https://leetcode.com/problems/sort-array-by-absolute-value/

object Solution {
  def sortByAbsoluteValue(nums: Array[Int]): Array[Int] = {
    val boxed = new Array[Integer](nums.length)
    var i = 0
    while (i < nums.length) {
      boxed(i) = nums(i)
      i += 1
    }
    java.util.Arrays.sort(boxed, (a: Integer, b: Integer) => Integer.compare(math.abs(a), math.abs(b)))
    i = 0
    while (i < nums.length) {
      nums(i) = boxed(i)
      i += 1
    }
    nums
  }
}
'''

FILES["3668_restore_finishing_order"] = r'''// LeetCode 3668 - Restore Finishing Order
// https://leetcode.com/problems/restore-finishing-order/

object Solution {
  def recoverOrder(order: Array[Int], friends: Array[Int]): Array[Int] = {
    val n = order.length
    val d = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      d(order(i)) = i
      i += 1
    }
    val boxed = new Array[Integer](friends.length)
    i = 0
    while (i < friends.length) {
      boxed(i) = friends(i)
      i += 1
    }
    java.util.Arrays.sort(boxed, (a: Integer, b: Integer) => Integer.compare(d(a), d(b)))
    i = 0
    while (i < friends.length) {
      friends(i) = boxed(i)
      i += 1
    }
    friends
  }
}
'''

FILES["3669_balanced_k_factor_decomposition"] = r'''// LeetCode 3669 - Balanced K-Factor Decomposition
// https://leetcode.com/problems/balanced-k-factor-decomposition/

object Solution {
  private val MX = 100001
  private var g: Array[java.util.List[Integer]] = null
  private var inited = false

  private def ensureInit(): Unit = {
    if (inited) return
    g = Array.fill(MX)(new java.util.ArrayList[Integer]())
    var i = 1
    while (i < MX) {
      var j = i
      while (j < MX) {
        g(j).add(i)
        j += i
      }
      i += 1
    }
    inited = true
  }

  def minDifference(n: Int, k: Int): Array[Int] = {
    ensureInit()
    var cur = Int.MaxValue
    var ans = new Array[Int](0)
    val path = new Array[Int](k)

    def dfs(i: Int, x: Int, mi: Int, mx: Int): Unit = {
      if (i == 0) {
        val d = math.max(mx, x) - math.min(mi, x)
        if (d < cur) {
          cur = d
          path(i) = x
          ans = path.clone()
        }
        return
      }
      val it = g(x).iterator()
      while (it.hasNext) {
        val y = it.next().intValue()
        path(i) = y
        dfs(i - 1, x / y, math.min(mi, y), math.max(mx, y))
      }
    }
    dfs(k - 1, n, Int.MaxValue, 0)
    ans
  }
}
'''

FILES["3670_maximum_product_of_two_integers_with_no_common_bits"] = r'''// LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
// https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

object Solution {
  def maxProduct(nums: Array[Int]): Long = {
    var maxV = 0
    for (v <- nums) if (v > maxV) maxV = v
    var bitsN = 0
    var x = maxV
    while (x > 0) {
      bitsN += 1
      x >>= 1
    }
    if (bitsN == 0) bitsN = 1
    val size = 1 << bitsN
    val best = new Array[Int](size)
    for (v <- nums) if (v > best(v)) best(v) = v
    var mask = 0
    while (mask < size) {
      var b = 0
      while (b < bitsN) {
        if ((mask & (1 << b)) != 0) {
          val sub = mask ^ (1 << b)
          if (best(sub) > best(mask)) best(mask) = best(sub)
        }
        b += 1
      }
      mask += 1
    }
    var ans = 0L
    for (v <- nums) {
      val comp = (size - 1) ^ v
      if (best(comp) > 0) {
        val p = v.toLong * best(comp)
        if (p > ans) ans = p
      }
    }
    ans
  }
}
'''

FILES["3671_sum_of_beautiful_subsequences"] = r'''// LeetCode 3671 - Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/

object Solution {
  def totalBeauty(nums: Array[Int]): Int = {
    val MOD = 1000000007
    var mx = 0
    for (v <- nums) if (v > mx) mx = v
    val pos = Array.fill(mx + 1)(new java.util.ArrayList[Integer]())
    var i = 0
    while (i < nums.length) {
      pos(nums(i)).add(i)
      i += 1
    }
    val cnt = new Array[Int](mx + 1)
    var g = 1
    while (g <= mx) {
      val seq = new java.util.ArrayList[Integer]()
      var m = g
      while (m <= mx) {
        seq.addAll(pos(m))
        m += g
      }
      if (!seq.isEmpty) {
        java.util.Collections.sort(seq)
        var ways = 1
        i = 0
        while (i < seq.size()) {
          ways = ((ways * 2L) % MOD).toInt
          i += 1
        }
        cnt(g) = (ways - 1 + MOD) % MOD
      }
      g += 1
    }
    var ans = 0
    g = mx
    while (g >= 1) {
      var m = 2 * g
      while (m <= mx) {
        cnt(g) = (cnt(g) - cnt(m) + MOD) % MOD
        m += g
      }
      ans = ((ans + 1L * cnt(g) * g) % MOD).toInt
      g -= 1
    }
    ans
  }
}
'''

FILES["3672_sum_of_weighted_modes_in_subarrays"] = r'''// LeetCode 3672 - Sum of Weighted Modes in Subarrays
// https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

object Solution {
  def modeWeight(nums: Array[Int], k: Int): Long = {
    val cnt = new java.util.HashMap[Integer, Integer]()
    val pq = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) =>
      if (a(0) != b(0)) Integer.compare(b(0), a(0)) else Integer.compare(a(1), b(1))
    )

    def getMode(): Long = {
      while (true) {
        val top = pq.peek()
        val freq = top(0)
        val `val` = -top(1)
        if (cnt.getOrDefault(`val`, 0) == freq) return 1L * freq * `val`
        pq.poll()
      }
      0L
    }

    var i = 0
    while (i < k) {
      val x = nums(i)
      cnt.merge(x, 1, Integer.sum)
      pq.offer(Array(cnt.get(x), -x))
      i += 1
    }
    var ans = getMode()
    i = k
    while (i < nums.length) {
      val x = nums(i)
      val y = nums(i - k)
      cnt.merge(x, 1, Integer.sum)
      cnt.merge(y, -1, Integer.sum)
      pq.offer(Array(cnt.get(x), -x))
      pq.offer(Array(cnt.get(y), -y))
      ans += getMode()
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
