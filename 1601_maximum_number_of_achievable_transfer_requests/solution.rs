// LeetCode 1601 - Maximum Number of Achievable Transfer Requests
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

impl Solution {
    pub fn maximum_requests(n: i32, requests: Vec<Vec<i32>>) -> i32 {
        let m = requests.len();
        let mut ans = 0;
        for mask in 0u32..(1u32 << m) {
            let cnt = mask.count_ones() as i32;
            if cnt <= ans {
                continue;
            }
            let mut bal = vec![0i32; n as usize];
            for (i, req) in requests.iter().enumerate() {
                if mask >> i & 1 == 1 {
                    bal[req[0] as usize] -= 1;
                    bal[req[1] as usize] += 1;
                }
            }
            if bal.iter().all(|&v| v == 0) {
                ans = cnt;
            }
        }
        ans
    }
}
