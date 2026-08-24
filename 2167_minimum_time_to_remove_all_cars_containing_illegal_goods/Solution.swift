// LeetCode 2167 - Minimum Time to Remove All Cars Containing Illegal Goods
// https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

class Solution {
    func minimumTime(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var left = [Int](repeating: 0, count: n)
        if chars[0] == "1" { left[0] = 1 }
        for i in 1..<n {
            left[i] = left[i - 1]
            if chars[i] == "1" { left[i] = min(i + 1, left[i - 1] + 2) }
        }
        var ans = left[n - 1], right = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            if chars[i] == "1" { right = min(n - i, right + 2) }
            let leftCost = i > 0 ? left[i - 1] : 0
            ans = min(ans, leftCost + right)
        }
        return ans
    }
}
