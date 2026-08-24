// LeetCode 0605 - Can Place Flowers
// https://leetcode.com/problems/can-place-flowers/

impl Solution {
    pub fn can_place_flowers(mut flowerbed: Vec<i32>, mut n: i32) -> bool {
        if n == 0 {
            return true;
        }
        let len = flowerbed.len();
        for i in 0..len {
            if flowerbed[i] == 1 {
                continue;
            }
            let left_empty = i == 0 || flowerbed[i - 1] == 0;
            let right_empty = i == len - 1 || flowerbed[i + 1] == 0;
            if left_empty && right_empty {
                flowerbed[i] = 1;
                n -= 1;
                if n == 0 {
                    return true;
                }
            }
        }
        false
    }
}
