// LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
// https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

impl Solution {
    pub fn max_subarrays(n: i32, conflicting_pairs: Vec<Vec<i32>>) -> i64 {
        let m = conflicting_pairs.len();
        let mut best = 0i64;
        for skip in 0..m {
            let mut banned = Vec::new();
            for i in 0..m {
                if i == skip {
                    continue;
                }
                let mut a = conflicting_pairs[i][0];
                let mut b = conflicting_pairs[i][1];
                if a > b {
                    std::mem::swap(&mut a, &mut b);
                }
                banned.push((a, b));
            }
            let mut right_limit = vec![n + 1; (n + 2) as usize];
            for &(a, b) in &banned {
                if b < right_limit[a as usize] {
                    right_limit[a as usize] = b;
                }
            }
            let mut min_right = n + 1;
            let mut cnt = 0i64;
            for l in (1..=n).rev() {
                if right_limit[l as usize] < min_right {
                    min_right = right_limit[l as usize];
                }
                cnt += (min_right - l) as i64;
            }
            if cnt > best {
                best = cnt;
            }
        }
        best
    }
}
