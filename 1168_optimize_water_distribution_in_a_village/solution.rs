// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

impl Solution {
    pub fn min_cost_to_supply_water(n: i32, wells: Vec<i32>, pipes: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut parent: Vec<usize> = (0..=n).collect();
        fn find(parent: &mut [usize], mut x: usize) -> usize {
            while parent[x] != x {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }
        let mut edges = Vec::new();
        for (i, &w) in wells.iter().enumerate() {
            edges.push(vec![0, (i + 1) as i32, w]);
        }
        edges.extend(pipes);
        edges.sort_by_key(|e| e[2]);
        let mut ans = 0;
        for e in edges {
            let a = find(&mut parent, e[0] as usize);
            let b = find(&mut parent, e[1] as usize);
            if a == b {
                continue;
            }
            parent[b] = a;
            ans += e[2];
        }
        ans
    }
}
