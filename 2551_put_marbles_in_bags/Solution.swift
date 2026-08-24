// LeetCode 2551 - Put Marbles in Bags
// https://leetcode.com/problems/put-marbles-in-bags/

class Solution {
    func putMarbles(_ weights: [Int], _ k: Int) -> Int {
        let n = weights.count
        if k == 1 || k == n { return 0 }
        var pair = [Int]()
        for i in 0..<(n - 1) { pair.append(weights[i] + weights[i + 1]) }
        pair.sort()
        var mn = 0, mx = 0
        for i in 0..<(k - 1) {
            mn += pair[i]
            mx += pair[n - 2 - i]
        }
        return mx - mn
    }
}
