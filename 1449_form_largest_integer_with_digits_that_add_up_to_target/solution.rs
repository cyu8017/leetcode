// LeetCode 1449 - Form Largest Integer With Digits That Add up to Target
// https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/

impl Solution {
    pub fn largest_number(cost: Vec<i32>, target: i32) -> String {
        let target = target as usize;
        let mut dp: Vec<Option<String>> = vec![None; target + 1];
        dp[0] = Some(String::new());
        for total in 1..=target {
            let mut best: Option<String> = None;
            for digit in 1..=9 {
                let price = cost[digit - 1] as usize;
                if total >= price {
                    if let Some(prev) = &dp[total - price] {
                        let candidate = format!("{}{}", digit, prev);
                        let take = match &best {
                            None => true,
                            Some(b) => {
                                (candidate.len(), candidate.as_str()) > (b.len(), b.as_str())
                            }
                        };
                        if take {
                            best = Some(candidate);
                        }
                    }
                }
            }
            dp[total] = best;
        }
        dp[target].clone().unwrap_or_else(|| "0".to_string())
    }
}
