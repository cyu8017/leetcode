// LeetCode 0907 - Sum of Subarray Minimums
// https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution {
    func sumSubarrayMins(_ arr: [Int]) -> Int {
        let mod = 1_000_000_007
        let n = arr.count
        var left = Array(repeating: -1, count: n)
        var right = Array(repeating: n, count: n)
        var st = [Int]()
        for i in 0..<n {
            while !st.isEmpty && arr[st.last!] > arr[i] { st.removeLast() }
            left[i] = st.isEmpty ? -1 : st.last!
            st.append(i)
        }
        st.removeAll()
        for i in stride(from: n - 1, through: 0, by: -1) {
            while !st.isEmpty && arr[st.last!] >= arr[i] { st.removeLast() }
            right[i] = st.isEmpty ? n : st.last!
            st.append(i)
        }
        var ans = 0
        for i in 0..<n {
            ans = (ans + arr[i] * (i - left[i]) * (right[i] - i)) % mod
        }
        return ans
    }
}
