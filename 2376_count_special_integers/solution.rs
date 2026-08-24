// LeetCode 2376 - Count Special Integers
// https://leetcode.com/problems/count-special-integers/

impl Solution {
    pub fn count_special_numbers(n: i32) -> i32 {
        let s = n.to_string();
        let m = s.len();
        let bytes = s.as_bytes();
        let mut ans = 0;
        let mut perm = 9;
        for i in 1..m {
            ans += perm;
            perm *= 10 - i as i32;
        }
        let mut used = [false; 10];
        for i in 0..m {
            let start = if i == 0 { 1 } else { 0 };
            let digit = (bytes[i] - b'0') as i32;
            for d in start..digit {
                if used[d as usize] {
                    continue;
                }
                let mut rem = 10 - (i as i32 + 1);
                let mut ways = 1;
                for _ in i + 1..m {
                    ways *= rem;
                    rem -= 1;
                }
                ans += ways;
            }
            if used[digit as usize] {
                return ans;
            }
            used[digit as usize] = true;
        }
        ans + 1
    }
}
