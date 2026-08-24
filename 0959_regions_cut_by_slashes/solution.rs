// LeetCode 0959 - Regions Cut By Slashes
// https://leetcode.com/problems/regions-cut-by-slashes/

impl Solution {
    pub fn regions_by_slashes(grid: Vec<String>) -> i32 {
        let n = grid.len();
        let mut parent: Vec<usize> = (0..n * n * 4).collect();
        fn find(parent: &mut [usize], x: usize) -> usize {
            if parent[x] != x {
                parent[x] = find(parent, parent[x]);
            }
            parent[x]
        }
        fn unite(parent: &mut [usize], a: usize, b: usize) {
            let pa = find(parent, a);
            let pb = find(parent, b);
            parent[pa] = pb;
        }
        for r in 0..n {
            for c in 0..n {
                let root = 4 * (r * n + c);
                let ch = grid[r].as_bytes()[c];
                if ch == b'/' {
                    unite(&mut parent, root, root + 3);
                    unite(&mut parent, root + 1, root + 2);
                } else if ch == b'\\' {
                    unite(&mut parent, root, root + 1);
                    unite(&mut parent, root + 2, root + 3);
                } else {
                    unite(&mut parent, root, root + 1);
                    unite(&mut parent, root + 1, root + 2);
                    unite(&mut parent, root + 2, root + 3);
                }
                if r + 1 < n {
                    unite(&mut parent, root + 2, root + 4 * n);
                }
                if c + 1 < n {
                    unite(&mut parent, root + 1, root + 4 + 3);
                }
            }
        }
        let mut ans = 0;
        for i in 0..parent.len() {
            if find(&mut parent, i) == i {
                ans += 1;
            }
        }
        ans
    }
}
