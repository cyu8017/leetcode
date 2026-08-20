// LeetCode 1505 - Minimum Possible Integer After at Most K Adjacent Swaps On Digits
// https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

class Fenwick {
    private var bit: [Int]
    init(_ n: Int) { bit = Array(repeating: 0, count: n + 1) }
    func add(_ i: Int, _ delta: Int) {
        var i = i + 1
        while i < bit.count {
            bit[i] += delta
            i += i & -i
        }
    }
    func sum(_ i: Int) -> Int {
        var i = i, out = 0
        while i > 0 {
            out += bit[i]
            i -= i & -i
        }
        return out
    }
}

class Solution {
    func minInteger(_ num: String, _ k: Int) -> String {
        var k = k
        let chars = Array(num)
        var positions = Array(repeating: [Int](), count: 10)
        for (i, ch) in chars.enumerated() {
            positions[Int(String(ch))!].append(i)
        }
        var heads = Array(repeating: 0, count: 10)
        let fw = Fenwick(chars.count)
        var out = [Character]()
        for _ in 0..<chars.count {
            for digit in 0..<10 {
                if heads[digit] >= positions[digit].count { continue }
                let index = positions[digit][heads[digit]]
                let cost = index - fw.sum(index)
                if cost <= k {
                    k -= cost
                    heads[digit] += 1
                    fw.add(index, 1)
                    out.append(Character(String(digit)))
                    break
                }
            }
        }
        return String(out)
    }
}
