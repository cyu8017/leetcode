// LeetCode 3012 - Minimize Length of Array Using Operations
// https://leetcode.com/problems/minimize-length-of-array-using-operations/

class Solution {
    func minimumArrayLength(_ nums: [Int]) -> Int {
        let mi = nums.min()!
        var cnt = 0
        for x in nums {
            if x % mi != 0 { return 1 }
            if x == mi { cnt += 1 }
        }
        return (cnt + 1) / 2
    }
}
