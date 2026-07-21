// LeetCode 1868 - Product of Two Run-Length Encoded Arrays
// https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

class Solution {
    func findRLEArray(_ encoded1: [[Int]], _ encoded2: [[Int]]) -> [[Int]] {
        var result: [[Int]] = []
        var i = 0
        var j = 0
        var rem1 = encoded1[0][1]
        var rem2 = encoded2[0][1]

        while i < encoded1.count {
            let take = min(rem1, rem2)
            let value = encoded1[i][0] * encoded2[j][0]
            if !result.isEmpty && result.last![0] == value {
                result[result.count - 1][1] += take
            } else {
                result.append([value, take])
            }

            rem1 -= take
            rem2 -= take
            if rem1 == 0 {
                i += 1
                if i < encoded1.count {
                    rem1 = encoded1[i][1]
                }
            }
            if rem2 == 0 {
                j += 1
                if j < encoded2.count {
                    rem2 = encoded2[j][1]
                }
            }
        }

        return result
    }
}
