// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

class Solution {
    func findMissingElements(_ nums: [Int]) -> [Int] {
        var mn = 100, mx = 0
        var s = Set<Int>()
        for x in nums {
            mn = min(mn, x)
            mx = max(mx, x)
            s.insert(x)
        }
        var ans = [Int]()
        if mn + 1 < mx {
            for x in (mn + 1)..<mx {
                if !s.contains(x) { ans.append(x) }
            }
        }
        return ans
    }
}
