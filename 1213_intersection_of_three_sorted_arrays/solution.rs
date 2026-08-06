// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

impl Solution {
    pub fn arrays_intersection(arr1: Vec<i32>, arr2: Vec<i32>, arr3: Vec<i32>) -> Vec<i32> {
        let mut i = 0;
        let mut j = 0;
        let mut k = 0;
        let mut ans = Vec::new();
        while i < arr1.len() && j < arr2.len() && k < arr3.len() {
            let a = arr1[i];
            let b = arr2[j];
            let c = arr3[k];
            if a == b && b == c {
                ans.push(a);
                i += 1;
                j += 1;
                k += 1;
            } else if a <= b && a <= c {
                i += 1;
            } else if b <= a && b <= c {
                j += 1;
            } else {
                k += 1;
            }
        }
        ans
    }
}
