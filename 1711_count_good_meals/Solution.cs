// LeetCode 1711 - Count Good Meals
// https://leetcode.com/problems/count-good-meals/

public class Solution {
    public int CountPairs(int[] deliciousness) {
        const long mod = 1000000007L;
        var seen = new Dictionary<int, long>();
        long ans = 0;
        foreach (int value in deliciousness) {
            for (int power = 0; power < 22; power++) {
                if (seen.TryGetValue((1 << power) - value, out long count)) {
                    ans += count;
                }
            }
            seen[value] = seen.GetValueOrDefault(value) + 1;
        }
        return (int)(ans % mod);
    }
}
