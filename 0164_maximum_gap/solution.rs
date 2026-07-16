// LeetCode 0164 - Maximum Gap
impl Solution {
    pub fn maximum_gap(nums: Vec<i32>) -> i32 {
        if nums.len() < 2 { return 0; }
        let low = *nums.iter().min().unwrap();
        let high = *nums.iter().max().unwrap();
        if low == high { return 0; }
        let size = ((high - low) / (nums.len() as i32 - 1)).max(1);
        let count = ((high - low) / size + 1) as usize;
        let mut mins = vec![i32::MAX; count];
        let mut maxs = vec![i32::MIN; count];
        let mut used = vec![false; count];
        for n in nums {
            let i = ((n - low) / size) as usize;
            mins[i] = mins[i].min(n); maxs[i] = maxs[i].max(n); used[i] = true;
        }
        let (mut best, mut previous) = (0, low);
        for i in 0..count { if used[i] { best = best.max(mins[i] - previous); previous = maxs[i]; } }
        best
    }
}