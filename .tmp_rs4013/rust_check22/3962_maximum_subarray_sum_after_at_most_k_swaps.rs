struct Solution;
// LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
// https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

impl Solution {
    pub fn max_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut unique = nums.clone();
        unique.sort_unstable();
        unique.dedup();
        let mut rank = vec![0; n];
        let mut global_count = vec![0i32; unique.len() + 1];
        let mut global_sum = vec![0i64; unique.len() + 1];
        let add = |count: &mut [i32], sum: &mut [i64], unique: &[i32], mut index: usize, delta: i32| {
            let value = unique[index - 1] as i64;
            while index < count.len() {
                count[index] += delta;
                sum[index] += delta as i64 * value;
                index += index & index.wrapping_neg();
            }
        };
        for i in 0..n {
            rank[i] = unique.binary_search(&nums[i]).unwrap_or_else(|e| e) + 1;
            add(&mut global_count, &mut global_sum, &unique, rank[i], 1);
        }
        let query_count = |bit: &[i32], mut index: usize| -> i32 {
            let mut result = 0;
            while index > 0 {
                result += bit[index];
                index -= index & index.wrapping_neg();
            }
            result
        };
        let query_sum = |bit: &[i64], mut index: usize| -> i64 {
            let mut result = 0;
            while index > 0 {
                result += bit[index];
                index -= index & index.wrapping_neg();
            }
            result
        };
        let kth = |bit: &[i32], mut order: i32| -> usize {
            let mut index = 0usize;
            let mut step = 1usize;
            while (step << 1) < bit.len() {
                step <<= 1;
            }
            while step > 0 {
                let next = index + step;
                if next < bit.len() && bit[next] < order {
                    index = next;
                    order -= bit[next];
                }
                step >>= 1;
            }
            index + 1
        };
        let sum_smallest = |count: &[i32], sum: &[i64], amount: i32| -> i64 {
            if amount <= 0 {
                return 0;
            }
            let index = kth(count, amount);
            let count_before = query_count(count, index - 1);
            let sum_before = query_sum(sum, index - 1);
            sum_before + (amount - count_before) as i64 * unique[index - 1] as i64
        };
        let mut answer = -(1i64 << 60);
        for left in 0..n {
            let mut inside_count = vec![0i32; unique.len() + 1];
            let mut inside_sum = vec![0i64; unique.len() + 1];
            let mut outside_count = global_count.clone();
            let mut outside_sum = global_sum.clone();
            let mut subarray_sum = 0i64;
            for right in left..n {
                add(&mut outside_count, &mut outside_sum, &unique, rank[right], -1);
                add(&mut inside_count, &mut inside_sum, &unique, rank[right], 1);
                subarray_sum += nums[right] as i64;
                let inside_size = (right - left + 1) as i32;
                let outside_size = n as i32 - inside_size;
                let limit = k.min(inside_size).min(outside_size);
                let mut low = 0;
                let mut high = limit;
                while low < high {
                    let mid = (low + high + 1) / 2;
                    let inside_value = unique[kth(&inside_count, mid) - 1];
                    let outside_order = outside_size - mid + 1;
                    let outside_value = unique[kth(&outside_count, outside_order) - 1];
                    if outside_value > inside_value {
                        low = mid;
                    } else {
                        high = mid - 1;
                    }
                }
                let swaps = low;
                let mut gain = 0i64;
                if swaps > 0 {
                    let small_inside = sum_smallest(&inside_count, &inside_sum, swaps);
                    let total_outside = query_sum(&outside_sum, unique.len());
                    let large_outside =
                        total_outside - sum_smallest(&outside_count, &outside_sum, outside_size - swaps);
                    gain = large_outside - small_inside;
                }
                answer = answer.max(subarray_sum + gain);
            }
        }
        answer
    }
}

fn main() {}
