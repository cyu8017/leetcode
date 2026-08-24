// LeetCode 3664 - Two-Letter Card Game
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
