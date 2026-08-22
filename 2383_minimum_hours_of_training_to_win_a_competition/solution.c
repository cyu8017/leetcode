// LeetCode 2383 - Minimum Hours of Training to Win a Competition
// https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

int minNumberOfHours(int initialEnergy, int initialExperience, int* energy, int energySize, int* experience, int experienceSize) {
    (void)experienceSize;
    int ans = 0, en = initialEnergy, ex = initialExperience;
    for (int i = 0; i < energySize; i++) {
        if (en <= energy[i]) { int need = energy[i] - en + 1; ans += need; en += need; }
        if (ex <= experience[i]) { int need = experience[i] - ex + 1; ans += need; ex += need; }
        en -= energy[i];
        ex += experience[i];
    }
    return ans;
}
