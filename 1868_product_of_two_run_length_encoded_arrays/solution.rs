// LeetCode 1868 - Product of Two Run-Length Encoded Arrays
// https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

impl Solution {
    pub fn find_rle_array(encoded1: Vec<Vec<i32>>, encoded2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut i = 0usize;
        let mut j = 0usize;
        let mut rem1 = encoded1[0][1];
        let mut rem2 = encoded2[0][1];
        while i < encoded1.len() {
            let take = rem1.min(rem2);
            let value = encoded1[i][0] * encoded2[j][0];
            if let Some(last) = result.last_mut() {
                if last[0] == value {
                    last[1] += take;
                } else {
                    result.push(vec![value, take]);
                }
            } else {
                result.push(vec![value, take]);
            }
            rem1 -= take;
            rem2 -= take;
            if rem1 == 0 {
                i += 1;
                if i < encoded1.len() {
                    rem1 = encoded1[i][1];
                }
            }
            if rem2 == 0 {
                j += 1;
                if j < encoded2.len() {
                    rem2 = encoded2[j][1];
                }
            }
        }
        result
    }
}
