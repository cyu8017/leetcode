class Solution {
    func partition(_ s: String) -> [[String]] {
        let chars = Array(s)
        var result = [[String]]()
        var path = [String]()

        func isPalindrome(_ left: Int, _ right: Int) -> Bool {
            var left = left, right = right
            while left < right {
                if chars[left] != chars[right] { return false }
                left += 1
                right -= 1
            }
            return true
        }

        func dfs(_ start: Int) {
            if start == chars.count {
                result.append(path)
                return
            }
            for end in start..<chars.count where isPalindrome(start, end) {
                path.append(String(chars[start...end]))
                dfs(end + 1)
                path.removeLast()
            }
        }

        dfs(0)
        return result
    }
}