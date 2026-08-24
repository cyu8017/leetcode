// LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

class Solution {
    func makeSimilar(_ nums: [Int], _ target: [Int]) -> Int {
        let nums = nums.sorted()
        let target = target.sorted()
        var oddN = [Int](), evenN = [Int](), oddT = [Int](), evenT = [Int]()
        for x in nums {
            if x % 2 == 0 { evenN.append(x) } else { oddN.append(x) }
        }
        for x in target {
            if x % 2 == 0 { evenT.append(x) } else { oddT.append(x) }
        }
        var ans = 0
        for i in 0..<oddN.count {
            let diff = oddN[i] - oddT[i]
            if diff > 0 { ans += diff / 2 }
        }
        for i in 0..<evenN.count {
            let diff = evenN[i] - evenT[i]
            if diff > 0 { ans += diff / 2 }
        }
        return ans
    }
}
