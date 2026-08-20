// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/


import "time"

type TimeLimitedCache struct {
	data map[int]struct {
		value  int
		expire int64
	}
}

func Constructor() TimeLimitedCache {
	return TimeLimitedCache{data: map[int]struct {
		value  int
		expire int64
	}{}}
}

func (c *TimeLimitedCache) Set(key, value, duration int) bool {
	now := time.Now().UnixMilli()
	_, ok := c.data[key]
	alive := ok && c.data[key].expire > now
	c.data[key] = struct {
		value  int
		expire int64
	}{value, now + int64(duration)}
	return alive
}

func (c *TimeLimitedCache) Get(key int) int {
	now := time.Now().UnixMilli()
	e, ok := c.data[key]
	if !ok || e.expire <= now {
		return -1
	}
	return e.value
}

func (c *TimeLimitedCache) Count() int {
	now := time.Now().UnixMilli()
	cnt := 0
	for k, e := range c.data {
		if e.expire > now {
			cnt++
		} else {
			delete(c.data, k)
		}
	}
	return cnt
}
