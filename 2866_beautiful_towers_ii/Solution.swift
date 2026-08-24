// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

class Solution {
    func maximumSumOfHeights(_ maxHeights: [Int]) -> Int {
        let n = maxHeights.count
        var left = Array(repeating: 0, count: n)
        var st = [-1]
        var sum = 0
        for i in 0..<n {
            while st.count > 1 && maxHeights[st.last!] >= maxHeights[i] {
                let j = st.removeLast()
                sum -= maxHeights[j] * (j - st.last!)
            }
            sum += maxHeights[i] * (i - st.last!)
            left[i] = sum
            st.append(i)
        }
        var right = Array(repeating: 0, count: n)
        st = [n]
        sum = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            while st.count > 1 && maxHeights[st.last!] >= maxHeights[i] {
                let j = st.removeLast()
                sum -= maxHeights[j] * (st.last! - j)
            }
            sum += maxHeights[i] * (st.last! - i)
            right[i] = sum
            st.append(i)
        }
        var ans = 0
        for i in 0..<n {
            ans = max(ans, left[i] + right[i] - maxHeights[i])
        }
        return ans
    }
}
