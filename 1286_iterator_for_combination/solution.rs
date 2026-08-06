// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

struct CombinationIterator {
    items: Vec<String>,
    idx: usize,
}

impl CombinationIterator {
    fn new(characters: String, combination_length: i32) -> Self {
        let chars: Vec<u8> = characters.into_bytes();
        let combination_length = combination_length as usize;
        let mut items = Vec::new();
        fn dfs(start: usize, cur: &mut Vec<u8>, chars: &[u8], len: usize, items: &mut Vec<String>) {
            if cur.len() == len {
                items.push(String::from_utf8(cur.clone()).unwrap());
                return;
            }
            for i in start..chars.len() {
                cur.push(chars[i]);
                dfs(i + 1, cur, chars, len, items);
                cur.pop();
            }
        }
        dfs(0, &mut Vec::new(), &chars, combination_length, &mut items);
        Self { items, idx: 0 }
    }

    fn next(&mut self) -> String {
        let v = self.items[self.idx].clone();
        self.idx += 1;
        v
    }

    fn has_next(&self) -> bool {
        self.idx < self.items.len()
    }
}
