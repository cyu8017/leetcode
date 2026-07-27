// LeetCode 1679 - Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution {
    func maxOperations(_ nums: [Int], _ k: Int) -> Int {
        var c = [Int: Int]()
        var ans = 0
        for x in nums {
            let need = k - x
            if let cnt = c[need], cnt > 0 {
                c[need] = cnt - 1
                ans += 1
            } else {
                c[x, default: 0] += 1
            }
        }
        return ans
    }
}
