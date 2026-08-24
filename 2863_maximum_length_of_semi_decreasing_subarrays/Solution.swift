// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

class Solution {
    func maxSubarrayLength(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        var st: [Int] = []
        for i in stride(from: n - 1, through: 0, by: -1) {
            if st.isEmpty || nums[i] > nums[st.last!] {
                st.append(i)
            }
        }
        for i in 0..<n {
            while !st.isEmpty && nums[i] > nums[st.last!] {
                let j = st.removeLast()
                ans = max(ans, j - i + 1)
            }
        }
        return ans
    }
}
