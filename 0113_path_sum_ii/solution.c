// LeetCode 0113 - Path Sum II
#include <stdlib.h>
struct TreeNode { int val; struct TreeNode *left, *right; };
static void dfs(struct TreeNode* n,int sum,int* path,int len,int*** out,int** cols,int* size) {
    if (!n) return; path[len++]=n->val; sum-=n->val;
    if (!n->left&&!n->right&&sum==0) { (*out)[*size]=malloc(len*sizeof(int)); for(int i=0;i<len;i++)(*out)[*size][i]=path[i]; (*cols)[(*size)++]=len; return; }
    dfs(n->left,sum,path,len,out,cols,size); dfs(n->right,sum,path,len,out,cols,size);
}
int** pathSum(struct TreeNode* root,int targetSum,int* returnSize,int** returnColumnSizes) {
    int **out=malloc(5000*sizeof(int*)); *returnColumnSizes=malloc(5000*sizeof(int)); *returnSize=0; int path[5000];
    dfs(root,targetSum,path,0,&out,*returnColumnSizes,returnSize); return out;
}