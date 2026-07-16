// LeetCode 0327 - Count of Range Sum
// https://leetcode.com/problems/count-of-range-sum/

impl Solution {
    fn merge_sort(
        prefix: &mut [i64],
        temp: &mut [i64],
        left: usize,
        right: usize,
        lower: i64,
        upper: i64,
    ) -> i32 {
        if left >= right {
            return 0;
        }
        let mid = left + (right - left) / 2;
        let mut count = Self::merge_sort(prefix, temp, left, mid, lower, upper)
            + Self::merge_sort(prefix, temp, mid + 1, right, lower, upper);

        let mut start = mid + 1;
        let mut end = mid + 1;
        for index in left..=mid {
            while start <= right && prefix[start] - prefix[index] < lower {
                start += 1;
            }
            while end <= right && prefix[end] - prefix[index] <= upper {
                end += 1;
            }
            count += (end - start) as i32;
        }

        let mut temp_left = left;
        let mut temp_right = mid + 1;
        let mut write = left;
        while temp_left <= mid && temp_right <= right {
            if prefix[temp_left] <= prefix[temp_right] {
                temp[write] = prefix[temp_left];
                temp_left += 1;
            } else {
                temp[write] = prefix[temp_right];
                temp_right += 1;
            }
            write += 1;
        }
        while temp_left <= mid {
            temp[write] = prefix[temp_left];
            temp_left += 1;
            write += 1;
        }
        while temp_right <= right {
            temp[write] = prefix[temp_right];
            temp_right += 1;
            write += 1;
        }
        prefix[left..=right].copy_from_slice(&temp[left..=right]);
        count
    }

    pub fn count_range_sum(nums: Vec<i32>, lower: i32, upper: i32) -> i32 {
        let mut prefix = vec![0i64];
        for num in nums {
            prefix.push(prefix.last().copied().unwrap_or(0) + num as i64);
        }
        let mut temp = vec![0; prefix.len()];
        Self::merge_sort(
            &mut prefix,
            &mut temp,
            0,
            prefix.len() - 1,
            lower as i64,
            upper as i64,
        )
    }
}
