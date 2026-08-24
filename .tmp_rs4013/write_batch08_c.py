#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

TREE = """use std::cell::RefCell;
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
"""

LIST = """#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}
"""

FILES = {}

FILES["2462_total_cost_to_hire_k_workers"] = r'''// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn total_cost(costs: Vec<i32>, k: i32, candidates: i32) -> i64 {
        let n = costs.len();
        let candidates = candidates as usize;
        let mut left_h: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
        let mut right_h: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
        let mut l = 0usize;
        let mut r = n as i32 - 1;
        while l as i32 <= r && left_h.len() < candidates {
            left_h.push(Reverse((costs[l], l)));
            l += 1;
        }
        while r >= l as i32 && right_h.len() < candidates {
            right_h.push(Reverse((costs[r as usize], r as usize)));
            r -= 1;
        }
        let mut ans = 0i64;
        for _ in 0..k {
            let use_left = match (left_h.peek(), right_h.peek()) {
                (Some(Reverse((lv, li))), Some(Reverse((rv, ri)))) => {
                    *lv < *rv || (*lv == *rv && *li <= *ri)
                }
                (Some(_), None) => true,
                _ => false,
            };
            if use_left {
                let Reverse((v, _)) = left_h.pop().unwrap();
                ans += v as i64;
                if (l as i32) <= r {
                    left_h.push(Reverse((costs[l], l)));
                    l += 1;
                }
            } else {
                let Reverse((v, _)) = right_h.pop().unwrap();
                ans += v as i64;
                if (l as i32) <= r {
                    right_h.push(Reverse((costs[r as usize], r as usize)));
                    r -= 1;
                }
            }
        }
        ans
    }
}
'''

FILES["2463_minimum_total_distance_traveled"] = r'''// LeetCode 2463 - Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/

impl Solution {
    pub fn minimum_total_distance(mut robot: Vec<i32>, mut factory: Vec<Vec<i32>>) -> i64 {
        robot.sort_unstable();
        factory.sort_unstable();
        let m = robot.len();
        let mut pos = Vec::new();
        for f in &factory {
            for _ in 0..f[1] {
                pos.push(f[0]);
            }
        }
        let n = pos.len();
        const INF: i64 = 1 << 60;
        let mut dp = vec![vec![INF; n + 1]; m + 1];
        for j in 0..=n {
            dp[0][j] = 0;
        }
        for i in 1..=m {
            for j in i..=n {
                dp[i][j] = dp[i][j - 1];
                let mut diff = robot[i - 1] as i64 - pos[j - 1] as i64;
                if diff < 0 {
                    diff = -diff;
                }
                if dp[i - 1][j - 1] + diff < dp[i][j] {
                    dp[i][j] = dp[i - 1][j - 1] + diff;
                }
            }
        }
        dp[m][n]
    }
}
'''

FILES["2464_minimum_subarrays_in_a_valid_split"] = r'''// LeetCode 2464 - Minimum Subarrays in a Valid Split
// https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

impl Solution {
    pub fn valid_subarray_split(nums: Vec<i32>) -> i32 {
        fn gcd(mut x: i32, mut y: i32) -> i32 {
            while y != 0 {
                let t = x % y;
                x = y;
                y = t;
            }
            x
        }
        let n = nums.len();
        const INF: i32 = 1 << 30;
        let mut dp = vec![INF; n + 1];
        dp[0] = 0;
        for i in 0..n {
            if dp[i] >= INF {
                continue;
            }
            for j in i..n {
                if gcd(nums[i], nums[j]) > 1 && dp[i] + 1 < dp[j + 1] {
                    dp[j + 1] = dp[i] + 1;
                }
            }
        }
        if dp[n] >= INF {
            -1
        } else {
            dp[n]
        }
    }
}
'''

FILES["2465_number_of_distinct_averages"] = r'''// LeetCode 2465 - Number of Distinct Averages
// https://leetcode.com/problems/number-of-distinct-averages/

use std::collections::HashSet;

impl Solution {
    pub fn distinct_averages(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut seen = HashSet::new();
        let mut l = 0;
        let mut r = nums.len() - 1;
        while l < r {
            seen.insert(nums[l] + nums[r]);
            l += 1;
            r -= 1;
        }
        seen.len() as i32
    }
}
'''

FILES["2466_count_ways_to_build_good_strings"] = r'''// LeetCode 2466 - Count Ways To Build Good Strings
// https://leetcode.com/problems/count-ways-to-build-good-strings/

impl Solution {
    pub fn count_good_strings(low: i32, high: i32, zero: i32, one: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let high = high as usize;
        let low = low as usize;
        let zero = zero as usize;
        let one = one as usize;
        let mut dp = vec![0; high + 1];
        dp[0] = 1;
        let mut ans = 0;
        for i in 1..=high {
            if i >= zero {
                dp[i] = (dp[i] + dp[i - zero]) % MOD;
            }
            if i >= one {
                dp[i] = (dp[i] + dp[i - one]) % MOD;
            }
            if i >= low {
                ans = (ans + dp[i]) % MOD;
            }
        }
        ans
    }
}
'''

FILES["2467_most_profitable_path_in_a_tree"] = r'''// LeetCode 2467 - Most Profitable Path in a Tree
// https://leetcode.com/problems/most-profitable-path-in-a-tree/

impl Solution {
    pub fn most_profitable_path(edges: Vec<Vec<i32>>, bob: i32, amount: Vec<i32>) -> i32 {
        let n = amount.len();
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        let mut bob_time = vec![n as i32; n];
        fn find_bob(
            u: usize,
            p: i32,
            t: i32,
            g: &[Vec<usize>],
            bob_time: &mut [i32],
        ) -> bool {
            if u == 0 {
                bob_time[u] = t;
                return true;
            }
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                if find_bob(v, u as i32, t + 1, g, bob_time) {
                    bob_time[u] = t;
                    return true;
                }
            }
            false
        }
        find_bob(bob as usize, -1, 0, &g, &mut bob_time);
        let mut ans = i32::MIN;
        fn dfs(
            u: usize,
            p: i32,
            t: i32,
            income: i32,
            g: &[Vec<usize>],
            amount: &[i32],
            bob_time: &[i32],
            ans: &mut i32,
        ) {
            let mut cur = amount[u];
            if t > bob_time[u] {
                cur = 0;
            } else if t == bob_time[u] {
                cur /= 2;
            }
            let income = income + cur;
            let mut is_leaf = true;
            for &v in &g[u] {
                if v as i32 != p {
                    is_leaf = false;
                    dfs(v, u as i32, t + 1, income, g, amount, bob_time, ans);
                }
            }
            if is_leaf && income > *ans {
                *ans = income;
            }
        }
        dfs(0, -1, 0, 0, &g, &amount, &bob_time, &mut ans);
        ans
    }
}
'''

FILES["2468_split_message_based_on_limit"] = r'''// LeetCode 2468 - Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/

impl Solution {
    pub fn split_message(message: String, limit: i32) -> Vec<String> {
        let n = message.len();
        let bytes = message.as_bytes();
        for parts in 1..=n {
            let sb_digits = parts.to_string().len();
            let mut ok = true;
            let mut idx = 0;
            let mut res = Vec::new();
            for i in 1..=parts {
                let tail = 3 + i.to_string().len() + sb_digits;
                let cap = limit as isize - tail as isize;
                if cap <= 0 || idx >= n {
                    ok = false;
                    break;
                }
                let mut take = cap as usize;
                if take > n - idx {
                    take = n - idx;
                }
                let mut part = String::from_utf8(bytes[idx..idx + take].to_vec()).unwrap();
                part.push_str(&format!("<{}/{}>", i, parts));
                res.push(part);
                idx += take;
            }
            if ok && idx == n {
                return res;
            }
        }
        vec![]
    }
}
'''

FILES["2469_convert_the_temperature"] = r'''// LeetCode 2469 - Convert the Temperature
// https://leetcode.com/problems/convert-the-temperature/

impl Solution {
    pub fn convert_temperature(celsius: f64) -> Vec<f64> {
        vec![celsius + 273.15, celsius * 1.80 + 32.00]
    }
}
'''

FILES["2470_number_of_subarrays_with_lcm_equal_to_k"] = r'''// LeetCode 2470 - Number of Subarrays With LCM Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

impl Solution {
    pub fn subarray_lcm(nums: Vec<i32>, k: i32) -> i32 {
        fn gcd(mut x: i64, mut y: i64) -> i64 {
            while y != 0 {
                let t = x % y;
                x = y;
                y = t;
            }
            x
        }
        let mut ans = 0;
        let n = nums.len();
        for i in 0..n {
            let mut cur = 1i64;
            for j in i..n {
                let x = nums[j] as i64;
                cur = cur / gcd(cur, x) * x;
                if cur > k as i64 {
                    break;
                }
                if cur == k as i64 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["2471_minimum_number_of_operations_to_sort_a_binary_tree_by_level"] = f'''// LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

use std::collections::{{HashMap, VecDeque}};
{TREE}
impl Solution {{
    pub fn minimum_operations(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {{
        let Some(root) = root else {{
            return 0;
        }};
        let mut ans = 0;
        let mut q = VecDeque::new();
        q.push_back(root);
        while !q.is_empty() {{
            let sz = q.len();
            let mut vals = vec![0; sz];
            for i in 0..sz {{
                let node = q.pop_front().unwrap();
                let n = node.borrow();
                vals[i] = n.val;
                if let Some(l) = &n.left {{
                    q.push_back(l.clone());
                }}
                if let Some(r) = &n.right {{
                    q.push_back(r.clone());
                }}
            }}
            let mut sorted = vals.clone();
            sorted.sort_unstable();
            let mut pos: HashMap<i32, usize> = HashMap::new();
            for i in 0..sz {{
                pos.insert(vals[i], i);
            }}
            for i in 0..sz {{
                if vals[i] != sorted[i] {{
                    let j = pos[&sorted[i]];
                    vals.swap(i, j);
                    pos.insert(vals[j], j);
                    pos.insert(vals[i], i);
                    ans += 1;
                }}
            }}
        }}
        ans
    }}
}}
'''

FILES["2472_maximum_number_of_non_overlapping_palindrome_substrings"] = r'''// LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

impl Solution {
    pub fn max_palindromes(s: String, k: i32) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let k = k as usize;
        let mut is_pal = vec![vec![false; n]; n];
        for i in 0..n {
            is_pal[i][i] = true;
        }
        for i in 0..n.saturating_sub(1) {
            is_pal[i][i + 1] = b[i] == b[i + 1];
        }
        for length in 3..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                is_pal[i][j] = b[i] == b[j] && is_pal[i + 1][j - 1];
            }
        }
        let mut dp = vec![0; n + 1];
        for i in (0..n).rev() {
            dp[i] = dp[i + 1];
            if i + k - 1 < n {
                for j in (i + k - 1)..n {
                    if is_pal[i][j] && 1 + dp[j + 1] > dp[i] {
                        dp[i] = 1 + dp[j + 1];
                    }
                }
            }
        }
        dp[0]
    }
}
'''

FILES["2473_minimum_cost_to_buy_apples"] = r'''// LeetCode 2473 - Minimum Cost to Buy Apples
// https://leetcode.com/problems/minimum-cost-to-buy-apples/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_cost(n: i32, roads: Vec<Vec<i32>>, apple_cost: Vec<i32>, k: i32) -> Vec<i64> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n + 1];
        for r in &roads {
            let (a, b, w) = (r[0] as usize, r[1] as usize, r[2] as i64);
            g[a].push((b, w));
            g[b].push((a, w));
        }
        let mut ans = vec![0i64; n];
        const INF: i64 = 1 << 60;
        for start in 1..=n {
            let mut dist = vec![INF; n + 1];
            dist[start] = 0;
            let mut pq: BinaryHeap<Reverse<(i64, usize)>> = BinaryHeap::new();
            pq.push(Reverse((0, start)));
            while let Some(Reverse((d, u))) = pq.pop() {
                if d != dist[u] {
                    continue;
                }
                for &(v, w) in &g[u] {
                    let nd = d + w;
                    if nd < dist[v] {
                        dist[v] = nd;
                        pq.push(Reverse((nd, v)));
                    }
                }
            }
            let mut best = INF;
            for city in 1..=n {
                let cost = dist[city] * (k as i64 + 1) + apple_cost[city - 1] as i64;
                if cost < best {
                    best = cost;
                }
            }
            ans[start - 1] = best;
        }
        ans
    }
}
'''

FILES["2475_number_of_unequal_triplets_in_array"] = r'''// LeetCode 2475 - Number of Unequal Triplets in Array
// https://leetcode.com/problems/number-of-unequal-triplets-in-array/

use std::collections::HashMap;

impl Solution {
    pub fn unequal_triplets(nums: Vec<i32>) -> i32 {
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        for x in &nums {
            *cnt.entry(*x).or_insert(0) += 1;
        }
        let mut ans = 0;
        let n = nums.len() as i32;
        let mut left = 0;
        for &c in cnt.values() {
            let right = n - left - c;
            ans += left * c * right;
            left += c;
        }
        ans
    }
}
'''

FILES["2476_closest_nodes_queries_in_a_binary_search_tree"] = f'''// LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

{TREE}
impl Solution {{
    pub fn closest_nodes(
        root: Option<Rc<RefCell<TreeNode>>>,
        queries: Vec<i32>,
    ) -> Vec<Vec<i32>> {{
        let mut vals = Vec::new();
        fn inorder(node: &Option<Rc<RefCell<TreeNode>>>, vals: &mut Vec<i32>) {{
            if let Some(n) = node {{
                let n = n.borrow();
                inorder(&n.left, vals);
                vals.push(n.val);
                inorder(&n.right, vals);
            }}
        }}
        inorder(&root, &mut vals);
        let mut ans = vec![vec![0; 2]; queries.len()];
        for (i, &q) in queries.iter().enumerate() {{
            let j = vals.partition_point(|&x| x < q);
            let mx = if j < vals.len() {{ vals[j] }} else {{ -1 }};
            let mn = if j < vals.len() && vals[j] == q {{
                q
            }} else if j > 0 {{
                vals[j - 1]
            }} else {{
                -1
            }};
            ans[i] = vec![mn, mx];
        }}
        ans
    }}
}}
'''

FILES["2477_minimum_fuel_cost_to_report_to_the_capital"] = r'''// LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

impl Solution {
    pub fn minimum_fuel_cost(roads: Vec<Vec<i32>>, seats: i32) -> i64 {
        let n = roads.len() + 1;
        let mut g = vec![Vec::new(); n];
        for r in &roads {
            let (a, b) = (r[0] as usize, r[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        let mut ans = 0i64;
        fn dfs(u: usize, p: i32, seats: i32, g: &[Vec<usize>], ans: &mut i64) -> i32 {
            let mut people = 1;
            for &v in &g[u] {
                if v as i32 != p {
                    people += dfs(v, u as i32, seats, g, ans);
                }
            }
            if u != 0 {
                *ans += ((people + seats - 1) / seats) as i64;
            }
            people
        }
        dfs(0, -1, seats, &g, &mut ans);
        ans
    }
}
'''

FILES["2478_number_of_beautiful_partitions"] = r'''// LeetCode 2478 - Number of Beautiful Partitions
// https://leetcode.com/problems/number-of-beautiful-partitions/

impl Solution {
    pub fn beautiful_partitions(s: String, k: i32, min_length: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        fn is_prime(c: u8) -> bool {
            matches!(c, b'2' | b'3' | b'5' | b'7')
        }
        let b = s.as_bytes();
        let n = b.len();
        if !is_prime(b[0]) || is_prime(b[n - 1]) {
            return 0;
        }
        let k = k as usize;
        let min_length = min_length as usize;
        let mut dp = vec![vec![0; n + 1]; k + 1];
        dp[0][0] = 1;
        for p in 1..=k {
            let mut pref = 0;
            let mut j = 0;
            for i in 1..=n {
                while j + min_length <= i {
                    if j == 0 || (is_prime(b[j]) && !is_prime(b[j - 1])) {
                        pref = (pref + dp[p - 1][j]) % MOD;
                    }
                    j += 1;
                }
                if !is_prime(b[i - 1]) {
                    dp[p][i] = pref;
                }
            }
        }
        dp[k][n]
    }
}
'''

FILES["2479_maximum_xor_of_two_non_overlapping_subtrees"] = r'''// LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
// https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

impl Solution {
    pub fn max_xor(n: i32, edges: Vec<Vec<i32>>, values: Vec<i32>) -> i64 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        let mut sum = vec![0i64; n];
        fn dfs_sum(u: usize, p: i32, g: &[Vec<usize>], values: &[i32], sum: &mut [i64]) -> i64 {
            let mut s = values[u] as i64;
            for &v in &g[u] {
                if v as i32 != p {
                    s += dfs_sum(v, u as i32, g, values, sum);
                }
            }
            sum[u] = s;
            s
        }
        dfs_sum(0, -1, &g, &values, &mut sum);

        struct TrieNode {
            child: [Option<Box<TrieNode>>; 2],
        }
        impl TrieNode {
            fn new() -> Self {
                Self {
                    child: [None, None],
                }
            }
        }
        let mut root = TrieNode::new();
        fn insert(root: &mut TrieNode, x: i64) {
            let mut cur = root;
            for b in (0..=46).rev() {
                let bit = ((x >> b) & 1) as usize;
                if cur.child[bit].is_none() {
                    cur.child[bit] = Some(Box::new(TrieNode::new()));
                }
                cur = cur.child[bit].as_mut().unwrap();
            }
        }
        fn query(root: &TrieNode, x: i64) -> i64 {
            if root.child[0].is_none() && root.child[1].is_none() {
                return 0;
            }
            let mut cur = root;
            let mut ans = 0i64;
            for b in (0..=46).rev() {
                let bit = ((x >> b) & 1) as usize;
                let want = bit ^ 1;
                if cur.child[want].is_some() {
                    ans |= 1i64 << b;
                    cur = cur.child[want].as_ref().unwrap();
                } else if cur.child[bit].is_some() {
                    cur = cur.child[bit].as_ref().unwrap();
                } else {
                    return ans;
                }
            }
            ans
        }

        let mut ans = 0i64;
        fn dfs(
            u: usize,
            p: i32,
            g: &[Vec<usize>],
            sum: &[i64],
            root: &mut TrieNode,
            ans: &mut i64,
        ) {
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                let xorv = query(root, sum[v]);
                if xorv > *ans {
                    *ans = xorv;
                }
                dfs(v, u as i32, g, sum, root, ans);
                insert(root, sum[v]);
            }
        }
        dfs(0, -1, &g, &sum, &mut root, &mut ans);
        ans
    }
}
'''

FILES["2481_minimum_cuts_to_divide_a_circle"] = r'''// LeetCode 2481 - Minimum Cuts to Divide a Circle
// https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

impl Solution {
    pub fn number_of_cuts(n: i32) -> i32 {
        if n == 1 {
            0
        } else if n % 2 == 0 {
            n / 2
        } else {
            n
        }
    }
}
'''

FILES["2482_difference_between_ones_and_zeros_in_row_and_column"] = r'''// LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

impl Solution {
    pub fn ones_minus_zeros(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut row = vec![0; m];
        let mut col = vec![0; n];
        for i in 0..m {
            for j in 0..n {
                row[i] += grid[i][j];
                col[j] += grid[i][j];
            }
        }
        let mut ans = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                ans[i][j] = row[i] + col[j] - (m as i32 - row[i]) - (n as i32 - col[j]);
            }
        }
        ans
    }
}
'''

FILES["2483_minimum_penalty_for_a_shop"] = r'''// LeetCode 2483 - Minimum Penalty for a Shop
// https://leetcode.com/problems/minimum-penalty-for-a-shop/

impl Solution {
    pub fn best_closing_time(customers: String) -> i32 {
        let b = customers.as_bytes();
        let mut penalty = b.iter().filter(|&&c| c == b'Y').count() as i32;
        let mut best = penalty;
        let mut ans = 0;
        for (i, &c) in b.iter().enumerate() {
            if c == b'Y' {
                penalty -= 1;
            } else {
                penalty += 1;
            }
            if penalty < best {
                best = penalty;
                ans = i as i32 + 1;
            }
        }
        ans
    }
}
'''

FILES["2484_count_palindromic_subsequences"] = r'''// LeetCode 2484 - Count Palindromic Subsequences
// https://leetcode.com/problems/count-palindromic-subsequences/

impl Solution {
    pub fn count_palindromes(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let b = s.as_bytes();
        let n = b.len();
        let mut pref = vec![[[0i64; 10]; 10]; n];
        let mut suf = vec![[[0i64; 10]; 10]; n];
        let mut cnt = [0i64; 10];
        for i in 0..n {
            if i > 0 {
                pref[i] = pref[i - 1];
            }
            let d = (b[i] - b'0') as usize;
            for a in 0..10 {
                pref[i][a][d] += cnt[a];
            }
            cnt[d] += 1;
        }
        cnt = [0; 10];
        for i in (0..n).rev() {
            if i + 1 < n {
                suf[i] = suf[i + 1];
            }
            let d = (b[i] - b'0') as usize;
            for a in 0..10 {
                suf[i][a][d] += cnt[a];
            }
            cnt[d] += 1;
        }
        let mut ans = 0i64;
        for i in 2..n.saturating_sub(2) {
            for a in 0..10 {
                for bb in 0..10 {
                    ans = (ans + pref[i - 1][a][bb] * suf[i + 1][a][bb]) % MOD;
                }
            }
        }
        ans as i32
    }
}
'''

FILES["2485_find_the_pivot_integer"] = r'''// LeetCode 2485 - Find the Pivot Integer
// https://leetcode.com/problems/find-the-pivot-integer/

impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        let total = n * (n + 1) / 2;
        let mut sum = 0;
        for x in 1..=n {
            sum += x;
            if sum == total - sum + x {
                return x;
            }
        }
        -1
    }
}
'''

FILES["2486_append_characters_to_string_to_make_subsequence"] = r'''// LeetCode 2486 - Append Characters to String to Make Subsequence
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

impl Solution {
    pub fn append_characters(s: String, t: String) -> i32 {
        let sb = s.as_bytes();
        let tb = t.as_bytes();
        let mut j = 0;
        for &c in sb {
            if j < tb.len() && c == tb[j] {
                j += 1;
            }
        }
        (tb.len() - j) as i32
    }
}
'''

FILES["2487_remove_nodes_from_linked_list"] = f'''// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

{LIST}
impl Solution {{
    pub fn remove_nodes(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {{
        fn rev(mut node: Option<Box<ListNode>>) -> Option<Box<ListNode>> {{
            let mut prev = None;
            while let Some(mut cur) = node {{
                node = cur.next.take();
                cur.next = prev;
                prev = Some(cur);
            }}
            prev
        }}
        let mut head = rev(head);
        let mut mx = 0;
        let mut dummy = Box::new(ListNode {{ val: 0, next: head }});
        let mut prev = dummy.as_mut();
        while prev.next.is_some() {{
            if prev.next.as_ref().unwrap().val >= mx {{
                mx = prev.next.as_ref().unwrap().val;
                prev = prev.next.as_mut().unwrap();
            }} else {{
                prev.next = prev.next.as_mut().unwrap().next.take();
            }}
        }}
        rev(dummy.next)
    }}
}}
'''

FILES["2488_count_subarrays_with_median_k"] = r'''// LeetCode 2488 - Count Subarrays With Median K
// https://leetcode.com/problems/count-subarrays-with-median-k/

use std::collections::HashMap;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i32 {
        let mut pos = 0;
        for (i, &x) in nums.iter().enumerate() {
            if x == k {
                pos = i;
                break;
            }
        }
        let mut bal: HashMap<i32, i32> = HashMap::new();
        bal.insert(0, 1);
        let mut cur = 0;
        for i in (0..pos).rev() {
            cur += if nums[i] < k { -1 } else { 1 };
            *bal.entry(cur).or_insert(0) += 1;
        }
        let mut ans = *bal.get(&0).unwrap_or(&0) + *bal.get(&1).unwrap_or(&0);
        cur = 0;
        for i in pos + 1..nums.len() {
            cur += if nums[i] < k { -1 } else { 1 };
            ans += *bal.get(&(-cur)).unwrap_or(&0) + *bal.get(&(1 - cur)).unwrap_or(&0);
        }
        ans
    }
}
'''

FILES["2489_number_of_substrings_with_fixed_ratio"] = r'''// LeetCode 2489 - Number of Substrings With Fixed Ratio
// https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

use std::collections::HashMap;

impl Solution {
    pub fn fixed_ratio(s: String, num1: i32, num2: i32) -> i64 {
        let mut pref: HashMap<i64, i32> = HashMap::new();
        pref.insert(0, 1);
        let mut zeros = 0i64;
        let mut ones = 0i64;
        let mut ans = 0i64;
        for c in s.bytes() {
            if c == b'0' {
                zeros += 1;
            } else {
                ones += 1;
            }
            let key = zeros * num2 as i64 - ones * num1 as i64;
            ans += *pref.get(&key).unwrap_or(&0) as i64;
            *pref.entry(key).or_insert(0) += 1;
        }
        ans
    }
}
'''

FILES["2490_circular_sentence"] = r'''// LeetCode 2490 - Circular Sentence
// https://leetcode.com/problems/circular-sentence/

impl Solution {
    pub fn is_circular_sentence(sentence: String) -> bool {
        let b = sentence.as_bytes();
        let n = b.len();
        if b[0] != b[n - 1] {
            return false;
        }
        for i in 0..n {
            if b[i] == b' ' && b[i - 1] != b[i + 1] {
                return false;
            }
        }
        true
    }
}
'''

def main():
    n = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(content)
        n += 1
        print(f"wrote {folder}")
    print(f"total {n}")

if __name__ == "__main__":
    main()
