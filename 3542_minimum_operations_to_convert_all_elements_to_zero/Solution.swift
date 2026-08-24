// LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var stk = [Int]()
        var ans = 0
        for x in nums {
            while !stk.isEmpty && stk.last! > x {
                ans += 1
                stk.removeLast()
            }
            if x != 0 && (stk.isEmpty || stk.last! != x) { stk.append(x) }
        }
        ans += stk.count
        return ans
    }
}
