// LeetCode 2749 - Minimum Operations to Make the Integer Zero
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

class Solution {
    func makeTheIntegerZero(_ num1: Int, _ num2: Int) -> Int {
        for k in 1...60 {
            let rem = num1 - k * num2
            if rem < k { continue }
            if rem.nonzeroBitCount <= k { return k }
        }
        return -1
    }
}
