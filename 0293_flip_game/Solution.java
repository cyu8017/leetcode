// LeetCode 0293 - Flip Game
// https://leetcode.com/problems/flip-game/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generatePossibleNextMoves(String currentState) {
        List<String> result = new ArrayList<>();
        for (int index = 0; index < currentState.length() - 1; index++) {
            if (currentState.charAt(index) == '+' && currentState.charAt(index + 1) == '+') {
                result.add(currentState.substring(0, index) + "--" + currentState.substring(index + 2));
            }
        }
        return result;
    }
}
