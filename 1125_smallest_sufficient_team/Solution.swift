// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

class Solution {
    func smallestSufficientTeam(_ req_skills: [String], _ people: [[String]]) -> [Int] {
        var skillId: [String: Int] = [:]
        for (i, s) in req_skills.enumerated() { skillId[s] = i }
        let n = people.count
        var personMasks = [Int](repeating: 0, count: n)
        for i in 0..<n {
            var mask = 0
            for skill in people[i] { mask |= 1 << skillId[skill]! }
            personMasks[i] = mask
        }
        let target = (1 << req_skills.count) - 1
        var teamMask = [Int](repeating: 0, count: 1 << req_skills.count)
        var teamSize = [Int](repeating: Int.max, count: 1 << req_skills.count)
        teamSize[0] = 0
        for state in 0...target {
            if teamSize[state] == Int.max { continue }
            for i in 0..<n {
                let next = state | personMasks[i]
                if teamSize[next] > teamSize[state] + 1 {
                    teamSize[next] = teamSize[state] + 1
                    teamMask[next] = teamMask[state] | (1 << i)
                }
            }
        }
        var team: [Int] = []
        for i in 0..<n {
            if (teamMask[target] >> i) & 1 == 1 { team.append(i) }
        }
        return team
    }
}
