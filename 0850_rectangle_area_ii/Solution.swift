// LeetCode 0850 - Rectangle Area II
// https://leetcode.com/problems/rectangle-area-ii/

class Solution {
    func rectangleArea(_ rectangles: [[Int]]) -> Int {
        let mod = 1_000_000_007
        var events = [(Int, Int, Int, Int)]()
        for r in rectangles {
            events.append((r[0], 1, r[1], r[3]))
            events.append((r[2], -1, r[1], r[3]))
        }
        events.sort { $0.0 < $1.0 }
        var active = [(Int, Int)]()
        var area = 0
        var prevX = events[0].0
        for e in events {
            let (x, typ, y1, y2) = e
            area = (area + coveredLength(active) * (x - prevX)) % mod
            if typ == 1 {
                active.append((y1, y2))
            } else {
                if let idx = active.firstIndex(where: { $0.0 == y1 && $0.1 == y2 }) {
                    active.remove(at: idx)
                }
            }
            prevX = x
        }
        return area
    }

    private func coveredLength(_ active: [(Int, Int)]) -> Int {
        if active.isEmpty { return 0 }
        let sorted = active.sorted { $0.0 < $1.0 }
        var total = 0, curStart = sorted[0].0, curEnd = sorted[0].1
        for i in 1..<sorted.count {
            let start = sorted[i].0, end = sorted[i].1
            if start > curEnd {
                total += curEnd - curStart
                curStart = start
                curEnd = end
            } else {
                curEnd = max(curEnd, end)
            }
        }
        total += curEnd - curStart
        return total
    }
}
