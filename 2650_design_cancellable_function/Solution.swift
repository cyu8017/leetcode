// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

class Solution {
    func cancellable(_ generator: @escaping () -> Int) -> (() -> Void, () -> Int) {
        var cancelled = false
        var done = false
        var result = 0
        let cancel: () -> Void = { cancelled = true }
        let run: () -> Int = {
            if !done {
                result = generator()
                done = true
            }
            return result
        }
        return (cancel, run)
    }
}
