#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

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

FILES["2761_prime_pairs_with_target_sum"] = r'''// LeetCode 2761 - Prime Pairs With Target Sum
// https://leetcode.com/problems/prime-pairs-with-target-sum/

impl Solution {
    pub fn find_prime_pairs(n: i32) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut is_prime = vec![false; n + 1];
        for i in 2..=n {
            is_prime[i] = true;
        }
        let mut i = 2;
        while i * i <= n {
            if is_prime[i] {
                let mut j = i * i;
                while j <= n {
                    is_prime[j] = false;
                    j += i;
                }
            }
            i += 1;
        }
        let mut ans = Vec::new();
        for x in 2..=n / 2 {
            let y = n - x;
            if is_prime[x] && is_prime[y] {
                ans.push(vec![x as i32, y as i32]);
            }
        }
        ans
    }
}
'''

FILES["2762_continuous_subarrays"] = r'''// LeetCode 2762 - Continuous Subarrays
// https://leetcode.com/problems/continuous-subarrays/

use std::collections::BTreeMap;

impl Solution {
    pub fn continuous_subarrays(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        let mut left = 0;
        let mut freq: BTreeMap<i32, i32> = BTreeMap::new();
        for right in 0..nums.len() {
            *freq.entry(nums[right]).or_insert(0) += 1;
            while freq.keys().next_back().unwrap() - freq.keys().next().unwrap() > 2 {
                let e = freq.get_mut(&nums[left]).unwrap();
                *e -= 1;
                if *e == 0 {
                    freq.remove(&nums[left]);
                }
                left += 1;
            }
            ans += (right - left + 1) as i64;
        }
        ans
    }
}
'''

FILES["2763_sum_of_imbalance_numbers_of_all_subarrays"] = r'''// LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
// https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

use std::collections::{BTreeSet, HashSet};

impl Solution {
    pub fn sum_imbalance_numbers(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            let mut seen = HashSet::new();
            let mut sorted_vals = BTreeSet::new();
            let mut imbalance = 0;
            for j in i..n {
                let x = nums[j];
                if seen.insert(x) {
                    if let Some(&nxt) = sorted_vals.range(x..).next() {
                        if nxt - x != 1 {
                            imbalance += 1;
                        }
                    }
                    if let Some(&prv) = sorted_vals.range(..x).next_back() {
                        if x - prv != 1 {
                            imbalance += 1;
                        }
                    }
                    if let (Some(&prv), Some(&nxt)) = (
                        sorted_vals.range(..x).next_back(),
                        sorted_vals.range(x..).next(),
                    ) {
                        if nxt - prv > 1 {
                            imbalance -= 1;
                        }
                    }
                    sorted_vals.insert(x);
                }
                ans += imbalance;
            }
        }
        ans
    }
}
'''

FILES["2764_is_array_a_preorder_of_some_binary_tree"] = r'''// LeetCode 2764 - Is Array a Preorder of Some Binary Tree
// https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

impl Solution {
    pub fn is_preorder(nodes: Vec<Vec<i32>>) -> bool {
        if nodes.is_empty() {
            return true;
        }
        let mut stack = vec![nodes[0][0]];
        for node in nodes.iter().skip(1) {
            let id = node[0];
            let parent = node[1];
            while !stack.is_empty() && *stack.last().unwrap() != parent {
                stack.pop();
            }
            if stack.is_empty() {
                return false;
            }
            stack.push(id);
        }
        true
    }
}
'''

FILES["2765_longest_alternating_subarray"] = r'''// LeetCode 2765 - Longest Alternating Subarray
// https://leetcode.com/problems/longest-alternating-subarray/

impl Solution {
    pub fn alternating_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = -1;
        for i in 0..n {
            for j in i + 1..n {
                let expect = if (j - i) % 2 == 0 { -1 } else { 1 };
                if nums[j] - nums[j - 1] != expect {
                    break;
                }
                if nums[i + 1] - nums[i] != 1 {
                    break;
                }
                ans = ans.max((j - i + 1) as i32);
            }
        }
        ans
    }
}
'''

FILES["2766_relocate_marbles"] = r'''// LeetCode 2766 - Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/

use std::collections::HashSet;

impl Solution {
    pub fn relocate_marbles(nums: Vec<i32>, move_from: Vec<i32>, move_to: Vec<i32>) -> Vec<i32> {
        let mut pos: HashSet<i32> = nums.into_iter().collect();
        for i in 0..move_from.len() {
            pos.remove(&move_from[i]);
            pos.insert(move_to[i]);
        }
        let mut ans: Vec<i32> = pos.into_iter().collect();
        ans.sort_unstable();
        ans
    }
}
'''

FILES["2767_partition_string_into_minimum_beautiful_substrings"] = r'''// LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

use std::collections::HashSet;

impl Solution {
    pub fn minimum_beautiful_substrings(s: String) -> i32 {
        let n = s.len();
        let mut pow5 = HashSet::new();
        let mut x: i64 = 1;
        loop {
            let mut t = x;
            let mut b = String::new();
            while t > 0 {
                b.push(char::from(b'0' + (t & 1) as u8));
                t >>= 1;
            }
            let b: String = b.chars().rev().collect();
            let b = if b.is_empty() { "0".to_string() } else { b };
            if b.len() > n {
                break;
            }
            pow5.insert(b);
            x *= 5;
        }
        const INF: i32 = 1 << 30;
        let mut dp = vec![INF; n + 1];
        dp[0] = 0;
        let bytes = s.as_bytes();
        for i in 0..n {
            if dp[i] == INF || bytes[i] == b'0' {
                continue;
            }
            for j in i + 1..=n {
                if pow5.contains(&s[i..j]) {
                    dp[j] = dp[j].min(dp[i] + 1);
                }
            }
        }
        if dp[n] == INF { -1 } else { dp[n] }
    }
}
'''

FILES["2768_number_of_black_blocks"] = r'''// LeetCode 2768 - Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/

use std::collections::HashMap;

impl Solution {
    pub fn count_black_blocks(m: i32, n: i32, coordinates: Vec<Vec<i32>>) -> Vec<i64> {
        let mut cnt: HashMap<(i32, i32), i32> = HashMap::new();
        for c in coordinates {
            let (x, y) = (c[0], c[1]);
            for i in x - 1..=x {
                for j in y - 1..=y {
                    if i >= 0 && j >= 0 && i < m - 1 && j < n - 1 {
                        *cnt.entry((i, j)).or_insert(0) += 1;
                    }
                }
            }
        }
        let mut ans = vec![0i64; 5];
        ans[0] = (m as i64 - 1) * (n as i64 - 1);
        for &v in cnt.values() {
            ans[v as usize] += 1;
            ans[0] -= 1;
        }
        ans
    }
}
'''

FILES["2769_find_the_maximum_achievable_number"] = r'''// LeetCode 2769 - Find the Maximum Achievable Number
// https://leetcode.com/problems/find-the-maximum-achievable-number/

impl Solution {
    pub fn the_maximum_achievable_x(num: i32, t: i32) -> i32 {
        num + 2 * t
    }
}
'''

FILES["2770_maximum_number_of_jumps_to_reach_the_last_index"] = r'''// LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

impl Solution {
    pub fn maximum_jumps(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let mut dp = vec![-1; n];
        dp[0] = 0;
        for i in 0..n {
            if dp[i] < 0 {
                continue;
            }
            for j in i + 1..n {
                if (nums[j] - nums[i]).abs() <= target {
                    dp[j] = dp[j].max(dp[i] + 1);
                }
            }
        }
        dp[n - 1]
    }
}
'''

FILES["2771_longest_non_decreasing_subarray_from_two_arrays"] = r'''// LeetCode 2771 - Longest Non-decreasing Subarray From Two Arrays
// https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

impl Solution {
    pub fn max_non_decreasing_length(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let mut dp1 = 1;
        let mut dp2 = 1;
        let mut ans = 1;
        for i in 1..n {
            let mut nd1 = 1;
            let mut nd2 = 1;
            if nums1[i] >= nums1[i - 1] {
                nd1 = nd1.max(dp1 + 1);
            }
            if nums1[i] >= nums2[i - 1] {
                nd1 = nd1.max(dp2 + 1);
            }
            if nums2[i] >= nums1[i - 1] {
                nd2 = nd2.max(dp1 + 1);
            }
            if nums2[i] >= nums2[i - 1] {
                nd2 = nd2.max(dp2 + 1);
            }
            dp1 = nd1;
            dp2 = nd2;
            ans = ans.max(dp1.max(dp2));
        }
        ans
    }
}
'''

FILES["2772_apply_operations_to_make_all_array_elements_equal_to_zero"] = r'''// LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
// https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

impl Solution {
    pub fn check_array(nums: Vec<i32>, k: i32) -> bool {
        let n = nums.len();
        let k = k as usize;
        let mut diff = vec![0i32; n + 1];
        let mut cur = 0;
        for i in 0..n {
            cur += diff[i];
            let need = nums[i] - cur;
            if need < 0 {
                return false;
            }
            if need > 0 {
                if i + k > n {
                    return false;
                }
                cur += need;
                diff[i + k] -= need;
            }
        }
        true
    }
}
'''

FILES["2773_height_of_special_binary_tree"] = f'''// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/

{TREE}
impl Solution {{
    pub fn height_of_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {{
        Self::dfs(root)
    }}

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>) -> i32 {{
        let Some(n) = node else {{
            return -1;
        }};
        let left = n.borrow().left.clone();
        let right = n.borrow().right.clone();
        if let Some(l) = &left {{
            if let Some(lr) = l.borrow().right.clone() {{
                if Rc::ptr_eq(&lr, &n) {{
                    return Self::dfs(right) + 1;
                }}
            }}
        }}
        if let Some(r) = &right {{
            if let Some(rl) = r.borrow().left.clone() {{
                if Rc::ptr_eq(&rl, &n) {{
                    return Self::dfs(left) + 1;
                }}
            }}
        }}
        Self::dfs(left).max(Self::dfs(right)) + 1
    }}
}}
'''

FILES["2774_array_upper_bound"] = r'''// LeetCode 2774 - Array Upper Bound
// https://leetcode.com/problems/array-upper-bound/

impl Solution {
    pub fn upper_bound(nums: Vec<i32>, target: i32) -> i32 {
        let mut lo = 0i32;
        let mut hi = nums.len() as i32;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if nums[mid as usize] <= target {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        lo
    }
}
'''

FILES["2775_undefined_to_null"] = r'''// LeetCode 2775 - Undefined to Null
// https://leetcode.com/problems/undefined-to-null/

impl Solution {
    pub fn undefined_to_null(obj: i32) -> i32 {
        obj
    }
}
'''

FILES["2776_convert_callback_based_function_to_promise_based_function"] = r'''// LeetCode 2776 - Convert Callback Based Function to Promise Based Function
// https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/

impl Solution {
    pub fn promisify<F: Fn()>(_fn: F) -> Box<dyn Fn() -> i32> {
        Box::new(|| 0)
    }
}
'''

FILES["2777_date_range_generator"] = r'''// LeetCode 2777 - Date Range Generator
// https://leetcode.com/problems/date-range-generator/

impl Solution {
    pub fn date_range_generator(start: String, end: String, step: i32) -> Vec<String> {
        let parse = |s: &str| -> Option<(i32, i32, i32)> {
            let p: Vec<i32> = s.split('-').filter_map(|x| x.parse().ok()).collect();
            if p.len() == 3 {
                Some((p[0], p[1], p[2]))
            } else {
                None
            }
        };
        let Some((mut y, mut m, mut d)) = parse(&start) else {
            return vec![];
        };
        let Some((ey, em, ed)) = parse(&end) else {
            return vec![];
        };
        let is_leap = |yy: i32| (yy % 4 == 0 && yy % 100 != 0) || yy % 400 == 0;
        let add_days = |yy: &mut i32, mm: &mut i32, dd: &mut i32, days: i32| {
            let mut days = days;
            while days > 0 {
                let mut mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
                if is_leap(*yy) {
                    mdays[2] = 29;
                }
                *dd += 1;
                if *dd > mdays[*mm as usize] {
                    *dd = 1;
                    *mm += 1;
                }
                if *mm > 12 {
                    *mm = 1;
                    *yy += 1;
                }
                days -= 1;
            }
        };
        let mut ans = Vec::new();
        while y < ey || (y == ey && m < em) || (y == ey && m == em && d <= ed) {
            ans.push(format!("{:04}-{:02}-{:02}", y, m, d));
            add_days(&mut y, &mut m, &mut d, step);
        }
        ans
    }
}
'''

FILES["2778_sum_of_squares_of_special_elements"] = r'''// LeetCode 2778 - Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/

impl Solution {
    pub fn sum_of_squares(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut ans = 0;
        for (i, &v) in nums.iter().enumerate() {
            if n % (i as i32 + 1) == 0 {
                ans += v * v;
            }
        }
        ans
    }
}
'''

FILES["2779_maximum_beauty_of_an_array_after_applying_operation"] = r'''// LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
// https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

impl Solution {
    pub fn maximum_beauty(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut ans = 0;
        let mut left = 0;
        for right in 0..nums.len() {
            while nums[right] - nums[left] > 2 * k {
                left += 1;
            }
            ans = ans.max((right - left + 1) as i32);
        }
        ans
    }
}
'''

FILES["2780_minimum_index_of_a_valid_split"] = r'''// LeetCode 2780 - Minimum Index of a Valid Split
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_index(nums: Vec<i32>) -> i32 {
        let mut freq = HashMap::new();
        let mut dom = 0;
        let mut best = 0;
        for &v in &nums {
            let e = freq.entry(v).or_insert(0);
            *e += 1;
            if *e > best {
                best = *e;
                dom = v;
            }
        }
        let mut left = 0;
        let n = nums.len() as i32;
        for i in 0..n - 1 {
            if nums[i as usize] == dom {
                left += 1;
            }
            let right = best - left;
            if left * 2 > i + 1 && right * 2 > n - i - 1 {
                return i;
            }
        }
        -1
    }
}
'''

FILES["2781_length_of_the_longest_valid_substring"] = r'''// LeetCode 2781 - Length of the Longest Valid Substring
// https://leetcode.com/problems/length-of-the-longest-valid-substring/

use std::collections::HashSet;

impl Solution {
    pub fn longest_valid_substring(word: String, forbidden: Vec<String>) -> i32 {
        let forbid: HashSet<String> = forbidden.iter().cloned().collect();
        let max_len = forbidden.iter().map(|f| f.len()).max().unwrap_or(0);
        let n = word.len();
        let mut ans = 0i32;
        let mut right = n as i32 - 1;
        for left in (0..n).rev() {
            let mut k = left;
            while k <= right as usize && k - left + 1 <= max_len {
                if forbid.contains(&word[left..=k]) {
                    right = k as i32 - 1;
                    break;
                }
                k += 1;
            }
            ans = ans.max(right - left as i32 + 1);
        }
        ans
    }
}
'''

FILES["2782_number_of_unique_categories"] = r'''// LeetCode 2782 - Number of Unique Categories
// https://leetcode.com/problems/number-of-unique-categories/

use std::collections::HashSet;

impl Solution {
    pub fn number_of_categories(_n: i32, category_handler: Vec<i32>) -> i32 {
        category_handler.into_iter().collect::<HashSet<_>>().len() as i32
    }
}
'''

FILES["2784_check_if_array_is_good"] = r'''// LeetCode 2784 - Check if Array is Good
// https://leetcode.com/problems/check-if-array-is-good/

impl Solution {
    pub fn is_good(nums: Vec<i32>) -> bool {
        let n = nums.len() as i32 - 1;
        if n < 1 {
            return false;
        }
        let mut freq = vec![0; (n + 1) as usize];
        for v in nums {
            if v < 1 || v > n {
                return false;
            }
            freq[v as usize] += 1;
        }
        for i in 1..n {
            if freq[i as usize] != 1 {
                return false;
            }
        }
        freq[n as usize] == 2
    }
}
'''

FILES["2785_sort_vowels_in_a_string"] = r'''// LeetCode 2785 - Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/

impl Solution {
    pub fn sort_vowels(s: String) -> String {
        fn is_vowel(c: u8) -> bool {
            matches!(c, b'a' | b'e' | b'i' | b'o' | b'u' | b'A' | b'E' | b'I' | b'O' | b'U')
        }
        let mut b = s.into_bytes();
        let mut vowels: Vec<u8> = b.iter().copied().filter(|&c| is_vowel(c)).collect();
        vowels.sort_unstable();
        let mut vi = 0;
        for c in &mut b {
            if is_vowel(*c) {
                *c = vowels[vi];
                vi += 1;
            }
        }
        String::from_utf8(b).unwrap()
    }
}
'''

FILES["2786_visit_array_positions_to_maximize_score"] = r'''// LeetCode 2786 - Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

impl Solution {
    pub fn max_score(nums: Vec<i32>, x: i32) -> i64 {
        let neg = -(1i64 << 60);
        let mut even = nums[0] as i64;
        let mut odd = nums[0] as i64;
        if nums[0] % 2 == 0 {
            odd = neg;
        } else {
            even = neg;
        }
        for i in 1..nums.len() {
            let v = nums[i] as i64;
            if nums[i] % 2 == 0 {
                even = (even + v).max(odd + v - x as i64);
            } else {
                odd = (odd + v).max(even + v - x as i64);
            }
        }
        even.max(odd)
    }
}
'''

FILES["2787_ways_to_express_an_integer_as_sum_of_powers"] = r'''// LeetCode 2787 - Ways to Express an Integer as Sum of Powers
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

impl Solution {
    pub fn number_of_ways(n: i32, x: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = n as i64;
        let mut powers = Vec::new();
        let mut i = 1i64;
        loop {
            let mut p = 1i64;
            for _ in 0..x {
                p *= i;
                if p > n {
                    break;
                }
            }
            if p > n {
                break;
            }
            powers.push(p as i32);
            i += 1;
        }
        let n = n as usize;
        let mut dp = vec![0i32; n + 1];
        dp[0] = 1;
        for p in powers {
            let p = p as usize;
            for s in (p..=n).rev() {
                dp[s] = (dp[s] + dp[s - p]) % MOD;
            }
        }
        dp[n]
    }
}
'''

FILES["2788_split_strings_by_separator"] = r'''// LeetCode 2788 - Split Strings by Separator
// https://leetcode.com/problems/split-strings-by-separator/

impl Solution {
    pub fn split_words_by_separator(words: Vec<String>, separator: char) -> Vec<String> {
        let mut ans = Vec::new();
        for w in words {
            let b = w.as_bytes();
            let mut start = 0;
            for i in 0..=b.len() {
                if i == b.len() || b[i] == separator as u8 {
                    if i > start {
                        ans.push(w[start..i].to_string());
                    }
                    start = i + 1;
                }
            }
        }
        ans
    }
}
'''

FILES["2789_largest_element_in_an_array_after_merge_operations"] = r'''// LeetCode 2789 - Largest Element in an Array after Merge Operations
// https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

impl Solution {
    pub fn max_array_value(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut cur = nums[n - 1] as i64;
        let mut ans = cur;
        for i in (0..n - 1).rev() {
            if nums[i] as i64 <= cur {
                cur += nums[i] as i64;
            } else {
                cur = nums[i] as i64;
            }
            ans = ans.max(cur);
        }
        ans
    }
}
'''

FILES["2790_maximum_number_of_groups_with_increasing_length"] = r'''// LeetCode 2790 - Maximum Number of Groups With Increasing Length
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

impl Solution {
    pub fn max_increasing_groups(mut usage_limits: Vec<i32>) -> i32 {
        usage_limits.sort_unstable();
        let mut ans = 0i32;
        let mut sum = 0i64;
        for v in usage_limits {
            sum += v as i64;
            let need = (ans as i64 + 1) * (ans as i64 + 2) / 2;
            if sum >= need {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["2791_count_paths_that_can_form_a_palindrome_in_a_tree"] = r'''// LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

use std::collections::HashMap;

impl Solution {
    pub fn count_palindrome_paths(parent: Vec<i32>, s: String) -> i64 {
        let n = parent.len();
        let mut g = vec![Vec::new(); n];
        for i in 1..n {
            g[parent[i] as usize].push(i);
        }
        let bytes = s.as_bytes();
        let mut freq = HashMap::new();
        freq.insert(0i32, 1i64);
        let mut ans = 0i64;
        fn dfs(
            u: usize,
            mask: i32,
            g: &[Vec<usize>],
            bytes: &[u8],
            freq: &mut HashMap<i32, i64>,
            ans: &mut i64,
        ) {
            for &v in &g[u] {
                let nm = mask ^ (1 << (bytes[v] - b'a'));
                *ans += *freq.get(&nm).unwrap_or(&0);
                for b in 0..26 {
                    *ans += *freq.get(&(nm ^ (1 << b))).unwrap_or(&0);
                }
                *freq.entry(nm).or_insert(0) += 1;
                dfs(v, nm, g, bytes, freq, ans);
            }
        }
        dfs(0, 0, &g, bytes, &mut freq, &mut ans);
        ans
    }
}
'''

FILES["2792_count_nodes_that_are_great_enough"] = f'''// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/

{TREE}
impl Solution {{
    pub fn count_great_enough_nodes(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {{
        let mut ans = 0;
        Self::dfs(root, k, &mut ans);
        ans
    }}

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, k: i32, ans: &mut i32) -> Vec<i32> {{
        let Some(n) = node else {{
            return vec![];
        }};
        let val = n.borrow().val;
        let left = n.borrow().left.clone();
        let right = n.borrow().right.clone();
        let mut vals = vec![val];
        vals.extend(Self::dfs(left, k, ans));
        vals.extend(Self::dfs(right, k, ans));
        let smaller = vals.iter().filter(|&&v| v < val).count() as i32;
        if smaller >= k {{
            *ans += 1;
        }}
        vals
    }}
}}
'''

FILES["2794_create_object_from_two_arrays"] = r'''// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/

use std::collections::HashMap;

impl Solution {
    pub fn create_object(keys_arr: Vec<String>, values_arr: Vec<i32>) -> HashMap<String, i32> {
        let n = keys_arr.len().min(values_arr.len());
        let mut out = HashMap::new();
        for i in 0..n {
            out.entry(keys_arr[i].clone()).or_insert(values_arr[i]);
        }
        out
    }
}
'''

FILES["2795_parallel_execution_of_promises_for_individual_results_retrieval"] = r'''// LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
// https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/

impl Solution {
    pub fn promise_all_settled<F: Fn() -> i32>(functions: Vec<F>) -> Vec<(String, i32)> {
        functions
            .into_iter()
            .map(|f| ("fulfilled".to_string(), f()))
            .collect()
    }
}
'''

FILES["2796_repeat_string"] = r'''// LeetCode 2796 - Repeat String
// https://leetcode.com/problems/repeat-string/

impl Solution {
    pub fn replicate(s: String, times: i32) -> String {
        if times <= 0 {
            return String::new();
        }
        s.repeat(times as usize)
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
    print(f"part B written={written}")

if __name__ == "__main__":
    main()
