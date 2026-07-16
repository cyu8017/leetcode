// LeetCode 0321 - Create Maximum Number
// https://leetcode.com/problems/create-maximum-number/

impl Solution {
    fn pick_max(values: &[i32], count: usize) -> Vec<i32> {
        let mut drop = values.len().saturating_sub(count);
        let mut stack: Vec<i32> = Vec::new();
        for &value in values {
            while drop > 0 && stack.last().copied().unwrap_or(i32::MIN) < value {
                stack.pop();
                drop -= 1;
            }
            stack.push(value);
        }
        stack.truncate(count);
        stack
    }

    fn suffix_greater(first: &[i32], left: usize, second: &[i32], right: usize) -> bool {
        let mut left = left;
        let mut right = right;
        while left < first.len() && right < second.len() {
            if first[left] != second[right] {
                return first[left] > second[right];
            }
            left += 1;
            right += 1;
        }
        first.len() - left > second.len() - right
    }

    fn merge(first: Vec<i32>, second: Vec<i32>) -> Vec<i32> {
        let mut result = Vec::new();
        let mut left = 0;
        let mut right = 0;
        while left < first.len() && right < second.len() {
            if Self::suffix_greater(&first, left, &second, right) {
                result.push(first[left]);
                left += 1;
            } else {
                result.push(second[right]);
                right += 1;
            }
        }
        result.extend_from_slice(&first[left..]);
        result.extend_from_slice(&second[right..]);
        result
    }

    pub fn max_number(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let min_first = k.saturating_sub(nums2.len());
        let max_first = k.min(nums1.len());
        let mut best: Vec<i32> = Vec::new();
        for take_first in min_first..=max_first {
            let take_second = k - take_first;
            let candidate = Self::merge(
                Self::pick_max(&nums1, take_first),
                Self::pick_max(&nums2, take_second),
            );
            if candidate > best {
                best = candidate;
            }
        }
        best
    }
}
