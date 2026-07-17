// LeetCode 1792 - Maximum Average Pass Ratio
// https://leetcode.com/problems/maximum-average-pass-ratio/

impl Solution {
    pub fn max_average_ratio(classes: Vec<Vec<i32>>, extra_students: i32) -> f64 {
        fn gain(p: f64, t: f64) -> f64 {
            (p + 1.0) / (t + 1.0) - p / t
        }
        fn sift_down(heap: &mut Vec<(f64, f64, f64)>, mut i: usize) {
            let n = heap.len();
            loop {
                let mut largest = i;
                let l = 2 * i + 1;
                let r = 2 * i + 2;
                if l < n && heap[l].0 > heap[largest].0 {
                    largest = l;
                }
                if r < n && heap[r].0 > heap[largest].0 {
                    largest = r;
                }
                if largest == i {
                    break;
                }
                heap.swap(i, largest);
                i = largest;
            }
        }

        let mut heap: Vec<(f64, f64, f64)> = classes
            .iter()
            .map(|cls| {
                let p = cls[0] as f64;
                let t = cls[1] as f64;
                (gain(p, t), p, t)
            })
            .collect();
        for i in (0..heap.len() / 2).rev() {
            sift_down(&mut heap, i);
        }
        for _ in 0..extra_students {
            let (_, p, t) = heap[0];
            heap[0] = (gain(p + 1.0, t + 1.0), p + 1.0, t + 1.0);
            sift_down(&mut heap, 0);
        }
        let total: f64 = heap.iter().map(|&(_, p, t)| p / t).sum();
        total / classes.len() as f64
    }
}
