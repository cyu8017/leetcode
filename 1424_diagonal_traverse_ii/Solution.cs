// LeetCode 1424 - Diagonal Traverse Ii
// https://leetcode.com/problems/diagonal-traverse-ii/

using System.Collections.Generic;
using System.Linq;
public class Solution {
    public int[] FindDiagonalOrder(IList<IList<int>> nums) {
        var diagonals = new SortedDictionary<int, List<int>>();
        for (int row = 0; row < nums.Count; row++)
            for (int col = 0; col < nums[row].Count; col++) {
                int key = row + col;
                if (!diagonals.ContainsKey(key)) diagonals[key] = new List<int>();
                diagonals[key].Add(nums[row][col]);
            }
        var answer = new List<int>();
        foreach (var list in diagonals.Values) {
            list.Reverse();
            answer.AddRange(list);
        }
        return answer.ToArray();
    }
}
