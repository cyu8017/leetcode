// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

class Solution {
    func kConcatenationMaxSum(_ arr: [Int], _ k: Int) -> Int {
        let MOD = 1_000_000_007
        let one = kadane(arr)
        if k == 1 { return Int(one % Int64(MOD)) }
        let twice = arr + arr
        let two = kadane(twice)
        let total = arr.reduce(0) { $0 + Int64($1) }
        let ans = total > 0 ? max(one, two + total * Int64(k - 2)) : max(one, two)
        return Int(ans % Int64(MOD))
    }

    private func kadane(_ nums: [Int]) -> Int64 {
        var best: Int64 = 0, cur: Int64 = 0
        for x in nums {
            cur = max(0, cur + Int64(x))
            best = max(best, cur)
        }
        return best
    }
}
