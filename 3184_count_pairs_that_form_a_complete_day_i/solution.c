// LeetCode 3184 - Count Pairs That Form a Complete Day I
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

int countCompleteDayPairs(int* hours, int hoursSize) {
    int cnt[24] = {0}, ans = 0;
    for (int i = 0; i < hoursSize; i++) {
        ans += cnt[(24 - hours[i] % 24) % 24];
        cnt[hours[i] % 24]++;
    }
    return ans;
}
