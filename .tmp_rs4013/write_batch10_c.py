#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["2689_extract_kth_character_from_the_rope_tree"] = r'''// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

use std::cell::RefCell;
use std::rc::Rc;

pub struct RopeTreeNode {
    pub len: i32,
    pub val: char,
    pub left: Option<Rc<RefCell<RopeTreeNode>>>,
    pub right: Option<Rc<RefCell<RopeTreeNode>>>,
}

impl Solution {
    pub fn get_kth_character(root: Option<Rc<RefCell<RopeTreeNode>>>, k: i32) -> char {
        fn dfs(node: &Rc<RefCell<RopeTreeNode>>, kk: i32) -> char {
            let n = node.borrow();
            if n.left.is_none() && n.right.is_none() {
                return n.val;
            }
            let left_len = if let Some(ref left) = n.left {
                let llen = left.borrow().len;
                if llen > 0 {
                    llen
                } else {
                    1
                }
            } else {
                0
            };
            if kk <= left_len {
                dfs(n.left.as_ref().unwrap(), kk)
            } else {
                dfs(n.right.as_ref().unwrap(), kk - left_len)
            }
        }
        dfs(root.as_ref().unwrap(), k)
    }
}
'''

FILES["2690_infinite_method_object"] = r'''// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

impl Solution {
    pub fn create_infinite_object() -> impl Fn(String) -> String {
        |_| "Hello World".to_string()
    }
}
'''

FILES["2691_immutability_helper"] = r'''// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/

use std::collections::BTreeMap;

impl Solution {
    pub fn immutable_helper(
        obj: BTreeMap<String, i32>,
        mutators: Vec<Box<dyn Fn(&mut BTreeMap<String, i32>)>>,
    ) -> Vec<BTreeMap<String, i32>> {
        let mut out = Vec::new();
        for m in mutators {
            let mut copy = obj.clone();
            m(&mut copy);
            out.push(copy);
        }
        out
    }
}
'''

FILES["2692_make_object_immutable"] = r'''// LeetCode 2692 - Make Object Immutable
// https://leetcode.com/problems/make-object-immutable/

use std::collections::BTreeMap;

impl Solution {
    pub fn make_immutable(obj: BTreeMap<String, i32>) -> BTreeMap<String, i32> {
        obj
    }
}
'''

FILES["2693_call_function_with_custom_context"] = r'''// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

impl Solution {
    pub fn call(f: impl Fn(i32, i32) -> i32, ctx: i32, arg: i32) -> i32 {
        f(ctx, arg)
    }
}
'''

FILES["2694_event_emitter"] = r'''// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

pub struct EventEmitter {
    handlers: Rc<RefCell<HashMap<String, Vec<Option<Box<dyn Fn(&Vec<i32>)>>>>>>,
}

impl EventEmitter {
    pub fn new() -> Self {
        Self {
            handlers: Rc::new(RefCell::new(HashMap::new())),
        }
    }

    pub fn subscribe(
        &self,
        event_name: String,
        callback: Box<dyn Fn(&Vec<i32>)>,
    ) -> impl Fn() {
        let mut h = self.handlers.borrow_mut();
        let v = h.entry(event_name.clone()).or_default();
        v.push(Some(callback));
        let idx = v.len() - 1;
        let handlers = self.handlers.clone();
        move || {
            if let Some(list) = handlers.borrow_mut().get_mut(&event_name) {
                if idx < list.len() {
                    list[idx] = None;
                }
            }
        }
    }

    pub fn emit(&self, event_name: String, args: Vec<i32>) -> Vec<i32> {
        let h = self.handlers.borrow();
        let mut res = Vec::new();
        if let Some(list) = h.get(&event_name) {
            for cb in list.iter().flatten() {
                cb(&args);
                res.push(0);
            }
        }
        res
    }
}

impl Solution {
    pub fn create_emitter() -> EventEmitter {
        EventEmitter::new()
    }
}
'''

FILES["2695_array_wrapper"] = r'''// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

pub struct ArrayWrapper {
    nums: Vec<i32>,
}

impl ArrayWrapper {
    pub fn new(nums: Vec<i32>) -> Self {
        Self { nums }
    }

    pub fn value_of(&self) -> i32 {
        self.nums.iter().sum()
    }

    pub fn to_string(&self) -> String {
        let mut s = String::from("[");
        for (i, x) in self.nums.iter().enumerate() {
            if i > 0 {
                s.push(',');
            }
            s.push_str(&x.to_string());
        }
        s.push(']');
        s
    }
}

impl Solution {
    pub fn array_wrapper_create(nums: Vec<i32>) -> ArrayWrapper {
        ArrayWrapper::new(nums)
    }
}
'''

FILES["2696_minimum_string_length_after_removing_substrings"] = r'''// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

impl Solution {
    pub fn min_length(s: String) -> i32 {
        let mut st = String::new();
        for c in s.chars() {
            if let Some(last) = st.chars().last() {
                if (last == 'A' && c == 'B') || (last == 'C' && c == 'D') {
                    st.pop();
                    continue;
                }
            }
            st.push(c);
        }
        st.len() as i32
    }
}
'''

FILES["2697_lexicographically_smallest_palindrome"] = r'''// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

impl Solution {
    pub fn make_smallest_palindrome(s: String) -> String {
        let mut b = s.into_bytes();
        let n = b.len();
        for i in 0..n / 2 {
            let c = b[i].min(b[n - 1 - i]);
            b[i] = c;
            b[n - 1 - i] = c;
        }
        String::from_utf8(b).unwrap()
    }
}
'''

FILES["2698_find_the_punishment_number_of_an_integer"] = r'''// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

impl Solution {
    pub fn punishment_number(n: i32) -> i32 {
        fn can(sq: i32, target: i32) -> bool {
            let s = sq.to_string();
            let bytes = s.as_bytes();
            fn dfs(bytes: &[u8], i: usize, sum: i32, target: i32) -> bool {
                if i == bytes.len() {
                    return sum == target;
                }
                let mut cur = 0;
                for j in i..bytes.len() {
                    cur = cur * 10 + (bytes[j] - b'0') as i32;
                    if sum + cur > target {
                        break;
                    }
                    if dfs(bytes, j + 1, sum + cur, target) {
                        return true;
                    }
                }
                false
            }
            dfs(bytes, 0, 0, target)
        }
        let mut ans = 0;
        for i in 1..=n {
            let sq = i * i;
            if can(sq, i) {
                ans += sq;
            }
        }
        ans
    }
}
'''

FILES["2699_modify_graph_edge_weights"] = r'''// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn modified_graph_edges(
        n: i32,
        mut edges: Vec<Vec<i32>>,
        source: i32,
        destination: i32,
        target: i32,
    ) -> Vec<Vec<i32>> {
        const INF: i32 = 2_000_000_000;
        let n = n as usize;
        let dijkstra = |edges: &[Vec<i32>], ignore_neg: bool| -> Vec<i32> {
            let mut dist = vec![INF; n];
            dist[source as usize] = 0;
            let mut pq = BinaryHeap::new();
            pq.push(Reverse((0, source)));
            while let Some(Reverse((d, u))) = pq.pop() {
                if d != dist[u as usize] {
                    continue;
                }
                for e in edges {
                    let a = e[0];
                    let b = e[1];
                    let mut w = e[2];
                    if a != u && b != u {
                        continue;
                    }
                    let to = if a == u { b } else { a };
                    if w == -1 {
                        if ignore_neg {
                            continue;
                        }
                        w = 1;
                    }
                    if d + w < dist[to as usize] {
                        dist[to as usize] = d + w;
                        pq.push(Reverse((dist[to as usize], to)));
                    }
                }
            }
            dist
        };
        let mut d = dijkstra(&edges, true);
        if d[destination as usize] < target {
            return vec![];
        }
        let mut matched = d[destination as usize] == target;
        for i in 0..edges.len() {
            if edges[i][2] != -1 {
                continue;
            }
            if matched {
                edges[i][2] = INF;
                continue;
            }
            edges[i][2] = 1;
            d = dijkstra(&edges, false);
            if d[destination as usize] <= target {
                edges[i][2] += target - d[destination as usize];
                matched = true;
            }
        }
        d = dijkstra(&edges, false);
        if d[destination as usize] != target {
            return vec![];
        }
        edges
    }
}
'''

FILES["2700_differences_between_two_objects"] = r'''// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/

use std::collections::BTreeMap;

impl Solution {
    pub fn obj_diff(
        obj1: BTreeMap<String, i32>,
        obj2: BTreeMap<String, i32>,
    ) -> BTreeMap<String, Vec<i32>> {
        let mut diff = BTreeMap::new();
        for (k, v) in &obj1 {
            if let Some(&v2) = obj2.get(k) {
                if v2 != *v {
                    diff.insert(k.clone(), vec![*v, v2]);
                }
            }
        }
        diff
    }
}
'''

FILES["2702_minimum_operations_to_make_numbers_non_positive"] = r'''// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32, y: i32) -> i32 {
        let ok = |ops: i32| -> bool {
            let mut extra = 0i64;
            for &v in &nums {
                let remain = v as i64 - ops as i64 * y as i64;
                if remain > 0 {
                    extra += (remain + (x - y) as i64 - 1) / (x - y) as i64;
                }
            }
            extra <= ops as i64
        };
        let mut lo = 0;
        let mut hi = 0;
        for &v in &nums {
            hi = hi.max((v + y - 1) / y);
            hi = hi.max((v + x - 1) / x);
        }
        hi += nums.len() as i32;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
'''

FILES["2703_return_length_of_arguments_passed"] = r'''// LeetCode 2703 - Return Length of Arguments Passed
// https://leetcode.com/problems/return-length-of-arguments-passed/

impl Solution {
    pub fn arguments_length(args: Vec<i32>) -> i32 {
        args.len() as i32
    }
}
'''

FILES["2704_to_be_or_not_to_be"] = r'''// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

pub struct Expect {
    val: i32,
}

impl Expect {
    pub fn new(val: i32) -> Self {
        Self { val }
    }

    pub fn to_be(&self, other: i32) -> Result<bool, &'static str> {
        if self.val == other {
            Ok(true)
        } else {
            Err("Not Equal")
        }
    }

    pub fn not_to_be(&self, other: i32) -> Result<bool, &'static str> {
        if self.val != other {
            Ok(true)
        } else {
            Err("Equal")
        }
    }
}

impl Solution {
    pub fn expect(val: i32) -> Expect {
        Expect::new(val)
    }
}
'''

FILES["2705_compact_object"] = r'''// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/

impl Solution {
    pub fn compact_object(obj: Vec<i32>) -> Vec<i32> {
        obj.into_iter().filter(|&x| x != 0).collect()
    }
}
'''

FILES["2706_buy_two_chocolates"] = r'''// LeetCode 2706 - Buy Two Chocolates
// https://leetcode.com/problems/buy-two-chocolates/

impl Solution {
    pub fn buy_choco(mut prices: Vec<i32>, money: i32) -> i32 {
        prices.sort_unstable();
        let cost = prices[0] + prices[1];
        if cost <= money {
            money - cost
        } else {
            money
        }
    }
}
'''

FILES["2707_extra_characters_in_a_string"] = r'''// LeetCode 2707 - Extra Characters in a String
// https://leetcode.com/problems/extra-characters-in-a-string/

use std::collections::HashSet;

impl Solution {
    pub fn min_extra_char(s: String, dictionary: Vec<String>) -> i32 {
        let dict: HashSet<String> = dictionary.into_iter().collect();
        let n = s.len();
        let mut dp = vec![n as i32; n + 1];
        dp[0] = 0;
        for i in 0..n {
            dp[i + 1] = dp[i + 1].min(dp[i] + 1);
            for j in i + 1..=n {
                if dict.contains(&s[i..j]) {
                    dp[j] = dp[j].min(dp[i]);
                }
            }
        }
        dp[n]
    }
}
'''

FILES["2708_maximum_strength_of_a_group"] = r'''// LeetCode 2708 - Maximum Strength of a Group
// https://leetcode.com/problems/maximum-strength-of-a-group/

impl Solution {
    pub fn max_strength(mut nums: Vec<i32>) -> i64 {
        nums.sort_unstable();
        let n = nums.len();
        if n == 1 {
            return nums[0] as i64;
        }
        let mut prod = 1i64;
        let mut used = false;
        let mut i = 0;
        while i + 1 < n && nums[i] < 0 && nums[i + 1] < 0 {
            prod *= nums[i] as i64 * nums[i + 1] as i64;
            used = true;
            i += 2;
        }
        let neg_left = i < n && nums[i] < 0;
        while i < n {
            if nums[i] > 0 {
                prod *= nums[i] as i64;
                used = true;
            }
            i += 1;
        }
        if !used {
            if neg_left {
                if nums.iter().any(|&x| x == 0) {
                    return 0;
                }
                return nums[n - 1] as i64;
            }
            return 0;
        }
        prod
    }
}
'''

FILES["2709_greatest_common_divisor_traversal"] = r'''// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

impl Solution {
    pub fn can_traverse_all_pairs(nums: Vec<i32>) -> bool {
        let n = nums.len();
        if n == 1 {
            return true;
        }
        let mx = *nums.iter().max().unwrap() as usize;
        let mut parent: Vec<usize> = (0..=mx).collect();
        fn find(parent: &mut [usize], mut x: usize) -> usize {
            while parent[x] != x {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }
        let unite = |parent: &mut [usize], a: usize, b: usize| {
            let ra = find(parent, a);
            let rb = find(parent, b);
            if ra != rb {
                parent[ra] = rb;
            }
        };
        let mut has = vec![false; mx + 1];
        for &x in &nums {
            if x == 1 {
                return false;
            }
            has[x as usize] = true;
        }
        let mut sieve = vec![0usize; mx + 1];
        for i in 2..=mx {
            if sieve[i] == 0 {
                let mut j = i;
                while j <= mx {
                    if sieve[j] == 0 {
                        sieve[j] = i;
                    }
                    if has[j] {
                        unite(&mut parent, i, j);
                    }
                    j += i;
                }
            }
        }
        let root = find(&mut parent, nums[0] as usize);
        for &x in &nums {
            if find(&mut parent, x as usize) != root {
                return false;
            }
        }
        true
    }
}
'''

FILES["2710_remove_trailing_zeros_from_a_string"] = r'''// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

impl Solution {
    pub fn remove_trailing_zeros(mut num: String) -> String {
        while num.ends_with('0') {
            num.pop();
        }
        num
    }
}
'''

FILES["2711_difference_of_number_of_distinct_values_on_diagonals"] = r'''// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

use std::collections::HashSet;

impl Solution {
    pub fn difference_of_distinct_values(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut ans = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                let mut top = HashSet::new();
                let mut bot = HashSet::new();
                let mut r = i as i32 - 1;
                let mut c = j as i32 - 1;
                while r >= 0 && c >= 0 {
                    top.insert(grid[r as usize][c as usize]);
                    r -= 1;
                    c -= 1;
                }
                r = i as i32 + 1;
                c = j as i32 + 1;
                while r < m as i32 && c < n as i32 {
                    bot.insert(grid[r as usize][c as usize]);
                    r += 1;
                    c += 1;
                }
                ans[i][j] = (top.len() as i32 - bot.len() as i32).abs();
            }
        }
        ans
    }
}
'''

FILES["2712_minimum_cost_to_make_all_characters_equal"] = r'''// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

impl Solution {
    pub fn minimum_cost(s: String) -> i64 {
        let n = s.len();
        let b = s.as_bytes();
        let mut ans = 0i64;
        for i in 1..n {
            if b[i] != b[i - 1] {
                ans += (i as i64).min((n - i) as i64);
            }
        }
        ans
    }
}
'''

FILES["2713_maximum_strictly_increasing_cells_in_a_matrix"] = r'''// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

impl Solution {
    pub fn max_increasing_cells(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let mut cells = Vec::with_capacity(m * n);
        for i in 0..m {
            for j in 0..n {
                cells.push((mat[i][j], i, j));
            }
        }
        cells.sort_unstable_by_key(|&(v, _, _)| v);
        let mut row_max = vec![0; m];
        let mut col_max = vec![0; n];
        let mut dp = vec![vec![0; n]; m];
        let mut ans = 0;
        let mut i = 0;
        while i < cells.len() {
            let mut j = i;
            while j < cells.len() && cells[j].0 == cells[i].0 {
                j += 1;
            }
            let mut buf = Vec::new();
            for k in i..j {
                let r = cells[k].1;
                let c = cells[k].2;
                let best = row_max[r].max(col_max[c]);
                dp[r][c] = best + 1;
                ans = ans.max(dp[r][c]);
                buf.push((r, c, dp[r][c]));
            }
            for (r, c, val) in buf {
                row_max[r] = row_max[r].max(val);
                col_max[c] = col_max[c].max(val);
            }
            i = j;
        }
        ans
    }
}
'''

FILES["2714_find_shortest_path_with_k_hops"] = r'''// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn shortest_path_with_hops(
        n: i32,
        edges: Vec<Vec<i32>>,
        s: i32,
        d: i32,
        k: i32,
    ) -> i32 {
        let n = n as usize;
        let k = k as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
            g[e[1] as usize].push((e[0] as usize, e[2]));
        }
        let mut dist = vec![vec![i32::MAX / 4; k + 1]; n];
        dist[s as usize][0] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0, s as usize, 0usize)));
        while let Some(Reverse((cd, u, hops))) = pq.pop() {
            if u == d as usize {
                return cd;
            }
            if cd > dist[u][hops] {
                continue;
            }
            for &(to, w) in &g[u] {
                if cd + w < dist[to][hops] {
                    dist[to][hops] = cd + w;
                    pq.push(Reverse((dist[to][hops], to, hops)));
                }
                if hops < k && cd < dist[to][hops + 1] {
                    dist[to][hops + 1] = cd;
                    pq.push(Reverse((cd, to, hops + 1)));
                }
            }
        }
        -1
    }
}
'''

FILES["2715_timeout_cancellation"] = r'''// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

use std::cell::Cell;
use std::rc::Rc;

impl Solution {
    pub fn cancellable(
        f: impl Fn() -> i32,
        _t: i32,
    ) -> (impl Fn(), impl Fn() -> Option<i32>) {
        let cancelled = Rc::new(Cell::new(false));
        let c1 = cancelled.clone();
        let cancel = move || c1.set(true);
        let result = move || {
            if cancelled.get() {
                None
            } else {
                Some(f())
            }
        };
        (cancel, result)
    }
}
'''

FILES["2716_minimize_string_length"] = r'''// LeetCode 2716 - Minimize String Length
// https://leetcode.com/problems/minimize-string-length/

use std::collections::HashSet;

impl Solution {
    pub fn minimized_string_length(s: String) -> i32 {
        s.chars().collect::<HashSet<_>>().len() as i32
    }
}
'''

FILES["2717_semi_ordered_permutation"] = r'''// LeetCode 2717 - Semi-Ordered Permutation
// https://leetcode.com/problems/semi-ordered-permutation/

impl Solution {
    pub fn semi_ordered_permutation(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut p1 = 0;
        let mut pn = 0;
        for i in 0..n {
            if nums[i] == 1 {
                p1 = i;
            }
            if nums[i] == n as i32 {
                pn = i;
            }
        }
        let mut ans = p1 as i32 + (n as i32 - 1 - pn as i32);
        if p1 > pn {
            ans -= 1;
        }
        ans
    }
}
'''

FILES["2718_sum_of_matrix_after_queries"] = r'''// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/

impl Solution {
    pub fn matrix_sum_queries(n: i32, queries: Vec<Vec<i32>>) -> i64 {
        let n = n as usize;
        let mut row_done = vec![false; n];
        let mut col_done = vec![false; n];
        let mut rows_left = n as i64;
        let mut cols_left = n as i64;
        let mut ans = 0i64;
        for q in queries.iter().rev() {
            let typ = q[0];
            let idx = q[1] as usize;
            let val = q[2] as i64;
            if typ == 0 {
                if !row_done[idx] {
                    ans += val * cols_left;
                    row_done[idx] = true;
                    rows_left -= 1;
                }
            } else if !col_done[idx] {
                ans += val * rows_left;
                col_done[idx] = true;
                cols_left -= 1;
            }
        }
        ans
    }
}
'''

FILES["2719_count_of_integers"] = r'''// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

use std::collections::HashMap;

impl Solution {
    pub fn count(num1: String, num2: String, min_sum: i32, max_sum: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        fn dec(mut s: String) -> String {
            let mut b = s.into_bytes();
            let mut i = b.len() as i32 - 1;
            while i >= 0 && b[i as usize] == b'0' {
                b[i as usize] = b'9';
                i -= 1;
            }
            if i >= 0 {
                b[i as usize] -= 1;
            }
            let mut j = 0;
            while j + 1 < b.len() && b[j] == b'0' {
                j += 1;
            }
            String::from_utf8(b[j..].to_vec()).unwrap()
        }
        fn dp(s: &str, min_sum: i32, max_sum: i32) -> i32 {
            const MOD: i32 = 1_000_000_007;
            let bytes = s.as_bytes();
            let n = bytes.len();
            let mut memo: HashMap<(i32, i32, i32), i32> = HashMap::new();
            fn dfs(
                pos: usize,
                sum: i32,
                tight: bool,
                bytes: &[u8],
                n: usize,
                min_sum: i32,
                max_sum: i32,
                memo: &mut HashMap<(i32, i32, i32), i32>,
            ) -> i32 {
                if sum > max_sum {
                    return 0;
                }
                if pos == n {
                    return if sum >= min_sum { 1 } else { 0 };
                }
                let key = (pos as i32, sum, if tight { 1 } else { 0 });
                if let Some(&v) = memo.get(&key) {
                    return v;
                }
                let up = if tight { (bytes[pos] - b'0') as i32 } else { 9 };
                let mut res = 0;
                for d in 0..=up {
                    res = (res
                        + dfs(
                            pos + 1,
                            sum + d,
                            tight && d == up,
                            bytes,
                            n,
                            min_sum,
                            max_sum,
                            memo,
                        ))
                        % MOD;
                }
                memo.insert(key, res);
                res
            }
            dfs(0, 0, true, bytes, n, min_sum, max_sum, &mut memo)
        }
        let a = dp(&dec(num1), min_sum, max_sum);
        let b = dp(&num2, min_sum, max_sum);
        (b - a + MOD) % MOD
    }
}
'''

FILES["2721_execute_asynchronous_functions_in_parallel"] = r'''// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

impl Solution {
    pub fn promise_all(functions: Vec<fn() -> i32>) -> Vec<i32> {
        functions.into_iter().map(|f| f()).collect()
    }
}
'''

FILES["2722_join_two_arrays_by_id"] = r'''// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/

use std::collections::BTreeMap;

impl Solution {
    pub fn join(
        arr1: Vec<BTreeMap<String, i32>>,
        arr2: Vec<BTreeMap<String, i32>>,
    ) -> Vec<BTreeMap<String, i32>> {
        let mut by_id: BTreeMap<i32, BTreeMap<String, i32>> = BTreeMap::new();
        let merge = |arr: Vec<BTreeMap<String, i32>>,
                     by_id: &mut BTreeMap<i32, BTreeMap<String, i32>>| {
            for obj in arr {
                let id = *obj.get("id").unwrap();
                let dest = by_id.entry(id).or_default();
                for (k, v) in obj {
                    dest.insert(k, v);
                }
            }
        };
        merge(arr1, &mut by_id);
        merge(arr2, &mut by_id);
        by_id.into_values().collect()
    }
}
'''

FILES["2723_add_two_promises"] = r'''// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

impl Solution {
    pub fn add_two_promises(promise1: impl Fn() -> i32, promise2: impl Fn() -> i32) -> i32 {
        promise1() + promise2()
    }
}
'''

FILES["2724_sort_by"] = r'''// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

impl Solution {
    pub fn sort_by(arr: Vec<i32>, f: impl Fn(i32) -> f64) -> Vec<i32> {
        let mut out = arr;
        out.sort_by(|a, b| f(*a).partial_cmp(&f(*b)).unwrap());
        out
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
    print(f"batch C written: {n}")

if __name__ == "__main__":
    main()
