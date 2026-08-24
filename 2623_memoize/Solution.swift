// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

class Solution {
    func memoize(_ fn: @escaping (Int) -> Int) -> (Int) -> Int {
        var cache: [Int: Int] = [:]
        return { x in
            if let v = cache[x] { return v }
            let v = fn(x)
            cache[x] = v
            return v
        }
    }
}
