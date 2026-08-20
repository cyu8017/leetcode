// LeetCode 1477 - Find Two Non-overlapping Sub-arrays Each With Target Sum
// https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

class Solution {
    func minSumOfLengths(_ arr: [Int], _ target: Int) -> Int {
        let inf = Int.max / 4
        var left = 0, total = 0, best = inf, ans = inf
        var shortest = Array(repeating: inf, count: arr.count)
        for (right, x) in arr.enumerated() {
            total += x
            while total > target {
                total -= arr[left]; left += 1
            }
            if total == target {
                let length = right - left + 1
                if left > 0 { ans = min(ans, length + shortest[left - 1]) }
                best = min(best, length)
            }
            shortest[right] = best
        }
        return ans == inf ? -1 : ans
    }
}
