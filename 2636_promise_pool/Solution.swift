// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

class Solution {
    func promisePool(_ functions: [() -> Int], _ n: Int) -> [Int] {
        var ans = Array(repeating: 0, count: functions.count)
        for i in functions.indices { ans[i] = functions[i]() }
        return ans
    }
}
