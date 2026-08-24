// LeetCode 0830 - Positions of Large Groups
// https://leetcode.com/problems/positions-of-large-groups/

impl Solution {
    pub fn large_group_positions(s: String) -> Vec<Vec<i32>> {
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        let mut ans = Vec::new();
        let mut i = 0;
        while i < n {
            let mut j = i;
            while j < n && chars[j] == chars[i] {
                j += 1;
            }
            if j - i >= 3 {
                ans.push(vec![i as i32, (j - 1) as i32]);
            }
            i = j;
        }
        ans
    }
}
