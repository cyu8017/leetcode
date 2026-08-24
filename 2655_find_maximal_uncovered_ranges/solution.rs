// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

impl Solution {
    pub fn find_maximal_uncovered_ranges(n: i32, mut ranges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        ranges.sort_unstable();
        let mut ans = Vec::new();
        let mut cur = 0;
        for r in &ranges {
            if r[0] > cur {
                ans.push(vec![cur, r[0] - 1]);
            }
            if r[1] + 1 > cur {
                cur = r[1] + 1;
            }
        }
        if cur < n {
            ans.push(vec![cur, n - 1]);
        }
        ans
    }
}
