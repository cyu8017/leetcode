// LeetCode 3577 - Count the Number of Computer Unlocking Permutations
// https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

int countPermutations(int* complexity, int complexitySize) {
    const long long mod = 1000000007LL;
    long long ans = 1;
    for (int i = 1; i < complexitySize; i++) {
        if (complexity[i] <= complexity[0]) return 0;
        ans = ans * i % mod;
    }
    return (int)ans;
}
