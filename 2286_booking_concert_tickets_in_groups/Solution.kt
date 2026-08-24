// LeetCode 2286 - Booking Concert Tickets in Groups
// https://leetcode.com/problems/booking-concert-tickets-in-groups/

class BookMyShow {
    private var n = 0
    private var m = 0
    private lateinit var sum: LongArray
    private lateinit var mx: LongArray

    private fun pull(idx: Int) {
        sum[idx] = sum[idx * 2] + sum[idx * 2 + 1]
        mx[idx] = maxOf(mx[idx * 2], mx[idx * 2 + 1])
    }

    private fun build(idx: Int, l: Int, r: Int) {
        if (l == r) {
            sum[idx] = m.toLong()
            mx[idx] = m.toLong()
            return
        }
        val mid = (l + r) / 2
        build(idx * 2, l, mid)
        build(idx * 2 + 1, mid + 1, r)
        pull(idx)
    }

    private fun update(idx: Int, l: Int, r: Int, pos: Int, value: Long) {
        if (l == r) {
            sum[idx] = value
            mx[idx] = value
            return
        }
        val mid = (l + r) / 2
        if (pos <= mid) update(idx * 2, l, mid, pos, value)
        else update(idx * 2 + 1, mid + 1, r, pos, value)
        pull(idx)
    }

    private fun querySum(idx: Int, l: Int, r: Int, ql: Int, qr: Int): Long {
        if (qr < l || r < ql) return 0
        if (ql <= l && r <= qr) return sum[idx]
        val mid = (l + r) / 2
        return querySum(idx * 2, l, mid, ql, qr) + querySum(idx * 2 + 1, mid + 1, r, ql, qr)
    }

    private fun findFirst(idx: Int, l: Int, r: Int, maxRow: Int, k: Long): Int {
        if (l > maxRow || mx[idx] < k) return -1
        if (l == r) return l
        val mid = (l + r) / 2
        val left = findFirst(idx * 2, l, mid, maxRow, k)
        if (left != -1) return left
        return findFirst(idx * 2 + 1, mid + 1, r, maxRow, k)
    }

    constructor(n: Int, m: Int) {
        this.n = n
        this.m = m
        sum = LongArray(4 * n)
        mx = LongArray(4 * n)
        build(1, 0, n - 1)
    }

    fun gather(k: Int, maxRow: Int): IntArray {
        val row = findFirst(1, 0, n - 1, maxRow, k.toLong())
        if (row == -1) return IntArray(0)
        val remain = querySum(1, 0, n - 1, row, row)
        val seat = (m - remain).toInt()
        update(1, 0, n - 1, row, remain - k)
        return intArrayOf(row, seat)
    }

    fun scatter(k: Int, maxRow: Int): Boolean {
        if (querySum(1, 0, n - 1, 0, maxRow) < k) return false
        var need = k.toLong()
        var row = 0
        while (row <= maxRow && need > 0) {
            val remain = querySum(1, 0, n - 1, row, row)
            if (remain != 0L) {
                val take = minOf(remain, need)
                update(1, 0, n - 1, row, remain - take)
                need -= take
            }
            row++
        }
        return true
    }
}
