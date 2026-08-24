struct Solution;
// LeetCode 3224 - Minimum Array Changes to Make Differences Equal
// https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

impl Solution {
    pub fn min_changes(nums: Vec<i32>, k: i32) -> i32 {
        let mut d = vec![0; (k + 2) as usize];
        let n = nums.len();
        for i in 0..n / 2 {
            let mut x = nums[i];
            let mut y = nums[n - 1 - i];
            if x > y {
                std::mem::swap(&mut x, &mut y);
            }
            d[0] += 1;
            d[(y - x) as usize] -= 1;
            d[(y - x + 1) as usize] += 1;
            let mx = y.max(k - x);
            d[(mx + 1) as usize] -= 1;
            d[(mx + 1) as usize] += 2;
        }
        let mut ans = n as i32;
        let mut s = 0;
        for x in d {
            s += x;
            ans = ans.min(s);
        }
        ans
    }
}

fn main() {}
