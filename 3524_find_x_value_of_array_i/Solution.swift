// LeetCode 3524 - Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/

class Solution {
    func resultArray(_ nums: [Int], _ k: Int) -> [Int] {
        var ans = Array(repeating: 0, count: k)
        var dp = Array(repeating: 0, count: k)
        for num in nums {
            var newDp = Array(repeating: 0, count: k)
            let nm = num % k
            newDp[nm] = 1
            for i in 0..<k { newDp[(i * nm) % k] += dp[i] }
            for i in 0..<k { ans[i] += newDp[i] }
            dp = newDp
        }
        return ans
    }
}
