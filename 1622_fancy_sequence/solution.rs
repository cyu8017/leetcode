// LeetCode 1622 - Fancy Sequence
// https://leetcode.com/problems/fancy-sequence/

const FANCY_MOD: i64 = 1_000_000_007;

pub struct Fancy {
    vals: Vec<i64>,
    mul: i64,
    add: i64,
}

impl Fancy {
    pub fn new() -> Self {
        Self { vals: Vec::new(), mul: 1, add: 0 }
    }

    pub fn append(&mut self, val: i32) {
        let inv = Self::mod_pow(self.mul, FANCY_MOD - 2);
        let v = ((val as i64 - self.add) % FANCY_MOD + FANCY_MOD) % FANCY_MOD * inv % FANCY_MOD;
        self.vals.push(v);
    }

    pub fn add_all(&mut self, inc: i32) {
        if !self.vals.is_empty() {
            self.add = (self.add + inc as i64) % FANCY_MOD;
        }
    }

    pub fn mult_all(&mut self, m: i32) {
        if self.vals.is_empty() {
            return;
        }
        self.mul = self.mul * m as i64 % FANCY_MOD;
        self.add = self.add * m as i64 % FANCY_MOD;
    }

    pub fn get_index(&self, idx: i32) -> i32 {
        let idx = idx as usize;
        if idx >= self.vals.len() {
            return -1;
        }
        ((self.vals[idx] * self.mul + self.add) % FANCY_MOD) as i32
    }

    fn mod_pow(mut base: i64, mut exp: i64) -> i64 {
        let mut res = 1i64;
        base %= FANCY_MOD;
        while exp > 0 {
            if exp & 1 == 1 {
                res = res * base % FANCY_MOD;
            }
            base = base * base % FANCY_MOD;
            exp >>= 1;
        }
        res
    }
}
