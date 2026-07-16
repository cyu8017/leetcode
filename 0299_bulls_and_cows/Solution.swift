// LeetCode 0299 - Bulls and Cows
// https://leetcode.com/problems/bulls-and-cows/

class Solution {
    func getHint(_ secret: String, _ guess: String) -> String {
        var bulls = 0
        var secretCounts: [Character: Int] = [:]
        var guessCounts: [Character: Int] = [:]
        let secretChars = Array(secret)
        let guessChars = Array(guess)
        for index in 0..<secretChars.count {
            if secretChars[index] == guessChars[index] {
                bulls += 1
            } else {
                secretCounts[secretChars[index], default: 0] += 1
                guessCounts[guessChars[index], default: 0] += 1
            }
        }
        var cows = 0
        for (digit, count) in guessCounts {
            cows += min(count, secretCounts[digit, default: 0])
        }
        return "\(bulls)A\(cows)B"
    }
}
