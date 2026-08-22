// LeetCode 3606 - Coupon Code Validator
// https://leetcode.com/problems/coupon-code-validator/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
static bool check(char* s){ if(!s||!*s) return false; for(int i=0;s[i];i++) if(!isalnum((unsigned char)s[i])&&s[i]!='_') return false; return true; }
static int bl_rank(char* b){
    if(!strcmp(b,"electronics")) return 0;
    if(!strcmp(b,"grocery")) return 1;
    if(!strcmp(b,"pharmacy")) return 2;
    if(!strcmp(b,"restaurant")) return 3;
    return -1;
}
typedef struct { int i; char* code; char* bl; } Item;
static char** g_code; static char** g_bl;
static int cmp_item(const void* a, const void* b){
    const Item* pa=a; const Item* pb=b;
    int c=strcmp(pa->bl,pb->bl); if(c) return c; return strcmp(pa->code,pb->code);
}
char** validateCoupons(char** code, int codeSize, char** businessLine, int businessLineSize, bool* isActive, int isActiveSize, int* returnSize) {
    (void)businessLineSize;(void)isActiveSize;
    Item* idx=(Item*)malloc((size_t)codeSize*sizeof(Item)); int n=0;
    for(int i=0;i<codeSize;i++) if(isActive[i] && bl_rank(businessLine[i])>=0 && check(code[i])) idx[n++]=(Item){i,code[i],businessLine[i]};
    qsort(idx,(size_t)n,sizeof(Item),cmp_item);
    char** ans=(char**)malloc((size_t)n*sizeof(char*));
    for(int i=0;i<n;i++){ ans[i]=(char*)malloc(strlen(idx[i].code)+1); strcpy(ans[i],idx[i].code); }
    free(idx); *returnSize=n; return ans;
}
