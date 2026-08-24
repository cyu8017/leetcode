// LeetCode 2213 - Longest Substring of One Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/

#[derive(Clone, Copy)]
struct Seg {
    l_char: u8,
    r_char: u8,
    l_len: i32,
    r_len: i32,
    best: i32,
    size: i32,
}

impl Default for Seg {
    fn default() -> Self {
        Self {
            l_char: 0,
            r_char: 0,
            l_len: 0,
            r_len: 0,
            best: 0,
            size: 0,
        }
    }
}

impl Solution {
    fn merge(a: Seg, b: Seg) -> Seg {
        if a.size == 0 {
            return b;
        }
        if b.size == 0 {
            return a;
        }
        let mut res = Seg {
            l_char: a.l_char,
            r_char: b.r_char,
            size: a.size + b.size,
            best: a.best.max(b.best),
            l_len: a.l_len,
            r_len: b.r_len,
        };
        if a.r_char == b.l_char {
            let mid = a.r_len + b.l_len;
            res.best = res.best.max(mid);
            if a.l_len == a.size {
                res.l_len = a.size + b.l_len;
            }
            if b.r_len == b.size {
                res.r_len = b.size + a.r_len;
            }
        }
        res
    }

    fn build(tree: &mut [Seg], s: &[u8], idx: usize, l: usize, r: usize) {
        if l == r {
            tree[idx] = Seg {
                l_char: s[l],
                r_char: s[l],
                l_len: 1,
                r_len: 1,
                best: 1,
                size: 1,
            };
            return;
        }
        let mid = (l + r) / 2;
        Self::build(tree, s, idx * 2, l, mid);
        Self::build(tree, s, idx * 2 + 1, mid + 1, r);
        tree[idx] = Self::merge(tree[idx * 2], tree[idx * 2 + 1]);
    }

    fn update(tree: &mut [Seg], s: &mut [u8], idx: usize, l: usize, r: usize, pos: usize, ch: u8) {
        if l == r {
            s[pos] = ch;
            tree[idx] = Seg {
                l_char: ch,
                r_char: ch,
                l_len: 1,
                r_len: 1,
                best: 1,
                size: 1,
            };
            return;
        }
        let mid = (l + r) / 2;
        if pos <= mid {
            Self::update(tree, s, idx * 2, l, mid, pos, ch);
        } else {
            Self::update(tree, s, idx * 2 + 1, mid + 1, r, pos, ch);
        }
        tree[idx] = Self::merge(tree[idx * 2], tree[idx * 2 + 1]);
    }

    pub fn longest_repeating(s: String, query_characters: String, query_indices: Vec<i32>) -> Vec<i32> {
        let mut s = s.into_bytes();
        let n = s.len();
        let mut tree = vec![Seg::default(); 4 * n + 5];
        Self::build(&mut tree, &s, 1, 0, n - 1);
        let qc = query_characters.into_bytes();
        let mut ans = vec![0; query_indices.len()];
        for i in 0..query_indices.len() {
            Self::update(&mut tree, &mut s, 1, 0, n - 1, query_indices[i] as usize, qc[i]);
            ans[i] = tree[1].best;
        }
        ans
    }
}
