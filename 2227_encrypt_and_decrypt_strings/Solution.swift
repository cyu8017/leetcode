// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

class Encrypter {
    private var enc: [Character: String] = [:]
    private var cnt: [String: Int] = [:]

    init(_ keys: [Character], _ values: [String], _ dictionary: [String]) {
        for i in 0..<keys.count { enc[keys[i]] = values[i] }
        for w in dictionary {
            let e = encrypt(w)
            cnt[e, default: 0] += 1
        }
    }

    func encrypt(_ word1: String) -> String {
        var b = ""
        for c in word1 {
            guard let v = enc[c] else { return "" }
            b += v
        }
        return b
    }

    func decrypt(_ word2: String) -> Int {
        cnt[word2, default: 0]
    }
}
