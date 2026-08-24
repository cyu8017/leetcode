#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")


def w(folder, text):
    path = ROOT / folder / "Solution.scala"
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")
    print("wrote", folder)


w("2254_design_video_sharing_platform", r'''
// LeetCode 2254 - Design Video Sharing Platform
// https://leetcode.com/problems/design-video-sharing-platform/

class VideoSharingPlatform() {
  private var nextID = 0
  private val free = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
  private val videos = scala.collection.mutable.HashMap.empty[Int, String]
  private val views = scala.collection.mutable.HashMap.empty[Int, Int]
  private val likes = scala.collection.mutable.HashMap.empty[Int, Int]
  private val dislikes = scala.collection.mutable.HashMap.empty[Int, Int]

  def upload(video: String): Int = {
    val id = if (free.isEmpty) {
      val v = nextID
      nextID += 1
      v
    } else free.dequeue()
    videos(id) = video
    views(id) = 0
    likes(id) = 0
    dislikes(id) = 0
    id
  }

  def remove(videoId: Int): Unit = {
    if (!videos.contains(videoId)) return
    videos.remove(videoId)
    views.remove(videoId)
    likes.remove(videoId)
    dislikes.remove(videoId)
    free.enqueue(videoId)
  }

  def watch(videoId: Int, startMinute: Int, endMinute0: Int): String = {
    val v = videos.getOrElse(videoId, null)
    if (v == null) return "-1"
    views(videoId) = views(videoId) + 1
    if (startMinute >= v.length) return ""
    val endMinute = math.min(endMinute0, v.length - 1)
    v.substring(startMinute, endMinute + 1)
  }

  def like(videoId: Int): Unit = {
    if (videos.contains(videoId)) likes(videoId) = likes(videoId) + 1
  }

  def dislike(videoId: Int): Unit = {
    if (videos.contains(videoId)) dislikes(videoId) = dislikes(videoId) + 1
  }

  def getLikesAndDislikes(videoId: Int): Array[Int] = {
    if (!videos.contains(videoId)) return Array(-1)
    Array(likes(videoId), dislikes(videoId))
  }

  def getViews(videoId: Int): Int = {
    if (!videos.contains(videoId)) return -1
    views(videoId)
  }
}
''')

w("2255_count_prefixes_of_a_given_string", r'''
// LeetCode 2255 - Count Prefixes of a Given String
// https://leetcode.com/problems/count-prefixes-of-a-given-string/

object Solution {
  def countPrefixes(words: Array[String], s: String): Int = {
    var ans = 0
    for (w <- words) {
      if (w.length <= s.length && s.startsWith(w)) ans += 1
    }
    ans
  }
}
''')

w("2256_minimum_average_difference", r'''
// LeetCode 2256 - Minimum Average Difference
// https://leetcode.com/problems/minimum-average-difference/

object Solution {
  def minimumAverageDifference(nums: Array[Int]): Int = {
    val n = nums.length
    var total = 0L
    for (v <- nums) total += v
    var left = 0L
    var bestDiff = Long.MaxValue
    var bestIdx = 0
    var i = 0
    while (i < n) {
      left += nums(i)
      val leftAvg = left / (i + 1)
      var rightAvg = 0L
      if (i != n - 1) rightAvg = (total - left) / (n - i - 1)
      val diff = math.abs(leftAvg - rightAvg)
      if (diff < bestDiff) {
        bestDiff = diff
        bestIdx = i
      }
      i += 1
    }
    bestIdx
  }
}
''')

w("2257_count_unguarded_cells_in_the_grid", r'''
// LeetCode 2257 - Count Unguarded Cells in the Grid
// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

object Solution {
  def countUnguarded(m: Int, n: Int, guards: Array[Array[Int]], walls: Array[Array[Int]]): Int = {
    val grid = Array.ofDim[Int](m, n)
    for (w <- walls) grid(w(0))(w(1)) = 2
    for (g <- guards) grid(g(0))(g(1)) = 2
    val dirs = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))
    for (g <- guards) {
      for (d <- dirs) {
        var r = g(0) + d(0)
        var c = g(1) + d(1)
        while (r >= 0 && r < m && c >= 0 && c < n && grid(r)(c) != 2) {
          grid(r)(c) = 1
          r += d(0)
          c += d(1)
        }
      }
    }
    var ans = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 0) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
''')

w("2258_escape_the_spreading_fire", r'''
// LeetCode 2258 - Escape the Spreading Fire
// https://leetcode.com/problems/escape-the-spreading-fire/

object Solution {
  def maximumMinutes(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val inf = 1000000000
    val fire = Array.fill(m, n)(inf)
    val q = scala.collection.mutable.Queue.empty[(Int, Int)]
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 1) {
          fire(i)(j) = 0
          q.enqueue((i, j))
        }
        j += 1
      }
      i += 1
    }
    val dirs = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))
    while (q.nonEmpty) {
      val (r, c) = q.dequeue()
      for (d <- dirs) {
        val nr = r + d(0)
        val nc = c + d(1)
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) != 2 && fire(nr)(nc) == inf) {
          fire(nr)(nc) = fire(r)(c) + 1
          q.enqueue((nr, nc))
        }
      }
    }
    def can(wait: Int): Boolean = {
      if (wait >= fire(0)(0)) return false
      val vis = Array.fill(m, n)(false)
      val qq = scala.collection.mutable.Queue.empty[(Int, Int, Int)]
      qq.enqueue((0, 0, wait))
      vis(0)(0) = true
      while (qq.nonEmpty) {
        val (r, c, t) = qq.dequeue()
        for (d <- dirs) {
          val nr = r + d(0)
          val nc = c + d(1)
          val nt = t + 1
          if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) != 2 && !vis(nr)(nc)) {
            if (nr == m - 1 && nc == n - 1) {
              if (nt <= fire(nr)(nc)) return true
            } else if (nt < fire(nr)(nc)) {
              vis(nr)(nc) = true
              qq.enqueue((nr, nc, nt))
            }
          }
        }
      }
      false
    }
    var lo = 0
    var hi = m * n + 10
    var ans = -1
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      if (can(mid)) {
        ans = mid
        lo = mid + 1
      } else hi = mid - 1
    }
    if (ans >= m * n) inf else ans
  }
}
''')

w("2259_remove_digit_from_number_to_maximize_result", r'''
// LeetCode 2259 - Remove Digit From Number to Maximize Result
// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

object Solution {
  def removeDigit(number: String, digit: Char): String = {
    var best = ""
    var i = 0
    while (i < number.length) {
      if (number.charAt(i) == digit) {
        val cand = number.substring(0, i) + number.substring(i + 1)
        if (cand.compareTo(best) > 0) best = cand
      }
      i += 1
    }
    best
  }
}
''')

w("2260_minimum_consecutive_cards_to_pick_up", r'''
// LeetCode 2260 - Minimum Consecutive Cards to Pick Up
// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

object Solution {
  def minimumCardPickup(cards: Array[Int]): Int = {
    val last = scala.collection.mutable.HashMap.empty[Int, Int]
    var ans = -1
    var i = 0
    while (i < cards.length) {
      if (last.contains(cards(i))) {
        val diff = i - last(cards(i)) + 1
        if (ans == -1 || diff < ans) ans = diff
      }
      last(cards(i)) = i
      i += 1
    }
    ans
  }
}
''')

w("2261_k_divisible_elements_subarrays", r'''
// LeetCode 2261 - K Divisible Elements Subarrays
// https://leetcode.com/problems/k-divisible-elements-subarrays/

object Solution {
  def countDistinct(nums: Array[Int], k: Int, p: Int): Int = {
    val n = nums.length
    val seen = scala.collection.mutable.HashSet.empty[String]
    var i = 0
    while (i < n) {
      var div = 0
      val key = new StringBuilder
      var j = i
      while (j < n) {
        if (nums(j) % p == 0) div += 1
        if (div > k) {
          j = n
        } else {
          key.append(nums(j) + 1).append(',')
          seen += key.toString
          j += 1
        }
      }
      i += 1
    }
    seen.size
  }
}
''')

w("2262_total_appeal_of_a_string", r'''
// LeetCode 2262 - Total Appeal of A String
// https://leetcode.com/problems/total-appeal-of-a-string/

object Solution {
  def appealSum(s: String): Long = {
    val last = Array.fill(26)(-1)
    var ans = 0L
    var cur = 0L
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i) - 'a'
      cur += i - last(c)
      last(c) = i
      ans += cur
      i += 1
    }
    ans
  }
}
''')

w("2263_make_array_non_decreasing_or_non_increasing", r'''
// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

object Solution {
  def convertArray(nums: Array[Int]): Int = {
    def cost(arr: Array[Int]): Int = {
      val h = scala.collection.mutable.PriorityQueue.empty[Int]
      var ans = 0
      for (x <- arr) {
        if (h.nonEmpty && h.head > x) {
          val t = h.dequeue()
          ans += t - x
          h.enqueue(x)
        }
        h.enqueue(x)
      }
      ans
    }
    val rev = new Array[Int](nums.length)
    var i = 0
    while (i < nums.length) {
      rev(i) = nums(nums.length - 1 - i)
      i += 1
    }
    math.min(cost(nums), cost(rev))
  }
}
''')

w("2264_largest_3_same_digit_number_in_string", r'''
// LeetCode 2264 - Largest 3-Same-Digit Number in String
// https://leetcode.com/problems/largest-3-same-digit-number-in-string/

object Solution {
  def largestGoodInteger(num: String): String = {
    var best = ""
    var i = 0
    while (i + 2 < num.length) {
      if (num.charAt(i) == num.charAt(i + 1) && num.charAt(i) == num.charAt(i + 2)) {
        val cand = num.substring(i, i + 3)
        if (cand.compareTo(best) > 0) best = cand
      }
      i += 1
    }
    best
  }
}
''')

w("2265_count_nodes_equal_to_average_of_subtree", r'''
// LeetCode 2265 - Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def averageOfSubtree(root: TreeNode): Int = {
    var ans = 0
    def dfs(node: TreeNode): Array[Int] = {
      if (node == null) return Array(0, 0)
      val L = dfs(node.left)
      val R = dfs(node.right)
      val sum = L(0) + R(0) + node.value
      val cnt = L(1) + R(1) + 1
      if (sum / cnt == node.value) ans += 1
      Array(sum, cnt)
    }
    dfs(root)
    ans
  }
}
''')

w("2266_count_number_of_texts", r'''
// LeetCode 2266 - Count Number of Texts
// https://leetcode.com/problems/count-number-of-texts/

object Solution {
  def countTexts(pressedKeys: String): Int = {
    val mod = 1000000007
    val n = pressedKeys.length
    val dp = new Array[Int](n + 1)
    dp(0) = 1
    var i = 1
    while (i <= n) {
      dp(i) = dp(i - 1)
      val maxPress = if (pressedKeys.charAt(i - 1) == '7' || pressedKeys.charAt(i - 1) == '9') 4 else 3
      var j = 2
      var cont = true
      while (cont && j <= maxPress && j <= i) {
        if (pressedKeys.charAt(i - j) != pressedKeys.charAt(i - 1)) cont = false
        else {
          dp(i) = (dp(i) + dp(i - j)) % mod
          j += 1
        }
      }
      i += 1
    }
    dp(n)
  }
}
''')

w("2267_check_if_there_is_a_valid_parentheses_string_path", r'''
// LeetCode 2267 - Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

object Solution {
  def hasValidPath(grid: Array[Array[Char]]): Boolean = {
    val m = grid.length
    val n = grid(0).length
    if ((m + n - 1) % 2 == 1 || grid(0)(0) == ')' || grid(m - 1)(n - 1) == '(') return false
    val vis = scala.collection.mutable.HashSet.empty[Long]
    def dfs(r: Int, c: Int, bal0: Int): Boolean = {
      if (r >= m || c >= n) return false
      val bal = bal0 + (if (grid(r)(c) == '(') 1 else -1)
      if (bal < 0) return false
      if (r == m - 1 && c == n - 1) return bal == 0
      val k = (((r.toLong * n + c) << 10) | bal)
      if (!vis.add(k)) return false
      dfs(r + 1, c, bal) || dfs(r, c + 1, bal)
    }
    dfs(0, 0, 0)
  }
}
''')

w("2268_minimum_number_of_keypresses", r'''
// LeetCode 2268 - Minimum Number of Keypresses
// https://leetcode.com/problems/minimum-number-of-keypresses/

object Solution {
  def minimumKeypresses(s: String): Int = {
    val freq = Array.fill(26)(0)
    var i = 0
    while (i < s.length) {
      freq(s.charAt(i) - 'a') += 1
      i += 1
    }
    val sorted = freq.sorted(Ordering[Int].reverse)
    var ans = 0
    i = 0
    while (i < 26) {
      if (sorted(i) == 0) return ans
      ans += sorted(i) * (i / 9 + 1)
      i += 1
    }
    ans
  }
}
''')

w("2269_find_the_k_beauty_of_a_number", r'''
// LeetCode 2269 - Find the K-Beauty of a Number
// https://leetcode.com/problems/find-the-k-beauty-of-a-number/

object Solution {
  def divisorSubstrings(num: Int, k: Int): Int = {
    val s = num.toString
    var ans = 0
    var i = 0
    while (i + k <= s.length) {
      var sub = 0
      var j = 0
      while (j < k) {
        sub = sub * 10 + (s.charAt(i + j) - '0')
        j += 1
      }
      if (sub != 0 && num % sub == 0) ans += 1
      i += 1
    }
    ans
  }
}
''')

w("2270_number_of_ways_to_split_array", r'''
// LeetCode 2270 - Number of Ways to Split Array
// https://leetcode.com/problems/number-of-ways-to-split-array/

object Solution {
  def waysToSplitArray(nums: Array[Int]): Int = {
    var total = 0L
    for (v <- nums) total += v
    var left = 0L
    var ans = 0
    var i = 0
    while (i + 1 < nums.length) {
      left += nums(i)
      if (left >= total - left) ans += 1
      i += 1
    }
    ans
  }
}
''')

w("2271_maximum_white_tiles_covered_by_a_carpet", r'''
// LeetCode 2271 - Maximum White Tiles Covered by a Carpet
// https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

object Solution {
  def maximumWhiteTiles(tiles: Array[Array[Int]], carpetLen: Int): Int = {
    java.util.Arrays.sort(tiles, (a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    val n = tiles.length
    val pref = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + (tiles(i)(1) - tiles(i)(0) + 1)
      i += 1
    }
    var ans = 0
    var j = 0
    i = 0
    while (i < n) {
      val end = tiles(i)(0) + carpetLen - 1
      while (j < n && tiles(j)(0) <= end) j += 1
      var cover = pref(j) - pref(i)
      if (j > 0 && tiles(j - 1)(1) > end) cover -= tiles(j - 1)(1) - end
      ans = math.max(ans, cover)
      i += 1
    }
    ans
  }
}
''')

w("2272_substring_with_largest_variance", r'''
// LeetCode 2272 - Substring With Largest Variance
// https://leetcode.com/problems/substring-with-largest-variance/

object Solution {
  def largestVariance(s: String): Int = {
    var ans = 0
    var a = 'a'
    while (a <= 'z') {
      var b = 'a'
      while (b <= 'z') {
        if (a != b) {
          var bal = 0
          var hasB = false
          var i = 0
          while (i < s.length) {
            val c = s.charAt(i)
            if (c == a) bal += 1
            else if (c == b) {
              bal -= 1
              hasB = true
            }
            if (hasB) ans = math.max(ans, bal)
            if (bal < 0) {
              bal = 0
              hasB = false
            }
            i += 1
          }
        }
        b = (b + 1).toChar
      }
      a = (a + 1).toChar
    }
    ans
  }
}
''')

w("2273_find_resultant_array_after_removing_anagrams", r'''
// LeetCode 2273 - Find Resultant Array After Removing Anagrams
// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

object Solution {
  def removeAnagrams(words: Array[String]): List[String] = {
    def sig(w: String): Array[Int] = {
      val c = new Array[Int](26)
      var i = 0
      while (i < w.length) {
        c(w.charAt(i) - 'a') += 1
        i += 1
      }
      c
    }
    def eq(a: Array[Int], b: Array[Int]): Boolean = {
      var i = 0
      while (i < 26) {
        if (a(i) != b(i)) return false
        i += 1
      }
      true
    }
    val ans = scala.collection.mutable.ListBuffer(words(0))
    var prev = sig(words(0))
    var i = 1
    while (i < words.length) {
      val cur = sig(words(i))
      if (!eq(cur, prev)) {
        ans += words(i)
        prev = cur
      }
      i += 1
    }
    ans.toList
  }
}
''')

print("batch c done")
