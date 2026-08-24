// LeetCode 2241 - Design an ATM Machine
// https://leetcode.com/problems/design-an-atm-machine/

pub struct ATM {
    cnt: [i64; 5],
    vals: [i32; 5],
}

impl ATM {
    pub fn new() -> Self {
        Self {
            cnt: [0; 5],
            vals: [20, 50, 100, 200, 500],
        }
    }

    pub fn deposit(&mut self, banknotes_count: Vec<i32>) {
        for i in 0..5 {
            self.cnt[i] += banknotes_count[i] as i64;
        }
    }

    pub fn withdraw(&mut self, amount: i32) -> Vec<i32> {
        let mut take = vec![0; 5];
        let mut remain = amount as i64;
        let tmp = self.cnt;
        for i in (0..5).rev() {
            let mut need = remain / self.vals[i] as i64;
            if need > tmp[i] {
                need = tmp[i];
            }
            take[i] = need as i32;
            remain -= need * self.vals[i] as i64;
        }
        if remain != 0 {
            return vec![-1];
        }
        for i in 0..5 {
            self.cnt[i] -= take[i] as i64;
        }
        take
    }
}
