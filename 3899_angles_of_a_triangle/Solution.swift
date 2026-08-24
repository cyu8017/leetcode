// LeetCode 3899 - Angles Of A Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

import Foundation

class Solution {
    func internalAngles(_ sides: [Int]) -> [Double] {
        let s = sides.sorted()
        let a = Double(s[0]), b = Double(s[1]), c = Double(s[2])
        if a + b <= c { return [] }
        let PI = acos(-1.0)
        let A = acos((b * b + c * c - a * a) / (2.0 * b * c)) * 180.0 / PI
        let B = acos((a * a + c * c - b * b) / (2.0 * a * c)) * 180.0 / PI
        let C = 180.0 - A - B
        return [A, B, C]
    }
}
