#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3820_pythagorean_distance_nodes_in_a_tree"] = r'''// LeetCode 3820 - Pythagorean Distance Nodes in a Tree
// https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

use std::collections::VecDeque;

impl Solution {
    pub fn special_nodes(n: i32, edges: Vec<Vec<i32>>, x: i32, y: i32, z: i32) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            g[a].push(b);
            g[b].push(a);
        }
        let bfs = |start: i32| {
            let mut dist = vec![1_000_000_000; n];
            let mut q = VecDeque::new();
            dist[start as usize] = 0;
            q.push_back(start as usize);
            while let Some(u) = q.pop_front() {
                for &v in &g[u] {
                    if dist[v] > dist[u] + 1 {
                        dist[v] = dist[u] + 1;
                        q.push_back(v);
                    }
                }
            }
            dist
        };
        let d1 = bfs(x);
        let d2 = bfs(y);
        let d3 = bfs(z);
        let mut ans = 0;
        for i in 0..n {
            let mut a = [d1[i], d2[i], d3[i]];
            a.sort_unstable();
            let x0 = a[0] as i64;
            let x1 = a[1] as i64;
            let x2 = a[2] as i64;
            if x0 * x0 + x1 * x1 == x2 * x2 {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["3821_find_nth_smallest_integer_with_k_one_bits"] = r'''// LeetCode 3821 - Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/

impl Solution {
    pub fn nth_smallest(n: i64, k: i32) -> i64 {
        const MX: usize = 50;
        let mut c = [[0i64; MX + 1]; MX];
        for i in 0..MX {
            c[i][0] = 1;
            for j in 1..=i {
                c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
            }
        }
        let mut n = n;
        let mut k = k as usize;
        let mut ans = 0i64;
        for i in (0..50).rev() {
            if n > c[i][k] {
                n -= c[i][k];
                ans |= 1i64 << i;
                k -= 1;
                if k == 0 {
                    break;
                }
            }
        }
        ans
    }
}
'''

FILES["3822_design_order_management_system"] = r'''// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design-order-management-system/

use std::collections::HashMap;

pub struct OrderManagementSystem {
    order_type_map: HashMap<i32, String>,
    price_map: HashMap<i32, i32>,
    t: HashMap<(String, i32), Vec<i32>>,
}

impl OrderManagementSystem {
    pub fn new() -> Self {
        Self {
            order_type_map: HashMap::new(),
            price_map: HashMap::new(),
            t: HashMap::new(),
        }
    }

    pub fn add_order(&mut self, order_id: i32, order_type: String, price: i32) {
        self.order_type_map.insert(order_id, order_type.clone());
        self.price_map.insert(order_id, price);
        self.t.entry((order_type, price)).or_default().push(order_id);
    }

    pub fn modify_order(&mut self, order_id: i32, new_price: i32) {
        let order_type = self.order_type_map[&order_id].clone();
        let old_price = self.price_map[&order_id];
        self.price_map.insert(order_id, new_price);
        if let Some(old_list) = self.t.get_mut(&(order_type.clone(), old_price)) {
            if let Some(i) = old_list.iter().position(|&id| id == order_id) {
                old_list.remove(i);
            }
        }
        self.t
            .entry((order_type, new_price))
            .or_default()
            .push(order_id);
    }

    pub fn cancel_order(&mut self, order_id: i32) {
        let order_type = self.order_type_map.remove(&order_id).unwrap();
        let price = self.price_map.remove(&order_id).unwrap();
        if let Some(list) = self.t.get_mut(&(order_type, price)) {
            if let Some(i) = list.iter().position(|&id| id == order_id) {
                list.remove(i);
            }
        }
    }

    pub fn get_orders_at_price(&self, order_type: String, price: i32) -> Vec<i32> {
        self.t.get(&(order_type, price)).cloned().unwrap_or_default()
    }
}
'''

FILES["3823_reverse_letters_then_special_characters_in_a_string"] = r'''// LeetCode 3823 - Reverse Letters Then Special Characters in a String
// https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

impl Solution {
    pub fn reverse_by_type(s: String) -> String {
        let mut bytes = s.into_bytes();
        let mut a = Vec::new();
        let mut b = Vec::new();
        for &c in &bytes {
            if c.is_ascii_alphabetic() {
                a.push(c);
            } else {
                b.push(c);
            }
        }
        let mut j = a.len();
        let mut k = b.len();
        for c in &mut bytes {
            if c.is_ascii_alphabetic() {
                j -= 1;
                *c = a[j];
            } else {
                k -= 1;
                *c = b[k];
            }
        }
        String::from_utf8(bytes).unwrap()
    }
}
'''

FILES["3824_minimum_k_to_reduce_array_within_limit"] = r'''// LeetCode 3824 - Minimum K to Reduce Array Within Limit
// https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

impl Solution {
    pub fn minimum_k(nums: Vec<i32>) -> i32 {
        let check = |k: i32| {
            let mut t = 0i64;
            for &x in &nums {
                t += (x as i64 + k as i64 - 1) / k as i64;
            }
            t <= k as i64 * k as i64
        };
        let mut lo = 1;
        let mut hi = 100000;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if check(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
'''

FILES["3825_longest_strictly_increasing_subsequence_with_non_zero_bitwise_and"] = r'''// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND
// https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/

impl Solution {
    pub fn longest_subsequence(nums: Vec<i32>) -> i32 {
        fn lis(arr: &[i32]) -> i32 {
            let mut g = Vec::new();
            for &x in arr {
                match g.binary_search(&x) {
                    Ok(_) => {}
                    Err(i) => {
                        if i == g.len() {
                            g.push(x);
                        } else {
                            g[i] = x;
                        }
                    }
                }
            }
            g.len() as i32
        }
        let mx = *nums.iter().max().unwrap_or(&0);
        let m = if mx == 0 { 0 } else { 32 - mx.leading_zeros() };
        let mut ans = 0;
        for i in 0..m {
            let arr: Vec<i32> = nums.iter().copied().filter(|&x| ((x >> i) & 1) == 1).collect();
            ans = ans.max(lis(&arr));
        }
        ans
    }
}
'''

FILES["3826_minimum_partition_score"] = r'''// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum-partition-score/

impl Solution {
    pub fn min_partition_score(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut prefix = vec![0i64; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + nums[i] as i64;
        }
        let value = |left: usize, right: usize| {
            let sum = prefix[right] - prefix[left];
            sum * (sum + 1) / 2
        };
        const INF: i64 = 1i64 << 62;
        let mut previous = vec![INF; n + 1];
        previous[0] = 0;
        for parts in 1..=k {
            let mut current = vec![INF; n + 1];
            fn compute(
                lo: usize,
                hi: i32,
                opt_lo: usize,
                opt_hi: usize,
                previous: &[i64],
                current: &mut [i64],
                value: &dyn Fn(usize, usize) -> i64,
            ) {
                if lo as i32 > hi {
                    return;
                }
                let mid = (lo as i32 + hi) as usize / 2;
                let mut best_index = None;
                let end = opt_hi.min(mid.saturating_sub(1));
                for split in opt_lo..=end {
                    if previous[split] == INF {
                        continue;
                    }
                    let candidate = previous[split] + value(split, mid);
                    if candidate < current[mid] {
                        current[mid] = candidate;
                        best_index = Some(split);
                    }
                }
                let best_index = best_index.unwrap_or(opt_lo);
                if mid > 0 {
                    compute(lo, mid as i32 - 1, opt_lo, best_index, previous, current, value);
                }
                compute(mid + 1, hi, best_index, opt_hi, previous, current, value);
            }
            compute(parts as usize, n as i32, (parts - 1) as usize, n.saturating_sub(1), &previous, &mut current, &value);
            previous = current;
        }
        previous[n]
    }
}
'''

FILES["3827_count_monobit_integers"] = r'''// LeetCode 3827 - Count Monobit Integers
// https://leetcode.com/problems/count-monobit-integers/

impl Solution {
    pub fn count_monobit(n: i32) -> i32 {
        let mut ans = 1;
        let mut i = 1;
        let mut x = 1i32;
        while x <= n {
            ans += 1;
            x += 1 << i;
            i += 1;
        }
        ans
    }
}
'''

FILES["3828_final_element_after_subarray_deletions"] = r'''// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

impl Solution {
    pub fn final_element(nums: Vec<i32>) -> i32 {
        *nums.first().unwrap().max(nums.last().unwrap())
    }
}
'''

FILES["3829_design_ride_sharing_system"] = r'''// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design-ride-sharing-system/

use std::collections::{BTreeMap, HashMap};

pub struct RideSharingSystem {
    t: i32,
    riders: BTreeMap<i32, i32>,
    drivers: BTreeMap<i32, i32>,
    d: HashMap<i32, i32>,
}

impl RideSharingSystem {
    pub fn new() -> Self {
        Self {
            t: 0,
            riders: BTreeMap::new(),
            drivers: BTreeMap::new(),
            d: HashMap::new(),
        }
    }

    pub fn add_rider(&mut self, rider_id: i32) {
        self.d.insert(rider_id, self.t);
        self.riders.insert(self.t, rider_id);
        self.t += 1;
    }

    pub fn add_driver(&mut self, driver_id: i32) {
        self.drivers.insert(self.t, driver_id);
        self.t += 1;
    }

    pub fn match_driver_with_rider(&mut self) -> Vec<i32> {
        if self.riders.is_empty() || self.drivers.is_empty() {
            return vec![-1, -1];
        }
        let (&dt, &driver_id) = self.drivers.iter().next().unwrap();
        let (&rt, &rider_id) = self.riders.iter().next().unwrap();
        self.drivers.remove(&dt);
        self.riders.remove(&rt);
        vec![driver_id, rider_id]
    }

    pub fn cancel_rider(&mut self, rider_id: i32) {
        if let Some(t) = self.d.get(&rider_id) {
            self.riders.remove(t);
        }
    }
}
'''

FILES["3830_longest_alternating_subarray_after_removing_at_most_one_element"] = r'''// LeetCode 3830 - Longest Alternating Subarray After Removing At Most One Element
// https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/

impl Solution {
    pub fn longest_alternating(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut l1 = vec![1; n];
        let mut l2 = vec![1; n];
        let mut r1 = vec![1; n];
        let mut r2 = vec![1; n];
        let mut ans = 0;
        for i in 1..n {
            if nums[i - 1] < nums[i] {
                l1[i] = l2[i - 1] + 1;
            } else if nums[i - 1] > nums[i] {
                l2[i] = l1[i - 1] + 1;
            }
            ans = ans.max(l1[i]).max(l2[i]);
        }
        for i in (0..n.saturating_sub(1)).rev() {
            if nums[i + 1] > nums[i] {
                r1[i] = r2[i + 1] + 1;
            } else if nums[i + 1] < nums[i] {
                r2[i] = r1[i + 1] + 1;
            }
        }
        if n >= 3 {
            for i in 1..n - 1 {
                if nums[i - 1] < nums[i + 1] {
                    ans = ans.max(l2[i - 1] + r2[i + 1]);
                } else if nums[i - 1] > nums[i + 1] {
                    ans = ans.max(l1[i - 1] + r1[i + 1]);
                }
            }
        }
        ans
    }
}
'''

FILES["3831_median_of_a_binary_search_tree_level"] = r'''// LeetCode 3831 - Median of a Binary Search Tree Level
// https://leetcode.com/problems/median-of-a-binary-search-tree-level/

use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn level_median(root: Option<Rc<RefCell<TreeNode>>>, level: i32) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, i: i32, level: i32, nums: &mut Vec<i32>) {
            let Some(node) = node else {
                return;
            };
            let node = node.borrow();
            dfs(node.left.clone(), i + 1, level, nums);
            if i == level {
                nums.push(node.val);
            }
            dfs(node.right.clone(), i + 1, level, nums);
        }
        let mut nums = Vec::new();
        dfs(root, 0, level, &mut nums);
        if nums.is_empty() {
            return -1;
        }
        nums[nums.len() / 2]
    }
}
'''

FILES["3833_count_dominant_indices"] = r'''// LeetCode 3833 - Count Dominant Indices
// https://leetcode.com/problems/count-dominant-indices/

impl Solution {
    pub fn dominant_indices(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        let mut suf = nums[n - 1] as i64;
        for i in (0..n - 1).rev() {
            if nums[i] as i64 * (n - i - 1) as i64 > suf {
                ans += 1;
            }
            suf += nums[i] as i64;
        }
        ans
    }
}
'''

FILES["3834_merge_adjacent_equal_elements"] = r'''// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge-adjacent-equal-elements/

impl Solution {
    pub fn merge_adjacent(nums: Vec<i32>) -> Vec<i64> {
        let mut stk = Vec::new();
        for x in nums {
            stk.push(x as i64);
            while stk.len() > 1 && stk[stk.len() - 1] == stk[stk.len() - 2] {
                let a = stk.pop().unwrap();
                let b = stk.pop().unwrap();
                stk.push(a + b);
            }
        }
        stk
    }
}
'''

FILES["3835_count_subarrays_with_cost_less_than_or_equal_to_k"] = r'''// LeetCode 3835 - Count Subarrays With Cost Less Than or Equal to K
// https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/

use std::collections::VecDeque;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i64) -> i64 {
        let mut ans = 0i64;
        let mut q1 = VecDeque::new();
        let mut q2 = VecDeque::new();
        let mut l = 0usize;
        for r in 0..nums.len() {
            let x = nums[r];
            while q1.back().map(|&i| nums[i] <= x).unwrap_or(false) {
                q1.pop_back();
            }
            while q2.back().map(|&i| nums[i] >= x).unwrap_or(false) {
                q2.pop_back();
            }
            q1.push_back(r);
            q2.push_back(r);
            while l < r
                && (nums[*q1.front().unwrap()] as i64 - nums[*q2.front().unwrap()] as i64)
                    * (r - l + 1) as i64
                    > k
            {
                l += 1;
                if *q1.front().unwrap() < l {
                    q1.pop_front();
                }
                if *q2.front().unwrap() < l {
                    q2.pop_front();
                }
            }
            ans += (r - l + 1) as i64;
        }
        ans
    }
}
'''

FILES["3836_maximum_score_using_exactly_k_pairs"] = r'''// LeetCode 3836 - Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/

impl Solution {
    pub fn max_score(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        let n = nums1.len();
        let m = nums2.len();
        let kk = k as usize;
        const NEG: i64 = i64::MIN / 4;
        let mut f = vec![vec![vec![NEG; kk + 1]; m + 1]; n + 1];
        f[0][0][0] = 0;
        for i in 0..=n {
            for j in 0..=m {
                for t in 0..=kk {
                    if i > 0 {
                        f[i][j][t] = f[i][j][t].max(f[i - 1][j][t]);
                    }
                    if j > 0 {
                        f[i][j][t] = f[i][j][t].max(f[i][j - 1][t]);
                    }
                    if i > 0 && j > 0 && t > 0 {
                        f[i][j][t] = f[i][j][t]
                            .max(f[i - 1][j - 1][t - 1] + nums1[i - 1] as i64 * nums2[j - 1] as i64);
                    }
                }
            }
        }
        f[n][m][kk]
    }
}
'''

FILES["3837_delayed_count_of_equal_elements"] = r'''// LeetCode 3837 - Delayed Count of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

use std::collections::HashMap;

impl Solution {
    pub fn delayed_count(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        let mut cnt = HashMap::new();
        let mut ans = vec![0; n];
        if n >= k + 2 {
            for i in (0..=n - k - 2).rev() {
                *cnt.entry(nums[i + k + 1]).or_insert(0) += 1;
                ans[i] = *cnt.get(&nums[i]).unwrap_or(&0);
            }
        }
        ans
    }
}
'''

FILES["3838_weighted_word_mapping"] = r'''// LeetCode 3838 - Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/

impl Solution {
    pub fn map_word_weights(words: Vec<String>, weights: Vec<i32>) -> String {
        let mut ans = String::new();
        for w in words {
            let mut s = 0;
            for c in w.bytes() {
                s = (s + weights[(c - b'a') as usize]) % 26;
            }
            ans.push((b'a' + (25 - s) as u8) as char);
        }
        ans
    }
}
'''

FILES["3839_number_of_prefix_connected_groups"] = r'''// LeetCode 3839 - Number of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

use std::collections::HashMap;

impl Solution {
    pub fn prefix_connected(words: Vec<String>, k: i32) -> i32 {
        let k = k as usize;
        let mut cnt = HashMap::new();
        for w in words {
            if w.len() >= k {
                *cnt.entry(w[..k].to_string()).or_insert(0) += 1;
            }
        }
        cnt.values().filter(|&&v| v > 1).count() as i32
    }
}
'''

FILES["3840_house_robber_v"] = r'''// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

impl Solution {
    pub fn rob(nums: Vec<i32>, colors: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut f = 0i64;
        let mut g = nums[0] as i64;
        for i in 1..n {
            if colors[i - 1] == colors[i] {
                let nf = f.max(g);
                g = f + nums[i] as i64;
                f = nf;
            } else {
                let nf = f.max(g);
                g = nf + nums[i] as i64;
                f = nf;
            }
        }
        f.max(g)
    }
}
'''

FILES["3841_palindromic_path_queries_in_a_tree"] = r'''// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

impl Solution {
    pub fn palindromic_path_queries(
        n: i32,
        edges: Vec<Vec<i32>>,
        s: String,
        queries: Vec<String>,
    ) -> Vec<bool> {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n];
        for e in &edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            graph[a].push(b);
            graph[b].push(a);
        }
        let mut parent = vec![-2i32; n];
        let mut depth = vec![0; n];
        parent[0] = -1;
        let mut order = vec![0];
        let mut i = 0;
        while i < order.len() {
            let u = order[i];
            for &v in &graph[u] {
                if parent[v] == -2 {
                    parent[v] = u as i32;
                    depth[v] = depth[u] + 1;
                    order.push(v);
                }
            }
            i += 1;
        }
        let mut size = vec![0; n];
        let mut heavy = vec![-1i32; n];
        for &u in order.iter().rev() {
            size[u] = 1;
            for &v in &graph[u] {
                if parent[v] == u as i32 {
                    size[u] += size[v];
                    if heavy[u] == -1 || size[v] > size[heavy[u] as usize] {
                        heavy[u] = v as i32;
                    }
                }
            }
        }
        let mut head = vec![0; n];
        let mut position = vec![0; n];
        let mut stack = vec![(0usize, 0usize)];
        let mut next_position = 0;
        while let Some((node, h)) = stack.pop() {
            let mut u = node as i32;
            while u != -1 {
                let uu = u as usize;
                head[uu] = h;
                position[uu] = next_position;
                next_position += 1;
                for &v in &graph[uu] {
                    if parent[v] == u && v as i32 != heavy[uu] {
                        stack.push((v, v));
                    }
                }
                u = heavy[uu];
            }
        }
        let mut bit = vec![0i32; n + 1];
        let update = |bit: &mut [i32], mut index: usize, value: i32| {
            index += 1;
            while index <= n {
                bit[index] ^= value;
                index += index & index.wrapping_neg();
            }
        };
        let prefix = |bit: &[i32], mut index: usize| {
            let mut result = 0;
            while index > 0 {
                result ^= bit[index];
                index -= index & index.wrapping_neg();
            }
            result
        };
        let path_mask = |bit: &[i32], mut u: usize, mut v: usize| {
            let mut result = 0;
            while head[u] != head[v] {
                if depth[head[u]] < depth[head[v]] {
                    std::mem::swap(&mut u, &mut v);
                }
                result ^= prefix(bit, position[u] + 1) ^ prefix(bit, position[head[u]]);
                u = parent[head[u]] as usize;
            }
            if position[u] > position[v] {
                std::mem::swap(&mut u, &mut v);
            }
            result ^ prefix(bit, position[v] + 1) ^ prefix(bit, position[u])
        };
        let mut current: Vec<u8> = s.into_bytes();
        for node in 0..n {
            update(&mut bit, position[node], 1 << (current[node] - b'a'));
        }
        let mut answer = Vec::new();
        for query in queries {
            let parts: Vec<&str> = query.split_whitespace().collect();
            let op = parts[0];
            let node: usize = parts[1].parse().unwrap();
            if op == "update" {
                let new_character = parts[2].as_bytes()[0];
                let delta =
                    (1 << (current[node] - b'a')) ^ (1 << (new_character - b'a'));
                update(&mut bit, position[node], delta);
                current[node] = new_character;
            } else {
                let other: usize = parts[2].parse().unwrap();
                let mask = path_mask(&bit, node, other);
                answer.push((mask & (mask - 1)) == 0);
            }
        }
        answer
    }
}
'''

FILES["3842_toggle_light_bulbs"] = r'''// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

impl Solution {
    pub fn toggle_light_bulbs(bulbs: Vec<i32>) -> Vec<i32> {
        let mut st = [0; 101];
        for x in bulbs {
            st[x as usize] ^= 1;
        }
        (0..101).filter(|&i| st[i] == 1).map(|i| i as i32).collect()
    }
}
'''

FILES["3843_first_element_with_unique_frequency"] = r'''// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

use std::collections::HashMap;

impl Solution {
    pub fn first_unique_freq(nums: Vec<i32>) -> i32 {
        let mut cnt = HashMap::new();
        for &x in &nums {
            *cnt.entry(x).or_insert(0) += 1;
        }
        let mut freq = HashMap::new();
        for &v in cnt.values() {
            *freq.entry(v).or_insert(0) += 1;
        }
        for x in nums {
            if freq[&cnt[&x]] == 1 {
                return x;
            }
        }
        -1
    }
}
'''

FILES["3844_longest_almost_palindromic_substring"] = r'''// LeetCode 3844 - Longest Almost Palindromic Substring
// https://leetcode.com/problems/longest-almost-palindromic-substring/

impl Solution {
    pub fn almost_palindromic(s: String) -> i32 {
        let s = s.as_bytes();
        let n = s.len() as i32;
        let f = |mut l: i32, mut r: i32| {
            while l >= 0 && r < n && s[l as usize] == s[r as usize] {
                l -= 1;
                r += 1;
            }
            let mut l1 = l - 1;
            let mut r1 = r;
            let mut l2 = l;
            let mut r2 = r + 1;
            while l1 >= 0 && r1 < n && s[l1 as usize] == s[r1 as usize] {
                l1 -= 1;
                r1 += 1;
            }
            while l2 >= 0 && r2 < n && s[l2 as usize] == s[r2 as usize] {
                l2 -= 1;
                r2 += 1;
            }
            n.min((r1 - l1 - 1).max(r2 - l2 - 1))
        };
        let mut ans = 0;
        for i in 0..n {
            ans = ans.max(f(i, i)).max(f(i, i + 1));
        }
        ans
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
