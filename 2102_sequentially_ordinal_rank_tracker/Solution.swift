// LeetCode 2102 - Sequentially Ordinal Rank Tracker
// https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

class SORTracker {
    private var best = [(String, Int)]()
    private var rest = [(String, Int)]()
    private var k = 0

    init() {}

    private func worse(_ a: (String, Int), _ b: (String, Int)) -> Bool {
        if a.1 != b.1 { return a.1 < b.1 }
        return a.0 > b.0
    }

    private func better(_ a: (String, Int), _ b: (String, Int)) -> Bool {
        if a.1 != b.1 { return a.1 > b.1 }
        return a.0 < b.0
    }

    func add(_ name: String, _ score: Int) {
        best.append((name, score))
        siftUp(&best, best.count - 1, worse)
        if best.count > k { rest.append(pop(&best, worse)); siftUp(&rest, rest.count - 1, better) }
    }

    func get() -> String {
        k += 1
        if !rest.isEmpty { best.append(pop(&rest, better)); siftUp(&best, best.count - 1, worse) }
        return best[0].0
    }

    private func siftUp(_ h: inout [(String, Int)], _ i: Int, _ cmp: ((String, Int), (String, Int)) -> Bool) {
        var i = i
        while i > 0 {
            let p = (i - 1) / 2
            if cmp(h[p], h[i]) { break }
            h.swapAt(p, i)
            i = p
        }
    }

    private func pop(_ h: inout [(String, Int)], _ cmp: ((String, Int), (String, Int)) -> Bool) -> (String, Int) {
        let top = h[0]
        h[0] = h.removeLast()
        if !h.isEmpty {
            var i = 0
            while true {
                var w = i
                let l = 2 * i + 1, r = 2 * i + 2
                if l < h.count && cmp(h[l], h[w]) { w = l }
                if r < h.count && cmp(h[r], h[w]) { w = r }
                if w == i { break }
                h.swapAt(i, w)
                i = w
            }
        }
        return top
    }
}
