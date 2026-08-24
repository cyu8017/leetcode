// LeetCode 2600 - K Items With the Maximum Sum
// https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution {
    func kItemsWithMaximumSum(_ numOnes: Int, _ numZeros: Int, _ numNegOnes: Int, _ k: Int) -> Int {
        var k = k
        var ans = 0
        var take = min(numOnes, k)
        ans += take
        k -= take
        take = min(numZeros, k)
        k -= take
        take = min(numNegOnes, k)
        ans -= take
        return ans
    }
}
