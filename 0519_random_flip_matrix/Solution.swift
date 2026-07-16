// LeetCode 0519 - Random Flip Matrix
// https://leetcode.com/problems/random-flip-matrix/

import Foundation

var uniform: ((Double, Double) -> Double)?

func setUniform(_ fn: @escaping (Double, Double) -> Double) {
    uniform = fn
}

class Solution {
    private let cols: Int
    private let total: Int
    private var available: [Int]

    init(_ m: Int, _ n: Int) {
        self.cols = n
        self.total = m * n
        self.available = []
        reset()
    }

    func flip() -> [Int] {
        let sample = uniform ?? { a, b in Double.random(in: a...b) }
        var index = Int(sample(0, Double(available.count - 1)))
        if index >= available.count {
            index = available.count - 1
        }
        let value = available[index]
        available[index] = available[available.count - 1]
        available.removeLast()
        return [value / cols, value % cols]
    }

    func reset() {
        available = Array(0..<total)
    }
}
