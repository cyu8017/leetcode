// LeetCode 3613 - Minimize Maximum Component Cost
// https://leetcode.com/problems/minimize-maximum-component-cost/

impl Solution {
    pub fn min_cost(n: i32, mut edges: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = n as usize;
        let mut p: Vec<usize> = (0..n).collect();
        fn find(p: &mut [usize], x: usize) -> usize {
            if p[x] != x {
                p[x] = find(p, p[x]);
            }
            p[x]
        }
        if k == n as i32 {
            return 0;
        }
        edges.sort_by_key(|e| e[2]);
        let mut cnt = n as i32;
        for e in edges {
            let pu = find(&mut p, e[0] as usize);
            let pv = find(&mut p, e[1] as usize);
            if pu != pv {
                p[pu] = pv;
                cnt -= 1;
                if cnt <= k {
                    return e[2];
                }
            }
        }
        0
    }
}
