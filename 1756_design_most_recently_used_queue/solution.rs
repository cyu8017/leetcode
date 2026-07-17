// LeetCode 1756 - Design Most Recently Used Queue
// https://leetcode.com/problems/design-most-recently-used-queue/

struct MRUQueue {
    q: Vec<i32>,
}

impl MRUQueue {
    fn new(n: i32) -> Self {
        MRUQueue {
            q: (1..=n).collect(),
        }
    }

    fn fetch(&mut self, k: i32) -> i32 {
        let val = self.q.remove((k - 1) as usize);
        self.q.push(val);
        val
    }
}
