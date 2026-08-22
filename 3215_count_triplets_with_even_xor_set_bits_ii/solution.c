// LeetCode 3215 - Count Triplets with Even XOR Set Bits II
// https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-ii/

static int pc3215(unsigned x) { int c = 0; while (x) { c += x & 1; x >>= 1; } return c; }

long long tripletCount(int* a, int aSize, int* b, int bSize, int* c, int cSize) {
    int cnt1[2] = {0}, cnt2[2] = {0}, cnt3[2] = {0};
    for (int i = 0; i < aSize; i++) cnt1[pc3215((unsigned)a[i]) % 2]++;
    for (int i = 0; i < bSize; i++) cnt2[pc3215((unsigned)b[i]) % 2]++;
    for (int i = 0; i < cSize; i++) cnt3[pc3215((unsigned)c[i]) % 2]++;
    long long ans = 0;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            for (int k = 0; k < 2; k++)
                if ((i + j + k) % 2 == 0)
                    ans += (long long)cnt1[i] * cnt2[j] * cnt3[k];
    return ans;
}
