// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

import Foundation

class FizzBuzz {
    private let n: Int
    private var current = 1
    private let lock = NSCondition()

    init(_ n: Int) {
        self.n = n
    }

    func fizz(_ printFizz: () -> Void) {
        run({ $0 % 3 == 0 && $0 % 5 != 0 }, printFizz)
    }

    func buzz(_ printBuzz: () -> Void) {
        run({ $0 % 5 == 0 && $0 % 3 != 0 }, printBuzz)
    }

    func fizzbuzz(_ printFizzBuzz: () -> Void) {
        run({ $0 % 15 == 0 }, printFizzBuzz)
    }

    func number(_ printNumber: (Int) -> Void) {
        lock.lock()
        while current <= n {
            if current % 3 != 0 && current % 5 != 0 {
                printNumber(current)
                current += 1
                lock.broadcast()
            } else {
                lock.wait()
            }
        }
        lock.unlock()
    }

    private func run(_ pred: (Int) -> Bool, _ action: () -> Void) {
        lock.lock()
        while current <= n {
            if pred(current) {
                action()
                current += 1
                lock.broadcast()
            } else {
                lock.wait()
            }
        }
        lock.unlock()
    }
}
