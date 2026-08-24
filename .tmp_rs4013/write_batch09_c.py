#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["2568_minimum_impossible_or"] = r'''// LeetCode 2568 - Minimum Impossible OR
// https://leetcode.com/problems/minimum-impossible-or/

use std::collections::HashSet;

impl Solution {
    pub fn min_impossible_or(nums: Vec<i32>) -> i32 {
        let set: HashSet<i32> = nums.into_iter().collect();
        let mut i = 1;
        loop {
            if !set.contains(&i) {
                return i;
            }
            i <<= 1;
        }
    }
}
'''

FILES["2569_handling_sum_queries_after_update"] = r'''// LeetCode 2569 - Handling Sum Queries After Update
// https://leetcode.com/problems/handling-sum-queries-after-update/

impl Solution {
    pub fn handle_query(nums1: Vec<i32>, nums2: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        let n = nums1.len();
        let mut ones = vec![0; 4 * n];
        let mut lazy = vec![false; 4 * n];
        fn build(idx: usize, l: usize, r: usize, nums1: &[i32], ones: &mut [i32]) {
            if l == r {
                ones[idx] = nums1[l];
                return;
            }
            let m = (l + r) / 2;
            build(idx * 2, l, m, nums1, ones);
            build(idx * 2 + 1, m + 1, r, nums1, ones);
            ones[idx] = ones[idx * 2] + ones[idx * 2 + 1];
        }
        fn apply(idx: usize, l: usize, r: usize, ones: &mut [i32], lazy: &mut [bool]) {
            ones[idx] = (r - l + 1) as i32 - ones[idx];
            lazy[idx] = !lazy[idx];
        }
        fn push(idx: usize, l: usize, r: usize, ones: &mut [i32], lazy: &mut [bool]) {
            if lazy[idx] && l != r {
                let m = (l + r) / 2;
                apply(idx * 2, l, m, ones, lazy);
                apply(idx * 2 + 1, m + 1, r, ones, lazy);
                lazy[idx] = false;
            }
        }
        fn update(
            idx: usize,
            l: usize,
            r: usize,
            ql: usize,
            qr: usize,
            ones: &mut [i32],
            lazy: &mut [bool],
        ) {
            if ql <= l && r <= qr {
                apply(idx, l, r, ones, lazy);
                return;
            }
            push(idx, l, r, ones, lazy);
            let m = (l + r) / 2;
            if ql <= m {
                update(idx * 2, l, m, ql, qr, ones, lazy);
            }
            if qr > m {
                update(idx * 2 + 1, m + 1, r, ql, qr, ones, lazy);
            }
            ones[idx] = ones[idx * 2] + ones[idx * 2 + 1];
        }
        build(1, 0, n - 1, &nums1, &mut ones);
        let mut sum2: i64 = nums2.iter().map(|&x| x as i64).sum();
        let mut ans = Vec::new();
        for q in queries {
            if q[0] == 1 {
                update(1, 0, n - 1, q[1] as usize, q[2] as usize, &mut ones, &mut lazy);
            } else if q[0] == 2 {
                sum2 += q[1] as i64 * ones[1] as i64;
            } else {
                ans.push(sum2);
            }
        }
        ans
    }
}
'''

FILES["2570_merge_two_2d_arrays_by_summing_values"] = r'''// LeetCode 2570 - Merge Two 2D Arrays by Summing Values
// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

impl Solution {
    pub fn merge_arrays(nums1: Vec<Vec<i32>>, nums2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut i = 0;
        let mut j = 0;
        let mut ans = Vec::new();
        while i < nums1.len() && j < nums2.len() {
            if nums1[i][0] == nums2[j][0] {
                ans.push(vec![nums1[i][0], nums1[i][1] + nums2[j][1]]);
                i += 1;
                j += 1;
            } else if nums1[i][0] < nums2[j][0] {
                ans.push(vec![nums1[i][0], nums1[i][1]]);
                i += 1;
            } else {
                ans.push(vec![nums2[j][0], nums2[j][1]]);
                j += 1;
            }
        }
        while i < nums1.len() {
            ans.push(vec![nums1[i][0], nums1[i][1]]);
            i += 1;
        }
        while j < nums2.len() {
            ans.push(vec![nums2[j][0], nums2[j][1]]);
            j += 1;
        }
        ans
    }
}
'''

FILES["2571_minimum_operations_to_reduce_an_integer_to_0"] = r'''// LeetCode 2571 - Minimum Operations to Reduce an Integer to 0
// https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/

impl Solution {
    pub fn min_operations(mut n: i32) -> i32 {
        let mut ans = 0;
        while n > 0 {
            if n & 3 == 3 {
                n += 1;
                ans += 1;
            } else if n & 1 == 1 {
                n -= 1;
                ans += 1;
            } else {
                n >>= 1;
            }
        }
        ans
    }
}
'''

FILES["2572_count_the_number_of_square_free_subsets"] = r'''// LeetCode 2572 - Count the Number of Square-Free Subsets
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/

use std::collections::HashMap;

impl Solution {
    pub fn square_free_subsets(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
        let mask_of = |mut x: i32| -> i32 {
            let mut mask = 0;
            for (i, &p) in primes.iter().enumerate() {
                let mut cnt = 0;
                while x % p == 0 {
                    x /= p;
                    cnt += 1;
                    if cnt > 1 {
                        return -1;
                    }
                }
                if cnt == 1 {
                    mask |= 1 << i;
                }
            }
            mask
        };
        let mut freq = HashMap::new();
        for x in nums {
            *freq.entry(x).or_insert(0) += 1;
        }
        let mut dp = vec![0i64; 1 << 10];
        dp[0] = 1;
        for (&x, &c) in &freq {
            if x == 1 {
                continue;
            }
            let m = mask_of(x);
            if m < 0 {
                continue;
            }
            let m = m as usize;
            for state in (0..(1 << 10)).rev() {
                if state & m == 0 {
                    dp[state | m] = (dp[state | m] + dp[state] * c as i64) % MOD;
                }
            }
        }
        let mut ans = 0i64;
        for v in dp {
            ans = (ans + v) % MOD;
        }
        let ones = *freq.get(&1).unwrap_or(&0);
        let mut mul = 1i64;
        for _ in 0..ones {
            mul = mul * 2 % MOD;
        }
        ans = ans * mul % MOD;
        ans = (ans - 1 + MOD) % MOD;
        ans as i32
    }
}
'''

FILES["2573_find_the_string_with_lcp"] = r'''// LeetCode 2573 - Find the String with LCP
// https://leetcode.com/problems/find-the-string-with-lcp/

impl Solution {
    pub fn find_the_string(lcp: Vec<Vec<i32>>) -> String {
        let n = lcp.len();
        let mut s = vec![0u8; n];
        let mut c = b'a';
        for i in 0..n {
            if s[i] != 0 {
                continue;
            }
            if c > b'z' {
                return String::new();
            }
            s[i] = c;
            for j in i + 1..n {
                if lcp[i][j] > 0 {
                    s[j] = c;
                }
            }
            c += 1;
        }
        for i in (0..n).rev() {
            for j in (0..n).rev() {
                let mut v = 0;
                if s[i] == s[j] {
                    v = 1;
                    if i + 1 < n && j + 1 < n {
                        v += lcp[i + 1][j + 1];
                    }
                }
                if lcp[i][j] != v {
                    return String::new();
                }
            }
        }
        String::from_utf8(s).unwrap()
    }
}
'''

FILES["2574_left_and_right_sum_differences"] = r'''// LeetCode 2574 - Left and Right Sum Differences
// https://leetcode.com/problems/left-and-right-sum-differences/

impl Solution {
    pub fn left_right_difference(nums: Vec<i32>) -> Vec<i32> {
        let total: i32 = nums.iter().sum();
        let mut ans = vec![0; nums.len()];
        let mut left = 0;
        for i in 0..nums.len() {
            let right = total - left - nums[i];
            ans[i] = (left - right).abs();
            left += nums[i];
        }
        ans
    }
}
'''

FILES["2575_find_the_divisibility_array_of_a_string"] = r'''// LeetCode 2575 - Find the Divisibility Array of a String
// https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

impl Solution {
    pub fn divisibility_array(word: String, m: i32) -> Vec<i32> {
        let mut ans = vec![0; word.len()];
        let mut cur = 0i64;
        let m = m as i64;
        for (i, c) in word.bytes().enumerate() {
            cur = (cur * 10 + (c - b'0') as i64) % m;
            if cur == 0 {
                ans[i] = 1;
            }
        }
        ans
    }
}
'''

FILES["2576_find_the_maximum_number_of_marked_indices"] = r'''// LeetCode 2576 - Find the Maximum Number of Marked Indices
// https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

impl Solution {
    pub fn max_num_of_marked_indices(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let mut i = 0;
        let mut ans = 0;
        for j in (n + 1) / 2..n {
            if 2 * nums[i] <= nums[j] {
                ans += 2;
                i += 1;
            }
        }
        ans
    }
}
'''

FILES["2577_minimum_time_to_visit_a_cell_in_a_grid"] = r'''// LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_time(grid: Vec<Vec<i32>>) -> i32 {
        if grid[0][1] > 1 && grid[1][0] > 1 {
            return -1;
        }
        let m = grid.len();
        let n = grid[0].len();
        let mut dist = vec![vec![i32::MAX / 2; n]; m];
        let mut h = BinaryHeap::new();
        h.push(Reverse((0, 0usize, 0usize)));
        dist[0][0] = 0;
        let dirs = [(1isize, 0isize), (-1, 0), (0, 1), (0, -1)];
        while let Some(Reverse((t, r, c))) = h.pop() {
            if r == m - 1 && c == n - 1 {
                return t;
            }
            if t > dist[r][c] {
                continue;
            }
            for (dr, dc) in dirs {
                let nr = r as isize + dr;
                let nc = c as isize + dc;
                if nr < 0 || nr >= m as isize || nc < 0 || nc >= n as isize {
                    continue;
                }
                let nr = nr as usize;
                let nc = nc as usize;
                let mut nt = t + 1;
                if nt < grid[nr][nc] {
                    let mut wait = grid[nr][nc] - nt;
                    if wait % 2 == 1 {
                        wait += 1;
                    }
                    nt += wait;
                }
                if nt < dist[nr][nc] {
                    dist[nr][nc] = nt;
                    h.push(Reverse((nt, nr, nc)));
                }
            }
        }
        -1
    }
}
'''

FILES["2578_split_with_minimum_sum"] = r'''// LeetCode 2578 - Split With Minimum Sum
// https://leetcode.com/problems/split-with-minimum-sum/

impl Solution {
    pub fn split_num(mut num: i32) -> i32 {
        let mut digits = Vec::new();
        while num > 0 {
            digits.push(num % 10);
            num /= 10;
        }
        digits.sort_unstable();
        let mut a = 0;
        let mut b = 0;
        for (i, d) in digits.into_iter().enumerate() {
            if i % 2 == 0 {
                a = a * 10 + d;
            } else {
                b = b * 10 + d;
            }
        }
        a + b
    }
}
'''

FILES["2579_count_total_number_of_colored_cells"] = r'''// LeetCode 2579 - Count Total Number of Colored Cells
// https://leetcode.com/problems/count-total-number-of-colored-cells/

impl Solution {
    pub fn colored_cells(n: i32) -> i64 {
        1 + 2 * n as i64 * (n as i64 - 1)
    }
}
'''

FILES["2580_count_ways_to_group_overlapping_ranges"] = r'''// LeetCode 2580 - Count Ways to Group Overlapping Ranges
// https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

impl Solution {
    pub fn count_ways(mut ranges: Vec<Vec<i32>>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        ranges.sort_unstable();
        let mut groups = 0;
        let mut end = -1;
        for r in ranges {
            if r[0] > end {
                groups += 1;
                end = r[1];
            } else if r[1] > end {
                end = r[1];
            }
        }
        let mut ans = 1i32;
        for _ in 0..groups {
            ans = ans * 2 % MOD;
        }
        ans
    }
}
'''

FILES["2581_count_number_of_possible_root_nodes"] = r'''// LeetCode 2581 - Count Number of Possible Root Nodes
// https://leetcode.com/problems/count-number-of-possible-root-nodes/

use std::collections::HashSet;

impl Solution {
    pub fn root_count(edges: Vec<Vec<i32>>, guesses: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = edges.len() + 1;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let guess_set: HashSet<(usize, usize)> = guesses
            .into_iter()
            .map(|gu| (gu[0] as usize, gu[1] as usize))
            .collect();
        fn dfs1(u: usize, p: i32, g: &[Vec<usize>], guess_set: &HashSet<(usize, usize)>) -> i32 {
            let mut cnt = 0;
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                if guess_set.contains(&(u, v)) {
                    cnt += 1;
                }
                cnt += dfs1(v, u as i32, g, guess_set);
            }
            cnt
        }
        let base = dfs1(0, -1, &g, &guess_set);
        let mut ans = 0;
        fn dfs2(
            u: usize,
            p: i32,
            cur: i32,
            k: i32,
            g: &[Vec<usize>],
            guess_set: &HashSet<(usize, usize)>,
            ans: &mut i32,
        ) {
            if cur >= k {
                *ans += 1;
            }
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                let mut nxt = cur;
                if guess_set.contains(&(u, v)) {
                    nxt -= 1;
                }
                if guess_set.contains(&(v, u)) {
                    nxt += 1;
                }
                dfs2(v, u as i32, nxt, k, g, guess_set, ans);
            }
        }
        dfs2(0, -1, base, k, &g, &guess_set, &mut ans);
        ans
    }
}
'''

FILES["2582_pass_the_pillow"] = r'''// LeetCode 2582 - Pass the Pillow
// https://leetcode.com/problems/pass-the-pillow/

impl Solution {
    pub fn pass_the_pillow(n: i32, time: i32) -> i32 {
        let cycle = 2 * (n - 1);
        let t = time % cycle;
        if t < n {
            1 + t
        } else {
            n - (t - (n - 1))
        }
    }
}
'''

FILES["2583_kth_largest_sum_in_a_binary_tree"] = r'''// LeetCode 2583 - Kth Largest Sum in a Binary Tree
// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

use std::cell::RefCell;
use std::collections::VecDeque;
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

impl Solution {
    pub fn kth_largest_level_sum(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i64 {
        let Some(root) = root else {
            return -1;
        };
        let mut sums = Vec::new();
        let mut q = VecDeque::new();
        q.push_back(root);
        while !q.is_empty() {
            let sz = q.len();
            let mut s = 0i64;
            for _ in 0..sz {
                let node = q.pop_front().unwrap();
                let n = node.borrow();
                s += n.val as i64;
                if let Some(left) = n.left.clone() {
                    q.push_back(left);
                }
                if let Some(right) = n.right.clone() {
                    q.push_back(right);
                }
            }
            sums.push(s);
        }
        sums.sort_by(|a, b| b.cmp(a));
        if k as usize > sums.len() {
            -1
        } else {
            sums[k as usize - 1]
        }
    }
}
'''

FILES["2584_split_the_array_to_make_coprime_products"] = r'''// LeetCode 2584 - Split the Array to Make Coprime Products
// https://leetcode.com/problems/split-the-array-to-make-coprime-products/

use std::collections::HashMap;

impl Solution {
    pub fn find_valid_split(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut first = HashMap::new();
        let mut last = HashMap::new();
        let factorize = |x: i32, idx: usize, first: &mut HashMap<i32, usize>, last: &mut HashMap<i32, usize>| {
            let mut x = x;
            let mut p = 2;
            while p * p <= x {
                if x % p == 0 {
                    first.entry(p).or_insert(idx);
                    last.insert(p, idx);
                    while x % p == 0 {
                        x /= p;
                    }
                }
                p += 1;
            }
            if x > 1 {
                first.entry(x).or_insert(idx);
                last.insert(x, idx);
            }
        };
        for i in 0..n {
            factorize(nums[i], i, &mut first, &mut last);
        }
        let mut far = 0usize;
        for i in 0..n - 1 {
            let mut x = nums[i];
            let mut p = 2;
            while p * p <= x {
                if x % p == 0 {
                    if let Some(&lf) = last.get(&p) {
                        if lf > far {
                            far = lf;
                        }
                    }
                    while x % p == 0 {
                        x /= p;
                    }
                }
                p += 1;
            }
            if x > 1 {
                if let Some(&lf) = last.get(&x) {
                    if lf > far {
                        far = lf;
                    }
                }
            }
            if far == i {
                return i as i32;
            }
        }
        -1
    }
}
'''

FILES["2585_number_of_ways_to_earn_points"] = r'''// LeetCode 2585 - Number of Ways to Earn Points
// https://leetcode.com/problems/number-of-ways-to-earn-points/

impl Solution {
    pub fn ways_to_reach_target(target: i32, types: Vec<Vec<i32>>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let target = target as usize;
        let mut dp = vec![0; target + 1];
        dp[0] = 1;
        for t in types {
            let count = t[0];
            let marks = t[1] as usize;
            for s in (0..=target).rev() {
                let mut k = 1;
                while k <= count && s >= k as usize * marks {
                    dp[s] = (dp[s] + dp[s - k as usize * marks]) % MOD;
                    k += 1;
                }
            }
        }
        dp[target]
    }
}
'''

FILES["2586_count_the_number_of_vowel_strings_in_range"] = r'''// LeetCode 2586 - Count the Number of Vowel Strings in Range
// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

impl Solution {
    pub fn vowel_strings(words: Vec<String>, left: i32, right: i32) -> i32 {
        fn is_v(c: u8) -> bool {
            matches!(c, b'a' | b'e' | b'i' | b'o' | b'u')
        }
        let mut ans = 0;
        for i in left as usize..=right as usize {
            let w = words[i].as_bytes();
            if is_v(w[0]) && is_v(w[w.len() - 1]) {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2587_rearrange_array_to_maximize_prefix_score"] = r'''// LeetCode 2587 - Rearrange Array to Maximize Prefix Score
// https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

impl Solution {
    pub fn max_score(mut nums: Vec<i32>) -> i32 {
        nums.sort_by(|a, b| b.cmp(a));
        let mut sum = 0i64;
        let mut ans = 0;
        for x in nums {
            sum += x as i64;
            if sum > 0 {
                ans += 1;
            } else {
                break;
            }
        }
        ans
    }
}
'''

FILES["2588_count_the_number_of_beautiful_subarrays"] = r'''// LeetCode 2588 - Count the Number of Beautiful Subarrays
// https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

use std::collections::HashMap;

impl Solution {
    pub fn beautiful_subarrays(nums: Vec<i32>) -> i64 {
        let mut freq = HashMap::from([(0, 1)]);
        let mut xorv = 0;
        let mut ans = 0i64;
        for x in nums {
            xorv ^= x;
            ans += *freq.get(&xorv).unwrap_or(&0);
            *freq.entry(xorv).or_insert(0) += 1;
        }
        ans
    }
}
'''

FILES["2589_minimum_time_to_complete_all_tasks"] = r'''// LeetCode 2589 - Minimum Time to Complete All Tasks
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

impl Solution {
    pub fn find_minimum_time(mut tasks: Vec<Vec<i32>>) -> i32 {
        tasks.sort_by_key(|t| t[1]);
        let mut used = vec![false; 2001];
        let mut ans = 0;
        for t in tasks {
            let start = t[0] as usize;
            let end = t[1] as usize;
            let dur = t[2];
            let mut have = 0;
            for i in start..=end {
                if used[i] {
                    have += 1;
                }
            }
            let mut need = dur - have;
            for i in (start..=end).rev() {
                if need <= 0 {
                    break;
                }
                if !used[i] {
                    used[i] = true;
                    need -= 1;
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["2590_design_a_todo_list"] = r'''// LeetCode 2590 - Design a Todo List
// https://leetcode.com/problems/design-a-todo-list/

use std::collections::{HashMap, HashSet};

struct Task {
    id: i32,
    description: String,
    due_date: i32,
    tags: HashSet<String>,
    done: bool,
    user_id: i32,
}

pub struct TodoList {
    next_id: i32,
    tasks: HashMap<i32, Task>,
    users: HashMap<i32, Vec<i32>>,
}

impl TodoList {
    pub fn new() -> Self {
        Self {
            next_id: 1,
            tasks: HashMap::new(),
            users: HashMap::new(),
        }
    }

    pub fn add_task(
        &mut self,
        user_id: i32,
        task_description: String,
        due_date: i32,
        tags: Vec<String>,
    ) -> i32 {
        let id = self.next_id;
        self.next_id += 1;
        let tk = Task {
            id,
            description: task_description,
            due_date,
            tags: tags.into_iter().collect(),
            done: false,
            user_id,
        };
        self.tasks.insert(id, tk);
        self.users.entry(user_id).or_default().push(id);
        id
    }

    pub fn get_all_tasks(&self, user_id: i32) -> Vec<String> {
        let mut ids = self.users.get(&user_id).cloned().unwrap_or_default();
        ids.sort_by_key(|id| self.tasks[id].due_date);
        ids.into_iter()
            .filter(|id| !self.tasks[id].done)
            .map(|id| self.tasks[&id].description.clone())
            .collect()
    }

    pub fn get_tasks_for_tag(&self, user_id: i32, tag: String) -> Vec<String> {
        let mut ids = self.users.get(&user_id).cloned().unwrap_or_default();
        ids.sort_by_key(|id| self.tasks[id].due_date);
        ids.into_iter()
            .filter(|id| {
                let tk = &self.tasks[id];
                !tk.done && tk.tags.contains(&tag)
            })
            .map(|id| self.tasks[&id].description.clone())
            .collect()
    }

    pub fn complete_task(&mut self, user_id: i32, task_id: i32) {
        if let Some(tk) = self.tasks.get_mut(&task_id) {
            if tk.user_id == user_id && !tk.done {
                tk.done = true;
            }
        }
    }
}
'''

FILES["2591_distribute_money_to_maximum_children"] = r'''// LeetCode 2591 - Distribute Money to Maximum Children
// https://leetcode.com/problems/distribute-money-to-maximum-children/

impl Solution {
    pub fn dist_money(mut money: i32, children: i32) -> i32 {
        if money < children {
            return -1;
        }
        money -= children;
        let mut ans = money / 7;
        if ans > children {
            ans = children;
        }
        let remain_money = money - ans * 7;
        let remain_child = children - ans;
        if remain_child == 0 && remain_money > 0 {
            ans -= 1;
        } else if remain_child == 1 && remain_money == 3 {
            ans -= 1;
        }
        if ans < 0 {
            0
        } else {
            ans
        }
    }
}
'''

FILES["2592_maximize_greatness_of_an_array"] = r'''// LeetCode 2592 - Maximize Greatness of an Array
// https://leetcode.com/problems/maximize-greatness-of-an-array/

impl Solution {
    pub fn maximize_greatness(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut i = 0;
        for &x in &nums {
            if x > nums[i] {
                i += 1;
            }
        }
        i as i32
    }
}
'''

def main():
    n = 0
    for folder, text in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(text, encoding="utf-8", newline="\n")
        n += 1
        print(f"wrote {folder}")
    print(f"total={n}")

if __name__ == "__main__":
    main()
