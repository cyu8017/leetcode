// LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

class Solution {
    func maximizeSquareArea(_ m: Int, _ n: Int, _ hFences: [Int], _ vFences: [Int]) -> Int {
        let mod = 1_000_000_007
        let hg = gaps(hFences, m)
        let vg = gaps(vFences, n)
        var best = -1
        for g in hg where vg.contains(g) {
            best = max(best, g)
        }
        if best < 0 { return -1 }
        return best * best % mod
    }

    private func gaps(_ fences: [Int], _ bound: Int) -> Set<Int> {
        var list = [1] + fences + [bound]
        list.sort()
        var gaps = Set<Int>()
        for i in 0..<list.count {
            for j in (i + 1)..<list.count {
                gaps.insert(list[j] - list[i])
            }
        }
        return gaps
    }
}
