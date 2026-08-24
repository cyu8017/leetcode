#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

def add(folder, body):
    FILES[folder] = body.strip() + "\n"

add("2859_sum_of_values_at_indices_with_k_set_bits", r'''
// LeetCode 2859 - Sum of Values at Indices With K Set Bits
// https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

impl Solution {
    pub fn sum_indices_with_k_set_bits(nums: Vec<i32>, k: i32) -> i32 {
        let mut ans = 0;
        for (i, &v) in nums.iter().enumerate() {
            let mut bits = 0;
            let mut x = i;
            while x > 0 {
                bits += (x & 1) as i32;
                x >>= 1;
            }
            if bits == k {
                ans += v;
            }
        }
        ans
    }
}
''')

add("2860_happy_students", r'''
// LeetCode 2860 - Happy Students
// https://leetcode.com/problems/happy-students/

impl Solution {
    pub fn count_ways(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let mut ans = 0;
        if nums[0] > 0 {
            ans += 1;
        }
        for i in 0..n {
            let selected = (i + 1) as i32;
            if selected > nums[i] && (i == n - 1 || selected < nums[i + 1]) {
                ans += 1;
            }
        }
        ans
    }
}
''')

add("2861_maximum_number_of_alloys", r'''
// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/

impl Solution {
    pub fn max_number_of_alloys(
        n: i32,
        _k: i32,
        budget: i32,
        composition: Vec<Vec<i32>>,
        stock: Vec<i32>,
        cost: Vec<i32>,
    ) -> i32 {
        let n = n as usize;
        let ok = |machines: i64| -> bool {
            for comp in &composition {
                let mut spend = 0i64;
                for i in 0..n {
                    let need = machines * comp[i] as i64 - stock[i] as i64;
                    if need > 0 {
                        spend += need * cost[i] as i64;
                    }
                }
                if spend <= budget as i64 {
                    return true;
                }
            }
            false
        };
        let mut lo = 0i64;
        let mut hi = 1_000_000_000i64;
        let mut ans = 0i64;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        ans as i32
    }
}
''')

add("2862_maximum_element_sum_of_a_complete_subset_of_indices", r'''
// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_sum(nums: Vec<i32>) -> i64 {
        fn square_free(mut x: i32) -> i32 {
            let mut res = 1;
            let mut p = 2;
            while p * p <= x {
                let mut cnt = 0;
                while x % p == 0 {
                    x /= p;
                    cnt += 1;
                }
                if cnt % 2 == 1 {
                    res *= p;
                }
                p += 1;
            }
            if x > 1 {
                res *= x;
            }
            res
        }
        let n = nums.len();
        let mut groups: HashMap<i32, i64> = HashMap::new();
        let mut ans = 0i64;
        for i in 1..=n {
            let sf = square_free(i as i32);
            let e = groups.entry(sf).or_insert(0);
            *e += nums[i - 1] as i64;
            if *e > ans {
                ans = *e;
            }
        }
        ans
    }
}
''')

add("2863_maximum_length_of_semi_decreasing_subarrays", r'''
// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0i32;
        let mut st: Vec<usize> = Vec::new();
        for i in (0..n).rev() {
            if st.is_empty() || nums[i] > nums[*st.last().unwrap()] {
                st.push(i);
            }
        }
        for i in 0..n {
            while !st.is_empty() && nums[i] > nums[*st.last().unwrap()] {
                let j = st.pop().unwrap();
                ans = ans.max((j - i + 1) as i32);
            }
        }
        ans
    }
}
''')

add("2864_maximum_odd_binary_number", r'''
// LeetCode 2864 - Maximum Odd Binary Number
// https://leetcode.com/problems/maximum-odd-binary-number/

impl Solution {
    pub fn maximum_odd_binary_number(s: String) -> String {
        let ones = s.bytes().filter(|&c| c == b'1').count();
        let zeros = s.len() - ones;
        let mut b = String::with_capacity(s.len());
        for _ in 0..ones.saturating_sub(1) {
            b.push('1');
        }
        for _ in 0..zeros {
            b.push('0');
        }
        b.push('1');
        b
    }
}
''')

add("2865_beautiful_towers_i", r'''
// LeetCode 2865 - Beautiful Towers I
// https://leetcode.com/problems/beautiful-towers-i/

impl Solution {
    pub fn maximum_sum_of_heights(heights: Vec<i32>) -> i64 {
        let n = heights.len();
        let mut ans = 0i64;
        for peak in 0..n {
            let mut sum = heights[peak] as i64;
            let mut mn = heights[peak];
            for i in (0..peak).rev() {
                if heights[i] < mn {
                    mn = heights[i];
                }
                sum += mn as i64;
            }
            mn = heights[peak];
            for i in peak + 1..n {
                if heights[i] < mn {
                    mn = heights[i];
                }
                sum += mn as i64;
            }
            ans = ans.max(sum);
        }
        ans
    }
}
''')

add("2866_beautiful_towers_ii", r'''
// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

impl Solution {
    pub fn maximum_sum_of_heights(max_heights: Vec<i32>) -> i64 {
        let n = max_heights.len();
        let mut left = vec![0i64; n];
        let mut st: Vec<i32> = vec![-1];
        let mut sum = 0i64;
        for i in 0..n {
            while st.len() > 1 && max_heights[*st.last().unwrap() as usize] >= max_heights[i] {
                let j = st.pop().unwrap();
                sum -= max_heights[j as usize] as i64 * (j - *st.last().unwrap()) as i64;
            }
            sum += max_heights[i] as i64 * (i as i32 - *st.last().unwrap()) as i64;
            left[i] = sum;
            st.push(i as i32);
        }
        let mut right = vec![0i64; n];
        st = vec![n as i32];
        sum = 0;
        for i in (0..n).rev() {
            while st.len() > 1 && max_heights[*st.last().unwrap() as usize] >= max_heights[i] {
                let j = st.pop().unwrap();
                sum -= max_heights[j as usize] as i64 * (*st.last().unwrap() - j) as i64;
            }
            sum += max_heights[i] as i64 * (*st.last().unwrap() - i as i32) as i64;
            right[i] = sum;
            st.push(i as i32);
        }
        let mut ans = 0i64;
        for i in 0..n {
            ans = ans.max(left[i] + right[i] - max_heights[i] as i64);
        }
        ans
    }
}
''')

add("2867_count_valid_paths_in_a_tree", r'''
// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

impl Solution {
    pub fn count_paths(n: i32, edges: Vec<Vec<i32>>) -> i64 {
        let n = n as usize;
        let mut is_prime = vec![true; n + 1];
        is_prime[0] = false;
        is_prime[1] = false;
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
        let mut g = vec![Vec::new(); n + 1];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        fn dfs(u: usize, p: usize, is_prime: &[bool], g: &[Vec<usize>]) -> i32 {
            if is_prime[u] {
                return 0;
            }
            let mut sz = 1;
            for &v in &g[u] {
                if v != p {
                    sz += dfs(v, u, is_prime, g);
                }
            }
            sz
        }
        let mut ans = 0i64;
        for u in 1..=n {
            if !is_prime[u] {
                continue;
            }
            let mut total = 0i64;
            for &v in &g[u] {
                let c = dfs(v, u, &is_prime, &g) as i64;
                ans += c;
                ans += total * c;
                total += c;
            }
        }
        ans
    }
}
''')

add("2868_the_wording_game", r'''
// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

impl Solution {
    pub fn can_alice_win(a: Vec<String>, b: Vec<String>) -> bool {
        let mut i = 0usize;
        let mut j = 0usize;
        let mut last: u8 = 0;
        let mut alice = true;
        loop {
            if alice {
                while i < a.len() && a[i].as_bytes()[0] <= last {
                    i += 1;
                }
                if i == a.len() {
                    return false;
                }
                last = *a[i].as_bytes().last().unwrap();
                i += 1;
            } else {
                while j < b.len() && b[j].as_bytes()[0] <= last {
                    j += 1;
                }
                if j == b.len() {
                    return true;
                }
                last = *b[j].as_bytes().last().unwrap();
                j += 1;
            }
            alice = !alice;
        }
    }
}
''')

add("2869_minimum_operations_to_collect_elements", r'''
// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

use std::collections::HashSet;

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut need: HashSet<i32> = (1..=k).collect();
        for i in (0..nums.len()).rev() {
            need.remove(&nums[i]);
            if need.is_empty() {
                return (nums.len() - i) as i32;
            }
        }
        nums.len() as i32
    }
}
''')

add("2870_minimum_number_of_operations_to_make_array_empty", r'''
// LeetCode 2870 - Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

use std::collections::HashMap;

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for v in nums {
            *freq.entry(v).or_insert(0) += 1;
        }
        let mut ans = 0;
        for c in freq.values() {
            if *c == 1 {
                return -1;
            }
            ans += (*c + 2) / 3;
        }
        ans
    }
}
''')

add("2871_split_array_into_maximum_number_of_subarrays", r'''
// LeetCode 2871 - Split Array Into Maximum Number of Subarrays
// https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

impl Solution {
    pub fn max_subarrays(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut cur = -1i32;
        for v in nums {
            if cur == -1 {
                cur = v;
            } else {
                cur &= v;
            }
            if cur == 0 {
                ans += 1;
                cur = -1;
            }
        }
        if ans == 0 { 1 } else { ans }
    }
}
''')

add("2872_maximum_number_of_k_divisible_components", r'''
// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

impl Solution {
    pub fn max_k_divisible_components(n: i32, edges: Vec<Vec<i32>>, values: Vec<i32>, k: i32) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        fn dfs(u: usize, p: i32, g: &[Vec<usize>], values: &[i32], k: i32, ans: &mut i32) -> i32 {
            let mut sum = values[u] % k;
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                sum = (sum + dfs(v, u as i32, g, values, k, ans)) % k;
            }
            if sum == 0 {
                *ans += 1;
            }
            sum
        }
        let mut ans = 0;
        dfs(0, -1, &g, &values, k, &mut ans);
        ans
    }
}
''')

add("2873_maximum_value_of_an_ordered_triplet_i", r'''
// LeetCode 2873 - Maximum Value of an Ordered Triplet I
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut ans = 0i64;
        for i in 0..n {
            for j in i + 1..n {
                for k in j + 1..n {
                    let cand = (nums[i] - nums[j]) as i64 * nums[k] as i64;
                    if cand > ans {
                        ans = cand;
                    }
                }
            }
        }
        ans
    }
}
''')

add("2874_maximum_value_of_an_ordered_triplet_ii", r'''
// LeetCode 2874 - Maximum Value of an Ordered Triplet II
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        let mut max_i = 0i64;
        let mut max_diff = 0i64;
        for v in nums {
            let val = v as i64;
            if max_diff * val > ans {
                ans = max_diff * val;
            }
            if max_i - val > max_diff {
                max_diff = max_i - val;
            }
            if val > max_i {
                max_i = val;
            }
        }
        ans
    }
}
''')

add("2875_minimum_size_subarray_in_infinite_array", r'''
// LeetCode 2875 - Minimum Size Subarray in Infinite Array
// https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

impl Solution {
    pub fn min_size_subarray(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let total: i64 = nums.iter().map(|&v| v as i64).sum();
        let mut ans = 1 << 30;
        if total > 0 {
            let loops = target as i64 / total;
            let remain = (target as i64 % total) as i32;
            if remain == 0 {
                return (loops * n as i64) as i32;
            }
            let mut arr = nums.clone();
            arr.extend_from_slice(&nums);
            let mut left = 0usize;
            let mut sum = 0i32;
            let mut best = 1 << 30;
            for right in 0..arr.len() {
                sum += arr[right];
                while sum > remain && left <= right {
                    sum -= arr[left];
                    left += 1;
                }
                if sum == remain && (right - left + 1) as i32 < best {
                    best = (right - left + 1) as i32;
                }
            }
            if best < (1 << 30) {
                ans = (loops * n as i64) as i32 + best;
            }
        }
        if ans == (1 << 30) { -1 } else { ans }
    }
}
''')

add("2876_count_visited_nodes_in_a_directed_graph", r'''
// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

impl Solution {
    pub fn count_visited_nodes(edges: Vec<i32>) -> Vec<i32> {
        let n = edges.len();
        let mut ans = vec![0i32; n];
        let mut state = vec![0i32; n];
        fn dfs(u: usize, edges: &[i32], ans: &mut [i32], state: &mut [i32], stack: &mut Vec<usize>) {
            state[u] = 1;
            stack.push(u);
            let v = edges[u] as usize;
            if state[v] == 0 {
                dfs(v, edges, ans, state, stack);
            } else if state[v] == 1 {
                let mut idx = stack.len() - 1;
                while stack[idx] != v {
                    idx -= 1;
                }
                let cyc = (stack.len() - idx) as i32;
                for i in idx..stack.len() {
                    ans[stack[i]] = cyc;
                }
            }
            if ans[u] == 0 {
                ans[u] = ans[edges[u] as usize] + 1;
            }
            state[u] = 2;
            stack.pop();
        }
        let mut stack = Vec::new();
        for i in 0..n {
            if state[i] == 0 {
                dfs(i, &edges, &mut ans, &mut state, &mut stack);
            }
        }
        ans
    }
}
''')

# Pandas stand-ins: C++ stubs; implement Vec-based equivalents of the Python logic.
add("2877_create_a_dataframe_from_list", r'''
// LeetCode 2877 - Create a DataFrame from List
// https://leetcode.com/problems/create-a-dataframe-from-list/

impl Solution {
    pub fn create_dataframe(student_data: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        student_data
    }
}
''')

add("2878_get_the_size_of_a_dataframe", r'''
// LeetCode 2878 - Get the Size of a DataFrame
// https://leetcode.com/problems/get-the-size-of-a-dataframe/

impl Solution {
    pub fn get_dataframe_size(players: Vec<Vec<i32>>) -> Vec<i32> {
        if players.is_empty() {
            return vec![0, 0];
        }
        vec![players.len() as i32, players[0].len() as i32]
    }
}
''')

add("2879_display_the_first_three_rows", r'''
// LeetCode 2879 - Display the First Three Rows
// https://leetcode.com/problems/display-the-first-three-rows/

impl Solution {
    pub fn select_first_rows(employees: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        employees.into_iter().take(3).collect()
    }
}
''')

add("2880_select_data", r'''
// LeetCode 2880 - Select Data
// https://leetcode.com/problems/select-data/

impl Solution {
    pub fn select_data(students: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        students
            .into_iter()
            .filter(|r| !r.is_empty() && r[0] == 101)
            .map(|r| r[1..].to_vec())
            .collect()
    }
}
''')

add("2881_create_a_new_column", r'''
// LeetCode 2881 - Create a New Column
// https://leetcode.com/problems/create-a-new-column/

impl Solution {
    pub fn create_bonus_column(employees: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        employees
            .into_iter()
            .map(|mut r| {
                let salary = *r.last().unwrap_or(&0);
                r.push(salary * 2);
                r
            })
            .collect()
    }
}
''')

add("2882_drop_duplicate_rows", r'''
// LeetCode 2882 - Drop Duplicate Rows
// https://leetcode.com/problems/drop-duplicate-rows/

use std::collections::HashSet;

impl Solution {
    pub fn drop_duplicate_emails(customers: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut seen = HashSet::new();
        let mut out = Vec::new();
        for r in customers {
            let email = *r.last().unwrap_or(&0);
            if seen.insert(email) {
                out.push(r);
            }
        }
        out
    }
}
''')

add("2883_drop_missing_data", r'''
// LeetCode 2883 - Drop Missing Data
// https://leetcode.com/problems/drop-missing-data/

impl Solution {
    pub fn drop_missing_data(students: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        students
            .into_iter()
            .filter(|r| r.len() < 2 || r[1] != 0)
            .collect()
    }
}
''')

add("2884_modify_columns", r'''
// LeetCode 2884 - Modify Columns
// https://leetcode.com/problems/modify-columns/

impl Solution {
    pub fn modify_salary_column(employees: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        employees
            .into_iter()
            .map(|mut r| {
                if let Some(last) = r.last_mut() {
                    *last *= 2;
                }
                r
            })
            .collect()
    }
}
''')

add("2885_rename_columns", r'''
// LeetCode 2885 - Rename Columns
// https://leetcode.com/problems/rename-columns/

impl Solution {
    pub fn rename_columns(students: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        students
    }
}
''')

add("2886_change_data_type", r'''
// LeetCode 2886 - Change Data Type
// https://leetcode.com/problems/change-data-type/

impl Solution {
    pub fn change_datatype(students: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        students
    }
}
''')

add("2887_fill_missing_data", r'''
// LeetCode 2887 - Fill Missing Data
// https://leetcode.com/problems/fill-missing-data/

impl Solution {
    pub fn fill_missing_values(products: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        products
            .into_iter()
            .map(|mut r| {
                if r.len() > 1 && r[1] < 0 {
                    r[1] = 0;
                }
                r
            })
            .collect()
    }
}
''')

add("2888_reshape_data_concatenate", r'''
// LeetCode 2888 - Reshape Data: Concatenate
// https://leetcode.com/problems/reshape-data-concatenate/

impl Solution {
    pub fn concatenate_tables(mut df1: Vec<Vec<i32>>, df2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        df1.extend(df2);
        df1
    }
}
''')

add("2889_reshape_data_pivot", r'''
// LeetCode 2889 - Reshape Data: Pivot
// https://leetcode.com/problems/reshape-data-pivot/

use std::collections::HashMap;

impl Solution {
    pub fn pivot_table(weather: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut months = Vec::new();
        let mut by_month: HashMap<i32, HashMap<i32, i32>> = HashMap::new();
        for r in weather {
            if r.len() < 3 {
                continue;
            }
            let (city, month, temperature) = (r[0], r[1], r[2]);
            if !by_month.contains_key(&month) {
                months.push(month);
            }
            by_month.entry(month).or_default().insert(city, temperature);
        }
        months
            .into_iter()
            .map(|month| {
                let mut row = vec![month];
                if let Some(cities) = by_month.get(&month) {
                    let mut keys: Vec<i32> = cities.keys().copied().collect();
                    keys.sort_unstable();
                    for k in keys {
                        row.push(cities[&k]);
                    }
                }
                row
            })
            .collect()
    }
}
''')

add("2890_reshape_data_melt", r'''
// LeetCode 2890 - Reshape Data: Melt
// https://leetcode.com/problems/reshape-data-melt/

impl Solution {
    pub fn melt_table(report: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut out = Vec::new();
        for r in report {
            if r.is_empty() {
                continue;
            }
            let product = r[0];
            for (q, &sales) in r.iter().enumerate().skip(1) {
                out.push(vec![product, q as i32, sales]);
            }
        }
        out
    }
}
''')

add("2891_method_chaining", r'''
// LeetCode 2891 - Method Chaining
// https://leetcode.com/problems/method-chaining/

impl Solution {
    pub fn find_heavy_animals(mut animals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        animals.retain(|r| r.len() > 3 && r[3] > 100);
        animals.sort_by(|a, b| b[3].cmp(&a[3]));
        animals.into_iter().map(|r| vec![r[0]]).collect()
    }
}
''')

def main():
    n = 0
    for folder, body in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(body, encoding="utf-8", newline="\n")
        n += 1
        print("wrote", folder)
    print("batch_b", n)

if __name__ == "__main__":
    main()
