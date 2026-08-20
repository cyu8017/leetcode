// LeetCode 1570 - Dot Product of Two Sparse Vectors
// https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

class SparseVector {
    private let values: [Int: Int]
    init(_ nums: [Int]) {
        var map = [Int: Int]()
        for (i, x) in nums.enumerated() where x != 0 {
            map[i] = x
        }
        values = map
    }

    func dotProduct(_ vec: SparseVector) -> Int {
        if values.count > vec.values.count {
            return vec.dotProduct(self)
        }
        var ans = 0
        for (i, x) in values {
            if let y = vec.values[i] { ans += x * y }
        }
        return ans
    }
}

class Solution {
    func dotProduct(_ nums1: [Int], _ nums2: [Int]) -> Int {
        SparseVector(nums1).dotProduct(SparseVector(nums2))
    }
}
