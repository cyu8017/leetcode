// LeetCode 0982 - Triples with Bitwise AND Equal To Zero
// https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

class Solution {
    func countTriplets(_ nums: [Int]) -> Int {
        var cnt = [Int: Int]()
        for a in nums {
            for b in nums {
                cnt[a & b, default: 0] += 1
            }
        }
        var ans = 0
        for c in nums {
            for (k, v) in cnt where (k & c) == 0 {
                ans += v
            }
        }
        return ans
    }
}
