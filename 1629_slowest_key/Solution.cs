// LeetCode 1629 - Slowest Key
// https://leetcode.com/problems/slowest-key/

public class Solution {
    public char SlowestKey(int[] releaseTimes, string keysPressed) {
        int bestDur = releaseTimes[0];
        char bestKey = keysPressed[0];
        for (int i = 1; i < releaseTimes.Length; i++) {
            int duration = releaseTimes[i] - releaseTimes[i - 1];
            if (duration > bestDur || (duration == bestDur && keysPressed[i] > bestKey)) {
                bestDur = duration;
                bestKey = keysPressed[i];
            }
        }
        return bestKey;
    }
}
