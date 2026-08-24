// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

class Solution {
    func countOperationsToEmptyArray(_ nums: [Int]) -> Int {
        let n = nums.count
        var idx = Array(0..<n)
        idx.sort { nums[$0] < nums[$1] }
        var ans = n
        for i in 1..<n where idx[i] < idx[i - 1] {
            ans += n - i
        }
        return ans
    }
}
