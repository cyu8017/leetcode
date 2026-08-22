// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

int furthestDistanceFromOrigin(char* moves) {
    int L = 0, R = 0, u = 0;
    for (int i = 0; moves[i]; i++) {
        if (moves[i] == 'L') L++;
        else if (moves[i] == 'R') R++;
        else u++;
    }
    int d = L - R;
    if (d < 0) d = -d;
    return d + u;
}
