// LeetCode 3037 - Find Pattern in Infinite Stream II
// https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

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
        let lps = getLPS(pattern)
        var i = 0, j = 0, bit = 0
        var readNext = false
        while true {
            if !readNext {
                bit = stream.next()
                readNext = true
            }
            if bit == pattern[j] {
                i += 1
                readNext = false
                j += 1
                if j == pattern.count { return i - j }
            } else if j > 0 {
                j = lps[j - 1]
            } else {
                i += 1
                readNext = false
            }
        }
    }

    private func getLPS(_ pattern: [Int]) -> [Int] {
        let n = pattern.count
        var lps = Array(repeating: 0, count: n)
        var j = 0
        for i in 1..<n {
            while j > 0 && pattern[j] != pattern[i] { j = lps[j - 1] }
            if pattern[i] == pattern[j] {
                j += 1
                lps[i] = j
            }
        }
        return lps
    }
}
