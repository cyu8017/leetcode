// LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
// https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

class Solution {
    func numberOfSubarrays(_ nums: [Int]) -> Int {
        var stk: [(Int, Int)] = []
        var ans = 0
        for x in nums {
            while !stk.isEmpty && stk.last!.0 < x { stk.removeLast() }
            if stk.isEmpty || stk.last!.0 > x {
                stk.append((x, 1))
            } else {
                stk[stk.count - 1].1 += 1
            }
            ans += stk.last!.1
        }
        return ans
    }
}
