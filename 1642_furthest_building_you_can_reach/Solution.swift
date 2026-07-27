// LeetCode 1642 - Furthest Building You Can Reach
// https://leetcode.com/problems/furthest-building-you-can-reach/

private struct IntMinHeap {
    private var data = [Int]()
    var count: Int { data.count }
    mutating func push(_ value: Int) {
        data.append(value)
        var i = data.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if data[p] <= data[i] { break }
            data.swapAt(p, i)
            i = p
        }
    }
    mutating func pop() -> Int {
        let result = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            var i = 0
            while true {
                var best = i
                let l = 2 * i + 1, r = l + 1
                if l < data.count && data[l] < data[best] { best = l }
                if r < data.count && data[r] < data[best] { best = r }
                if best == i { break }
                data.swapAt(i, best)
                i = best
            }
        }
        return result
    }
}

class Solution {
    func furthestBuilding(_ heights: [Int], _ bricks: Int, _ ladders: Int) -> Int {
        var bricks = bricks
        var climbs = IntMinHeap()
        for i in 0..<(heights.count - 1) {
            let d = heights[i + 1] - heights[i]
            if d <= 0 { continue }
            climbs.push(d)
            if climbs.count > ladders {
                bricks -= climbs.pop()
            }
            if bricks < 0 { return i }
        }
        return heights.count - 1
    }
}
