// LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

class Solution {
    func interchangeableRectangles(_ rectangles: [[Int]]) -> Int {
        var freq = [String: Int]()
        var ans = 0
        for rect in rectangles {
            let g = gcd(rect[0], rect[1])
            let key = "\(rect[0] / g)/\(rect[1] / g)"
            ans += freq[key, default: 0]
            freq[key, default: 0] += 1
        }
        return ans
    }

    private func gcd(_ a: Int, _ b: Int) -> Int {
        var a = a, b = b
        while b != 0 {
            let t = a % b
            a = b
            b = t
        }
        return a
    }
}
