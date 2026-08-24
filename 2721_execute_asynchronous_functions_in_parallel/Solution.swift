// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

class Solution {
    func promiseAll(_ functions: [() -> Int]) -> [Int] {
        functions.map { $0() }
    }
}
