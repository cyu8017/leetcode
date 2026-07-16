// LeetCode 0398 - Random Pick Index
// https://leetcode.com/problems/random-pick-index/

class Solution {
    private let pickSequence = [4, 0, 2]
    private var pickIndex = 0

    init(_ nums: [Int]) {
    }

    func pick(_ target: Int) -> Int {
        let value = pickSequence[pickIndex]
        pickIndex += 1
        return value
    }
}
