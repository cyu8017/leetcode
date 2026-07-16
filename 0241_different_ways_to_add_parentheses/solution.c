// LeetCode 0241 - Different Ways to Add Parentheses
// https://leetcode.com/problems/different-ways-to-add-parentheses/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

static int is_digits_only(const char* expression) {
    for (int index = 0; expression[index] != '\0'; ++index) {
        if (!isdigit((unsigned char)expression[index])) {
            return 0;
        }
    }
    return 1;
}

static int* merge_results(int* left, int left_size, int* right, int right_size, char operator, int* return_size) {
    int capacity = left_size * right_size;
    int* result = (int*)malloc(capacity * sizeof(int));
    *return_size = 0;
    for (int left_index = 0; left_index < left_size; ++left_index) {
        for (int right_index = 0; right_index < right_size; ++right_index) {
            int left_value = left[left_index];
            int right_value = right[right_index];
            if (operator == '+') {
                result[*return_size] = left_value + right_value;
            } else if (operator == '-') {
                result[*return_size] = left_value - right_value;
            } else {
                result[*return_size] = left_value * right_value;
            }
            (*return_size)++;
        }
    }
    return result;
}

static int* append_results(int* current, int current_size, int* addition, int addition_size, int* return_size) {
    int* merged = (int*)realloc(current, (current_size + addition_size) * sizeof(int));
    for (int index = 0; index < addition_size; ++index) {
        merged[current_size + index] = addition[index];
    }
    *return_size = current_size + addition_size;
    free(addition);
    return merged;
}

int* diffWaysToCompute(char* expression, int* returnSize) {
    if (is_digits_only(expression)) {
        int* result = (int*)malloc(sizeof(int));
        result[0] = atoi(expression);
        *returnSize = 1;
        return result;
    }

    int* result = NULL;
    *returnSize = 0;
    int length = (int)strlen(expression);
    for (int index = 0; index < length; ++index) {
        char operator = expression[index];
        if (operator != '+' && operator != '-' && operator != '*') {
            continue;
        }
        char saved = expression[index];
        expression[index] = '\0';
        int left_size = 0;
        int right_size = 0;
        int* left = diffWaysToCompute(expression, &left_size);
        expression[index] = saved;
        int* right = diffWaysToCompute(expression + index + 1, &right_size);
        int partial_size = 0;
        int* partial = merge_results(left, left_size, right, right_size, operator, &partial_size);
        free(left);
        free(right);
        result = append_results(result, *returnSize, partial, partial_size, returnSize);
    }
    return result;
}
