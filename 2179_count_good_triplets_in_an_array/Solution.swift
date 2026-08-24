// LeetCode 2179 - Count Good Triplets in an Array
// https://leetcode.com/problems/count-good-triplets-in-an-array/

class Solution {
    func goodTriplets(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        var pos2 = [Int](repeating: 0, count: n)
        for i in 0..<n { pos2[nums2[i]] = i }
        var mapped = [Int](repeating: 0, count: n)
        for i in 0..<n { mapped[i] = pos2[nums1[i]] }
        var bit = [Int](repeating: 0, count: n + 3)
        func add(_ i: Int, _ v: Int) {
            var i = i
            while i < bit.count { bit[i] += v; i += i & -i }
        }
        func sum(_ i: Int) -> Int {
            var i = i, s = 0
            while i > 0 { s += bit[i]; i -= i & -i }
            return s
        }
        var left = [Int](repeating: 0, count: n)
        for i in 0..<n {
            left[i] = sum(mapped[i])
            add(mapped[i] + 1, 1)
        }
        bit = [Int](repeating: 0, count: n + 3)
        var right = [Int](repeating: 0, count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            right[i] = sum(n) - sum(mapped[i] + 1)
            add(mapped[i] + 1, 1)
        }
        var ans = 0
        for i in 0..<n { ans += left[i] * right[i] }
        return ans
    }
}
