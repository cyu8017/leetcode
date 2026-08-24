// LeetCode 3513 - Number of Unique XOR Triplets I
// https://leetcode.com/problems/number-of-unique-xor-triplets-i/

class Solution {
    func uniqueXorTriplets(_ nums: [Int]) -> Int {
        let n = nums.count
        if n <= 2 { return n }
        var x = n
        var len = 0
        while x != 0 { len += 1; x >>= 1 }
        return 1 << len
    }
}
