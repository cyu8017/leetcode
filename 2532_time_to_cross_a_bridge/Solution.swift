// LeetCode 2532 - Time to Cross a Bridge
// https://leetcode.com/problems/time-to-cross-a-bridge/

class Solution {
    func findCrossingTime(_ n: Int, _ k: Int, _ time: [[Int]]) -> Int {
        struct Worker {
            let idx: Int
            let leftToRight: Int
            let pickOld: Int
            let rightToLeft: Int
            let putNew: Int
            var efficiency: Int { leftToRight + rightToLeft }
        }
        let ws = (0..<k).map { Worker(idx: $0, leftToRight: time[$0][0], pickOld: time[$0][1], rightToLeft: time[$0][2], putNew: time[$0][3]) }
        var left = Heap<Worker> { a, b in
            if a.efficiency != b.efficiency { return a.efficiency > b.efficiency }
            return a.idx > b.idx
        }
        var right = Heap<Worker> { a, b in
            if a.efficiency != b.efficiency { return a.efficiency > b.efficiency }
            return a.idx > b.idx
        }
        for w in ws { left.push(w) }
        var events = Heap<(Int, Int, Int)> { $0.0 < $1.0 }
        var cur = 0, bridgeFree = 0
        var remain = n, done = 0
        while done < n {
            while !events.isEmpty && events.peek()!.0 <= cur {
                let e = events.pop()
                let w = ws[e.2]
                if e.1 == 0 { left.push(w) } else { right.push(w) }
            }
            if cur < bridgeFree {
                cur = bridgeFree
                continue
            }
            if !right.isEmpty {
                let w = right.pop()
                cur += w.rightToLeft
                bridgeFree = cur
                events.push((cur + w.putNew, 0, w.idx))
                done += 1
                continue
            }
            if !left.isEmpty && remain > 0 {
                let w = left.pop()
                cur += w.leftToRight
                bridgeFree = cur
                remain -= 1
                events.push((cur + w.pickOld, 1, w.idx))
                continue
            }
            if events.isEmpty { break }
            cur = events.peek()!.0
        }
        return cur
    }

    private struct Heap<T> {
        var data = [T]()
        let less: (T, T) -> Bool
        init(_ less: @escaping (T, T) -> Bool) { self.less = less }
        var isEmpty: Bool { data.isEmpty }
        var count: Int { data.count }
        func peek() -> T? { data.first }
        mutating func push(_ x: T) {
            data.append(x)
            var i = data.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if !less(data[i], data[p]) { break }
                data.swapAt(i, p); i = p
            }
        }
        mutating func pop() -> T {
            let res = data[0]
            let last = data.removeLast()
            if !data.isEmpty {
                data[0] = last
                var i = 0
                while true {
                    var s = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < data.count && less(data[l], data[s]) { s = l }
                    if r < data.count && less(data[r], data[s]) { s = r }
                    if s == i { break }
                    data.swapAt(i, s); i = s
                }
            }
            return res
        }
    }

}
