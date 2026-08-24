// LeetCode 2359 - Find Closest Node to Given Two Nodes
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

impl Solution {
    pub fn closest_meeting_node(edges: Vec<i32>, node1: i32, node2: i32) -> i32 {
        let n = edges.len();
        let dist = |start: i32| {
            let mut d = vec![-1i32; n];
            let mut cur = start;
            let mut step = 0;
            while cur != -1 && d[cur as usize] == -1 {
                d[cur as usize] = step;
                cur = edges[cur as usize];
                step += 1;
            }
            d
        };
        let d1 = dist(node1);
        let d2 = dist(node2);
        let mut ans = -1;
        let mut best = i32::MAX;
        for i in 0..n {
            if d1[i] == -1 || d2[i] == -1 {
                continue;
            }
            let mx = d1[i].max(d2[i]);
            if mx < best {
                best = mx;
                ans = i as i32;
            }
        }
        ans
    }
}
