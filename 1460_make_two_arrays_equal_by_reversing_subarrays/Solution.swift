// LeetCode 1460 - Make Two Arrays Equal by Reversing Subarrays
// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

class Solution {
    func canBeEqual(_ target: [Int], _ arr: [Int]) -> Bool {
        var c = [Int: Int]()
        for x in target { c[x, default: 0] += 1 }
        for x in arr { c[x, default: 0] -= 1 }
        return c.values.allSatisfy { $0 == 0 }
    }
}
