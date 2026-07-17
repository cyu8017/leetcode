// LeetCode 1788 - Maximize the Beauty of the Garden
// https://leetcode.com/problems/maximize-the-beauty-of-the-garden/

class Solution {
    func maximumBeauty(_ flowers: [Int]) -> Int {
        var first = [Int: Int]()
        var prefix = [Int](repeating: 0, count: flowers.count + 1)
        for (i, value) in flowers.enumerated() {
            prefix[i + 1] = prefix[i] + max(value, 0)
        }
        var best = Int.min
        for (i, value) in flowers.enumerated() {
            if let left = first[value] {
                let between = prefix[i] - prefix[left + 1]
                best = max(best, flowers[left] + flowers[i] + between)
            } else {
                first[value] = i
            }
        }
        return best
    }
}
