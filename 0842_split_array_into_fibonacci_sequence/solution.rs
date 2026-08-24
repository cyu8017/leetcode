// LeetCode 0842 - Split Array into Fibonacci Sequence
// https://leetcode.com/problems/split-array-into-fibonacci-sequence/

impl Solution {
    pub fn split_into_fibonacci(num: String) -> Vec<i32> {
        let chars: Vec<u8> = num.into_bytes();
        let n = chars.len();
        let mut path = Vec::new();
        Self::dfs(&chars, 0, n, &mut path);
        path
    }

    fn dfs(num: &[u8], start: usize, n: usize, path: &mut Vec<i32>) -> bool {
        if start == n {
            return path.len() >= 3;
        }
        let mut val = 0i64;
        for end in start..n {
            if num[start] == b'0' && end > start {
                break;
            }
            val = val * 10 + (num[end] - b'0') as i64;
            if val > i32::MAX as i64 {
                break;
            }
            if path.len() >= 2 {
                let total = path[path.len() - 1] as i64 + path[path.len() - 2] as i64;
                if val < total {
                    continue;
                }
                if val > total {
                    break;
                }
            }
            path.push(val as i32);
            if Self::dfs(num, end + 1, n, path) {
                return true;
            }
            path.pop();
        }
        false
    }
}
