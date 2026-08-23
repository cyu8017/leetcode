// LeetCode 2043 - Simple Bank System
// https://leetcode.com/problems/simple-bank-system/

class Bank {
    private final long[] bal;

    public Bank(long[] balance) {
        bal = balance.clone();
    }

    private boolean valid(int account) {
        return account >= 1 && account <= bal.length;
    }

    public boolean transfer(int account1, int account2, long money) {
        if (!valid(account1) || !valid(account2) || bal[account1 - 1] < money) return false;
        bal[account1 - 1] -= money;
        bal[account2 - 1] += money;
        return true;
    }

    public boolean deposit(int account, long money) {
        if (!valid(account)) return false;
        bal[account - 1] += money;
        return true;
    }

    public boolean withdraw(int account, long money) {
        if (!valid(account) || bal[account - 1] < money) return false;
        bal[account - 1] -= money;
        return true;
    }
}
