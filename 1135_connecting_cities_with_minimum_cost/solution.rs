// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

impl Solution {
    pub fn minimum_cost(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut parent: Vec<usize> = (0..=n).collect();
        fn find(parent: &mut [usize], mut x: usize) -> usize {
            while parent[x] != x {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }
        let mut connections = connections;
        connections.sort_by_key(|e| e[2]);
        let mut ans = 0;
        let mut used = 0;
        for e in connections {
            let a = find(&mut parent, e[0] as usize);
            let b = find(&mut parent, e[1] as usize);
            if a == b {
                continue;
            }
            parent[b] = a;
            ans += e[2];
            used += 1;
            if used == n - 1 {
                return ans;
            }
        }
        -1
    }
}
