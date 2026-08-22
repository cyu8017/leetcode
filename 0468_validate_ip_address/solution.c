// LeetCode 0468 - Validate IP Address
// https://leetcode.com/problems/validate-ip-address/

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static bool isIPv4(const char* address) {
    int parts = 0;
    int i = 0;
    while (address[i] || parts > 0) {
        if (parts >= 4) {
            return false;
        }
        int len = 0;
        int value = 0;
        int start = i;
        while (address[i] && address[i] != '.') {
            if (!isdigit((unsigned char)address[i])) {
                return false;
            }
            value = value * 10 + (address[i] - '0');
            len++;
            i++;
            if (len > 3 || value > 255) {
                return false;
            }
        }
        if (len == 0 || (len > 1 && address[start] == '0')) {
            return false;
        }
        parts++;
        if (address[i] == '.') {
            i++;
            if (!address[i]) {
                return false;
            }
        } else {
            break;
        }
    }
    return parts == 4;
}

static bool isIPv6(const char* address) {
    int parts = 0;
    int i = 0;
    while (address[i] || parts > 0) {
        if (parts >= 8) {
            return false;
        }
        int len = 0;
        while (address[i] && address[i] != ':') {
            if (!isxdigit((unsigned char)address[i])) {
                return false;
            }
            len++;
            i++;
            if (len > 4) {
                return false;
            }
        }
        if (len == 0) {
            return false;
        }
        parts++;
        if (address[i] == ':') {
            i++;
            if (!address[i]) {
                return false;
            }
        } else {
            break;
        }
    }
    return parts == 8;
}

char* validIPAddress(char* queryIP) {
    if (isIPv4(queryIP)) {
        return "IPv4";
    }
    if (isIPv6(queryIP)) {
        return "IPv6";
    }
    return "Neither";
}
