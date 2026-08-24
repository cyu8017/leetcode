// LeetCode 0901 - Online Stock Span
// https://leetcode.com/problems/online-stock-span/

pub struct StockSpanner {
    stack: Vec<(i32, i32)>,
}

impl StockSpanner {
    pub fn new() -> Self {
        Self { stack: Vec::new() }
    }

    pub fn next(&mut self, price: i32) -> i32 {
        let mut span = 1;
        while let Some(&(p, s)) = self.stack.last() {
            if p <= price {
                span += s;
                self.stack.pop();
            } else {
                break;
            }
        }
        self.stack.push((price, span));
        span
    }
}
