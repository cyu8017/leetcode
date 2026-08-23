// LeetCode 0514 - Freedom Trail
// https://leetcode.com/problems/freedom-trail/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int findRotateSteps(String ring, String key) {
        Map<Character, List<Integer>> positions = new HashMap<>();
        for (int index = 0; index < ring.length(); index++) {
            positions.computeIfAbsent(ring.charAt(index), ignored -> new ArrayList<>()).add(index);
        }
        Map<String, Integer> memo = new HashMap<>();
        return dp(0, 0, ring, key, positions, memo);
    }

    private int dp(int ringIndex, int keyIndex, String ring, String key,
                   Map<Character, List<Integer>> positions, Map<String, Integer> memo) {
        if (keyIndex == key.length()) {
            return 0;
        }
        String state = ringIndex + "," + keyIndex;
        if (memo.containsKey(state)) {
            return memo.get(state);
        }
        int best = Integer.MAX_VALUE;
        for (int pos : positions.get(key.charAt(keyIndex))) {
            int clockwise = (pos - ringIndex + ring.length()) % ring.length();
            int counter = (ringIndex - pos + ring.length()) % ring.length();
            int steps = Math.min(clockwise, counter) + 1;
            best = Math.min(best, steps + dp(pos, keyIndex + 1, ring, key, positions, memo));
        }
        memo.put(state, best);
        return best;
    }
}
