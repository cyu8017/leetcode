// LeetCode 3640 - Trionic Array II
// https://leetcode.com/problems/trionic-array-ii/

#include <limits.h>
static long long llmax(long long a,long long b){return a>b?a:b;}
long long maxSumTrionic(int* nums, int numsSize) {
    int n=numsSize, i=0; long long ans=LLONG_MIN;
    while(i<n){
        int l=i;
        for(i++; i<n && nums[i-1]<nums[i]; ) i++;
        if(i==l+1) continue;
        int p=i-1; long long s=(long long)nums[p-1]+nums[p];
        while(i<n && nums[i-1]>nums[i]){ s+=nums[i]; i++; }
        if(i==p+1 || i==n || nums[i-1]==nums[i]) continue;
        int q=i-1; s+=nums[i]; i++;
        long long mx=0,t=0;
        while(i<n && nums[i-1]<nums[i]){ t+=nums[i]; i++; mx=llmax(mx,t); }
        s+=mx; mx=0; t=0;
        for(int j=p-2;j>=l;j--){ t+=nums[j]; mx=llmax(mx,t); }
        s+=mx; ans=llmax(ans,s); i=q;
    }
    return ans;
}
