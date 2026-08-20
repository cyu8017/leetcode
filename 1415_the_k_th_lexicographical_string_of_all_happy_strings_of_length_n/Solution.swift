// LeetCode 1415 - The k-th Lexicographical String of All Happy Strings of Length n
// https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

class Solution {
    func getHappyString(_ n: Int, _ k: Int) -> String {
        var answer = [String]()
        func build(_ path: String) {
            if path.count == n { answer.append(path); return }
            for char in ["a", "b", "c"] {
                if path.isEmpty || String(path.last!) != char { build(path + char) }
            }
        }
        build("")
        return k <= answer.count ? answer[k - 1] : ""
    }
}
