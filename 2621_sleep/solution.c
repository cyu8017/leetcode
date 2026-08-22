// LeetCode 2621 - Sleep
// https://leetcode.com/problems/sleep/

#include <unistd.h>

// JavaScript problem; C stand-in sleeps millis via usleep.
void sleep_ms(int millis) {
    if (millis > 0) usleep((useconds_t)millis * 1000);
}
