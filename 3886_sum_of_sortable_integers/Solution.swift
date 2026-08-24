// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

class Solution {
    private func rotationMatches(_ block: [Int], _ target: [Int]) -> Bool {
        let k = block.count
        var prefix = [Int](repeating: 0, count: k)
        if k > 1 {
            for i in 1..<k {
                var j = prefix[i - 1]
                while j > 0 && target[i] != target[j] { j = prefix[j - 1] }
                if target[i] == target[j] { j += 1 }
                prefix[i] = j
            }
        }
        var matched = 0
        for i in 0..<(2 * k - 1) {
            let x = block[i % k]
            while matched > 0 && x != target[matched] { matched = prefix[matched - 1] }
            if x == target[matched] { matched += 1 }
            if matched == k { return true }
        }
        return false
    }

    func sumOfSortableIntegers(_ nums: [Int]) -> Int {
        let n = nums.count
        let sorted = nums.sorted()
        var divisors = [Int]()
        var d = 1
        while d * d <= n {
            if n % d == 0 {
                divisors.append(d)
                if d * d != n { divisors.append(n / d) }
            }
            d += 1
        }
        var answer = 0
        for k in divisors {
            var ok = true
            var start = 0
            while start < n {
                let block = Array(nums[start..<(start + k)])
                let target = Array(sorted[start..<(start + k)])
                if !rotationMatches(block, target) { ok = false; break }
                start += k
            }
            if ok { answer += k }
        }
        return answer
    }
}
