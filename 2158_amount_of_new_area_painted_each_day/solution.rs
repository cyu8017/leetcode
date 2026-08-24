// LeetCode 2158 - Amount of New Area Painted Each Day
// https://leetcode.com/problems/amount-of-new-area-painted-each-day/

impl Solution {
    pub fn amount_painted(paint: Vec<Vec<i32>>) -> Vec<i32> {
        let mut ans = vec![0; paint.len()];
        let mut line = vec![0i32; 50001];
        for (i, p) in paint.iter().enumerate() {
            let (start, end) = (p[0], p[1]);
            let mut j = start;
            while j < end {
                if line[j as usize] == 0 {
                    ans[i] += 1;
                    line[j as usize] = end;
                    j += 1;
                } else {
                    let next = line[j as usize];
                    line[j as usize] = end.max(next);
                    j = next;
                }
            }
        }
        ans
    }
}
