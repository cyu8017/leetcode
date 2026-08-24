// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/

class Solution {
    func createObject(_ keysArr: [String], _ valuesArr: [Int]) -> [String: Int] {
        var output: [String: Int] = [:]
        let n = min(keysArr.count, valuesArr.count)
        for i in 0..<n where output[keysArr[i]] == nil {
            output[keysArr[i]] = valuesArr[i]
        }
        return output
    }
}
