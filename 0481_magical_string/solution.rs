// LeetCode 0481 - Magical String
// https://leetcode.com/problems/magical-string/

impl Solution {
    pub fn magical_string(n: i32) -> i32 {
        if n == 0 {
            return 0;
        }
        let n = n as usize;
        let mut seq = vec![1, 2, 2];
        let mut index = 2;
        while seq.len() < n {
            if seq[index] == 1 {
                seq.push(if *seq.last().unwrap() == 2 { 1 } else { 2 });
            } else {
                let value = if *seq.last().unwrap() == 2 { 1 } else { 2 };
                seq.push(value);
                seq.push(value);
            }
            index += 1;
        }
        seq[..n].iter().filter(|&&value| value == 1).count() as i32
    }
}
