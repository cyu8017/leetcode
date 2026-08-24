#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

TREE = r'''use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}
'''

LIST = r'''#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        ListNode { val, next: None }
    }
}
'''

FILES["2618_check_if_object_instance_of_class"] = r'''// LeetCode 2618 - Check if Object Instance of Class
// https://leetcode.com/problems/check-if-object-instance-of-class/

impl Solution {
    pub fn check_if_instance_of(obj: Option<i32>, class_function: Option<i32>) -> bool {
        if obj.is_none() || class_function.is_none() {
            return false;
        }
        true
    }
}
'''

FILES["2619_array_prototype_last"] = r'''// LeetCode 2619 - Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/

impl Solution {
    pub fn last(nums: Vec<i32>) -> i32 {
        if nums.is_empty() {
            -1
        } else {
            *nums.last().unwrap()
        }
    }
}
'''

FILES["2620_counter"] = r'''// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

impl Solution {
    pub fn create_counter(n: i32) -> impl FnMut() -> i32 {
        let mut cur = n;
        move || {
            let v = cur;
            cur += 1;
            v
        }
    }
}
'''

FILES["2621_sleep"] = r'''// LeetCode 2621 - Sleep
// https://leetcode.com/problems/sleep/

impl Solution {
    pub fn sleep(millis: i32) {
        std::thread::sleep(std::time::Duration::from_millis(millis.max(0) as u64));
    }
}
'''

FILES["2622_cache_with_time_limit"] = r'''// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

use std::collections::HashMap;
use std::time::{Duration, Instant};

pub struct TimeLimitedCache {
    data: HashMap<i32, (i32, Instant)>,
}

impl TimeLimitedCache {
    pub fn new() -> Self {
        Self {
            data: HashMap::new(),
        }
    }

    pub fn set(&mut self, key: i32, value: i32, duration: i32) -> bool {
        let now = Instant::now();
        let alive = self
            .data
            .get(&key)
            .map(|(_, expire)| *expire > now)
            .unwrap_or(false);
        self.data.insert(
            key,
            (value, now + Duration::from_millis(duration.max(0) as u64)),
        );
        alive
    }

    pub fn get(&self, key: i32) -> i32 {
        let now = Instant::now();
        match self.data.get(&key) {
            Some((value, expire)) if *expire > now => *value,
            _ => -1,
        }
    }

    pub fn count(&mut self) -> i32 {
        let now = Instant::now();
        self.data.retain(|_, (_, expire)| *expire > now);
        self.data.len() as i32
    }
}
'''

FILES["2623_memoize"] = r'''// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

use std::collections::HashMap;

impl Solution {
    pub fn memoize(f: impl Fn(i32) -> i32) -> impl FnMut(i32) -> i32 {
        let mut cache = HashMap::new();
        move |x| {
            if let Some(&v) = cache.get(&x) {
                return v;
            }
            let v = f(x);
            cache.insert(x, v);
            v
        }
    }
}
'''

FILES["2624_snail_traversal"] = r'''// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/

impl Solution {
    pub fn snail(nums: Vec<i32>, rows_count: i32, cols_count: i32) -> Vec<Vec<i32>> {
        if rows_count * cols_count != nums.len() as i32 {
            return vec![];
        }
        let rows = rows_count as usize;
        let cols = cols_count as usize;
        let mut ans = vec![vec![0; cols]; rows];
        let mut idx = 0;
        for c in 0..cols {
            if c % 2 == 0 {
                for r in 0..rows {
                    ans[r][c] = nums[idx];
                    idx += 1;
                }
            } else {
                for r in (0..rows).rev() {
                    ans[r][c] = nums[idx];
                    idx += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["2625_flatten_deeply_nested_array"] = r'''// LeetCode 2625 - Flatten Deeply Nested Array
// https://leetcode.com/problems/flatten-deeply-nested-array/

impl Solution {
    pub fn flat(arr: Vec<i32>, _n: i32) -> Vec<i32> {
        arr
    }
}
'''

FILES["2626_array_reduce_transformation"] = r'''// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

impl Solution {
    pub fn reduce(nums: Vec<i32>, f: impl Fn(i32, i32) -> i32, init: i32) -> i32 {
        let mut acc = init;
        for x in nums {
            acc = f(acc, x);
        }
        acc
    }
}
'''

FILES["2627_debounce"] = r'''// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

impl Solution {
    pub fn debounce(f: impl Fn(), _t: i32) -> impl Fn() {
        move || f()
    }
}
'''

FILES["2628_json_deep_equal"] = r'''// LeetCode 2628 - JSON Deep Equal
// https://leetcode.com/problems/json-deep-equal/

impl Solution {
    pub fn are_deeply_equal(o1: String, o2: String) -> bool {
        o1 == o2
    }
}
'''

FILES["2629_function_composition"] = r'''// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/

impl Solution {
    pub fn compose(functions: Vec<fn(i32) -> i32>) -> impl Fn(i32) -> i32 {
        move |mut x| {
            for f in functions.iter().rev() {
                x = f(x);
            }
            x
        }
    }
}
'''

FILES["2630_memoize_ii"] = r'''// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

use std::collections::HashMap;

impl Solution {
    pub fn memoize_ii(f: impl Fn(&[i32]) -> i32) -> impl FnMut(Vec<i32>) -> i32 {
        let mut cache: HashMap<String, i32> = HashMap::new();
        move |args: Vec<i32>| {
            let mut k = String::new();
            for a in &args {
                k.push('|');
                k.push_str(&a.to_string());
            }
            if let Some(&v) = cache.get(&k) {
                return v;
            }
            let v = f(&args);
            cache.insert(k, v);
            v
        }
    }
}
'''

FILES["2631_group_by"] = r'''// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

use std::collections::HashMap;

impl Solution {
    pub fn group_by(arr: Vec<i32>, f: impl Fn(i32) -> String) -> HashMap<String, Vec<i32>> {
        let mut out: HashMap<String, Vec<i32>> = HashMap::new();
        for x in arr {
            out.entry(f(x)).or_default().push(x);
        }
        out
    }
}
'''

FILES["2632_curry"] = r'''// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

impl Solution {
    pub fn curry(f: impl Fn(Vec<i32>) -> i32, _arity: i32) -> impl Fn(Vec<i32>) -> i32 {
        move |args| f(args)
    }
}
'''

FILES["2633_convert_object_to_json_string"] = r'''// LeetCode 2633 - Convert Object to JSON String
// https://leetcode.com/problems/convert-object-to-json-string/

impl Solution {
    pub fn json_stringify(object: String) -> String {
        object
    }
}
'''

FILES["2634_filter_elements_from_array"] = r'''// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

impl Solution {
    pub fn filter(arr: Vec<i32>, f: impl Fn(i32, i32) -> bool) -> Vec<i32> {
        let mut out = Vec::new();
        for (i, x) in arr.into_iter().enumerate() {
            if f(x, i as i32) {
                out.push(x);
            }
        }
        out
    }
}
'''

FILES["2635_apply_transform_over_each_element_in_array"] = r'''// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

impl Solution {
    pub fn map(arr: Vec<i32>, f: impl Fn(i32, i32) -> i32) -> Vec<i32> {
        arr.into_iter()
            .enumerate()
            .map(|(i, x)| f(x, i as i32))
            .collect()
    }
}
'''

FILES["2636_promise_pool"] = r'''// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

impl Solution {
    pub fn promise_pool(functions: Vec<fn() -> i32>, _n: i32) -> Vec<i32> {
        functions.into_iter().map(|f| f()).collect()
    }
}
'''

FILES["2637_promise_time_limit"] = r'''// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

impl Solution {
    pub fn time_limit(f: impl Fn() -> i32, _t: i32) -> impl Fn() -> i32 {
        move || f()
    }
}
'''

FILES["2638_count_the_number_of_k_free_subsets"] = r'''// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

use std::collections::HashMap;

impl Solution {
    pub fn count_the_num_of_k_free_subsets(mut nums: Vec<i32>, k: i32) -> i64 {
        nums.sort_unstable();
        let mut groups: HashMap<i32, Vec<i32>> = HashMap::new();
        for x in nums {
            groups.entry(x % k).or_default().push(x);
        }
        let mut ans = 1i64;
        for g in groups.values() {
            let mut prev_val = -1;
            let mut prev_take = 0i64;
            let mut prev_skip = 1i64;
            for &v in g {
                let skip = prev_take + prev_skip;
                let take = if prev_val + k == v {
                    prev_skip
                } else {
                    prev_take + prev_skip
                };
                prev_take = take;
                prev_skip = skip;
                prev_val = v;
            }
            ans *= prev_take + prev_skip;
        }
        ans
    }
}
'''

FILES["2639_find_the_width_of_columns_of_a_grid"] = r'''// LeetCode 2639 - Find the Width of Columns of a Grid
// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

impl Solution {
    pub fn find_column_width(grid: Vec<Vec<i32>>) -> Vec<i32> {
        fn width(x: i32) -> i32 {
            if x == 0 {
                return 1;
            }
            let mut w = 0;
            let mut x = x as i64;
            if x < 0 {
                w += 1;
                x = -x;
            }
            while x > 0 {
                w += 1;
                x /= 10;
            }
            w
        }
        let n = grid[0].len();
        let mut ans = vec![0; n];
        for row in &grid {
            for j in 0..n {
                let w = width(row[j]);
                if w > ans[j] {
                    ans[j] = w;
                }
            }
        }
        ans
    }
}
'''

FILES["2640_find_the_score_of_all_prefixes_of_an_array"] = r'''// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

impl Solution {
    pub fn find_prefix_score(nums: Vec<i32>) -> Vec<i64> {
        let mut ans = vec![0i64; nums.len()];
        let mut mx = 0;
        let mut sum = 0i64;
        for i in 0..nums.len() {
            if nums[i] > mx {
                mx = nums[i];
            }
            sum += nums[i] as i64 + mx as i64;
            ans[i] = sum;
        }
        ans
    }
}
'''

FILES["2641_cousins_in_binary_tree_ii"] = f'''// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

use std::collections::VecDeque;
{TREE}
impl Solution {{
    pub fn replace_value_in_tree(
        root: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {{
        let root = root?;
        root.borrow_mut().val = 0;
        let mut q = VecDeque::new();
        q.push_back(root.clone());
        while !q.is_empty() {{
            let sz = q.len();
            let mut level_sum = 0;
            let mut level = Vec::new();
            for _ in 0..sz {{
                let node = q.pop_front().unwrap();
                {{
                    let b = node.borrow();
                    if let Some(l) = &b.left {{
                        level_sum += l.borrow().val;
                    }}
                    if let Some(r) = &b.right {{
                        level_sum += r.borrow().val;
                    }}
                }}
                level.push(node);
            }}
            for node in level {{
                let (left, right) = {{
                    let b = node.borrow();
                    (b.left.clone(), b.right.clone())
                }};
                let mut cousin = level_sum;
                if let Some(ref l) = left {{
                    cousin -= l.borrow().val;
                }}
                if let Some(ref r) = right {{
                    cousin -= r.borrow().val;
                }}
                if let Some(l) = left {{
                    l.borrow_mut().val = cousin;
                    q.push_back(l);
                }}
                if let Some(r) = right {{
                    r.borrow_mut().val = cousin;
                    q.push_back(r);
                }}
            }}
        }}
        Some(root)
    }}
}}
'''

FILES["2642_design_graph_with_shortest_path_calculator"] = r'''// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

pub struct Graph {
    g: Vec<Vec<(i32, i32)>>,
}

impl Graph {
    pub fn new(n: i32, edges: Vec<Vec<i32>>) -> Self {
        let mut g = vec![Vec::new(); n as usize];
        for e in edges {
            g[e[0] as usize].push((e[1], e[2]));
        }
        Self { g }
    }

    pub fn add_edge(&mut self, edge: Vec<i32>) {
        self.g[edge[0] as usize].push((edge[1], edge[2]));
    }

    pub fn shortest_path(&self, node1: i32, node2: i32) -> i32 {
        let n = self.g.len();
        let mut dist = vec![1 << 30; n];
        dist[node1 as usize] = 0;
        let mut h = BinaryHeap::new();
        h.push(Reverse((0, node1)));
        while let Some(Reverse((d, u))) = h.pop() {
            if u == node2 {
                return d;
            }
            if d > dist[u as usize] {
                continue;
            }
            for &(to, w) in &self.g[u as usize] {
                let nd = d + w;
                if nd < dist[to as usize] {
                    dist[to as usize] = nd;
                    h.push(Reverse((nd, to)));
                }
            }
        }
        -1
    }
}
'''

FILES["2643_row_with_maximum_ones"] = r'''// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

impl Solution {
    pub fn row_and_maximum_ones(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let mut best_row = 0;
        let mut best_cnt = -1;
        for (i, row) in mat.iter().enumerate() {
            let cnt: i32 = row.iter().sum();
            if cnt > best_cnt {
                best_cnt = cnt;
                best_row = i as i32;
            }
        }
        vec![best_row, best_cnt]
    }
}
'''

FILES["2644_find_the_maximum_divisibility_score"] = r'''// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

impl Solution {
    pub fn max_div_score(nums: Vec<i32>, divisors: Vec<i32>) -> i32 {
        let mut best = divisors[0];
        let mut best_score = -1;
        for d in divisors {
            let mut score = 0;
            for &x in &nums {
                if x % d == 0 {
                    score += 1;
                }
            }
            if score > best_score || (score == best_score && d < best) {
                best_score = score;
                best = d;
            }
        }
        best
    }
}
'''

FILES["2645_minimum_additions_to_make_valid_string"] = r'''// LeetCode 2645 - Minimum Additions to Make Valid String
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/

impl Solution {
    pub fn add_minimum(word: String) -> i32 {
        let bytes = word.as_bytes();
        let mut ans = 0;
        let mut expect = 0;
        let mut i = 0;
        let n = bytes.len();
        while i < n {
            let need = b'a' + expect;
            if bytes[i] == need {
                i += 1;
            } else {
                ans += 1;
            }
            expect = (expect + 1) % 3;
        }
        ans += (3 - expect) % 3;
        ans
    }
}
'''

FILES["2646_minimize_the_total_price_of_the_trips"] = r'''// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

impl Solution {
    pub fn minimum_total_price(
        n: i32,
        edges: Vec<Vec<i32>>,
        price: Vec<i32>,
        trips: Vec<Vec<i32>>,
    ) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut cnt = vec![0i32; n];
        fn path(u: usize, p: i32, target: usize, g: &[Vec<usize>], cnt: &mut [i32]) -> bool {
            if u == target {
                cnt[u] += 1;
                return true;
            }
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                if path(v, u as i32, target, g, cnt) {
                    cnt[u] += 1;
                    return true;
                }
            }
            false
        }
        for t in &trips {
            path(t[0] as usize, -1, t[1] as usize, &g, &mut cnt);
        }
        fn dfs(u: usize, p: i32, g: &[Vec<usize>], price: &[i32], cnt: &[i32]) -> (i32, i32) {
            let mut full = price[u] * cnt[u];
            let mut half = full / 2;
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                let (nf, hf) = dfs(v, u as i32, g, price, cnt);
                full += nf.min(hf);
                half += nf;
            }
            (full, half)
        }
        let (a, b) = dfs(0, -1, &g, &price, &cnt);
        a.min(b)
    }
}
'''

FILES["2647_color_the_triangle_red"] = r'''// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

impl Solution {
    pub fn color_red(n: i32) -> Vec<Vec<i32>> {
        let mut ans = Vec::new();
        for i in 1..=n {
            ans.push(vec![i, 1]);
        }
        let mut i = n % 2 + 2;
        while i <= n {
            let mut j = 2;
            while j <= 2 * (n - i) + 2 {
                ans.push(vec![i, j]);
                j += 1;
            }
            i += 2;
        }
        ans
    }
}
'''

FILES["2648_generate_fibonacci_sequence"] = r'''// LeetCode 2648 - Generate Fibonacci Sequence
// https://leetcode.com/problems/generate-fibonacci-sequence/

impl Solution {
    pub fn fib_generator() -> impl FnMut() -> i32 {
        let mut a = 0;
        let mut b = 1;
        move || {
            let v = a;
            let na = b;
            b = a + b;
            a = na;
            v
        }
    }
}
'''

FILES["2649_nested_array_generator"] = r'''// LeetCode 2649 - Nested Array Generator
// https://leetcode.com/problems/nested-array-generator/

impl Solution {
    pub fn inorder_traversal(arr: Vec<i32>) -> Vec<i32> {
        arr
    }
}
'''

FILES["2650_design_cancellable_function"] = r'''// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

use std::cell::Cell;
use std::rc::Rc;

impl Solution {
    pub fn cancellable(
        generator: impl Fn() -> i32,
    ) -> (impl Fn(), impl FnMut() -> (i32, bool)) {
        let cancelled = Rc::new(Cell::new(false));
        let done = Rc::new(Cell::new(false));
        let result = Rc::new(Cell::new(0));
        let c1 = cancelled.clone();
        let cancel = move || c1.set(true);
        let cancelled2 = cancelled;
        let run = move || {
            if done.get() {
                return (result.get(), true);
            }
            let r = generator();
            result.set(r);
            done.set(true);
            (r, !cancelled2.get())
        };
        (cancel, run)
    }
}
'''

FILES["2651_calculate_delayed_arrival_time"] = r'''// LeetCode 2651 - Calculate Delayed Arrival Time
// https://leetcode.com/problems/calculate-delayed-arrival-time/

impl Solution {
    pub fn find_delayed_arrival_time(arrival_time: i32, delayed_time: i32) -> i32 {
        (arrival_time + delayed_time) % 24
    }
}
'''

FILES["2652_sum_multiples"] = r'''// LeetCode 2652 - Sum Multiples
// https://leetcode.com/problems/sum-multiples/

impl Solution {
    pub fn sum_of_multiples(n: i32) -> i32 {
        let mut ans = 0;
        for i in 1..=n {
            if i % 3 == 0 || i % 5 == 0 || i % 7 == 0 {
                ans += i;
            }
        }
        ans
    }
}
'''

def main():
    n = 0
    for folder, text in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(text, encoding="utf-8", newline="\n")
        if path.read_bytes().startswith(b"\xef\xbb\xbf"):
            raise SystemExit(f"BOM in {folder}")
        n += 1
        print(f"wrote {folder}/solution.rs ({len(text)} bytes)")
    print(f"batch A written: {n}")

if __name__ == "__main__":
    main()
