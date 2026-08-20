// LeetCode 1982 - Find Array Given Subset Sums
// https://leetcode.com/problems/find-array-given-subset-sums/

class Solution {
    func recoverArray(_ n: Int, _ sums: [Int]) -> [Int] {
        var sums = sums.sorted()
        var ans: [Int] = []
        for _ in 0..<n {
            let d = sums[1] - sums[0]
            var count: [Int: Int] = [:]
            for x in sums { count[x, default: 0] += 1 }
            var without: [Int] = []
            var withD: [Int] = []
            for x in sums {
                if count[x, default: 0] == 0 { continue }
                count[x]! -= 1
                count[x + d]! -= 1
                without.append(x)
                withD.append(x + d)
            }
            if without.contains(0) {
                ans.append(d)
                sums = without
            } else {
                ans.append(-d)
                sums = withD
            }
        }
        return ans
    }
}
