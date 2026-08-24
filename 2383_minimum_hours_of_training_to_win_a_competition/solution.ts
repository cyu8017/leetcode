// LeetCode 2383 - Minimum Hours of Training to Win a Competition
// https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

export function minNumberOfHours(initialEnergy: number, initialExperience: number, energy: number[], experience: number[]): number {
    let ans = 0;
    let en = initialEnergy, ex = initialExperience;
    for (let i = 0; i < energy.length; i++) {
        if (en <= energy[i]) {
            const need = energy[i] - en + 1;
            ans += need;
            en += need;
        }
        if (ex <= experience[i]) {
            const need = experience[i] - ex + 1;
            ans += need;
            ex += need;
        }
        en -= energy[i];
        ex += experience[i];
    }
    return ans;
}
