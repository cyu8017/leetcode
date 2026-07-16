// LeetCode 0363 - Max Sum of Rectangle No Larger Than K
// https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

impl Solution {
    pub fn max_sum_submatrix(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
        let rows = matrix.len();
        if rows == 0 {
            return 0;
        }
        let cols = matrix[0].len();
        let mut result = i32::MIN;

        for top in 0..rows {
            let mut col_sums = vec![0; cols];
            for bottom in top..rows {
                let mut prefix_sums = vec![0];
                let mut running = 0;

                for col in 0..cols {
                    col_sums[col] += matrix[bottom][col];
                    running += col_sums[col];

                    let index = match prefix_sums.binary_search(&(running - k)) {
                        Ok(found) => found,
                        Err(found) => found,
                    };
                    if index < prefix_sums.len() {
                        result = result.max(running - prefix_sums[index]);
                    }

                    match prefix_sums.binary_search(&running) {
                        Ok(_) => {}
                        Err(insert_index) => prefix_sums.insert(insert_index, running),
                    }
                }
            }
        }

        result
    }
}
