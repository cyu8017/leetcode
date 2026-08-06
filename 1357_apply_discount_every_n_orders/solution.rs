// LeetCode 1357 - Apply Discount Every n Orders
// https://leetcode.com/problems/apply-discount-every-n-orders/

use std::collections::HashMap;

struct Cashier {
    n: i32,
    discount: i32,
    price: HashMap<i32, i32>,
    count: i32,
}

impl Cashier {
    fn new(n: i32, discount: i32, products: Vec<i32>, prices: Vec<i32>) -> Self {
        let mut price = HashMap::new();
        for (p, pr) in products.into_iter().zip(prices) {
            price.insert(p, pr);
        }
        Self { n, discount, price, count: 0 }
    }

    fn get_bill(&mut self, product: Vec<i32>, amount: Vec<i32>) -> f64 {
        self.count += 1;
        let total: i32 = product
            .iter()
            .zip(amount.iter())
            .map(|(&p, &a)| self.price[&p] * a)
            .sum();
        if self.count % self.n == 0 {
            total as f64 * (100 - self.discount) as f64 / 100.0
        } else {
            total as f64
        }
    }
}
