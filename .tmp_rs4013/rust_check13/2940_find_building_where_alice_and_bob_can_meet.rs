#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2940 - Find Building Where Alice and Bob Can Meet
// https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

impl Solution {
    pub fn leftmost_building_queries(heights: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let qn = queries.len();
        let mut ans = vec![-1; qn];
        let mut buckets = vec![Vec::<(i32, usize)>::new(); heights.len()];
        for (qi, q) in queries.iter().enumerate() {
            let mut a = q[0] as usize;
            let mut b = q[1] as usize;
            if a > b {
                std::mem::swap(&mut a, &mut b);
            }
            if a == b || heights[a] < heights[b] {
                ans[qi] = b as i32;
                continue;
            }
            buckets[b].push((heights[a], qi));
        }
        let mut st: Vec<(i32, i32)> = Vec::new();
        for i in (0..heights.len()).rev() {
            for &(h, qi) in &buckets[i] {
                let mut lo = 0i32;
                let mut hi = st.len() as i32 - 1;
                let mut pos = -1;
                while lo <= hi {
                    let mid = (lo + hi) / 2;
                    if st[mid as usize].0 > h {
                        pos = st[mid as usize].1;
                        lo = mid + 1;
                    } else {
                        hi = mid - 1;
                    }
                }
                ans[qi] = pos;
            }
            while !st.is_empty() && st.last().unwrap().0 <= heights[i] {
                st.pop();
            }
            st.push((heights[i], i as i32));
        }
        ans
    }
}
