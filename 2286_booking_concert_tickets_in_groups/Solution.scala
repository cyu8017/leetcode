// LeetCode 2286 - Booking Concert Tickets in Groups
// https://leetcode.com/problems/booking-concert-tickets-in-groups/

class BookMyShow(_n: Int, _m: Int) {
  private val n = _n
  private val m = _m
  private val sum = new Array[Long](4 * n)
  private val mx = new Array[Long](4 * n)

  private def pull(idx: Int): Unit = {
    sum(idx) = sum(idx * 2) + sum(idx * 2 + 1)
    mx(idx) = math.max(mx(idx * 2), mx(idx * 2 + 1))
  }

  private def build(idx: Int, l: Int, r: Int): Unit = {
    if (l == r) {
      sum(idx) = m
      mx(idx) = m
      return
    }
    val mid = (l + r) / 2
    build(idx * 2, l, mid)
    build(idx * 2 + 1, mid + 1, r)
    pull(idx)
  }

  private def update(idx: Int, l: Int, r: Int, pos: Int, value: Long): Unit = {
    if (l == r) {
      sum(idx) = value
      mx(idx) = value
      return
    }
    val mid = (l + r) / 2
    if (pos <= mid) update(idx * 2, l, mid, pos, value)
    else update(idx * 2 + 1, mid + 1, r, pos, value)
    pull(idx)
  }

  private def querySum(idx: Int, l: Int, r: Int, ql: Int, qr: Int): Long = {
    if (qr < l || r < ql) return 0L
    if (ql <= l && r <= qr) return sum(idx)
    val mid = (l + r) / 2
    querySum(idx * 2, l, mid, ql, qr) + querySum(idx * 2 + 1, mid + 1, r, ql, qr)
  }

  private def findFirst(idx: Int, l: Int, r: Int, maxRow: Int, k: Long): Int = {
    if (l > maxRow || mx(idx) < k) return -1
    if (l == r) return l
    val mid = (l + r) / 2
    val left = findFirst(idx * 2, l, mid, maxRow, k)
    if (left != -1) left else findFirst(idx * 2 + 1, mid + 1, r, maxRow, k)
  }

  build(1, 0, n - 1)

  def gather(k: Int, maxRow: Int): Array[Int] = {
    val row = findFirst(1, 0, n - 1, maxRow, k)
    if (row == -1) return Array.empty[Int]
    val remain = querySum(1, 0, n - 1, row, row)
    val seat = (m - remain).toInt
    update(1, 0, n - 1, row, remain - k)
    Array(row, seat)
  }

  def scatter(k: Int, maxRow: Int): Boolean = {
    if (querySum(1, 0, n - 1, 0, maxRow) < k) return false
    var need = k.toLong
    var row = 0
    while (row <= maxRow && need > 0) {
      val remain = querySum(1, 0, n - 1, row, row)
      if (remain != 0) {
        val take = math.min(remain, need)
        update(1, 0, n - 1, row, remain - take)
        need -= take
      }
      row += 1
    }
    true
  }
}
