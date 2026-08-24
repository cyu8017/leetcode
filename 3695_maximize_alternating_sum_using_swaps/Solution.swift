// LeetCode 3695 - Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

class Solution {
    var parent = [Int]()

    func find(_ x: Int) -> Int {
        if parent[x] != x { parent[x] = find(parent[x]) }
        return parent[x]
    }

    func maxAlternatingSum(_ nums: [Int], _ swaps: [[Int]]) -> Int {
        let n = nums.count
        parent = Array(0..<n)
        for s in swaps {
            let a = find(s[0]), b = find(s[1])
            if a != b { parent[a] = b }
        }
        var compVals = [Int: [Int]]()
        var compIdx = [Int: [Int]]()
        for i in 0..<n {
            let r = find(i)
            compVals[r, default: []].append(nums[i])
            compIdx[r, default: []].append(i)
        }
        var arr = Array(repeating: 0, count: n)
        for (r, vals0) in compVals {
            var vals = vals0.sorted(by: >)
            let idxs = compIdx[r]!
            var even = [Int]()
            var odd = [Int]()
            for i in idxs {
                if i % 2 == 0 { even.append(i) } else { odd.append(i) }
            }
            even.sort(); odd.sort()
            var ei = 0
            for v in vals {
                if ei < even.count {
                    arr[even[ei]] = v
                } else {
                    arr[odd[ei - even.count]] = v
                }
                ei += 1
            }
        }
        var ans = 0
        for i in 0..<n {
            if i % 2 == 0 { ans += arr[i] } else { ans -= arr[i] }
        }
        return ans
    }
}
