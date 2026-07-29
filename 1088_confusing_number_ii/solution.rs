// LeetCode 1088 - Confusing Number II
// https://leetcode.com/problems/confusing-number-ii/

impl Solution {
    pub fn confusing_number_ii(n: i32) -> i32 {
        let rotate = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6];
        let digits = [0, 1, 6, 8, 9];
        let mut ans = 0;

        fn is_confusing(mut num: i32, rotate: &[i32; 10]) -> bool {
            let original = num;
            let mut rotated = 0;
            while num > 0 {
                let d = (num % 10) as usize;
                rotated = rotated * 10 + rotate[d];
                num /= 10;
            }
            rotated != original
        }

        fn dfs(cur: i64, n: i64, ans: &mut i32, digits: &[i32; 5], rotate: &[i32; 10]) {
            if cur > n {
                return;
            }
            if cur > 0 && is_confusing(cur as i32, rotate) {
                *ans += 1;
            }
            if cur == 0 {
                for &d in &[1, 6, 8, 9] {
                    dfs(d as i64, n, ans, digits, rotate);
                }
            } else {
                for &d in digits {
                    dfs(cur * 10 + d as i64, n, ans, digits, rotate);
                }
            }
        }

        dfs(0, n as i64, &mut ans, &digits, &rotate);
        ans
    }
}
