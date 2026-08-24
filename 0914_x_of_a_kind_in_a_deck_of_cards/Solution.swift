// LeetCode 0914 - X of a Kind in a Deck of Cards
// https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution {
    func hasGroupsSizeX(_ deck: [Int]) -> Bool {
        var count = [Int: Int]()
        for x in deck { count[x, default: 0] += 1 }
        var g = 0
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        for c in count.values { g = gcd(g, c) }
        return g >= 2
    }
}
