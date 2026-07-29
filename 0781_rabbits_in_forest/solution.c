// LeetCode 0781 - Rabbits in Forest
// https://leetcode.com/problems/rabbits-in-forest/

int numRabbits(int* answers, int answersSize) {
    int cnt[1000] = {0};
    for (int i = 0; i < answersSize; i++) cnt[answers[i]]++;
    int ans = 0;
    for (int x = 0; x < 1000; x++) {
        if (!cnt[x]) continue;
        int group = x + 1;
        ans += ((cnt[x] + group - 1) / group) * group;
    }
    return ans;
}
