// LeetCode 0997 - Find the Town Judge
// https://leetcode.com/problems/find-the-town-judge/

impl Solution {
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
        let mut score = vec![0; (n + 1) as usize];
        for t in trust {
            score[t[0] as usize] -= 1;
            score[t[1] as usize] += 1;
        }
        for i in 1..=n {
            if score[i as usize] == n - 1 {
                return i;
            }
        }
        -1
    }
}
