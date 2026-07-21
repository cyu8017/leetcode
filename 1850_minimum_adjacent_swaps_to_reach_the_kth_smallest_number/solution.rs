// LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

impl Solution {
    pub fn get_min_swaps(num: String, k: i32) -> i32 {
        fn next_permutation(arr: &mut [u8]) {
            let mut i = arr.len() as i32 - 2;
            while i >= 0 && arr[i as usize] >= arr[(i + 1) as usize] {
                i -= 1;
            }
            if i < 0 {
                arr.reverse();
                return;
            }
            let mut j = arr.len() as i32 - 1;
            while arr[j as usize] <= arr[i as usize] {
                j -= 1;
            }
            arr.swap(i as usize, j as usize);
            arr[(i as usize + 1)..].reverse();
        }

        let mut target = num.clone().into_bytes();
        for _ in 0..k {
            next_permutation(&mut target);
        }

        let mut source = num.into_bytes();
        let mut swaps = 0;
        for i in 0..source.len() {
            if source[i] == target[i] {
                continue;
            }
            let mut j = i;
            while source[j] != target[i] {
                j += 1;
            }
            while j > i {
                source.swap(j, j - 1);
                swaps += 1;
                j -= 1;
            }
        }
        swaps
    }
}
