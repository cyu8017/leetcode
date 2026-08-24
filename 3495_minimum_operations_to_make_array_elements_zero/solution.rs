// LeetCode 3495 - Minimum Operations to Make Array Elements Zero
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

impl Solution {
    fn ops_to_zero(mut x: i32) -> i32 {
        let mut ops = 0;
        while x > 0 {
            x /= 4;
            ops += 1;
        }
        ops
    }

    pub fn min_operations(queries: Vec<Vec<i32>>) -> i64 {
        let mut ans = 0i64;
        for q in queries {
            let l = q[0];
            let r = q[1];
            let mut sum = 0i64;
            for x in l..=r {
                sum += Self::ops_to_zero(x) as i64;
            }
            ans += (sum + 1) / 2;
        }
        ans
    }
}
