// LeetCode 0851 - Loud and Rich
// https://leetcode.com/problems/loud-and-rich/

impl Solution {
    pub fn loud_and_rich(richer: Vec<Vec<i32>>, quiet: Vec<i32>) -> Vec<i32> {
        let n = quiet.len();
        let mut graph = vec![Vec::new(); n];
        for e in &richer {
            graph[e[1] as usize].push(e[0] as usize);
        }
        let mut ans = vec![-1; n];
        for i in 0..n {
            Self::dfs(i, &graph, &quiet, &mut ans);
        }
        ans
    }

    fn dfs(person: usize, graph: &[Vec<usize>], quiet: &[i32], ans: &mut [i32]) -> i32 {
        if ans[person] != -1 {
            return ans[person];
        }
        let mut best = person;
        for &richer_person in &graph[person] {
            let cand = Self::dfs(richer_person, graph, quiet, ans) as usize;
            if quiet[cand] < quiet[best] {
                best = cand;
            }
        }
        ans[person] = best as i32;
        ans[person]
    }
}
