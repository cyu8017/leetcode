// LeetCode 1845 - Seat Reservation Manager
// https://leetcode.com/problems/seat-reservation-manager/

#include <functional>
#include <queue>
#include <vector>

class SeatManager {
public:
    SeatManager(int n) {
        for (int i = 1; i <= n; ++i) {
            available.push(i);
        }
    }

    int reserve() {
        int seat = available.top();
        available.pop();
        return seat;
    }

    void unreserve(int seatNumber) {
        available.push(seatNumber);
    }

private:
    std::priority_queue<int, std::vector<int>, std::greater<>> available;
};
