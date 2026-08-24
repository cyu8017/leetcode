struct Solution;
// LeetCode 2890 - Reshape Data: Melt
// https://leetcode.com/problems/reshape-data-melt/

impl Solution {
    pub fn melt_table(report: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut out = Vec::new();
        for r in report {
            if r.is_empty() {
                continue;
            }
            let product = r[0];
            for (q, &sales) in r.iter().enumerate().skip(1) {
                out.push(vec![product, q as i32, sales]);
            }
        }
        out
    }
}

fn main() {}
