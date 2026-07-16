// LeetCode 0514 - Freedom Trail
// https://leetcode.com/problems/freedom-trail/

class Solution {
    func findRotateSteps(_ ring: String, _ key: String) -> Int {
        let ringChars = Array(ring)
        let keyChars = Array(key)
        var positions: [Character: [Int]] = [:]
        for (index, char) in ringChars.enumerated() {
            positions[char, default: []].append(index)
        }

        var memo: [String: Int] = [:]

        func dp(_ ringIndex: Int, _ keyIndex: Int) -> Int {
            if keyIndex == keyChars.count {
                return 0
            }

            let state = "\(ringIndex),\(keyIndex)"
            if let cached = memo[state] {
                return cached
            }

            var best = Int.max
            for pos in positions[keyChars[keyIndex], default: []] {
                let clockwise = (pos - ringIndex + ringChars.count) % ringChars.count
                let counter = (ringIndex - pos + ringChars.count) % ringChars.count
                let steps = min(clockwise, counter) + 1
                best = min(best, steps + dp(pos, keyIndex + 1))
            }

            memo[state] = best
            return best
        }

        return dp(0, 0)
    }
}
