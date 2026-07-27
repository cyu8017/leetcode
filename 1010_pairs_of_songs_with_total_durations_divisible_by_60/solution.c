// LeetCode 1010 - Pairs of Songs With Total Durations Divisible by 60
// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

int numPairsDivisibleBy60(int* time, int timeSize) {
    int count[60] = {0};
    int ans = 0;
    for (int i = 0; i < timeSize; i++) {
        int t = time[i] % 60;
        ans += count[(60 - t) % 60];
        count[t]++;
    }
    return ans;
}
