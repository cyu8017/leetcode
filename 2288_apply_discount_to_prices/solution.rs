// LeetCode 2288 - Apply Discount to Prices
// https://leetcode.com/problems/apply-discount-to-prices/

impl Solution {
    pub fn discount_prices(sentence: String, discount: i32) -> String {
        let mut parts: Vec<String> = sentence.split_whitespace().map(|s| s.to_string()).collect();
        for part in parts.iter_mut() {
            if part.len() >= 2 && part.starts_with('$') {
                let rest = &part[1..];
                if !rest.is_empty() && rest.bytes().all(|c| c.is_ascii_digit()) {
                    let val: i64 = rest.parse().unwrap();
                    let price = val as f64 * (100.0 - discount as f64) / 100.0;
                    *part = format!("${price:.2}");
                }
            }
        }
        parts.join(" ")
    }
}
