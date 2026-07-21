// LeetCode 1842 - Next Palindrome Using Same Digits
// https://leetcode.com/problems/next-palindrome-using-same-digits/

impl Solution {
    pub fn next_palindrome(num: String) -> String {
        let mut nums: Vec<u8> = num.into_bytes();
        if !Self::next_permutation_half(&mut nums) {
            return String::new();
        }
        let n = nums.len();
        for i in 0..n / 2 {
            nums[n - i - 1] = nums[i];
        }
        String::from_utf8(nums).unwrap()
    }

    fn next_permutation_half(nums: &mut [u8]) -> bool {
        let n = nums.len() / 2;
        let mut i = n as i32 - 2;
        while i >= 0 && nums[i as usize] >= nums[(i + 1) as usize] {
            i -= 1;
        }
        if i < 0 {
            return false;
        }
        let mut j = n as i32 - 1;
        while nums[j as usize] <= nums[i as usize] {
            j -= 1;
        }
        nums.swap(i as usize, j as usize);
        nums[(i as usize + 1)..n].reverse();
        true
    }
}
