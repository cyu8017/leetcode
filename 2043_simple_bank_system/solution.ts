// LeetCode 2043 - Simple Bank System
// https://leetcode.com/problems/simple-bank-system/

export class Bank {
    constructor(balance: any) {
        this.bal = balance.slice();
    }

    valid(account: any): any {
        return account >= 1 && account <= this.bal.length;
    }

    transfer(account1: any, account2: any, money: any): any {
        if (!this.valid(account1) || !this.valid(account2) || this.bal[account1 - 1] < money) return false;
        this.bal[account1 - 1] -= money;
        this.bal[account2 - 1] += money;
        return true;
    }

    deposit(account: any, money: any): any {
        if (!this.valid(account)) return false;
        this.bal[account - 1] += money;
        return true;
    }

    withdraw(account: any, money: any): any {
        if (!this.valid(account) || this.bal[account - 1] < money) return false;
        this.bal[account - 1] -= money;
        return true;
    }
}
