// LeetCode 2150 - Find All Lonely Numbers in the Array
// https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

public class Solution {
    public IList<int> FindLonely(int[] nums) {
        var freq = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!freq.ContainsKey(x)) freq[x] = 0;
            freq[x]++;
        }
        var ans = new List<int>();
        foreach (var kv in freq)
            if (kv.Value == 1 && !freq.ContainsKey(kv.Key - 1) && !freq.ContainsKey(kv.Key + 1))
                ans.Add(kv.Key);
        return ans;
    }
}
