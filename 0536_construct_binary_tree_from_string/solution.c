// LeetCode 0536 - Construct Binary Tree from String
// https://leetcode.com/problems/construct-binary-tree-from-string/

#include <ctype.h>
#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct {
    const char* text;
    int index;
} Parser;

static struct TreeNode* create_node(int value) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    if (!node) {
        return NULL;
    }
    node->val = value;
    node->left = NULL;
    node->right = NULL;
    return node;
}

static struct TreeNode* parse_node(Parser* parser) {
    if (parser->index >= (int)strlen(parser->text)) {
        return NULL;
    }

    int sign = 1;
    if (parser->text[parser->index] == '-') {
        sign = -1;
        parser->index++;
    }

    int value = 0;
    while (parser->text[parser->index] != '\0' &&
           isdigit((unsigned char)parser->text[parser->index])) {
        value = value * 10 + (parser->text[parser->index] - '0');
        parser->index++;
    }

    struct TreeNode* node = create_node(sign * value);
    if (!node) {
        return NULL;
    }

    if (parser->text[parser->index] == '(') {
        parser->index++;
        node->left = parse_node(parser);
        parser->index++;
    }

    if (parser->text[parser->index] == '(') {
        parser->index++;
        node->right = parse_node(parser);
        parser->index++;
    }

    return node;
}

struct TreeNode* str2tree(char* s) {
    if (!s || s[0] == '\0') {
        return NULL;
    }

    Parser parser = {s, 0};
    return parse_node(&parser);
}
