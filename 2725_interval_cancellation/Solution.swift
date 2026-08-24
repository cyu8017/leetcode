// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

class Solution {
    func cancellable(_ fn: () -> Int, _ t: Int, _ times: Int) -> (() -> Void, [Int]) {
        var cancelled = false
        var results: [Int] = []
        var i = 0
        while i < times && !cancelled {
            results.append(fn())
            i += 1
        }
        let cancel: () -> Void = { cancelled = true }
        return (cancel, results)
    }
}
