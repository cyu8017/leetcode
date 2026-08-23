// LeetCode 2766 - Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<Integer> relocateMarbles(int[] nums, int[] moveFrom, int[] moveTo) {
        var pos = new HashSet<Integer>(nums);
        for (int i = 0; i < moveFrom.length; i++) {
            pos.remove(moveFrom[i]);
            pos.add(moveTo[i]);
        }
        return pos.OrderBy(x -> x).ToList();
    }
}
