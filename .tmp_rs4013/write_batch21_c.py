#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3871_count_commas_in_range_ii"] = r'''// LeetCode 3871 - Count Commas in Range II
// https://leetcode.com/problems/count-commas-in-range-ii/

impl Solution {
    pub fn count_commas(n: i64) -> i64 {
        let mut ans = 0i64;
        let mut x = 1000i64;
        while x <= n {
            ans += n - x + 1;
            if x > i64::MAX / 1000 {
                break;
            }
            x *= 1000;
        }
        ans
    }
}
'''

FILES["3872_longest_arithmetic_sequence_after_changing_at_most_one_element"] = r'''// LeetCode 3872 - Longest Arithmetic Sequence After Changing at Most One Element
// https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

impl Solution {
    pub fn longest_arithmetic(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut d = vec![0; n];
        for i in 1..n {
            d[i] = nums[i] - nums[i - 1];
        }
        let mut f = vec![2; n];
        let mut g = vec![2; n];
        f[0] = 1;
        g[n - 1] = 1;
        for i in 2..n {
            if d[i] == d[i - 1] {
                f[i] = f[i - 1] + 1;
            }
        }
        for i in (0..n.saturating_sub(2)).rev() {
            if d[i + 1] == d[i + 2] {
                g[i] = g[i + 1] + 1;
            }
        }
        let mut ans = 3;
        for i in 0..n {
            ans = ans.max(f[i]).max(g[i]);
            if i > 0 {
                ans = ans.max(f[i - 1] + 1);
            }
            if i + 1 < n {
                ans = ans.max(g[i + 1] + 1);
            }
            if i > 0 && i < n - 1 {
                let mut diff = nums[i + 1] - nums[i - 1];
                if diff % 2 == 0 {
                    diff /= 2;
                    let mut k = 3;
                    if i > 1 && diff == d[i - 1] {
                        k += f[i - 1] - 1;
                    }
                    if i < n - 2 && diff == d[i + 2] {
                        k += g[i + 1] - 1;
                    }
                    ans = ans.max(k);
                }
            }
        }
        ans
    }
}
'''

FILES["3873_maximum_points_activated_with_one_addition"] = r'''// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

use std::collections::HashMap;

impl Solution {
    pub fn max_activated(points: Vec<Vec<i32>>) -> i32 {
        const M: i64 = 3_000_000_000;
        let mut p = HashMap::new();
        let mut size = HashMap::new();
        fn find(x: i64, p: &mut HashMap<i64, i64>, size: &mut HashMap<i64, i32>) -> i64 {
            if !p.contains_key(&x) {
                p.insert(x, x);
                size.insert(x, 1);
            }
            let px = p[&x];
            if px != x {
                let r = find(px, p, size);
                p.insert(x, r);
                return r;
            }
            x
        }
        fn unite(a: i64, b: i64, p: &mut HashMap<i64, i64>, size: &mut HashMap<i64, i32>) {
            let pa = find(a, p, size);
            let pb = find(b, p, size);
            if pa == pb {
                return;
            }
            if size[&pa] > size[&pb] {
                p.insert(pb, pa);
                *size.get_mut(&pa).unwrap() += size[&pb];
            } else {
                p.insert(pa, pb);
                *size.get_mut(&pb).unwrap() += size[&pa];
            }
        }
        for pt in &points {
            unite(pt[0] as i64, pt[1] as i64 + M, &mut p, &mut size);
        }
        let mut cnt = HashMap::new();
        for pt in &points {
            let r = find(pt[0] as i64, &mut p, &mut size);
            *cnt.entry(r).or_insert(0) += 1;
        }
        let mut mx1 = 0;
        let mut mx2 = 0;
        for &x in cnt.values() {
            if mx1 < x {
                mx2 = mx1;
                mx1 = x;
            } else if mx2 < x {
                mx2 = x;
            }
        }
        mx1 + mx2 + 1
    }
}
'''

FILES["3874_valid_subarrays_with_exactly_one_peak"] = r'''// LeetCode 3874 - Valid Subarrays With Exactly One Peak
// https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

impl Solution {
    pub fn valid_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut peaks = Vec::new();
        for i in 1..n.saturating_sub(1) {
            if nums[i] > nums[i - 1] && nums[i] > nums[i + 1] {
                peaks.push(i as i32);
            }
        }
        let mut ans = 0i64;
        for j in 0..peaks.len() {
            let p = peaks[j];
            let mut left_min = (p - k).max(0);
            if j > 0 {
                left_min = left_min.max(peaks[j - 1] + 1);
            }
            let mut right_max = (p + k).min(n as i32 - 1);
            if j + 1 < peaks.len() {
                right_max = right_max.min(peaks[j + 1] - 1);
            }
            ans += (p - left_min + 1) as i64 * (right_max - p + 1) as i64;
        }
        ans
    }
}
'''

FILES["3875_construct_uniform_parity_array_i"] = r'''// LeetCode 3875 - Construct Uniform Parity Array I
// https://leetcode.com/problems/construct-uniform-parity-array-i/

impl Solution {
    pub fn uniform_array(_nums1: Vec<i32>) -> bool {
        true
    }
}
'''

FILES["3876_construct_uniform_parity_array_ii"] = r'''// LeetCode 3876 - Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

impl Solution {
    pub fn uniform_array(nums1: Vec<i32>) -> bool {
        let mut mn = i32::MAX;
        for &x in &nums1 {
            if x % 2 == 1 && x < mn {
                mn = x;
            }
        }
        for &x in &nums1 {
            if x % 2 == 0 && mn != i32::MAX && x < mn {
                return false;
            }
        }
        true
    }
}
'''

FILES["3877_minimum_removals_to_achieve_target_xor"] = r'''// LeetCode 3877 - Minimum Removals to Achieve Target XOR
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

impl Solution {
    pub fn min_removals(nums: Vec<i32>, target: i32) -> i32 {
        let mx = *nums.iter().max().unwrap();
        let mut m = 0;
        if mx > 0 {
            let mut u = mx as u32;
            while u > 0 {
                m += 1;
                u >>= 1;
            }
        }
        if (1 << m) <= target {
            return -1;
        }
        let n = nums.len();
        let nmask = 1 << m;
        let mut f = vec![vec![i32::MIN; nmask]; n + 1];
        f[0][0] = 0;
        for i in 1..=n {
            let x = nums[i - 1] as usize;
            for j in 0..nmask {
                f[i][j] = f[i - 1][j];
                if f[i - 1][j ^ x] != i32::MIN {
                    f[i][j] = f[i][j].max(f[i - 1][j ^ x] + 1);
                }
            }
        }
        if f[n][target as usize] < 0 {
            return -1;
        }
        n as i32 - f[n][target as usize]
    }
}
'''

FILES["3878_count_good_subarrays"] = r'''// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

impl Solution {
    pub fn count_good_subarrays(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut l = vec![-1i32; n];
        let mut stk = Vec::new();
        for i in 0..n {
            let x = nums[i];
            while !stk.is_empty() {
                let last = *stk.last().unwrap();
                if nums[last] < x && (nums[last] | x) == x {
                    stk.pop();
                } else {
                    break;
                }
            }
            if !stk.is_empty() {
                l[i] = *stk.last().unwrap() as i32;
            }
            stk.push(i);
        }
        let mut r = vec![n as i32; n];
        stk.clear();
        for i in (0..n).rev() {
            while !stk.is_empty() {
                let last = *stk.last().unwrap();
                if (nums[last] | nums[i]) == nums[i] {
                    stk.pop();
                } else {
                    break;
                }
            }
            if !stk.is_empty() {
                r[i] = *stk.last().unwrap() as i32;
            }
            stk.push(i);
        }
        let mut ans = 0i64;
        for i in 0..n {
            ans += (i as i32 - l[i]) as i64 * (r[i] - i as i32) as i64;
        }
        ans
    }
}
'''

FILES["3879_maximum_distinct_path_sum_in_a_binary_tree"] = r'''// LeetCode 3879 - Maximum Distinct Path Sum in a Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl Solution {
    pub fn max_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut nodes = Vec::new();
        fn collect(node: Option<Rc<RefCell<TreeNode>>>, nodes: &mut Vec<Rc<RefCell<TreeNode>>>) {
            if let Some(n) = node {
                nodes.push(n.clone());
                let b = n.borrow();
                collect(b.left.clone(), nodes);
                collect(b.right.clone(), nodes);
            }
        }
        collect(root.clone(), &mut nodes);
        let idx: HashMap<usize, usize> = nodes
            .iter()
            .enumerate()
            .map(|(i, n)| (Rc::as_ptr(n) as usize, i))
            .collect();
        let mut g = vec![Vec::new(); nodes.len()];
        fn build(
            node: Option<Rc<RefCell<TreeNode>>>,
            parent: Option<usize>,
            idx: &HashMap<usize, usize>,
            g: &mut [Vec<Option<usize>>],
        ) {
            let Some(n) = node else {
                return;
            };
            let i = idx[&(Rc::as_ptr(&n) as usize)];
            let b = n.borrow();
            let left = b.left.as_ref().map(|c| idx[&(Rc::as_ptr(c) as usize)]);
            let right = b.right.as_ref().map(|c| idx[&(Rc::as_ptr(c) as usize)]);
            g[i] = vec![parent, left, right];
            build(b.left.clone(), Some(i), idx, g);
            build(b.right.clone(), Some(i), idx, g);
        }
        build(root, None, &idx, &mut g);
        fn dfs2(
            i: Option<usize>,
            nodes: &[Rc<RefCell<TreeNode>>],
            g: &[Vec<Option<usize>>],
            vis: &mut HashMap<i32, bool>,
        ) -> i32 {
            let Some(i) = i else {
                return 0;
            };
            let val = nodes[i].borrow().val;
            if *vis.get(&val).unwrap_or(&false) {
                return 0;
            }
            vis.insert(val, true);
            let mut best = 0;
            for &nxt in &g[i] {
                best = best.max(dfs2(nxt, nodes, g, vis));
            }
            vis.insert(val, false);
            val + best
        }
        let mut ans = i32::MIN;
        for i in 0..nodes.len() {
            let mut vis = HashMap::new();
            ans = ans.max(dfs2(Some(i), &nodes, &g, &mut vis));
        }
        ans
    }
}
'''

FILES["3880_minimum_absolute_difference_between_two_values"] = r'''// LeetCode 3880 - Minimum Absolute Difference Between Two Values
// https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

impl Solution {
    pub fn min_absolute_difference(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut ans = n + 1;
        let mut last = [-ans, -ans, -ans];
        for (i, &x) in nums.iter().enumerate() {
            if x != 0 {
                ans = ans.min(i as i32 - last[(3 - x) as usize]);
                last[x as usize] = i as i32;
            }
        }
        if ans > n {
            -1
        } else {
            ans
        }
    }
}
'''

FILES["3881_direction_assignments_with_exactly_k_visible_people"] = r'''// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

impl Solution {
    pub fn count_visible_people(n: i32, pos: i32, k: i32) -> i32 {
        const N: usize = 100001;
        const MOD: i64 = 1_000_000_007;
        fn qmi(mut a: i64, mut k: i64, p: i64) -> i64 {
            let mut res = 1;
            while k > 0 {
                if k & 1 == 1 {
                    res = res * a % p;
                }
                k >>= 1;
                a = a * a % p;
            }
            res
        }
        let mut fact = vec![0i64; N];
        let mut inv_fact = vec![0i64; N];
        fact[0] = 1;
        inv_fact[0] = 1;
        for i in 1..N {
            fact[i] = fact[i - 1] * i as i64 % MOD;
            inv_fact[i] = qmi(fact[i], MOD - 2, MOD);
        }
        let comb = |nn: i32, kk: i32| fact[nn as usize] * inv_fact[kk as usize] % MOD * inv_fact[(nn - kk) as usize] % MOD;
        let l = pos;
        let r = n - pos - 1;
        let mut ans = 0i64;
        for a in 0..=k.min(l) {
            let b = k - a;
            if b <= r {
                ans = (ans + 2 * comb(l, a) % MOD * comb(r, b) % MOD) % MOD;
            }
        }
        ans as i32
    }
}
'''

FILES["3882_minimum_xor_path_in_a_grid"] = r'''// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

impl Solution {
    pub fn min_xor(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut dp = vec![[false; 1024]; cols];
        for row in 0..rows {
            let mut left = [false; 1024];
            for col in 0..cols {
                let mut next = [false; 1024];
                let value = grid[row][col] as usize;
                if row == 0 && col == 0 {
                    next[value] = true;
                } else {
                    for xorv in 0..1024 {
                        if dp[col][xorv] || left[xorv] {
                            next[xorv ^ value] = true;
                        }
                    }
                }
                dp[col] = next;
                left = next;
            }
        }
        for xorv in 0..1024 {
            if dp[cols - 1][xorv] {
                return xorv as i32;
            }
        }
        -1
    }
}
'''

FILES["3883_count_non_decreasing_arrays_with_given_digit_sums"] = r'''// LeetCode 3883 - Count Non-Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

impl Solution {
    pub fn count_non_decreasing_arrays(digit_sum: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut groups: Vec<Vec<i32>> = vec![Vec::new(); 51];
        for x in 0..=5000 {
            let mut s = 0;
            let mut y = x;
            while y > 0 {
                s += y % 10;
                y /= 10;
            }
            groups[s as usize].push(x);
        }
        let mut prev_vals = groups[digit_sum[0] as usize].clone();
        let mut dp = vec![1; prev_vals.len()];
        for pos in 1..digit_sum.len() {
            let cur_vals = &groups[digit_sum[pos] as usize];
            let mut next = vec![0; cur_vals.len()];
            let mut j = 0;
            let mut prefix = 0;
            for i in 0..cur_vals.len() {
                let x = cur_vals[i];
                while j < prev_vals.len() && prev_vals[j] <= x {
                    prefix += dp[j];
                    if prefix >= MOD {
                        prefix -= MOD;
                    }
                    j += 1;
                }
                next[i] = prefix;
            }
            prev_vals = cur_vals.clone();
            dp = next;
        }
        let mut ans = 0;
        for x in dp {
            ans += x;
            if ans >= MOD {
                ans -= MOD;
            }
        }
        ans
    }
}
'''

FILES["3884_first_matching_character_from_both_ends"] = r'''// LeetCode 3884 - First Matching Character From Both Ends
// https://leetcode.com/problems/first-matching-character-from-both-ends/

impl Solution {
    pub fn first_matching_index(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        for i in 0..n / 2 + 1 {
            if b[i] == b[n - i - 1] {
                return i as i32;
            }
        }
        -1
    }
}
'''

FILES["3885_design_event_manager"] = r'''// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

use std::collections::{BTreeSet, HashMap};

pub struct EventManager {
    sl: BTreeSet<(i32, i32)>,
    d: HashMap<i32, i32>,
}

impl EventManager {
    pub fn new(events: Vec<Vec<i32>>) -> Self {
        let mut sl = BTreeSet::new();
        let mut d = HashMap::new();
        for e in events {
            let event_id = e[0];
            let priority = e[1];
            sl.insert((-priority, event_id));
            d.insert(event_id, priority);
        }
        Self { sl, d }
    }

    pub fn update_priority(&mut self, event_id: i32, new_priority: i32) {
        let old = self.d[&event_id];
        self.sl.remove(&(-old, event_id));
        self.sl.insert((-new_priority, event_id));
        self.d.insert(event_id, new_priority);
    }

    pub fn poll_highest(&mut self) -> i32 {
        let Some(&(neg_p, event_id)) = self.sl.iter().next() else {
            return -1;
        };
        self.sl.remove(&(neg_p, event_id));
        self.d.remove(&event_id);
        event_id
    }
}
'''

FILES["3886_sum_of_sortable_integers"] = r'''// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

impl Solution {
    pub fn sum_of_sortable_integers(nums: Vec<i32>) -> i32 {
        fn rotation_matches(block: &[i32], target: &[i32]) -> bool {
            let k = block.len();
            let mut prefix = vec![0; k];
            for i in 1..k {
                let mut j = prefix[i - 1];
                while j > 0 && target[i] != target[j] {
                    j = prefix[j - 1];
                }
                if target[i] == target[j] {
                    j += 1;
                }
                prefix[i] = j;
            }
            let mut matched = 0;
            for i in 0..2 * k - 1 {
                let x = block[i % k];
                while matched > 0 && x != target[matched] {
                    matched = prefix[matched - 1];
                }
                if x == target[matched] {
                    matched += 1;
                }
                if matched == k {
                    return true;
                }
            }
            false
        }
        let n = nums.len();
        let mut sorted = nums.clone();
        sorted.sort_unstable();
        let mut divisors = Vec::new();
        let mut d = 1;
        while d * d <= n {
            if n % d == 0 {
                divisors.push(d);
                if d * d != n {
                    divisors.push(n / d);
                }
            }
            d += 1;
        }
        let mut answer = 0;
        for k in divisors {
            let mut ok = true;
            let mut start = 0;
            while start < n {
                if !rotation_matches(&nums[start..start + k], &sorted[start..start + k]) {
                    ok = false;
                    break;
                }
                start += k;
            }
            if ok {
                answer += k as i32;
            }
        }
        answer
    }
}
'''

FILES["3887_incremental_even_weighted_cycle_queries"] = r'''// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

impl Solution {
    pub fn count_valid_edges(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut parent: Vec<usize> = (0..n).collect();
        let mut size = vec![1; n];
        let mut parity = vec![0; n];
        fn find(x: usize, parent: &mut [usize], parity: &mut [i32]) -> (usize, i32) {
            if parent[x] == x {
                return (x, 0);
            }
            let (root, p) = find(parent[x], parent, parity);
            parity[x] ^= p;
            parent[x] = root;
            (root, parity[x])
        }
        let mut ans = 0;
        for e in edges {
            let (mut ru, mut pu) = find(e[0] as usize, &mut parent, &mut parity);
            let (mut rv, mut pv) = find(e[1] as usize, &mut parent, &mut parity);
            if ru == rv {
                if (pu ^ pv) == e[2] {
                    ans += 1;
                }
                continue;
            }
            if size[ru] < size[rv] {
                std::mem::swap(&mut ru, &mut rv);
                std::mem::swap(&mut pu, &mut pv);
            }
            parent[rv] = ru;
            parity[rv] = pu ^ pv ^ e[2];
            size[ru] += size[rv];
            ans += 1;
        }
        ans
    }
}
'''

FILES["3888_minimum_operations_to_make_all_grid_elements_equal"] = r'''// LeetCode 3888 - Minimum Operations to Make All Grid Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

impl Solution {
    pub fn min_operations(grid: Vec<Vec<i32>>, k: i32) -> i64 {
        let m = grid.len();
        let n = grid[0].len();
        let max_val = grid.iter().flat_map(|row| row.iter()).copied().max().unwrap();
        let check = |target: i32| -> i64 {
            let mut diff = vec![vec![0i64; n + 2]; m + 2];
            let mut total_ops = 0i64;
            for i in 1..=m {
                for j in 1..=n {
                    diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1];
                    let cur_val = grid[i - 1][j - 1] as i64 + diff[i][j];
                    if cur_val > target as i64 {
                        return -1;
                    }
                    if cur_val < target as i64 {
                        if i + k as usize - 1 > m || j + k as usize - 1 > n {
                            return -1;
                        }
                        let needed = target as i64 - cur_val;
                        total_ops += needed;
                        diff[i][j] += needed;
                        diff[i + k as usize][j] -= needed;
                        diff[i][j + k as usize] -= needed;
                        diff[i + k as usize][j + k as usize] += needed;
                    }
                }
            }
            total_ops
        };
        for t in max_val..=max_val + 1 {
            let res = check(t);
            if res != -1 {
                return res;
            }
        }
        -1
    }
}
'''

FILES["3889_mirror_frequency_distance"] = r'''// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

use std::collections::HashMap;

impl Solution {
    pub fn mirror_frequency(s: String) -> i32 {
        let mut freq = HashMap::new();
        for c in s.chars() {
            *freq.entry(c).or_insert(0) += 1;
        }
        let mut ans = 0;
        let mut vis = HashMap::new();
        for (&c, &v) in &freq {
            let m = if c.is_ascii_lowercase() {
                (b'a' + 25 - (c as u8 - b'a')) as char
            } else {
                (b'0' + (9 - (c as u8 - b'0'))) as char
            };
            if *vis.get(&m).unwrap_or(&false) {
                continue;
            }
            vis.insert(c, true);
            let mv = *freq.get(&m).unwrap_or(&0);
            ans += (v - mv).abs();
        }
        ans
    }
}
'''

FILES["3890_integers_with_multiple_sum_of_two_cubes"] = r'''// LeetCode 3890 - Integers With Multiple Sum of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

use std::collections::HashMap;

impl Solution {
    pub fn find_good_integers(n: i32) -> Vec<i32> {
        const LIMIT: i64 = 1_000_000_000;
        let mut cnt = HashMap::new();
        let cubes: Vec<i64> = (0..=1000).map(|i| i as i64 * i as i64 * i as i64).collect();
        for a in 1..=1000 {
            for b in a..=1000 {
                let x = cubes[a] + cubes[b];
                if x > LIMIT {
                    break;
                }
                *cnt.entry(x as i32).or_insert(0) += 1;
            }
        }
        let mut good: Vec<i32> = cnt.into_iter().filter(|(_, v)| *v > 1).map(|(x, _)| x).collect();
        good.sort_unstable();
        let pos = good.partition_point(|&x| x <= n);
        good[..pos].to_vec()
    }
}
'''

FILES["3891_minimum_increase_to_maximize_special_indices"] = r'''// LeetCode 3891 - Minimum Increase to Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

impl Solution {
    pub fn min_increase(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut f = vec![[-1i64; 2]; n];
        fn dfs(i: usize, j: usize, nums: &[i32], f: &mut [[i64; 2]]) -> i64 {
            if i >= nums.len() - 1 {
                return 0;
            }
            if f[i][j] != -1 {
                return f[i][j];
            }
            let cost = 0.max(nums[i - 1].max(nums[i + 1]) + 1 - nums[i]);
            let mut ans = cost as i64 + dfs(i + 2, j, nums, f);
            if j > 0 {
                ans = ans.min(dfs(i + 1, 0, nums, f));
            }
            f[i][j] = ans;
            ans
        }
        dfs(1, ((n & 1) ^ 1), &nums, &mut f)
    }
}
'''

FILES["3892_minimum_operations_to_achieve_at_least_k_peaks"] = r'''// LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        if k == 0 {
            return 0;
        }
        if k > n as i32 / 2 {
            return -1;
        }
        let mut cost = vec![0i64; n];
        for i in 0..n {
            let left = nums[(i + n - 1) % n];
            let right = nums[(i + 1) % n];
            let need = left.max(right);
            if need >= nums[i] {
                cost[i] = need as i64 - nums[i] as i64 + 1;
            }
        }
        const INF: i64 = 1i64 << 60;
        let line = |left: i32, right: i32, choose: i32| -> i64 {
            if choose == 0 {
                return 0;
            }
            if left > right || choose > (right - left + 2) / 2 {
                return INF;
            }
            let choose = choose as usize;
            let mut prev2 = vec![INF; choose + 1];
            let mut prev1 = vec![INF; choose + 1];
            prev2[0] = 0;
            prev1[0] = 0;
            for i in left..=right {
                let mut current = prev1.clone();
                for j in 1..=choose {
                    if prev2[j - 1] != INF && prev2[j - 1] + cost[i as usize] < current[j] {
                        current[j] = prev2[j - 1] + cost[i as usize];
                    }
                }
                prev2 = prev1;
                prev1 = current;
            }
            prev1[choose]
        };
        let mut answer = line(1, n as i32 - 1, k);
        let mut with_first = line(2, n as i32 - 2, k - 1);
        if with_first != INF {
            with_first += cost[0];
            answer = answer.min(with_first);
        }
        if answer == INF {
            -1
        } else {
            answer
        }
    }
}
'''

FILES["3893_maximum_team_size_with_overlapping_intervals"] = r'''// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

impl Solution {
    pub fn maximum_team_size(start_time: Vec<i32>, end_time: Vec<i32>) -> i32 {
        let n = start_time.len();
        let mut intervals = Vec::with_capacity(n);
        for i in 0..n {
            intervals.push((start_time[i], end_time[i]));
        }
        let mut st = start_time;
        let mut en = end_time;
        st.sort_unstable();
        en.sort_unstable();
        let mut ans = 0;
        for &(l, r) in &intervals {
            let i = en.partition_point(|&x| x <= l - 1);
            let j = st.partition_point(|&x| x <= r);
            ans = ans.max((j - i) as i32);
        }
        ans
    }
}
'''

FILES["3894_traffic_signal_color"] = r'''// LeetCode 3894 - Traffic Signal Color
// https://leetcode.com/problems/traffic-signal-color/

impl Solution {
    pub fn traffic_signal(timer: i32) -> String {
        if timer == 0 {
            "Green".to_string()
        } else if timer == 30 {
            "Orange".to_string()
        } else if timer > 30 && timer <= 90 {
            "Red".to_string()
        } else {
            "Invalid".to_string()
        }
    }
}
'''

FILES["3895_count_digit_appearances"] = r'''// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

impl Solution {
    pub fn count_digit_occurrences(nums: Vec<i32>, digit: i32) -> i32 {
        let mut ans = 0;
        for mut x in nums {
            while x > 0 {
                if x % 10 == digit {
                    ans += 1;
                }
                x /= 10;
            }
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
