// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

class Solution {
    func countOppositeParity(_ nums: [Int]) -> [Int] {
        var cnt = [0, 0]
        for x in nums { cnt[x & 1] += 1 }
        let n = nums.count
        var ans = [Int](repeating: 0, count: n)
        for i in 0..<n {
            let x = nums[i]
            cnt[x & 1] -= 1
            ans[i] = cnt[(x & 1) ^ 1]
        }
        return ans
    }
}
