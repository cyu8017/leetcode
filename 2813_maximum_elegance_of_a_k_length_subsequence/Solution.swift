// LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

class Solution {
    func findMaximumElegance(_ items: [[Int]], _ k: Int) -> Int {
        let items = items.sorted { $0[0] > $1[0] }
        var seen = Set<Int>()
        var total = 0
        var dup: [Int] = []
        for i in 0..<k {
            total += items[i][0]
            let c = items[i][1]
            if seen.contains(c) { dup.append(items[i][0]) } else { seen.insert(c) }
        }
        var ans = total + seen.count * seen.count
        for i in k..<items.count {
            let c = items[i][1]
            if seen.contains(c) || dup.isEmpty { continue }
            total += items[i][0] - dup.removeLast()
            seen.insert(c)
            ans = max(ans, total + seen.count * seen.count)
        }
        return ans
    }
}
