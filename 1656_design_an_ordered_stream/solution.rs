// LeetCode 1656 - Design an Ordered Stream
// https://leetcode.com/problems/design-an-ordered-stream/

pub struct OrderedStream {
    a: Vec<Option<String>>,
    p: usize,
}

impl OrderedStream {
    pub fn new(n: i32) -> Self {
        Self {
            a: vec![None; (n + 1) as usize],
            p: 1,
        }
    }

    pub fn insert(&mut self, id_key: i32, value: String) -> Vec<String> {
        self.a[id_key as usize] = Some(value);
        let mut out = Vec::new();
        while self.p < self.a.len() && self.a[self.p].is_some() {
            out.push(self.a[self.p].take().unwrap());
            self.p += 1;
        }
        out
    }
}
