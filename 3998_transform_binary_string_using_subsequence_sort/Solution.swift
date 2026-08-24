// LeetCode 3998 - Transform Binary String Using Subsequence Sort
// https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/


class Solution {
    func transformStr(_ s: String, _ strs: [String]) -> [Bool] {
        let sArr = Array(s)
        let n = sArr.count
        var prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + (sArr[i] == "1" ? 1 : 0) }
        var result = Array(repeating: false, count: strs.count)
        for i in 0..<strs.count {
            let t = Array(strs[i])
            var left = 0, right = 0
            var ok = true
            for j in 0..<n {
                left += (t[j] == "1" ? 1 : 0)
                let add = (t[j] != "0" ? 1 : 0)
                right = right + add
                if right > prefix[j + 1] { right = prefix[j + 1] }
                if left > right {
                    ok = false
                    break
                }
            }
            result[i] = ok && left <= prefix[n] && prefix[n] <= right
        }
        return result
    }
}
