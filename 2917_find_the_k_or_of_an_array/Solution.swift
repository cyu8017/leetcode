// LeetCode 2917 - Find the K-or of an Array
// https://leetcode.com/problems/find-the-k-or-of-an-array/

class Solution {
    func findKOr(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0
        for b in 0..<31 {
            var cnt = 0
            for v in nums where (v & (1 << b)) != 0 { cnt += 1 }
            if cnt >= k { ans |= 1 << b }
        }
        return ans
    }
}
