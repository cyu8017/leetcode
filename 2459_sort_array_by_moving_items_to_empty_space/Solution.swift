// LeetCode 2459 - Sort Array By Moving Items to Empty Space
// https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

class Solution {
    func sortArray(_ nums: [Int]) -> Int {
        min(solveOne(nums, true), solveOne(nums, false))
    }

    private func solveOne(_ nums: [Int], _ startZero: Bool) -> Int {
        let n = nums.count
        var arr = nums
        var pos = [Int: Int]()
        for i in 0..<n { pos[arr[i]] = i }
        var ops = 0
        while true {
            let empty = pos[0]!
            let should = startZero ? empty : (empty == n - 1 ? 0 : empty + 1)
            if arr[empty] == should {
                var found = -1
                for i in 0..<n {
                    let want = startZero ? i : (i == n - 1 ? 0 : i + 1)
                    if arr[i] != want {
                        found = i
                        break
                    }
                }
                if found == -1 { return ops }
                let v = arr[found]
                arr.swapAt(empty, found)
                pos[0] = found
                pos[v] = empty
                ops += 1
                continue
            }
            let j = pos[should]!
            let vv = arr[j]
            arr.swapAt(empty, j)
            pos[0] = j
            pos[vv] = empty
            ops += 1
        }
    }
}
