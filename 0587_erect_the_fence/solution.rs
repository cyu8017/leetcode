// LeetCode 0587 - Erect the Fence
// https://leetcode.com/problems/erect-the-fence/

impl Solution {
    fn cross(o: &[i32], a: &[i32], b: &[i32]) -> i64 {
        (a[0] as i64 - o[0] as i64) * (b[1] as i64 - o[1] as i64)
            - (a[1] as i64 - o[1] as i64) * (b[0] as i64 - o[0] as i64)
    }

    pub fn outer_trees(trees: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut points = trees;
        points.sort();
        if points.len() <= 1 {
            return points;
        }
        let build = |ordered: &[Vec<i32>]| {
            let mut hull: Vec<Vec<i32>> = Vec::new();
            for point in ordered {
                while hull.len() >= 2
                    && Self::cross(&hull[hull.len() - 2], &hull[hull.len() - 1], point) < 0
                {
                    hull.pop();
                }
                hull.push(point.clone());
            }
            hull
        };
        let lower = build(&points);
        let mut reversed = points.clone();
        reversed.reverse();
        let upper = build(&reversed);
        let mut unique = std::collections::BTreeSet::new();
        for i in 0..lower.len().saturating_sub(1) {
            unique.insert(lower[i].clone());
        }
        for i in 0..upper.len().saturating_sub(1) {
            unique.insert(upper[i].clone());
        }
        unique.into_iter().collect()
    }
}
