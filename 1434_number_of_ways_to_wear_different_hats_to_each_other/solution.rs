// LeetCode 1434 - Number of Ways to Wear Different Hats to Each Other
// https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

impl Solution {
    pub fn number_ways(hats: Vec<Vec<i32>>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let people = hats.len();
        let mut wearers = vec![Vec::new(); 41];
        for (person, choices) in hats.into_iter().enumerate() {
            for hat in choices {
                wearers[hat as usize].push(person);
            }
        }
        let mut dp = vec![0; 1 << people];
        dp[0] = 1;
        for hat in 1..=40 {
            let mut nxt = dp.clone();
            for (mask, &ways) in dp.iter().enumerate() {
                for &person in &wearers[hat] {
                    if mask >> person & 1 == 0 {
                        let nm = mask | (1 << person);
                        nxt[nm] = (nxt[nm] + ways) % MOD;
                    }
                }
            }
            dp = nxt;
        }
        dp[(1 << people) - 1]
    }
}
