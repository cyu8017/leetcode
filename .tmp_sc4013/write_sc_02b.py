#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

TREE = """class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}
"""

LISTN = """class ListNode(var x: Int = 0) {
  var next: ListNode = null
}
"""


def hdr(num: str, title: str, slug: str) -> str:
    return f"// LeetCode {num} - {title}\n// https://leetcode.com/problems/{slug}/\n\n"


FILES = {}

FILES["0830_positions_of_large_groups"] = hdr("0830", "Positions of Large Groups", "positions-of-large-groups") + """object Solution {
  def largeGroupPositions(s: String): List[List[Int]] = {
    val ans = scala.collection.mutable.ListBuffer.empty[List[Int]]
    val n = s.length
    var i = 0
    while (i < n) {
      var j = i
      while (j < n && s.charAt(j) == s.charAt(i)) j += 1
      if (j - i >= 3) ans += List(i, j - 1)
      i = j
    }
    ans.toList
  }
}
"""

FILES["0831_masking_personal_information"] = hdr("0831", "Masking Personal Information", "masking-personal-information") + """object Solution {
  def maskPII(s: String): String = {
    var at = s.indexOf('@')
    if (at >= 0) {
      val lower = s.toLowerCase
      at = lower.indexOf('@')
      val name = lower.substring(0, at)
      val domain = lower.substring(at + 1)
      return name.charAt(0) + "*****" + name.charAt(name.length - 1) + "@" + domain
    }
    val digits = new StringBuilder
    s.foreach { ch => if (ch.isDigit) digits.append(ch) }
    val local = digits.substring(digits.length - 4)
    val country = digits.length - 10
    if (country == 0) "***-***-" + local
    else "+" + ("*" * country) + "-***-***-" + local
  }
}
"""

FILES["0832_flipping_an_image"] = hdr("0832", "Flipping an Image", "flipping-an-image") + """object Solution {
  def flipAndInvertImage(image: Array[Array[Int]]): Array[Array[Int]] = {
    image.foreach { row =>
      var i = 0
      var j = row.length - 1
      while (i <= j) {
        val a = 1 - row(i)
        val b = 1 - row(j)
        row(i) = b
        row(j) = a
        i += 1
        j -= 1
      }
    }
    image
  }
}
"""

FILES["0833_find_and_replace_in_string"] = hdr("0833", "Find And Replace in String", "find-and-replace-in-string") + """object Solution {
  def findReplaceString(s: String, indices: Array[Int], sources: Array[String], targets: Array[String]): String = {
    val replaceIdx = scala.collection.mutable.Map.empty[Int, Int]
    val replaceStr = scala.collection.mutable.Map.empty[Int, String]
    indices.indices.foreach { k =>
      val i = indices(k)
      if (s.startsWith(sources(k), i)) {
        replaceIdx(i) = sources(k).length
        replaceStr(i) = targets(k)
      }
    }
    val out = new StringBuilder
    var i = 0
    val n = s.length
    while (i < n) {
      if (replaceStr.contains(i)) {
        out.append(replaceStr(i))
        i += replaceIdx(i)
      } else {
        out.append(s.charAt(i))
        i += 1
      }
    }
    out.toString
  }
}
"""

FILES["0834_sum_of_distances_in_tree"] = hdr("0834", "Sum of Distances in Tree", "sum-of-distances-in-tree") + """object Solution {
  def sumOfDistancesInTree(n: Int, edges: Array[Array[Int]]): Array[Int] = {
    val graph = Array.fill(n)(scala.collection.mutable.ListBuffer.empty[Int])
    edges.foreach { e =>
      graph(e(0)) += e(1)
      graph(e(1)) += e(0)
    }
    val count = Array.fill(n)(1)
    val ans = Array.ofDim[Int](n)
    def post(node: Int, parent: Int): Unit = {
      graph(node).foreach { child =>
        if (child != parent) {
          post(child, node)
          count(node) += count(child)
          ans(node) += ans(child) + count(child)
        }
      }
    }
    def reroot(node: Int, parent: Int): Unit = {
      graph(node).foreach { child =>
        if (child != parent) {
          ans(child) = ans(node) - count(child) + (n - count(child))
          reroot(child, node)
        }
      }
    }
    post(0, -1)
    reroot(0, -1)
    ans
  }
}
"""

FILES["0835_image_overlap"] = hdr("0835", "Image Overlap", "image-overlap") + """object Solution {
  def largestOverlap(img1: Array[Array[Int]], img2: Array[Array[Int]]): Int = {
    val n = img1.length
    val ones1 = scala.collection.mutable.ListBuffer.empty[(Int, Int)]
    val ones2 = scala.collection.mutable.ListBuffer.empty[(Int, Int)]
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (img1(i)(j) == 1) ones1 += ((i, j))
        if (img2(i)(j) == 1) ones2 += ((i, j))
        j += 1
      }
      i += 1
    }
    if (ones1.isEmpty || ones2.isEmpty) return 0
    val shifts = scala.collection.mutable.Map.empty[Long, Int]
    var best = 0
    ones1.foreach { case (a0, a1) =>
      ones2.foreach { case (b0, b1) =>
        val key = ((a0 - b0 + n).toLong << 16) | (a1 - b1 + n)
        val nxt = shifts.getOrElse(key, 0) + 1
        shifts(key) = nxt
        best = math.max(best, nxt)
      }
    }
    best
  }
}
"""

FILES["0836_rectangle_overlap"] = hdr("0836", "Rectangle Overlap", "rectangle-overlap") + """object Solution {
  def isRectangleOverlap(rec1: Array[Int], rec2: Array[Int]): Boolean = {
    !(rec1(2) <= rec2(0) || rec1(0) >= rec2(2) || rec1(3) <= rec2(1) || rec1(1) >= rec2(3))
  }
}
"""

FILES["0837_new_21_game"] = hdr("0837", "New 21 Game", "new-21-game") + """object Solution {
  def new21Game(n: Int, k: Int, maxPts: Int): Double = {
    if (k == 0 || n >= k - 1 + maxPts) return 1.0
    val dp = Array.ofDim[Double](n + 1)
    dp(0) = 1.0
    var window = 1.0
    var ans = 0.0
    var i = 1
    while (i <= n) {
      dp(i) = window / maxPts
      if (i < k) window += dp(i)
      else ans += dp(i)
      if (i - maxPts >= 0 && i - maxPts < k) window -= dp(i - maxPts)
      i += 1
    }
    ans
  }
}
"""

FILES["0838_push_dominoes"] = hdr("0838", "Push Dominoes", "push-dominoes") + """object Solution {
  def pushDominoes(dominoes: String): String = {
    val arr = dominoes.toCharArray
    val n = arr.length
    val force = Array.ofDim[Int](n)
    var f = 0
    var i = 0
    while (i < n) {
      if (arr(i) == 'R') f = n
      else if (arr(i) == 'L') f = 0
      else f = math.max(f - 1, 0)
      force(i) += f
      i += 1
    }
    f = 0
    i = n - 1
    while (i >= 0) {
      if (arr(i) == 'L') f = n
      else if (arr(i) == 'R') f = 0
      else f = math.max(f - 1, 0)
      force(i) -= f
      i -= 1
    }
    i = 0
    while (i < n) {
      if (force(i) > 0) arr(i) = 'R'
      else if (force(i) < 0) arr(i) = 'L'
      else arr(i) = '.'
      i += 1
    }
    new String(arr)
  }
}
"""

FILES["0839_similar_string_groups"] = hdr("0839", "Similar String Groups", "similar-string-groups") + """object Solution {
  def numSimilarGroups(strs: Array[String]): Int = {
    val n = strs.length
    val parent = Array.tabulate(n)(identity)
    def find(x0: Int): Int = {
      var x = x0
      while (parent(x) != x) {
        parent(x) = parent(parent(x))
        x = parent(x)
      }
      x
    }
    def similar(a: String, b: String): Boolean = {
      var d0 = -1
      var d1 = -1
      var diffs = 0
      var i = 0
      while (i < a.length) {
        if (a.charAt(i) != b.charAt(i)) {
          diffs += 1
          if (diffs > 2) return false
          if (d0 < 0) d0 = i else d1 = i
        }
        i += 1
      }
      diffs == 0 || (diffs == 2 && a.charAt(d0) == b.charAt(d1) && a.charAt(d1) == b.charAt(d0))
    }
    var groups = n
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        if (similar(strs(i), strs(j))) {
          val pi = find(i)
          val pj = find(j)
          if (pi != pj) {
            parent(pi) = pj
            groups -= 1
          }
        }
        j += 1
      }
      i += 1
    }
    groups
  }
}
"""

FILES["0840_magic_squares_in_grid"] = hdr("0840", "Magic Squares In Grid", "magic-squares-in-grid") + """object Solution {
  def numMagicSquaresInside(grid: Array[Array[Int]]): Int = {
    val rows = grid.length
    val cols = grid(0).length
    if (rows < 3 || cols < 3) return 0
    def magic(r: Int, c: Int): Boolean = {
      val vals = Array.ofDim[Int](9)
      var k = 0
      var i = 0
      while (i < 3) {
        var j = 0
        while (j < 3) {
          vals(k) = grid(r + i)(c + j)
          k += 1
          j += 1
        }
        i += 1
      }
      scala.util.Sorting.quickSort(vals)
      i = 0
      while (i < 9) {
        if (vals(i) != i + 1) return false
        i += 1
      }
      grid(r)(c) + grid(r)(c + 1) + grid(r)(c + 2) == 15 &&
        grid(r + 1)(c) + grid(r + 1)(c + 1) + grid(r + 1)(c + 2) == 15 &&
        grid(r + 2)(c) + grid(r + 2)(c + 1) + grid(r + 2)(c + 2) == 15 &&
        grid(r)(c) + grid(r + 1)(c) + grid(r + 2)(c) == 15 &&
        grid(r)(c + 1) + grid(r + 1)(c + 1) + grid(r + 2)(c + 1) == 15 &&
        grid(r)(c + 2) + grid(r + 1)(c + 2) + grid(r + 2)(c + 2) == 15 &&
        grid(r)(c) + grid(r + 1)(c + 1) + grid(r + 2)(c + 2) == 15 &&
        grid(r)(c + 2) + grid(r + 1)(c + 1) + grid(r + 2)(c) == 15
    }
    var ans = 0
    var i = 0
    while (i < rows - 2) {
      var j = 0
      while (j < cols - 2) {
        if (magic(i, j)) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
"""

FILES["0841_keys_and_rooms"] = hdr("0841", "Keys and Rooms", "keys-and-rooms") + """object Solution {
  def canVisitAllRooms(rooms: Array[Array[Int]]): Boolean = {
    val seen = scala.collection.mutable.Set(0)
    val stack = scala.collection.mutable.ArrayDeque(0)
    while (stack.nonEmpty) {
      val room = stack.removeLast()
      rooms(room).foreach { key =>
        if (seen.add(key)) stack.append(key)
      }
    }
    seen.size == rooms.length
  }
}
"""

FILES["0842_split_array_into_fibonacci_sequence"] = hdr("0842", "Split Array into Fibonacci Sequence", "split-array-into-fibonacci-sequence") + """object Solution {
  def splitIntoFibonacci(num: String): List[Int] = {
    val path = scala.collection.mutable.ListBuffer.empty[Int]
    def dfs(start: Int): Boolean = {
      val n = num.length
      if (start == n) return path.length >= 3
      var value = 0L
      var end = start
      while (end < n) {
        if (num.charAt(start) == '0' && end > start) return false
        value = value * 10 + (num.charAt(end) - '0')
        if (value > Int.MaxValue) return false
        if (path.length >= 2) {
          val total = path(path.length - 1).toLong + path(path.length - 2)
          if (value < total) { end += 1; }
          else if (value > total) return false
          else {
            path += value.toInt
            if (dfs(end + 1)) return true
            path.remove(path.length - 1)
            end += 1
          }
        } else {
          path += value.toInt
          if (dfs(end + 1)) return true
          path.remove(path.length - 1)
          end += 1
        }
      }
      false
    }
    dfs(0)
    path.toList
  }
}
"""

FILES["0843_guess_the_word"] = hdr("0843", "Guess the Word", "guess-the-word") + """trait Master {
  def guess(word: String): Int
}

object Solution {
  def findSecretWord(words: Array[String], master: Master): Unit = {
    def matchCount(a: String, b: String): Int = {
      var m = 0
      var i = 0
      while (i < a.length) {
        if (a.charAt(i) == b.charAt(i)) m += 1
        i += 1
      }
      m
    }
    var candidates = words.toList
    while (candidates.nonEmpty) {
      var best = candidates.head
      var bestWorst = candidates.length + 1
      candidates.foreach { w =>
        val buckets = Array.ofDim[Int](7)
        candidates.foreach { c => buckets(matchCount(w, c)) += 1 }
        val worst = buckets.max
        if (worst < bestWorst) {
          bestWorst = worst
          best = w
        }
      }
      val score = master.guess(best)
      if (score == 6) return
      candidates = candidates.filter(c => matchCount(c, best) == score)
    }
  }
}
"""

FILES["0844_backspace_string_compare"] = hdr("0844", "Backspace String Compare", "backspace-string-compare") + """object Solution {
  def backspaceCompare(s: String, t: String): Boolean = {
    def build(text: String): String = {
      val stack = new StringBuilder
      text.foreach { ch =>
        if (ch == '#') {
          if (stack.nonEmpty) stack.deleteCharAt(stack.length - 1)
        } else stack.append(ch)
      }
      stack.toString
    }
    build(s) == build(t)
  }
}
"""

FILES["0845_longest_mountain_in_array"] = hdr("0845", "Longest Mountain in Array", "longest-mountain-in-array") + """object Solution {
  def longestMountain(arr: Array[Int]): Int = {
    val n = arr.length
    var ans = 0
    var i = 0
    while (i < n) {
      var j = i
      if (j + 1 < n && arr(j) < arr(j + 1)) {
        while (j + 1 < n && arr(j) < arr(j + 1)) j += 1
        if (j + 1 < n && arr(j) > arr(j + 1)) {
          while (j + 1 < n && arr(j) > arr(j + 1)) j += 1
          ans = math.max(ans, j - i + 1)
          i = j
        } else i += 1
      } else i += 1
    }
    ans
  }
}
"""

FILES["0846_hand_of_straights"] = hdr("0846", "Hand of Straights", "hand-of-straights") + """object Solution {
  def isNStraightHand(hand: Array[Int], groupSize: Int): Boolean = {
    if (hand.length % groupSize != 0) return false
    val count = scala.collection.mutable.TreeMap.empty[Int, Int]
    hand.foreach { x => count(x) = count.getOrElse(x, 0) + 1 }
    while (count.nonEmpty) {
      val start = count.firstKey
      var x = start
      while (x < start + groupSize) {
        count.get(x) match {
          case None => return false
          case Some(1) => count.remove(x)
          case Some(c) => count(x) = c - 1
        }
        x += 1
      }
    }
    true
  }
}
"""

FILES["0847_shortest_path_visiting_all_nodes"] = hdr("0847", "Shortest Path Visiting All Nodes", "shortest-path-visiting-all-nodes") + """object Solution {
  def shortestPathLength(graph: Array[Array[Int]]): Int = {
    val n = graph.length
    val target = (1 << n) - 1
    val queue = scala.collection.mutable.Queue.empty[(Int, Int, Int)]
    val seen = scala.collection.mutable.Set.empty[Long]
    var i = 0
    while (i < n) {
      queue.enqueue((i, 1 << i, 0))
      seen += ((i.toLong << 20) | (1 << i))
      i += 1
    }
    while (queue.nonEmpty) {
      val (node, mask, dist) = queue.dequeue()
      if (mask == target) return dist
      graph(node).foreach { nxt =>
        val nmask = mask | (1 << nxt)
        val state = (nxt.toLong << 20) | nmask
        if (seen.add(state)) queue.enqueue((nxt, nmask, dist + 1))
      }
    }
    -1
  }
}
"""

FILES["0848_shifting_letters"] = hdr("0848", "Shifting Letters", "shifting-letters") + """object Solution {
  def shiftingLetters(s: String, shifts: Array[Int]): String = {
    val arr = s.toCharArray
    var total = 0
    var i = arr.length - 1
    while (i >= 0) {
      total = (total + shifts(i)) % 26
      arr(i) = ((arr(i) - 'a' + total) % 26 + 'a').toChar
      i -= 1
    }
    new String(arr)
  }
}
"""

FILES["0849_maximize_distance_to_closest_person"] = hdr("0849", "Maximize Distance to Closest Person", "maximize-distance-to-closest-person") + """object Solution {
  def maxDistToClosest(seats: Array[Int]): Int = {
    val n = seats.length
    var prev = -1
    var ans = 0
    var i = 0
    while (i < n) {
      if (seats(i) == 1) {
        if (prev == -1) ans = i
        else ans = math.max(ans, (i - prev) / 2)
        prev = i
      }
      i += 1
    }
    math.max(ans, n - 1 - prev)
  }
}
"""

FILES["0850_rectangle_area_ii"] = hdr("0850", "Rectangle Area II", "rectangle-area-ii") + """object Solution {
  def rectangleArea(rectangles: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val events = scala.collection.mutable.ListBuffer.empty[Array[Int]]
    rectangles.foreach { r =>
      events += Array(r(0), 1, r(1), r(3))
      events += Array(r(2), -1, r(1), r(3))
    }
    val ev = events.toArray
    scala.util.Sorting.quickSort(ev)(Ordering.by(_(0)))
    def coveredLength(active: List[Array[Int]]): Int = {
      if (active.isEmpty) return 0
      val sorted = active.sortBy(_(0))
      var total = 0
      var curStart = sorted.head(0)
      var curEnd = sorted.head(1)
      sorted.tail.foreach { iv =>
        val start = iv(0)
        val end = iv(1)
        if (start > curEnd) {
          total += curEnd - curStart
          curStart = start
          curEnd = end
        } else curEnd = math.max(curEnd, end)
      }
      total + curEnd - curStart
    }
    var active = List.empty[Array[Int]]
    var area = 0L
    var prevX = ev(0)(0)
    ev.foreach { e =>
      val x = e(0)
      val typ = e(1)
      val y1 = e(2)
      val y2 = e(3)
      area += coveredLength(active).toLong * (x - prevX)
      if (typ == 1) active = active :+ Array(y1, y2)
      else {
        val idx = active.indexWhere(a => a(0) == y1 && a(1) == y2)
        if (idx >= 0) active = active.patch(idx, Nil, 1)
      }
      prevX = x
    }
    (area % MOD).toInt
  }
}
"""

FILES["0851_loud_and_rich"] = hdr("0851", "Loud and Rich", "loud-and-rich") + """object Solution {
  def loudAndRich(richer: Array[Array[Int]], quiet: Array[Int]): Array[Int] = {
    val n = quiet.length
    val graph = Array.fill(n)(scala.collection.mutable.ListBuffer.empty[Int])
    richer.foreach { e => graph(e(1)) += e(0) }
    val ans = Array.fill(n)(-1)
    def dfs(person: Int): Int = {
      if (ans(person) != -1) return ans(person)
      var best = person
      graph(person).foreach { richerPerson =>
        val cand = dfs(richerPerson)
        if (quiet(cand) < quiet(best)) best = cand
      }
      ans(person) = best
      best
    }
    (0 until n).foreach(dfs)
    ans
  }
}
"""

FILES["0852_peak_index_in_a_mountain_array"] = hdr("0852", "Peak Index in a Mountain Array", "peak-index-in-a-mountain-array") + """object Solution {
  def peakIndexInMountainArray(arr: Array[Int]): Int = {
    var lo = 0
    var hi = arr.length - 1
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (arr(mid) < arr(mid + 1)) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
"""

FILES["0853_car_fleet"] = hdr("0853", "Car Fleet", "car-fleet") + """object Solution {
  def carFleet(target: Int, position: Array[Int], speed: Array[Int]): Int = {
    val n = position.length
    val cars = Array.tabulate(n)(i => (position(i), speed(i)))
    scala.util.Sorting.quickSort(cars)(Ordering.by[(Int, Int), Int](_._1).reverse)
    var fleets = 0
    var maxTime = 0.0
    cars.foreach { case (pos, spd) =>
      val time = (target - pos).toDouble / spd
      if (time > maxTime) {
        fleets += 1
        maxTime = time
      }
    }
    fleets
  }
}
"""

FILES["0854_k_similar_strings"] = hdr("0854", "K-Similar Strings", "k-similar-strings") + """object Solution {
  def kSimilarity(s1: String, s2: String): Int = {
    if (s1 == s2) return 0
    def neighbors(s: String): List[String] = {
      val arr = s.toCharArray
      var i = 0
      while (arr(i) == s2.charAt(i)) i += 1
      val res = scala.collection.mutable.ListBuffer.empty[String]
      var j = i + 1
      while (j < arr.length) {
        if (arr(j) == s2.charAt(i) && arr(j) != s2.charAt(j)) {
          val tmp = arr(i)
          arr(i) = arr(j)
          arr(j) = tmp
          res += new String(arr)
          arr(j) = arr(i)
          arr(i) = tmp
        }
        j += 1
      }
      res.toList
    }
    val queue = scala.collection.mutable.Queue(s1)
    val dist = scala.collection.mutable.Map(s1 -> 0)
    while (queue.nonEmpty) {
      val cur = queue.dequeue()
      val d = dist(cur)
      neighbors(cur).foreach { nxt =>
        if (nxt == s2) return d + 1
        if (!dist.contains(nxt)) {
          dist(nxt) = d + 1
          queue.enqueue(nxt)
        }
      }
    }
    -1
  }
}
"""

FILES["0855_exam_room"] = hdr("0855", "Exam Room", "exam-room") + """class ExamRoom(_n: Int) {
  private val n = _n
  private val seats = scala.collection.mutable.TreeSet.empty[Int]

  def seat(): Int = {
    if (seats.isEmpty) {
      seats += 0
      return 0
    }
    var bestSeat = 0
    var bestDist = seats.head
    var prev = seats.head
    seats.foreach { cur =>
      if (cur != prev) {
        val dist = (cur - prev) / 2
        if (dist > bestDist) {
          bestDist = dist
          bestSeat = prev + dist
        }
        prev = cur
      }
    }
    if (n - 1 - seats.last > bestDist) bestSeat = n - 1
    seats += bestSeat
    bestSeat
  }

  def leave(p: Int): Unit = {
    seats -= p
  }
}
"""

FILES["0856_score_of_parentheses"] = hdr("0856", "Score of Parentheses", "score-of-parentheses") + """object Solution {
  def scoreOfParentheses(s: String): Int = {
    val stack = scala.collection.mutable.ArrayDeque(0)
    s.foreach { ch =>
      if (ch == '(') stack.append(0)
      else {
        val value = stack.removeLast()
        val prev = stack.removeLast()
        stack.append(prev + math.max(2 * value, 1))
      }
    }
    stack.last
  }
}
"""

FILES["0857_minimum_cost_to_hire_k_workers"] = hdr("0857", "Minimum Cost to Hire K Workers", "minimum-cost-to-hire-k-workers") + """object Solution {
  def mincostToHireWorkers(quality: Array[Int], wage: Array[Int], k: Int): Double = {
    val n = quality.length
    val workers = Array.tabulate(n)(i => (wage(i).toDouble / quality(i), quality(i)))
    scala.util.Sorting.quickSort(workers)(Ordering.by(_._1))
    val heap = scala.collection.mutable.PriorityQueue.empty[Int]
    var totalQ = 0L
    var ans = 1e18
    workers.foreach { case (ratio, q) =>
      heap.enqueue(q)
      totalQ += q
      if (heap.size > k) totalQ -= heap.dequeue()
      if (heap.size == k) ans = math.min(ans, totalQ * ratio)
    }
    ans
  }
}
"""

FILES["0858_mirror_reflection"] = hdr("0858", "Mirror Reflection", "mirror-reflection") + """object Solution {
  def mirrorReflection(p: Int, q: Int): Int = {
    def gcd(a0: Int, b0: Int): Int = {
      var a = a0
      var b = b0
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    var pp = p
    var qq = q
    val g = gcd(pp, qq)
    pp /= g
    qq /= g
    if (pp % 2 == 0) 2
    else if (qq % 2 == 0) 0
    else 1
  }
}
"""

FILES["0859_buddy_strings"] = hdr("0859", "Buddy Strings", "buddy-strings") + """object Solution {
  def buddyStrings(s: String, goal: String): Boolean = {
    if (s.length != goal.length) return false
    if (s == goal) {
      val seen = scala.collection.mutable.Set.empty[Char]
      s.foreach { ch => if (!seen.add(ch)) return true }
      return false
    }
    val diffs = scala.collection.mutable.ListBuffer.empty[(Char, Char)]
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) != goal.charAt(i)) diffs += ((s.charAt(i), goal.charAt(i)))
      i += 1
    }
    diffs.length == 2 && diffs(0)._1 == diffs(1)._2 && diffs(0)._2 == diffs(1)._1
  }
}
"""

FILES["0860_lemonade_change"] = hdr("0860", "Lemonade Change", "lemonade-change") + """object Solution {
  def lemonadeChange(bills: Array[Int]): Boolean = {
    var fives = 0
    var tens = 0
    bills.foreach { bill =>
      if (bill == 5) fives += 1
      else if (bill == 10) {
        if (fives == 0) return false
        fives -= 1
        tens += 1
      } else {
        if (tens > 0 && fives > 0) {
          tens -= 1
          fives -= 1
        } else if (fives >= 3) fives -= 3
        else return false
      }
    }
    true
  }
}
"""

FILES["0861_score_after_flipping_matrix"] = hdr("0861", "Score After Flipping Matrix", "score-after-flipping-matrix") + """object Solution {
  def matrixScore(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    grid.foreach { row =>
      if (row(0) == 0) {
        var j = 0
        while (j < n) {
          row(j) ^= 1
          j += 1
        }
      }
    }
    var ans = m * (1 << (n - 1))
    var j = 1
    while (j < n) {
      var ones = 0
      var i = 0
      while (i < m) {
        ones += grid(i)(j)
        i += 1
      }
      ans += math.max(ones, m - ones) * (1 << (n - 1 - j))
      j += 1
    }
    ans
  }
}
"""

FILES["0862_shortest_subarray_with_sum_at_least_k"] = hdr("0862", "Shortest Subarray with Sum at Least K", "shortest-subarray-with-sum-at-least-k") + """object Solution {
  def shortestSubarray(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val prefix = Array.ofDim[Long](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + nums(i)
      i += 1
    }
    val dq = scala.collection.mutable.ArrayDeque.empty[Int]
    var ans = n + 1
    i = 0
    while (i <= n) {
      while (dq.nonEmpty && prefix(i) - prefix(dq.head) >= k) {
        ans = math.min(ans, i - dq.removeHead())
      }
      while (dq.nonEmpty && prefix(i) <= prefix(dq.last)) dq.removeLast()
      dq.append(i)
      i += 1
    }
    if (ans <= n) ans else -1
  }
}
"""

FILES["0863_all_nodes_distance_k_in_binary_tree"] = hdr("0863", "All Nodes Distance K in Binary Tree", "all-nodes-distance-k-in-binary-tree") + TREE + """
object Solution {
  def distanceK(root: TreeNode, target: TreeNode, k: Int): List[Int] = {
    val graph = scala.collection.mutable.Map.empty[TreeNode, scala.collection.mutable.ListBuffer[TreeNode]]
    def build(node: TreeNode, parent: TreeNode): Unit = {
      if (node == null) return
      if (parent != null) {
        graph.getOrElseUpdate(node, scala.collection.mutable.ListBuffer.empty) += parent
        graph.getOrElseUpdate(parent, scala.collection.mutable.ListBuffer.empty) += node
      }
      build(node.left, node)
      build(node.right, node)
    }
    build(root, null)
    val queue = scala.collection.mutable.Queue(target)
    val seen = scala.collection.mutable.Set(target)
    var dist = 0
    while (queue.nonEmpty) {
      if (dist == k) return queue.toList.map(_.value)
      val size = queue.size
      var i = 0
      while (i < size) {
        val node = queue.dequeue()
        graph.getOrElse(node, scala.collection.mutable.ListBuffer.empty[TreeNode]).foreach { nei =>
          if (seen.add(nei)) queue.enqueue(nei)
        }
        i += 1
      }
      dist += 1
    }
    Nil
  }
}
"""

FILES["0864_shortest_path_to_get_all_keys"] = hdr("0864", "Shortest Path to Get All Keys", "shortest-path-to-get-all-keys") + """object Solution {
  def shortestPathAllKeys(grid: Array[String]): Int = {
    val m = grid.length
    val n = grid(0).length
    var allKeys = 0
    var sr = 0
    var sc = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val ch = grid(i).charAt(j)
        if (ch == '@') { sr = i; sc = j }
        else if (ch >= 'a' && ch <= 'f') allKeys |= 1 << (ch - 'a')
        j += 1
      }
      i += 1
    }
    def encode(r: Int, c: Int, mask: Int): Long = (r.toLong << 20) | (c.toLong << 10) | mask
    val queue = scala.collection.mutable.Queue((sr, sc, 0, 0))
    val seen = scala.collection.mutable.Set(encode(sr, sc, 0))
    val dr = Array(1, -1, 0, 0)
    val dc = Array(0, 0, 1, -1)
    while (queue.nonEmpty) {
      val (r, c, mask, dist) = queue.dequeue()
      if (mask == allKeys) return dist
      var k = 0
      while (k < 4) {
        val nr = r + dr(k)
        val nc = c + dc(k)
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr).charAt(nc) != '#') {
          val cell = grid(nr).charAt(nc)
          var nmask = mask
          if (cell >= 'a' && cell <= 'f') nmask |= 1 << (cell - 'a')
          if (!(cell >= 'A' && cell <= 'F' && (mask & (1 << (cell - 'A'))) == 0)) {
            if (seen.add(encode(nr, nc, nmask))) queue.enqueue((nr, nc, nmask, dist + 1))
          }
        }
        k += 1
      }
    }
    -1
  }
}
"""

FILES["0865_smallest_subtree_with_all_the_deepest_nodes"] = hdr("0865", "Smallest Subtree with all the Deepest Nodes", "smallest-subtree-with-all-the-deepest-nodes") + TREE + """
object Solution {
  def subtreeWithAllDeepest(root: TreeNode): TreeNode = {
    def dfs(node: TreeNode): (Int, TreeNode) = {
      if (node == null) return (0, null)
      val (ld, ln) = dfs(node.left)
      val (rd, rn) = dfs(node.right)
      if (ld > rd) (ld + 1, ln)
      else if (rd > ld) (rd + 1, rn)
      else (ld + 1, node)
    }
    dfs(root)._2
  }
}
"""

FILES["0866_prime_palindrome"] = hdr("0866", "Prime Palindrome", "prime-palindrome") + """object Solution {
  def primePalindrome(n: Int): Int = {
    if (n <= 2) return 2
    if (n <= 3) return 3
    if (n <= 5) return 5
    if (n <= 7) return 7
    if (n <= 11) return 11
    def isPrime(x: Int): Boolean = {
      if (x < 2) return false
      if (x % 2 == 0) return x == 2
      var d = 3
      while (d.toLong * d <= x) {
        if (x % d == 0) return false
        d += 2
      }
      true
    }
    var length = 1
    while (length <= 5) {
      val start = math.pow(10, length - 1).toInt
      val end = math.pow(10, length).toInt
      var root = start
      while (root < end) {
        val s = root.toString
        val pal = new StringBuilder(s)
        var i = s.length - 2
        while (i >= 0) {
          pal.append(s.charAt(i))
          i -= 1
        }
        val value = pal.toString.toInt
        if (value >= n && isPrime(value)) return value
        root += 1
      }
      length += 1
    }
    0
  }
}
"""

FILES["0867_transpose_matrix"] = hdr("0867", "Transpose Matrix", "transpose-matrix") + """object Solution {
  def transpose(matrix: Array[Array[Int]]): Array[Array[Int]] = {
    val m = matrix.length
    val n = matrix(0).length
    val ans = Array.ofDim[Int](n, m)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        ans(j)(i) = matrix(i)(j)
        j += 1
      }
      i += 1
    }
    ans
  }
}
"""

FILES["0868_binary_gap"] = hdr("0868", "Binary Gap", "binary-gap") + """object Solution {
  def binaryGap(n: Int): Int = {
    var num = n
    var last = -1
    var ans = 0
    var bit = 0
    while (num != 0) {
      if ((num & 1) == 1) {
        if (last != -1) ans = math.max(ans, bit - last)
        last = bit
      }
      num >>= 1
      bit += 1
    }
    ans
  }
}
"""

FILES["0869_reordered_power_of_2"] = hdr("0869", "Reordered Power of 2", "reordered-power-of-2") + """object Solution {
  def reorderedPowerOf2(n: Int): Boolean = {
    def sig(x: Int): String = x.toString.sorted
    val target = sig(n)
    (0 until 31).exists(i => sig(1 << i) == target)
  }
}
"""

FILES["0870_advantage_shuffle"] = hdr("0870", "Advantage Shuffle", "advantage-shuffle") + """object Solution {
  def advantageCount(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
    val sorted1 = nums1.sorted
    val dq = scala.collection.mutable.ArrayDeque(sorted1: _*)
    val ans = Array.ofDim[Int](nums1.length)
    val indexed = nums2.indices.map(i => (nums2(i), i)).sortBy(-_._1)
    indexed.foreach { case (value, i) =>
      if (dq.last > value) ans(i) = dq.removeLast()
      else ans(i) = dq.removeHead()
    }
    ans
  }
}
"""

FILES["0871_minimum_number_of_refueling_stops"] = hdr("0871", "Minimum Number of Refueling Stops", "minimum-number-of-refueling-stops") + """object Solution {
  def minRefuelStops(target: Int, startFuel: Int, stations: Array[Array[Int]]): Int = {
    val pq = scala.collection.mutable.PriorityQueue.empty[Int]
    val all = stations :+ Array(target, 0)
    var ans = 0
    var prev = 0
    var fuel = startFuel.toLong
    all.foreach { st =>
      val pos = st(0)
      val gas = st(1)
      fuel -= pos - prev
      while (pq.nonEmpty && fuel < 0) {
        fuel += pq.dequeue()
        ans += 1
      }
      if (fuel < 0) return -1
      pq.enqueue(gas)
      prev = pos
    }
    ans
  }
}
"""

FILES["0872_leaf_similar_trees"] = hdr("0872", "Leaf-Similar Trees", "leaf-similar-trees") + TREE + """
object Solution {
  def leafSimilar(root1: TreeNode, root2: TreeNode): Boolean = {
    def leaves(node: TreeNode): List[Int] = {
      val result = scala.collection.mutable.ListBuffer.empty[Int]
      def dfs(cur: TreeNode): Unit = {
        if (cur == null) return
        if (cur.left == null && cur.right == null) {
          result += cur.value
          return
        }
        dfs(cur.left)
        dfs(cur.right)
      }
      dfs(node)
      result.toList
    }
    leaves(root1) == leaves(root2)
  }
}
"""

FILES["0873_length_of_longest_fibonacci_subsequence"] = hdr("0873", "Length of Longest Fibonacci Subsequence", "length-of-longest-fibonacci-subsequence") + """object Solution {
  def lenLongestFibSubseq(arr: Array[Int]): Int = {
    val n = arr.length
    val index = arr.zipWithIndex.toMap
    val dp = Array.fill(n, n)(2)
    var ans = 0
    var j = 0
    while (j < n) {
      var i = 0
      while (i < j) {
        index.get(arr(j) - arr(i)) match {
          case Some(k) if k < i =>
            dp(i)(j) = dp(k)(i) + 1
            ans = math.max(ans, dp(i)(j))
          case _ =>
        }
        i += 1
      }
      j += 1
    }
    if (ans >= 3) ans else 0
  }
}
"""

FILES["0874_walking_robot_simulation"] = hdr("0874", "Walking Robot Simulation", "walking-robot-simulation") + """object Solution {
  def robotSim(commands: Array[Int], obstacles: Array[Array[Int]]): Int = {
    def encode(x: Int, y: Int): Long = ((x + 30000).toLong << 20) | (y + 30000)
    val blocked = obstacles.map(o => encode(o(0), o(1))).toSet
    val dirs = Array(Array(0, 1), Array(1, 0), Array(0, -1), Array(-1, 0))
    var x = 0
    var y = 0
    var d = 0
    var best = 0
    commands.foreach { cmd =>
      if (cmd == -1) d = (d + 1) % 4
      else if (cmd == -2) d = (d + 3) % 4
      else {
        val dx = dirs(d)(0)
        val dy = dirs(d)(1)
        var step = 0
        var cont = true
        while (step < cmd && cont) {
          val nx = x + dx
          val ny = y + dy
          if (blocked.contains(encode(nx, ny))) cont = false
          else {
            x = nx
            y = ny
          }
          step += 1
        }
        best = math.max(best, x * x + y * y)
      }
    }
    best
  }
}
"""

FILES["0875_koko_eating_bananas"] = hdr("0875", "Koko Eating Bananas", "koko-eating-bananas") + """object Solution {
  def minEatingSpeed(piles: Array[Int], h: Int): Int = {
    var lo = 1
    var hi = piles.max
    while (lo < hi) {
      val mid = (lo + hi) / 2
      var hours = 0L
      piles.foreach { p => hours += (p + mid - 1) / mid }
      if (hours <= h) hi = mid
      else lo = mid + 1
    }
    lo
  }
}
"""

FILES["0876_middle_of_the_linked_list"] = hdr("0876", "Middle of the Linked List", "middle-of-the-linked-list") + LISTN + """
object Solution {
  def middleNode(head: ListNode): ListNode = {
    var slow = head
    var fast = head
    while (fast != null && fast.next != null) {
      slow = slow.next
      fast = fast.next.next
    }
    slow
  }
}
"""

FILES["0877_stone_game"] = hdr("0877", "Stone Game", "stone-game") + """object Solution {
  def stoneGame(piles: Array[Int]): Boolean = true
}
"""

FILES["0878_nth_magical_number"] = hdr("0878", "Nth Magical Number", "nth-magical-number") + """object Solution {
  def nthMagicalNumber(n: Int, a: Int, b: Int): Int = {
    val MOD = 1000000007
    def gcd(x0: Long, y0: Long): Long = {
      var x = x0
      var y = y0
      while (y != 0) {
        val t = x % y
        x = y
        y = t
      }
      x
    }
    val lcm = a.toLong / gcd(a.toLong, b.toLong) * b
    var lo = 1L
    var hi = n.toLong * math.min(a, b)
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (mid / a + mid / b - mid / lcm >= n) hi = mid
      else lo = mid + 1
    }
    (lo % MOD).toInt
  }
}
"""

FILES["0879_profitable_schemes"] = hdr("0879", "Profitable Schemes", "profitable-schemes") + """object Solution {
  def profitableSchemes(n: Int, minProfit: Int, group: Array[Int], profit: Array[Int]): Int = {
    val MOD = 1000000007
    val dp = Array.ofDim[Int](n + 1, minProfit + 1)
    dp(0)(0) = 1
    var i = 0
    while (i < group.length) {
      val members = group(i)
      val p = profit(i)
      var people = n
      while (people >= members) {
        var prof = minProfit
        while (prof >= 0) {
          val np = math.min(minProfit, prof + p)
          dp(people)(np) = (dp(people)(np) + dp(people - members)(prof)) % MOD
          prof -= 1
        }
        people -= 1
      }
      i += 1
    }
    var ans = 0
    var people = 0
    while (people <= n) {
      ans = (ans + dp(people)(minProfit)) % MOD
      people += 1
    }
    ans
  }
}
"""

written = 0
for folder, src in FILES.items():
    path = ROOT / folder / "Solution.scala"
    path.write_text(src, encoding="utf-8", newline="\n")
    written += 1
print(f"wrote {written}")
