// LeetCode 0351 - Android Unlock Patterns
// https://leetcode.com/problems/android-unlock-patterns/

impl Solution {
    fn jump_middle(last: i32, next_cell: i32) -> i32 {
        const JUMPS: [i32; 81] = [
            -1, -1, 1, -1, -1, -1, 3, -1, 4,
            -1, -1, -1, 2, -1, 4, -1, -1, -1,
            1, -1, -1, -1, 6, -1, -1, -1, 5,
            -1, 2, -1, -1, -1, 5, -1, 6, -1,
            -1, -1, 4, -1, -1, -1, 7, -1, 8,
            -1, -1, -1, 5, -1, -1, -1, 8, -1,
            3, -1, 7, -1, -1, -1, -1, -1, 7,
            -1, -1, -1, 6, -1, 8, -1, -1, -1,
            4, -1, 5, -1, -1, -1, 7, -1, -1,
        ];
        JUMPS[(last * 9 + next_cell) as usize]
    }

    fn is_valid(visited: i32, last: i32, next_cell: i32) -> bool {
        if visited & (1 << next_cell) != 0 {
            return false;
        }

        let middle = Self::jump_middle(last, next_cell);
        if middle >= 0 {
            return visited & (1 << middle) == 0;
        }

        (last / 3 - next_cell / 3).abs() <= 1 && (last % 3 - next_cell % 3).abs() <= 1
    }

    fn dfs(visited: i32, last: i32, length: i32, m: i32, n: i32) -> i32 {
        if length > n {
            return 0;
        }

        let mut count = if m <= length && length <= n { 1 } else { 0 };
        for next_cell in 0..9 {
            if Self::is_valid(visited, last, next_cell) {
                count += Self::dfs(visited | (1 << next_cell), next_cell, length + 1, m, n);
            }
        }

        count
    }

    pub fn number_of_patterns(m: i32, n: i32) -> i32 {
        Self::dfs(1 << 0, 0, 1, m, n) * 4
            + Self::dfs(1 << 1, 1, 1, m, n) * 4
            + Self::dfs(1 << 4, 4, 1, m, n)
    }
}
