// LeetCode 2043 - Simple Bank System
// https://leetcode.com/problems/simple-bank-system/

#include <algorithm>
#include <array>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

class Bank {
    vector<long long> bal;
    bool valid(int account) { return account >= 1 && account <= (int)bal.size(); }
public:
    Bank(vector<long long>& balance) : bal(balance) {}
    bool transfer(int account1, int account2, long long money) {
        if (!valid(account1) || !valid(account2) || bal[account1 - 1] < money) return false;
        bal[account1 - 1] -= money;
        bal[account2 - 1] += money;
        return true;
    }
    bool deposit(int account, long long money) {
        if (!valid(account)) return false;
        bal[account - 1] += money;
        return true;
    }
    bool withdraw(int account, long long money) {
        if (!valid(account) || bal[account - 1] < money) return false;
        bal[account - 1] -= money;
        return true;
    }
};
