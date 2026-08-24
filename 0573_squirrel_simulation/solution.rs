// LeetCode 0573 - Squirrel Simulation
// https://leetcode.com/problems/squirrel-simulation/

impl Solution {
    fn dist(a: &[i32], b: &[i32]) -> i32 {
        (a[0] - b[0]).abs() + (a[1] - b[1]).abs()
    }

    pub fn min_distance(
        _height: i32,
        _width: i32,
        tree: Vec<i32>,
        squirrel: Vec<i32>,
        nuts: Vec<Vec<i32>>,
    ) -> i32 {
        let mut total = 0;
        let mut best_save = i32::MIN;
        for nut in &nuts {
            let tree_dist = Self::dist(&tree, nut);
            let squirrel_dist = Self::dist(&squirrel, nut);
            total += 2 * tree_dist;
            best_save = best_save.max(tree_dist - squirrel_dist);
        }
        total - best_save
    }
}
