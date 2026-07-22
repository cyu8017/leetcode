// LeetCode 1628 - Design an Expression Tree With Evaluate Function
// https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

struct Node {
    char* val;
    struct Node* left;
    struct Node* right;
};

static int evaluateNode(struct Node* node) {
    if (!strchr("+-*/", node->val[0]) || node->val[1] != '\0') {
        return atoi(node->val);
    }
    int a = evaluateNode(node->left);
    int b = evaluateNode(node->right);
    switch (node->val[0]) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return a / b;
    }
    return 0;
}

typedef struct {
    int unused;
} TreeBuilder;

TreeBuilder* treeBuilderCreate(void) {
    return (TreeBuilder*)calloc(1, sizeof(TreeBuilder));
}

struct Node* treeBuilderExpTree(TreeBuilder* obj, char** postfix, int postfixSize) {
    (void)obj;
    struct Node** stack = (struct Node**)malloc((size_t)postfixSize * sizeof(struct Node*));
    int top = 0;
    for (int i = 0; i < postfixSize; i++) {
        struct Node* node = (struct Node*)calloc(1, sizeof(struct Node));
        node->val = postfix[i];
        if (strchr("+-*/", postfix[i][0]) && postfix[i][1] == '\0') {
            node->right = stack[--top];
            node->left = stack[--top];
        }
        stack[top++] = node;
    }
    struct Node* root = stack[0];
    free(stack);
    return root;
}

/* Convenience free-function alias matching LeetCode style. */
struct Node* expTree(char** postfix, int postfixSize) {
    TreeBuilder* b = treeBuilderCreate();
    struct Node* root = treeBuilderExpTree(b, postfix, postfixSize);
    free(b);
    return root;
}

int NodeEvaluate(struct Node* node) {
    return evaluateNode(node);
}

void treeBuilderFree(TreeBuilder* obj) {
    free(obj);
}
