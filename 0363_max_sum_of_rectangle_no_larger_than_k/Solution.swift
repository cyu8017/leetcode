// LeetCode 0363 - Max Sum of Rectangle No Larger Than K
// https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

class Solution {
    func maxSumSubmatrix(_ matrix: [[Int]], _ k: Int) -> Int {
        let rows = matrix.count
        let cols = rows == 0 ? 0 : matrix[0].count
        var result = Int.min

        for top in 0..<rows {
            var colSums = Array(repeating: 0, count: cols)
            for bottom in top..<rows {
                var prefixSums = [0]
                var running = 0
                for col in 0..<cols {
                    colSums[col] += matrix[bottom][col]
                    running += colSums[col]
                    let index = bisectLeft(prefixSums, running - k)
                    if index < prefixSums.count {
                        result = max(result, running - prefixSums[index])
                    }
                    insortLeft(&prefixSums, running)
                }
            }
        }

        return result
    }

    private func bisectLeft(_ array: [Int], _ target: Int) -> Int {
        var left = 0
        var right = array.count
        while left < right {
            let mid = (left + right) / 2
            if array[mid] < target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }

    private func insortLeft(_ array: inout [Int], _ value: Int) {
        let index = bisectLeft(array, value)
        array.insert(value, at: index)
    }
}
