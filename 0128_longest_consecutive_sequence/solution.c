// LeetCode 0128 - Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

#include <stdlib.h>
static int compareInt(const void* a,const void* b){int x=*(const int*)a,y=*(const int*)b;return (x>y)-(x<y);}
int longestConsecutive(int* nums, int numsSize) { if(!numsSize)return 0;qsort(nums,numsSize,sizeof(int),compareInt);int best=1,length=1;for(int i=1;i<numsSize;i++){if(nums[i]==nums[i-1])continue;if(nums[i]==nums[i-1]+1)length++;else length=1;if(length>best)best=length;}return best; }