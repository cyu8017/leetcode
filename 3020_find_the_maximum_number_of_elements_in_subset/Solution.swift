// LeetCode 3020 - Find the Maximum Number of Elements in Subset
// https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

class Solution {
    func maximumLength(_ nums: [Int]) -> Int {
        var cnt: [Int: Int] = [:]
        for x in nums { cnt[x, default: 0] += 1 }
        let ones = cnt[1, default: 0]
        var ans = ones - ((ones % 2) ^ 1)
        cnt.removeValue(forKey: 1)
        for start in cnt.keys {
            var x = start
            var t = 0
            while cnt[x, default: 0] > 1 {
                if x > (1 << 30) { break }
                x = x * x
                t += 2
            }
            if cnt[x, default: 0] > 0 { t += 1 }
            else { t -= 1 }
            ans = max(ans, t)
        }
        return ans
    }
}
