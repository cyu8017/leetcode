// LeetCode 3595 - Once Twice
// https://leetcode.com/problems/once-twice/

#include <stdlib.h>
int* onceTwice(int* nums, int numsSize, int* returnSize) {
    /* frequency via sort */
    int* a=(int*)malloc((size_t)numsSize*sizeof(int));
    for(int i=0;i<numsSize;i++) a[i]=nums[i];
    for(int i=0;i<numsSize;i++) for(int j=i+1;j<numsSize;j++) if(a[j]<a[i]){int t=a[i];a[i]=a[j];a[j]=t;}
    int once=0,twice=0;
    for(int i=0;i<numsSize;){
        int j=i; while(j<numsSize && a[j]==a[i]) j++;
        if(j-i==1) once=a[i]; else if(j-i==2) twice=a[i];
        i=j;
    }
    free(a);
    int* ans=(int*)malloc(2*sizeof(int)); ans[0]=once; ans[1]=twice;
    *returnSize=2; return ans;
}
