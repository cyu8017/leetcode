// LeetCode 2147 - Number of Ways to Divide a Long Corridor
// https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

impl Solution {
    pub fn number_of_ways(corridor: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let seats: Vec<usize> = corridor
            .bytes()
            .enumerate()
            .filter(|&(_, c)| c == b'S')
            .map(|(i, _)| i)
            .collect();
        if seats.is_empty() || seats.len() % 2 == 1 {
            return 0;
        }
        let mut ans = 1i64;
        let mut i = 2;
        while i < seats.len() {
            ans = ans * (seats[i] - seats[i - 1]) as i64 % MOD;
            i += 2;
        }
        ans as i32
    }
}
