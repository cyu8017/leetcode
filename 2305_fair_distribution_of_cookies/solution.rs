// LeetCode 2305 - Fair Distribution of Cookies
// https://leetcode.com/problems/fair-distribution-of-cookies/

impl Solution {
    pub fn distribute_cookies(cookies: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut bags = vec![0i32; k];
        let mut ans = i32::MAX;
        fn dfs(i: usize, cookies: &[i32], bags: &mut [i32], ans: &mut i32) {
            if i == cookies.len() {
                *ans = (*ans).min(*bags.iter().max().unwrap());
                return;
            }
            let mut seen = std::collections::HashSet::new();
            for j in 0..bags.len() {
                if !seen.insert(bags[j]) {
                    continue;
                }
                bags[j] += cookies[i];
                if bags[j] < *ans {
                    dfs(i + 1, cookies, bags, ans);
                }
                bags[j] -= cookies[i];
                if bags[j] == 0 {
                    break;
                }
            }
        }
        dfs(0, &cookies, &mut bags, &mut ans);
        ans
    }
}
