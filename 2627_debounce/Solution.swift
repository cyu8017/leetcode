// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

import Dispatch

class Solution {
    func debounce(_ fn: @escaping () -> Void, _ t: Int) -> () -> Void {
        var work: DispatchWorkItem?
        return {
            work?.cancel()
            let item = DispatchWorkItem { fn() }
            work = item
            DispatchQueue.main.asyncAfter(deadline: .now() + .milliseconds(t), execute: item)
        }
    }
}
