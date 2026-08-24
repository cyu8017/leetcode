// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

class Solution {
    func minCost(_ arr: [Int], _ brr: [Int], _ k: Int) -> Int {
        var noSwap = 0
        for i in 0..<arr.count { noSwap += abs(arr[i] - brr[i]) }
        let a2 = arr.sorted(), b2 = brr.sorted()
        var withSwap = k
        for i in 0..<a2.count { withSwap += abs(a2[i] - b2[i]) }
        return min(noSwap, withSwap)
    }
}
