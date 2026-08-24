// LeetCode 3777 - Minimum Deletions To Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

struct Bit {
    n: usize,
    c: Vec<i32>,
}

impl Bit {
    fn new(n: usize) -> Self {
        Self {
            n,
            c: vec![0; n + 1],
        }
    }

    fn update(&mut self, mut x: usize, delta: i32) {
        while x <= self.n {
            self.c[x] += delta;
            x += x & x.wrapping_neg();
        }
    }

    fn query(&self, mut x: usize) -> i32 {
        let mut s = 0;
        while x > 0 {
            s += self.c[x];
            x -= x & x.wrapping_neg();
        }
        s
    }
}

impl Solution {
    pub fn min_deletions(s: String, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = s.len();
        let bytes = s.as_bytes();
        let mut nums = vec![0i32; n];
        let mut bit = Bit::new(n);
        for i in 1..n {
            if bytes[i] == bytes[i - 1] {
                nums[i] = 1;
                bit.update(i + 1, 1);
            }
        }
        let mut ans = Vec::new();
        for q in queries {
            if q[0] == 1 {
                let j = q[1] as usize;
                let delta = (nums[j] ^ 1) - nums[j];
                nums[j] ^= 1;
                bit.update(j + 1, delta);
                if j + 1 < n {
                    let delta = (nums[j + 1] ^ 1) - nums[j + 1];
                    nums[j + 1] ^= 1;
                    bit.update(j + 2, delta);
                }
            } else {
                let l = q[1] as usize;
                let r = q[2] as usize;
                ans.push(bit.query(r + 1) - bit.query(l + 1));
            }
        }
        ans
    }
}
