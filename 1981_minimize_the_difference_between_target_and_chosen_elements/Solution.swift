// LeetCode 1981 - Minimize the Difference Between Target and Chosen Elements
// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

class Solution {
    func minimizeTheDifference(_ mat: [[Int]], _ target: Int) -> Int {
        var possible: Set<Int> = [0]
        for row in mat {
            let uniq = Set(row)
            var nxt = Set<Int>()
            for s in possible {
                for x in uniq { nxt.insert(s + x) }
            }
            var kept = Set(nxt.filter { $0 <= target })
            let above = nxt.filter { $0 > target }
            if let mn = above.min() { kept.insert(mn) }
            possible = kept.isEmpty ? [nxt.min()!] : kept
        }
        return possible.map { abs($0 - target) }.min()!
    }
}
