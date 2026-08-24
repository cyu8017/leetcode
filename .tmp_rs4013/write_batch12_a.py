#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

def add(folder, body):
    FILES[folder] = body.strip() + "\n"

add("2830_maximize_the_profit_as_the_salesman", r'''
// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

impl Solution {
    pub fn maximize_the_profit(n: i32, offers: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut by_end = vec![Vec::new(); n];
        for o in offers {
            by_end[o[1] as usize].push(o);
        }
        let mut dp = vec![0i32; n + 1];
        for end in 0..n {
            dp[end + 1] = dp[end];
            for o in &by_end[end] {
                dp[end + 1] = dp[end + 1].max(dp[o[0] as usize] + o[2]);
            }
        }
        dp[n]
    }
}
''')

add("2831_find_the_longest_equal_subarray", r'''
// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

use std::collections::HashMap;

impl Solution {
    pub fn longest_equal_subarray(nums: Vec<i32>, k: i32) -> i32 {
        let mut pos: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in nums.iter().enumerate() {
            pos.entry(v).or_default().push(i);
        }
        let mut ans = 0i32;
        for p in pos.values() {
            let mut left = 0usize;
            for right in 0..p.len() {
                while p[right] - p[left] - (right - left) > k as usize {
                    left += 1;
                }
                ans = ans.max((right - left + 1) as i32);
            }
        }
        ans
    }
}
''')

add("2832_maximal_range_that_each_element_is_maximum_in_it", r'''
// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut left = vec![0i32; n];
        let mut right = vec![0i32; n];
        let mut st: Vec<usize> = Vec::new();
        for i in 0..n {
            while !st.is_empty() && nums[*st.last().unwrap()] < nums[i] {
                st.pop();
            }
            left[i] = if st.is_empty() { -1 } else { *st.last().unwrap() as i32 };
            st.push(i);
        }
        st.clear();
        for i in (0..n).rev() {
            while !st.is_empty() && nums[*st.last().unwrap()] <= nums[i] {
                st.pop();
            }
            right[i] = if st.is_empty() { n as i32 } else { *st.last().unwrap() as i32 };
            st.push(i);
        }
        (0..n).map(|i| right[i] - left[i] - 1).collect()
    }
}
''')

add("2833_furthest_point_from_origin", r'''
// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

impl Solution {
    pub fn furthest_distance_from_origin(moves: String) -> i32 {
        let mut l = 0i32;
        let mut r = 0i32;
        let mut u = 0i32;
        for c in moves.chars() {
            match c {
                'L' => l += 1,
                'R' => r += 1,
                _ => u += 1,
            }
        }
        (l - r).abs() + u
    }
}
''')

add("2834_find_the_minimum_possible_sum_of_a_beautiful_array", r'''
// LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
// https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

impl Solution {
    pub fn minimum_possible_sum(n: i32, target: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as i64;
        let target = target as i64;
        let m = target / 2;
        if n <= m {
            return (n * (n + 1) / 2 % MOD) as i32;
        }
        let mut sum = m * (m + 1) / 2;
        let remain = n - m;
        sum += remain * target + remain * (remain - 1) / 2;
        (sum % MOD) as i32
    }
}
''')

add("2835_minimum_operations_to_form_subsequence_with_target_sum", r'''
// LeetCode 2835 - Minimum Operations to Form Subsequence With Target Sum
// https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, target: i32) -> i32 {
        let mut cnt = [0i32; 32];
        let mut sum = 0i64;
        for &v in &nums {
            sum += v as i64;
            let mut b = 0;
            while (1 << b) < v {
                b += 1;
            }
            cnt[b as usize] += 1;
        }
        if sum < target as i64 {
            return -1;
        }
        let mut ans = 0i32;
        for i in 0..31 {
            if (target & (1 << i)) != 0 {
                if cnt[i] > 0 {
                    cnt[i] -= 1;
                } else {
                    let mut j = i + 1;
                    while j < 32 && cnt[j] == 0 {
                        j += 1;
                    }
                    if j == 32 {
                        return -1;
                    }
                    while j > i {
                        cnt[j] -= 1;
                        cnt[j - 1] += 2;
                        ans += 1;
                        j -= 1;
                    }
                    cnt[i] -= 1;
                }
            }
            cnt[i + 1] += cnt[i] / 2;
        }
        ans
    }
}
''')

add("2836_maximize_value_of_function_in_a_ball_passing_game", r'''
// LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

impl Solution {
    pub fn get_max_function_value(receiver: Vec<i32>, k: i64) -> i64 {
        let n = receiver.len();
        const LOG: usize = 36;
        let mut up = vec![vec![0usize; n]; LOG];
        let mut sum = vec![vec![0i64; n]; LOG];
        for i in 0..n {
            up[0][i] = receiver[i] as usize;
            sum[0][i] = receiver[i] as i64;
        }
        for j in 1..LOG {
            for i in 0..n {
                let mid = up[j - 1][i];
                up[j][i] = up[j - 1][mid];
                sum[j][i] = sum[j - 1][i] + sum[j - 1][mid];
            }
        }
        let mut ans = 0i64;
        for i in 0..n {
            let mut cur = i;
            let mut total = i as i64;
            let mut kk = k;
            for j in 0..LOG {
                if (kk & (1i64 << j)) != 0 {
                    total += sum[j][cur];
                    cur = up[j][cur];
                }
            }
            ans = ans.max(total);
        }
        ans
    }
}
''')

add("2838_maximum_coins_heroes_can_collect", r'''
// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/

impl Solution {
    pub fn maximum_coins(heroes: Vec<i32>, monsters: Vec<i32>, coins: Vec<i32>) -> Vec<i64> {
        let n = monsters.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_unstable_by_key(|&i| monsters[i]);
        let mut pref = vec![0i64; n + 1];
        let mut ms = vec![0i32; n];
        for i in 0..n {
            ms[i] = monsters[idx[i]];
            pref[i + 1] = pref[i] + coins[idx[i]] as i64;
        }
        heroes
            .into_iter()
            .map(|h| {
                let p = ms.partition_point(|&m| m <= h);
                pref[p]
            })
            .collect()
    }
}
''')

add("2839_check_if_strings_can_be_made_equal_with_operations_i", r'''
// LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

impl Solution {
    pub fn can_be_equal(s1: String, s2: String) -> bool {
        let a: Vec<u8> = s1.bytes().collect();
        let b: Vec<u8> = s2.bytes().collect();
        let mut even1 = [a[0], a[2]];
        let mut even2 = [b[0], b[2]];
        let mut odd1 = [a[1], a[3]];
        let mut odd2 = [b[1], b[3]];
        even1.sort_unstable();
        even2.sort_unstable();
        odd1.sort_unstable();
        odd2.sort_unstable();
        even1 == even2 && odd1 == odd2
    }
}
''')

add("2840_check_if_strings_can_be_made_equal_with_operations_ii", r'''
// LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

impl Solution {
    pub fn check_strings(s1: String, s2: String) -> bool {
        let mut even1 = [0i32; 26];
        let mut odd1 = [0i32; 26];
        let mut even2 = [0i32; 26];
        let mut odd2 = [0i32; 26];
        for (i, (c1, c2)) in s1.bytes().zip(s2.bytes()).enumerate() {
            if i % 2 == 0 {
                even1[(c1 - b'a') as usize] += 1;
                even2[(c2 - b'a') as usize] += 1;
            } else {
                odd1[(c1 - b'a') as usize] += 1;
                odd2[(c2 - b'a') as usize] += 1;
            }
        }
        even1 == even2 && odd1 == odd2
    }
}
''')

add("2841_maximum_sum_of_almost_unique_subarray", r'''
// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

use std::collections::HashMap;

impl Solution {
    pub fn max_sum(nums: Vec<i32>, m: i32, k: i32) -> i64 {
        let k = k as usize;
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut sum = 0i64;
        let mut ans = 0i64;
        for i in 0..nums.len() {
            *freq.entry(nums[i]).or_insert(0) += 1;
            sum += nums[i] as i64;
            if i >= k {
                let out = nums[i - k];
                sum -= out as i64;
                if let Some(c) = freq.get_mut(&out) {
                    *c -= 1;
                    if *c == 0 {
                        freq.remove(&out);
                    }
                }
            }
            if i + 1 >= k && freq.len() as i32 >= m {
                ans = ans.max(sum);
            }
        }
        ans
    }
}
''')

add("2842_count_k_subsequences_of_a_string_with_maximum_beauty", r'''
// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

impl Solution {
    pub fn count_k_subsequences_with_max_beauty(s: String, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut freq = [0i32; 26];
        for c in s.bytes() {
            freq[(c - b'a') as usize] += 1;
        }
        let mut vals: Vec<i32> = freq.into_iter().filter(|&f| f > 0).collect();
        if vals.len() < k as usize {
            return 0;
        }
        vals.sort_unstable_by(|a, b| b.cmp(a));
        let threshold = vals[k as usize - 1];
        let mut need = 0i32;
        let mut avail = 0i32;
        let mut prod = 1i64;
        for v in vals {
            if v > threshold {
                prod = prod * v as i64 % MOD;
                need += 1;
            } else if v == threshold {
                avail += 1;
            }
        }
        let remain = k - need;
        fn mod_pow(mut a: i64, mut b: i64) -> i64 {
            const MOD: i64 = 1_000_000_007;
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
        fn comb(n: i32, r: i32) -> i64 {
            const MOD: i64 = 1_000_000_007;
            if r < 0 || r > n {
                return 0;
            }
            let mut num = 1i64;
            let mut den = 1i64;
            for i in 0..r {
                num = num * (n - i) as i64 % MOD;
                den = den * (i + 1) as i64 % MOD;
            }
            num * mod_pow(den, MOD - 2) % MOD
        }
        prod = prod * comb(avail, remain) % MOD;
        for _ in 0..remain {
            prod = prod * threshold as i64 % MOD;
        }
        prod as i32
    }
}
''')

add("2843_count_symmetric_integers", r'''
// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

impl Solution {
    pub fn count_symmetric_integers(low: i32, high: i32) -> i32 {
        let mut ans = 0;
        for x in low..=high {
            let s = x.to_string();
            let b = s.as_bytes();
            if b.len() % 2 == 1 {
                continue;
            }
            let mid = b.len() / 2;
            let mut a = 0;
            let mut c = 0;
            for i in 0..mid {
                a += (b[i] - b'0') as i32;
                c += (b[mid + i] - b'0') as i32;
            }
            if a == c {
                ans += 1;
            }
        }
        ans
    }
}
''')

add("2844_minimum_operations_to_make_a_special_number", r'''
// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

impl Solution {
    pub fn minimum_operations(num: String) -> i32 {
        let n = num.len() as i32;
        let bytes = num.as_bytes();
        let mut ans = n;
        if bytes.contains(&b'0') {
            ans = ans.min(n - 1);
        }
        for t in [b"00", b"25", b"50", b"75"] {
            let mut j = n - 1;
            while j >= 0 && bytes[j as usize] != t[1] {
                j -= 1;
            }
            if j < 0 {
                continue;
            }
            let mut i = j - 1;
            while i >= 0 && bytes[i as usize] != t[0] {
                i -= 1;
            }
            if i < 0 {
                continue;
            }
            ans = ans.min(n - i - 2);
        }
        ans
    }
}
''')

add("2845_count_of_interesting_subarrays", r'''
// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

use std::collections::HashMap;

impl Solution {
    pub fn count_interesting_subarrays(nums: Vec<i32>, modulo: i32, k: i32) -> i64 {
        let mut freq: HashMap<i32, i64> = HashMap::new();
        freq.insert(0, 1);
        let mut ans = 0i64;
        let mut pref = 0i32;
        for v in nums {
            if v % modulo == k {
                pref += 1;
            }
            let mut need = (pref - k) % modulo;
            if need < 0 {
                need += modulo;
            }
            ans += *freq.get(&need).unwrap_or(&0);
            *freq.entry(pref % modulo).or_insert(0) += 1;
        }
        ans
    }
}
''')

add("2846_minimum_edge_weight_equilibrium_queries_in_a_tree", r'''
// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

impl Solution {
    pub fn min_operations_queries(n: i32, edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push((e[1] as usize, e[2] as usize));
            g[e[1] as usize].push((e[0] as usize, e[2] as usize));
        }
        const LOG: usize = 15;
        let mut up = vec![vec![0usize; n]; LOG];
        let mut depth = vec![0i32; n];
        let mut cnt = vec![[0i32; 27]; n];
        fn dfs(
            u: usize,
            p: usize,
            g: &[Vec<(usize, usize)>],
            up: &mut [Vec<usize>],
            depth: &mut [i32],
            cnt: &mut [[i32; 27]],
        ) {
            up[0][u] = p;
            for &(v, w) in &g[u] {
                if v == p {
                    continue;
                }
                depth[v] = depth[u] + 1;
                cnt[v] = cnt[u];
                cnt[v][w] += 1;
                dfs(v, u, g, up, depth, cnt);
            }
        }
        dfs(0, 0, &g, &mut up, &mut depth, &mut cnt);
        for j in 1..LOG {
            for i in 0..n {
                up[j][i] = up[j - 1][up[j - 1][i]];
            }
        }
        let lca = |mut a: usize, mut b: usize, up: &[Vec<usize>], depth: &[i32]| -> usize {
            if depth[a] < depth[b] {
                std::mem::swap(&mut a, &mut b);
            }
            let mut diff = depth[a] - depth[b];
            for j in 0..LOG {
                if (diff & (1 << j)) != 0 {
                    a = up[j][a];
                }
            }
            if a == b {
                return a;
            }
            for j in (0..LOG).rev() {
                if up[j][a] != up[j][b] {
                    a = up[j][a];
                    b = up[j][b];
                }
            }
            up[0][a]
        };
        queries
            .into_iter()
            .map(|q| {
                let a = q[0] as usize;
                let b = q[1] as usize;
                let c = lca(a, b, &up, &depth);
                let total = depth[a] + depth[b] - 2 * depth[c];
                let mut best = 0;
                for w in 1..=26 {
                    let f = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w];
                    best = best.max(f);
                }
                total - best
            })
            .collect()
    }
}
''')

add("2847_smallest_number_with_given_digit_product", r'''
// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

impl Solution {
    pub fn smallest_number(n: i64) -> String {
        if n == 0 {
            return "0".to_string();
        }
        if n == 1 {
            return "1".to_string();
        }
        let mut n = n;
        let mut digits = String::new();
        for d in (2..=9).rev() {
            while n % d == 0 {
                digits.push(char::from(b'0' + d as u8));
                n /= d;
            }
        }
        if n > 1 {
            return "-1".to_string();
        }
        digits.chars().rev().collect()
    }
}
''')

add("2848_points_that_intersect_with_cars", r'''
// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/

impl Solution {
    pub fn number_of_points(nums: Vec<Vec<i32>>) -> i32 {
        let mut cov = [0i32; 102];
        for r in nums {
            for x in r[0]..=r[1] {
                cov[x as usize] = 1;
            }
        }
        cov.iter().sum()
    }
}
''')

add("2849_determine_if_a_cell_is_reachable_at_a_given_time", r'''
// LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

impl Solution {
    pub fn is_reachable_at_time(sx: i32, sy: i32, fx: i32, fy: i32, t: i32) -> bool {
        let need = (sx - fx).abs().max((sy - fy).abs());
        if need == 0 {
            return t != 1;
        }
        t >= need
    }
}
''')

add("2850_minimum_moves_to_spread_stones_over_grid", r'''
// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

impl Solution {
    pub fn minimum_moves(grid: Vec<Vec<i32>>) -> i32 {
        let mut extras = Vec::new();
        let mut zeros = Vec::new();
        for i in 0..3 {
            for j in 0..3 {
                if grid[i][j] == 0 {
                    zeros.push((i as i32, j as i32));
                } else if grid[i][j] > 1 {
                    for _ in 0..grid[i][j] - 1 {
                        extras.push((i as i32, j as i32));
                    }
                }
            }
        }
        if zeros.is_empty() {
            return 0;
        }
        fn dfs(i: usize, cost: i32, extras: &mut [(i32, i32)], zeros: &[(i32, i32)], best: &mut i32) {
            if cost >= *best {
                return;
            }
            if i == zeros.len() {
                *best = cost;
                return;
            }
            for j in 0..extras.len() {
                if extras[j].0 < 0 {
                    continue;
                }
                let e = extras[j];
                extras[j].0 = -1;
                let d = (e.0 - zeros[i].0).abs() + (e.1 - zeros[i].1).abs();
                dfs(i + 1, cost + d, extras, zeros, best);
                extras[j] = e;
            }
        }
        let mut best = 1 << 30;
        dfs(0, 0, &mut extras, &zeros, &mut best);
        best
    }
}
''')

add("2851_string_transformation", r'''
// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

impl Solution {
    pub fn number_of_ways(s: String, t: String, k: i64) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = s.len();
        let ss = format!("{}{}", s, s);
        if !ss[..2 * n - 1].contains(&t) {
            return 0;
        }
        let mut cnt = 0i32;
        for i in 0..n {
            if &ss[i..i + n] == t {
                cnt += 1;
            }
        }
        fn mod_pow(mut a: i64, mut b: i64) -> i64 {
            const MOD: i64 = 1_000_000_007;
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
        let same = s == t;
        let pk = mod_pow((n as i64 - 1).rem_euclid(MOD), k);
        let invn = mod_pow(n as i64, MOD - 2);
        let sign = if k % 2 == 1 { MOD - 1 } else { 1 };
        let ways_same = ((pk + ((n as i64 - 1) % MOD) * sign % MOD) % MOD * invn % MOD) as i32;
        let ways_diff = ((pk - sign + MOD) % MOD * invn % MOD) as i32;
        if same {
            ways_same
        } else {
            (ways_diff as i64 * cnt as i64 % MOD) as i32
        }
    }
}
''')

add("2852_sum_of_remoteness_of_all_cells", r'''
// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

use std::collections::VecDeque;

impl Solution {
    pub fn sum_remoteness(grid: Vec<Vec<i32>>) -> i64 {
        let m = grid.len();
        let n = grid[0].len();
        let mut seen = vec![vec![false; n]; m];
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
        let mut total = 0i64;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] != -1 {
                    total += grid[i][j] as i64;
                }
            }
        }
        let mut ans = 0i64;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == -1 || seen[i][j] {
                    continue;
                }
                let mut q = VecDeque::new();
                q.push_back((i, j));
                seen[i][j] = true;
                let mut sum = 0i64;
                let mut cnt = 0i64;
                while let Some((x, y)) = q.pop_front() {
                    sum += grid[x][y] as i64;
                    cnt += 1;
                    for (dx, dy) in dirs {
                        let ni = x as i32 + dx;
                        let nj = y as i32 + dy;
                        if ni >= 0
                            && nj >= 0
                            && (ni as usize) < m
                            && (nj as usize) < n
                            && !seen[ni as usize][nj as usize]
                            && grid[ni as usize][nj as usize] != -1
                        {
                            seen[ni as usize][nj as usize] = true;
                            q.push_back((ni as usize, nj as usize));
                        }
                    }
                }
                ans += (total - sum) * cnt;
            }
        }
        ans
    }
}
''')

add("2855_minimum_right_shifts_to_sort_the_array", r'''
// LeetCode 2855 - Minimum Right Shifts to Sort the Array
// https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

impl Solution {
    pub fn minimum_right_shifts(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut drops = 0;
        let mut idx = 0usize;
        for i in 0..n {
            if nums[i] > nums[(i + 1) % n] {
                drops += 1;
                idx = i;
            }
        }
        if drops == 0 {
            return 0;
        }
        if drops > 1 {
            return -1;
        }
        (n - 1 - idx) as i32
    }
}
''')

add("2856_minimum_array_length_after_pair_removals", r'''
// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

use std::collections::HashMap;

impl Solution {
    pub fn min_length_after_removals(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut mx = 0i32;
        for v in nums {
            let e = freq.entry(v).or_insert(0);
            *e += 1;
            mx = mx.max(*e);
        }
        if mx <= n / 2 {
            return n % 2;
        }
        2 * mx - n
    }
}
''')

add("2857_count_pairs_of_points_with_distance_k", r'''
// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

use std::collections::HashMap;

impl Solution {
    pub fn count_pairs(coordinates: Vec<Vec<i32>>, k: i32) -> i32 {
        let mut freq: HashMap<(i32, i32), i32> = HashMap::new();
        let mut ans = 0i32;
        for p in coordinates {
            let x = p[0];
            let y = p[1];
            for a in 0..=k {
                let b = k - a;
                ans += *freq.get(&(x ^ a, y ^ b)).unwrap_or(&0);
            }
            *freq.entry((x, y)).or_insert(0) += 1;
        }
        ans
    }
}
''')

add("2858_minimum_edge_reversals_so_every_node_is_reachable", r'''
// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

impl Solution {
    pub fn min_edge_reversals(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            g[u].push((v, 0i32));
            g[v].push((u, 1i32));
        }
        let mut ans = vec![0i32; n];
        fn dfs1(u: usize, p: i32, g: &[Vec<(usize, i32)>], ans: &mut [i32]) {
            for &(v, ww) in &g[u] {
                if v as i32 == p {
                    continue;
                }
                ans[0] += ww;
                dfs1(v, u as i32, g, ans);
            }
        }
        fn dfs2(u: usize, p: i32, g: &[Vec<(usize, i32)>], ans: &mut [i32]) {
            for &(v, ww) in &g[u] {
                if v as i32 == p {
                    continue;
                }
                if ww == 0 {
                    ans[v] = ans[u] + 1;
                } else {
                    ans[v] = ans[u] - 1;
                }
                dfs2(v, u as i32, g, ans);
            }
        }
        dfs1(0, -1, &g, &mut ans);
        dfs2(0, -1, &g, &mut ans);
        ans
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
    print("batch_a", n)

if __name__ == "__main__":
    main()
