#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3169_count_days_without_meetings"] = r'''// LeetCode 3169 - Count Days Without Meetings
// https://leetcode.com/problems/count-days-without-meetings/

impl Solution {
    pub fn count_days(days: i32, mut meetings: Vec<Vec<i32>>) -> i32 {
        meetings.sort_unstable();
        let mut last = 0;
        let mut ans = 0;
        for e in meetings {
            let st = e[0];
            let ed = e[1];
            if last < st {
                ans += st - last - 1;
            }
            last = last.max(ed);
        }
        ans += days - last;
        ans
    }
}
'''

FILES["3170_lexicographically_minimum_string_after_removing_stars"] = r'''// LeetCode 3170 - Lexicographically Minimum String After Removing Stars
// https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

impl Solution {
    pub fn clear_stars(s: String) -> String {
        let bytes = s.into_bytes();
        let n = bytes.len();
        let mut g: Vec<Vec<usize>> = vec![Vec::new(); 26];
        let mut rem = vec![false; n];
        for i in 0..n {
            if bytes[i] == b'*' {
                rem[i] = true;
                for j in 0..26 {
                    if let Some(idx) = g[j].pop() {
                        rem[idx] = true;
                        break;
                    }
                }
            } else {
                g[(bytes[i] - b'a') as usize].push(i);
            }
        }
        let mut ans = Vec::new();
        for i in 0..n {
            if !rem[i] {
                ans.push(bytes[i]);
            }
        }
        String::from_utf8(ans).unwrap()
    }
}
'''

FILES["3171_find_subarray_with_bitwise_or_closest_to_k"] = r'''// LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
// https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

impl Solution {
    pub fn minimum_difference(nums: Vec<i32>, k: i32) -> i32 {
        let mx = *nums.iter().max().unwrap();
        let m = if mx == 0 { 1 } else { 32 - mx.leading_zeros() as i32 };
        let mut cnt = vec![0; m as usize];
        let mut ans = i32::MAX;
        let mut s = 0;
        let mut i = 0;
        for j in 0..nums.len() {
            let x = nums[j];
            s |= x;
            ans = ans.min((s - k).abs());
            for h in 0..m {
                if (x >> h) & 1 == 1 {
                    cnt[h as usize] += 1;
                }
            }
            while i < j && s > k {
                let y = nums[i];
                for h in 0..m {
                    if (y >> h) & 1 == 1 {
                        cnt[h as usize] -= 1;
                        if cnt[h as usize] == 0 {
                            s ^= 1 << h;
                        }
                    }
                }
                ans = ans.min((s - k).abs());
                i += 1;
            }
        }
        ans
    }
}
'''

FILES["3173_bitwise_or_of_adjacent_elements"] = r'''// LeetCode 3173 - Bitwise OR of Adjacent Elements
// https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

impl Solution {
    pub fn or_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = Vec::new();
        for i in 1..nums.len() {
            ans.push(nums[i] | nums[i - 1]);
        }
        ans
    }
}
'''

FILES["3174_clear_digits"] = r'''// LeetCode 3174 - Clear Digits
// https://leetcode.com/problems/clear-digits/

impl Solution {
    pub fn clear_digits(s: String) -> String {
        let mut stk = String::new();
        for c in s.chars() {
            if c.is_ascii_digit() {
                stk.pop();
            } else {
                stk.push(c);
            }
        }
        stk
    }
}
'''

FILES["3175_find_the_first_player_to_win_k_games_in_a_row"] = r'''// LeetCode 3175 - Find The First Player to win K Games in a Row
// https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

impl Solution {
    pub fn find_winning_player(skills: Vec<i32>, k: i32) -> i32 {
        let n = skills.len() as i32;
        let k = k.min(n - 1);
        let mut i = 0;
        let mut cnt = 0;
        for j in 1..n {
            if skills[i as usize] < skills[j as usize] {
                i = j;
                cnt = 1;
            } else {
                cnt += 1;
            }
            if cnt == k {
                break;
            }
        }
        i
    }
}
'''

FILES["3176_find_the_maximum_length_of_a_good_subsequence_i"] = r'''// LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k = k as usize;
        let mut f = vec![vec![0; k + 1]; n];
        let mut ans = 0;
        for i in 0..n {
            for h in 0..=k {
                for j in 0..i {
                    if nums[i] == nums[j] {
                        f[i][h] = f[i][h].max(f[j][h]);
                    } else if h > 0 {
                        f[i][h] = f[i][h].max(f[j][h - 1]);
                    }
                }
                f[i][h] += 1;
            }
            ans = ans.max(f[i][k]);
        }
        ans
    }
}
'''

FILES["3177_find_the_maximum_length_of_a_good_subsequence_ii"] = r'''// LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k = k as usize;
        let mut f = vec![vec![0; k + 1]; n];
        let mut mp: Vec<HashMap<i32, i32>> = vec![HashMap::new(); k + 1];
        let mut g = vec![[0; 3]; k + 1];
        let mut ans = 0;
        for i in 0..n {
            for h in 0..=k {
                f[i][h] = *mp[h].get(&nums[i]).unwrap_or(&0);
                if h > 0 {
                    if g[h - 1][0] != nums[i] {
                        f[i][h] = f[i][h].max(g[h - 1][1]);
                    } else {
                        f[i][h] = f[i][h].max(g[h - 1][2]);
                    }
                }
                f[i][h] += 1;
                let e = mp[h].entry(nums[i]).or_insert(0);
                *e = (*e).max(f[i][h]);
                if g[h][0] != nums[i] {
                    if f[i][h] >= g[h][1] {
                        g[h][2] = g[h][1];
                        g[h][1] = f[i][h];
                        g[h][0] = nums[i];
                    } else if f[i][h] > g[h][2] {
                        g[h][2] = f[i][h];
                    }
                } else if f[i][h] > g[h][1] {
                    g[h][1] = f[i][h];
                }
                ans = ans.max(f[i][h]);
            }
        }
        ans
    }
}
'''

FILES["3178_find_the_child_who_has_the_ball_after_k_seconds"] = r'''// LeetCode 3178 - Find the Child Who Has the Ball After K Seconds
// https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/

impl Solution {
    pub fn number_of_child(n: i32, k: i32) -> i32 {
        let mut k = k;
        let m = k % (n - 1);
        k /= n - 1;
        if k % 2 == 1 {
            n - m - 1
        } else {
            m
        }
    }
}
'''

FILES["3179_find_the_n_th_value_after_k_seconds"] = r'''// LeetCode 3179 - Find the N-th Value After K Seconds
// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

impl Solution {
    pub fn value_after_k_seconds(n: i32, k: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = n as usize;
        let mut a = vec![1; n];
        for _ in 0..k {
            for i in 1..n {
                a[i] = (a[i] + a[i - 1]) % MOD;
            }
        }
        a[n - 1]
    }
}
'''

FILES["3180_maximum_total_reward_using_operations_i"] = r'''// LeetCode 3180 - Maximum Total Reward Using Operations I
// https://leetcode.com/problems/maximum-total-reward-using-operations-i/

impl Solution {
    pub fn max_total_reward(mut reward_values: Vec<i32>) -> i32 {
        reward_values.sort_unstable();
        let mx = *reward_values.last().unwrap();
        let mut f = vec![-1; (mx << 1) as usize];
        fn dfs(x: i32, reward_values: &[i32], f: &mut [i32]) -> i32 {
            if f[x as usize] != -1 {
                return f[x as usize];
            }
            let mut best = 0;
            for &v in reward_values.iter() {
                if v > x {
                    best = best.max(v + dfs(x + v, reward_values, f));
                }
            }
            f[x as usize] = best;
            best
        }
        dfs(0, &reward_values, &mut f)
    }
}
'''

FILES["3181_maximum_total_reward_using_operations_ii"] = r'''// LeetCode 3181 - Maximum Total Reward Using Operations II
// https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

impl Solution {
    pub fn max_total_reward(mut reward_values: Vec<i32>) -> i32 {
        reward_values.sort_unstable();
        reward_values.dedup();
        const N: usize = 100001;
        let mut f = vec![false; N];
        f[0] = true;
        for &v in &reward_values {
            let v = v as usize;
            let mut mask = f.clone();
            for i in v..N {
                mask[i] = false;
            }
            for i in 0..N {
                if mask[i] && i + v < N {
                    f[i + v] = true;
                }
            }
        }
        for i in (0..N).rev() {
            if f[i] {
                return i as i32;
            }
        }
        0
    }
}
'''

FILES["3183_the_number_of_ways_to_make_the_sum"] = r'''// LeetCode 3183 - The Number of Ways to Make the Sum
// https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/

impl Solution {
    pub fn number_of_ways(n: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let coins = [1, 2, 6];
        let n = n as usize;
        let mut f = vec![0; n + 1];
        f[0] = 1;
        for &x in &coins {
            for j in x..=n {
                f[j] = (f[j] + f[j - x]) % MOD;
            }
        }
        let mut ans = f[n];
        if n >= 4 {
            ans = (ans + f[n - 4]) % MOD;
        }
        if n >= 8 {
            ans = (ans + f[n - 8]) % MOD;
        }
        ans
    }
}
'''

FILES["3184_count_pairs_that_form_a_complete_day_i"] = r'''// LeetCode 3184 - Count Pairs That Form a Complete Day I
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

impl Solution {
    pub fn count_complete_day_pairs(hours: Vec<i32>) -> i32 {
        let mut cnt = [0; 24];
        let mut ans = 0;
        for x in hours {
            ans += cnt[(24 - x % 24) as usize % 24];
            cnt[(x % 24) as usize] += 1;
        }
        ans
    }
}
'''

FILES["3185_count_pairs_that_form_a_complete_day_ii"] = r'''// LeetCode 3185 - Count Pairs That Form a Complete Day II
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/

impl Solution {
    pub fn count_complete_day_pairs(hours: Vec<i32>) -> i64 {
        let mut cnt = [0i64; 24];
        let mut ans = 0i64;
        for x in hours {
            ans += cnt[(24 - x % 24) as usize % 24];
            cnt[(x % 24) as usize] += 1;
        }
        ans
    }
}
'''

FILES["3186_maximum_total_damage_with_spell_casting"] = r'''// LeetCode 3186 - Maximum Total Damage With Spell Casting
// https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_total_damage(mut power: Vec<i32>) -> i64 {
        let n = power.len();
        power.sort_unstable();
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut nxt = vec![0; n];
        for i in 0..n {
            *cnt.entry(power[i]).or_insert(0) += 1;
            nxt[i] = power.partition_point(|&x| x < power[i] + 3);
        }
        let mut f = vec![None; n];
        fn dfs(
            i: usize,
            n: usize,
            power: &[i32],
            cnt: &HashMap<i32, i32>,
            nxt: &[usize],
            f: &mut [Option<i64>],
        ) -> i64 {
            if i >= n {
                return 0;
            }
            if let Some(v) = f[i] {
                return v;
            }
            let c = *cnt.get(&power[i]).unwrap() as usize;
            let a = dfs(i + c, n, power, cnt, nxt, f);
            let b = power[i] as i64 * c as i64 + dfs(nxt[i], n, power, cnt, nxt, f);
            let res = a.max(b);
            f[i] = Some(res);
            res
        }
        dfs(0, n, &power, &cnt, &nxt, &mut f)
    }
}
'''

FILES["3187_peaks_in_array"] = r'''// LeetCode 3187 - Peaks in Array
// https://leetcode.com/problems/peaks-in-array/

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
    pub fn count_of_peaks(mut nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        let mut tree = Bit::new(n.saturating_sub(1));
        let update = |tree: &mut Bit, nums: &[i32], i: i32, val: i32| {
            if i <= 0 || i >= n as i32 - 1 {
                return;
            }
            let i = i as usize;
            if nums[i - 1] < nums[i] && nums[i] > nums[i + 1] {
                tree.update(i, val);
            }
        };
        for i in 1..n.saturating_sub(1) {
            update(&mut tree, &nums, i as i32, 1);
        }
        let mut ans = Vec::new();
        for q in queries {
            if q[0] == 1 {
                let l = q[1] + 1;
                let r = q[2] - 1;
                let t = if l <= r {
                    tree.query(r as usize) - tree.query((l - 1) as usize)
                } else {
                    0
                };
                ans.push(t);
            } else {
                let idx = q[1];
                let val = q[2];
                for i in idx - 1..=idx + 1 {
                    update(&mut tree, &nums, i, -1);
                }
                nums[idx as usize] = val;
                for i in idx - 1..=idx + 1 {
                    update(&mut tree, &nums, i, 1);
                }
            }
        }
        ans
    }
}
'''

FILES["3189_minimum_moves_to_get_a_peaceful_board"] = r'''// LeetCode 3189 - Minimum Moves to Get a Peaceful Board
// https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

impl Solution {
    pub fn min_moves(mut rooks: Vec<Vec<i32>>) -> i32 {
        let mut ans = 0;
        rooks.sort_unstable_by_key(|a| a[0]);
        for (i, r) in rooks.iter().enumerate() {
            ans += (r[0] - i as i32).abs();
        }
        rooks.sort_unstable_by_key(|a| a[1]);
        for (j, r) in rooks.iter().enumerate() {
            ans += (r[1] - j as i32).abs();
        }
        ans
    }
}
'''

FILES["3190_find_minimum_operations_to_make_all_elements_divisible_by_three"] = r'''// LeetCode 3190 - Find Minimum Operations to Make All Elements Divisible by Three
// https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        nums.iter().filter(|&&x| x % 3 != 0).count() as i32
    }
}
'''

FILES["3191_minimum_operations_to_make_binary_array_elements_equal_to_one_i"] = r'''// LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

impl Solution {
    pub fn min_operations(mut nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let n = nums.len();
        for i in 0..n {
            if nums[i] == 0 {
                if i + 2 >= n {
                    return -1;
                }
                nums[i + 1] ^= 1;
                nums[i + 2] ^= 1;
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["3192_minimum_operations_to_make_binary_array_elements_equal_to_one_ii"] = r'''// LeetCode 3192 - Minimum Operations to Make Binary Array Elements Equal to One II
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut v = 0;
        for x in nums {
            let x = x ^ v;
            if x == 0 {
                v ^= 1;
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["3193_count_the_number_of_inversions"] = r'''// LeetCode 3193 - Count the Number of Inversions
// https://leetcode.com/problems/count-the-number-of-inversions/

impl Solution {
    pub fn number_of_permutations(n: i32, requirements: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut req = vec![-1; n];
        for r in &requirements {
            req[r[0] as usize] = r[1];
        }
        if req[0] > 0 {
            return 0;
        }
        req[0] = 0;
        let m = *req.iter().max().unwrap() as usize;
        const MOD: i32 = 1_000_000_007;
        let mut f = vec![vec![0; m + 1]; n];
        f[0][0] = 1;
        for i in 1..n {
            let (mut l, mut r) = (0, m as i32);
            if req[i] >= 0 {
                l = req[i];
                r = req[i];
            }
            for j in l..=r {
                let j = j as usize;
                for k in 0..=i.min(j) {
                    f[i][j] = (f[i][j] + f[i - 1][j - k]) % MOD;
                }
            }
        }
        f[n - 1][req[n - 1] as usize]
    }
}
'''

FILES["3194_minimum_average_of_smallest_and_largest_elements"] = r'''// LeetCode 3194 - Minimum Average of Smallest and Largest Elements
// https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

impl Solution {
    pub fn minimum_average(mut nums: Vec<i32>) -> f64 {
        nums.sort_unstable();
        let n = nums.len();
        let mut ans = 1 << 30;
        for i in 0..n / 2 {
            ans = ans.min(nums[i] + nums[n - i - 1]);
        }
        ans as f64 / 2.0
    }
}
'''

FILES["3195_find_the_minimum_area_to_cover_all_ones_i"] = r'''// LeetCode 3195 - Find the Minimum Area to Cover All Ones I
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

impl Solution {
    pub fn minimum_area(grid: Vec<Vec<i32>>) -> i32 {
        let mut x1 = grid.len() as i32;
        let mut y1 = grid[0].len() as i32;
        let mut x2 = 0;
        let mut y2 = 0;
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                if grid[i][j] == 1 {
                    x1 = x1.min(i as i32);
                    y1 = y1.min(j as i32);
                    x2 = x2.max(i as i32);
                    y2 = y2.max(j as i32);
                }
            }
        }
        (x2 - x1 + 1) * (y2 - y1 + 1)
    }
}
'''

FILES["3196_maximize_total_cost_of_alternating_subarrays"] = r'''// LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
// https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

impl Solution {
    pub fn maximum_total_cost(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        const NEG: i64 = -1_000_000_000_000_000_000;
        let mut memo = vec![[NEG, NEG]; n];
        fn dfs(i: usize, j: usize, nums: &[i32], memo: &mut [[i64; 2]]) -> i64 {
            if i >= nums.len() {
                return 0;
            }
            if memo[i][j] != -1_000_000_000_000_000_000 {
                return memo[i][j];
            }
            let mut res = nums[i] as i64 + dfs(i + 1, 1, nums, memo);
            if j > 0 {
                res = res.max(-(nums[i] as i64) + dfs(i + 1, 0, nums, memo));
            }
            memo[i][j] = res;
            res
        }
        dfs(0, 0, &nums, &mut memo)
    }
}
'''

FILES["3197_find_the_minimum_area_to_cover_all_ones_ii"] = r'''// LeetCode 3197 - Find the Minimum Area to Cover All Ones II
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

impl Solution {
    pub fn minimum_sum(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len() as i32;
        let n = grid[0].len() as i32;
        let mut ans = m * n;
        const INF: i32 = i32::MAX / 4;
        let f = |i1: i32, j1: i32, i2: i32, j2: i32| -> i32 {
            let mut x1 = INF;
            let mut y1 = INF;
            let mut x2 = -INF;
            let mut y2 = -INF;
            for i in i1..=i2 {
                for j in j1..=j2 {
                    if grid[i as usize][j as usize] == 1 {
                        x1 = x1.min(i);
                        y1 = y1.min(j);
                        x2 = x2.max(i);
                        y2 = y2.max(j);
                    }
                }
            }
            if x1 == INF {
                0
            } else {
                (x2 - x1 + 1) * (y2 - y1 + 1)
            }
        };
        for i1 in 0..m - 1 {
            for i2 in i1 + 1..m - 1 {
                ans = ans.min(f(0, 0, i1, n - 1) + f(i1 + 1, 0, i2, n - 1) + f(i2 + 1, 0, m - 1, n - 1));
            }
        }
        for j1 in 0..n - 1 {
            for j2 in j1 + 1..n - 1 {
                ans = ans.min(f(0, 0, m - 1, j1) + f(0, j1 + 1, m - 1, j2) + f(0, j2 + 1, m - 1, n - 1));
            }
        }
        for i in 0..m - 1 {
            for j in 0..n - 1 {
                ans = ans.min(f(0, 0, i, j) + f(0, j + 1, i, n - 1) + f(i + 1, 0, m - 1, n - 1));
                ans = ans.min(f(0, 0, i, n - 1) + f(i + 1, 0, m - 1, j) + f(i + 1, j + 1, m - 1, n - 1));
                ans = ans.min(f(0, 0, i, j) + f(i + 1, 0, m - 1, j) + f(0, j + 1, m - 1, n - 1));
                ans = ans.min(f(0, 0, m - 1, j) + f(0, j + 1, i, n - 1) + f(i + 1, j + 1, m - 1, n - 1));
            }
        }
        ans
    }
}
'''

def main():
    n = 0
    for folder, src in FILES.items():
        path = ROOT / folder / "solution.rs"
        path.write_text(src, encoding="utf-8", newline="\n")
        n += 1
        print("wrote", folder)
    print("total", n)

if __name__ == "__main__":
    main()
