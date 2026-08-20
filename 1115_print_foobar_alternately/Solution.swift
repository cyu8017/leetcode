// LeetCode 1115 - Print FooBar Alternately
// https://leetcode.com/problems/print-foobar-alternately/

import Foundation

class FooBar {
    private let n: Int
    private let fooSem = DispatchSemaphore(value: 1)
    private let barSem = DispatchSemaphore(value: 0)

    init(_ n: Int) { self.n = n }

    func foo(_ printFoo: () -> Void) {
        for _ in 0..<n {
            fooSem.wait()
            printFoo()
            barSem.signal()
        }
    }

    func bar(_ printBar: () -> Void) {
        for _ in 0..<n {
            barSem.wait()
            printBar()
            fooSem.signal()
        }
    }
}
