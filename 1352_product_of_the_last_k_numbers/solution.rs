// LeetCode 1352 - Product of the Last K Numbers
// https://leetcode.com/problems/product-of-the-last-k-numbers/

struct ProductOfNumbers {
    p: Vec<i32>,
}

impl ProductOfNumbers {
    fn new() -> Self {
        Self { p: vec![1] }
    }

    fn add(&mut self, num: i32) {
        if num == 0 {
            self.p = vec![1];
        } else {
            let last = *self.p.last().unwrap();
            self.p.push(last * num);
        }
    }

    fn get_product(&self, k: i32) -> i32 {
        let k = k as usize;
        if k >= self.p.len() {
            0
        } else {
            self.p[self.p.len() - 1] / self.p[self.p.len() - 1 - k]
        }
    }
}
