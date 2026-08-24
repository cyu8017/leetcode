// LeetCode 2151 - Maximum Good People Based on Statements
// https://leetcode.com/problems/maximum-good-people-based-on-statements/

impl Solution {
    pub fn maximum_good(statements: Vec<Vec<i32>>) -> i32 {
        let n = statements.len();
        let mut ans = 0;
        for mask in 0..(1 << n) {
            let mut ok = true;
            for i in 0..n {
                if (mask & (1 << i)) == 0 {
                    continue;
                }
                for j in 0..n {
                    let s = statements[i][j];
                    if s == 2 {
                        continue;
                    }
                    let good_j = (mask & (1 << j)) != 0;
                    if (s == 1 && !good_j) || (s == 0 && good_j) {
                        ok = false;
                    }
                }
            }
            if ok {
                ans = ans.max(mask.count_ones() as i32);
            }
        }
        ans
    }
}
