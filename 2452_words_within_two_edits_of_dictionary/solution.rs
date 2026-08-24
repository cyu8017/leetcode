// LeetCode 2452 - Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

impl Solution {
    pub fn two_edit_words(queries: Vec<String>, dictionary: Vec<String>) -> Vec<String> {
        let mut ans = Vec::new();
        for q in &queries {
            let qb = q.as_bytes();
            let mut ok = false;
            for d in &dictionary {
                let db = d.as_bytes();
                let mut diff = 0;
                for i in 0..qb.len() {
                    if qb[i] != db[i] {
                        diff += 1;
                        if diff > 2 {
                            break;
                        }
                    }
                }
                if diff <= 2 {
                    ok = true;
                    break;
                }
            }
            if ok {
                ans.push(q.clone());
            }
        }
        ans
    }
}
