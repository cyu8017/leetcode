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

FILES = {}

FILES["2439_minimize_maximum_of_array"] = r'''// LeetCode 2439 - Minimize Maximum of Array
// https://leetcode.com/problems/minimize-maximum-of-array/

impl Solution {
    pub fn minimize_array_value(nums: Vec<i32>) -> i32 {
        let mut sum = 0i64;
        let mut ans = 0;
        for (i, &x) in nums.iter().enumerate() {
            sum += x as i64;
            let avg = ((sum + i as i64) / (i as i64 + 1)) as i32;
            if avg > ans {
                ans = avg;
            }
        }
        ans
    }
}
'''

FILES["2440_create_components_with_same_value"] = r'''// LeetCode 2440 - Create Components With Same Value
// https://leetcode.com/problems/create-components-with-same-value/

impl Solution {
    pub fn component_value(nums: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        let total: i32 = nums.iter().sum();
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        fn dfs(u: usize, p: i32, target: i32, nums: &[i32], g: &[Vec<usize>]) -> i32 {
            let mut sum = nums[u];
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                let sub = dfs(v, u as i32, target, nums, g);
                if sub < 0 {
                    return -1;
                }
                sum += sub;
            }
            if sum > target {
                return -1;
            }
            if sum == target {
                return 0;
            }
            sum
        }
        for parts in (1..=n as i32).rev() {
            if total % parts != 0 {
                continue;
            }
            let target = total / parts;
            if dfs(0, -1, target, &nums, &g) == 0 {
                return parts - 1;
            }
        }
        0
    }
}
'''

FILES["2441_largest_positive_integer_that_exists_with_its_negative"] = r'''// LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

use std::collections::HashSet;

impl Solution {
    pub fn find_max_k(nums: Vec<i32>) -> i32 {
        let mut seen = HashSet::new();
        let mut ans = -1;
        for x in nums {
            seen.insert(x);
            if x > 0 && seen.contains(&(-x)) && x > ans {
                ans = x;
            }
            if x < 0 && seen.contains(&(-x)) && -x > ans {
                ans = -x;
            }
        }
        ans
    }
}
'''

FILES["2442_count_number_of_distinct_integers_after_reverse_operations"] = r'''// LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

use std::collections::HashSet;

impl Solution {
    pub fn count_distinct_integers(nums: Vec<i32>) -> i32 {
        fn rev(mut x: i32) -> i32 {
            let mut r = 0;
            while x > 0 {
                r = r * 10 + x % 10;
                x /= 10;
            }
            r
        }
        let mut seen = HashSet::new();
        for x in nums {
            seen.insert(x);
            seen.insert(rev(x));
        }
        seen.len() as i32
    }
}
'''

FILES["2443_sum_of_number_and_its_reverse"] = r'''// LeetCode 2443 - Sum of Number and Its Reverse
// https://leetcode.com/problems/sum-of-number-and-its-reverse/

impl Solution {
    pub fn sum_of_number_and_reverse(num: i32) -> bool {
        fn rev(mut x: i32) -> i32 {
            let mut r = 0;
            while x > 0 {
                r = r * 10 + x % 10;
                x /= 10;
            }
            r
        }
        for i in 0..=num {
            if i + rev(i) == num {
                return true;
            }
        }
        false
    }
}
'''

FILES["2444_count_subarrays_with_fixed_bounds"] = r'''// LeetCode 2444 - Count Subarrays With Fixed Bounds
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        let mut ans = 0i64;
        let mut imin = -1i32;
        let mut imax = -1i32;
        let mut ibad = -1i32;
        for (i, &x) in nums.iter().enumerate() {
            let i = i as i32;
            if x < min_k || x > max_k {
                ibad = i;
            }
            if x == min_k {
                imin = i;
            }
            if x == max_k {
                imax = i;
            }
            let bound = imin.min(imax);
            if bound > ibad {
                ans += (bound - ibad) as i64;
            }
        }
        ans
    }
}
'''

FILES["2445_number_of_nodes_with_value_one"] = r'''// LeetCode 2445 - Number of Nodes With Value One
// https://leetcode.com/problems/number-of-nodes-with-value-one/

impl Solution {
    pub fn number_of_nodes(n: i32, queries: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut flip = vec![0; n + 1];
        let mut val = vec![0; n + 1];
        for q in queries {
            flip[q as usize] ^= 1;
        }
        let mut ans = 0;
        for i in 1..=n {
            val[i] = flip[i];
            if i > 1 {
                val[i] ^= val[i / 2];
            }
            ans += val[i];
        }
        ans
    }
}
'''

FILES["2446_determine_if_two_events_have_conflict"] = r'''// LeetCode 2446 - Determine if Two Events Have Conflict
// https://leetcode.com/problems/determine-if-two-events-have-conflict/

impl Solution {
    pub fn have_conflict(event1: Vec<String>, event2: Vec<String>) -> bool {
        event1[0] <= event2[1] && event2[0] <= event1[1]
    }
}
'''

FILES["2447_number_of_subarrays_with_gcd_equal_to_k"] = r'''// LeetCode 2447 - Number of Subarrays With GCD Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

impl Solution {
    pub fn subarray_gcd(nums: Vec<i32>, k: i32) -> i32 {
        fn gcd(mut x: i32, mut y: i32) -> i32 {
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
            let mut g = 0;
            for j in i..n {
                g = gcd(g, nums[j]);
                if g < k {
                    break;
                }
                if g == k {
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["2448_minimum_cost_to_make_array_equal"] = r'''// LeetCode 2448 - Minimum Cost to Make Array Equal
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/

impl Solution {
    pub fn min_cost(nums: Vec<i32>, cost: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by_key(|&i| nums[i]);
        let total_cost: i64 = cost.iter().map(|&c| c as i64).sum();
        let mut pref = 0i64;
        let mut median = 0;
        for &i in &idx {
            pref += cost[i] as i64;
            if pref * 2 >= total_cost {
                median = nums[i];
                break;
            }
        }
        let mut ans = 0i64;
        for i in 0..n {
            let mut diff = nums[i] as i64 - median as i64;
            if diff < 0 {
                diff = -diff;
            }
            ans += diff * cost[i] as i64;
        }
        ans
    }
}
'''

FILES["2449_minimum_number_of_operations_to_make_arrays_similar"] = r'''// LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

impl Solution {
    pub fn make_similar(mut nums: Vec<i32>, mut target: Vec<i32>) -> i64 {
        nums.sort_unstable();
        target.sort_unstable();
        let mut odd_n = Vec::new();
        let mut even_n = Vec::new();
        let mut odd_t = Vec::new();
        let mut even_t = Vec::new();
        for x in nums {
            if x % 2 == 0 {
                even_n.push(x);
            } else {
                odd_n.push(x);
            }
        }
        for x in target {
            if x % 2 == 0 {
                even_t.push(x);
            } else {
                odd_t.push(x);
            }
        }
        let mut ans = 0i64;
        for i in 0..odd_n.len() {
            let diff = odd_n[i] - odd_t[i];
            if diff > 0 {
                ans += (diff / 2) as i64;
            }
        }
        for i in 0..even_n.len() {
            let diff = even_n[i] - even_t[i];
            if diff > 0 {
                ans += (diff / 2) as i64;
            }
        }
        ans
    }
}
'''

FILES["2450_number_of_distinct_binary_strings_after_applying_operations"] = r'''// LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
// https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

impl Solution {
    pub fn count_distinct_strings(s: String, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = s.len() as i32;
        let mut ans = 1i64;
        for _ in 0..n - k + 1 {
            ans = ans * 2 % MOD;
        }
        ans as i32
    }
}
'''

FILES["2451_odd_string_difference"] = r'''// LeetCode 2451 - Odd String Difference
// https://leetcode.com/problems/odd-string-difference/

impl Solution {
    pub fn odd_string(words: Vec<String>) -> String {
        fn diff(w: &str) -> Vec<i32> {
            let b = w.as_bytes();
            let mut d = Vec::new();
            for i in 1..b.len() {
                d.push(b[i] as i32 - b[i - 1] as i32);
            }
            d
        }
        let d0 = diff(&words[0]);
        let d1 = diff(&words[1]);
        if d0 == d1 {
            for i in 2..words.len() {
                if diff(&words[i]) != d0 {
                    return words[i].clone();
                }
            }
        }
        if diff(&words[2]) == d0 {
            return words[1].clone();
        }
        words[0].clone()
    }
}
'''

FILES["2452_words_within_two_edits_of_dictionary"] = r'''// LeetCode 2452 - Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

impl Solution {
    pub fn two_edit_words(queries: Vec<String>, dictionary: Vec<String>) -> Vec<String> {
        let mut ans = Vec::new();
        for q in &queries {
            let qb = q.as_bytes();
            let mut ok = false;
            for d in &dictionary {
                let db = d.as_bytes();
                let mut diff = 0;
                for i in 0..qb.len() {
                    if qb[i] != db[i] {
                        diff += 1;
                        if diff > 2 {
                            break;
                        }
                    }
                }
                if diff <= 2 {
                    ok = true;
                    break;
                }
            }
            if ok {
                ans.push(q.clone());
            }
        }
        ans
    }
}
'''

FILES["2453_destroy_sequential_targets"] = r'''// LeetCode 2453 - Destroy Sequential Targets
// https://leetcode.com/problems/destroy-sequential-targets/

use std::collections::HashMap;

impl Solution {
    pub fn destroy_targets(nums: Vec<i32>, space: i32) -> i32 {
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        for &x in &nums {
            *cnt.entry(x % space).or_insert(0) += 1;
        }
        let best_cnt = *cnt.values().max().unwrap();
        let mut ans = 1_000_000_000;
        for (&m, &c) in &cnt {
            if c == best_cnt {
                for &x in &nums {
                    if x % space == m && x < ans {
                        ans = x;
                    }
                }
            }
        }
        ans
    }
}
'''

FILES["2454_next_greater_element_iv"] = r'''// LeetCode 2454 - Next Greater Element IV
// https://leetcode.com/problems/next-greater-element-iv/

impl Solution {
    pub fn second_greater_element(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut ans = vec![-1; n];
        let mut stack1 = Vec::new();
        let mut stack2 = Vec::new();
        for i in 0..n {
            let x = nums[i];
            while !stack2.is_empty() && nums[*stack2.last().unwrap()] < x {
                ans[stack2.pop().unwrap()] = x;
            }
            let mut tmp = Vec::new();
            while !stack1.is_empty() && nums[*stack1.last().unwrap()] < x {
                tmp.push(stack1.pop().unwrap());
            }
            for &j in tmp.iter().rev() {
                stack2.push(j);
            }
            stack1.push(i);
        }
        ans
    }
}
'''

FILES["2455_average_value_of_even_numbers_that_are_divisible_by_three"] = r'''// LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

impl Solution {
    pub fn average_value(nums: Vec<i32>) -> i32 {
        let mut sum = 0;
        let mut cnt = 0;
        for x in nums {
            if x % 6 == 0 {
                sum += x;
                cnt += 1;
            }
        }
        if cnt == 0 {
            0
        } else {
            sum / cnt
        }
    }
}
'''

FILES["2456_most_popular_video_creator"] = r'''// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

use std::collections::HashMap;

impl Solution {
    pub fn most_popular_creator(
        creators: Vec<String>,
        ids: Vec<String>,
        views: Vec<i32>,
    ) -> Vec<Vec<String>> {
        struct Info {
            total: i64,
            best_id: String,
            best_views: i32,
        }
        let mut mp: HashMap<String, Info> = HashMap::new();
        let mut max_total = 0i64;
        for i in 0..creators.len() {
            let entry = mp.entry(creators[i].clone()).or_insert_with(|| Info {
                total: 0,
                best_id: ids[i].clone(),
                best_views: views[i],
            });
            if entry.total == 0 && entry.best_id.is_empty() {
                entry.best_id = ids[i].clone();
                entry.best_views = views[i];
            }
            entry.total += views[i] as i64;
            if views[i] > entry.best_views
                || (views[i] == entry.best_views && ids[i] < entry.best_id)
            {
                entry.best_views = views[i];
                entry.best_id = ids[i].clone();
            }
            if entry.total > max_total {
                max_total = entry.total;
            }
        }
        let mut ans = Vec::new();
        for (c, inf) in mp {
            if inf.total == max_total {
                ans.push(vec![c, inf.best_id]);
            }
        }
        ans
    }
}
'''

FILES["2457_minimum_addition_to_make_integer_beautiful"] = r'''// LeetCode 2457 - Minimum Addition to Make Integer Beautiful
// https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

impl Solution {
    pub fn make_integer_beautiful(n: i64, target: i32) -> i64 {
        fn digit_sum(mut x: i64) -> i32 {
            let mut s = 0;
            while x > 0 {
                s += (x % 10) as i32;
                x /= 10;
            }
            s
        }
        let orig = n;
        let mut n = n;
        let mut pow = 1i64;
        while digit_sum(n) > target {
            n = n / 10 + 1;
            pow *= 10;
        }
        n * pow - orig
    }
}
'''

FILES["2458_height_of_binary_tree_after_subtree_removal_queries"] = f'''// LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

use std::collections::HashMap;
{TREE}
impl Solution {{
    pub fn tree_queries(
        root: Option<Rc<RefCell<TreeNode>>>,
        queries: Vec<i32>,
    ) -> Vec<i32> {{
        let mut height: HashMap<i32, i32> = HashMap::new();
        let mut level: HashMap<i32, i32> = HashMap::new();
        let mut level_max: HashMap<i32, Vec<i32>> = HashMap::new();
        fn dfs(
            node: &Option<Rc<RefCell<TreeNode>>>,
            d: i32,
            height: &mut HashMap<i32, i32>,
            level: &mut HashMap<i32, i32>,
            level_max: &mut HashMap<i32, Vec<i32>>,
        ) -> i32 {{
            let Some(n) = node else {{
                return -1;
            }};
            let n = n.borrow();
            level.insert(n.val, d);
            let h = 1
                + dfs(&n.left, d + 1, height, level, level_max)
                    .max(dfs(&n.right, d + 1, height, level, level_max));
            height.insert(n.val, h);
            let arr = level_max.entry(d).or_default();
            if arr.is_empty() {{
                *arr = vec![h];
            }} else if h >= arr[0] {{
                *arr = vec![h, arr[0]];
            }} else if arr.len() == 1 || h > arr[1] {{
                *arr = vec![arr[0], h];
            }}
            h
        }}
        dfs(&root, 0, &mut height, &mut level, &mut level_max);
        let mut ans = vec![0; queries.len()];
        for (i, &q) in queries.iter().enumerate() {{
            let d = level[&q];
            let h = height[&q];
            let top = &level_max[&d];
            if top[0] == h {{
                if top.len() > 1 {{
                    ans[i] = d + top[1];
                }} else {{
                    ans[i] = d - 1;
                }}
            }} else {{
                ans[i] = d + top[0];
            }}
        }}
        ans
    }}
}}
'''

FILES["2459_sort_array_by_moving_items_to_empty_space"] = r'''// LeetCode 2459 - Sort Array By Moving Items to Empty Space
// https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

use std::collections::HashMap;

impl Solution {
    pub fn sort_array(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        fn solve(nums: &[i32], start_zero: bool) -> i32 {
            let n = nums.len();
            let mut arr = nums.to_vec();
            let mut pos: HashMap<i32, usize> = HashMap::new();
            for i in 0..n {
                pos.insert(arr[i], i);
            }
            let mut ops = 0;
            loop {
                let empty = pos[&0];
                let should = if start_zero {
                    empty as i32
                } else if empty == n - 1 {
                    0
                } else {
                    empty as i32 + 1
                };
                if arr[empty] == should {
                    let mut found = None;
                    for i in 0..n {
                        let want = if start_zero {
                            i as i32
                        } else if i == n - 1 {
                            0
                        } else {
                            i as i32 + 1
                        };
                        if arr[i] != want {
                            found = Some(i);
                            break;
                        }
                    }
                    if found.is_none() {
                        return ops;
                    }
                    let found = found.unwrap();
                    let v = arr[found];
                    arr.swap(empty, found);
                    pos.insert(0, found);
                    pos.insert(v, empty);
                    ops += 1;
                    continue;
                }
                let j = pos[&should];
                let v = arr[j];
                arr.swap(empty, j);
                pos.insert(0, j);
                pos.insert(v, empty);
                ops += 1;
            }
        }
        solve(&nums, true).min(solve(&nums, false))
    }
}
'''

FILES["2460_apply_operations_to_an_array"] = r'''// LeetCode 2460 - Apply Operations to an Array
// https://leetcode.com/problems/apply-operations-to-an-array/

impl Solution {
    pub fn apply_operations(mut nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        for i in 0..n.saturating_sub(1) {
            if nums[i] == nums[i + 1] {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }
        let mut ans = vec![0; n];
        let mut j = 0;
        for x in nums {
            if x != 0 {
                ans[j] = x;
                j += 1;
            }
        }
        ans
    }
}
'''

FILES["2461_maximum_sum_of_distinct_subarrays_with_length_k"] = r'''// LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let k = k as usize;
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut sum = 0i64;
        let mut ans = 0i64;
        for i in 0..nums.len() {
            sum += nums[i] as i64;
            *cnt.entry(nums[i]).or_insert(0) += 1;
            if i >= k {
                sum -= nums[i - k] as i64;
                let e = cnt.get_mut(&nums[i - k]).unwrap();
                *e -= 1;
                if *e == 0 {
                    cnt.remove(&nums[i - k]);
                }
            }
            if i + 1 >= k && cnt.len() == k {
                ans = ans.max(sum);
            }
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
