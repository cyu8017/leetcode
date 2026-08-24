// LeetCode 3072 - Distribute Elements Into Two Arrays II
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

struct Bit {
    n: usize,
    c: Vec<i32>,
}

impl Bit {
    fn new(n: usize) -> Self {
        Self { n, c: vec![0; n + 1] }
    }
    fn update(&mut self, mut x: usize, delta: i32) {
        while x <= self.n {
            self.c[x] += delta;
            x += x & x.wrapping_neg();
        }
    }
    fn query(&self, mut x: usize) -> i32 {
        let mut s = 0;
        while x > 0 {
            s += self.c[x];
            x -= x & x.wrapping_neg();
        }
        s
    }
}

impl Solution {
    pub fn result_array(nums: Vec<i32>) -> Vec<i32> {
        let mut st = nums.clone();
        st.sort_unstable();
        let n = st.len();
        let idx = |x: i32| -> usize { st.partition_point(|&v| v < x) + 1 };
        let mut tree1 = Bit::new(n + 1);
        let mut tree2 = Bit::new(n + 1);
        tree1.update(idx(nums[0]), 1);
        tree2.update(idx(nums[1]), 1);
        let mut arr1 = vec![nums[0]];
        let mut arr2 = vec![nums[1]];
        for &x in &nums[2..] {
            let id = idx(x);
            let a = arr1.len() as i32 - tree1.query(id);
            let b = arr2.len() as i32 - tree2.query(id);
            if a > b || (a == b && arr1.len() <= arr2.len()) {
                arr1.push(x);
                tree1.update(id, 1);
            } else {
                arr2.push(x);
                tree2.update(id, 1);
            }
        }
        arr1.extend(arr2);
        arr1
    }
}
