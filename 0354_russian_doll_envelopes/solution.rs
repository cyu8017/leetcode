// LeetCode 0354 - Russian Doll Envelopes
// https://leetcode.com/problems/russian-doll-envelopes/

impl Solution {
    pub fn max_envelopes(mut envelopes: Vec<Vec<i32>>) -> i32 {
        envelopes.sort_by(|left, right| {
            if left[0] != right[0] {
                left[0].cmp(&right[0])
            } else {
                right[1].cmp(&left[1])
            }
        });

        let mut tails = Vec::new();
        for envelope in envelopes {
            let height = envelope[1];
            match tails.binary_search(&height) {
                Ok(index) => tails[index] = height,
                Err(index) => {
                    if index == tails.len() {
                        tails.push(height);
                    } else {
                        tails[index] = height;
                    }
                }
            }
        }

        tails.len() as i32
    }
}
