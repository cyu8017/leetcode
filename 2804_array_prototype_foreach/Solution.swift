// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/

class Solution {
    func forEach(_ arr: [Int], _ callback: (Int, Int, [Int]) -> Void) {
        for i in arr.indices { callback(arr[i], i, arr) }
    }
}
