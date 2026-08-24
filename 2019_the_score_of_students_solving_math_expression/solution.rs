// LeetCode 2019 - The Score of Students Solving Math Expression
// https://leetcode.com/problems/the-score-of-students-solving-math-expression/

use std::collections::{HashMap, HashSet};

impl Solution {
    fn eval_correct(s: &str) -> i32 {
        let mut nums = Vec::new();
        let mut ops = Vec::new();
        for c in s.chars() {
            if c.is_ascii_digit() {
                nums.push((c as u8 - b'0') as i32);
            } else {
                ops.push(c);
            }
        }
        let mut new_nums = vec![nums[0]];
        let mut new_ops = Vec::new();
        for j in 0..ops.len() {
            if ops[j] == '*' {
                let last = new_nums.last_mut().unwrap();
                *last *= nums[j + 1];
            } else {
                new_ops.push(ops[j]);
                new_nums.push(nums[j + 1]);
            }
        }
        let mut res = new_nums[0];
        for j in 0..new_ops.len() {
            res += new_nums[j + 1];
        }
        res
    }

    pub fn score_of_students(s: String, answers: Vec<i32>) -> i32 {
        let n = s.len();
        let bytes = s.as_bytes();
        let correct = Self::eval_correct(&s);
        let mut memo: HashMap<(usize, usize), HashSet<i32>> = HashMap::new();
        fn dfs(
            l: usize,
            r: usize,
            bytes: &[u8],
            memo: &mut HashMap<(usize, usize), HashSet<i32>>,
        ) -> HashSet<i32> {
            if let Some(v) = memo.get(&(l, r)) {
                return v.clone();
            }
            let mut res = HashSet::new();
            if l == r {
                res.insert((bytes[l] - b'0') as i32);
                memo.insert((l, r), res.clone());
                return res;
            }
            let mut i = l + 1;
            while i < r {
                let left = dfs(l, i - 1, bytes, memo);
                let right = dfs(i + 1, r, bytes, memo);
                for a in &left {
                    for b in &right {
                        let v = if bytes[i] == b'+' { a + b } else { a * b };
                        if v <= 1000 {
                            res.insert(v);
                        }
                    }
                }
                i += 2;
            }
            memo.insert((l, r), res.clone());
            res
        }
        let possible = dfs(0, n - 1, bytes, &mut memo);
        let mut ans = 0;
        for a in answers {
            if a == correct {
                ans += 5;
            } else if possible.contains(&a) {
                ans += 2;
            }
        }
        ans
    }
}
