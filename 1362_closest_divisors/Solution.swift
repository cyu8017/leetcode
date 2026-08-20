// LeetCode 1362 - Closest Divisors
// https://leetcode.com/problems/closest-divisors/

class Solution {
    func closestDivisors(_ num: Int) -> [Int] {
        var best: [Int]? = nil
        for x in [num + 1, num + 2] {
            var a = Int(Double(x).squareRoot())
            while a > 0 {
                if x % a == 0 {
                    let pair = [a, x / a]
                    if best == nil || pair[1] - pair[0] < best![1] - best![0] { best = pair }
                    break
                }
                a -= 1
            }
        }
        return best ?? []
    }
}
