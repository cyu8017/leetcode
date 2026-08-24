// LeetCode 2797 - Partial Function with Placeholders
// https://leetcode.com/problems/partial-function-with-placeholders/

class Solution {
    func partial(_ fn: @escaping ([Int]) -> Int, _ args: [Int]) -> ([Int]) -> Int {
        { rest in
            var full: [Int] = []
            var ri = 0
            for a in args {
                if a == Int.min, ri < rest.count {
                    full.append(rest[ri])
                    ri += 1
                } else {
                    full.append(a)
                }
            }
            while ri < rest.count {
                full.append(rest[ri])
                ri += 1
            }
            return fn(full)
        }
    }
}
