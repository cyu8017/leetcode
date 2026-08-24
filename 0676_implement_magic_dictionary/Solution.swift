// LeetCode 0676 - Implement Magic Dictionary
// https://leetcode.com/problems/implement-magic-dictionary/

class MagicDictionary {
    private var words = [String]()

    init() {}

    func buildDict(_ dictionary: [String]) {
        words = dictionary
    }

    func search(_ searchWord: String) -> Bool {
        let target = Array(searchWord)
        for word in words {
            let w = Array(word)
            if w.count != target.count { continue }
            var diff = 0
            for i in 0..<w.count where w[i] != target[i] { diff += 1 }
            if diff == 1 { return true }
        }
        return false
    }
}
