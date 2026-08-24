// LeetCode 2197 - Replace Non-Coprime Numbers in Array
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

class Solution {
    func replaceNonCoprimes(_ nums: [Int]) -> [Int] {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 {
                let t = a % b
                a = b
                b = t
            }
            return a
        }
        var stack: [Int] = []
        for x0 in nums {
            var x = x0
            while let last = stack.last {
                let g = gcd(last, x)
                if g == 1 { break }
                x = last / g * x
                stack.removeLast()
            }
            stack.append(x)
        }
        return stack
    }
}
