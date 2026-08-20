// LeetCode 1531 - String Compression II
// https://leetcode.com/problems/string-compression-ii/

class Solution {
    func getLengthOfOptimalCompression(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var memo = [Int: Int]()
        func dp(_ index: Int, _ remaining: Int) -> Int {
            if remaining < 0 { return 1_000_000_000 }
            if index == n || n - index <= remaining { return 0 }
            let key = index * 101 + remaining
            if let v = memo[key] { return v }
            var answer = dp(index + 1, remaining - 1)
            var same = 0, removed = 0
            for j in index..<n {
                if chars[j] == chars[index] {
                    same += 1
                    let encoded = 1 + (same >= 2 ? 1 : 0) + (same >= 10 ? 1 : 0) + (same >= 100 ? 1 : 0)
                    answer = min(answer, encoded + dp(j + 1, remaining - removed))
                } else {
                    removed += 1
                    if removed > remaining { break }
                }
            }
            memo[key] = answer
            return answer
        }
        return dp(0, k)
    }
}
