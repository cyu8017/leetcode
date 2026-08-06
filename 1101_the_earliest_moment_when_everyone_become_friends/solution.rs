// LeetCode 1101 - The Earliest Moment When Everyone Become Friends
// https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

impl Solution {
    pub fn earliest_acq(logs: Vec<Vec<i32>>, n: i32) -> i32 {
        let n = n as usize;
        let mut parent: Vec<usize> = (0..n).collect();
        fn find(parent: &mut [usize], mut x: usize) -> usize {
            while parent[x] != x {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }
        let mut logs = logs;
        logs.sort_by_key(|l| l[0]);
        let mut components = n;
        for log in logs {
            let a = find(&mut parent, log[1] as usize);
            let b = find(&mut parent, log[2] as usize);
            if a != b {
                parent[b] = a;
                components -= 1;
                if components == 1 {
                    return log[0];
                }
            }
        }
        -1
    }
}
