// LeetCode 2178 - Maximum Split of Positive Even Integers
// https://leetcode.com/problems/maximum-split-of-positive-even-integers/

public class Solution {
    public IList<long> MaximumEvenSplit(long finalSum) {
        if (finalSum % 2 != 0) return new List<long>();
        var ans = new List<long>();
        for (long x = 2; x <= finalSum; x += 2) {
            ans.Add(x);
            finalSum -= x;
        }
        ans[ans.Count - 1] += finalSum;
        return ans;
    }
}
