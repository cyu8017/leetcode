// LeetCode 0321 - Create Maximum Number
// https://leetcode.com/problems/create-maximum-number/

class Solution {
    func maxNumber(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> [Int] {
        func pickMax(_ values: [Int], _ count: Int) -> [Int] {
            var drop = values.count - count
            var stack: [Int] = []
            for value in values {
                while drop > 0, let last = stack.last, last < value {
                    stack.removeLast()
                    drop -= 1
                }
                stack.append(value)
            }
            return Array(stack.prefix(count))
        }

        func merge(_ first: [Int], _ second: [Int]) -> [Int] {
            var result: [Int] = []
            var left = 0
            var right = 0
            while left < first.count && right < second.count {
                if Array(first[left...]) > Array(second[right...]) {
                    result.append(first[left])
                    left += 1
                } else {
                    result.append(second[right])
                    right += 1
                }
            }
            result.append(contentsOf: first[left...])
            result.append(contentsOf: second[right...])
            return result
        }

        var best: [Int] = []
        let startTake = max(0, k - nums2.count)
        let endTake = min(k, nums1.count)
        for takeFirst in startTake...endTake {
            let takeSecond = k - takeFirst
            let candidate = merge(pickMax(nums1, takeFirst), pickMax(nums2, takeSecond))
            if candidate > best {
                best = candidate
            }
        }
        return best
    }
}
