// LeetCode 3185 - Count Pairs That Form a Complete Day II
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/

long long countCompleteDayPairs(int* hours, int hoursSize) {
    int cnt[24] = {0};
    long long ans = 0;
    for (int i = 0; i < hoursSize; i++) {
        ans += cnt[(24 - hours[i] % 24) % 24];
        cnt[hours[i] % 24]++;
    }
    return ans;
}
