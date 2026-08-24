// LeetCode 2166 - Design Bitset
// https://leetcode.com/problems/design-bitset/

pub struct Bitset {
    bits: Vec<u8>,
    ones: i32,
    flipped: bool,
    size: i32,
}

impl Bitset {
    pub fn new(size: i32) -> Self {
        Self {
            bits: vec![0; size as usize],
            ones: 0,
            flipped: false,
            size,
        }
    }

    pub fn fix(&mut self, idx: i32) {
        let target = if self.flipped { 0 } else { 1 };
        let i = idx as usize;
        if self.bits[i] != target {
            self.bits[i] = target;
            self.ones += if self.flipped { -1 } else { 1 };
        }
    }

    pub fn unfix(&mut self, idx: i32) {
        let target = if self.flipped { 1 } else { 0 };
        let i = idx as usize;
        if self.bits[i] != target {
            self.bits[i] = target;
            self.ones += if self.flipped { 1 } else { -1 };
        }
    }

    pub fn flip(&mut self) {
        self.flipped = !self.flipped;
        self.ones = self.size - self.ones;
    }

    pub fn all(&self) -> bool {
        self.ones == self.size
    }

    pub fn one(&self) -> bool {
        self.ones > 0
    }

    pub fn count(&self) -> i32 {
        self.ones
    }

    pub fn to_string(&self) -> String {
        let mut b = vec![b'0'; self.size as usize];
        for i in 0..self.size as usize {
            let mut v = self.bits[i];
            if self.flipped {
                v ^= 1;
            }
            b[i] = b'0' + v;
        }
        String::from_utf8(b).unwrap()
    }
}
