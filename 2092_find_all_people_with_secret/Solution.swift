// LeetCode 2092 - Find All People With Secret
// https://leetcode.com/problems/find-all-people-with-secret/

class Solution {
    func findAllPeople(_ n: Int, _ meetings: [[Int]], _ firstPerson: Int) -> [Int] {
        let meetings = meetings.sorted { $0[2] < $1[2] }
        var parent = Array(0..<n)
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        func unite(_ a: Int, _ b: Int) {
            let a = find(a), b = find(b)
            if a != b { parent[a] = b }
        }
        var know = [Bool](repeating: false, count: n)
        know[0] = true
        know[firstPerson] = true
        unite(0, firstPerson)
        var i = 0
        while i < meetings.count {
            var j = i
            while j < meetings.count && meetings[j][2] == meetings[i][2] { j += 1 }
            for k in i..<j { unite(meetings[k][0], meetings[k][1]) }
            let root0 = find(0)
            var reset = [Int]()
            for k in i..<j {
                let a = meetings[k][0], b = meetings[k][1]
                if find(a) != root0 {
                    reset.append(a)
                    reset.append(b)
                } else {
                    know[a] = true
                    know[b] = true
                }
            }
            for x in reset { parent[x] = x }
            i = j
        }
        return (0..<n).filter { find($0) == find(0) || know[$0] }
    }
}
