// LeetCode 1601 - Maximum Number of Achievable Transfer Requests
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

class Solution {
    func maximumRequests(_ n: Int, _ requests: [[Int]]) -> Int {
        let m = requests.count
        var ans = 0
        for mask in 0..<(1 << m) {
            let bits = mask.nonzeroBitCount
            if bits <= ans { continue }
            var bal = [Int](repeating: 0, count: n)
            for i in 0..<m where (mask >> i) & 1 == 1 {
                bal[requests[i][0]] -= 1
                bal[requests[i][1]] += 1
            }
            if bal.allSatisfy({ $0 == 0 }) {
                ans = bits
            }
        }
        return ans
    }
}
