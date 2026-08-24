// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

class ArrayWrapper {
    private let nums: [Int]

    init(_ nums: [Int]) {
        self.nums = nums
    }

    func valueOf() -> Int {
        nums.reduce(0, +)
    }

    var description: String {
        "[" + nums.map(String.init).joined(separator: ",") + "]"
    }
}

class Solution {
    func arrayWrapperCreate(_ nums: [Int]) -> ArrayWrapper {
        ArrayWrapper(nums)
    }
}
