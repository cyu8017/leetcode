// LeetCode 0849 - Maximize Distance to Closest Person
// https://leetcode.com/problems/maximize-distance-to-closest-person/

#define MAX(a,b) ((a)>(b)?(a):(b))

int maxDistToClosest(int* seats, int seatsSize) {
    int prev = -1, ans = 0;
    for (int i = 0; i < seatsSize; i++) {
        if (seats[i]) {
            if (prev == -1) ans = i;
            else ans = MAX(ans, (i - prev) / 2);
            prev = i;
        }
    }
    ans = MAX(ans, seatsSize - 1 - prev);
    return ans;
}
