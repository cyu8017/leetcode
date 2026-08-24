// LeetCode 3929 - Minimum Partition Score II
// https://leetcode.com/problems/minimum-partition-score-ii/

object Solution {
  private class Line(
      var slope: Long = 0,
      var intercept: Long = 0,
      var count: Int = 0,
      var valid: Boolean = false
  )

  private class State(
      var value: Long = 0,
      var count: Int = 0,
      var valid: Boolean = false
  )

  private def better(a: State, b: State): State = {
    if (!a.valid) return b
    if (!b.valid) return a
    if (a.value != b.value) if (a.value < b.value) a else b
    else if (a.count >= b.count) a else b
  }

  private def evaluate(line: Line, x: Long): State = {
    if (!line.valid) new State()
    else new State(line.slope * x + line.intercept, line.count, true)
  }

  private var prefix: Array[Long] = Array.empty
  private var n: Int = 0

  private def insert(tree: Array[Line], node: Int, left: Int, right: Int, incoming: Line): Unit = {
    var line = incoming
    if (!tree(node).valid) {
      tree(node) = line
      return
    }
    val mid = (left + right) / 2
    val xLeft = prefix(left)
    val xMid = prefix(mid)
    val leftBetter = better(evaluate(line, xLeft), evaluate(tree(node), xLeft))
    val midBetter = better(evaluate(line, xMid), evaluate(tree(node), xMid))
    val lineWinsLeft = leftBetter.value == evaluate(line, xLeft).value && leftBetter.count == line.count
    val lineWinsMid = midBetter.value == evaluate(line, xMid).value && midBetter.count == line.count
    if (lineWinsMid) {
      val tmp = tree(node)
      tree(node) = line
      line = tmp
    }
    if (left == right) return
    if (lineWinsLeft != lineWinsMid) insert(tree, node * 2, left, mid, line)
    else insert(tree, node * 2 + 1, mid + 1, right, line)
  }

  private def query(tree: Array[Line], node: Int, left: Int, right: Int, index: Int): State = {
    val result = evaluate(tree(node), prefix(index))
    if (left == right) return result
    val mid = (left + right) / 2
    if (index <= mid) better(result, query(tree, node * 2, left, mid, index))
    else better(result, query(tree, node * 2 + 1, mid + 1, right, index))
  }

  private def run(penalty: Long): State = {
    val tree = Array.fill(4 * (n + 1))(new Line())
    insert(tree, 1, 0, n, new Line(0, 0, 0, true))
    var current = new State()
    var i = 1
    while (i <= n) {
      val best = query(tree, 1, 0, n, i)
      val x = prefix(i)
      current = new State(best.value + x * x + x + penalty, best.count + 1, true)
      insert(tree, 1, 0, n, new Line(-2 * x, current.value + x * x - x, current.count, true))
      i += 1
    }
    current
  }

  def minPartitionScore(nums: Array[Int], k: Int): Long = {
    n = nums.length
    prefix = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + nums(i)
      i += 1
    }
    val bound = prefix(n) * prefix(n) + prefix(n) + 1
    var low = 0L
    var high = bound
    while (low < high) {
      val mid = low + (high - low + 1) / 2
      if (run(mid).count >= k) low = mid
      else high = mid - 1
    }
    val state = run(low)
    (state.value - low * k) / 2
  }
}
