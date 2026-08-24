// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

impl Solution {
    pub fn color_red(n: i32) -> Vec<Vec<i32>> {
        let mut ans = Vec::new();
        for i in 1..=n {
            ans.push(vec![i, 1]);
        }
        let mut i = n % 2 + 2;
        while i <= n {
            let mut j = 2;
            while j <= 2 * (n - i) + 2 {
                ans.push(vec![i, j]);
                j += 1;
            }
            i += 2;
        }
        ans
    }
}
