// LeetCode 2924 - Find Champion II
// https://leetcode.com/problems/find-champion-ii/

impl Solution {
    pub fn find_champion(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let mut indeg = vec![0i32; n as usize];
        for e in edges {
            indeg[e[1] as usize] += 1;
        }
        let mut ans = -1;
        for i in 0..n {
            if indeg[i as usize] == 0 {
                if ans != -1 {
                    return -1;
                }
                ans = i;
            }
        }
        ans
    }
}
