// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

class Solution {
    func invalidTransactions(_ transactions: [String]) -> [String] {
        struct Tx {
            let name: String, time: Int, amount: Int, city: String, raw: String
        }
        let txs: [Tx] = transactions.map { t in
            let p = t.split(separator: ",")
            return Tx(name: String(p[0]), time: Int(p[1])!, amount: Int(p[2])!, city: String(p[3]), raw: t)
        }
        var ans: [String] = []
        for i in 0..<txs.count {
            let a = txs[i]
            var invalid = a.amount > 1000
            if !invalid {
                for j in 0..<txs.count where i != j {
                    let b = txs[j]
                    if a.name == b.name && a.city != b.city && abs(a.time - b.time) <= 60 {
                        invalid = true
                        break
                    }
                }
            }
            if invalid { ans.append(a.raw) }
        }
        return ans
    }
}
