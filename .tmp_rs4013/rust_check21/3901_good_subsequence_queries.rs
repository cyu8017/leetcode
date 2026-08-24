struct Solution;
// LeetCode 3901 - Good Subsequence Queries
// https://leetcode.com/problems/good-subsequence-queries/

struct Node {
    l: i32,
    r: i32,
    g: i32,
}

fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

struct SegmentTree {
    tr: Vec<Node>,
}

impl SegmentTree {
    fn new(n: usize) -> Self {
        let mut st = Self {
            tr: (0..(n << 2)).map(|_| Node { l: 0, r: 0, g: 0 }).collect(),
        };
        st.build(1, 1, n as i32);
        st
    }
    fn build(&mut self, u: usize, l: i32, r: i32) {
        self.tr[u] = Node { l, r, g: 0 };
        if l == r {
            return;
        }
        let mid = (l + r) >> 1;
        self.build(u << 1, l, mid);
        self.build(u << 1 | 1, mid + 1, r);
    }
    fn pushup(&mut self, u: usize) {
        self.tr[u].g = gcd(self.tr[u << 1].g, self.tr[u << 1 | 1].g);
    }
    fn modify(&mut self, u: usize, x: i32, v: i32) {
        if self.tr[u].l == self.tr[u].r {
            self.tr[u].g = v;
            return;
        }
        let mid = (self.tr[u].l + self.tr[u].r) >> 1;
        if x <= mid {
            self.modify(u << 1, x, v);
        } else {
            self.modify(u << 1 | 1, x, v);
        }
        self.pushup(u);
    }
    fn query(&self, u: usize, l: i32, r: i32) -> i32 {
        if l > r {
            return 0;
        }
        if self.tr[u].l >= l && self.tr[u].r <= r {
            return self.tr[u].g;
        }
        let mid = (self.tr[u].l + self.tr[u].r) >> 1;
        if r <= mid {
            return self.query(u << 1, l, r);
        }
        if l > mid {
            return self.query(u << 1 | 1, l, r);
        }
        gcd(self.query(u << 1, l, mid), self.query(u << 1 | 1, mid + 1, r))
    }
}

impl Solution {
    pub fn count_good_subseq(mut nums: Vec<i32>, p: i32, queries: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        let mut tree = SegmentTree::new(n);
        let mut cnt = 0;
        for i in 0..n {
            if nums[i] % p == 0 {
                tree.modify(1, (i + 1) as i32, nums[i]);
                cnt += 1;
            }
        }
        let mut ans = 0;
        for q in queries {
            let idx = q[0] as usize;
            let val = q[1];
            if nums[idx] % p == 0 {
                tree.modify(1, (idx + 1) as i32, 0);
                cnt -= 1;
            }
            if val % p == 0 {
                tree.modify(1, (idx + 1) as i32, val);
                cnt += 1;
            }
            nums[idx] = val;
            if tree.tr[1].g != p {
                continue;
            }
            if cnt < n as i32 || n > 6 {
                ans += 1;
                continue;
            }
            for i in 1..=n as i32 {
                let left_g = tree.query(1, 1, i - 1);
                let right_g = tree.query(1, i + 1, n as i32);
                if gcd(left_g, right_g) == p {
                    ans += 1;
                    break;
                }
            }
        }
        ans
    }
}
