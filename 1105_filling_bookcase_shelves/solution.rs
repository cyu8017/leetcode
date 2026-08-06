// LeetCode 1105 - Filling Bookcase Shelves
// https://leetcode.com/problems/filling-bookcase-shelves/

impl Solution {
    pub fn min_height_shelves(books: Vec<Vec<i32>>, shelf_width: i32) -> i32 {
        let n = books.len();
        let mut dp = vec![0; n + 1];
        for i in 1..=n {
            let mut width = 0;
            let mut height = 0;
            dp[i] = i32::MAX;
            for j in (1..=i).rev() {
                let w = books[j - 1][0];
                let h = books[j - 1][1];
                width += w;
                if width > shelf_width {
                    break;
                }
                height = height.max(h);
                dp[i] = dp[i].min(dp[j - 1] + height);
            }
        }
        dp[n]
    }
}
