// LeetCode 2043 - Simple Bank System
// https://leetcode.com/problems/simple-bank-system/

class Bank {
    /**
     * @param {number[]} balance
     */
    constructor(balance) {
        this.bal = balance.slice();
    }

    valid(account) {
        return account >= 1 && account <= this.bal.length;
    }

    /**
     * @param {number} account1
     * @param {number} account2
     * @param {number} money
     * @return {boolean}
     */
    transfer(account1, account2, money) {
        if (!this.valid(account1) || !this.valid(account2) || this.bal[account1 - 1] < money) return false;
        this.bal[account1 - 1] -= money;
        this.bal[account2 - 1] += money;
        return true;
    }

    /**
     * @param {number} account
     * @param {number} money
     * @return {boolean}
     */
    deposit(account, money) {
        if (!this.valid(account)) return false;
        this.bal[account - 1] += money;
        return true;
    }

    /**
     * @param {number} account
     * @param {number} money
     * @return {boolean}
     */
    withdraw(account, money) {
        if (!this.valid(account) || this.bal[account - 1] < money) return false;
        this.bal[account - 1] -= money;
        return true;
    }
}
