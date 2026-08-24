// LeetCode 3218 - Minimum Cost for Cutting Cake I
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

class Solution {
    func minimumCost(_ m: Int, _ n: Int, _ horizontalCut: [Int], _ verticalCut: [Int]) -> Int {
        let hCut = horizontalCut.sorted(by: >)
        let vCut = verticalCut.sorted(by: >)
        var i = 0, j = 0, h = 1, v = 1, ans = 0
        while i < m - 1 || j < n - 1 {
            if j == n - 1 || (i < m - 1 && hCut[i] > vCut[j]) {
                ans += hCut[i] * v
                h += 1; i += 1
            } else {
                ans += vCut[j] * h
                v += 1; j += 1
            }
        }
        return ans
    }
}
