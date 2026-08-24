// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

impl Solution {
    pub fn punishment_number(n: i32) -> i32 {
        fn can(sq: i32, target: i32) -> bool {
            let s = sq.to_string();
            let bytes = s.as_bytes();
            fn dfs(bytes: &[u8], i: usize, sum: i32, target: i32) -> bool {
                if i == bytes.len() {
                    return sum == target;
                }
                let mut cur = 0;
                for j in i..bytes.len() {
                    cur = cur * 10 + (bytes[j] - b'0') as i32;
                    if sum + cur > target {
                        break;
                    }
                    if dfs(bytes, j + 1, sum + cur, target) {
                        return true;
                    }
                }
                false
            }
            dfs(bytes, 0, 0, target)
        }
        let mut ans = 0;
        for i in 1..=n {
            let sq = i * i;
            if can(sq, i) {
                ans += sq;
            }
        }
        ans
    }
}
