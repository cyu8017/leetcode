// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

class Solution {
    func cancellable(_ fn: @escaping () -> Int, _ t: Int) -> (() -> Void, () -> Int?) {
        var cancelled = false
        let cancel: () -> Void = { cancelled = true }
        let result: () -> Int? = { cancelled ? nil : fn() }
        return (cancel, result)
    }
}
