struct Solution;
// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

impl Solution {
    pub fn max_profit(mut workers: Vec<i32>, mut tasks: Vec<Vec<i32>>) -> i64 {
        workers.sort_unstable();
        tasks.sort_by_key(|a| a[0]);
        let mut ans = 0i64;
        let mut used = vec![false; tasks.len()];
        for w in workers {
            let mut best = -1;
            let mut bi = -1i32;
            for i in 0..tasks.len() {
                if used[i] {
                    continue;
                }
                if tasks[i][0] > w {
                    break;
                }
                if tasks[i][1] > best {
                    best = tasks[i][1];
                    bi = i as i32;
                }
            }
            if bi >= 0 {
                used[bi as usize] = true;
                ans += best as i64;
            }
        }
        ans
    }
}

fn main() {}
