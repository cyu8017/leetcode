#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")

LIST = """
#[derive(Eq, PartialEq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}
"""

FILES = {}

FILES["3047_find_the_largest_area_of_square_inside_two_rectangles"] = r'''// LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
// https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

impl Solution {
    pub fn largest_square_area(bottom_left: Vec<Vec<i32>>, top_right: Vec<Vec<i32>>) -> i64 {
        let mut ans = 0i64;
        let n = bottom_left.len();
        for i in 0..n {
            let (x1, y1) = (bottom_left[i][0], bottom_left[i][1]);
            let (x2, y2) = (top_right[i][0], top_right[i][1]);
            for j in i + 1..n {
                let (x3, y3) = (bottom_left[j][0], bottom_left[j][1]);
                let (x4, y4) = (top_right[j][0], top_right[j][1]);
                let ww = x2.min(x4) - x1.max(x3);
                let h = y2.min(y4) - y1.max(y3);
                let e = ww.min(h);
                if e > 0 {
                    ans = ans.max(e as i64 * e as i64);
                }
            }
        }
        ans
    }
}
'''

FILES["3048_earliest_second_to_mark_indices_i"] = r'''// LeetCode 3048 - Earliest Second to Mark Indices I
// https://leetcode.com/problems/earliest-second-to-mark-indices-i/

impl Solution {
    pub fn earliest_second_to_mark_indices(nums: Vec<i32>, change_indices: Vec<i32>) -> i32 {
        let n = nums.len();
        let m = change_indices.len();
        let ok = |t: usize| -> bool {
            let mut last = vec![0usize; n + 1];
            for s in 0..t {
                last[change_indices[s] as usize] = s;
            }
            let mut decrement = 0i32;
            let mut marked = 0usize;
            for s in 0..t {
                let i = change_indices[s] as usize;
                if last[i] == s {
                    if decrement < nums[i - 1] {
                        return false;
                    }
                    decrement -= nums[i - 1];
                    marked += 1;
                } else {
                    decrement += 1;
                }
            }
            marked == n
        };
        let mut l = 0usize;
        let mut r = m + 1;
        while l < r {
            let mid = (l + r) / 2;
            if ok(mid) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        if l > m { -1 } else { l as i32 }
    }
}
'''

FILES["3049_earliest_second_to_mark_indices_ii"] = r'''// LeetCode 3049 - Earliest Second to Mark Indices II
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};

impl Solution {
    fn get_second_to_index(nums: &[i32], change_indices: &[i32]) -> HashMap<i32, usize> {
        let mut index_to_first = HashMap::new();
        for (second, &ci) in change_indices.iter().enumerate() {
            let index = (ci - 1) as usize;
            if nums[index] > 0 {
                index_to_first.entry(index).or_insert(second as i32);
            }
        }
        let mut second_to_index = HashMap::new();
        for (index, second) in index_to_first {
            second_to_index.insert(second, index);
        }
        second_to_index
    }

    fn can_mark(nums: &[i32], second_to_index: &HashMap<i32, usize>, max_second: i32, nums_sum: i64) -> bool {
        let mut h = BinaryHeap::new();
        let mut marks = 0i32;
        for second in (0..max_second).rev() {
            if let Some(&idx) = second_to_index.get(&second) {
                h.push(Reverse(nums[idx]));
                if marks == 0 {
                    h.pop();
                    marks += 1;
                } else {
                    marks -= 1;
                }
            } else {
                marks += 1;
            }
        }
        let heap_size = h.len() as i64;
        let heap_sum: i64 = h.into_iter().map(|Reverse(v)| v as i64).sum();
        let decrement_and_mark = nums_sum - heap_sum + (nums.len() as i64 - heap_size);
        let zero_and_mark = heap_size + heap_size;
        decrement_and_mark + zero_and_mark <= max_second as i64
    }

    pub fn earliest_second_to_mark_indices(nums: Vec<i32>, change_indices: Vec<i32>) -> i32 {
        let second_to_index = Self::get_second_to_index(&nums, &change_indices);
        let nums_sum: i64 = nums.iter().map(|&v| v as i64).sum();
        let mut l = 0i32;
        let mut r = change_indices.len() as i32 + 1;
        while l < r {
            let m = (l + r) / 2;
            if Self::can_mark(&nums, &second_to_index, m, nums_sum) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        if l <= change_indices.len() as i32 { l } else { -1 }
    }
}
'''

FILES["3062_winner_of_the_linked_list_game"] = f'''// LeetCode 3062 - Winner of the Linked List Game
// https://leetcode.com/problems/winner-of-the-linked-list-game/

{LIST}
impl Solution {{
    pub fn game_result(mut head: Option<Box<ListNode>>) -> String {{
        let mut odd = 0;
        let mut even = 0;
        while let Some(node) = head {{
            let a = node.val;
            let next = node.next.unwrap();
            let b = next.val;
            if a < b {{
                odd += 1;
            }}
            if a > b {{
                even += 1;
            }}
            head = next.next;
        }}
        if odd > even {{
            "Odd".to_string()
        }} else if odd < even {{
            "Even".to_string()
        }} else {{
            "Tie".to_string()
        }}
    }}
}}
'''

FILES["3063_linked_list_frequency"] = f'''// LeetCode 3063 - Linked List Frequency
// https://leetcode.com/problems/linked-list-frequency/

use std::collections::HashMap;

{LIST}
impl Solution {{
    pub fn frequencies_of_elements(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {{
        let mut cnt = HashMap::new();
        while let Some(node) = head {{
            *cnt.entry(node.val).or_insert(0) += 1;
            head = node.next;
        }}
        let mut dummy = ListNode {{ val: 0, next: None }};
        for &val in cnt.values() {{
            dummy.next = Some(Box::new(ListNode {{
                val,
                next: dummy.next.take(),
            }}));
        }}
        dummy.next
    }}
}}
'''

FILES["3064_guess_the_number_using_bitwise_questions_i"] = r'''// LeetCode 3064 - Guess the Number Using Bitwise Questions I
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

fn common_set_bits(num: i32) -> i32 {
    let _ = num;
    0
}

impl Solution {
    pub fn find_number() -> i32 {
        let mut n = 0i32;
        for i in 0..32 {
            let bit = 1i32.wrapping_shl(i);
            if common_set_bits(bit) > 0 {
                n |= bit;
            }
        }
        n
    }
}
'''

FILES["3065_minimum_operations_to_exceed_threshold_value_i"] = r'''// LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        nums.iter().filter(|&&x| x < k).count() as i32
    }
}
'''

FILES["3066_minimum_operations_to_exceed_threshold_value_ii"] = r'''// LeetCode 3066 - Minimum Operations to Exceed Threshold Value II
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut pq = BinaryHeap::new();
        for x in nums {
            pq.push(Reverse(x as i64));
        }
        let k = k as i64;
        let mut ans = 0;
        while pq.len() > 1 {
            if let Some(Reverse(x)) = pq.peek() {
                if *x >= k {
                    break;
                }
            }
            let Reverse(x) = pq.pop().unwrap();
            let Reverse(y) = pq.pop().unwrap();
            pq.push(Reverse(x * 2 + y));
            ans += 1;
        }
        ans
    }
}
'''

FILES["3067_count_pairs_of_connectable_servers_in_a_weighted_tree_network"] = r'''// LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
// https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

impl Solution {
    pub fn count_pairs_of_connectable_servers(edges: Vec<Vec<i32>>, signal_speed: i32) -> Vec<i32> {
        let n = edges.len() + 1;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
            g[e[1] as usize].push((e[0] as usize, e[2]));
        }
        fn dfs(g: &[Vec<(usize, i32)>], a: usize, fa: usize, ws: i32, signal_speed: i32) -> i32 {
            let mut cnt = if ws % signal_speed == 0 { 1 } else { 0 };
            for &(b, w) in &g[a] {
                if b != fa {
                    cnt += dfs(g, b, a, ws + w, signal_speed);
                }
            }
            cnt
        }
        let mut ans = vec![0; n];
        for a in 0..n {
            let mut s = 0;
            for &(b, w) in &g[a] {
                let t = dfs(&g, b, a, w, signal_speed);
                ans[a] += s * t;
                s += t;
            }
        }
        ans
    }
}
'''

FILES["3068_find_the_maximum_sum_of_node_values"] = r'''// LeetCode 3068 - Find the Maximum Sum of Node Values
// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

impl Solution {
    pub fn maximum_value_sum(nums: Vec<i32>, k: i32, _edges: Vec<Vec<i32>>) -> i64 {
        let mut f0 = 0i64;
        let mut f1 = -0x3f3f3f3fi64;
        for x in nums {
            let x = x as i64;
            let xk = (x as i32 ^ k) as i64;
            let nf0 = (f0 + x).max(f1 + xk);
            let nf1 = (f1 + x).max(f0 + xk);
            f0 = nf0;
            f1 = nf1;
        }
        f0
    }
}
'''

FILES["3069_distribute_elements_into_two_arrays_i"] = r'''// LeetCode 3069 - Distribute Elements Into Two Arrays I
// https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

impl Solution {
    pub fn result_array(nums: Vec<i32>) -> Vec<i32> {
        let mut arr1 = vec![nums[0]];
        let mut arr2 = vec![nums[1]];
        for &x in &nums[2..] {
            if *arr1.last().unwrap() > *arr2.last().unwrap() {
                arr1.push(x);
            } else {
                arr2.push(x);
            }
        }
        arr1.extend(arr2);
        arr1
    }
}
'''

FILES["3070_count_submatrices_with_top_left_element_and_sum_less_than_k"] = r'''// LeetCode 3070 - Count Submatrices with Top-Left Element and Sum Less Than k
// https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

impl Solution {
    pub fn count_submatrices(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = grid.len();
        let m = grid[0].len();
        let mut ans = 0;
        let mut s = vec![vec![0; m + 1]; n + 1];
        for i in 0..n {
            for j in 0..m {
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + grid[i][j];
                if s[i + 1][j + 1] <= k {
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["3071_minimum_operations_to_write_the_letter_y_on_a_grid"] = r'''// LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
// https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

impl Solution {
    pub fn minimum_operations_to_write_y(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len() as i32;
        let mut cnt1 = [0i32; 3];
        let mut cnt2 = [0i32; 3];
        for i in 0..n {
            for j in 0..n {
                let x = grid[i as usize][j as usize] as usize;
                let a = i == j && i <= n / 2;
                let b = i + j == n - 1 && i <= n / 2;
                let c = j == n / 2 && i >= n / 2;
                if a || b || c {
                    cnt1[x] += 1;
                } else {
                    cnt2[x] += 1;
                }
            }
        }
        let mut ans = n * n;
        for i in 0..3 {
            for j in 0..3 {
                if i != j {
                    ans = ans.min(n * n - cnt1[i] - cnt2[j]);
                }
            }
        }
        ans
    }
}
'''

FILES["3072_distribute_elements_into_two_arrays_ii"] = r'''// LeetCode 3072 - Distribute Elements Into Two Arrays II
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

struct Bit {
    n: usize,
    c: Vec<i32>,
}

impl Bit {
    fn new(n: usize) -> Self {
        Self { n, c: vec![0; n + 1] }
    }
    fn update(&mut self, mut x: usize, delta: i32) {
        while x <= self.n {
            self.c[x] += delta;
            x += x & x.wrapping_neg();
        }
    }
    fn query(&self, mut x: usize) -> i32 {
        let mut s = 0;
        while x > 0 {
            s += self.c[x];
            x -= x & x.wrapping_neg();
        }
        s
    }
}

impl Solution {
    pub fn result_array(nums: Vec<i32>) -> Vec<i32> {
        let mut st = nums.clone();
        st.sort_unstable();
        let n = st.len();
        let idx = |x: i32| -> usize { st.partition_point(|&v| v < x) + 1 };
        let mut tree1 = Bit::new(n + 1);
        let mut tree2 = Bit::new(n + 1);
        tree1.update(idx(nums[0]), 1);
        tree2.update(idx(nums[1]), 1);
        let mut arr1 = vec![nums[0]];
        let mut arr2 = vec![nums[1]];
        for &x in &nums[2..] {
            let id = idx(x);
            let a = arr1.len() as i32 - tree1.query(id);
            let b = arr2.len() as i32 - tree2.query(id);
            if a > b || (a == b && arr1.len() <= arr2.len()) {
                arr1.push(x);
                tree1.update(id, 1);
            } else {
                arr2.push(x);
                tree2.update(id, 1);
            }
        }
        arr1.extend(arr2);
        arr1
    }
}
'''

FILES["3073_maximum_increasing_triplet_value"] = r'''// LeetCode 3073 - Maximum Increasing Triplet Value
// https://leetcode.com/problems/maximum-increasing-triplet-value/

use std::collections::BTreeSet;

impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut right = vec![0; n];
        right[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            right[i] = nums[i].max(right[i + 1]);
        }
        let mut ts = BTreeSet::new();
        ts.insert(nums[0]);
        let mut ans = 0;
        for j in 1..n - 1 {
            if right[j + 1] > nums[j] {
                if let Some(&v) = ts.range(..nums[j]).next_back() {
                    ans = ans.max(v - nums[j] + right[j + 1]);
                }
            }
            ts.insert(nums[j]);
        }
        ans
    }
}
'''

FILES["3074_apple_redistribution_into_boxes"] = r'''// LeetCode 3074 - Apple Redistribution into Boxes
// https://leetcode.com/problems/apple-redistribution-into-boxes/

impl Solution {
    pub fn minimum_boxes(apple: Vec<i32>, mut capacity: Vec<i32>) -> i32 {
        capacity.sort_unstable();
        let mut s: i32 = apple.iter().sum();
        let mut i = 1;
        loop {
            s -= capacity[capacity.len() - i];
            if s <= 0 {
                return i as i32;
            }
            i += 1;
        }
    }
}
'''

FILES["3075_maximize_happiness_of_selected_children"] = r'''// LeetCode 3075 - Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

impl Solution {
    pub fn maximum_happiness_sum(mut happiness: Vec<i32>, k: i32) -> i64 {
        happiness.sort_unstable();
        let mut ans = 0i64;
        let n = happiness.len();
        for i in 0..k {
            let x = happiness[n - i as usize - 1] - i;
            ans += x.max(0) as i64;
        }
        ans
    }
}
'''

FILES["3076_shortest_uncommon_substring_in_an_array"] = r'''// LeetCode 3076 - Shortest Uncommon Substring in an Array
// https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

impl Solution {
    pub fn shortest_substrings(arr: Vec<String>) -> Vec<String> {
        let n = arr.len();
        let mut ans = vec![String::new(); n];
        for i in 0..n {
            let s = arr[i].as_bytes();
            let m = s.len();
            let mut j = 1;
            while j <= m && ans[i].is_empty() {
                for l in 0..=m - j {
                    let sub = std::str::from_utf8(&s[l..l + j]).unwrap();
                    if ans[i].is_empty() || ans[i].as_str() > sub {
                        let mut ok = true;
                        for k in 0..n {
                            if k != i && arr[k].contains(sub) {
                                ok = false;
                                break;
                            }
                        }
                        if ok {
                            ans[i] = sub.to_string();
                        }
                    }
                }
                j += 1;
            }
        }
        ans
    }
}
'''

FILES["3077_maximum_strength_of_k_disjoint_subarrays"] = r'''// LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
// https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

impl Solution {
    pub fn maximum_strength(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let k = k as usize;
        let inf = i64::MIN / 2;
        let mut f = vec![vec![vec![inf; 2]; k + 1]; n + 1];
        f[0][0][0] = 0;
        for i in 1..=n {
            let x = nums[i - 1] as i64;
            for j in 0..=k {
                let sign = if j & 1 == 1 { 1i64 } else { -1i64 };
                let val = sign * x * (k as i64 - j as i64 + 1);
                f[i][j][0] = f[i - 1][j][0].max(f[i - 1][j][1]);
                f[i][j][1] = f[i][j][1].max(f[i - 1][j][1].saturating_add(val));
                if j > 0 {
                    let t = f[i - 1][j - 1][0].max(f[i - 1][j - 1][1]).saturating_add(val);
                    f[i][j][1] = f[i][j][1].max(t);
                }
            }
        }
        f[n][k][0].max(f[n][k][1])
    }
}
'''

FILES["3078_match_alphanumerical_pattern_in_matrix_i"] = r'''// LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
// https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

impl Solution {
    pub fn find_pattern(board: Vec<Vec<i32>>, pattern: Vec<String>) -> Vec<i32> {
        let m = board.len();
        let n = board[0].len();
        let r = pattern.len();
        let c = pattern[0].len();
        let pats: Vec<Vec<u8>> = pattern.iter().map(|s| s.as_bytes().to_vec()).collect();
        let check = |i: usize, j: usize| -> bool {
            let mut d1 = [0i32; 26];
            let mut d2 = [0i32; 10];
            for a in 0..r {
                for b in 0..c {
                    let x = i + a;
                    let y = j + b;
                    let ch = pats[a][b];
                    if ch.is_ascii_digit() {
                        if (ch - b'0') as i32 != board[x][y] {
                            return false;
                        }
                    } else {
                        let v = (ch - b'a') as usize;
                        let cell = board[x][y] as usize;
                        if d1[v] > 0 && d1[v] - 1 != board[x][y] {
                            return false;
                        }
                        if d2[cell] > 0 && d2[cell] - 1 != v as i32 {
                            return false;
                        }
                        d1[v] = board[x][y] + 1;
                        d2[cell] = v as i32 + 1;
                    }
                }
            }
            true
        };
        for i in 0..=m - r {
            for j in 0..=n - c {
                if check(i, j) {
                    return vec![i as i32, j as i32];
                }
            }
        }
        vec![-1, -1]
    }
}
'''

FILES["3079_find_the_sum_of_encrypted_integers"] = r'''// LeetCode 3079 - Find the Sum of Encrypted Integers
// https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

impl Solution {
    fn encrypt(mut x: i32) -> i32 {
        let mut mx = 0;
        let mut p = 0;
        while x > 0 {
            mx = mx.max(x % 10);
            p = p * 10 + 1;
            x /= 10;
        }
        mx * p
    }

    pub fn sum_of_encrypted_int(nums: Vec<i32>) -> i32 {
        nums.into_iter().map(Self::encrypt).sum()
    }
}
'''

FILES["3080_mark_elements_on_array_by_performing_queries"] = r'''// LeetCode 3080 - Mark Elements on Array by Performing Queries
// https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

impl Solution {
    pub fn unmarked_sum_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        let n = nums.len();
        let mut s: i64 = nums.iter().map(|&x| x as i64).sum();
        let mut mark = vec![false; n];
        let mut arr: Vec<(i32, usize)> = nums.iter().enumerate().map(|(i, &v)| (v, i)).collect();
        arr.sort_unstable();
        let mut ans = vec![0i64; queries.len()];
        let mut j = 0;
        for (qi, q) in queries.iter().enumerate() {
            let index = q[0] as usize;
            let mut k = q[1];
            if !mark[index] {
                mark[index] = true;
                s -= nums[index] as i64;
            }
            while k > 0 && j < n {
                if !mark[arr[j].1] {
                    mark[arr[j].1] = true;
                    s -= arr[j].0 as i64;
                    k -= 1;
                }
                j += 1;
            }
            ans[qi] = s;
        }
        ans
    }
}
'''

FILES["3081_replace_question_marks_in_string_to_minimize_its_value"] = r'''// LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
// https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimize_string_value(s: String) -> String {
        let mut cnt = [0i32; 26];
        let mut k = 0;
        let bytes = s.as_bytes();
        for &c in bytes {
            if c == b'?' {
                k += 1;
            } else {
                cnt[(c - b'a') as usize] += 1;
            }
        }
        let mut pq = BinaryHeap::new();
        for i in 0..26 {
            pq.push(Reverse((cnt[i], i)));
        }
        let mut t = vec![0usize; k];
        for i in 0..k {
            let Reverse((freq, idx)) = pq.pop().unwrap();
            t[i] = idx;
            pq.push(Reverse((freq + 1, idx)));
        }
        t.sort_unstable();
        let mut j = 0;
        let mut out = s.into_bytes();
        for c in &mut out {
            if *c == b'?' {
                *c = t[j] as u8 + b'a';
                j += 1;
            }
        }
        String::from_utf8(out).unwrap()
    }
}
'''

FILES["3082_find_the_sum_of_the_power_of_all_subsequences"] = r'''// LeetCode 3082 - Find the Sum of the Power of All Subsequences
// https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

impl Solution {
    pub fn sum_of_power(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let k = k as usize;
        let mut f = vec![vec![0i64; k + 1]; n + 1];
        f[0][0] = 1;
        for i in 1..=n {
            let x = nums[i - 1] as usize;
            for j in 0..=k {
                f[i][j] = (f[i - 1][j] * 2) % MOD;
                if j >= x {
                    f[i][j] = (f[i][j] + f[i - 1][j - x]) % MOD;
                }
            }
        }
        f[n][k] as i32
    }
}
'''

FILES["3083_existence_of_a_substring_in_a_string_and_its_reverse"] = r'''// LeetCode 3083 - Existence of a Substring in a String and Its Reverse
// https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

impl Solution {
    pub fn is_substring_present(s: String) -> bool {
        let b = s.as_bytes();
        let mut st = [[false; 26]; 26];
        for i in 0..b.len().saturating_sub(1) {
            st[(b[i + 1] - b'a') as usize][(b[i] - b'a') as usize] = true;
        }
        for i in 0..b.len().saturating_sub(1) {
            if st[(b[i] - b'a') as usize][(b[i + 1] - b'a') as usize] {
                return true;
            }
        }
        false
    }
}
'''

FILES["3084_count_substrings_starting_and_ending_with_given_character"] = r'''// LeetCode 3084 - Count Substrings Starting and Ending with Given Character
// https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

impl Solution {
    pub fn count_substrings(s: String, c: char) -> i64 {
        let cnt = s.chars().filter(|&ch| ch == c).count() as i64;
        cnt + cnt * (cnt - 1) / 2
    }
}
'''

FILES["3085_minimum_deletions_to_make_string_k_special"] = r'''// LeetCode 3085 - Minimum Deletions to Make String K-Special
// https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

impl Solution {
    pub fn minimum_deletions(word: String, k: i32) -> i32 {
        let mut freq = [0i32; 26];
        for c in word.bytes() {
            freq[(c - b'a') as usize] += 1;
        }
        let nums: Vec<i32> = freq.iter().copied().filter(|&v| v > 0).collect();
        let f = |v: i32| -> i32 {
            let mut ans = 0;
            for &x in &nums {
                if x < v {
                    ans += x;
                } else if x > v + k {
                    ans += x - v - k;
                }
            }
            ans
        };
        let mut ans = word.len() as i32;
        for i in 0..=word.len() as i32 {
            ans = ans.min(f(i));
        }
        ans
    }
}
'''

FILES["3086_minimum_moves_to_pick_k_ones"] = r'''// LeetCode 3086 - Minimum Moves to Pick K Ones
// https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

impl Solution {
    pub fn minimum_moves(nums: Vec<i32>, k: i32, max_changes: i32) -> i64 {
        let n = nums.len();
        let mut cnt = vec![0i32; n + 1];
        let mut s = vec![0i64; n + 1];
        for i in 1..=n {
            cnt[i] = cnt[i - 1] + nums[i - 1];
            s[i] = s[i - 1] + i as i64 * nums[i - 1] as i64;
        }
        let mut ans = i64::MAX;
        for i in 1..=n {
            let mut t = 0i64;
            let mut need = k - nums[i - 1];
            for j in [i as i32 - 1, i as i32 + 1] {
                if need > 0 && 1 <= j && j <= n as i32 && nums[j as usize - 1] == 1 {
                    need -= 1;
                    t += 1;
                }
            }
            let c = need.min(max_changes);
            need -= c;
            t += c as i64 * 2;
            if need <= 0 {
                ans = ans.min(t);
                continue;
            }
            let mut l = 2i32;
            let mut r = (i as i32 - 1).max(n as i32 - i as i32);
            while l <= r {
                let mid = (l + r) >> 1;
                let l1 = 1.max(i as i32 - mid) as usize;
                let r1 = 0.max(i as i32 - 2) as usize;
                let l2 = (n as i32 + 1).min(i as i32 + 2) as usize;
                let r2 = (n as i32).min(i as i32 + mid) as usize;
                let c1 = cnt[r1] - cnt[l1 - 1];
                let c2 = cnt[r2] - cnt[l2 - 1];
                if c1 + c2 >= need {
                    let t1 = c1 as i64 * i as i64 - (s[r1] - s[l1 - 1]);
                    let t2 = s[r2] - s[l2 - 1] - c2 as i64 * i as i64;
                    ans = ans.min(t + t1 + t2);
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
        }
        ans
    }
}
'''

FILES["3088_make_string_anti_palindrome"] = r'''// LeetCode 3088 - Make String Anti-palindrome
// https://leetcode.com/problems/make-string-anti-palindrome/

impl Solution {
    pub fn make_anti_palindrome(s: String) -> String {
        let mut s: Vec<u8> = s.into_bytes();
        s.sort_unstable();
        let n = s.len();
        let m = n / 2;
        if s[m] == s[m - 1] {
            let mut i = m;
            while i < n && s[i] == s[i - 1] {
                i += 1;
            }
            let mut j = m;
            while j < n && s[j] == s[n - j - 1] {
                if i >= n {
                    return "-1".to_string();
                }
                s.swap(i, j);
                i += 1;
                j += 1;
            }
        }
        String::from_utf8(s).unwrap()
    }
}
'''

FILES["3090_maximum_length_substring_with_two_occurrences"] = r'''// LeetCode 3090 - Maximum Length Substring With Two Occurrences
// https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

impl Solution {
    pub fn maximum_length_substring(s: String) -> i32 {
        let b = s.as_bytes();
        let mut l = 0usize;
        let mut ans = 0i32;
        let mut cnt = [0i32; 26];
        for r in 0..b.len() {
            let idx = (b[r] - b'a') as usize;
            cnt[idx] += 1;
            while cnt[idx] > 2 {
                cnt[(b[l] - b'a') as usize] -= 1;
                l += 1;
            }
            ans = ans.max((r - l + 1) as i32);
        }
        ans
    }
}
'''

FILES["3091_apply_operations_to_make_sum_of_array_greater_than_or_equal_to_k"] = r'''// LeetCode 3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
// https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

impl Solution {
    pub fn min_operations(k: i32) -> i32 {
        let mut ans = k;
        for a in 0..k {
            let x = a + 1;
            let b = (k + x - 1) / x - 1;
            ans = ans.min(a + b);
        }
        ans
    }
}
'''

FILES["3092_most_frequent_ids"] = r'''// LeetCode 3092 - Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/

use std::collections::{BinaryHeap, HashMap};

impl Solution {
    pub fn most_frequent_ids(nums: Vec<i32>, freq: Vec<i32>) -> Vec<i64> {
        let n = nums.len();
        let mut cnt: HashMap<i32, i64> = HashMap::new();
        let mut lazy: HashMap<i64, i32> = HashMap::new();
        let mut ans = vec![0i64; n];
        let mut pq = BinaryHeap::new();
        for i in 0..n {
            let x = nums[i];
            let f = freq[i] as i64;
            let old = *cnt.get(&x).unwrap_or(&0);
            *lazy.entry(old).or_insert(0) += 1;
            let now = old + f;
            cnt.insert(x, now);
            pq.push(now);
            while let Some(&top) = pq.peek() {
                if *lazy.get(&top).unwrap_or(&0) > 0 {
                    *lazy.get_mut(&top).unwrap() -= 1;
                    pq.pop();
                } else {
                    break;
                }
            }
            if let Some(&top) = pq.peek() {
                ans[i] = top;
            }
        }
        ans
    }
}
'''

FILES["3093_longest_common_suffix_queries"] = r'''// LeetCode 3093 - Longest Common Suffix Queries
// https://leetcode.com/problems/longest-common-suffix-queries/

struct Trie {
    children: [Option<Box<Trie>>; 26],
    length: i32,
    idx: i32,
}

impl Trie {
    fn new() -> Self {
        const INF: i32 = 1 << 30;
        Self {
            children: Default::default(),
            length: INF,
            idx: INF,
        }
    }

    fn insert(&mut self, w: &[u8], i: i32) {
        let mut node = self;
        if node.length > w.len() as i32 {
            node.length = w.len() as i32;
            node.idx = i;
        }
        for k in (0..w.len()).rev() {
            let id = (w[k] - b'a') as usize;
            node = node.children[id].get_or_insert_with(|| Box::new(Trie::new()));
            if node.length > w.len() as i32 {
                node.length = w.len() as i32;
                node.idx = i;
            }
        }
    }

    fn query(&self, w: &[u8]) -> i32 {
        let mut node = self;
        for k in (0..w.len()).rev() {
            let id = (w[k] - b'a') as usize;
            match &node.children[id] {
                Some(child) => node = child,
                None => break,
            }
        }
        node.idx
    }
}

impl Solution {
    pub fn string_indices(words_container: Vec<String>, words_query: Vec<String>) -> Vec<i32> {
        let mut trie = Trie::new();
        for (i, w) in words_container.iter().enumerate() {
            trie.insert(w.as_bytes(), i as i32);
        }
        words_query.iter().map(|w| trie.query(w.as_bytes())).collect()
    }
}
'''

FILES["3094_guess_the_number_using_bitwise_questions_ii"] = r'''// LeetCode 3094 - Guess the Number Using Bitwise Questions II
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

fn common_bits(num: i32) -> i32 {
    let _ = num;
    0
}

impl Solution {
    pub fn find_number() -> i32 {
        let mut n = 0i32;
        for i in 0..32 {
            let bit = 1i32.wrapping_shl(i);
            let count1 = common_bits(bit);
            let count2 = common_bits(bit);
            if count1 > count2 {
                n |= bit;
            }
        }
        n
    }
}
'''

FILES["3095_shortest_subarray_with_or_at_least_k_i"] = r'''// LeetCode 3095 - Shortest Subarray With OR at Least K I
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/

impl Solution {
    pub fn minimum_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut cnt = [0i32; 32];
        let mut ans = n as i32 + 1;
        let mut s = 0i32;
        let mut i = 0usize;
        for j in 0..n {
            let x = nums[j];
            s |= x;
            for h in 0..32 {
                if (x >> h) & 1 == 1 {
                    cnt[h] += 1;
                }
            }
            while s >= k && i <= j {
                ans = ans.min((j - i + 1) as i32);
                for h in 0..32 {
                    if (nums[i] >> h) & 1 == 1 {
                        cnt[h] -= 1;
                        if cnt[h] == 0 {
                            s ^= 1 << h;
                        }
                    }
                }
                i += 1;
            }
        }
        if ans == n as i32 + 1 { -1 } else { ans }
    }
}
'''

FILES["3096_minimum_levels_to_gain_more_points"] = r'''// LeetCode 3096 - Minimum Levels to Gain More Points
// https://leetcode.com/problems/minimum-levels-to-gain-more-points/

impl Solution {
    pub fn minimum_levels(possible: Vec<i32>) -> i32 {
        let s: i32 = possible.iter().map(|&x| if x == 0 { -1 } else { x }).sum();
        let mut t = 0;
        for i in 0..possible.len() - 1 {
            let x = if possible[i] == 0 { -1 } else { possible[i] };
            t += x;
            if t > s - t {
                return i as i32 + 1;
            }
        }
        -1
    }
}
'''

FILES["3097_shortest_subarray_with_or_at_least_k_ii"] = r'''// LeetCode 3097 - Shortest Subarray With OR at Least K II
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

impl Solution {
    pub fn minimum_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut cnt = [0i32; 32];
        let mut ans = n as i32 + 1;
        let mut s = 0i32;
        let mut i = 0usize;
        for j in 0..n {
            let x = nums[j];
            s |= x;
            for h in 0..32 {
                if (x >> h) & 1 == 1 {
                    cnt[h] += 1;
                }
            }
            while s >= k && i <= j {
                ans = ans.min((j - i + 1) as i32);
                for h in 0..32 {
                    if (nums[i] >> h) & 1 == 1 {
                        cnt[h] -= 1;
                        if cnt[h] == 0 {
                            s ^= 1 << h;
                        }
                    }
                }
                i += 1;
            }
        }
        if ans == n as i32 + 1 { -1 } else { ans }
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
