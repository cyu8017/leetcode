// LeetCode 2355 - Maximum Number of Books You Can Take
// https://leetcode.com/problems/maximum-number-of-books-you-can-take/

class Solution {
    func maximumBooks(_ books: [Int]) -> Int {
        let n = books.count
        var dp = [Int](repeating: 0, count: n)
        var stack: [Int] = []
        var ans = 0
        func sum(_ l: Int, _ r: Int, _ h: Int) -> Int {
            let width = r - l + 1
            if h >= width { return width * (2 * h - width + 1) / 2 }
            return h * (h + 1) / 2
        }
        for i in 0..<n {
            while let last = stack.last, books[last] >= books[i] - (i - last) {
                stack.removeLast()
            }
            if stack.isEmpty {
                dp[i] = sum(0, i, books[i])
            } else {
                let j = stack.last!
                dp[i] = dp[j] + sum(j + 1, i, books[i])
            }
            ans = max(ans, dp[i])
            stack.append(i)
        }
        return ans
    }
}
