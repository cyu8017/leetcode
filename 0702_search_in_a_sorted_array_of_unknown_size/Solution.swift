// LeetCode 0702 - Search in a Sorted Array of Unknown Size
// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

class ArrayReader {
    private let secret: [Int]
    init(_ secret: [Int]) { self.secret = secret }
    func get(_ index: Int) -> Int {
        if index < 0 || index >= secret.count { return 2147483647 }
        return secret[index]
    }
}

class Solution {
    func search(_ secret: [Int], _ target: Int) -> Int {
        search(ArrayReader(secret), target)
    }

    func search(_ reader: ArrayReader, _ target: Int) -> Int {
        var right = 1
        while reader.get(right) < target { right <<= 1 }
        var left = right >> 1
        while left <= right {
            let mid = left + (right - left) / 2
            let value = reader.get(mid)
            if value == target { return mid }
            if value > target { right = mid - 1 }
            else { left = mid + 1 }
        }
        return -1
    }
}
