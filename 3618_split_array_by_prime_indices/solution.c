// LeetCode 3618 - Split Array by Prime Indices
// https://leetcode.com/problems/split-array-by-prime-indices/

#include <stdbool.h>
long long splitArray(int* nums, int numsSize) {
    static bool init=false; static bool primes[100010];
    if(!init){
        for(int i=0;i<100010;i++) primes[i]=true;
        primes[0]=primes[1]=false;
        for(int i=2;i<100010;i++) if(primes[i]) for(int j=i+i;j<100010;j+=i) primes[j]=false;
        init=true;
    }
    long long ans=0;
    for(int i=0;i<numsSize;i++) ans += primes[i]?nums[i]:-nums[i];
    return ans>=0?ans:-ans;
}
