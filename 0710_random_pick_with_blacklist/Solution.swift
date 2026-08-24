// LeetCode 0710 - Random Pick with Blacklist
// https://leetcode.com/problems/random-pick-with-blacklist/

class Solution {
    private let size: Int
    private var mapping = [Int: Int]()

    init(_ n: Int, _ blacklist: [Int]) {
        size = n - blacklist.count
        let black = Set(blacklist)
        var white = size
        for b in blacklist where b < size {
            while black.contains(white) { white += 1 }
            mapping[b] = white
            white += 1
        }
    }

    func pick() -> Int {
        let index = Int.random(in: 0..<size)
        return mapping[index] ?? index
    }
}
