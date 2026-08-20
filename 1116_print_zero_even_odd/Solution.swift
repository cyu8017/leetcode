// LeetCode 1116 - Print Zero Even Odd
// https://leetcode.com/problems/print-zero-even-odd/

import Foundation

class ZeroEvenOdd {
    private let n: Int
    private let zeroSem = DispatchSemaphore(value: 1)
    private let evenSem = DispatchSemaphore(value: 0)
    private let oddSem = DispatchSemaphore(value: 0)

    init(_ n: Int) { self.n = n }

    func zero(_ printNumber: (Int) -> Void) {
        for i in 1...n {
            zeroSem.wait()
            printNumber(0)
            if i % 2 == 1 { oddSem.signal() } else { evenSem.signal() }
        }
    }

    func even(_ printNumber: (Int) -> Void) {
        for i in stride(from: 2, through: n, by: 2) {
            evenSem.wait()
            printNumber(i)
            zeroSem.signal()
        }
    }

    func odd(_ printNumber: (Int) -> Void) {
        for i in stride(from: 1, through: n, by: 2) {
            oddSem.wait()
            printNumber(i)
            zeroSem.signal()
        }
    }
}
