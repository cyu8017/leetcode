// LeetCode 2034 - Stock Price Fluctuation
// https://leetcode.com/problems/stock-price-fluctuation/

use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};

pub struct StockPrice {
    latest_ts: i32,
    price_at: HashMap<i32, i32>,
    max_heap: BinaryHeap<(i32, i32)>,
    min_heap: BinaryHeap<Reverse<(i32, i32)>>,
}

impl StockPrice {
    pub fn new() -> Self {
        Self {
            latest_ts: 0,
            price_at: HashMap::new(),
            max_heap: BinaryHeap::new(),
            min_heap: BinaryHeap::new(),
        }
    }

    pub fn update(&mut self, timestamp: i32, price: i32) {
        self.price_at.insert(timestamp, price);
        if timestamp >= self.latest_ts {
            self.latest_ts = timestamp;
        }
        self.max_heap.push((price, timestamp));
        self.min_heap.push(Reverse((price, timestamp)));
    }

    pub fn current(&self) -> i32 {
        self.price_at[&self.latest_ts]
    }

    pub fn maximum(&mut self) -> i32 {
        loop {
            let &(price, ts) = self.max_heap.peek().unwrap();
            if self.price_at[&ts] == price {
                return price;
            }
            self.max_heap.pop();
        }
    }

    pub fn minimum(&mut self) -> i32 {
        loop {
            let Reverse((price, ts)) = *self.min_heap.peek().unwrap();
            if self.price_at[&ts] == price {
                return price;
            }
            self.min_heap.pop();
        }
    }
}
