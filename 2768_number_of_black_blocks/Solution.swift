// LeetCode 2768 - Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/

class Solution {
    func countBlackBlocks(_ m: Int, _ n: Int, _ coordinates: [[Int]]) -> [Int] {
        var cnt: [Int: Int] = [:]
        for c in coordinates {
            let x = c[0], y = c[1]
            for i in (x - 1)...x {
                for j in (y - 1)...y {
                    if i >= 0 && j >= 0 && i < m - 1 && j < n - 1 {
                        let key = (i << 32) | (j & 0xffffffff)
                        cnt[key, default: 0] += 1
                    }
                }
            }
        }
        var ans = Array(repeating: 0, count: 5)
        ans[0] = (m - 1) * (n - 1)
        for v in cnt.values {
            ans[v] += 1
            ans[0] -= 1
        }
        return ans
    }
}
