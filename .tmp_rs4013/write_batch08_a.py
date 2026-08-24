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

FILES["2414_length_of_the_longest_alphabetical_continuous_substring"] = r'''// LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

impl Solution {
    pub fn longest_continuous_substring(s: String) -> i32 {
        let b = s.as_bytes();
        let mut ans = 1;
        let mut cur = 1;
        for i in 1..b.len() {
            if b[i] == b[i - 1] + 1 {
                cur += 1;
                ans = ans.max(cur);
            } else {
                cur = 1;
            }
        }
        ans
    }
}
'''

FILES["2415_reverse_odd_levels_of_binary_tree"] = f'''// LeetCode 2415 - Reverse Odd Levels of Binary Tree
// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

{TREE}
impl Solution {{
    pub fn reverse_odd_levels(
        root: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {{
        fn dfs(
            a: Option<Rc<RefCell<TreeNode>>>,
            b: Option<Rc<RefCell<TreeNode>>>,
            level: i32,
        ) {{
            let (Some(a), Some(b)) = (a, b) else {{
                return;
            }};
            if level % 2 == 1 {{
                let mut aa = a.borrow_mut();
                let mut bb = b.borrow_mut();
                std::mem::swap(&mut aa.val, &mut bb.val);
            }}
            let (al, ar) = {{
                let n = a.borrow();
                (n.left.clone(), n.right.clone())
            }};
            let (bl, br) = {{
                let n = b.borrow();
                (n.left.clone(), n.right.clone())
            }};
            dfs(al, br, level + 1);
            dfs(ar, bl, level + 1);
        }}
        if let Some(r) = &root {{
            let (l, ri) = {{
                let n = r.borrow();
                (n.left.clone(), n.right.clone())
            }};
            dfs(l, ri, 1);
        }}
        root
    }}
}}
'''

FILES["2416_sum_of_prefix_scores_of_strings"] = r'''// LeetCode 2416 - Sum of Prefix Scores of Strings
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

impl Solution {
    pub fn sum_prefix_scores(words: Vec<String>) -> Vec<i32> {
        struct TrieNode {
            child: [Option<Box<TrieNode>>; 26],
            cnt: i32,
        }
        impl TrieNode {
            fn new() -> Self {
                Self {
                    child: Default::default(),
                    cnt: 0,
                }
            }
        }
        let mut root = TrieNode::new();
        for w in &words {
            let mut cur = &mut root;
            for &ch in w.as_bytes() {
                let c = (ch - b'a') as usize;
                if cur.child[c].is_none() {
                    cur.child[c] = Some(Box::new(TrieNode::new()));
                }
                cur = cur.child[c].as_mut().unwrap();
                cur.cnt += 1;
            }
        }
        let mut ans = vec![0; words.len()];
        for (i, w) in words.iter().enumerate() {
            let mut cur = &root;
            let mut sum = 0;
            for &ch in w.as_bytes() {
                cur = cur.child[(ch - b'a') as usize].as_ref().unwrap();
                sum += cur.cnt;
            }
            ans[i] = sum;
        }
        ans
    }
}
'''

FILES["2417_closest_fair_integer"] = r'''// LeetCode 2417 - Closest Fair Integer
// https://leetcode.com/problems/closest-fair-integer/

impl Solution {
    pub fn closest_fair(n: i32) -> i32 {
        let mut x = n;
        loop {
            let s = x.to_string();
            if s.len() % 2 != 0 {
                let mut p = 1i32;
                for _ in 0..s.len() {
                    p *= 10;
                }
                return Self::closest_fair(p);
            }
            let mut even = 0;
            let mut odd = 0;
            for c in s.bytes() {
                if (c - b'0') % 2 == 0 {
                    even += 1;
                } else {
                    odd += 1;
                }
            }
            if even == odd {
                return x;
            }
            x += 1;
        }
    }
}
'''

FILES["2418_sort_the_people"] = r'''// LeetCode 2418 - Sort the People
// https://leetcode.com/problems/sort-the-people/

impl Solution {
    pub fn sort_people(names: Vec<String>, heights: Vec<i32>) -> Vec<String> {
        let n = names.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by(|&a, &b| heights[b].cmp(&heights[a]));
        idx.into_iter().map(|i| names[i].clone()).collect()
    }
}
'''

FILES["2419_longest_subarray_with_maximum_bitwise_and"] = r'''// LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let mx = *nums.iter().max().unwrap();
        let mut ans = 0;
        let mut cur = 0;
        for x in nums {
            if x == mx {
                cur += 1;
                ans = ans.max(cur);
            } else {
                cur = 0;
            }
        }
        ans
    }
}
'''

FILES["2420_find_all_good_indices"] = r'''// LeetCode 2420 - Find All Good Indices
// https://leetcode.com/problems/find-all-good-indices/

impl Solution {
    pub fn good_indices(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        let mut dec = vec![0; n];
        let mut inc = vec![0; n];
        dec[0] = 1;
        for i in 1..n {
            dec[i] = if nums[i] <= nums[i - 1] {
                dec[i - 1] + 1
            } else {
                1
            };
        }
        inc[n - 1] = 1;
        for i in (0..n - 1).rev() {
            inc[i] = if nums[i] <= nums[i + 1] {
                inc[i + 1] + 1
            } else {
                1
            };
        }
        let mut ans = Vec::new();
        if n > 2 * k {
            for i in k..n - k {
                if dec[i - 1] >= k && inc[i + 1] >= k {
                    ans.push(i as i32);
                }
            }
        }
        ans
    }
}
'''

FILES["2421_number_of_good_paths"] = r'''// LeetCode 2421 - Number of Good Paths
// https://leetcode.com/problems/number-of-good-paths/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_good_paths(vals: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = vals.len();
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        let mut parent: Vec<usize> = (0..n).collect();
        let mut size = vec![1i32; n];
        fn find(parent: &mut [usize], x: usize) -> usize {
            if parent[x] != x {
                parent[x] = find(parent, parent[x]);
            }
            parent[x]
        }
        let mut nodes: Vec<usize> = (0..n).collect();
        nodes.sort_by_key(|&i| vals[i]);
        let mut ans = n as i32;
        let mut i = 0;
        while i < n {
            let mut j = i;
            while j < n && vals[nodes[j]] == vals[nodes[i]] {
                j += 1;
            }
            for k in i..j {
                let u = nodes[k];
                for &v in &g[u] {
                    if vals[v] <= vals[u] {
                        let ru = find(&mut parent, u);
                        let rv = find(&mut parent, v);
                        if ru != rv {
                            parent[ru] = rv;
                            size[rv] += size[ru];
                        }
                    }
                }
            }
            let mut freq: HashMap<usize, i32> = HashMap::new();
            for k in i..j {
                let r = find(&mut parent, nodes[k]);
                *freq.entry(r).or_insert(0) += 1;
            }
            for &c in freq.values() {
                ans += c * (c - 1) / 2;
            }
            i = j;
        }
        ans
    }
}
'''

FILES["2422_merge_operations_to_turn_array_into_a_palindrome"] = r'''// LeetCode 2422 - Merge Operations to Turn Array Into a Palindrome
// https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut l = 0usize;
        let mut r = nums.len() - 1;
        let mut left = nums[l] as i64;
        let mut right = nums[r] as i64;
        let mut ans = 0;
        while l < r {
            if left == right {
                l += 1;
                r -= 1;
                if l < r {
                    left = nums[l] as i64;
                    right = nums[r] as i64;
                }
            } else if left < right {
                l += 1;
                left += nums[l] as i64;
                ans += 1;
            } else {
                r -= 1;
                right += nums[r] as i64;
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2423_remove_letter_to_equalize_frequency"] = r'''// LeetCode 2423 - Remove Letter To Equalize Frequency
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

use std::collections::HashMap;

impl Solution {
    pub fn equal_frequency(word: String) -> bool {
        let b = word.as_bytes();
        for skip in 0..b.len() {
            let mut cnt = [0i32; 26];
            for (i, &ch) in b.iter().enumerate() {
                if i == skip {
                    continue;
                }
                cnt[(ch - b'a') as usize] += 1;
            }
            let mut freq: HashMap<i32, i32> = HashMap::new();
            for c in cnt {
                if c > 0 {
                    *freq.entry(c).or_insert(0) += 1;
                }
            }
            if freq.len() == 1 {
                return true;
            }
        }
        false
    }
}
'''

FILES["2424_longest_uploaded_prefix"] = r'''// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

pub struct LUPrefix {
    uploaded: Vec<bool>,
    prefix_len: i32,
}

impl LUPrefix {
    pub fn new(n: i32) -> Self {
        Self {
            uploaded: vec![false; (n + 2) as usize],
            prefix_len: 0,
        }
    }

    pub fn upload(&mut self, video: i32) {
        self.uploaded[video as usize] = true;
        while self.uploaded[(self.prefix_len + 1) as usize] {
            self.prefix_len += 1;
        }
    }

    pub fn longest(&self) -> i32 {
        self.prefix_len
    }
}
'''

FILES["2425_bitwise_xor_of_all_pairings"] = r'''// LeetCode 2425 - Bitwise XOR of All Pairings
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

impl Solution {
    pub fn xor_all_nums(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut ans = 0;
        if nums2.len() % 2 == 1 {
            for x in nums1 {
                ans ^= x;
            }
        }
        if nums1.len() % 2 == 1 {
            for x in &nums2 {
                ans ^= x;
            }
        }
        ans
    }
}
'''

# Fix 2425 - after first loop nums1 is moved. Need to not consume nums1 if we need its length later.
# I used nums1.len() after moving nums1 - that's a bug. Let me fix in the write.

FILES["2425_bitwise_xor_of_all_pairings"] = r'''// LeetCode 2425 - Bitwise XOR of All Pairings
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

impl Solution {
    pub fn xor_all_nums(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut ans = 0;
        if nums2.len() % 2 == 1 {
            for &x in &nums1 {
                ans ^= x;
            }
        }
        if nums1.len() % 2 == 1 {
            for x in nums2 {
                ans ^= x;
            }
        }
        ans
    }
}
'''

FILES["2426_number_of_pairs_satisfying_inequality"] = r'''// LeetCode 2426 - Number of Pairs Satisfying Inequality
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, nums2: Vec<i32>, diff: i32) -> i64 {
        let n = nums1.len();
        let mut arr: Vec<i32> = (0..n).map(|i| nums1[i] - nums2[i]).collect();
        let mut tmp = vec![0; n];
        fn merge_count(arr: &mut [i32], tmp: &mut [i32], l: usize, r: usize, diff: i32) -> i64 {
            if r - l <= 1 {
                return 0;
            }
            let m = (l + r) / 2;
            let mut ans = merge_count(arr, tmp, l, m, diff) + merge_count(arr, tmp, m, r, diff);
            let mut j = m;
            for i in l..m {
                while j < r && arr[j] < arr[i] - diff {
                    j += 1;
                }
                ans += (r - j) as i64;
            }
            let mut i = l;
            let mut p = l;
            let mut q = m;
            while p < m && q < r {
                if arr[p] <= arr[q] {
                    tmp[i] = arr[p];
                    i += 1;
                    p += 1;
                } else {
                    tmp[i] = arr[q];
                    i += 1;
                    q += 1;
                }
            }
            while p < m {
                tmp[i] = arr[p];
                i += 1;
                p += 1;
            }
            while q < r {
                tmp[i] = arr[q];
                i += 1;
                q += 1;
            }
            for t in l..r {
                arr[t] = tmp[t];
            }
            ans
        }
        merge_count(&mut arr, &mut tmp, 0, n, diff)
    }
}
'''

FILES["2427_number_of_common_factors"] = r'''// LeetCode 2427 - Number of Common Factors
// https://leetcode.com/problems/number-of-common-factors/

impl Solution {
    pub fn common_factors(a: i32, b: i32) -> i32 {
        fn gcd(mut x: i32, mut y: i32) -> i32 {
            while y != 0 {
                let t = x % y;
                x = y;
                y = t;
            }
            x
        }
        let g = gcd(a, b);
        let mut ans = 0;
        let mut i = 1;
        while i * i <= g {
            if g % i == 0 {
                ans += 1;
                if i * i != g {
                    ans += 1;
                }
            }
            i += 1;
        }
        ans
    }
}
'''

FILES["2428_maximum_sum_of_an_hourglass"] = r'''// LeetCode 2428 - Maximum Sum of an Hourglass
// https://leetcode.com/problems/maximum-sum-of-an-hourglass/

impl Solution {
    pub fn max_sum(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut ans = 0;
        for i in 0..m.saturating_sub(2) {
            for j in 0..n.saturating_sub(2) {
                let s = grid[i][j]
                    + grid[i][j + 1]
                    + grid[i][j + 2]
                    + grid[i + 1][j + 1]
                    + grid[i + 2][j]
                    + grid[i + 2][j + 1]
                    + grid[i + 2][j + 2];
                ans = ans.max(s);
            }
        }
        ans
    }
}
'''

FILES["2429_minimize_xor"] = r'''// LeetCode 2429 - Minimize XOR
// https://leetcode.com/problems/minimize-xor/

impl Solution {
    pub fn minimize_xor(num1: i32, num2: i32) -> i32 {
        let mut bits = num2.count_ones() as i32;
        let mut ans = 0;
        for i in (0..32).rev() {
            if bits <= 0 {
                break;
            }
            if (num1 >> i) & 1 == 1 {
                ans |= 1 << i;
                bits -= 1;
            }
        }
        for i in 0..32 {
            if bits <= 0 {
                break;
            }
            if (ans >> i) & 1 == 0 {
                ans |= 1 << i;
                bits -= 1;
            }
        }
        ans
    }
}
'''

FILES["2430_maximum_deletions_on_a_string"] = r'''// LeetCode 2430 - Maximum Deletions on a String
// https://leetcode.com/problems/maximum-deletions-on-a-string/

impl Solution {
    pub fn delete_string(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut lcp = vec![vec![0; n + 1]; n + 1];
        for i in (0..n).rev() {
            for j in (0..n).rev() {
                if b[i] == b[j] {
                    lcp[i][j] = lcp[i + 1][j + 1] + 1;
                }
            }
        }
        let mut dp = vec![0; n];
        for i in (0..n).rev() {
            dp[i] = 1;
            let mut len = 1;
            while i + 2 * len <= n {
                if lcp[i][i + len] >= len {
                    dp[i] = dp[i].max(1 + dp[i + len]);
                }
                len += 1;
            }
        }
        dp[0]
    }
}
'''

FILES["2431_maximize_total_tastiness_of_purchased_fruits"] = r'''// LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
// https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

impl Solution {
    pub fn max_tastiness(
        price: Vec<i32>,
        tastiness: Vec<i32>,
        max_amount: i32,
        max_coupons: i32,
    ) -> i32 {
        let n = price.len();
        let max_amount = max_amount as usize;
        let max_coupons = max_coupons as usize;
        let mut dp = vec![vec![i32::MIN / 2; max_coupons + 1]; max_amount + 1];
        dp[0][0] = 0;
        for i in 0..n {
            let p = price[i] as usize;
            let t = tastiness[i];
            for a in (0..=max_amount).rev() {
                for c in (0..=max_coupons).rev() {
                    if dp[a][c] < 0 {
                        continue;
                    }
                    if a + p <= max_amount {
                        dp[a + p][c] = dp[a + p][c].max(dp[a][c] + t);
                    }
                    if c + 1 <= max_coupons && a + p / 2 <= max_amount {
                        dp[a + p / 2][c + 1] = dp[a + p / 2][c + 1].max(dp[a][c] + t);
                    }
                }
            }
        }
        let mut ans = 0;
        for a in 0..=max_amount {
            for c in 0..=max_coupons {
                ans = ans.max(dp[a][c]);
            }
        }
        ans
    }
}
'''

FILES["2432_the_employee_that_worked_on_the_longest_task"] = r'''// LeetCode 2432 - The Employee That Worked on the Longest Task
// https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

impl Solution {
    pub fn hardest_worker(_n: i32, logs: Vec<Vec<i32>>) -> i32 {
        let mut ans = logs[0][0];
        let mut best = logs[0][1];
        let mut prev = 0;
        for log in &logs {
            let dur = log[1] - prev;
            if dur > best || (dur == best && log[0] < ans) {
                best = dur;
                ans = log[0];
            }
            prev = log[1];
        }
        ans
    }
}
'''

FILES["2433_find_the_original_array_of_prefix_xor"] = r'''// LeetCode 2433 - Find The Original Array of Prefix Xor
// https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

impl Solution {
    pub fn find_array(pref: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![0; pref.len()];
        ans[0] = pref[0];
        for i in 1..pref.len() {
            ans[i] = pref[i] ^ pref[i - 1];
        }
        ans
    }
}
'''

FILES["2434_using_a_robot_to_print_the_lexicographically_smallest_string"] = r'''// LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

impl Solution {
    pub fn robot_with_string(s: String) -> String {
        let b = s.as_bytes();
        let n = b.len();
        let mut min_suf = vec![b'z' + 1; n + 1];
        for i in (0..n).rev() {
            min_suf[i] = b[i].min(min_suf[i + 1]);
        }
        let mut stack = Vec::new();
        let mut ans = Vec::new();
        for i in 0..n {
            stack.push(b[i]);
            while !stack.is_empty() && *stack.last().unwrap() <= min_suf[i + 1] {
                ans.push(stack.pop().unwrap());
            }
        }
        while let Some(c) = stack.pop() {
            ans.push(c);
        }
        String::from_utf8(ans).unwrap()
    }
}
'''

FILES["2435_paths_in_matrix_whose_sum_is_divisible_by_k"] = r'''// LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

impl Solution {
    pub fn number_of_paths(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let m = grid.len();
        let n = grid[0].len();
        let k = k as usize;
        let mut dp = vec![vec![vec![0; k]; n]; m];
        dp[0][0][(grid[0][0] as usize) % k] = 1;
        for i in 0..m {
            for j in 0..n {
                for r in 0..k {
                    if dp[i][j][r] == 0 {
                        continue;
                    }
                    if i + 1 < m {
                        let nr = (r + grid[i + 1][j] as usize) % k;
                        dp[i + 1][j][nr] = (dp[i + 1][j][nr] + dp[i][j][r]) % MOD;
                    }
                    if j + 1 < n {
                        let nr = (r + grid[i][j + 1] as usize) % k;
                        dp[i][j + 1][nr] = (dp[i][j + 1][nr] + dp[i][j][r]) % MOD;
                    }
                }
            }
        }
        dp[m - 1][n - 1][0]
    }
}
'''

FILES["2436_minimum_split_into_subarrays_with_gcd_greater_than_one"] = r'''// LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
// https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

impl Solution {
    pub fn minimum_splits(nums: Vec<i32>) -> i32 {
        fn gcd(mut x: i32, mut y: i32) -> i32 {
            while y != 0 {
                let t = x % y;
                x = y;
                y = t;
            }
            x
        }
        let mut ans = 1;
        let mut g = nums[0];
        for i in 1..nums.len() {
            let ng = gcd(g, nums[i]);
            if ng == 1 {
                ans += 1;
                g = nums[i];
            } else {
                g = ng;
            }
        }
        ans
    }
}
'''

FILES["2437_number_of_valid_clock_times"] = r'''// LeetCode 2437 - Number of Valid Clock Times
// https://leetcode.com/problems/number-of-valid-clock-times/

impl Solution {
    pub fn count_time(time: String) -> i32 {
        let t = time.as_bytes();
        let mut ans = 0;
        for h in 0..24 {
            for m in 0..60 {
                let hs = [b'0' + (h / 10) as u8, b'0' + (h % 10) as u8];
                let ms = [b'0' + (m / 10) as u8, b'0' + (m % 10) as u8];
                if t[0] != b'?' && t[0] != hs[0] {
                    continue;
                }
                if t[1] != b'?' && t[1] != hs[1] {
                    continue;
                }
                if t[3] != b'?' && t[3] != ms[0] {
                    continue;
                }
                if t[4] != b'?' && t[4] != ms[1] {
                    continue;
                }
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2438_range_product_queries_of_powers"] = r'''// LeetCode 2438 - Range Product Queries of Powers
// https://leetcode.com/problems/range-product-queries-of-powers/

impl Solution {
    pub fn product_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;
        let mut powers = Vec::new();
        for bit in 0..31 {
            if (n >> bit) & 1 == 1 {
                powers.push(1 << bit);
            }
        }
        let mut ans = vec![0; queries.len()];
        for (i, q) in queries.iter().enumerate() {
            let mut prod = 1i64;
            for j in q[0] as usize..=q[1] as usize {
                prod = prod * powers[j] as i64 % MOD;
            }
            ans[i] = prod as i32;
        }
        ans
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
