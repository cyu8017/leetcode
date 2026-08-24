// LeetCode 3245 - Alternating Groups III
// https://leetcode.com/problems/alternating-groups-iii/

private class SegTree {
    let n: Int
    var treeIntervalCounts: [Int]
    var treeIntervalLengths: [Int]
    init(_ n: Int) {
        self.n = n
        treeIntervalCounts = Array(repeating: 0, count: 4 * n)
        treeIntervalLengths = Array(repeating: 0, count: 4 * n)
    }
    func add(_ i: Int, _ val: Int) { addRec(0, 0, n - 1, i, val) }
    private func addRec(_ treeIndex: Int, _ lo: Int, _ hi: Int, _ i: Int, _ val: Int) {
        if lo == hi {
            treeIntervalCounts[treeIndex] += val
            treeIntervalLengths[treeIndex] = treeIntervalCounts[treeIndex] * i
            return
        }
        let mid = (lo + hi) / 2
        if i <= mid { addRec(2 * treeIndex + 1, lo, mid, i, val) }
        else { addRec(2 * treeIndex + 2, mid + 1, hi, i, val) }
        treeIntervalCounts[treeIndex] = treeIntervalCounts[2 * treeIndex + 1] + treeIntervalCounts[2 * treeIndex + 2]
        treeIntervalLengths[treeIndex] = treeIntervalLengths[2 * treeIndex + 1] + treeIntervalLengths[2 * treeIndex + 2]
    }
    func queryIntervalCounts(_ i: Int) -> Int { query(treeIntervalCounts, 0, 0, n - 1, i, n - 1) }
    func queryIntervalLengths(_ i: Int) -> Int { query(treeIntervalLengths, 0, 0, n - 1, i, n - 1) }
    private func query(_ tree: [Int], _ treeIndex: Int, _ lo: Int, _ hi: Int, _ i: Int, _ j: Int) -> Int {
        if i <= lo && hi <= j { return tree[treeIndex] }
        if j < lo || hi < i { return 0 }
        let mid = (lo + hi) / 2
        return query(tree, treeIndex * 2 + 1, lo, mid, i, j) + query(tree, treeIndex * 2 + 2, mid + 1, hi, i, j)
    }
}

class Solution {
    func numberOfAlternatingGroups(_ colors: [Int], _ queries: [[Int]]) -> [Int] {
        let n = colors.count
        var arr = colors + Array(colors.prefix(n - 1))
        let tree = SegTree(2 * n - 1)
        var intervals = Set<Int>()
        func pack(_ l: Int, _ r: Int) -> Int { (l << 32) | (r & 0xffffffff) }
        func unpackL(_ v: Int) -> Int { v >> 32 }
        func unpackR(_ v: Int) -> Int { Int(Int32(bitPattern: UInt32(v & 0xffffffff))) }

        func insert(_ l: Int, _ r: Int) {
            intervals.insert(pack(l, r))
            if l < n { tree.add(r - l + 1, 1) }
        }
        func remove(_ l: Int, _ r: Int) {
            intervals.remove(pack(l, r))
            if l < n { tree.add(r - l + 1, -1) }
        }
        func findInterval(_ target: Int) -> (Int, Int) {
            var bestL = -1, bestR = -1
            for k in intervals {
                let kl = unpackL(k), kr = unpackR(k)
                if kl <= target && target <= kr && kl > bestL {
                    bestL = kl; bestR = kr
                }
            }
            return (bestL, bestR)
        }
        func getNum(_ sz: Int) -> Int {
            let numIntervals = tree.queryIntervalCounts(sz)
            let sumIntervals = tree.queryIntervalLengths(sz)
            var numAlternatingGroups = sumIntervals - numIntervals * sz + numIntervals
            let (l, r) = findInterval(n)
            if l < 0 || l >= n || r - l + 1 < sz { return numAlternatingGroups }
            if r >= n {
                let nonDuplicateGroups = n - l
                let numGroups = (r - l + 1) - sz + 1
                let extra = numGroups - nonDuplicateGroups
                if extra > 0 { numAlternatingGroups -= extra }
            }
            return numAlternatingGroups
        }
        func update(_ index: Int, _ color: Int) {
            if arr[index] == color { return }
            arr[index] = color
            let (start, end) = findInterval(index)
            remove(start, end)
            if start < index && index < end {
                insert(start, index - 1)
                insert(index, index)
                insert(index + 1, end)
                return
            }
            if start == index && index < end { insert(start + 1, end) }
            if start < index && index == end { insert(start, end - 1) }
            var ns = index, ne = index
            while true {
                var merged = false
                for k in Array(intervals) {
                    let kl = unpackL(k), kr = unpackR(k)
                    if kr + 1 == ns && arr[kr] != arr[ns] {
                        remove(kl, kr)
                        ns = kl
                        merged = true
                        break
                    }
                }
                if !merged { break }
            }
            while true {
                var merged = false
                for k in Array(intervals) {
                    let kl = unpackL(k), kr = unpackR(k)
                    if kl == ne + 1 && arr[kl] != arr[ne] {
                        remove(kl, kr)
                        ne = kr
                        merged = true
                        break
                    }
                }
                if !merged { break }
            }
            insert(ns, ne)
        }

        var st = 0
        for i in 1..<(2 * n - 1) {
            if arr[i] == arr[i - 1] {
                insert(st, i - 1)
                st = i
            }
        }
        insert(st, 2 * n - 2)
        var ans: [Int] = []
        for query in queries {
            if query[0] == 1 {
                ans.append(getNum(query[1]))
            } else {
                let index = query[1], color = query[2]
                if arr[index] != color {
                    update(index, color)
                    if index < n - 1 { update(index + n, color) }
                }
            }
        }
        return ans
    }
}
