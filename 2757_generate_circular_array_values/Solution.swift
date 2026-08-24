// LeetCode 2757 - Generate Circular Array Values
// https://leetcode.com/problems/generate-circular-array-values/

class Solution {
    func cyclicGenerator(_ arr: [Int], _ startIndex: Int) -> () -> Int {
        var i = startIndex
        let n = arr.count
        return {
            let v = arr[i]
            i = (i + 1) % n
            return v
        }
    }
}
