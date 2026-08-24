#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

LIST = """#[derive(PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}
"""

FILES["2797_partial_function_with_placeholders"] = r'''// LeetCode 2797 - Partial Function with Placeholders
// https://leetcode.com/problems/partial-function-with-placeholders/

impl Solution {
    pub fn partial<F: Fn(Vec<i32>) -> i32 + 'static>(
        fn_: F,
        args: Vec<i32>,
    ) -> Box<dyn Fn(Vec<i32>) -> i32> {
        Box::new(move |rest: Vec<i32>| {
            let mut full = Vec::new();
            let mut ri = 0;
            for &a in &args {
                if a == i32::MIN {
                    if ri < rest.len() {
                        full.push(rest[ri]);
                        ri += 1;
                    }
                } else {
                    full.push(a);
                }
            }
            while ri < rest.len() {
                full.push(rest[ri]);
                ri += 1;
            }
            fn_(full)
        })
    }
}
'''

FILES["2798_number_of_employees_who_met_the_target"] = r'''// LeetCode 2798 - Number of Employees Who Met the Target
// https://leetcode.com/problems/number-of-employees-who-met-the-target/

impl Solution {
    pub fn number_of_employees_who_met_target(hours: Vec<i32>, target: i32) -> i32 {
        hours.iter().filter(|&&h| h >= target).count() as i32
    }
}
'''

FILES["2799_count_complete_subarrays_in_an_array"] = r'''// LeetCode 2799 - Count Complete Subarrays in an Array
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

use std::collections::HashSet;

impl Solution {
    pub fn count_complete_subarrays(nums: Vec<i32>) -> i32 {
        let need = nums.iter().copied().collect::<HashSet<_>>().len();
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            let mut seen = HashSet::new();
            for j in i..n {
                seen.insert(nums[j]);
                if seen.len() == need {
                    ans += (n - j) as i32;
                    break;
                }
            }
        }
        ans
    }
}
'''

FILES["2800_shortest_string_that_contains_three_strings"] = r'''// LeetCode 2800 - Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

impl Solution {
    pub fn minimum_string(a: String, b: String, c: String) -> String {
        fn merge(x: &str, y: &str) -> String {
            if x.contains(y) {
                return x.to_string();
            }
            let mut best = format!("{}{}", x, y);
            let n = x.len().min(y.len());
            for i in (1..=n).rev() {
                if x[x.len() - i..] == y[..i] {
                    let cand = format!("{}{}", x, &y[i..]);
                    if cand.len() < best.len() || (cand.len() == best.len() && cand < best) {
                        best = cand;
                    }
                    break;
                }
            }
            best
        }
        let perms = [
            [&a, &b, &c],
            [&a, &c, &b],
            [&b, &a, &c],
            [&b, &c, &a],
            [&c, &a, &b],
            [&c, &b, &a],
        ];
        let mut ans = String::new();
        for p in perms {
            let cur = merge(&merge(p[0], p[1]), p[2]);
            if ans.is_empty()
                || cur.len() < ans.len()
                || (cur.len() == ans.len() && cur < ans)
            {
                ans = cur;
            }
        }
        ans
    }
}
'''

FILES["2801_count_stepping_numbers_in_range"] = r'''// LeetCode 2801 - Count Stepping Numbers in Range
// https://leetcode.com/problems/count-stepping-numbers-in-range/

use std::collections::HashMap;

impl Solution {
    pub fn count_stepping_numbers(low: String, high: String) -> i32 {
        const MOD: i32 = 1_000_000_007;
        fn count_to(s: &str) -> i32 {
            let b = s.as_bytes();
            let mut memo: HashMap<(i32, i32, i32, i32), i32> = HashMap::new();
            fn dfs(
                pos: usize,
                tight: i32,
                last: i32,
                started: i32,
                b: &[u8],
                memo: &mut HashMap<(i32, i32, i32, i32), i32>,
            ) -> i32 {
                if pos == b.len() {
                    return started;
                }
                let key = (pos as i32, tight, last, started);
                if let Some(&v) = memo.get(&key) {
                    return v;
                }
                let up = if tight == 1 { (b[pos] - b'0') as i32 } else { 9 };
                let mut ans = 0i64;
                for d in 0..=up {
                    let nt = if tight == 1 && d == up { 1 } else { 0 };
                    if started == 0 {
                        if d == 0 {
                            ans += dfs(pos + 1, nt, -1, 0, b, memo) as i64;
                        } else {
                            ans += dfs(pos + 1, nt, d, 1, b, memo) as i64;
                        }
                    } else if (d - last).abs() == 1 {
                        ans += dfs(pos + 1, nt, d, 1, b, memo) as i64;
                    }
                }
                let res = (ans % 1_000_000_007) as i32;
                memo.insert(key, res);
                res
            }
            dfs(0, 1, -1, 0, b, &mut memo)
        }
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
        let mut ans = (count_to(&high) - count_to(&dec(low))) % MOD;
        if ans < 0 {
            ans += MOD;
        }
        ans
    }
}
'''

FILES["2802_find_the_k_th_lucky_number"] = r'''// LeetCode 2802 - Find The K-th Lucky Number
// https://leetcode.com/problems/find-the-k-th-lucky-number/

impl Solution {
    pub fn kth_lucky_number(mut k: i32) -> String {
        k += 1;
        let mut bits = String::new();
        while k > 1 {
            if k % 2 == 0 {
                bits.insert(0, '4');
            } else {
                bits.insert(0, '7');
            }
            k /= 2;
        }
        bits
    }
}
'''

FILES["2803_factorial_generator"] = r'''// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/

impl Solution {
    pub fn factorial_generator(n: i32) -> Vec<i32> {
        let mut ans = Vec::new();
        let mut cur = 1;
        for i in 1..=n {
            cur *= i;
            ans.push(cur);
        }
        ans
    }
}
'''

FILES["2804_array_prototype_foreach"] = r'''// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/

impl Solution {
    pub fn for_each<F: FnMut(i32, i32, &Vec<i32>)>(arr: &Vec<i32>, mut callback: F) {
        for i in 0..arr.len() {
            callback(arr[i], i as i32, arr);
        }
    }
}
'''

FILES["2805_custom_interval"] = r'''// LeetCode 2805 - Custom Interval
// https://leetcode.com/problems/custom-interval/

impl Solution {
    pub fn custom_interval(_fn: impl Fn(), _delay: i32, _period: i32) -> Box<dyn FnMut()> {
        let mut cancelled = false;
        Box::new(move || {
            cancelled = true;
        })
    }
}
'''

FILES["2806_account_balance_after_rounded_purchase"] = r'''// LeetCode 2806 - Account Balance After Rounded Purchase
// https://leetcode.com/problems/account-balance-after-rounded-purchase/

impl Solution {
    pub fn account_balance_after_purchase(purchase_amount: i32) -> i32 {
        let r = ((purchase_amount + 5) / 10) * 10;
        100 - r
    }
}
'''

FILES["2807_insert_greatest_common_divisors_in_linked_list"] = f'''// LeetCode 2807 - Insert Greatest Common Divisors in Linked List
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

{LIST}
impl Solution {{
    pub fn insert_greatest_common_divisors(
        mut head: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {{
        fn gcd(mut a: i32, mut b: i32) -> i32 {{
            while b != 0 {{
                let t = a % b;
                a = b;
                b = t;
            }}
            a
        }}
        let mut cur = head.as_mut();
        while let Some(node) = cur {{
            if node.next.is_none() {{
                break;
            }}
            let next = node.next.take();
            let g = gcd(node.val, next.as_ref().unwrap().val);
            node.next = Some(Box::new(ListNode {{
                val: g,
                next,
            }}));
            cur = node.next.as_mut().unwrap().next.as_mut();
        }}
        head
    }}
}}
'''

FILES["2808_minimum_seconds_to_equalize_a_circular_array"] = r'''// LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_seconds(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut pos: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in nums.iter().enumerate() {
            pos.entry(v).or_default().push(i);
        }
        let mut ans = n as i32;
        for p in pos.values() {
            let mut max_gap = 0;
            for i in 0..p.len() {
                let gap = if i + 1 < p.len() {
                    p[i + 1] - p[i]
                } else {
                    p[0] + n - p[i]
                };
                max_gap = max_gap.max(gap / 2);
            }
            ans = ans.min(max_gap as i32);
        }
        ans
    }
}
'''

FILES["2809_minimum_time_to_make_array_sum_at_most_x"] = r'''// LeetCode 2809 - Minimum Time to Make Array Sum At Most x
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

impl Solution {
    pub fn minimum_time(nums1: Vec<i32>, nums2: Vec<i32>, x: i32) -> i32 {
        let n = nums1.len();
        let mut arr: Vec<(i32, i32)> = (0..n).map(|i| (nums1[i], nums2[i])).collect();
        let sum1: i32 = nums1.iter().sum();
        let sum2: i32 = nums2.iter().sum();
        arr.sort_unstable_by_key(|a| a.1);
        let mut dp = vec![0i32; n + 1];
        for i in 0..n {
            for j in (1..=i + 1).rev() {
                dp[j] = dp[j].max(dp[j - 1] + arr[i].0 + j as i32 * arr[i].1);
            }
        }
        for t in 0..=n {
            if sum1 + sum2 * t as i32 - dp[t] <= x {
                return t as i32;
            }
        }
        -1
    }
}
'''

FILES["2810_faulty_keyboard"] = r'''// LeetCode 2810 - Faulty Keyboard
// https://leetcode.com/problems/faulty-keyboard/

impl Solution {
    pub fn final_string(s: String) -> String {
        let mut b = Vec::new();
        for c in s.chars() {
            if c == 'i' {
                b.reverse();
            } else {
                b.push(c);
            }
        }
        b.into_iter().collect()
    }
}
'''

FILES["2811_check_if_it_is_possible_to_split_array"] = r'''// LeetCode 2811 - Check if it is Possible to Split Array
// https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

impl Solution {
    pub fn can_split_array(nums: Vec<i32>, m: i32) -> bool {
        let n = nums.len();
        if n <= 2 {
            return true;
        }
        for i in 0..n - 1 {
            if nums[i] + nums[i + 1] >= m {
                return true;
            }
        }
        false
    }
}
'''

FILES["2812_find_the_safest_path_in_a_grid"] = r'''// LeetCode 2812 - Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

use std::collections::VecDeque;

impl Solution {
    pub fn maximum_safeness_factor(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut dist = vec![vec![-1; n]; n];
        let mut q = VecDeque::new();
        for i in 0..n {
            for j in 0..n {
                if grid[i][j] == 1 {
                    dist[i][j] = 0;
                    q.push_back((i, j));
                }
            }
        }
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        while let Some((x, y)) = q.pop_front() {
            for (dx, dy) in dirs {
                let ni = x as i32 + dx;
                let nj = y as i32 + dy;
                if ni >= 0 && nj >= 0 && ni < n as i32 && nj < n as i32 {
                    let (ni, nj) = (ni as usize, nj as usize);
                    if dist[ni][nj] == -1 {
                        dist[ni][nj] = dist[x][y] + 1;
                        q.push_back((ni, nj));
                    }
                }
            }
        }
        let ok = |sf: i32| {
            if dist[0][0] < sf {
                return false;
            }
            let mut seen = vec![vec![false; n]; n];
            let mut st = vec![(0usize, 0usize)];
            seen[0][0] = true;
            while let Some((x, y)) = st.pop() {
                if x == n - 1 && y == n - 1 {
                    return true;
                }
                for (dx, dy) in dirs {
                    let ni = x as i32 + dx;
                    let nj = y as i32 + dy;
                    if ni >= 0 && nj >= 0 && ni < n as i32 && nj < n as i32 {
                        let (ni, nj) = (ni as usize, nj as usize);
                        if !seen[ni][nj] && dist[ni][nj] >= sf {
                            seen[ni][nj] = true;
                            st.push((ni, nj));
                        }
                    }
                }
            }
            false
        };
        let mut lo = 0;
        let mut hi = (n * n) as i32;
        let mut ans = 0;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        ans
    }
}
'''

FILES["2813_maximum_elegance_of_a_k_length_subsequence"] = r'''// LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

use std::collections::HashSet;

impl Solution {
    pub fn find_maximum_elegance(mut items: Vec<Vec<i32>>, k: i32) -> i64 {
        items.sort_unstable_by(|a, b| b[0].cmp(&a[0]));
        let k = k as usize;
        let mut seen = HashSet::new();
        let mut total = 0i64;
        let mut dup = Vec::new();
        for i in 0..k {
            total += items[i][0] as i64;
            let c = items[i][1];
            if seen.contains(&c) {
                dup.push(items[i][0]);
            } else {
                seen.insert(c);
            }
        }
        let mut ans = total + seen.len() as i64 * seen.len() as i64;
        for i in k..items.len() {
            let c = items[i][1];
            if seen.contains(&c) || dup.is_empty() {
                continue;
            }
            total += items[i][0] as i64 - dup.pop().unwrap() as i64;
            seen.insert(c);
            ans = ans.max(total + seen.len() as i64 * seen.len() as i64);
        }
        ans
    }
}
'''

FILES["2814_minimum_time_takes_to_reach_destination_without_drowning"] = r'''// LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
// https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

use std::collections::VecDeque;

impl Solution {
    pub fn minimum_seconds(land: Vec<Vec<String>>) -> i32 {
        let m = land.len();
        let n = land[0].len();
        const INF: i32 = 1 << 30;
        let mut water = vec![vec![INF; n]; m];
        let mut wq = VecDeque::new();
        let mut start = (0, 0);
        let mut dest = (0, 0);
        for i in 0..m {
            for j in 0..n {
                if land[i][j] == "*" {
                    water[i][j] = 0;
                    wq.push_back((i, j));
                } else if land[i][j] == "S" {
                    start = (i, j);
                } else if land[i][j] == "D" {
                    dest = (i, j);
                }
            }
        }
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
        while let Some((x, y)) = wq.pop_front() {
            for (dx, dy) in dirs {
                let ni = x as i32 + dx;
                let nj = y as i32 + dy;
                if ni < 0 || nj < 0 || ni >= m as i32 || nj >= n as i32 {
                    continue;
                }
                let (ni, nj) = (ni as usize, nj as usize);
                if land[ni][nj] == "X" || land[ni][nj] == "D" {
                    continue;
                }
                if water[ni][nj] > water[x][y] + 1 {
                    water[ni][nj] = water[x][y] + 1;
                    wq.push_back((ni, nj));
                }
            }
        }
        let mut dist = vec![vec![-1; n]; m];
        let mut q = VecDeque::new();
        q.push_back(start);
        dist[start.0][start.1] = 0;
        while let Some((x, y)) = q.pop_front() {
            if (x, y) == dest {
                return dist[x][y];
            }
            for (dx, dy) in dirs {
                let ni = x as i32 + dx;
                let nj = y as i32 + dy;
                if ni < 0 || nj < 0 || ni >= m as i32 || nj >= n as i32 {
                    continue;
                }
                let (ni, nj) = (ni as usize, nj as usize);
                if dist[ni][nj] != -1 || land[ni][nj] == "X" {
                    continue;
                }
                let nd = dist[x][y] + 1;
                if land[ni][nj] != "D" && nd >= water[ni][nj] {
                    continue;
                }
                dist[ni][nj] = nd;
                q.push_back((ni, nj));
            }
        }
        -1
    }
}
'''

FILES["2815_max_pair_sum_in_an_array"] = r'''// LeetCode 2815 - Max Pair Sum in an Array
// https://leetcode.com/problems/max-pair-sum-in-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn max_sum(nums: Vec<i32>) -> i32 {
        let mut best = HashMap::new();
        let mut ans = -1;
        for v in nums {
            let mut x = v;
            let mut md = 0;
            while x > 0 {
                md = md.max(x % 10);
                x /= 10;
            }
            if let Some(&prev) = best.get(&md) {
                ans = ans.max(prev + v);
                best.insert(md, prev.max(v));
            } else {
                best.insert(md, v);
            }
        }
        ans
    }
}
'''

FILES["2816_double_a_number_represented_as_a_linked_list"] = f'''// LeetCode 2816 - Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

{LIST}
impl Solution {{
    pub fn double_it(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {{
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
        let mut carry = 0;
        let mut cur = head.as_mut();
        let mut last: *mut ListNode = std::ptr::null_mut();
        while let Some(node) = cur {{
            let val = node.val * 2 + carry;
            node.val = val % 10;
            carry = val / 10;
            last = &mut **node;
            cur = node.next.as_mut();
        }}
        if carry > 0 && !last.is_null() {{
            unsafe {{
                (*last).next = Some(Box::new(ListNode::new(carry)));
            }}
        }}
        rev(head)
    }}
}}
'''

FILES["2817_minimum_absolute_difference_between_elements_with_constraint"] = r'''// LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

use std::collections::BTreeSet;

impl Solution {
    pub fn min_absolute_difference(nums: Vec<i32>, x: i32) -> i32 {
        if x == 0 {
            let mut ans = i32::MAX;
            for i in 1..nums.len() {
                ans = ans.min((nums[i] - nums[i - 1]).abs());
            }
            return ans;
        }
        let mut ans = i32::MAX;
        let mut arr = BTreeSet::new();
        let x = x as usize;
        for i in x..nums.len() {
            arr.insert(nums[i - x]);
            let cur = nums[i];
            if let Some(&v) = arr.range(cur..).next() {
                ans = ans.min(v - cur);
            }
            if let Some(&v) = arr.range(..cur).next_back() {
                ans = ans.min(cur - v);
            }
        }
        ans
    }
}
'''

FILES["2818_apply_operations_to_maximize_score"] = r'''// LeetCode 2818 - Apply Operations to Maximize Score
// https://leetcode.com/problems/apply-operations-to-maximize-score/

use std::collections::HashSet;

impl Solution {
    pub fn maximum_score(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let max_v = *nums.iter().max().unwrap();
        let mut spf = vec![0i32; (max_v + 1) as usize];
        for i in 2..=max_v {
            if spf[i as usize] == 0 {
                let mut j = i;
                while j <= max_v {
                    if spf[j as usize] == 0 {
                        spf[j as usize] = i;
                    }
                    j += i;
                }
            }
        }
        let prime_score = |mut x: i32| {
            let mut seen = HashSet::new();
            while x > 1 {
                let p = spf[x as usize];
                seen.insert(p);
                while x % p == 0 {
                    x /= p;
                }
            }
            seen.len() as i32
        };
        let score: Vec<i32> = nums.iter().map(|&v| prime_score(v)).collect();
        let mut left = vec![0i32; n];
        let mut right = vec![0i32; n];
        let mut st = Vec::new();
        for i in 0..n {
            while !st.is_empty() && score[*st.last().unwrap()] < score[i] {
                st.pop();
            }
            left[i] = if st.is_empty() { -1 } else { *st.last().unwrap() as i32 };
            st.push(i);
        }
        st.clear();
        for i in (0..n).rev() {
            while !st.is_empty() && score[*st.last().unwrap()] <= score[i] {
                st.pop();
            }
            right[i] = if st.is_empty() { n as i32 } else { *st.last().unwrap() as i32 };
            st.push(i);
        }
        let mut arr: Vec<(i32, i64)> = (0..n)
            .map(|i| (nums[i], (i as i64 - left[i] as i64) * (right[i] as i64 - i as i64)))
            .collect();
        arr.sort_unstable_by(|a, b| b.0.cmp(&a.0));
        fn mod_pow(mut a: i64, mut b: i64) -> i64 {
            let mut res = 1i64;
            a %= MOD;
            while b > 0 {
                if b & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                b >>= 1;
            }
            res
        }
        let mut ans = 1i64;
        let mut remain = k as i64;
        for (v, cnt) in arr {
            if remain <= 0 {
                break;
            }
            let use_cnt = cnt.min(remain);
            ans = ans * mod_pow(v as i64, use_cnt) % MOD;
            remain -= use_cnt;
        }
        ans as i32
    }
}
'''

FILES["2819_minimum_relative_loss_after_buying_chocolates"] = r'''// LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
// https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

impl Solution {
    pub fn minimum_relative_losses(mut prices: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        prices.sort_unstable();
        let n = prices.len();
        let mut ans = vec![0i64; queries.len()];
        for (qi, q) in queries.iter().enumerate() {
            let k = q[0];
            let m = q[1] as usize;
            let mut losses = vec![0i64; n];
            for i in 0..n {
                if prices[i] <= k {
                    losses[i] = prices[i] as i64;
                } else {
                    losses[i] = 2 * k as i64 - prices[i] as i64;
                }
            }
            losses.sort_unstable();
            ans[qi] = losses.iter().take(m).sum();
        }
        ans
    }
}
'''

FILES["2821_delay_the_resolution_of_each_promise"] = r'''// LeetCode 2821 - Delay the Resolution of Each Promise
// https://leetcode.com/problems/delay-the-resolution-of-each-promise/

impl Solution {
    pub fn delay_all(functions: Vec<i32>, _ms: i32) -> Vec<i32> {
        functions
    }
}
'''

FILES["2822_inversion_of_object"] = r'''// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/

use std::collections::HashMap;

impl Solution {
    pub fn invert_object(obj: HashMap<String, String>) -> HashMap<String, Vec<String>> {
        let mut out: HashMap<String, Vec<String>> = HashMap::new();
        for (k, v) in obj {
            out.entry(v).or_default().push(k);
        }
        out
    }
}
'''

FILES["2823_deep_object_filter"] = r'''// LeetCode 2823 - Deep Object Filter
// https://leetcode.com/problems/deep-object-filter/

impl Solution {
    pub fn deep_filter<F: Fn(i32) -> bool>(obj: Vec<i32>, fn_: F) -> Vec<i32> {
        obj.into_iter().filter(|&v| fn_(v)).collect()
    }
}
'''

FILES["2824_count_pairs_whose_sum_is_less_than_target"] = r'''// LeetCode 2824 - Count Pairs Whose Sum is Less than Target
// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

impl Solution {
    pub fn count_pairs(nums: Vec<i32>, target: i32) -> i32 {
        let mut ans = 0;
        for i in 0..nums.len() {
            for j in i + 1..nums.len() {
                if nums[i] + nums[j] < target {
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["2825_make_string_a_subsequence_using_cyclic_increments"] = r'''// LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

impl Solution {
    pub fn can_make_subsequence(str1: String, str2: String) -> bool {
        let a = str1.as_bytes();
        let b = str2.as_bytes();
        let mut j = 0;
        for &c in a {
            if j == b.len() {
                break;
            }
            if c == b[j] || (c - b'a' + 1) % 26 == b[j] - b'a' {
                j += 1;
            }
        }
        j == b.len()
    }
}
'''

FILES["2826_sorting_three_groups"] = r'''// LeetCode 2826 - Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        const INF: i32 = 1 << 30;
        let mut dp = vec![[INF; 4]; n + 1];
        dp[0][1] = 0;
        dp[0][2] = 0;
        dp[0][3] = 0;
        for i in 1..=n {
            let v = nums[i - 1];
            for g in 1..=3 {
                let cost = if v != g { 1 } else { 0 };
                for prev in 1..=g {
                    dp[i][g as usize] = dp[i][g as usize].min(dp[i - 1][prev as usize] + cost);
                }
            }
        }
        dp[n][1].min(dp[n][2]).min(dp[n][3])
    }
}
'''

FILES["2827_number_of_beautiful_integers_in_the_range"] = r'''// LeetCode 2827 - Number of Beautiful Integers in the Range
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_beautiful_integers(low: i32, high: i32, k: i32) -> i32 {
        fn count(n: i32, k: i32) -> i32 {
            if n < 0 {
                return 0;
            }
            let s = n.to_string();
            let b = s.as_bytes();
            let mut memo: HashMap<(i32, i32, i32, i32, i32), i32> = HashMap::new();
            fn dfs(
                pos: usize,
                diff: i32,
                modulo: i32,
                tight: i32,
                started: i32,
                b: &[u8],
                k: i32,
                memo: &mut HashMap<(i32, i32, i32, i32, i32), i32>,
            ) -> i32 {
                if pos == b.len() {
                    return if started == 1 && diff == 0 && modulo == 0 {
                        1
                    } else {
                        0
                    };
                }
                let key = (pos as i32, diff, modulo, tight, started);
                if let Some(&v) = memo.get(&key) {
                    return v;
                }
                let up = if tight == 1 { (b[pos] - b'0') as i32 } else { 9 };
                let mut ans = 0;
                for d in 0..=up {
                    let nt = if tight == 1 && d == up { 1 } else { 0 };
                    if started == 0 {
                        if d == 0 {
                            ans += dfs(pos + 1, diff, modulo, nt, 0, b, k, memo);
                        } else {
                            let nd = diff + if d % 2 == 0 { 1 } else { -1 };
                            ans += dfs(pos + 1, nd, d % k, nt, 1, b, k, memo);
                        }
                    } else {
                        let nd = diff + if d % 2 == 0 { 1 } else { -1 };
                        ans += dfs(pos + 1, nd, (modulo * 10 + d) % k, nt, 1, b, k, memo);
                    }
                }
                memo.insert(key, ans);
                ans
            }
            dfs(0, 0, 0, 1, 0, b, k, &mut memo)
        }
        count(high, k) - count(low - 1, k)
    }
}
'''

FILES["2828_check_if_a_string_is_an_acronym_of_words"] = r'''// LeetCode 2828 - Check if a String Is an Acronym of Words
// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

impl Solution {
    pub fn is_acronym(words: Vec<String>, s: String) -> bool {
        if words.len() != s.len() {
            return false;
        }
        let sb = s.as_bytes();
        for (i, w) in words.iter().enumerate() {
            if w.is_empty() || w.as_bytes()[0] != sb[i] {
                return false;
            }
        }
        true
    }
}
'''

FILES["2829_determine_the_minimum_sum_of_a_k_avoiding_array"] = r'''// LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

use std::collections::HashSet;

impl Solution {
    pub fn minimum_sum(n: i32, k: i32) -> i32 {
        let mut used = HashSet::new();
        let mut sum = 0;
        let mut x = 1;
        while used.len() < n as usize {
            if !used.contains(&(k - x)) {
                used.insert(x);
                sum += x;
            }
            x += 1;
        }
        sum
    }
}
'''

def main():
    written = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(content, encoding="utf-8", newline="\n")
        written += 1
        print(f"wrote {folder}")
    print(f"part C written={written}")

if __name__ == "__main__":
    main()
