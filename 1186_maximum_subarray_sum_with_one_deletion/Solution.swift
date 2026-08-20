// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

class Solution {
    func maximumSum(_ arr: [Int]) -> Int {
        var keep = arr[0], deleted = arr[0], ans = arr[0]
        for i in 1..<arr.count {
            let x = arr[i]
            deleted = max(keep, deleted + x)
            keep = max(keep + x, x)
            ans = max(ans, keep, deleted)
        }
        return ans
    }
}
