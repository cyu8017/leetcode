// LeetCode 3605 - Minimum Stability Factor of Array
// https://leetcode.com/problems/minimum-stability-factor-of-array/

static int gcd(int a,int b){while(b){int t=a%b;a=b;b=t;}return a;}
int minStable(int* nums, int numsSize, int maxC) {
    int n=numsSize;
    int ok(int x){
        if(x>=n) return 1;
        int changes=0,i=0;
        while(i+x<n){
            int g=nums[i];
            for(int j=i+1;j<=i+x;j++) g=gcd(g,nums[j]);
            if(g>1){ changes++; i+=x+1; } else i++;
        }
        return changes<=maxC;
    }
    int lo=0,hi=n;
    while(lo<hi){ int mid=(lo+hi)/2; if(ok(mid)) hi=mid; else lo=mid+1; }
    return lo;
}
