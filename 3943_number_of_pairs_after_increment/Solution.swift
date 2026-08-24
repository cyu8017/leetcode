// LeetCode 3943 - Number of Pairs After Increment
// https://leetcode.com/problems/number-of-pairs-after-increment/


class Solution {
    func numberOfPairs(_ nums1: [Int], _ nums2: [Int], _ queries: [[Int]]) -> [Int] {
        let blockSize = 225
        var nums2 = nums2
        let n = nums2.count
        let blocks = (n + blockSize - 1) / blockSize
        var lazy = Array(repeating: 0, count: max(blocks, 1))
        var freq = Array(repeating: [Int: Int](), count: max(blocks, 1))
        func rebuild(_ b: Int) {
            freq[b].removeAll()
            let end = min((b + 1) * blockSize, n)
            if b * blockSize < end {
                for i in (b * blockSize)..<end {
                    freq[b][nums2[i], default: 0] += 1
                }
            }
        }
        func push(_ b: Int) {
            if lazy[b] != 0 {
                let end = min((b + 1) * blockSize, n)
                if b * blockSize < end {
                    for i in (b * blockSize)..<end { nums2[i] += lazy[b] }
                }
                lazy[b] = 0
            }
        }
        if n > 0 {
            for b in 0..<blocks { rebuild(b) }
        }
        var fixed = [Int: Int]()
        for x in nums1 { fixed[x, default: 0] += 1 }
        var answer = [Int]()
        for q in queries {
            if q[0] == 1 {
                let l = q[1], r = q[2], delta = q[3]
                let first = l / blockSize, last = r / blockSize
                if first == last {
                    push(first)
                    for i in l...r { nums2[i] += delta }
                    rebuild(first)
                    continue
                }
                push(first)
                for i in l..<((first + 1) * blockSize) { nums2[i] += delta }
                rebuild(first)
                push(last)
                for i in (last * blockSize)...r { nums2[i] += delta }
                rebuild(last)
                if first + 1 < last {
                    for b in (first + 1)..<last { lazy[b] += delta }
                }
            } else {
                var total = 0
                for (a, countA) in fixed {
                    let target = q[1] - a
                    for b in 0..<blocks {
                        if let c = freq[b][target - lazy[b]] {
                            total += countA * c
                        }
                    }
                }
                answer.append(total)
            }
        }
        return answer
    }
}
