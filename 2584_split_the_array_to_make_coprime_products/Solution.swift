// LeetCode 2584 - Split the Array to Make Coprime Products
// https://leetcode.com/problems/split-the-array-to-make-coprime-products/

class Solution {
    func findValidSplit(_ nums: [Int]) -> Int {
        var last = [Int: Int]()
        func factorize(_ x: Int, _ idx: Int) {
            var x = x
            var p = 2
            while p * p <= x {
                if x % p == 0 {
                    last[p] = idx
                    while x % p == 0 { x /= p }
                }
                p += 1
            }
            if x > 1 { last[x] = idx }
        }
        for i in 0..<nums.count { factorize(nums[i], i) }
        var far = 0
        for i in 0..<(nums.count - 1) {
            var x = nums[i]
            var p = 2
            while p * p <= x {
                if x % p == 0 {
                    far = max(far, last[p] ?? 0)
                    while x % p == 0 { x /= p }
                }
                p += 1
            }
            if x > 1 { far = max(far, last[x] ?? 0) }
            if far == i { return i }
        }
        return -1
    }
}
