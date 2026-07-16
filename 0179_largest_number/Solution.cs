using System;
using System.Linq;

public class Solution
{
    public string LargestNumber(int[] nums)
    {
        var parts = nums.Select(num => num.ToString()).ToArray();
        Array.Sort(parts, (a, b) => string.CompareOrdinal(b + a, a + b));
        return parts[0] == "0" ? "0" : string.Concat(parts);
    }
}
