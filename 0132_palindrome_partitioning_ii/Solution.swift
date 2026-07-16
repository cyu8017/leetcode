class Solution {
    func minCut(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        guard n > 0 else { return 0 }
        var isPalindrome = Array(repeating: Array(repeating: false, count: n), count: n)

        for start in stride(from: n - 1, through: 0, by: -1) {
            for end in start..<n where chars[start] == chars[end] &&
                (end - start < 2 || isPalindrome[start + 1][end - 1]) {
                isPalindrome[start][end] = true
            }
        }

        var cuts = Array(0..<n)
        for end in 0..<n {
            if isPalindrome[0][end] {
                cuts[end] = 0
            } else {
                for start in 0..<end where isPalindrome[start + 1][end] {
                    cuts[end] = min(cuts[end], cuts[start] + 1)
                }
            }
        }
        return cuts[n - 1]
    }
}