// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

import Foundation

class H2O {
    private let lock = NSCondition()
    private var h = 0
    private var o = 0

    func hydrogen(_ releaseHydrogen: () -> Void) {
        lock.lock()
        while h == 2 { lock.wait() }
        releaseHydrogen()
        h += 1
        if h == 2 && o == 1 {
            h = 0; o = 0
            lock.broadcast()
        }
        lock.unlock()
    }

    func oxygen(_ releaseOxygen: () -> Void) {
        lock.lock()
        while o == 1 { lock.wait() }
        releaseOxygen()
        o += 1
        if h == 2 && o == 1 {
            h = 0; o = 0
            lock.broadcast()
        }
        lock.unlock()
    }
}
