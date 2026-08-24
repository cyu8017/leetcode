// LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
// https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

impl Solution {
    pub fn min_swaps(nums: Vec<i32>) -> i32 {
        let mut pos = [Vec::<i32>::new(), Vec::<i32>::new()];
        for (i, &x) in nums.iter().enumerate() {
            pos[(x & 1) as usize].push(i as i32);
        }
        if (pos[0].len() as i32 - pos[1].len() as i32).abs() > 1 {
            return -1;
        }
        let calc = |k: usize| -> i32 {
            let mut res = 0;
            let mut i = 0;
            while i < nums.len() {
                res += (pos[k][i / 2] - i as i32).abs();
                i += 2;
            }
            res
        };
        if pos[0].len() > pos[1].len() {
            calc(0)
        } else if pos[0].len() < pos[1].len() {
            calc(1)
        } else {
            calc(0).min(calc(1))
        }
    }
}
