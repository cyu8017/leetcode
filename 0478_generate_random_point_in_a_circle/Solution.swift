// LeetCode 0478 - Generate Random Point in a Circle
// https://leetcode.com/problems/generate-random-point-in-a-circle/

import Foundation

var uniform: ((Double, Double) -> Double)?

func setUniform(_ fn: @escaping (Double, Double) -> Double) {
    uniform = fn
}

class Solution {
    private let radius: Double
    private let xCenter: Double
    private let yCenter: Double

    init(_ radius: Double, _ xCenter: Double, _ yCenter: Double) {
        self.radius = radius
        self.xCenter = xCenter
        self.yCenter = yCenter
    }

    func randPoint() -> [Double] {
        while true {
            let sample = uniform ?? { a, b in Double.random(in: a...b) }
            let x = sample(-radius, radius)
            let y = sample(-radius, radius)
            if x * x + y * y <= radius * radius {
                return [
                    (xCenter + x * 100000).rounded() / 100000,
                    (yCenter + y * 100000).rounded() / 100000,
                ]
            }
        }
    }
}
