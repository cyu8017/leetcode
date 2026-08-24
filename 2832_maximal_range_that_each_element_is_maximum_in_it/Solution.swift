// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

class Solution {
    func maximumLength(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var left = Array(repeating: 0, count: n)
        var right = Array(repeating: 0, count: n)
        var st: [Int] = []
        for i in 0..<n {
            while !st.isEmpty && nums[st.last!] < nums[i] {
                st.removeLast()
            }
            left[i] = st.isEmpty ? -1 : st.last!
            st.append(i)
        }
        st.removeAll()
        for i in stride(from: n - 1, through: 0, by: -1) {
            while !st.isEmpty && nums[st.last!] <= nums[i] {
                st.removeLast()
            }
            right[i] = st.isEmpty ? n : st.last!
            st.append(i)
        }
        var ans = Array(repeating: 0, count: n)
        for i in 0..<n {
            ans[i] = right[i] - left[i] - 1
        }
        return ans
    }
}
