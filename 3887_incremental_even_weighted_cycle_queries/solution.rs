// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

impl Solution {
    pub fn count_valid_edges(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut parent: Vec<usize> = (0..n).collect();
        let mut size = vec![1; n];
        let mut parity = vec![0; n];
        fn find(x: usize, parent: &mut [usize], parity: &mut [i32]) -> (usize, i32) {
            if parent[x] == x {
                return (x, 0);
            }
            let (root, p) = find(parent[x], parent, parity);
            parity[x] ^= p;
            parent[x] = root;
            (root, parity[x])
        }
        let mut ans = 0;
        for e in edges {
            let (mut ru, mut pu) = find(e[0] as usize, &mut parent, &mut parity);
            let (mut rv, mut pv) = find(e[1] as usize, &mut parent, &mut parity);
            if ru == rv {
                if (pu ^ pv) == e[2] {
                    ans += 1;
                }
                continue;
            }
            if size[ru] < size[rv] {
                std::mem::swap(&mut ru, &mut rv);
                std::mem::swap(&mut pu, &mut pv);
            }
            parent[rv] = ru;
            parity[rv] = pu ^ pv ^ e[2];
            size[ru] += size[rv];
            ans += 1;
        }
        ans
    }
}
