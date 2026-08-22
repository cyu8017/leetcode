// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
int minTime(char* s, int* order, int orderSize, int k) {
    (void)orderSize;
    int n=(int)strlen(s); long long total=(long long)n*(n+1)/2;
    if((long long)k>total) return -1;
    long long countValid(int t){
        bool* star=(bool*)calloc((size_t)n,sizeof(bool));
        for(int i=0;i<=t;i++) star[order[i]]=true;
        long long invalid=0; int i=0;
        while(i<n){ if(star[i]){i++;continue;} int j=i; while(j<n&&!star[j]) j++; long long L=j-i; invalid+=L*(L+1)/2; i=j; }
        free(star); return total-invalid;
    }
    int lo=0,hi=n-1,ans=-1;
    while(lo<=hi){ int mid=(lo+hi)/2; if(countValid(mid)>=k){ ans=mid; hi=mid-1; } else lo=mid+1; }
    return ans;
}
