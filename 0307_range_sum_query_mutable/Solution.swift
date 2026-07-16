// LeetCode 0307 - Range Sum Query - Mutable
// https://leetcode.com/problems/range-sum-query-mutable/

class NumArray {
    private var nums: [Int]
    private var size: Int
    private var tree: [Int]

    init(_ nums: [Int]) {
        self.nums = nums
        self.size = nums.count
        self.tree = Array(repeating: 0, count: size + 1)
        for index in 0..<size {
            add(index + 1, nums[index])
        }
    }

    func update(_ index: Int, _ val: Int) {
        let delta = val - nums[index]
        nums[index] = val
        add(index + 1, delta)
    }

    func sumRange(_ left: Int, _ right: Int) -> Int {
        return prefix(right + 1) - prefix(left)
    }

    private func add(_ index: Int, _ delta: Int) {
        var current = index
        while current <= size {
            tree[current] += delta
            current += current & -current
        }
    }

    private func prefix(_ index: Int) -> Int {
        var total = 0
        var current = index
        while current > 0 {
            total += tree[current]
            current -= current & -current
        }
        return total
    }
}
