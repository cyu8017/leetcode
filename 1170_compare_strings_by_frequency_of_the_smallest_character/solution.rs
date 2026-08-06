// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

impl Solution {
    pub fn num_smaller_by_frequency(queries: Vec<String>, words: Vec<String>) -> Vec<i32> {
        fn f(s: &str) -> i32 {
            let mut best = b'z' + 1;
            let mut cnt = 0;
            for b in s.bytes() {
                if b < best {
                    best = b;
                    cnt = 1;
                } else if b == best {
                    cnt += 1;
                }
            }
            cnt
        }
        let wf: Vec<i32> = words.iter().map(|w| f(w)).collect();
        queries
            .iter()
            .map(|q| {
                let fq = f(q);
                wf.iter().filter(|&&w| w > fq).count() as i32
            })
            .collect()
    }
}
