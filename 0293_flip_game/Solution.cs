// LeetCode 0293 - Flip Game
// https://leetcode.com/problems/flip-game/

using System.Collections.Generic;

public class Solution {
    public IList<string> GeneratePossibleNextMoves(string currentState) {
        var result = new List<string>();
        for (int index = 0; index < currentState.Length - 1; index++) {
            if (currentState[index] == '+' && currentState[index + 1] == '+') {
                result.Add(currentState.Substring(0, index) + "--" + currentState.Substring(index + 2));
            }
        }
        return result;
    }
}
