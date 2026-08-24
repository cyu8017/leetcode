// LeetCode 2286 - Booking Concert Tickets in Groups
// https://leetcode.com/problems/booking-concert-tickets-in-groups/

#[derive(Clone, Copy, Default)]
struct Node {
    sum: i64,
    mx: i64,
}

pub struct BookMyShow {
    n: i32,
    m: i32,
    tree: Vec<Node>,
}

impl BookMyShow {
    fn pull(&mut self, idx: usize) {
        self.tree[idx].sum = self.tree[idx * 2].sum + self.tree[idx * 2 + 1].sum;
        self.tree[idx].mx = self.tree[idx * 2].mx.max(self.tree[idx * 2 + 1].mx);
    }

    fn build(&mut self, idx: usize, l: i32, r: i32) {
        if l == r {
            self.tree[idx] = Node {
                sum: self.m as i64,
                mx: self.m as i64,
            };
            return;
        }
        let mid = (l + r) / 2;
        self.build(idx * 2, l, mid);
        self.build(idx * 2 + 1, mid + 1, r);
        self.pull(idx);
    }

    fn update(&mut self, idx: usize, l: i32, r: i32, pos: i32, val: i64) {
        if l == r {
            self.tree[idx].sum = val;
            self.tree[idx].mx = val;
            return;
        }
        let mid = (l + r) / 2;
        if pos <= mid {
            self.update(idx * 2, l, mid, pos, val);
        } else {
            self.update(idx * 2 + 1, mid + 1, r, pos, val);
        }
        self.pull(idx);
    }

    fn query_sum(&self, idx: usize, l: i32, r: i32, ql: i32, qr: i32) -> i64 {
        if qr < l || r < ql {
            return 0;
        }
        if ql <= l && r <= qr {
            return self.tree[idx].sum;
        }
        let mid = (l + r) / 2;
        self.query_sum(idx * 2, l, mid, ql, qr) + self.query_sum(idx * 2 + 1, mid + 1, r, ql, qr)
    }

    fn find_first(&self, idx: usize, l: i32, r: i32, max_row: i32, k: i64) -> i32 {
        if l > max_row || self.tree[idx].mx < k {
            return -1;
        }
        if l == r {
            return l;
        }
        let mid = (l + r) / 2;
        let left = self.find_first(idx * 2, l, mid, max_row, k);
        if left != -1 {
            return left;
        }
        self.find_first(idx * 2 + 1, mid + 1, r, max_row, k)
    }

    pub fn new(n: i32, m: i32) -> Self {
        let mut this = Self {
            n,
            m,
            tree: vec![Node::default(); 4 * n as usize],
        };
        this.build(1, 0, n - 1);
        this
    }

    pub fn gather(&mut self, k: i32, max_row: i32) -> Vec<i32> {
        let row = self.find_first(1, 0, self.n - 1, max_row, k as i64);
        if row == -1 {
            return vec![];
        }
        let remain = self.query_sum(1, 0, self.n - 1, row, row);
        let seat = self.m as i64 - remain;
        self.update(1, 0, self.n - 1, row, remain - k as i64);
        vec![row, seat as i32]
    }

    pub fn scatter(&mut self, k: i32, max_row: i32) -> bool {
        if self.query_sum(1, 0, self.n - 1, 0, max_row) < k as i64 {
            return false;
        }
        let mut need = k as i64;
        let mut row = 0;
        while row <= max_row && need > 0 {
            let remain = self.query_sum(1, 0, self.n - 1, row, row);
            if remain != 0 {
                let take = remain.min(need);
                self.update(1, 0, self.n - 1, row, remain - take);
                need -= take;
            }
            row += 1;
        }
        true
    }
}
