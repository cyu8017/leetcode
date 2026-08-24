struct Solution;
// LeetCode 3937 - Minimum Operations To Make Array Modulo Alternating I
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

impl Solution {
    pub fn min_operations(mut nums: Vec<i32>, k: i32) -> i32 {
        for v in nums.iter_mut() {
            *v %= k;
        }
        let mut ans = i32::MAX;
        for x in 0..k {
            for y in 0..k {
                if x == y {
                    continue;
                }
                let mut cnt = 0;
                for (i, &num) in nums.iter().enumerate() {
                    let target = if i & 1 == 1 { y } else { x };
                    let diff = (target - num).abs();
                    cnt += diff.min(k - diff);
                }
                ans = ans.min(cnt);
            }
        }
        ans
    }
}

fn main() {}
