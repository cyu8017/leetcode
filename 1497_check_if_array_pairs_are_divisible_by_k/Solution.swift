// LeetCode 1497 - Check If Array Pairs Are Divisible by k
// https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution {
    func canArrange(_ arr: [Int], _ k: Int) -> Bool {
        var count = Array(repeating: 0, count: k)
        for x in arr { count[((x % k) + k) % k] += 1 }
        if count[0] % 2 != 0 { return false }
        for r in 1..<k {
            if count[r] != count[k - r] { return false }
        }
        return true
    }
}
