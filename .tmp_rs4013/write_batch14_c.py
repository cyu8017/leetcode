#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

TREE = """use std::cell::RefCell;
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
"""

FILES = {}

FILES["3134_find_the_median_of_the_uniqueness_array"] = r'''// LeetCode 3134 - Find the Median of the Uniqueness Array
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

use std::collections::HashMap;

impl Solution {
    pub fn median_of_uniqueness_array(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let m = (1 + n as i64) * n as i64 / 2;
        let check = |mx: usize| -> bool {
            let mut cnt: HashMap<i32, i32> = HashMap::new();
            let mut l = 0usize;
            let mut k = 0i64;
            for r in 0..n {
                *cnt.entry(nums[r]).or_insert(0) += 1;
                while cnt.len() > mx {
                    let y = nums[l];
                    l += 1;
                    let e = cnt.get_mut(&y).unwrap();
                    *e -= 1;
                    if *e == 0 {
                        cnt.remove(&y);
                    }
                }
                k += (r - l + 1) as i64;
                if k >= (m + 1) / 2 {
                    return true;
                }
            }
            false
        };
        let mut lo = 1usize;
        let mut hi = n;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if check(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }
}
'''

FILES["3135_equalize_strings_by_adding_or_removing_characters_at_ends"] = r'''// LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
// https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

impl Solution {
    pub fn min_operations(initial: String, target: String) -> i32 {
        let a = initial.as_bytes();
        let b = target.as_bytes();
        let m = a.len();
        let n = b.len();
        let mut f = vec![vec![0i32; n + 1]; m + 1];
        let mut mx = 0;
        for i in 0..m {
            for j in 0..n {
                if a[i] == b[j] {
                    f[i + 1][j + 1] = f[i][j] + 1;
                    mx = mx.max(f[i + 1][j + 1]);
                }
            }
        }
        m as i32 + n as i32 - 2 * mx
    }
}
'''

FILES["3136_valid_word"] = r'''// LeetCode 3136 - Valid Word
// https://leetcode.com/problems/valid-word/

impl Solution {
    pub fn is_valid(word: String) -> bool {
        if word.len() < 3 {
            return false;
        }
        let mut has_vowel = false;
        let mut has_consonant = false;
        let mut vs = [false; 26];
        for c in b"aeiou" {
            vs[(c - b'a') as usize] = true;
        }
        for c in word.bytes() {
            if c.is_ascii_alphabetic() {
                let lower = c.to_ascii_lowercase();
                if vs[(lower - b'a') as usize] {
                    has_vowel = true;
                } else {
                    has_consonant = true;
                }
            } else if !c.is_ascii_digit() {
                return false;
            }
        }
        has_vowel && has_consonant
    }
}
'''

FILES["3137_minimum_number_of_operations_to_make_word_k_periodic"] = r'''// LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
// https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_operations_to_make_k_periodic(word: String, k: i32) -> i32 {
        let k = k as usize;
        let n = word.len();
        let mut cnt: HashMap<&str, i32> = HashMap::new();
        let mut mx = 0;
        let mut i = 0;
        while i < n {
            let s = &word[i..i + k];
            let e = cnt.entry(s).or_insert(0);
            *e += 1;
            mx = mx.max(*e);
            i += k;
        }
        n as i32 / k as i32 - mx
    }
}
'''

FILES["3138_minimum_length_of_anagram_concatenation"] = r'''// LeetCode 3138 - Minimum Length of Anagram Concatenation
// https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

impl Solution {
    pub fn min_anagram_length(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut cnt = [0i32; 26];
        for &c in b {
            cnt[(c - b'a') as usize] += 1;
        }
        let check = |k: usize| -> bool {
            let mut i = 0;
            while i < n {
                let mut cnt1 = [0i32; 26];
                for j in i..i + k {
                    cnt1[(b[j] - b'a') as usize] += 1;
                }
                for j in 0..26 {
                    if cnt1[j] * (n as i32 / k as i32) != cnt[j] {
                        return false;
                    }
                }
                i += k;
            }
            true
        };
        let mut i = 1;
        loop {
            if n % i == 0 && check(i) {
                return i as i32;
            }
            i += 1;
        }
    }
}
'''

FILES["3139_minimum_cost_to_equalize_array"] = r'''// LeetCode 3139 - Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/

impl Solution {
    pub fn min_cost_to_equalize_array(nums: Vec<i32>, cost1: i32, cost2: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len() as i64;
        let mut min_num = nums[0];
        let mut max_num = nums[0];
        let mut sum = 0i64;
        for &v in &nums {
            min_num = min_num.min(v);
            max_num = max_num.max(v);
            sum += v as i64;
        }
        if cost1 as i64 * 2 <= cost2 as i64 || n < 3 {
            let total_gap = max_num as i64 * n - sum;
            return (cost1 as i64 * total_gap % MOD) as i32;
        }
        let mut ans = i64::MAX;
        for target in max_num..2 * max_num {
            let max_gap = (target - min_num) as i64;
            let total_gap = target as i64 * n - sum;
            let mut pairs = total_gap / 2;
            let alt = total_gap - max_gap;
            if alt < pairs {
                pairs = alt;
            }
            let cost = cost1 as i64 * (total_gap - 2 * pairs) + cost2 as i64 * pairs;
            ans = ans.min(cost);
        }
        (ans % MOD) as i32
    }
}
'''

FILES["3141_maximum_hamming_distances"] = r'''// LeetCode 3141 - Maximum Hamming Distances
// https://leetcode.com/problems/maximum-hamming-distances/

impl Solution {
    pub fn max_hamming_distances(mut nums: Vec<i32>, m: i32) -> Vec<i32> {
        let m = m as usize;
        let mut dist = vec![-1i32; 1 << m];
        let mut q = Vec::new();
        for &x in &nums {
            dist[x as usize] = 0;
            q.push(x as usize);
        }
        let mut k = 1;
        while !q.is_empty() {
            let mut t = Vec::new();
            for &x in &q {
                for i in 0..m {
                    let y = x ^ (1 << i);
                    if dist[y] == -1 {
                        dist[y] = k;
                        t.push(y);
                    }
                }
            }
            q = t;
            k += 1;
        }
        let mask = (1 << m) - 1;
        for i in 0..nums.len() {
            let x = nums[i] as usize;
            nums[i] = m as i32 - dist[x ^ mask];
        }
        nums
    }
}
'''

FILES["3142_check_if_grid_satisfies_conditions"] = r'''// LeetCode 3142 - Check if Grid Satisfies Conditions
// https://leetcode.com/problems/check-if-grid-satisfies-conditions/

impl Solution {
    pub fn satisfies_conditions(grid: Vec<Vec<i32>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        for i in 0..m {
            for j in 0..n {
                let x = grid[i][j];
                if i + 1 < m && x != grid[i + 1][j] {
                    return false;
                }
                if j + 1 < n && x == grid[i][j + 1] {
                    return false;
                }
            }
        }
        true
    }
}
'''

FILES["3143_maximum_points_inside_the_square"] = r'''// LeetCode 3143 - Maximum Points Inside the Square
// https://leetcode.com/problems/maximum-points-inside-the-square/

use std::collections::BTreeMap;

impl Solution {
    pub fn max_points_inside_square(points: Vec<Vec<i32>>, s: String) -> i32 {
        let sb = s.as_bytes();
        let mut g: BTreeMap<i32, Vec<usize>> = BTreeMap::new();
        for i in 0..points.len() {
            let key = points[i][0].abs().max(points[i][1].abs());
            g.entry(key).or_default().push(i);
        }
        let mut vis = [false; 26];
        let mut ans = 0;
        for idx in g.values() {
            for &i in idx {
                let j = (sb[i] - b'a') as usize;
                if vis[j] {
                    return ans;
                }
                vis[j] = true;
            }
            ans += idx.len() as i32;
        }
        ans
    }
}
'''

FILES["3144_minimum_substring_partition_of_equal_character_frequency"] = r'''// LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
// https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_substrings_in_partition(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut memo = vec![-1i32; n];
        fn dfs(b: &[u8], i: usize, memo: &mut [i32]) -> i32 {
            let n = b.len();
            if i >= n {
                return 0;
            }
            if memo[i] != -1 {
                return memo[i];
            }
            let mut cnt = [0i32; 26];
            let mut freq: HashMap<i32, i32> = HashMap::new();
            memo[i] = (n - i) as i32;
            for j in i..n {
                let k = (b[j] - b'a') as usize;
                if cnt[k] > 0 {
                    let e = freq.get_mut(&cnt[k]).unwrap();
                    *e -= 1;
                    if *e == 0 {
                        freq.remove(&cnt[k]);
                    }
                }
                cnt[k] += 1;
                *freq.entry(cnt[k]).or_insert(0) += 1;
                if freq.len() == 1 {
                    memo[i] = memo[i].min(1 + dfs(b, j + 1, memo));
                }
            }
            memo[i]
        }
        dfs(b, 0, &mut memo)
    }
}
'''

FILES["3145_find_products_of_elements_of_big_array"] = r'''// LeetCode 3145 - Find Products of Elements of Big Array
// https://leetcode.com/problems/find-products-of-elements-of-big-array/

impl Solution {
    fn init_tables() -> ([i64; 51], [i64; 51]) {
        let mut cnt = [0i64; 51];
        let mut s = [0i64; 51];
        let mut p = 1i64;
        for i in 1..=50 {
            cnt[i] = cnt[i - 1] * 2 + p;
            s[i] = s[i - 1] * 2 + p * (i as i64 - 1);
            p *= 2;
        }
        (cnt, s)
    }

    fn num_idx_and_sum(mut x: i64, cnt: &[i64; 51], s: &[i64; 51]) -> (i64, i64) {
        let mut idx = 0i64;
        let mut total_sum = 0i64;
        while x > 0 {
            let i = 63 - (x as u64).leading_zeros() as i32;
            idx += cnt[i as usize];
            total_sum += s[i as usize];
            x -= 1i64 << i;
            total_sum += (x + 1) * i as i64;
            idx += x + 1;
        }
        (idx, total_sum)
    }

    fn f(i: i64, cnt: &[i64; 51], s: &[i64; 51]) -> i64 {
        const M: i32 = 50;
        let mut l = 0i64;
        let mut r = 1i64 << M;
        while l < r {
            let mid = (l + r + 1) >> 1;
            let (idx, _) = Self::num_idx_and_sum(mid, cnt, s);
            if idx < i {
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        let (idx, mut total_sum) = Self::num_idx_and_sum(l, cnt, s);
        let mut rem = i - idx;
        let mut x = l + 1;
        for _ in 0..rem {
            let y = x & x.wrapping_neg();
            total_sum += (y as u64).trailing_zeros() as i64;
            x -= y;
        }
        total_sum
    }

    fn qpow(mut a: i64, mut n: i64, modn: i64) -> i64 {
        let mut ans = 1 % modn;
        a %= modn;
        while n > 0 {
            if n & 1 == 1 {
                ans = ans * a % modn;
            }
            a = a * a % modn;
            n >>= 1;
        }
        ans
    }

    pub fn find_products_of_elements(queries: Vec<Vec<i64>>) -> Vec<i32> {
        let (cnt, s) = Self::init_tables();
        queries
            .iter()
            .map(|q| {
                let (left, right, modn) = (q[0], q[1], q[2]);
                let power = Self::f(right + 1, &cnt, &s) - Self::f(left, &cnt, &s);
                Self::qpow(2, power, modn) as i32
            })
            .collect()
    }
}
'''

FILES["3146_permutation_difference_between_two_strings"] = r'''// LeetCode 3146 - Permutation Difference between Two Strings
// https://leetcode.com/problems/permutation-difference-between-two-strings/

impl Solution {
    pub fn find_permutation_difference(s: String, t: String) -> i32 {
        let mut d = [0i32; 26];
        for (i, c) in s.bytes().enumerate() {
            d[(c - b'a') as usize] = i as i32;
        }
        let mut ans = 0;
        for (i, c) in t.bytes().enumerate() {
            ans += (d[(c - b'a') as usize] - i as i32).abs();
        }
        ans
    }
}
'''

FILES["3147_taking_maximum_energy_from_the_mystic_dungeon"] = r'''// LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
// https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

impl Solution {
    pub fn maximum_energy(energy: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let n = energy.len();
        let mut ans = -(1 << 30);
        for i in n - k..n {
            let mut s = 0;
            let mut j = i as i32;
            while j >= 0 {
                s += energy[j as usize];
                ans = ans.max(s);
                j -= k as i32;
            }
        }
        ans
    }
}
'''

FILES["3148_maximum_difference_score_in_a_grid"] = r'''// LeetCode 3148 - Maximum Difference Score in a Grid
// https://leetcode.com/problems/maximum-difference-score-in-a-grid/

impl Solution {
    pub fn max_score(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        const INF: i32 = 1 << 30;
        let mut f = vec![vec![0; n]; m];
        let mut ans = -INF;
        for i in 0..m {
            for j in 0..n {
                let x = grid[i][j];
                let mut mi = INF;
                if i > 0 {
                    mi = mi.min(f[i - 1][j]);
                }
                if j > 0 {
                    mi = mi.min(f[i][j - 1]);
                }
                ans = ans.max(x - mi);
                f[i][j] = x.min(mi);
            }
        }
        ans
    }
}
'''

FILES["3149_find_the_minimum_cost_array_permutation"] = r'''// LeetCode 3149 - Find the Minimum Cost Array Permutation
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

impl Solution {
    pub fn find_permutation(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut memo = vec![vec![-1i32; n]; 1 << n];
        fn dfs(nums: &[i32], n: usize, mask: usize, pre: usize, memo: &mut [Vec<i32>]) -> i32 {
            if mask == (1 << n) - 1 {
                return (pre as i32 - nums[0]).abs();
            }
            if memo[mask][pre] != -1 {
                return memo[mask][pre];
            }
            let mut res = i32::MAX;
            for cur in 1..n {
                if (mask >> cur) & 1 == 0 {
                    res = res.min((pre as i32 - nums[cur]).abs() + dfs(nums, n, mask | (1 << cur), cur, memo));
                }
            }
            memo[mask][pre] = res;
            res
        }
        let mut ans = Vec::new();
        fn g(
            nums: &[i32],
            n: usize,
            mask: usize,
            pre: usize,
            memo: &mut [Vec<i32>],
            ans: &mut Vec<i32>,
        ) {
            ans.push(pre as i32);
            if mask == (1 << n) - 1 {
                return;
            }
            let res = dfs(nums, n, mask, pre, memo);
            for cur in 1..n {
                if (mask >> cur) & 1 == 0 {
                    if (pre as i32 - nums[cur]).abs() + dfs(nums, n, mask | (1 << cur), cur, memo) == res {
                        g(nums, n, mask | (1 << cur), cur, memo, ans);
                        break;
                    }
                }
            }
        }
        g(&nums, n, 1, 0, &mut memo, &mut ans);
        ans
    }
}
'''

FILES["3151_special_array_i"] = r'''// LeetCode 3151 - Special Array I
// https://leetcode.com/problems/special-array-i/

impl Solution {
    pub fn is_array_special(nums: Vec<i32>) -> bool {
        for i in 1..nums.len() {
            if nums[i] % 2 == nums[i - 1] % 2 {
                return false;
            }
        }
        true
    }
}
'''

FILES["3152_special_array_ii"] = r'''// LeetCode 3152 - Special Array II
// https://leetcode.com/problems/special-array-ii/

impl Solution {
    pub fn is_array_special(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n = nums.len();
        let mut d = vec![0; n];
        for i in 0..n {
            d[i] = i;
        }
        for i in 1..n {
            if nums[i] % 2 != nums[i - 1] % 2 {
                d[i] = d[i - 1];
            }
        }
        queries.iter().map(|q| d[q[1] as usize] <= q[0] as usize).collect()
    }
}
'''

FILES["3153_sum_of_digit_differences_of_all_pairs"] = r'''// LeetCode 3153 - Sum of Digit Differences of All Pairs
// https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

impl Solution {
    pub fn sum_digit_differences(mut nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let m = ((nums[0] as f64).log10().floor() as i32) + 1;
        let mut ans = 0i64;
        for _ in 0..m {
            let mut cnt = [0i32; 10];
            for i in 0..n {
                cnt[(nums[i] % 10) as usize] += 1;
                nums[i] /= 10;
            }
            for v in cnt {
                ans += v as i64 * (n as i64 - v as i64);
            }
        }
        ans / 2
    }
}
'''

FILES["3154_find_number_of_ways_to_reach_the_k_th_stair"] = r'''// LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

use std::collections::HashMap;

impl Solution {
    pub fn ways_to_reach_stair(k: i32) -> i32 {
        let mut f = HashMap::new();
        fn dfs(i: i64, j: i32, jump: i32, k: i64, f: &mut HashMap<i64, i32>) -> i32 {
            if i > k + 1 {
                return 0;
            }
            let key = (i << 32) | ((jump as i64) << 1) | j as i64;
            if let Some(&v) = f.get(&key) {
                return v;
            }
            let mut ans = 0;
            if i == k {
                ans += 1;
            }
            if i > 0 && j == 0 {
                ans += dfs(i - 1, 1, jump, k, f);
            }
            ans += dfs(i + (1i64 << jump), 0, jump + 1, k, f);
            f.insert(key, ans);
            ans
        }
        dfs(1, 0, 0, k as i64, &mut f)
    }
}
'''

FILES["3155_maximum_number_of_upgradable_servers"] = r'''// LeetCode 3155 - Maximum Number of Upgradable Servers
// https://leetcode.com/problems/maximum-number-of-upgradable-servers/

impl Solution {
    pub fn max_upgrades(count: Vec<i32>, upgrade: Vec<i32>, sell: Vec<i32>, money: Vec<i32>) -> Vec<i32> {
        count
            .iter()
            .enumerate()
            .map(|(i, &cnt)| {
                let cnt = cnt as i64;
                cnt.min((cnt * sell[i] as i64 + money[i] as i64) / (upgrade[i] as i64 + sell[i] as i64)) as i32
            })
            .collect()
    }
}
'''

FILES["3157_find_the_level_of_tree_with_minimum_sum"] = f'''// LeetCode 3157 - Find the Level of Tree with Minimum Sum
// https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

{TREE}
impl Solution {{
    pub fn minimum_level(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {{
        let Some(root) = root else {{
            return 0;
        }};
        let mut q = VecDeque::new();
        q.push_back(root);
        let mut s = i64::MAX;
        let mut ans = 0;
        let mut level = 1;
        while !q.is_empty() {{
            let m = q.len();
            let mut t = 0i64;
            for _ in 0..m {{
                let node = q.pop_front().unwrap();
                let node = node.borrow();
                t += node.val as i64;
                if let Some(l) = node.left.clone() {{
                    q.push_back(l);
                }}
                if let Some(r) = node.right.clone() {{
                    q.push_back(r);
                }}
            }}
            if s > t {{
                s = t;
                ans = level;
            }}
            level += 1;
        }}
        ans
    }}
}}
'''

FILES["3158_find_the_xor_of_numbers_which_appear_twice"] = r'''// LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
// https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

impl Solution {
    pub fn duplicate_numbers_xor(nums: Vec<i32>) -> i32 {
        let mut cnt = [0i32; 51];
        let mut ans = 0;
        for x in nums {
            cnt[x as usize] += 1;
            if cnt[x as usize] == 2 {
                ans ^= x;
            }
        }
        ans
    }
}
'''

FILES["3159_find_occurrences_of_an_element_in_an_array"] = r'''// LeetCode 3159 - Find Occurrences of an Element in an Array
// https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

impl Solution {
    pub fn occurrences_of_element(nums: Vec<i32>, queries: Vec<i32>, x: i32) -> Vec<i32> {
        let ids: Vec<i32> = nums
            .iter()
            .enumerate()
            .filter(|(_, &v)| v == x)
            .map(|(i, _)| i as i32)
            .collect();
        queries
            .into_iter()
            .map(|i| {
                if (i as usize) - 1 < ids.len() {
                    ids[i as usize - 1]
                } else {
                    -1
                }
            })
            .collect()
    }
}
'''

FILES["3160_find_the_number_of_distinct_colors_among_the_balls"] = r'''// LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
// https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

use std::collections::HashMap;

impl Solution {
    pub fn query_results(_limit: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut g: HashMap<i32, i32> = HashMap::new();
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut ans = Vec::with_capacity(queries.len());
        for q in queries {
            let (x, y) = (q[0], q[1]);
            *cnt.entry(y).or_insert(0) += 1;
            if let Some(&old) = g.get(&x) {
                let e = cnt.get_mut(&old).unwrap();
                *e -= 1;
                if *e == 0 {
                    cnt.remove(&old);
                }
            }
            g.insert(x, y);
            ans.push(cnt.len() as i32);
        }
        ans
    }
}
'''

FILES["3161_block_placement_queries"] = r'''// LeetCode 3161 - Block Placement Queries
// https://leetcode.com/problems/block-placement-queries/

struct FenwickMax {
    vals: Vec<i32>,
}

impl FenwickMax {
    fn new(n: usize) -> Self {
        Self { vals: vec![0; n + 1] }
    }
    fn maximize(&mut self, mut i: usize, val: i32) {
        while i < self.vals.len() {
            self.vals[i] = self.vals[i].max(val);
            i += i & i.wrapping_neg();
        }
    }
    fn get(&self, mut i: usize) -> i32 {
        let mut res = 0;
        while i > 0 {
            res = res.max(self.vals[i]);
            i -= i & i.wrapping_neg();
        }
        res
    }
}

impl Solution {
    pub fn get_results(queries: Vec<Vec<i32>>) -> Vec<bool> {
        let mut n = queries.len() * 3;
        if n > 50000 {
            n = 50000;
        }
        let mut tree = FenwickMax::new(n + 1);
        let mut obs = vec![0i32, n as i32];
        for q in &queries {
            if q[0] == 1 {
                let x = q[1];
                let j = obs.partition_point(|&v| v < x);
                if j == obs.len() || obs[j] != x {
                    obs.insert(j, x);
                }
            }
        }
        for i in 0..obs.len() - 1 {
            tree.maximize(obs[i + 1] as usize, obs[i + 1] - obs[i]);
        }
        let mut ans = Vec::new();
        for i in (0..queries.len()).rev() {
            let typ = queries[i][0];
            let x = queries[i][1];
            if typ == 1 {
                let j = obs.partition_point(|&v| v < x);
                let prev = obs[j - 1];
                let next = obs[j + 1];
                obs.remove(j);
                tree.maximize(next as usize, next - prev);
            } else {
                let sz = queries[i][2];
                let j = obs.partition_point(|&v| v < x + 1) - 1;
                let prev = obs[j];
                ans.push(tree.get(prev as usize) >= sz || x - prev >= sz);
            }
        }
        ans.reverse();
        ans
    }
}
'''

FILES["3162_find_the_number_of_good_pairs_i"] = r'''// LeetCode 3162 - Find the Number of Good Pairs I
// https://leetcode.com/problems/find-the-number-of-good-pairs-i/

impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i32 {
        let mut ans = 0;
        for &x in &nums1 {
            for &y in &nums2 {
                if x % (y * k) == 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["3163_string_compression_iii"] = r'''// LeetCode 3163 - String Compression III
// https://leetcode.com/problems/string-compression-iii/

impl Solution {
    pub fn compressed_string(word: String) -> String {
        let b = word.as_bytes();
        let n = b.len();
        let mut ans = String::new();
        let mut i = 0;
        while i < n {
            let mut j = i + 1;
            while j < n && b[j] == b[i] {
                j += 1;
            }
            let mut k = j - i;
            while k > 0 {
                let x = 9.min(k);
                ans.push((b'0' + x as u8) as char);
                ans.push(b[i] as char);
                k -= x;
            }
            i = j;
        }
        ans
    }
}
'''

FILES["3164_find_the_number_of_good_pairs_ii"] = r'''// LeetCode 3164 - Find the Number of Good Pairs II
// https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        let mut cnt1: HashMap<i32, i32> = HashMap::new();
        for x in nums1 {
            if x % k == 0 {
                *cnt1.entry(x / k).or_insert(0) += 1;
            }
        }
        if cnt1.is_empty() {
            return 0;
        }
        let mut cnt2: HashMap<i32, i32> = HashMap::new();
        for x in nums2 {
            *cnt2.entry(x).or_insert(0) += 1;
        }
        let mx = *cnt1.keys().max().unwrap();
        let mut ans = 0i64;
        for (&x, &v) in &cnt2 {
            let mut s = 0i32;
            let mut y = x;
            while y <= mx {
                if let Some(&c) = cnt1.get(&y) {
                    s += c;
                }
                y += x;
            }
            ans += s as i64 * v as i64;
        }
        ans
    }
}
'''

FILES["3165_maximum_sum_of_subsequence_with_non_adjacent_elements"] = r'''// LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
// https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

#[derive(Clone, Copy, Default)]
struct Node {
    l: i32,
    r: i32,
    s00: i32,
    s01: i32,
    s10: i32,
    s11: i32,
}

impl Solution {
    fn build(tr: &mut [Node], u: usize, l: i32, r: i32) {
        tr[u].l = l;
        tr[u].r = r;
        if l == r {
            return;
        }
        let mid = (l + r) >> 1;
        Self::build(tr, u << 1, l, mid);
        Self::build(tr, u << 1 | 1, mid + 1, r);
    }

    fn pushup(tr: &mut [Node], u: usize) {
        let left = tr[u << 1];
        let right = tr[u << 1 | 1];
        tr[u].s00 = (left.s00 + right.s10).max(left.s01 + right.s00);
        tr[u].s01 = (left.s00 + right.s11).max(left.s01 + right.s01);
        tr[u].s10 = (left.s10 + right.s10).max(left.s11 + right.s00);
        tr[u].s11 = (left.s10 + right.s11).max(left.s11 + right.s01);
    }

    fn modify(tr: &mut [Node], u: usize, x: i32, v: i32) {
        if tr[u].l == tr[u].r {
            tr[u].s11 = 0.max(v);
            return;
        }
        let mid = (tr[u].l + tr[u].r) >> 1;
        if x <= mid {
            Self::modify(tr, u << 1, x, v);
        } else {
            Self::modify(tr, u << 1 | 1, x, v);
        }
        Self::pushup(tr, u);
    }

    fn query(tr: &[Node], u: usize, l: i32, r: i32) -> i32 {
        if tr[u].l >= l && tr[u].r <= r {
            return tr[u].s11;
        }
        let mid = (tr[u].l + tr[u].r) >> 1;
        let mut ans = 0;
        if r <= mid {
            ans = Self::query(tr, u << 1, l, r);
        }
        if l > mid {
            ans = ans.max(Self::query(tr, u << 1 | 1, l, r));
        }
        ans
    }

    pub fn maximum_sum_subsequence(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        let mut tr = vec![Node::default(); n * 4];
        Self::build(&mut tr, 1, 1, n as i32);
        for i in 0..n {
            Self::modify(&mut tr, 1, i as i32 + 1, nums[i]);
        }
        const MOD: i32 = 1_000_000_007;
        let mut ans = 0;
        for q in queries {
            Self::modify(&mut tr, 1, q[0] + 1, q[1]);
            ans = (ans + Self::query(&tr, 1, 1, n as i32)) % MOD;
        }
        ans
    }
}
'''

FILES["3167_better_compression_of_string"] = r'''// LeetCode 3167 - Better Compression of String
// https://leetcode.com/problems/better-compression-of-string/

use std::collections::HashMap;

impl Solution {
    pub fn better_compression(compressed: String) -> String {
        let b = compressed.as_bytes();
        let n = b.len();
        let mut cnt: HashMap<u8, i32> = HashMap::new();
        let mut i = 0;
        while i < n {
            let c = b[i];
            let mut j = i + 1;
            let mut x = 0i32;
            while j < n && b[j].is_ascii_digit() {
                x = x * 10 + (b[j] - b'0') as i32;
                j += 1;
            }
            *cnt.entry(c).or_insert(0) += x;
            i = j;
        }
        let mut ans = String::new();
        for c in b'a'..=b'z' {
            if let Some(&v) = cnt.get(&c) {
                if v > 0 {
                    ans.push(c as char);
                    ans.push_str(&v.to_string());
                }
            }
        }
        ans
    }
}
'''

FILES["3168_minimum_number_of_chairs_in_a_waiting_room"] = r'''// LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

impl Solution {
    pub fn minimum_chairs(s: String) -> i32 {
        let mut cnt = 0;
        let mut left = 0;
        for c in s.chars() {
            if c == 'E' {
                if left > 0 {
                    left -= 1;
                } else {
                    cnt += 1;
                }
            } else {
                left += 1;
            }
        }
        cnt
    }
}
'''

def main():
    n = 0
    for folder, content in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(content, encoding="utf-8", newline="\n")
        n += 1
        print("wrote", folder)
    print("total", n)

if __name__ == "__main__":
    main()
