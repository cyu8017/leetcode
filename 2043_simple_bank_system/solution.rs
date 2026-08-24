// LeetCode 2043 - Simple Bank System
// https://leetcode.com/problems/simple-bank-system/

pub struct Bank {
    bal: Vec<i64>,
}

impl Bank {
    pub fn new(balance: Vec<i64>) -> Self {
        Self { bal: balance }
    }

    fn valid(&self, account: i32) -> bool {
        account >= 1 && account as usize <= self.bal.len()
    }

    pub fn transfer(&mut self, account1: i32, account2: i32, money: i64) -> bool {
        if !self.valid(account1) || !self.valid(account2) || self.bal[account1 as usize - 1] < money {
            return false;
        }
        self.bal[account1 as usize - 1] -= money;
        self.bal[account2 as usize - 1] += money;
        true
    }

    pub fn deposit(&mut self, account: i32, money: i64) -> bool {
        if !self.valid(account) {
            return false;
        }
        self.bal[account as usize - 1] += money;
        true
    }

    pub fn withdraw(&mut self, account: i32, money: i64) -> bool {
        if !self.valid(account) || self.bal[account as usize - 1] < money {
            return false;
        }
        self.bal[account as usize - 1] -= money;
        true
    }
}
