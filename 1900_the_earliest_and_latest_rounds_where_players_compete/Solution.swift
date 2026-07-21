// LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

class Solution {
    func earliestAndLatest(_ n: Int, _ firstPlayer: Int, _ secondPlayer: Int) -> [Int] {
        let first = firstPlayer
        let second = secondPlayer
        var memo: [[Int]: (Int, Int)] = [:]

        func dfs(_ players: [Int]) -> (Int, Int) {
            if let cached = memo[players] {
                return cached
            }

            let count = players.count
            let firstIndex = players.firstIndex(of: first)!
            let secondIndex = players.firstIndex(of: second)!
            if firstIndex + secondIndex == count - 1 {
                let result = (1, 1)
                memo[players] = result
                return result
            }

            var choices: [[Int]] = []
            for index in 0..<(count / 2) {
                let left = players[index]
                let right = players[count - 1 - index]
                if left == first || left == second {
                    choices.append([left])
                } else if right == first || right == second {
                    choices.append([right])
                } else {
                    choices.append([left, right])
                }
            }
            if count % 2 == 1 {
                choices.append([players[count / 2]])
            }

            var earliest = Int.max
            var latest = 0

            func enumeratePicks(_ i: Int, _ current: [Int]) {
                if i == choices.count {
                    let winners = current.sorted()
                    let (early, late) = dfs(winners)
                    earliest = min(earliest, early + 1)
                    latest = max(latest, late + 1)
                    return
                }
                for pick in choices[i] {
                    enumeratePicks(i + 1, current + [pick])
                }
            }

            enumeratePicks(0, [])

            let result = (earliest, latest)
            memo[players] = result
            return result
        }

        let result = dfs(Array(1...n))
        return [result.0, result.1]
    }
}
