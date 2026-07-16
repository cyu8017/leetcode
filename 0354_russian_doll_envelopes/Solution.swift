// LeetCode 0354 - Russian Doll Envelopes
// https://leetcode.com/problems/russian-doll-envelopes/

class Solution {
    func maxEnvelopes(_ envelopes: [[Int]]) -> Int {
        let sorted = envelopes.sorted {
            if $0[0] == $1[0] {
                return $0[1] > $1[1]
            }
            return $0[0] < $1[0]
        }

        var tails: [Int] = []
        for envelope in sorted {
            let height = envelope[1]
            let index = bisectLeft(tails, height)
            if index == tails.count {
                tails.append(height)
            } else {
                tails[index] = height
            }
        }

        return tails.count
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
}
