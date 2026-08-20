// LeetCode 1916 - Count Ways to Build Rooms in an Ant Colony
// https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

class Solution {
    func waysToBuildRooms(_ prevRoom: [Int]) -> Int {
        let MOD = 1_000_000_007
        let n = prevRoom.count
        var children = Array(repeating: [Int](), count: n)
        for (room, prev) in prevRoom.enumerated() {
            if prev != -1 { children[prev].append(room) }
        }
        var fact = Array(repeating: 1, count: n + 1)
        var invFact = Array(repeating: 1, count: n + 1)
        for i in 1...n { fact[i] = fact[i - 1] * i % MOD }
        func modPow(_ base: Int, _ exp: Int) -> Int {
            var b = base % MOD, e = exp, r = 1
            while e > 0 {
                if e & 1 == 1 { r = r * b % MOD }
                b = b * b % MOD
                e >>= 1
            }
            return r
        }
        invFact[n] = modPow(fact[n], MOD - 2)
        for i in stride(from: n, through: 1, by: -1) {
            invFact[i - 1] = invFact[i] * i % MOD
        }
        func comb(_ a: Int, _ b: Int) -> Int {
            fact[a] * invFact[b] % MOD * invFact[a - b] % MOD
        }
        func dfs(_ node: Int) -> (Int, Int) {
            var size = 0, ways = 1
            for child in children[node] {
                let (cs, cw) = dfs(child)
                ways = ways * cw % MOD * comb(size + cs, cs) % MOD
                size += cs
            }
            return (size + 1, ways)
        }
        return dfs(0).1
    }
}
