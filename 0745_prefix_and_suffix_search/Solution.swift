// LeetCode 0745 - Prefix and Suffix Search
// https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter {
    private var index = [String: Int]()

    init(_ words: [String]) {
        for (i, word) in words.enumerated() {
            let chars = Array(word)
            for p in 0...chars.count {
                for s in 0...chars.count {
                    let key = String(chars.prefix(p)) + "#" + String(chars.suffix(s))
                    index[key] = i
                }
            }
        }
    }

    func f(_ pref: String, _ suff: String) -> Int {
        index[pref + "#" + suff] ?? -1
    }
}
