// LeetCode 1718 - Construct the Lexicographically Largest Valid Sequence
// https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

impl Solution {
    pub fn construct_distanced_sequence(n: i32) -> Vec<i32> {
        fn backtrack(mut i: usize, n: i32, ans: &mut Vec<i32>, used: &mut Vec<bool>) -> bool {
            while i < ans.len() && ans[i] != 0 {
                i += 1;
            }
            if i == ans.len() {
                return true;
            }
            for value in (1..=n).rev() {
                if used[value as usize] {
                    continue;
                }
                if value == 1 {
                    ans[i] = 1;
                    used[1] = true;
                    if backtrack(i + 1, n, ans, used) {
                        return true;
                    }
                    used[1] = false;
                    ans[i] = 0;
                } else {
                    let j = i + value as usize;
                    if j < ans.len() && ans[j] == 0 {
                        ans[i] = value;
                        ans[j] = value;
                        used[value as usize] = true;
                        if backtrack(i + 1, n, ans, used) {
                            return true;
                        }
                        used[value as usize] = false;
                        ans[i] = 0;
                        ans[j] = 0;
                    }
                }
            }
            false
        }

        let size = (2 * n - 1) as usize;
        let mut ans = vec![0; size];
        let mut used = vec![false; (n + 1) as usize];
        backtrack(0, n, &mut ans, &mut used);
        ans
    }
}
