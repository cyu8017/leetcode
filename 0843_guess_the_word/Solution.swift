// LeetCode 0843 - Guess the Word
// https://leetcode.com/problems/guess-the-word/

protocol Master {
    func guess(_ word: String) -> Int
}

class Solution {
    func findSecretWord(_ words: [String], _ master: Master) {
        var candidates = words
        while !candidates.isEmpty {
            var best = candidates[0]
            var bestWorst = candidates.count + 1
            for w in candidates {
                var buckets = Array(repeating: 0, count: 7)
                for c in candidates { buckets[match(w, c)] += 1 }
                let worst = buckets.max() ?? 0
                if worst < bestWorst {
                    bestWorst = worst
                    best = w
                }
            }
            let score = master.guess(best)
            if score == 6 { return }
            candidates = candidates.filter { match($0, best) == score }
        }
    }

    private func match(_ a: String, _ b: String) -> Int {
        let ca = Array(a), cb = Array(b)
        var m = 0
        for i in 0..<ca.count where ca[i] == cb[i] { m += 1 }
        return m
    }
}
