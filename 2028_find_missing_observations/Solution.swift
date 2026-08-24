// LeetCode 2028 - Find Missing Observations
// https://leetcode.com/problems/find-missing-observations/

class Solution {
    func missingRolls(_ rolls: [Int], _ mean: Int, _ n: Int) -> [Int] {
        let remain = mean * (rolls.count + n) - rolls.reduce(0, +)
        if remain < n || remain > 6 * n { return [] }
        let baseVal = remain / n, extra = remain % n
        return (0..<n).map { baseVal + ($0 < extra ? 1 : 0) }
    }
}
