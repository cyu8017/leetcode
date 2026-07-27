// LeetCode 1687 - Delivering Boxes From Storage to Ports
// https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

class Solution {
    func boxDelivering(_ boxes: [[Int]], _ portsCount: Int, _ maxBoxes: Int, _ maxWeight: Int) -> Int {
        let n = boxes.count
        var w = Array(repeating: 0, count: n + 1)
        var changes = Array(repeating: 0, count: n + 1)
        for i in 1...n {
            w[i] = w[i - 1] + boxes[i - 1][1]
            changes[i] = changes[i - 1] + (i > 1 && boxes[i - 1][0] != boxes[i - 2][0] ? 1 : 0)
        }
        var dp = Array(repeating: 0, count: n + 1)
        var q = [0]
        for i in 1...n {
            while !q.isEmpty && (i - q[0] > maxBoxes || w[i] - w[q[0]] > maxWeight) {
                q.removeFirst()
            }
            let j = q[0]
            dp[i] = dp[j] + changes[i] - changes[j + 1] + 2
            if i < n {
                let val = dp[i] - changes[i + 1]
                while !q.isEmpty && dp[q.last!] - changes[q.last! + 1] >= val {
                    q.removeLast()
                }
                q.append(i)
            }
        }
        return dp[n]
    }
}
