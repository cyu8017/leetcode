// LeetCode 0168 - Excel Sheet Column Title
#include <algorithm>
#include <string>
using namespace std;
class Solution {
public:
    string convertToTitle(int columnNumber) {
        string result;
        while (columnNumber) {
            --columnNumber;
            result += char('A' + columnNumber % 26);
            columnNumber /= 26;
        }
        reverse(result.begin(), result.end());
        return result;
    }
};