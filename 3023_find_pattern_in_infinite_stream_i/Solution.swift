// LeetCode 3023 - Find Pattern in Infinite Stream I
// https://leetcode.com/problems/find-pattern-in-infinite-stream-i/

class InfiniteStream {
    private var bits: [Int]
    private var i = 0
    init(_ bits: [Int]) { self.bits = bits }
    func next() -> Int {
        let v = bits[i]
        i += 1
        return v
    }
}

class Solution {
    func findPattern(_ stream: InfiniteStream, _ pattern: [Int]) -> Int {
        var a = 0, b = 0
        let m = pattern.count
        let half = m >> 1
        let mask1 = (1 << half) - 1
        let mask2 = (1 << (m - half)) - 1
        if half > 0 {
            for i in 0..<half { a |= pattern[i] << (half - 1 - i) }
        }
        for i in half..<m { b |= pattern[i] << (m - 1 - i) }
        var x = 0, y = 0
        var i = 1
        while true {
            var v = stream.next()
            y = y << 1 | v
            v = (y >> (m - half)) & 1
            y &= mask2
            x = x << 1 | v
            x &= mask1
            if i >= m && a == x && b == y { return i - m }
            i += 1
        }
    }
}
