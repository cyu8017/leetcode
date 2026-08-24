// LeetCode 3999 - Minimum Number of String Groups Through Transformations
// https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/


class Solution {
    func minimumGroups(_ words: [String]) -> Int {
        func leastRotation(_ s: [Character]) -> Int {
            let n = s.count
            var i = 0, j = 1, k = 0
            while i < n && j < n && k < n {
                let a = s[(i + k) % n]
                let b = s[(j + k) % n]
                if a == b { k += 1 }
                else {
                    if a > b { i += k + 1 }
                    else { j += k + 1 }
                    if i == j { j += 1 }
                    k = 0
                }
            }
            return i < j ? i : j
        }
        func canonicalRotate(_ s: String) -> String {
            let arr = Array(s)
            let n = arr.count
            if n <= 1 { return s }
            let r = leastRotation(arr)
            if r == 0 { return s }
            return String(arr[r...]) + String(arr[..<r])
        }
        var keys = [String]()
        for w in words {
            let arr = Array(w)
            var even = "", odd = ""
            for i in 0..<arr.count {
                if i % 2 == 0 { even.append(arr[i]) }
                else { odd.append(arr[i]) }
            }
            keys.append(canonicalRotate(even) + "#" + canonicalRotate(odd))
        }
        keys.sort()
        var groups = 0
        for i in 0..<keys.count {
            if i == 0 || keys[i] != keys[i - 1] { groups += 1 }
        }
        return groups
    }
}
