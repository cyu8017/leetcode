class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        best = (releaseTimes[0], keysPressed[0]); prev = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i-1]
            best = max(best, (duration, keysPressed[i]))
        return best[1]
