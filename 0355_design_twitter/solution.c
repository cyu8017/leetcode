// LeetCode 0355 - Design Twitter
// https://leetcode.com/problems/design-twitter/

#include <stdlib.h>

typedef struct {
    int timestamp;
    int tweetId;
} Tweet;

typedef struct {
    int userId;
    int* followees;
    int count;
    int capacity;
} FollowList;

typedef struct {
    int time;
    int* timelineUserIds;
    Tweet** timelines;
    int* timelineCounts;
    int* timelineCapacities;
    int timelineUsers;
    int timelineCapacity;
    FollowList* following;
    int followingCount;
    int followingCapacity;
} Twitter;

static int timelineIndexOf(Twitter* obj, int userId) {
    for (int index = 0; index < obj->timelineUsers; index++) {
        if (obj->timelineUserIds[index] == userId) {
            return index;
        }
    }
    return -1;
}

static int getUserTimelineIndex(Twitter* obj, int userId) {
    int index = timelineIndexOf(obj, userId);
    if (index >= 0) {
        return index;
    }

    if (obj->timelineUsers >= obj->timelineCapacity) {
        int newCapacity = obj->timelineCapacity == 0 ? 4 : obj->timelineCapacity * 2;
        obj->timelineUserIds = (int*)realloc(obj->timelineUserIds, (size_t)newCapacity * sizeof(int));
        obj->timelines = (Tweet**)realloc(obj->timelines, (size_t)newCapacity * sizeof(Tweet*));
        obj->timelineCounts = (int*)realloc(obj->timelineCounts, (size_t)newCapacity * sizeof(int));
        obj->timelineCapacities = (int*)realloc(obj->timelineCapacities, (size_t)newCapacity * sizeof(int));
        obj->timelineCapacity = newCapacity;
    }

    index = obj->timelineUsers++;
    obj->timelineUserIds[index] = userId;
    obj->timelines[index] = NULL;
    obj->timelineCounts[index] = 0;
    obj->timelineCapacities[index] = 0;
    return index;
}

static int getFollowListIndex(Twitter* obj, int followerId) {
    for (int index = 0; index < obj->followingCount; index++) {
        if (obj->following[index].userId == followerId) {
            return index;
        }
    }

    if (obj->followingCount >= obj->followingCapacity) {
        int newCapacity = obj->followingCapacity == 0 ? 4 : obj->followingCapacity * 2;
        obj->following = (FollowList*)realloc(obj->following, (size_t)newCapacity * sizeof(FollowList));
        obj->followingCapacity = newCapacity;
    }

    int index = obj->followingCount++;
    obj->following[index].userId = followerId;
    obj->following[index].followees = NULL;
    obj->following[index].count = 0;
    obj->following[index].capacity = 0;
    return index;
}

static int followListContains(FollowList* list, int followeeId) {
    for (int index = 0; index < list->count; index++) {
        if (list->followees[index] == followeeId) {
            return 1;
        }
    }
    return 0;
}

Twitter* twitterCreate() {
    return (Twitter*)calloc(1, sizeof(Twitter));
}

void twitterPostTweet(Twitter* obj, int userId, int tweetId) {
    int index = getUserTimelineIndex(obj, userId);
    if (obj->timelineCounts[index] >= obj->timelineCapacities[index]) {
        int newCapacity = obj->timelineCapacities[index] == 0 ? 4 : obj->timelineCapacities[index] * 2;
        obj->timelines[index] = (Tweet*)realloc(obj->timelines[index], (size_t)newCapacity * sizeof(Tweet));
        obj->timelineCapacities[index] = newCapacity;
    }

    obj->time += 1;
    obj->timelines[index][obj->timelineCounts[index]].timestamp = obj->time;
    obj->timelines[index][obj->timelineCounts[index]].tweetId = tweetId;
    obj->timelineCounts[index] += 1;
}

typedef struct {
    int timestamp;
    int tweetId;
} FeedItem;

static int compareFeedItems(const void* leftPtr, const void* rightPtr) {
    const FeedItem* left = (const FeedItem*)leftPtr;
    const FeedItem* right = (const FeedItem*)rightPtr;
    if (left->timestamp != right->timestamp) {
        return right->timestamp - left->timestamp;
    }
    return left->tweetId - right->tweetId;
}

static void appendTimeline(Twitter* obj, int userId, FeedItem* items, int* itemCount, int capacity) {
    int timelineIndex = timelineIndexOf(obj, userId);
    if (timelineIndex < 0) {
        return;
    }

    int start = obj->timelineCounts[timelineIndex] - 10;
    if (start < 0) {
        start = 0;
    }

    for (int index = start; index < obj->timelineCounts[timelineIndex] && *itemCount < capacity; index++) {
        items[*itemCount].timestamp = obj->timelines[timelineIndex][index].timestamp;
        items[*itemCount].tweetId = obj->timelines[timelineIndex][index].tweetId;
        *itemCount += 1;
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twitterGetNewsFeed(Twitter* obj, int userId, int* returnSize) {
    FeedItem items[256];
    int itemCount = 0;

    appendTimeline(obj, userId, items, &itemCount, 256);

    int followIndex = -1;
    for (int index = 0; index < obj->followingCount; index++) {
        if (obj->following[index].userId == userId) {
            followIndex = index;
            break;
        }
    }

    if (followIndex >= 0) {
        FollowList* list = &obj->following[followIndex];
        for (int followeeIndex = 0; followeeIndex < list->count; followeeIndex++) {
            appendTimeline(obj, list->followees[followeeIndex], items, &itemCount, 256);
        }
    }

    qsort(items, (size_t)itemCount, sizeof(FeedItem), compareFeedItems);

    int count = itemCount < 10 ? itemCount : 10;
    int* result = (int*)malloc((size_t)count * sizeof(int));
    for (int index = 0; index < count; index++) {
        result[index] = items[index].tweetId;
    }

    *returnSize = count;
    return result;
}

void twitterFollow(Twitter* obj, int followerId, int followeeId) {
    int index = getFollowListIndex(obj, followerId);
    FollowList* list = &obj->following[index];
    if (followListContains(list, followeeId)) {
        return;
    }

    if (list->count >= list->capacity) {
        int newCapacity = list->capacity == 0 ? 4 : list->capacity * 2;
        list->followees = (int*)realloc(list->followees, (size_t)newCapacity * sizeof(int));
        list->capacity = newCapacity;
    }

    list->followees[list->count++] = followeeId;
}

void twitterUnfollow(Twitter* obj, int followerId, int followeeId) {
    for (int index = 0; index < obj->followingCount; index++) {
        FollowList* list = &obj->following[index];
        if (list->userId != followerId) {
            continue;
        }
        for (int followeeIndex = 0; followeeIndex < list->count; followeeIndex++) {
            if (list->followees[followeeIndex] == followeeId) {
                list->followees[followeeIndex] = list->followees[list->count - 1];
                list->count -= 1;
                return;
            }
        }
    }
}

void twitterFree(Twitter* obj) {
    for (int index = 0; index < obj->timelineUsers; index++) {
        free(obj->timelines[index]);
    }
    free(obj->timelineUserIds);
    free(obj->timelines);
    free(obj->timelineCounts);
    free(obj->timelineCapacities);

    for (int index = 0; index < obj->followingCount; index++) {
        free(obj->following[index].followees);
    }
    free(obj->following);
    free(obj);
}
