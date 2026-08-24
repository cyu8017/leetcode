// LeetCode 3947 - Maximum Number of Items From Sale II
// https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

impl Solution {
    pub fn max_items(items: Vec<Vec<i32>>, budget: i32) -> i32 {
        let n = items.len();
        let mut frequency = vec![0; n + 1];
        let mut minimum_price = items[0][1];
        for item in &items {
            frequency[item[0] as usize] += 1;
            minimum_price = minimum_price.min(item[1]);
        }
        let mut batches: Vec<(i32, i32)> = Vec::new();
        for item in &items {
            let mut gain = 0;
            let mut multiple = item[0] as usize;
            while multiple <= n {
                gain += frequency[multiple];
                multiple += item[0] as usize;
            }
            gain -= 1;
            if gain > 0 && item[1] < 2 * minimum_price {
                batches.push((item[1], gain));
            }
        }
        batches.sort_by_key(|&(price, _)| price);
        let mut remaining = budget as i64;
        let mut answer = budget as i64 / minimum_price as i64;
        let mut boosted = 0i64;
        for (price, count_limit) in batches {
            let mut count = count_limit as i64;
            let affordable = remaining / price as i64;
            if affordable < count {
                count = affordable;
            }
            remaining -= count * price as i64;
            boosted += count;
            let total = 2 * boosted + remaining / minimum_price as i64;
            if total > answer {
                answer = total;
            }
            if count < count_limit as i64 {
                break;
            }
        }
        answer as i32
    }
}
