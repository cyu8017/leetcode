// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<IList<string>> SuggestedProducts(string[] products, string searchWord) {
        System.Array.Sort(products);
        var answer = new List<IList<string>>();
        string prefix = "";
        foreach (char ch in searchWord) {
            prefix += ch;
            int i = LowerBound(products, prefix);
            var row = new List<string>();
            for (int j = i; j < products.Length && j < i + 3; j++) {
                if (products[j].StartsWith(prefix)) row.Add(products[j]);
                else break;
            }
            answer.Add(row);
        }
        return answer;
    }

    private static int LowerBound(string[] arr, string target) {
        int lo = 0, hi = arr.Length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (string.CompareOrdinal(arr[mid], target) < 0) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
