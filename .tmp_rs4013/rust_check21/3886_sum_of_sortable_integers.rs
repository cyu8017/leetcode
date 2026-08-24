struct Solution;
// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

impl Solution {
    pub fn sum_of_sortable_integers(nums: Vec<i32>) -> i32 {
        fn rotation_matches(block: &[i32], target: &[i32]) -> bool {
            let k = block.len();
            let mut prefix = vec![0; k];
            for i in 1..k {
                let mut j = prefix[i - 1];
                while j > 0 && target[i] != target[j] {
                    j = prefix[j - 1];
                }
                if target[i] == target[j] {
                    j += 1;
                }
                prefix[i] = j;
            }
            let mut matched = 0;
            for i in 0..2 * k - 1 {
                let x = block[i % k];
                while matched > 0 && x != target[matched] {
                    matched = prefix[matched - 1];
                }
                if x == target[matched] {
                    matched += 1;
                }
                if matched == k {
                    return true;
                }
            }
            false
        }
        let n = nums.len();
        let mut sorted = nums.clone();
        sorted.sort_unstable();
        let mut divisors = Vec::new();
        let mut d = 1;
        while d * d <= n {
            if n % d == 0 {
                divisors.push(d);
                if d * d != n {
                    divisors.push(n / d);
                }
            }
            d += 1;
        }
        let mut answer = 0;
        for k in divisors {
            let mut ok = true;
            let mut start = 0;
            while start < n {
                if !rotation_matches(&nums[start..start + k], &sorted[start..start + k]) {
                    ok = false;
                    break;
                }
                start += k;
            }
            if ok {
                answer += k as i32;
            }
        }
        answer
    }
}
