// LeetCode 1108 - Defanging an IP Address
// https://leetcode.com/problems/defanging-an-ip-address/

#include <stdlib.h>
#include <string.h>

char* defangIPaddr(char* address) {
    int n = (int)strlen(address);
    char* ans = (char*)malloc((size_t)(n * 3 + 1));
    int j = 0;
    for (int i = 0; i < n; i++) {
        if (address[i] == '.') {
            ans[j++] = '['; ans[j++] = '.'; ans[j++] = ']';
        } else {
            ans[j++] = address[i];
        }
    }
    ans[j] = '\0';
    return ans;
}
