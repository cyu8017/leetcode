class Solution {
    func wordBreak(_ s: String, _ wordDict: [String]) -> [String] {
        let chars = Array(s)
        let words = Set(wordDict)
        var memo = [Int: [String]]()

        func dfs(_ start: Int) -> [String] {
            if start == chars.count { return [""] }
            if let sentences = memo[start] { return sentences }

            var sentences = [String]()
            for end in (start + 1)...chars.count {
                let word = String(chars[start..<end])
                guard words.contains(word) else { continue }
                for tail in dfs(end) {
                    sentences.append(tail.isEmpty ? word : "\(word) \(tail)")
                }
            }
            memo[start] = sentences
            return sentences
        }

        return dfs(0)
    }
}