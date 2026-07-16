// LeetCode 0384 - Shuffle an Array
// https://leetcode.com/problems/shuffle-an-array/

class Solution {
    private var original: [Int]

    init(_ nums: [Int]) {
        original = nums
        srand48(47)
    }

    func reset() -> [Int] {
        original
    }

    func shuffle() -> [Int] {
        var result = original
        for index in stride(from: result.count - 1, through: 1, by: -1) {
            let swapIndex = Int(drand48() * Double(index + 1))
            result.swapAt(index, swapIndex)
        }
        return result
    }
}
