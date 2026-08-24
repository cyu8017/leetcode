// LeetCode 2043 - Simple Bank System
// https://leetcode.com/problems/simple-bank-system/

class Bank {
    private lateinit var bal: LongArray

    constructor(balance: LongArray) {
        bal = balance.copyOf()
    }

    private fun valid(account: Int): Boolean {
        return account >= 1 && account <= bal.size
    }

    fun transfer(account1: Int, account2: Int, money: Long): Boolean {
        if (!valid(account1) || !valid(account2) || bal[account1 - 1] < money) return false
        bal[account1 - 1] -= money
        bal[account2 - 1] += money
        return true
    }

    fun deposit(account: Int, money: Long): Boolean {
        if (!valid(account)) return false
        bal[account - 1] += money
        return true
    }

    fun withdraw(account: Int, money: Long): Boolean {
        if (!valid(account) || bal[account - 1] < money) return false
        bal[account - 1] -= money
        return true
    }
}
