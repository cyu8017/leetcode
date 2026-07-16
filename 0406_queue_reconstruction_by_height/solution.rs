// LeetCode 0406 - Queue Reconstruction by Height
// https://leetcode.com/problems/queue-reconstruction-by-height/

impl Solution {
    pub fn reconstruct_queue(mut people: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        people.sort_by(|left, right| {
            right[0]
                .cmp(&left[0])
                .then_with(|| left[1].cmp(&right[1]))
        });

        let mut queue: Vec<Vec<i32>> = Vec::new();
        for person in people {
            let index = person[1] as usize;
            queue.insert(index, person);
        }

        queue
    }
}
