// LeetCode 2382 - Maximum Segment Sum After Removals
// https://leetcode.com/problems/maximum-segment-sum-after-removals/

impl Solution {
    pub fn maximum_segment_sum(nums: Vec<i32>, remove_queries: Vec<i32>) -> Vec<i64> {
        let n = nums.len();
        let mut parent: Vec<usize> = (0..n).collect();
        let mut sum = vec![0i64; n];
        let mut active = vec![false; n];
        fn find(x: usize, parent: &mut [usize]) -> usize {
            if parent[x] != x {
                parent[x] = find(parent[x], parent);
            }
            parent[x]
        }
        fn unite(a: usize, b: usize, parent: &mut [usize], sum: &mut [i64]) {
            let ra = find(a, parent);
            let rb = find(b, parent);
            if ra == rb {
                return;
            }
            parent[rb] = ra;
            sum[ra] += sum[rb];
        }
        let mut ans = vec![0i64; n];
        let mut best = 0i64;
        for i in (0..n).rev() {
            ans[i] = best;
            let idx = remove_queries[i] as usize;
            active[idx] = true;
            sum[idx] = nums[idx] as i64;
            if idx > 0 && active[idx - 1] {
                unite(idx, idx - 1, &mut parent, &mut sum);
            }
            if idx + 1 < n && active[idx + 1] {
                unite(idx, idx + 1, &mut parent, &mut sum);
            }
            let r = find(idx, &mut parent);
            best = best.max(sum[r]);
        }
        ans
    }
}
