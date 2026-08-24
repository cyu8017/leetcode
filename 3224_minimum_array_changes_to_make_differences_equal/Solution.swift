// LeetCode 3224 - Minimum Array Changes to Make Differences Equal
// https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

class Solution {
    func minChanges(_ nums: [Int], _ k: Int) -> Int {
        var d = Array(repeating: 0, count: k + 2)
        let n = nums.count
        for i in 0..<(n / 2) {
            var x = nums[i], y = nums[n - 1 - i]
            if x > y { swap(&x, &y) }
            d[0] += 1
            d[y - x] -= 1
            d[y - x + 1] += 1
            let mx = max(y, k - x)
            d[mx + 1] -= 1
            d[mx + 1] += 2
        }
        var ans = n, s = 0
        for x in d {
            s += x
            ans = min(ans, s)
        }
        return ans
    }
}
