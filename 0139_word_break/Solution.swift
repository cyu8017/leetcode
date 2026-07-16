class Solution {
    func wordBreak(_ s: String, _ wordDict: [String]) -> Bool {
        let chars = Array(s)
        let words = Set(wordDict)
        var canBreak = Array(repeating: false, count: chars.count + 1)
        canBreak[0] = true

        for end in 1...chars.count {
            for start in 0..<end where canBreak[start] &&
                words.contains(String(chars[start..<end])) {
                canBreak[end] = true
                break
            }
        }
        return canBreak[chars.count]
    }
}