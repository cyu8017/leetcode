// LeetCode 1597 - Build Binary Expression Tree From Infix Expression
// https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

#include <stdlib.h>

struct Node {
    char val;
    struct Node* left;
    struct Node* right;
};

static struct Node* newNode1597(char val) {
    struct Node* n = (struct Node*)malloc(sizeof(struct Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

static int pri1597(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

static void apply1597(struct Node** nodes, int* ns, char* ops, int* os) {
    char op = ops[--(*os)];
    struct Node* right = nodes[--(*ns)];
    struct Node* left = nodes[--(*ns)];
    struct Node* n = newNode1597(op);
    n->left = left;
    n->right = right;
    nodes[(*ns)++] = n;
}

struct Node* expTree(char* s) {
    struct Node* nodes[1005];
    char ops[1005];
    int ns = 0, os = 0;
    for (int i = 0; s[i]; i++) {
        char ch = s[i];
        if (ch >= '0' && ch <= '9') {
            nodes[ns++] = newNode1597(ch);
        } else if (ch == '(') {
            ops[os++] = ch;
        } else if (ch == ')') {
            while (ops[os - 1] != '(') apply1597(nodes, &ns, ops, &os);
            os--;
        } else {
            while (os > 0 && ops[os - 1] != '(' && pri1597(ops[os - 1]) >= pri1597(ch)) {
                apply1597(nodes, &ns, ops, &os);
            }
            ops[os++] = ch;
        }
    }
    while (os > 0) apply1597(nodes, &ns, ops, &os);
    return nodes[0];
}
