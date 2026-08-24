struct Solution;
// LeetCode 3447 - Assign Elements to Groups with Constraints
// https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

impl Solution {
    pub fn assign_elements(groups: Vec<i32>, elements: Vec<i32>) -> Vec<i32> {
        const MAX_V: usize = 100001;
        let mut first = vec![-1; MAX_V];
        for (i, &e) in elements.iter().enumerate() {
            if (e as usize) < MAX_V && first[e as usize] == -1 {
                first[e as usize] = i as i32;
            }
        }
        let mut ans = vec![0; groups.len()];
        for (gi, &g) in groups.iter().enumerate() {
            let mut best = -1;
            let mut d = 1;
            while d * d <= g {
                if g % d == 0 {
                    if first[d as usize] != -1 && (best == -1 || first[d as usize] < best) {
                        best = first[d as usize];
                    }
                    let other = g / d;
                    if first[other as usize] != -1 && (best == -1 || first[other as usize] < best) {
                        best = first[other as usize];
                    }
                }
                d += 1;
            }
            ans[gi] = best;
        }
        ans
    }
}

fn main() {}
