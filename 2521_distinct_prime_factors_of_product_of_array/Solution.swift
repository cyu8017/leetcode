// LeetCode 2521 - Distinct Prime Factors of Product of Array
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution {
    func distinctPrimeFactors(_ nums: [Int]) -> Int {
        var set = Set<Int>()
        for num in nums {
            var x = num
            var p = 2
            while p * p <= x {
                if x % p == 0 {
                    set.insert(p)
                    while x % p == 0 { x /= p }
                }
                p += 1
            }
            if x > 1 { set.insert(x) }
        }
        return set.count
    }
}
