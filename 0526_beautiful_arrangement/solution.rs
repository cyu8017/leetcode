// LeetCode 0526 - Beautiful Arrangement
// https://leetcode.com/problems/beautiful-arrangement/

impl Solution {
    pub fn count_arrangement(n: i32) -> i32 {
        let mut count = 0;
        let mut used = vec![false; (n + 1) as usize];

        fn backtrack(index: i32, n: i32, used: &mut [bool], count: &mut i32) {
            if index == n + 1 {
                *count += 1;
                return;
            }
            for num in 1..=n {
                if used[num as usize] {
                    continue;
                }
                if index % num == 0 || num % index == 0 {
                    used[num as usize] = true;
                    backtrack(index + 1, n, used, count);
                    used[num as usize] = false;
                }
            }
        }

        backtrack(1, n, &mut used, &mut count);
        count
    }
}
