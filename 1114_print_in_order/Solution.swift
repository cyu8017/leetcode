// LeetCode 1114 - Print in Order
// https://leetcode.com/problems/print-in-order/

import Foundation

class Foo {
    private let second = DispatchSemaphore(value: 0)
    private let third = DispatchSemaphore(value: 0)

    func first(_ printFirst: () -> Void) {
        printFirst()
        second.signal()
    }

    func second(_ printSecond: () -> Void) {
        second.wait()
        printSecond()
        third.signal()
    }

    func third(_ printThird: () -> Void) {
        third.wait()
        printThird()
    }
}
