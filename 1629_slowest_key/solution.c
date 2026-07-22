// LeetCode 1629 - Slowest Key
// https://leetcode.com/problems/slowest-key/

char slowestKey(int* releaseTimes, int releaseTimesSize, char* keysPressed) {
    int bestDur = releaseTimes[0];
    char bestKey = keysPressed[0];
    for (int i = 1; i < releaseTimesSize; i++) {
        int dur = releaseTimes[i] - releaseTimes[i - 1];
        if (dur > bestDur || (dur == bestDur && keysPressed[i] > bestKey)) {
            bestDur = dur;
            bestKey = keysPressed[i];
        }
    }
    return bestKey;
}
