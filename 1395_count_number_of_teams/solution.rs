// LeetCode 1395 - Count Number of Teams
// https://leetcode.com/problems/count-number-of-teams/

impl Solution {
    pub fn num_teams(rating: Vec<i32>) -> i32 {
        let mut ans = 0;
        for (j, &x) in rating.iter().enumerate() {
            let ll = rating[..j].iter().filter(|&&y| y < x).count();
            let lg = j - ll;
            let rg = rating[j + 1..].iter().filter(|&&y| y > x).count();
            let rl = rating.len() - j - 1 - rg;
            ans += (ll * rg + lg * rl) as i32;
        }
        ans
    }
}
