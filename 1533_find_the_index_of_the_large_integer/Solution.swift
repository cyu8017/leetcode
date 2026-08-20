// LeetCode 1533 - Find the Index of the Large Integer
// https://leetcode.com/problems/find-the-index-of-the-large-integer/

class ArrayReader {
    private let arr: [Int]
    init(_ arr: [Int]) { self.arr = arr }
    func compareSub(_ l: Int, _ r: Int, _ x: Int, _ y: Int) -> Int {
        var a = 0, b = 0
        for i in l...r { a += arr[i] }
        for i in x...y { b += arr[i] }
        return a == b ? 0 : (a > b ? 1 : -1)
    }
    func length() -> Int { arr.count }
}

class Solution {
    func getIndex(_ arr: [Int]) -> Int {
        getIndex(ArrayReader(arr))
    }

    func getIndex(_ reader: ArrayReader) -> Int {
        var left = 0, right = reader.length() - 1
        while left < right {
            let length = right - left + 1
            let half = length / 2
            let result = reader.compareSub(left, left + half - 1, right - half + 1, right)
            if result == 0 { return left + half }
            if result > 0 {
                right = left + half - 1
            } else {
                left = right - half + 1
            }
        }
        return left
    }
}
