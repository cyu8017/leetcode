// LeetCode 1095 - Find in Mountain Array
// https://leetcode.com/problems/find-in-mountain-array/

struct MountainArray;
impl MountainArray {
    fn get(&self, _index: i32) -> i32 {
        0
    }
    fn length(&self) -> i32 {
        0
    }
}

impl Solution {
    pub fn find_in_mountain_array(target: i32, mountain_arr: &MountainArray) -> i32 {
        let n = mountain_arr.length();
        let mut lo = 0;
        let mut hi = n - 1;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        let peak = lo;
        lo = 0;
        hi = peak;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            let val = mountain_arr.get(mid);
            if val == target {
                return mid;
            }
            if val < target {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        lo = peak + 1;
        hi = n - 1;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            let val = mountain_arr.get(mid);
            if val == target {
                return mid;
            }
            if val > target {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        -1
    }
}
