// LeetCode 1362 - Closest Divisors
// https://leetcode.com/problems/closest-divisors/

impl Solution {
    pub fn closest_divisors(num: i32) -> Vec<i32> {
        let mut best: Option<Vec<i32>> = None;
        for x in [num + 1, num + 2] {
            let mut a = (x as f64).sqrt() as i32;
            while a > 0 {
                if x % a == 0 {
                    let pair = vec![a, x / a];
                    best = Some(match best {
                        None => pair,
                        Some(cur) if pair[1] - pair[0] < cur[1] - cur[0] => pair,
                        Some(cur) => cur,
                    });
                    break;
                }
                a -= 1;
            }
        }
        best.unwrap()
    }
}
