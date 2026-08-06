// LeetCode 1505 - Minimum Possible Integer After at Most K Adjacent Swaps On Digits
// https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

struct Fenwick {
    bit: Vec<i32>,
}

impl Fenwick {
    fn new(n: usize) -> Self {
        Self { bit: vec![0; n + 1] }
    }

    fn add(&mut self, mut i: usize, delta: i32) {
        i += 1;
        while i < self.bit.len() {
            self.bit[i] += delta;
            i += i & i.wrapping_neg();
        }
    }

    fn sum(&self, mut i: usize) -> i32 {
        let mut out = 0;
        while i > 0 {
            out += self.bit[i];
            i -= i & i.wrapping_neg();
        }
        out
    }
}

impl Solution {
    pub fn min_integer(num: String, mut k: i32) -> String {
        let bytes = num.as_bytes();
        let mut positions: Vec<Vec<usize>> = vec![Vec::new(); 10];
        for (i, &ch) in bytes.iter().enumerate() {
            positions[(ch - b'0') as usize].push(i);
        }
        let mut heads = [0usize; 10];
        let mut fw = Fenwick::new(bytes.len());
        let mut out = Vec::with_capacity(bytes.len());
        for _ in 0..bytes.len() {
            for digit in 0..10 {
                if heads[digit] >= positions[digit].len() {
                    continue;
                }
                let index = positions[digit][heads[digit]];
                let cost = index as i32 - fw.sum(index);
                if cost <= k {
                    k -= cost;
                    heads[digit] += 1;
                    fw.add(index, 1);
                    out.push(b'0' + digit as u8);
                    break;
                }
            }
        }
        String::from_utf8(out).unwrap()
    }
}
