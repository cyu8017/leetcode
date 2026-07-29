// LeetCode 1088 - Confusing Number II
// https://leetcode.com/problems/confusing-number-ii/

class Solution {
    func confusingNumberII(_ n: Int) -> Int {
        let rotate = [0: 0, 1: 1, 6: 9, 8: 8, 9: 6]
        let digits = [0, 1, 6, 8, 9]
        var ans = 0

        func isConfusing(_ num: Int) -> Bool {
            var num = num
            let original = num
            var rotated = 0
            while num > 0 {
                let d = num % 10
                rotated = rotated * 10 + rotate[d]!
                num /= 10
            }
            return rotated != original
        }

        func dfs(_ cur: Int) {
            if cur > n { return }
            if cur != 0 && isConfusing(cur) {
                ans += 1
            }
            if cur == 0 {
                for d in [1, 6, 8, 9] {
                    dfs(d)
                }
            } else {
                for d in digits {
                    dfs(cur * 10 + d)
                }
            }
        }

        dfs(0)
        return ans
    }
}
