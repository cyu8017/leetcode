// LeetCode 0497 - Random Point in Non-overlapping Rectangles
// https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

import Foundation

var uniform: ((Double, Double) -> Double)?

func setUniform(_ fn: @escaping (Double, Double) -> Double) {
    uniform = fn
}

class Solution {
    private let rects: [[Int]]
    private let total: Int

    init(_ rects: [[Int]]) {
        self.rects = rects
        var areaTotal = 0
        for rect in rects {
            let a = rect[0]
            let b = rect[1]
            let x = rect[2]
            let y = rect[3]
            areaTotal += (x - a + 1) * (y - b + 1)
        }
        self.total = areaTotal
    }

    func pick() -> [Int] {
        let sample = uniform ?? { a, b in Double.random(in: a...b) }
        var index = Int(sample(0, Double(total)))
        if index >= total {
            index = total - 1
        }
        for rect in rects {
            let a = rect[0]
            let b = rect[1]
            let x = rect[2]
            let y = rect[3]
            let width = x - a + 1
            let height = y - b + 1
            let size = width * height
            if index < size {
                let offsetX = index % width
                let offsetY = index / width
                return [a + offsetX, b + offsetY]
            }
            index -= size
        }
        let last = rects[rects.count - 1]
        return [last[0], last[1]]
    }
}
