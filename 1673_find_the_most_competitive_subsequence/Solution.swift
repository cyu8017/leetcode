// LeetCode 1673 - Find the Most Competitive Subsequence
// https://leetcode.com/problems/find-the-most-competitive-subsequence/

class Solution {
    func mostCompetitive(_ nums: [Int], _ k: Int) -> [Int] {
        var st = [Int]()
        for i in 0..<nums.count {
            let x = nums[i]
            while !st.isEmpty && st.last! > x && st.count - 1 + nums.count - i >= k {
                st.removeLast()
            }
            if st.count < k { st.append(x) }
        }
        return st
    }
}
