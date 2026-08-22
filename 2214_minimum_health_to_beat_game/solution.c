// LeetCode 2214 - Minimum Health to Beat Game
// https://leetcode.com/problems/minimum-health-to-beat-game/

long long minimumHealth(int* damage, int damageSize, int armor) {
    long long sum = 0;
    int mx = 0;
    for (int i = 0; i < damageSize; i++) {
        sum += damage[i];
        if (damage[i] > mx) mx = damage[i];
    }
    int reduce = armor < mx ? armor : mx;
    return sum - reduce + 1;
}
