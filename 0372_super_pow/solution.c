// LeetCode 0372 - Super Pow
// https://leetcode.com/problems/super-pow/

static int powMod(int base, int exponent, int mod) {
    long long result = 1;
    long long current = base % mod;

    while (exponent > 0) {
        if (exponent & 1) {
            result = result * current % mod;
        }
        current = current * current % mod;
        exponent >>= 1;
    }

    return (int)result;
}

int superPow(int a, int* b, int bSize) {
    const int mod = 1337;
    int result = 1;

    a %= mod;
    for (int index = 0; index < bSize; index++) {
        result = (int)((long long)powMod(result, 10, mod) * powMod(a, b[index], mod) % mod);
    }

    return result;
}
