// LeetCode 3767 - Maximize Points After Choosing K Tasks
// https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

class Solution {
    func maxPoints(_ technique1: [Int], _ technique2: [Int], _ k: Int) -> Int {
        let n = technique1.count
        var idx = Array(0..<n)
        idx.sort { technique1[$0] - technique2[$0] > technique1[$1] - technique2[$1] }
        var ans = 0
        for x in technique2 { ans += x }
        if k > 0 {
            for i in 0..<k {
                let index = idx[i]
                ans -= technique2[index]
                ans += technique1[index]
            }
        }
        if k < n {
            for i in k..<n {
                let index = idx[i]
                if technique1[index] >= technique2[index] {
                    ans -= technique2[index]
                    ans += technique1[index]
                }
            }
        }
        return ans
    }
}
