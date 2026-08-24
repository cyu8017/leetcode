#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
FILES = {}

FILES["3026_maximum_good_subarray_sum"] = r'''// LeetCode 3026 - Maximum Good Subarray Sum
// https://leetcode.com/problems/maximum-good-subarray-sum/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let mut p: HashMap<i32, i64> = HashMap::new();
        p.insert(nums[0], 0);
        let mut s = 0i64;
        let n = nums.len();
        let mut ans = i64::MIN;
        for i in 0..n {
            s += nums[i] as i64;
            if let Some(&v) = p.get(&(nums[i] - k)) {
                ans = ans.max(s - v);
            }
            if let Some(&v) = p.get(&(nums[i] + k)) {
                ans = ans.max(s - v);
            }
            if i + 1 == n {
                break;
            }
            let nxt = nums[i + 1];
            if !p.contains_key(&nxt) || s < p[&nxt] {
                p.insert(nxt, s);
            }
        }
        if ans == i64::MIN { 0 } else { ans }
    }
}
'''

FILES["3027_find_the_number_of_ways_to_place_people_ii"] = r'''// LeetCode 3027 - Find the Number of Ways to Place People II
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

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

FILES["3028_ant_on_the_boundary"] = r'''// LeetCode 3028 - Ant on the Boundary
// https://leetcode.com/problems/ant-on-the-boundary/

impl Solution {
    pub fn return_to_boundary_count(nums: Vec<i32>) -> i32 {
        let mut s = 0;
        let mut ans = 0;
        for x in nums {
            s += x;
            if s == 0 {
                ans += 1;
            }
        }
        ans
    }
}
'''

FILES["3029_minimum_time_to_revert_word_to_initial_state_i"] = r'''// LeetCode 3029 - Minimum Time to Revert Word to Initial State I
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

impl Solution {
    pub fn minimum_time_to_initial_state(word: String, k: i32) -> i32 {
        let n = word.len();
        let k = k as usize;
        let mut i = k;
        while i < n {
            if &word[i..] == &word[..n - i] {
                return (i / k) as i32;
            }
            i += k;
        }
        ((n + k - 1) / k) as i32
    }
}
'''

FILES["3030_find_the_grid_of_region_average"] = r'''// LeetCode 3030 - Find the Grid of Region Average
// https://leetcode.com/problems/find-the-grid-of-region-average/

impl Solution {
    pub fn result_grid(image: Vec<Vec<i32>>, threshold: i32) -> Vec<Vec<i32>> {
        let n = image.len();
        let m = image[0].len();
        let mut ans = vec![vec![0; m]; n];
        let mut ct = vec![vec![0; m]; n];
        for i in 0..n.saturating_sub(2) {
            for j in 0..m.saturating_sub(2) {
                let mut region = true;
                for k in 0..3 {
                    for l in 0..2 {
                        region = region
                            && (image[i + k][j + l] - image[i + k][j + l + 1]).abs() <= threshold;
                    }
                }
                for k in 0..2 {
                    for l in 0..3 {
                        region = region
                            && (image[i + k][j + l] - image[i + k + 1][j + l]).abs() <= threshold;
                    }
                }
                if region {
                    let mut tot = 0;
                    for k in 0..3 {
                        for l in 0..3 {
                            tot += image[i + k][j + l];
                        }
                    }
                    for k in 0..3 {
                        for l in 0..3 {
                            ct[i + k][j + l] += 1;
                            ans[i + k][j + l] += tot / 9;
                        }
                    }
                }
            }
        }
        for i in 0..n {
            for j in 0..m {
                if ct[i][j] == 0 {
                    ans[i][j] = image[i][j];
                } else {
                    ans[i][j] /= ct[i][j];
                }
            }
        }
        ans
    }
}
'''

FILES["3031_minimum_time_to_revert_word_to_initial_state_ii"] = r'''// LeetCode 3031 - Minimum Time to Revert Word to Initial State II
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/

impl Solution {
    pub fn minimum_time_to_initial_state(word: String, k: i32) -> i32 {
        let n = word.len();
        let bytes = word.as_bytes();
        let mut p = vec![0i64; n + 1];
        let mut h = vec![0i64; n + 1];
        let base = 13331i64;
        let modulus = 998244353i64;
        p[0] = 1;
        for i in 1..=n {
            p[i] = p[i - 1] * base % modulus;
            h[i] = (h[i - 1] * base + (bytes[i - 1] - b'a') as i64) % modulus;
        }
        let query = |l: usize, r: usize| -> i64 {
            (h[r] - h[l - 1] * p[r - l + 1] % modulus + modulus) % modulus
        };
        let k = k as usize;
        let mut i = k;
        while i < n {
            if query(1, n - i) == query(i + 1, n) {
                return (i / k) as i32;
            }
            i += k;
        }
        ((n + k - 1) / k) as i32
    }
}
'''

FILES["3032_count_numbers_with_unique_digits_ii"] = r'''// LeetCode 3032 - Count Numbers With Unique Digits II
// https://leetcode.com/problems/count-numbers-with-unique-digits-ii/

impl Solution {
    pub fn number_count(a: i32, b: i32) -> i32 {
        fn solve(num: i32) -> i32 {
            if num < 0 {
                return 0;
            }
            let s = num.to_string();
            let bytes = s.as_bytes();
            let n = bytes.len();
            let mut f = vec![vec![-1i32; 1 << 10]; n];
            fn dfs(
                pos: usize,
                mask: usize,
                limit: bool,
                bytes: &[u8],
                f: &mut [Vec<i32>],
            ) -> i32 {
                if pos >= bytes.len() {
                    return if mask != 0 { 1 } else { 0 };
                }
                if !limit && f[pos][mask] != -1 {
                    return f[pos][mask];
                }
                let up = if limit { (bytes[pos] - b'0') as usize } else { 9 };
                let mut ans = 0;
                for i in 0..=up {
                    if (mask >> i) & 1 == 1 {
                        continue;
                    }
                    let mut nxt = mask | (1 << i);
                    if mask == 0 && i == 0 {
                        nxt = 0;
                    }
                    ans += dfs(pos + 1, nxt, limit && i == up, bytes, f);
                }
                if !limit {
                    f[pos][mask] = ans;
                }
                ans
            }
            dfs(0, 0, true, bytes, &mut f)
        }
        solve(b) - solve(a - 1)
    }
}
'''

FILES["3033_modify_the_matrix"] = r'''// LeetCode 3033 - Modify the Matrix
// https://leetcode.com/problems/modify-the-matrix/

impl Solution {
    pub fn modified_matrix(mut matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = matrix.len();
        let n = matrix[0].len();
        for j in 0..n {
            let mut mx = -1;
            for i in 0..m {
                mx = mx.max(matrix[i][j]);
            }
            for i in 0..m {
                if matrix[i][j] == -1 {
                    matrix[i][j] = mx;
                }
            }
        }
        matrix
    }
}
'''

FILES["3034_number_of_subarrays_that_match_a_pattern_i"] = r'''// LeetCode 3034 - Number of Subarrays That Match a Pattern I
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

impl Solution {
    pub fn count_matching_subarrays(nums: Vec<i32>, pattern: Vec<i32>) -> i32 {
        let f = |a: i32, b: i32| -> i32 {
            if a == b {
                0
            } else if a < b {
                1
            } else {
                -1
            }
        };
        let n = nums.len();
        let m = pattern.len();
        let mut ans = 0;
        for i in 0..n.saturating_sub(m) {
            let mut ok = 1;
            for k in 0..m {
                if f(nums[i + k], nums[i + k + 1]) != pattern[k] {
                    ok = 0;
                    break;
                }
            }
            ans += ok;
        }
        ans
    }
}
'''

FILES["3035_maximum_palindromes_after_operations"] = r'''// LeetCode 3035 - Maximum Palindromes After Operations
// https://leetcode.com/problems/maximum-palindromes-after-operations/

impl Solution {
    pub fn max_palindromes_after_operations(mut words: Vec<String>) -> i32 {
        let mut s = 0i32;
        let mut mask = 0u32;
        for w in &words {
            s += w.len() as i32;
            for c in w.bytes() {
                mask ^= 1 << (c - b'a');
            }
        }
        s -= mask.count_ones() as i32;
        words.sort_by_key(|w| w.len());
        let mut ans = 0;
        for w in &words {
            s -= (w.len() as i32 / 2) * 2;
            if s < 0 {
                break;
            }
            ans += 1;
        }
        ans
    }
}
'''

FILES["3036_number_of_subarrays_that_match_a_pattern_ii"] = r'''// LeetCode 3036 - Number of Subarrays That Match a Pattern II
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/

impl Solution {
    pub fn count_matching_subarrays(nums: Vec<i32>, pattern: Vec<i32>) -> i32 {
        let npat = pattern.len();
        let mut ps = vec![0i32; npat + 1];
        ps[0] = -1;
        ps[1] = 0;
        let mut p = 0i32;
        for i in 2..=npat {
            let x = pattern[i - 1];
            while p >= 0 && pattern[p as usize] != x {
                p = ps[p as usize];
            }
            p += 1;
            ps[i] = p;
        }
        let mut res = 0;
        let m = nums.len();
        p = 0;
        for i in 1..m {
            let mut t = nums[i] - nums[i - 1];
            if t > 0 {
                t = 1;
            } else if t < 0 {
                t = -1;
            }
            while p >= 0 && pattern[p as usize] != t {
                p = ps[p as usize];
            }
            p += 1;
            if p == npat as i32 {
                res += 1;
                p = ps[p as usize];
            }
        }
        res
    }
}
'''

FILES["3037_find_pattern_in_infinite_stream_ii"] = r'''// LeetCode 3037 - Find Pattern in Infinite Stream II
// https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

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
        fn get_lps(pattern: &[i32]) -> Vec<usize> {
            let n = pattern.len();
            let mut lps = vec![0; n];
            let mut j = 0;
            for i in 1..n {
                while j > 0 && pattern[j] != pattern[i] {
                    j = lps[j - 1];
                }
                if pattern[i] == pattern[j] {
                    j += 1;
                    lps[i] = j;
                }
            }
            lps
        }
        let lps = get_lps(&pattern);
        let mut i = 0i32;
        let mut j = 0usize;
        let mut bit = 0;
        let mut read_next = false;
        loop {
            if !read_next {
                bit = stream.next();
                read_next = true;
            }
            if bit == pattern[j] {
                i += 1;
                read_next = false;
                j += 1;
                if j == pattern.len() {
                    return i - j as i32;
                }
            } else if j > 0 {
                j = lps[j - 1];
            } else {
                i += 1;
                read_next = false;
            }
        }
    }
}
'''

FILES["3038_maximum_number_of_operations_with_the_same_score_i"] = r'''// LeetCode 3038 - Maximum Number of Operations With the Same Score I
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

impl Solution {
    pub fn max_operations(nums: Vec<i32>) -> i32 {
        let s = nums[0] + nums[1];
        let n = nums.len();
        let mut ans = 0;
        let mut i = 0;
        while i + 1 < n && nums[i] + nums[i + 1] == s {
            ans += 1;
            i += 2;
        }
        ans
    }
}
'''

FILES["3039_apply_operations_to_make_string_empty"] = r'''// LeetCode 3039 - Apply Operations to Make String Empty
// https://leetcode.com/problems/apply-operations-to-make-string-empty/

impl Solution {
    pub fn last_non_empty_string(s: String) -> String {
        let b = s.as_bytes();
        let mut cnt = [0i32; 26];
        let mut last = [0usize; 26];
        let mut mx = 0;
        for (i, &c) in b.iter().enumerate() {
            let ci = (c - b'a') as usize;
            cnt[ci] += 1;
            last[ci] = i;
            mx = mx.max(cnt[ci]);
        }
        let mut ans = String::new();
        for (i, &c) in b.iter().enumerate() {
            let ci = (c - b'a') as usize;
            if cnt[ci] == mx && last[ci] == i {
                ans.push(c as char);
            }
        }
        ans
    }
}
'''

FILES["3040_maximum_number_of_operations_with_the_same_score_ii"] = r'''// LeetCode 3040 - Maximum Number of Operations With the Same Score II
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

impl Solution {
    pub fn max_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        fn g(nums: &[i32], i0: usize, j0: i32, s: i32) -> i32 {
            let n = nums.len();
            if j0 < 0 {
                return 0;
            }
            let j0 = j0 as usize;
            let mut f = vec![vec![-1i32; n]; n];
            fn dfs(i: usize, j: usize, s: i32, nums: &[i32], f: &mut [Vec<i32>]) -> i32 {
                if j < i || j - i < 1 {
                    return 0;
                }
                if f[i][j] != -1 {
                    return f[i][j];
                }
                let mut ans = 0;
                if i + 1 <= j && nums[i] + nums[i + 1] == s {
                    ans = ans.max(1 + dfs(i + 2, j, s, nums, f));
                }
                if nums[i] + nums[j] == s {
                    if j >= 1 {
                        ans = ans.max(1 + dfs(i + 1, j - 1, s, nums, f));
                    }
                }
                if j >= 1 && nums[j - 1] + nums[j] == s {
                    if j >= 2 {
                        ans = ans.max(1 + dfs(i, j - 2, s, nums, f));
                    } else {
                        ans = ans.max(1);
                    }
                }
                f[i][j] = ans;
                ans
            }
            dfs(i0, j0, s, nums, &mut f)
        }
        let a = g(&nums, 2, n as i32 - 1, nums[0] + nums[1]);
        let b = g(&nums, 0, n as i32 - 3, nums[n - 1] + nums[n - 2]);
        let c = g(&nums, 1, n as i32 - 2, nums[0] + nums[n - 1]);
        1 + a.max(b).max(c)
    }
}
'''

FILES["3041_maximize_consecutive_elements_in_an_array_after_modification"] = r'''// LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
// https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

use std::collections::HashMap;

impl Solution {
    pub fn max_selected_elements(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut dp: HashMap<i32, i32> = HashMap::new();
        let mut ans = 0;
        for num in nums {
            let v_num = *dp.get(&num).unwrap_or(&0);
            let v_prev = *dp.get(&(num - 1)).unwrap_or(&0);
            dp.insert(num + 1, v_num + 1);
            dp.insert(num, v_prev + 1);
            ans = ans.max(*dp.get(&num).unwrap()).max(*dp.get(&(num + 1)).unwrap());
        }
        ans
    }
}
'''

FILES["3042_count_prefix_and_suffix_pairs_i"] = r'''// LeetCode 3042 - Count Prefix and Suffix Pairs I
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

impl Solution {
    pub fn count_prefix_suffix_pairs(words: Vec<String>) -> i32 {
        let mut ans = 0;
        for i in 0..words.len() {
            let s = words[i].as_bytes();
            for j in (i + 1)..words.len() {
                let t = words[j].as_bytes();
                if t.len() >= s.len() && t.starts_with(s) && t.ends_with(s) {
                    ans += 1;
                }
            }
        }
        ans
    }
}
'''

FILES["3043_find_the_length_of_the_longest_common_prefix"] = r'''// LeetCode 3043 - Find the Length of the Longest Common Prefix
// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

use std::collections::HashSet;

impl Solution {
    pub fn longest_common_prefix(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let mut s = HashSet::new();
        for mut x in arr1 {
            while x > 0 {
                s.insert(x);
                x /= 10;
            }
        }
        let mut mx = 0;
        for mut x in arr2 {
            while x > 0 {
                if s.contains(&x) {
                    mx = mx.max(x);
                    break;
                }
                x /= 10;
            }
        }
        if mx > 0 {
            mx.to_string().len() as i32
        } else {
            0
        }
    }
}
'''

FILES["3044_most_frequent_prime"] = r'''// LeetCode 3044 - Most Frequent Prime
// https://leetcode.com/problems/most-frequent-prime/

use std::collections::HashMap;

impl Solution {
    pub fn most_frequent_prime(mat: Vec<Vec<i32>>) -> i32 {
        fn is_prime(n: i32) -> bool {
            if n < 2 {
                return false;
            }
            let mut i = 2;
            while i <= n / i {
                if n % i == 0 {
                    return false;
                }
                i += 1;
            }
            true
        }
        let m = mat.len() as i32;
        let n = mat[0].len() as i32;
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        for i in 0..m {
            for j in 0..n {
                for a in -1..=1 {
                    for b in -1..=1 {
                        if a == 0 && b == 0 {
                            continue;
                        }
                        let mut x = i + a;
                        let mut y = j + b;
                        let mut v = mat[i as usize][j as usize];
                        while x >= 0 && x < m && y >= 0 && y < n {
                            v = v * 10 + mat[x as usize][y as usize];
                            if is_prime(v) {
                                *cnt.entry(v).or_insert(0) += 1;
                            }
                            x += a;
                            y += b;
                        }
                    }
                }
            }
        }
        let mut ans = -1;
        let mut mx = 0;
        for (&v, &x) in &cnt {
            if mx < x || (mx == x && ans < v) {
                mx = x;
                ans = v;
            }
        }
        ans
    }
}
'''

FILES["3045_count_prefix_and_suffix_pairs_ii"] = r'''// LeetCode 3045 - Count Prefix and Suffix Pairs II
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

use std::collections::HashMap;

struct Node {
    children: HashMap<i32, usize>,
    cnt: i64,
}

impl Solution {
    pub fn count_prefix_suffix_pairs(words: Vec<String>) -> i64 {
        let mut nodes = vec![Node {
            children: HashMap::new(),
            cnt: 0,
        }];
        let mut ans = 0i64;
        for s in &words {
            let b = s.as_bytes();
            let m = b.len();
            let mut node = 0usize;
            for i in 0..m {
                let p = b[i] as i32 * 32 + b[m - i - 1] as i32;
                if !nodes[node].children.contains_key(&p) {
                    nodes[node].children.insert(p, nodes.len());
                    nodes.push(Node {
                        children: HashMap::new(),
                        cnt: 0,
                    });
                }
                node = nodes[node].children[&p];
                ans += nodes[node].cnt;
            }
            nodes[node].cnt += 1;
        }
        ans
    }
}
'''

FILES["3046_split_the_array"] = r'''// LeetCode 3046 - Split the Array
// https://leetcode.com/problems/split-the-array/

impl Solution {
    pub fn is_possible_to_split(nums: Vec<i32>) -> bool {
        let mut cnt = [0i32; 101];
        for x in nums {
            cnt[x as usize] += 1;
            if cnt[x as usize] >= 3 {
                return false;
            }
        }
        true
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
