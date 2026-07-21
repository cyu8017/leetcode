// LeetCode 1871 - Jump Game VII
// https://leetcode.com/problems/jump-game-vii/

class Solution {
    func canReach(_ s: String, _ minJump: Int, _ maxJump: Int) -> Bool {
        let chars = Array(s)
        let n = chars.count
        var reachable = Array(repeating: false, count: n)
        reachable[0] = true
        var prefix = Array(repeating: 0, count: n + 1)

        for i in 0..<n {
            if i > 0 && chars[i] == "0" {
                let left = max(0, i - maxJump)
                let right = i - minJump
                if right >= left && prefix[right + 1] - prefix[left] > 0 {
                    reachable[i] = true
                }
            }
            prefix[i + 1] = prefix[i] + (reachable[i] ? 1 : 0)
        }

        return reachable[n - 1]
    }
}
