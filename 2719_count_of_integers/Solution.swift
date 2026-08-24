// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

class Solution {
    private let MOD = 1_000_000_007
    private var minSum = 0
    private var maxSum = 0

    func count(_ num1: String, _ num2: String, _ min_sum: Int, _ max_sum: Int) -> Int {
        minSum = min_sum
        maxSum = max_sum
        return (dp(num2) - dp(dec(num1)) + MOD) % MOD
    }

    private func dec(_ s: String) -> String {
        var arr = Array(s)
        var i = arr.count - 1
        while i >= 0 && arr[i] == "0" {
            arr[i] = "9"
            i -= 1
        }
        if i >= 0 {
            let v = Int(arr[i].asciiValue!) - 1
            arr[i] = Character(UnicodeScalar(v)!)
        }
        var j = 0
        while j < arr.count - 1 && arr[j] == "0" { j += 1 }
        return String(arr[j...])
    }

    private func dp(_ s: String) -> Int {
        var memo: [String: Int] = [:]
        return dfs(Array(s), 0, 0, true, &memo)
    }

    private func dfs(_ s: [Character], _ pos: Int, _ sum: Int, _ tight: Bool, _ memo: inout [String: Int]) -> Int {
        if sum > maxSum { return 0 }
        if pos == s.count { return sum >= minSum ? 1 : 0 }
        let key = "\(pos),\(sum),\(tight ? 1 : 0)"
        if let v = memo[key] { return v }
        let up = tight ? Int(String(s[pos]))! : 9
        var res = 0
        for d in 0...up {
            res = (res + dfs(s, pos + 1, sum + d, tight && d == up, &memo)) % MOD
        }
        memo[key] = res
        return res
    }
}
