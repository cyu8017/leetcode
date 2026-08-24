// LeetCode 2776 - Convert Callback Based Function to Promise Based Function
// https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/

class Solution {
    func promisify(_ fn: @escaping ([Int], (Int) -> Void) -> Void) -> ([Int]) -> Int {
        { args in
            var result = 0
            fn(args) { result = $0 }
            return result
        }
    }
}
