// LeetCode 3711 - Maximum Transactions Without Negative Balance
// https://leetcode.com/problems/maximum-transactions-without-negative-balance/

class Solution {
    func maxTransactions(_ transactions: [Int]) -> Int {
        var tm = [Int: Int]()
        var ans = transactions.count
        var s = 0
        for x in transactions {
            s += x
            tm[x, default: 0] += 1
            while s < 0 {
                let y = tm.keys.min()!
                s -= y
                ans -= 1
                let c = tm[y]!
                if c == 1 { tm[y] = nil } else { tm[y] = c - 1 }
            }
        }
        return ans
    }
}
