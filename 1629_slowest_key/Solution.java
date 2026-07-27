// LeetCode 1629 - Slowest Key
// https://leetcode.com/problems/slowest-key/

class Solution {
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        int bestDur = releaseTimes[0];
        char bestKey = keysPressed.charAt(0);
        for (int i = 1; i < releaseTimes.length; i++) {
            int duration = releaseTimes[i] - releaseTimes[i - 1];
            char key = keysPressed.charAt(i);
            if (duration > bestDur || (duration == bestDur && key > bestKey)) {
                bestDur = duration;
                bestKey = key;
            }
        }
        return bestKey;
    }
}
