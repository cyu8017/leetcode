// LeetCode 3435 - Frequencies of Shortest Supersequences
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/

class Solution {
    func supersequences(_ words: [String]) -> [[Int]] {
        var used = Array(repeating: false, count: 26)
        for w in words {
            let a = Array(w)
            used[Int(a[0].asciiValue! - 97)] = true
            used[Int(a[1].asciiValue! - 97)] = true
        }
        var letters = [Int]()
        for i in 0..<26 where used[i] { letters.append(i) }
        let m = letters.count
        var best = 1_000_000_000
        var bestFreqs = [[Int]]()
        var freq = Array(repeating: 0, count: 26)
        func dfs(_ i: Int) {
            if i == m {
                for w in words {
                    let a = Array(w)
                    let x = Int(a[0].asciiValue! - 97), y = Int(a[1].asciiValue! - 97)
                    if x == y {
                        if freq[x] < 2 { return }
                    } else if freq[x] < 1 || freq[y] < 1 { return }
                }
                let sum = freq.reduce(0, +)
                if sum < best {
                    best = sum
                    bestFreqs = [freq]
                } else if sum == best {
                    bestFreqs.append(freq)
                }
                return
            }
            let L = letters[i]
            for c in 1...2 {
                freq[L] = c
                dfs(i + 1)
            }
            freq[L] = 0
        }
        dfs(0)
        return bestFreqs
    }
}
