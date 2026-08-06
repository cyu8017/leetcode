// LeetCode 1477 - Find Two Non-overlapping Sub-arrays Each With Target Sum
// https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

impl Solution {
    pub fn min_sum_of_lengths(arr: Vec<i32>, target: i32) -> i32 {
        let inf = i32::MAX / 4;
        let mut left = 0usize;
        let mut total = 0;
        let mut best = inf;
        let mut ans = inf;
        let mut shortest = vec![inf; arr.len()];
        for (right, &x) in arr.iter().enumerate() {
            total += x;
            while total > target {
                total -= arr[left];
                left += 1;
            }
            if total == target {
                let length = (right - left + 1) as i32;
                if left > 0 {
                    ans = ans.min(length + shortest[left - 1]);
                }
                best = best.min(length);
            }
            shortest[right] = best;
        }
        if ans == inf { -1 } else { ans }
    }
}
