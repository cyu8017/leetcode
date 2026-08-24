// LeetCode 0900 - RLE Iterator
// https://leetcode.com/problems/rle-iterator/

class RLEIterator {
    private var enc: [Int]
    private var i = 0

    init(_ encoding: [Int]) {
        enc = encoding
    }

    func next(_ n: Int) -> Int {
        var n = n
        while i < enc.count {
            if enc[i] >= n {
                enc[i] -= n
                return enc[i + 1]
            }
            n -= enc[i]
            i += 2
        }
        return -1
    }
}
