// LeetCode 3005 - Count Elements With Maximum Frequency
// https://leetcode.com/problems/count-elements-with-maximum-frequency/

int maxFrequencyElements(int* nums, int numsSize) {
    int cnt[101] = {0};
    for (int i = 0; i < numsSize; i++) cnt[nums[i]]++;
    int mx = -1, ans = 0;
    for (int i = 0; i < 101; i++) {
        if (cnt[i] > mx) { mx = cnt[i]; ans = cnt[i]; }
        else if (cnt[i] == mx) ans += cnt[i];
    }
    return ans;
}
