#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3896_minimum_operations_to_transform_array_into_alternating_prime"] = r'''// LeetCode 3896 - Minimum Operations to Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        const MX: usize = 200000;
        let mut is_prime = vec![true; MX + 1];
        is_prime[0] = false;
        is_prime[1] = false;
        let mut i = 2;
        while i * i <= MX {
            if is_prime[i] {
                let mut j = i * i;
                while j <= MX {
                    is_prime[j] = false;
                    j += i;
                }
            }
            i += 1;
        }
        let primes: Vec<i32> = (2..=MX).filter(|&i| is_prime[i]).map(|i| i as i32).collect();
        let mut ans = 0;
        for (i, &x) in nums.iter().enumerate() {
            if i % 2 == 0 {
                let it = primes.partition_point(|&p| p < x);
                ans += primes[it] - x;
            } else if is_prime[x as usize] {
                ans += if x == 2 { 2 } else { 1 };
            }
        }
        ans
    }
}
'''

FILES["3897_maximum_value_of_concatenated_binary_segments"] = r'''// LeetCode 3897 - Maximum Value of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

impl Solution {
    pub fn max_value(nums1: Vec<i32>, nums0: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn group(p: &(i32, i32)) -> i32 {
            if p.1 == 0 {
                0
            } else if p.0 > 0 {
                1
            } else {
                2
            }
        }
        let n = nums1.len();
        let mut pairs: Vec<(i32, i32)> = (0..n).map(|i| (nums1[i], nums0[i])).collect();
        let mut b: i32 = pairs.iter().map(|(a, c)| a + c).sum();
        pairs.sort_by(|a, b| {
            let g1 = group(a);
            let g2 = group(b);
            if g1 != g2 {
                return g1.cmp(&g2);
            }
            if g1 == 0 {
                return b.0.cmp(&a.0);
            }
            if g1 == 1 {
                if a.0 != b.0 {
                    return b.0.cmp(&a.0);
                }
                return a.1.cmp(&b.1);
            }
            a.1.cmp(&b.1)
        });
        let mut p = vec![0i32; b as usize];
        p[0] = 1;
        for i in 1..b as usize {
            p[i] = (2i64 * p[i - 1] as i64 % MOD) as i32;
        }
        let mut ans = 0i32;
        b -= 1;
        for (mut cnt1, cnt0) in pairs {
            while cnt1 > 0 {
                ans = (ans + p[b as usize]) % MOD as i32;
                b -= 1;
                cnt1 -= 1;
            }
            b -= cnt0;
        }
        ans
    }
}
'''

FILES["3898_find_the_degree_of_each_vertex"] = r'''// LeetCode 3898 - Find the Degree of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

impl Solution {
    pub fn find_degrees(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        matrix.iter().map(|row| row.iter().sum()).collect()
    }
}
'''

FILES["3899_angles_of_a_triangle"] = r'''// LeetCode 3899 - Angles of a Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

impl Solution {
    pub fn internal_angles(mut sides: Vec<i32>) -> Vec<f64> {
        sides.sort_unstable();
        let a = sides[0] as f64;
        let b = sides[1] as f64;
        let c = sides[2] as f64;
        if a + b <= c {
            return vec![];
        }
        let pi = std::f64::consts::PI;
        let aa = ((b * b + c * c - a * a) / (2.0 * b * c)).acos() * 180.0 / pi;
        let bb = ((a * a + c * c - b * b) / (2.0 * a * c)).acos() * 180.0 / pi;
        let cc = 180.0 - aa - bb;
        vec![aa, bb, cc]
    }
}
'''

FILES["3900_longest_balanced_substring_after_one_swap"] = r'''// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

use std::collections::HashMap;

impl Solution {
    pub fn longest_balanced(s: String) -> i32 {
        let b = s.as_bytes();
        let cnt0 = b.iter().filter(|&&c| c == b'0').count() as i32;
        let cnt1 = b.len() as i32 - cnt0;
        let mut pos: HashMap<i32, Vec<i32>> = HashMap::new();
        pos.insert(0, vec![-1]);
        let mut ans = 0;
        let mut pre = 0;
        for (i, &c) in b.iter().enumerate() {
            if c == b'1' {
                pre += 1;
            } else {
                pre -= 1;
            }
            pos.entry(pre).or_default().push(i as i32);
            ans = ans.max(i as i32 - pos[&pre][0]);
            if let Some(p) = pos.get(&(pre - 2)) {
                if (i as i32 - p[0] - 2) / 2 < cnt0 {
                    ans = ans.max(i as i32 - p[0]);
                } else if p.len() > 1 {
                    ans = ans.max(i as i32 - p[1]);
                }
            }
            if let Some(p) = pos.get(&(pre + 2)) {
                if (i as i32 - p[0] - 2) / 2 < cnt1 {
                    ans = ans.max(i as i32 - p[0]);
                } else if p.len() > 1 {
                    ans = ans.max(i as i32 - p[1]);
                }
            }
        }
        ans
    }
}
'''

FILES["3901_good_subsequence_queries"] = r'''// LeetCode 3901 - Good Subsequence Queries
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
'''

FILES["3902_zigzag_level_sum_of_binary_tree"] = r'''// LeetCode 3902 - Zigzag Level Sum of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn zigzag_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i64> {
        let Some(root) = root else {
            return Vec::new();
        };
        let mut ans = Vec::new();
        let mut q = vec![root];
        let mut left = true;
        while !q.is_empty() {
            let mut nq = Vec::new();
            for node in &q {
                let b = node.borrow();
                if let Some(l) = b.left.clone() {
                    nq.push(l);
                }
                if let Some(r) = b.right.clone() {
                    nq.push(r);
                }
            }
            let m = q.len();
            let mut s = 0i64;
            for i in 0..m {
                let node = if left { &q[i] } else { &q[m - i - 1] };
                let b = node.borrow();
                let child = if left { b.left.clone() } else { b.right.clone() };
                if child.is_none() {
                    break;
                }
                s += b.val as i64;
            }
            ans.push(s);
            left = !left;
            q = nq;
        }
        ans
    }
}
'''

FILES["3903_smallest_stable_index_i"] = r'''// LeetCode 3903 - Smallest Stable Index I
// https://leetcode.com/problems/smallest-stable-index-i/

impl Solution {
    pub fn first_stable_index(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut right = vec![0; n];
        right[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            right[i] = right[i + 1].min(nums[i]);
        }
        let mut left = 0;
        for i in 0..n {
            left = left.max(nums[i]);
            if left - right[i] <= k {
                return i as i32;
            }
        }
        -1
    }
}
'''

FILES["3904_smallest_stable_index_ii"] = r'''// LeetCode 3904 - Smallest Stable Index II
// https://leetcode.com/problems/smallest-stable-index-ii/

impl Solution {
    pub fn first_stable_index(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut right = vec![0; n];
        right[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            right[i] = right[i + 1].min(nums[i]);
        }
        let mut left = 0;
        for i in 0..n {
            left = left.max(nums[i]);
            if left - right[i] <= k {
                return i as i32;
            }
        }
        -1
    }
}
'''

FILES["3905_multi_source_flood_fill"] = r'''// LeetCode 3905 - Multi-Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

use std::collections::BTreeMap;

impl Solution {
    pub fn color_grid(n: i32, m: i32, sources: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let m = m as usize;
        let mut ans = vec![vec![0; m]; n];
        let mut q = sources;
        let dirs = [-1, 0, 1, 0, -1];
        for s in &q {
            ans[s[0] as usize][s[1] as usize] = s[2];
        }
        while !q.is_empty() {
            let mut vis = BTreeMap::new();
            for curr in &q {
                let r = curr[0];
                let c = curr[1];
                let color = curr[2];
                for i in 0..4 {
                    let x = r + dirs[i];
                    let y = c + dirs[i + 1];
                    if x >= 0 && x < n as i32 && y >= 0 && y < m as i32 && ans[x as usize][y as usize] == 0 {
                        let key = (x, y);
                        let e = vis.entry(key).or_insert(0);
                        if color > *e {
                            *e = color;
                        }
                    }
                }
            }
            q.clear();
            for ((x, y), color) in vis {
                ans[x as usize][y as usize] = color;
                q.push(vec![x, y, color]);
            }
        }
        ans
    }
}
'''

FILES["3906_count_good_integers_on_a_grid_path"] = r'''// LeetCode 3906 - Count Good Integers on a Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

impl Solution {
    pub fn count_good_integers_on_path(l: i64, r: i64, directions: String) -> i64 {
        let mut key = [false; 16];
        let mut row = 0;
        let mut col = 0;
        key[0] = true;
        for c in directions.chars() {
            if c == 'D' {
                row += 1;
            } else {
                col += 1;
            }
            key[row * 4 + col] = true;
        }
        fn dfs(
            pos: usize,
            last: usize,
            lim: bool,
            s: &[u8],
            key: &[bool; 16],
            f: &mut [[i64; 10]; 16],
        ) -> i64 {
            if pos == 16 {
                return 1;
            }
            if !lim && f[pos][last] != -1 {
                return f[pos][last];
            }
            let mut res = 0i64;
            let start = if key[pos] { last } else { 0 };
            let end = if lim { (s[pos] - b'0') as usize } else { 9 };
            for i in start..=end {
                let next_last = if key[pos] { i } else { last };
                res += dfs(pos + 1, next_last, lim && i == end, s, key, f);
            }
            if !lim {
                f[pos][last] = res;
            }
            res
        }
        let calc = |x: i64| -> i64 {
            if x < 0 {
                return 0;
            }
            let t = x.to_string();
            let s = format!("{:0>16}", t);
            let sb = s.into_bytes();
            let mut f = [[-1i64; 10]; 16];
            dfs(0, 0, true, &sb, &key, &mut f)
        };
        calc(r) - calc(l - 1)
    }
}
'''

FILES["3907_count_smaller_elements_with_opposite_parity"] = r'''// LeetCode 3907 - Count Smaller Elements With Opposite Parity
// https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

struct Bit {
    n: usize,
    c: Vec<i32>,
}

impl Bit {
    fn new(n: usize) -> Self {
        Self { n, c: vec![0; n + 1] }
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
    pub fn count_smaller_opposite_parity(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut sorted = nums.clone();
        sorted.sort_unstable();
        sorted.dedup();
        let m = sorted.len();
        let mut bits = [Bit::new(m), Bit::new(m)];
        let mut ans = vec![0; n];
        for i in (0..n).rev() {
            let x = sorted.partition_point(|&v| v < nums[i]) + 1;
            ans[i] = bits[((nums[i] & 1) ^ 1) as usize].query(x - 1);
            bits[(nums[i] & 1) as usize].update(x, 1);
        }
        ans
    }
}
'''

FILES["3908_valid_digit_number"] = r'''// LeetCode 3908 - Valid Digit Number
// https://leetcode.com/problems/valid-digit-number/

impl Solution {
    pub fn valid_digit(mut n: i32, x: i32) -> bool {
        let mut has_x = false;
        while n > 9 {
            has_x = has_x || (n % 10 == x);
            n /= 10;
        }
        has_x && n != x
    }
}
'''

FILES["3909_compare_sums_of_bitonic_parts"] = r'''// LeetCode 3909 - Compare Sums of Bitonic Parts
// https://leetcode.com/problems/compare-sums-of-bitonic-parts/

impl Solution {
    pub fn compare_bitonic_sums(nums: Vec<i32>) -> i32 {
        let mut l = nums[0] as i64;
        let mut r: i64 = nums.iter().map(|&x| x as i64).sum();
        for i in 1..nums.len() {
            if nums[i - 1] > nums[i] {
                break;
            }
            l += nums[i] as i64;
            r -= nums[i - 1] as i64;
        }
        if l == r {
            -1
        } else if l > r {
            0
        } else {
            1
        }
    }
}
'''

FILES["3910_count_connected_subgraphs_with_even_node_sum"] = r'''// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

impl Solution {
    pub fn even_sum_subgraphs(nums: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let m = (1 << n) - 1;
        let mut ans = 0;
        fn dfs(u: usize, vis: &mut i32, g: &[Vec<usize>]) {
            *vis |= 1 << u;
            for &v in &g[u] {
                if ((*vis >> v) & 1) == 0 {
                    dfs(v, vis, g);
                }
            }
        }
        for sub in 1..=m {
            let mut s = 0;
            for i in 0..n {
                if (sub >> i) & 1 == 1 {
                    s += nums[i];
                }
            }
            if s % 2 != 0 {
                continue;
            }
            let mut vis = m ^ sub;
            let start = 31 - (sub as u32).leading_zeros();
            dfs(start as usize, &mut vis, &g);
            if vis == m {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["3911_k_th_smallest_remaining_even_integer_in_subarray_queries"] = r'''// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

impl Solution {
    pub fn kth_smallest_even(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        let n = nums.len();
        let mut even_prefix = vec![0; n + 1];
        for i in 0..n {
            even_prefix[i + 1] = even_prefix[i] + if nums[i] % 2 == 0 { 1 } else { 0 };
        }
        let mut ans = vec![0i64; queries.len()];
        for (qi, q) in queries.iter().enumerate() {
            let l = q[0] as usize;
            let r = q[1] as usize;
            let k = q[2] as i64;
            let mut lo = 1i64;
            let mut hi = k + (r - l + 1) as i64;
            while lo < hi {
                let mid = (lo + hi) / 2;
                let mut pos = nums.partition_point(|&v| v <= (2 * mid) as i32);
                if pos > r + 1 {
                    pos = r + 1;
                }
                let mut removed = 0;
                if pos > l {
                    removed = even_prefix[pos] - even_prefix[l];
                }
                if mid - removed as i64 >= k {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            ans[qi] = 2 * lo;
        }
        ans
    }
}
'''

FILES["3912_valid_elements_in_an_array"] = r'''// LeetCode 3912 - Valid Elements in an Array
// https://leetcode.com/problems/valid-elements-in-an-array/

impl Solution {
    pub fn find_valid_elements(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut right = vec![0; n];
        right[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            right[i] = right[i + 1].max(nums[i]);
        }
        let mut left = 0;
        let mut ans = Vec::new();
        for i in 0..n {
            let x = nums[i];
            if x > left || i == n - 1 || x > right[i + 1] {
                ans.push(x);
            }
            left = left.max(x);
        }
        ans
    }
}
'''

FILES["3913_sort_vowels_by_frequency"] = r'''// LeetCode 3913 - Sort Vowels by Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn sort_vowels(s: String) -> String {
        let st: HashSet<char> = ['a', 'e', 'i', 'o', 'u'].into_iter().collect();
        let mut vowels = Vec::new();
        let mut cnt = HashMap::new();
        for c in s.chars() {
            if !st.contains(&c) {
                continue;
            }
            if !cnt.contains_key(&c) {
                vowels.push(c);
            }
            *cnt.entry(c).or_insert(0) += 1;
        }
        vowels.sort_by(|a, b| cnt[b].cmp(&cnt[a]));
        let mut ans: Vec<char> = s.chars().collect();
        let mut i = 0;
        for k in 0..ans.len() {
            if !st.contains(&ans[k]) {
                continue;
            }
            let ch = vowels[i];
            ans[k] = ch;
            *cnt.get_mut(&ch).unwrap() -= 1;
            if cnt[&ch] == 0 {
                i += 1;
            }
        }
        ans.into_iter().collect()
    }
}
'''

FILES["3914_minimum_operations_to_make_array_non_decreasing"] = r'''// LeetCode 3914 - Minimum Operations to Make Array Non-Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        for i in 1..nums.len() {
            ans += 0.max(nums[i - 1] as i64 - nums[i] as i64);
        }
        ans
    }
}
'''

FILES["3915_maximum_sum_of_alternating_subsequence_with_distance_at_least_k"] = r'''// LeetCode 3915 - Maximum Sum of Alternating Subsequence With Distance at Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

struct Fenwick {
    f: Vec<i64>,
}

impl Fenwick {
    fn new(n: usize) -> Self {
        Self { f: vec![0; n] }
    }
    fn update(&mut self, mut i: usize, val: i64) {
        while i < self.f.len() {
            self.f[i] = self.f[i].max(val);
            i += i & i.wrapping_neg();
        }
    }
    fn pre_max(&self, mut i: usize) -> i64 {
        let mut res = 0i64;
        while i > 0 {
            res = res.max(self.f[i]);
            i &= i - 1;
        }
        res
    }
}

impl Solution {
    pub fn max_alternating_sum(mut nums: Vec<i32>, k: i32) -> i64 {
        let mut sorted = nums.clone();
        sorted.sort_unstable();
        sorted.dedup();
        let n = nums.len();
        let m = sorted.len();
        let mut f_inc = vec![0i64; n];
        let mut f_dec = vec![0i64; n];
        let mut inc = Fenwick::new(m + 1);
        let mut dec = Fenwick::new(m + 1);
        let mut ans = 0i64;
        let k = k as usize;
        for i in 0..n {
            let x = nums[i];
            if i >= k {
                let j = nums[i - k];
                inc.update(m - j as usize, f_inc[i - k]);
                dec.update(j as usize + 1, f_dec[i - k]);
            }
            let j = sorted.partition_point(|&v| v < x);
            nums[i] = j as i32;
            f_inc[i] = dec.pre_max(j) + x as i64;
            f_dec[i] = inc.pre_max(m - 1 - j) + x as i64;
            ans = ans.max(f_inc[i]).max(f_dec[i]);
        }
        ans
    }
}
'''

FILES["3916_number_of_zigzag_arrays_iii"] = r'''// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

impl Solution {
    pub fn zig_zag_arrays(n: i32, l: i32, r: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let points = n + 1;
        let mut values = vec![0i64; points + 1];
        for m in 1..=points {
            let mut up: Vec<i64> = (0..m).map(|v| v as i64).collect();
            let mut down: Vec<i64> = (0..m).map(|v| (m - 1 - v) as i64).collect();
            for _length in 3..=n {
                let mut next_up = vec![0i64; m];
                let mut next_down = vec![0i64; m];
                let mut prefix = 0i64;
                for value in 0..m {
                    next_up[value] = prefix;
                    prefix = (prefix + down[value]) % MOD;
                }
                let mut suffix = 0i64;
                for value in (0..m).rev() {
                    next_down[value] = suffix;
                    suffix = (suffix + up[value]) % MOD;
                }
                up = next_up;
                down = next_down;
            }
            for value in 0..m {
                values[m] = (values[m] + up[value] + down[value]) % MOD;
            }
        }
        let x = (r as i64 - l as i64 + 1).rem_euclid(MOD);
        if r - l + 1 <= points as i32 {
            return values[(r - l + 1) as usize] as i32;
        }
        let mut prefix = vec![0i64; points + 2];
        let mut suffix = vec![0i64; points + 2];
        prefix[0] = 1;
        for i in 1..=points {
            prefix[i] = prefix[i - 1] * ((x - i as i64 + MOD) % MOD) % MOD;
        }
        suffix[points + 1] = 1;
        for i in (1..=points).rev() {
            suffix[i] = suffix[i + 1] * ((x - i as i64 + MOD) % MOD) % MOD;
        }
        let mut factorial = vec![0i64; points + 1];
        factorial[0] = 1;
        for i in 1..=points {
            factorial[i] = factorial[i - 1] * i as i64 % MOD;
        }
        fn powm(mut a: i64, mut e: i64, m: i64) -> i64 {
            let mut res = 1;
            while e > 0 {
                if e & 1 == 1 {
                    res = res * a % m;
                }
                a = a * a % m;
                e >>= 1;
            }
            res
        }
        let mut answer = 0i64;
        for i in 1..=points {
            let numerator = prefix[i - 1] * suffix[i + 1] % MOD;
            let denominator = factorial[i - 1] * factorial[points - i] % MOD;
            let term = values[i] * numerator % MOD * powm(denominator, MOD - 2, MOD) % MOD;
            if (points - i) % 2 == 1 {
                answer -= term;
            } else {
                answer += term;
            }
            answer %= MOD;
        }
        if answer < 0 {
            answer += MOD;
        }
        answer as i32
    }
}
'''

FILES["3917_count_indices_with_opposite_parity"] = r'''// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

impl Solution {
    pub fn count_opposite_parity(nums: Vec<i32>) -> Vec<i32> {
        let mut cnt = [0, 0];
        for &x in &nums {
            cnt[(x & 1) as usize] += 1;
        }
        let n = nums.len();
        let mut ans = vec![0; n];
        for i in 0..n {
            let x = nums[i];
            cnt[(x & 1) as usize] -= 1;
            ans[i] = cnt[((x & 1) ^ 1) as usize];
        }
        ans
    }
}
'''

FILES["3918_sum_of_primes_between_number_and_its_reverse"] = r'''// LeetCode 3918 - Sum of Primes Between Number and Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

impl Solution {
    pub fn sum_of_primes_in_range(n: i32) -> i32 {
        let mut is_prime = [true; 1001];
        is_prime[0] = false;
        is_prime[1] = false;
        let mut i = 2;
        while i * i <= 1000 {
            if is_prime[i] {
                let mut j = i * i;
                while j <= 1000 {
                    is_prime[j] = false;
                    j += i;
                }
            }
            i += 1;
        }
        let mut r = 0;
        let mut x = n;
        while x > 0 {
            r = r * 10 + x % 10;
            x /= 10;
        }
        let low = n.min(r);
        let high = n.max(r);
        let mut ans = 0;
        for x in low..=high {
            if is_prime[x as usize] {
                ans += x;
            }
        }
        ans
    }
}
'''

FILES["3919_minimum_cost_to_move_between_indices"] = r'''// LeetCode 3919 - Minimum Cost to Move Between Indices
// https://leetcode.com/problems/minimum-cost-to-move-between-indices/

impl Solution {
    pub fn min_cost(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        let mut s1 = vec![0; n];
        let mut s2 = vec![0; n];
        for i in 1..n {
            let mut c1 = 1;
            if i > 1 && nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1] {
                c1 = nums[i] - nums[i - 1];
            }
            let mut c2 = 1;
            if i < n - 1 && nums[i] - nums[i - 1] > nums[i + 1] - nums[i] {
                c2 = nums[i] - nums[i - 1];
            }
            s1[i] = s1[i - 1] + c1;
            s2[i] = s2[i - 1] + c2;
        }
        queries
            .iter()
            .map(|q| {
                let l = q[0] as usize;
                let r = q[1] as usize;
                if l < r {
                    s1[r] - s1[l]
                } else {
                    s2[l] - s2[r]
                }
            })
            .collect()
    }
}
'''

FILES["3920_maximize_fixed_points_after_deletions"] = r'''// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

impl Solution {
    pub fn max_fixed_points(nums: Vec<i32>) -> i32 {
        let mut tails = Vec::new();
        for (i, &v) in nums.iter().enumerate() {
            if (i as i32) < v {
                continue;
            }
            let d = i as i32 - v;
            match tails.binary_search(&d) {
                Ok(_) => {}
                Err(pos) => {
                    if pos == tails.len() {
                        tails.push(d);
                    } else {
                        tails[pos] = d;
                    }
                }
            }
        }
        tails.len() as i32
    }
}
'''

def main():
    n = 0
    for folder, src in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(src, encoding="utf-8", newline="\n")
        n += 1
        print("wrote", folder)
    print("total", n)

if __name__ == "__main__":
    main()
