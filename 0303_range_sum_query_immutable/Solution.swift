// LeetCode 0303 - Range Sum Query - Immutable
// https://leetcode.com/problems/range-sum-query-immutable/

class NumArray {
    private var prefix: [Int]

    init(_ nums: [Int]) {
        prefix = [0]
        for num in nums {
            prefix.append(prefix.last! + num)
        }
    }

    func sumRange(_ left: Int, _ right: Int) -> Int {
        return prefix[right + 1] - prefix[left]
    }
}
