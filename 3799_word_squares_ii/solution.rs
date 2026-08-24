// LeetCode 3799 - Word Squares Ii
// https://leetcode.com/problems/word-squares-ii/

impl Solution {
    pub fn word_squares(mut words: Vec<String>) -> Vec<Vec<String>> {
        words.sort();
        let n = words.len();
        let mut ans = Vec::new();
        for i in 0..n {
            let top = &words[i];
            for j in 0..n {
                if j == i {
                    continue;
                }
                let left = &words[j];
                for k in 0..n {
                    if k == j || k == i {
                        continue;
                    }
                    let right = &words[k];
                    for h in 0..n {
                        if h == k || h == j || h == i {
                            continue;
                        }
                        let bottom = &words[h];
                        let tb = top.as_bytes();
                        let lb = left.as_bytes();
                        let rb = right.as_bytes();
                        let bb = bottom.as_bytes();
                        if tb[0] == lb[0]
                            && tb[3] == rb[0]
                            && bb[0] == lb[3]
                            && bb[3] == rb[3]
                        {
                            ans.push(vec![
                                top.clone(),
                                left.clone(),
                                right.clone(),
                                bottom.clone(),
                            ]);
                        }
                    }
                }
            }
        }
        ans
    }
}
