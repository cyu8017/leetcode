// LeetCode 1826 - Faulty Sensor
// https://leetcode.com/problems/faulty-sensor/

impl Solution {
    pub fn bad_sensor(sensor1: Vec<i32>, sensor2: Vec<i32>) -> i32 {
        if sensor1 == sensor2 {
            return -1;
        }

        fn is_defective(correct: &[i32], faulty: &[i32]) -> bool {
            let n = correct.len();
            let mut i = 0;
            while i < n && correct[i] == faulty[i] {
                i += 1;
            }
            if i == n {
                return false;
            }

            let mut j = i;
            while j < n - 1 && correct[j + 1] == faulty[j] {
                j += 1;
            }
            j == n - 1
        }

        let sensor1_bad = is_defective(&sensor2, &sensor1);
        let sensor2_bad = is_defective(&sensor1, &sensor2);

        if sensor1_bad && sensor2_bad {
            -1
        } else if sensor1_bad {
            1
        } else if sensor2_bad {
            2
        } else {
            -1
        }
    }
}
