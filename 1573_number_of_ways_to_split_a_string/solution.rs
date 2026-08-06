// LeetCode 1573 - Number of Ways to Split a String
// https://leetcode.com/problems/number-of-ways-to-split-a-string/

impl Solution {
    pub fn num_ways(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let ones = s.bytes().filter(|&c| c == b'1').count();
        if ones % 3 != 0 {
            return 0;
        }
        if ones == 0 {
            let gaps = s.len() as i64 - 1;
            return ((gaps * (gaps - 1) / 2) % MOD) as i32;
        }
        let target = ones / 3;
        let positions: Vec<usize> = s
            .bytes()
            .enumerate()
            .filter_map(|(i, c)| if c == b'1' { Some(i) } else { None })
            .collect();
        (((positions[target] - positions[target - 1]) as i64)
            * ((positions[2 * target] - positions[2 * target - 1]) as i64)
            % MOD) as i32
    }
}
