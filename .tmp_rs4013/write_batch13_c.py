#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3001_minimum_moves_to_capture_the_queen"] = r'''// LeetCode 3001 - Minimum Moves to Capture The Queen
// https://leetcode.com/problems/minimum-moves-to-capture-the-queen/

impl Solution {
    pub fn min_moves_to_capture_the_queen(a: i32, b: i32, c: i32, d: i32, e: i32, f: i32) -> i32 {
        if a == e && (c != a || (d - b) * (d - f) > 0) {
            return 1;
        }
        if b == f && (d != b || (c - a) * (c - e) > 0) {
            return 1;
        }
        if c - e == d - f && (a - e != b - f || (a - c) * (a - e) > 0) {
            return 1;
        }
        if c - e == f - d && (a - e != f - b || (a - c) * (a - e) > 0) {
            return 1;
        }
        2
    }
}
'''

FILES["3002_maximum_size_of_a_set_after_removals"] = r'''// LeetCode 3002 - Maximum Size of a Set After Removals
// https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

use std::collections::HashSet;

impl Solution {
    pub fn maximum_set_size(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let s1: HashSet<i32> = nums1.iter().copied().collect();
        let s2: HashSet<i32> = nums2.iter().copied().collect();
        let mut a = 0;
        let mut b = 0;
        let mut c = 0;
        for &x in &s1 {
            if !s2.contains(&x) {
                a += 1;
            }
        }
        for &x in &s2 {
            if !s1.contains(&x) {
                b += 1;
            } else {
                c += 1;
            }
        }
        let n = nums1.len() as i32;
        a = a.min(n / 2);
        b = b.min(n / 2);
        (a + b + c).min(n)
    }
}
'''

FILES["3003_maximize_the_number_of_partitions_after_operations"] = r'''// LeetCode 3003 - Maximize the Number of Partitions After Operations
// https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

use std::collections::HashMap;

impl Solution {
    pub fn max_partitions_after_operations(s: String, k: i32) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let mut memo: HashMap<i64, i32> = HashMap::new();
        fn key(i: usize, cur: i32, t: i32) -> i64 {
            ((i as i64) << 32) | ((cur as i64) << 1) | t as i64
        }
        fn dfs(
            i: usize,
            cur: i32,
            t: i32,
            n: usize,
            b: &[u8],
            k: i32,
            memo: &mut HashMap<i64, i32>,
        ) -> i32 {
            if i >= n {
                return 1;
            }
            let kkey = key(i, cur, t);
            if let Some(&v) = memo.get(&kkey) {
                return v;
            }
            let v = 1 << (b[i] - b'a');
            let nxt = cur | v;
            let mut ans = if nxt.count_ones() as i32 > k {
                dfs(i + 1, v, t, n, b, k, memo) + 1
            } else {
                dfs(i + 1, nxt, t, n, b, k, memo)
            };
            if t > 0 {
                for j in 0..26 {
                    let nxt = cur | (1 << j);
                    if nxt.count_ones() as i32 > k {
                        ans = ans.max(dfs(i + 1, 1 << j, 0, n, b, k, memo) + 1);
                    } else {
                        ans = ans.max(dfs(i + 1, nxt, 0, n, b, k, memo));
                    }
                }
            }
            memo.insert(kkey, ans);
            ans
        }
        dfs(0, 0, 1, n, b, k, &mut memo)
    }
}
'''

FILES["3004_maximum_subtree_of_the_same_color"] = r'''// LeetCode 3004 - Maximum Subtree of the Same Color
// https://leetcode.com/problems/maximum-subtree-of-the-same-color/

impl Solution {
    pub fn maximum_subtree_size(edges: Vec<Vec<i32>>, colors: Vec<i32>) -> i32 {
        let n = edges.len() + 1;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut size = vec![0; n];
        let mut ans = 0;
        fn dfs(
            a: usize,
            fa: i32,
            g: &[Vec<usize>],
            colors: &[i32],
            size: &mut [i32],
            ans: &mut i32,
        ) -> bool {
            size[a] = 1;
            let mut ok = true;
            for &b in &g[a] {
                if b as i32 != fa {
                    let t = dfs(b, a as i32, g, colors, size, ans);
                    ok = ok && t && colors[a] == colors[b];
                    size[a] += size[b];
                }
            }
            if ok {
                *ans = (*ans).max(size[a]);
            }
            ok
        }
        dfs(0, -1, &g, &colors, &mut size, &mut ans);
        ans
    }
}
'''

FILES["3005_count_elements_with_maximum_frequency"] = r'''// LeetCode 3005 - Count Elements With Maximum Frequency
// https://leetcode.com/problems/count-elements-with-maximum-frequency/

impl Solution {
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
        let mut cnt = [0i32; 101];
        for x in nums {
            cnt[x as usize] += 1;
        }
        let mut mx = -1;
        let mut ans = 0;
        for x in cnt {
            if mx < x {
                mx = x;
                ans = x;
            } else if mx == x {
                ans += x;
            }
        }
        ans
    }
}
'''

FILES["3006_find_beautiful_indices_in_the_given_array_i"] = r'''// LeetCode 3006 - Find Beautiful Indices in the Given Array I
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

impl Solution {
    pub fn beautiful_indices(s: String, a: String, b: String, k: i32) -> Vec<i32> {
        fn build_lps(pattern: &[u8]) -> Vec<i32> {
            let s_l = pattern.len();
            let mut lps = vec![0; s_l];
            let mut l = 0;
            let mut i = 1;
            while i < s_l {
                if pattern[i] == pattern[l] {
                    l += 1;
                    lps[i] = l as i32;
                    i += 1;
                } else if l != 0 {
                    l = lps[l - 1] as usize;
                } else {
                    lps[i] = l as i32;
                    i += 1;
                }
            }
            lps
        }
        fn kmp(s: &[u8], pat: &[u8], lps: &[i32]) -> Vec<i32> {
            let s_len = s.len();
            let pat_l = pat.len();
            let mut index = Vec::new();
            let mut i = 0;
            let mut j = 0;
            while s_len - i >= pat_l - j {
                if s[i] == pat[j] {
                    i += 1;
                    j += 1;
                }
                if j == pat_l {
                    index.push((i - pat_l) as i32);
                    j = lps[j - 1] as usize;
                } else if i < s_len && s[i] != pat[j] {
                    if j != 0 {
                        j = lps[j - 1] as usize;
                    } else {
                        i += 1;
                    }
                }
            }
            index
        }
        let sb = s.as_bytes();
        let ab = a.as_bytes();
        let bb = b.as_bytes();
        if ab.is_empty() || bb.is_empty() {
            return vec![];
        }
        let lps_a = build_lps(ab);
        let lps_b = build_lps(bb);
        let a_index = kmp(sb, ab, &lps_a);
        let b_index = kmp(sb, bb, &lps_b);
        let mut final_v = Vec::new();
        let mut i = 0;
        let mut j = 0;
        while i < a_index.len() && j < b_index.len() {
            if a_index[i] + k >= b_index[j] && a_index[i] - k <= b_index[j] {
                final_v.push(a_index[i]);
                i += 1;
            } else if a_index[i] - k > b_index[j] {
                j += 1;
            } else {
                i += 1;
            }
        }
        final_v
    }
}
'''

FILES["3007_maximum_number_that_sum_of_the_prices_is_less_than_or_equal_to_k"] = r'''// LeetCode 3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
// https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

impl Solution {
    pub fn find_maximum_number(k: i64, x: i32) -> i64 {
        let mut l = 1i64;
        let mut r = 10i64.pow(17);
        let mut num = 0i64;
        fn dfs(pos: i32, cnt: i32, limit: bool, num: i64, x: i32, f: &mut [[i64; 65]; 65]) -> i64 {
            if pos == 0 {
                return cnt as i64;
            }
            if !limit && f[pos as usize][cnt as usize] != -1 {
                return f[pos as usize][cnt as usize];
            }
            let mut ans = 0i64;
            let up = if limit {
                ((num >> (pos - 1)) & 1) as i32
            } else {
                1
            };
            for i in 0..=up {
                let mut v = cnt;
                if i == 1 && pos % x == 0 {
                    v += 1;
                }
                ans += dfs(pos - 1, v, limit && i == up, num, x, f);
            }
            if !limit {
                f[pos as usize][cnt as usize] = ans;
            }
            ans
        }
        while l < r {
            let mid = (l + r + 1) >> 1;
            num = mid;
            let m = if num == 0 {
                0
            } else {
                64 - num.leading_zeros() as i32
            };
            let mut f = [[-1i64; 65]; 65];
            if dfs(m, 0, true, num, x, &mut f) <= k {
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        l
    }
}
'''

FILES["3008_find_beautiful_indices_in_the_given_array_ii"] = r'''// LeetCode 3008 - Find Beautiful Indices in the Given Array II
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/

impl Solution {
    pub fn beautiful_indices(s: String, a: String, b: String, k: i32) -> Vec<i32> {
        fn build_lps(pattern: &[u8]) -> Vec<i32> {
            let s_l = pattern.len();
            let mut lps = vec![0; s_l];
            let mut l = 0;
            let mut i = 1;
            while i < s_l {
                if pattern[i] == pattern[l] {
                    l += 1;
                    lps[i] = l as i32;
                    i += 1;
                } else if l != 0 {
                    l = lps[l - 1] as usize;
                } else {
                    lps[i] = l as i32;
                    i += 1;
                }
            }
            lps
        }
        fn kmp(s: &[u8], pat: &[u8], lps: &[i32]) -> Vec<i32> {
            let s_len = s.len();
            let pat_l = pat.len();
            let mut index = Vec::new();
            let mut i = 0;
            let mut j = 0;
            while s_len - i >= pat_l - j {
                if s[i] == pat[j] {
                    i += 1;
                    j += 1;
                }
                if j == pat_l {
                    index.push((i - pat_l) as i32);
                    j = lps[j - 1] as usize;
                } else if i < s_len && s[i] != pat[j] {
                    if j != 0 {
                        j = lps[j - 1] as usize;
                    } else {
                        i += 1;
                    }
                }
            }
            index
        }
        let sb = s.as_bytes();
        let ab = a.as_bytes();
        let bb = b.as_bytes();
        if ab.is_empty() || bb.is_empty() {
            return vec![];
        }
        let lps_a = build_lps(ab);
        let lps_b = build_lps(bb);
        let a_index = kmp(sb, ab, &lps_a);
        let b_index = kmp(sb, bb, &lps_b);
        let mut final_v = Vec::new();
        let mut i = 0;
        let mut j = 0;
        while i < a_index.len() && j < b_index.len() {
            if a_index[i] + k >= b_index[j] && a_index[i] - k <= b_index[j] {
                final_v.push(a_index[i]);
                i += 1;
            } else if a_index[i] - k > b_index[j] {
                j += 1;
            } else {
                i += 1;
            }
        }
        final_v
    }
}
'''

FILES["3009_maximum_number_of_intersections_on_the_chart"] = r'''// LeetCode 3009 - Maximum Number of Intersections on the Chart
// https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

use std::collections::BTreeMap;

impl Solution {
    pub fn max_intersection_count(y: Vec<i32>) -> i32 {
        let n = y.len();
        let mut line: BTreeMap<i32, i32> = BTreeMap::new();
        for i in 1..n {
            let start = 2 * y[i - 1];
            let mut end = 2 * y[i];
            if i != n - 1 {
                if y[i] > y[i - 1] {
                    end -= 1;
                } else {
                    end += 1;
                }
            }
            let (a, b) = if start <= end { (start, end) } else { (end, start) };
            *line.entry(a).or_insert(0) += 1;
            *line.entry(b + 1).or_insert(0) -= 1;
        }
        let mut ans = 0;
        let mut cur = 0;
        for (_, v) in line {
            cur += v;
            if cur > ans {
                ans = cur;
            }
        }
        ans
    }
}
'''

FILES["3010_divide_an_array_into_subarrays_with_minimum_cost_i"] = r'''// LeetCode 3010 - Divide an Array Into Subarrays With Minimum Cost I
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

impl Solution {
    pub fn minimum_cost(nums: Vec<i32>) -> i32 {
        let a = nums[0];
        let mut b = 100;
        let mut c = 100;
        for &x in nums.iter().skip(1) {
            if x < b {
                c = b;
                b = x;
            } else if x < c {
                c = x;
            }
        }
        a + b + c
    }
}
'''

FILES["3011_find_if_array_can_be_sorted"] = r'''// LeetCode 3011 - Find if Array Can Be Sorted
// https://leetcode.com/problems/find-if-array-can-be-sorted/

impl Solution {
    pub fn can_sort_array(nums: Vec<i32>) -> bool {
        let mut pre_mx = 0;
        let n = nums.len();
        let mut i = 0;
        while i < n {
            let cnt = nums[i].count_ones();
            let mut j = i + 1;
            let mut mi = nums[i];
            let mut mx = nums[i];
            while j < n && nums[j].count_ones() == cnt {
                mi = mi.min(nums[j]);
                mx = mx.max(nums[j]);
                j += 1;
            }
            if pre_mx > mi {
                return false;
            }
            pre_mx = mx;
            i = j;
        }
        true
    }
}
'''

FILES["3012_minimize_length_of_array_using_operations"] = r'''// LeetCode 3012 - Minimize Length of Array Using Operations
// https://leetcode.com/problems/minimize-length-of-array-using-operations/

impl Solution {
    pub fn minimum_array_length(nums: Vec<i32>) -> i32 {
        let mi = *nums.iter().min().unwrap();
        let mut cnt = 0;
        for &x in &nums {
            if x % mi != 0 {
                return 1;
            }
            if x == mi {
                cnt += 1;
            }
        }
        (cnt + 1) / 2
    }
}
'''

FILES["3013_divide_an_array_into_subarrays_with_minimum_cost_ii"] = r'''// LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

struct Biti {
    n: usize,
    c: Vec<i32>,
}
impl Biti {
    fn new(n: usize) -> Self {
        Self { n, c: vec![0; n + 1] }
    }
    fn upd(&mut self, mut x: usize, d: i32) {
        while x <= self.n {
            self.c[x] += d;
            x += x & x.wrapping_neg();
        }
    }
    fn qry(&self, mut x: usize) -> i32 {
        let mut s = 0;
        while x > 0 {
            s += self.c[x];
            x -= x & x.wrapping_neg();
        }
        s
    }
}

struct Bitl {
    n: usize,
    c: Vec<i64>,
}
impl Bitl {
    fn new(n: usize) -> Self {
        Self { n, c: vec![0; n + 1] }
    }
    fn upd(&mut self, mut x: usize, d: i64) {
        while x <= self.n {
            self.c[x] += d;
            x += x & x.wrapping_neg();
        }
    }
    fn qry(&self, mut x: usize) -> i64 {
        let mut s = 0i64;
        while x > 0 {
            s += self.c[x];
            x -= x & x.wrapping_neg();
        }
        s
    }
}

impl Solution {
    pub fn minimum_cost(nums: Vec<i32>, k: i32, dist: i32) -> i64 {
        let mut k = k - 1;
        let n = nums.len();
        let mut uniq = nums.clone();
        uniq.sort_unstable();
        uniq.dedup();
        let m = uniq.len();
        let mut cnt = Biti::new(m + 2);
        let mut sum = Bitl::new(m + 2);
        let rank = |uniq: &[i32], x: i32| -> usize {
            uniq.binary_search(&x).unwrap_or_else(|e| e) + 1
        };
        let add_val = |cnt: &mut Biti, sum: &mut Bitl, uniq: &[i32], x: i32, d: i32| {
            let r = rank(uniq, x);
            cnt.upd(r, d);
            sum.upd(r, d as i64 * x as i64);
        };
        let kth = |cnt: &Biti, m: usize, mut kk: i32| -> usize {
            let mut idx = 0usize;
            let mut bit = 1usize << 20;
            while bit > 0 {
                let nidx = idx + bit;
                if nidx <= m && cnt.c[nidx] < kk {
                    kk -= cnt.c[nidx];
                    idx = nidx;
                }
                bit >>= 1;
            }
            idx + 1
        };
        let sum_smallest = |cnt: &Biti, sum: &Bitl, uniq: &[i32], kk: i32| -> i64 {
            if kk <= 0 {
                return 0;
            }
            let r = kth(cnt, m, kk);
            let before = cnt.qry(r - 1);
            let mut s = sum.qry(r - 1);
            s += (kk - before) as i64 * uniq[r - 1] as i64;
            s
        };
        let end = (dist as usize + 1).min(n - 1);
        for i in 1..=end {
            add_val(&mut cnt, &mut sum, &uniq, nums[i], 1);
        }
        let mut kk = k.min(end as i32);
        let mut ans = nums[0] as i64 + sum_smallest(&cnt, &sum, &uniq, kk);
        let start = dist as usize + 2;
        for i in start..n {
            add_val(&mut cnt, &mut sum, &uniq, nums[i - dist as usize - 1], -1);
            add_val(&mut cnt, &mut sum, &uniq, nums[i], 1);
            kk = k.min(dist + 1);
            ans = ans.min(nums[0] as i64 + sum_smallest(&cnt, &sum, &uniq, kk));
        }
        let _ = k;
        ans
    }
}
'''

FILES["3014_minimum_number_of_pushes_to_type_word_i"] = r'''// LeetCode 3014 - Minimum Number of Pushes to Type Word I
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

impl Solution {
    pub fn minimum_pushes(word: String) -> i32 {
        let n = word.len() as i32;
        let mut ans = 0;
        let mut k = 1;
        for _ in 0..(n / 8) {
            ans += k * 8;
            k += 1;
        }
        ans += k * (n % 8);
        ans
    }
}
'''

FILES["3015_count_the_number_of_houses_at_a_certain_distance_i"] = r'''// LeetCode 3015 - Count the Number of Houses at a Certain Distance I
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

impl Solution {
    pub fn count_of_pairs(n: i32, x: i32, y: i32) -> Vec<i32> {
        let n = n as usize;
        let mut ans = vec![0; n];
        let x = x as i32 - 1;
        let y = y as i32 - 1;
        for i in 0..n as i32 {
            for j in (i + 1)..n as i32 {
                let a = j - i;
                let b = (x - i).abs() + (y - j).abs() + 1;
                let c = (x - j).abs() + (y - i).abs() + 1;
                let d = a.min(b).min(c);
                ans[(d - 1) as usize] += 2;
            }
        }
        ans
    }
}
'''

FILES["3016_minimum_number_of_pushes_to_type_word_ii"] = r'''// LeetCode 3016 - Minimum Number of Pushes to Type Word II
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

impl Solution {
    pub fn minimum_pushes(word: String) -> i32 {
        let mut cnt = [0i32; 26];
        for c in word.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        cnt.sort_unstable();
        let mut ans = 0;
        for i in 0..26 {
            ans += (i as i32 / 8 + 1) * cnt[26 - i - 1];
        }
        ans
    }
}
'''

FILES["3017_count_the_number_of_houses_at_a_certain_distance_ii"] = r'''// LeetCode 3017 - Count the Number of Houses at a Certain Distance II
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

impl Solution {
    pub fn count_of_pairs(n: i32, mut x: i32, mut y: i32) -> Vec<i64> {
        if x > y {
            std::mem::swap(&mut x, &mut y);
        }
        let nu = n as usize;
        let mut a = vec![0i64; nu];
        for i in 1..=n {
            a[0] += 2;
            let i64i = i as i64;
            a[((i64i - 1).min((i - y).abs() as i64 + x as i64)) as usize] -= 1;
            a[((n as i64 - i64i).min((i - x).abs() as i64 + 1 + (n as i64 - y as i64))) as usize] -= 1;
            a[(((i - x).abs() as i64).min((y - i).abs() as i64 + 1)) as usize] += 1;
            a[(((i - x).abs() as i64 + 1).min((y - i).abs() as i64)) as usize] += 1;
            let r = (x - i).max(0) as i64 + (i - y).max(0) as i64;
            a[(r + (y - x) as i64 / 2) as usize] -= 1;
            a[(r + (y - x + 1) as i64 / 2) as usize] -= 1;
        }
        for i in 1..nu {
            a[i] += a[i - 1];
        }
        a
    }
}
'''

FILES["3018_maximum_number_of_removal_queries_that_can_be_processed_i"] = r'''// LeetCode 3018 - Maximum Number of Removal Queries That Can Be Processed I
// https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

impl Solution {
    pub fn maximum_processable_queries(nums: Vec<i32>, queries: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut f = vec![vec![0; n]; n];
        let m = queries.len();
        for i in 0..n {
            for j in (i..n).rev() {
                if i > 0 {
                    let qi = f[i - 1][j] as usize;
                    if qi >= m {
                        return m as i32;
                    }
                    let t = if nums[i - 1] >= queries[qi] { 1 } else { 0 };
                    f[i][j] = f[i][j].max(f[i - 1][j] + t);
                }
                if j + 1 < n {
                    let qi = f[i][j + 1] as usize;
                    if qi >= m {
                        return m as i32;
                    }
                    let t = if nums[j + 1] >= queries[qi] { 1 } else { 0 };
                    f[i][j] = f[i][j].max(f[i][j + 1] + t);
                }
                if f[i][j] == m as i32 {
                    return m as i32;
                }
            }
        }
        let mut ans = 0;
        for i in 0..n {
            let qi = f[i][i] as usize;
            if qi >= m {
                return m as i32;
            }
            let t = if nums[i] >= queries[qi] { 1 } else { 0 };
            ans = ans.max(f[i][i] + t);
        }
        ans
    }
}
'''

FILES["3019_number_of_changing_keys"] = r'''// LeetCode 3019 - Number of Changing Keys
// https://leetcode.com/problems/number-of-changing-keys/

impl Solution {
    pub fn count_key_changes(s: String) -> i32 {
        let s = s.to_ascii_lowercase();
        let b = s.as_bytes();
        let mut ans = 0;
        for i in 1..b.len() {
            if b[i] != b[i - 1] {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["3020_find_the_maximum_number_of_elements_in_subset"] = r'''// LeetCode 3020 - Find the Maximum Number of Elements in Subset
// https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        let mut cnt: HashMap<i64, i32> = HashMap::new();
        for x in nums {
            *cnt.entry(x as i64).or_insert(0) += 1;
        }
        let mut ans = {
            let c1 = *cnt.get(&1).unwrap_or(&0);
            c1 - ((c1 % 2) ^ 1)
        };
        cnt.remove(&1);
        let keys: Vec<i64> = cnt.keys().copied().collect();
        for mut x in keys {
            let mut t = 0;
            while *cnt.get(&x).unwrap_or(&0) > 1 {
                if x > i64::MAX / x {
                    break;
                }
                x = x * x;
                t += 2;
            }
            if *cnt.get(&x).unwrap_or(&0) > 0 {
                t += 1;
            } else {
                t -= 1;
            }
            ans = ans.max(t);
        }
        ans
    }
}
'''

FILES["3021_alice_and_bob_playing_flower_game"] = r'''// LeetCode 3021 - Alice and Bob Playing Flower Game
// https://leetcode.com/problems/alice-and-bob-playing-flower-game/

impl Solution {
    pub fn flower_game(n: i32, m: i32) -> i64 {
        let a1 = (n as i64 + 1) / 2;
        let b1 = (m as i64 + 1) / 2;
        let a2 = n as i64 / 2;
        let b2 = m as i64 / 2;
        a1 * b2 + a2 * b1
    }
}
'''

FILES["3022_minimize_or_of_remaining_elements_using_operations"] = r'''// LeetCode 3022 - Minimize OR of Remaining Elements Using Operations
// https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

impl Solution {
    pub fn min_or_after_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut ans = 0;
        let mut rans = 0;
        for i in (0..=29).rev() {
            let test = ans + (1 << i);
            let mut cnt = 0;
            let mut val = 0;
            for &num in &nums {
                if val == 0 {
                    val = test & num;
                } else {
                    val &= test & num;
                }
                if val != 0 {
                    cnt += 1;
                }
            }
            if cnt > k {
                rans += 1 << i;
            } else {
                ans += 1 << i;
            }
        }
        rans
    }
}
'''

FILES["3023_find_pattern_in_infinite_stream_i"] = r'''// LeetCode 3023 - Find Pattern in Infinite Stream I
// https://leetcode.com/problems/find-pattern-in-infinite-stream-i/

pub struct InfiniteStream {
    bits: Vec<i32>,
    i: usize,
}

impl InfiniteStream {
    pub fn new(bits: Vec<i32>) -> Self {
        Self { bits, i: 0 }
    }
    pub fn next(&mut self) -> i32 {
        let v = self.bits[self.i];
        self.i += 1;
        v
    }
}

impl Solution {
    pub fn find_pattern(stream: &mut InfiniteStream, pattern: Vec<i32>) -> i32 {
        let mut a = 0;
        let mut b = 0;
        let m = pattern.len();
        let half = m >> 1;
        let mask1 = if half == 0 { 0 } else { (1 << half) - 1 };
        let mask2 = (1 << (m - half)) - 1;
        for i in 0..half {
            a |= pattern[i] << (half - 1 - i);
        }
        for i in half..m {
            b |= pattern[i] << (m - 1 - i);
        }
        let mut x = 0;
        let mut y = 0;
        let mut i = 1;
        loop {
            let mut v = stream.next();
            y = y << 1 | v;
            v = (y >> (m - half)) & 1;
            y &= mask2;
            x = x << 1 | v;
            x &= mask1;
            if i >= m as i32 && a == x && b == y {
                return i - m as i32;
            }
            i += 1;
        }
    }
}
'''

FILES["3024_type_of_triangle"] = r'''// LeetCode 3024 - Type of Triangle
// https://leetcode.com/problems/type-of-triangle/

impl Solution {
    pub fn triangle_type(mut nums: Vec<i32>) -> String {
        nums.sort_unstable();
        if nums[0] + nums[1] <= nums[2] {
            return "none".to_string();
        }
        if nums[0] == nums[2] {
            return "equilateral".to_string();
        }
        if nums[0] == nums[1] || nums[1] == nums[2] {
            return "isosceles".to_string();
        }
        "scalene".to_string()
    }
}
'''

FILES["3025_find_the_number_of_ways_to_place_people_i"] = r'''// LeetCode 3025 - Find the Number of Ways to Place People I
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

impl Solution {
    pub fn number_of_pairs(mut points: Vec<Vec<i32>>) -> i32 {
        points.sort_by(|a, b| a[0].cmp(&b[0]).then(b[1].cmp(&a[1])));
        let mut ans = 0;
        for i in 0..points.len() {
            let y1 = points[i][1];
            let mut max_y = i32::MIN;
            for j in (i + 1)..points.len() {
                let y2 = points[j][1];
                if max_y < y2 && y2 <= y1 {
                    max_y = y2;
                    ans += 1;
                }
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
