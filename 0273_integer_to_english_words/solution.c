// LeetCode 0273 - Integer to English Words
// https://leetcode.com/problems/integer-to-english-words/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const char* ONES[] = {
    "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
    "Seventeen", "Eighteen", "Nineteen"
};
static const char* TENS[] = {
    "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
};
static const char* THOUSANDS[] = {"", "Thousand", "Million", "Billion"};

static void append_string(char* buffer, const char* text) {
    if (!text || text[0] == '\0') {
        return;
    }
    if (buffer[0] != '\0') {
        strcat(buffer, " ");
    }
    strcat(buffer, text);
}

static void convert_chunk(int value, char* buffer) {
    if (value == 0) {
        return;
    }
    if (value < 20) {
        append_string(buffer, ONES[value]);
        return;
    }
    if (value < 100) {
        append_string(buffer, TENS[value / 10]);
        append_string(buffer, ONES[value % 10]);
        return;
    }
    char hundreds[64];
    snprintf(hundreds, sizeof(hundreds), "%s Hundred", ONES[value / 100]);
    append_string(buffer, hundreds);
    convert_chunk(value % 100, buffer);
}

char* numberToWords(int num) {
    if (num == 0) {
        char* zero = (char*)malloc(5);
        strcpy(zero, "Zero");
        return zero;
    }

    char* result = (char*)calloc(256, 1);
    char parts[4][128];
    int part_count = 0;
    int chunk_index = 0;

    while (num > 0) {
        int chunk = num % 1000;
        if (chunk != 0) {
            parts[part_count][0] = '\0';
            convert_chunk(chunk, parts[part_count]);
            if (THOUSANDS[chunk_index][0] != '\0') {
                strcat(parts[part_count], " ");
                strcat(parts[part_count], THOUSANDS[chunk_index]);
            }
            part_count++;
        }
        num /= 1000;
        chunk_index++;
    }

    for (int i = part_count - 1; i >= 0; i--) {
        append_string(result, parts[i]);
    }
    return result;
}
