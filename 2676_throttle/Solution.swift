// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

import Dispatch

class Solution {
    func throttle(_ fn: @escaping () -> Void, _ t: Int) -> () -> Void {
        var last: UInt64 = 0
        var started = false
        return {
            let now = DispatchTime.now().uptimeNanoseconds
            if !started || (now &- last) / 1_000_000 >= UInt64(t) {
                started = true
                last = now
                fn()
            }
        }
    }
}
