// LeetCode 0327 - Count of Range Sum
// https://leetcode.com/problems/count-of-range-sum/

class Solution {
    func countRangeSum(_ nums: [Int], _ lower: Int, _ upper: Int) -> Int {
        var prefix = [0]
        for num in nums {
            prefix.append(prefix.last! + num)
        }
        var temp = Array(repeating: 0, count: prefix.count)
        return mergeSort(&prefix, &temp, 0, prefix.count - 1, lower, upper)
    }

    private func mergeSort(
        _ prefix: inout [Int],
        _ temp: inout [Int],
        _ left: Int,
        _ right: Int,
        _ lower: Int,
        _ upper: Int
    ) -> Int {
        if left >= right {
            return 0
        }
        let mid = (left + right) / 2
        var count = mergeSort(&prefix, &temp, left, mid, lower, upper)
        count += mergeSort(&prefix, &temp, mid + 1, right, lower, upper)

        var start = mid + 1
        var end = mid + 1
        for index in left...mid {
            while start <= right && prefix[start] - prefix[index] < lower {
                start += 1
            }
            while end <= right && prefix[end] - prefix[index] <= upper {
                end += 1
            }
            count += end - start
        }

        var tempLeft = left
        var tempRight = mid + 1
        var write = left
        while tempLeft <= mid && tempRight <= right {
            if prefix[tempLeft] <= prefix[tempRight] {
                temp[write] = prefix[tempLeft]
                tempLeft += 1
            } else {
                temp[write] = prefix[tempRight]
                tempRight += 1
            }
            write += 1
        }
        while tempLeft <= mid {
            temp[write] = prefix[tempLeft]
            tempLeft += 1
            write += 1
        }
        while tempRight <= right {
            temp[write] = prefix[tempRight]
            tempRight += 1
            write += 1
        }
        for index in left...right {
            prefix[index] = temp[index]
        }
        return count
    }
}
