// LeetCode 1534 - Count Good Triplets
// https://leetcode.com/problems/count-good-triplets/

class Solution {
    func countGoodTriplets(_ arr: [Int], _ a: Int, _ b: Int, _ c: Int) -> Int {
        var ans = 0
        let n = arr.count
        for i in 0..<n {
            for j in (i + 1)..<n {
                if abs(arr[i] - arr[j]) > a { continue }
                for k in (j + 1)..<n {
                    if abs(arr[j] - arr[k]) <= b && abs(arr[i] - arr[k]) <= c {
                        ans += 1
                    }
                }
            }
        }
        return ans
    }
}
