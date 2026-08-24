// LeetCode 0969 - Pancake Sorting
// https://leetcode.com/problems/pancake-sorting/

class Solution {
    func pancakeSort(_ arr: [Int]) -> [Int] {
        var a = arr
        var ans = [Int]()
        for size in stride(from: a.count, through: 2, by: -1) {
            let i = a.firstIndex(of: size)!
            if i == size - 1 { continue }
            if i > 0 {
                ans.append(i + 1)
                a[0...i].reverse()
            }
            ans.append(size)
            a[0...(size - 1)].reverse()
        }
        return ans
    }
}
