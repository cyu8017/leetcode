// LeetCode 2361 - Minimum Costs Using the Train Line
// https://leetcode.com/problems/minimum-costs-using-the-train-line/

class Solution {
    func minimumCosts(_ regular: [Int], _ express: [Int], _ expressCost: Int) -> [Int] {
        let n = regular.count
        var ans = [Int](repeating: 0, count: n)
        var reg = 0, exp = expressCost
        for i in 0..<n {
            let nextReg = min(reg + regular[i], exp + express[i])
            let nextExp = min(reg + regular[i] + expressCost, exp + express[i])
            reg = nextReg
            exp = nextExp
            ans[i] = min(reg, exp)
        }
        return ans
    }
}
