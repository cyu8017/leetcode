// LeetCode 1732 - Find the Highest Altitude
// https://leetcode.com/problems/find-the-highest-altitude/

int largestAltitude(int* gain, int gainSize) {
    int altitude = 0;
    int best = 0;
    for (int i = 0; i < gainSize; i++) {
        altitude += gain[i];
        if (altitude > best) {
            best = altitude;
        }
    }
    return best;
}
