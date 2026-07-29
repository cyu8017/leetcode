// LeetCode 0786 - K-th Smallest Prime Fraction
#include <stdlib.h>

typedef struct { double val; int i, j; } Frac;

static void swapF(Frac* a, Frac* b) { Frac t=*a; *a=*b; *b=t; }
static void pushF(Frac* h, int* sz, Frac v) {
    int i=(*sz)++; h[i]=v;
    while (i>0){int p=(i-1)/2; if(h[p].val<=h[i].val)break; swapF(&h[p],&h[i]); i=p;}
}
static Frac popF(Frac* h, int* sz) {
    Frac top=h[0]; h[0]=h[--(*sz)]; int i=0;
    while(1){int l=i*2+1,r=l+1,s=i; if(l<*sz&&h[l].val<h[s].val)s=l; if(r<*sz&&h[r].val<h[s].val)s=r; if(s==i)break; swapF(&h[i],&h[s]); i=s;}
    return top;
}

int* kthSmallestPrimeFraction(int* arr, int arrSize, int k, int* returnSize) {
    Frac* heap = (Frac*)malloc((size_t)arrSize * arrSize * sizeof(Frac));
    int hsz = 0;
    for (int i = 0; i < arrSize - 1; i++) pushF(heap, &hsz, (Frac){(double)arr[i]/arr[arrSize-1], i, arrSize-1});
    for (int t = 0; t < k - 1; t++) {
        Frac cur = popF(heap, &hsz);
        if (cur.j - 1 > cur.i) pushF(heap, &hsz, (Frac){(double)arr[cur.i]/arr[cur.j-1], cur.i, cur.j-1});
    }
    Frac ans = popF(heap, &hsz);
    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = arr[ans.i]; result[1] = arr[ans.j];
    *returnSize = 2; free(heap); return result;
}
