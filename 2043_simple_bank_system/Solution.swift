// LeetCode 2043 - Simple Bank System
// https://leetcode.com/problems/simple-bank-system/

class Bank {
    private var bal: [Int]

    init(_ balance: [Int]) {
        bal = balance
    }

    private func valid(_ account: Int) -> Bool {
        return account >= 1 && account <= bal.count
    }

    func transfer(_ account1: Int, _ account2: Int, _ money: Int) -> Bool {
        if !valid(account1) || !valid(account2) || bal[account1 - 1] < money { return false }
        bal[account1 - 1] -= money
        bal[account2 - 1] += money
        return true
    }

    func deposit(_ account: Int, _ money: Int) -> Bool {
        if !valid(account) { return false }
        bal[account - 1] += money
        return true
    }

    func withdraw(_ account: Int, _ money: Int) -> Bool {
        if !valid(account) || bal[account - 1] < money { return false }
        bal[account - 1] -= money
        return true
    }
}
