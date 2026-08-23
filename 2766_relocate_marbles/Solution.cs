// LeetCode 2766 - Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<int> RelocateMarbles(int[] nums, int[] moveFrom, int[] moveTo) {
        var pos = new HashSet<int>(nums);
        for (int i = 0; i < moveFrom.Length; i++) {
            pos.Remove(moveFrom[i]);
            pos.Add(moveTo[i]);
        }
        return pos.OrderBy(x => x).ToList();
    }
}
