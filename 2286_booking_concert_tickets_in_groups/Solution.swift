// LeetCode 2286 - Booking Concert Tickets in Groups
// https://leetcode.com/problems/booking-concert-tickets-in-groups/

class BookMyShow {
    private let n: Int
    private let m: Int
    private var sum: [Int]
    private var mx: [Int]

    init(_ n: Int, _ m: Int) {
        self.n = n
        self.m = m
        sum = [Int](repeating: 0, count: 4 * n)
        mx = [Int](repeating: 0, count: 4 * n)
        build(1, 0, n - 1)
    }

    func gather(_ k: Int, _ maxRow: Int) -> [Int] {
        let row = findFirst(1, 0, n - 1, maxRow, k)
        if row == -1 { return [] }
        let remain = querySum(1, 0, n - 1, row, row)
        let seat = m - remain
        update(1, 0, n - 1, row, remain - k)
        return [row, seat]
    }

    func scatter(_ k: Int, _ maxRow: Int) -> Bool {
        if querySum(1, 0, n - 1, 0, maxRow) < k { return false }
        var need = k
        var row = 0
        while row <= maxRow && need > 0 {
            let remain = querySum(1, 0, n - 1, row, row)
            if remain == 0 { row += 1; continue }
            let take = min(remain, need)
            update(1, 0, n - 1, row, remain - take)
            need -= take
            row += 1
        }
        return true
    }

    private func pull(_ idx: Int) {
        sum[idx] = sum[idx * 2] + sum[idx * 2 + 1]
        mx[idx] = max(mx[idx * 2], mx[idx * 2 + 1])
    }

    private func build(_ idx: Int, _ l: Int, _ r: Int) {
        if l == r {
            sum[idx] = m
            mx[idx] = m
            return
        }
        let mid = (l + r) / 2
        build(idx * 2, l, mid)
        build(idx * 2 + 1, mid + 1, r)
        pull(idx)
    }

    private func update(_ idx: Int, _ l: Int, _ r: Int, _ pos: Int, _ val: Int) {
        if l == r {
            sum[idx] = val
            mx[idx] = val
            return
        }
        let mid = (l + r) / 2
        if pos <= mid { update(idx * 2, l, mid, pos, val) }
        else { update(idx * 2 + 1, mid + 1, r, pos, val) }
        pull(idx)
    }

    private func querySum(_ idx: Int, _ l: Int, _ r: Int, _ ql: Int, _ qr: Int) -> Int {
        if qr < l || r < ql { return 0 }
        if ql <= l && r <= qr { return sum[idx] }
        let mid = (l + r) / 2
        return querySum(idx * 2, l, mid, ql, qr) + querySum(idx * 2 + 1, mid + 1, r, ql, qr)
    }

    private func findFirst(_ idx: Int, _ l: Int, _ r: Int, _ maxRow: Int, _ k: Int) -> Int {
        if l > maxRow || mx[idx] < k { return -1 }
        if l == r { return l }
        let mid = (l + r) / 2
        let left = findFirst(idx * 2, l, mid, maxRow, k)
        if left != -1 { return left }
        return findFirst(idx * 2 + 1, mid + 1, r, maxRow, k)
    }
}
