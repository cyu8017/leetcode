// LeetCode 2288 - Apply Discount to Prices
// https://leetcode.com/problems/apply-discount-to-prices/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>

char* discountPrices(char* sentence, int discount) {
    int n = (int)strlen(sentence);
    char* out = (char*)malloc((size_t)n * 4 + 64);
    out[0] = '\0';
    char* tmp = (char*)malloc((size_t)n + 1);
    strcpy(tmp, sentence);
    char* save = NULL;
    char* tok = strtok_r(tmp, " ", &save);
    int first = 1;
    while (tok) {
        bool ok = false;
        long long val = 0;
        if (tok[0] == '$' && tok[1] != '\0') {
            ok = true;
            for (int j = 1; tok[j]; j++) {
                if (tok[j] < '0' || tok[j] > '9') { ok = false; break; }
                val = val * 10 + (tok[j] - '0');
            }
        }
        if (!first) strcat(out, " ");
        first = 0;
        if (ok) {
            double price = (double)val * (100.0 - (double)discount) / 100.0;
            char buf[64];
            sprintf(buf, "$%.2f", price);
            strcat(out, buf);
        } else {
            strcat(out, tok);
        }
        tok = strtok_r(NULL, " ", &save);
    }
    free(tmp);
    return out;
}
