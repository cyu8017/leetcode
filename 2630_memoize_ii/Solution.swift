// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

class Solution {
    func memoizeII(_ fn: @escaping ([Int]) -> Int) -> ([Int]) -> Int {
        var cache: [String: Int] = [:]
        return { args in
            let k = args.map(String.init).joined(separator: "|")
            if let v = cache[k] { return v }
            let v = fn(args)
            cache[k] = v
            return v
        }
    }
}
