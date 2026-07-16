// LeetCode 0460 - LFU Cache
// https://leetcode.com/problems/lfu-cache/

type LFUCache struct {
	capacity  int
	minFreq   int
	keyValues map[int]int
	keyFreqs  map[int]int
	freqKeys  map[int][]int
}

func Constructor(capacity int) LFUCache {
	return LFUCache{
		capacity:  capacity,
		minFreq:   0,
		keyValues: make(map[int]int),
		keyFreqs:  make(map[int]int),
		freqKeys:  make(map[int][]int),
	}
}

func (c *LFUCache) touch(key int) {
	freq := c.keyFreqs[key]
	bucket := c.freqKeys[freq]
	for index, value := range bucket {
		if value == key {
			c.freqKeys[freq] = append(bucket[:index], bucket[index+1:]...)
			break
		}
	}
	if len(c.freqKeys[freq]) == 0 && freq == c.minFreq {
		c.minFreq++
	}
	c.keyFreqs[key] = freq + 1
	c.freqKeys[freq+1] = append(c.freqKeys[freq+1], key)
}

func (c *LFUCache) get(key int) int {
	if _, ok := c.keyValues[key]; !ok {
		return -1
	}
	c.touch(key)
	return c.keyValues[key]
}

func (c *LFUCache) put(key, value int) {
	if c.capacity == 0 {
		return
	}
	if _, ok := c.keyValues[key]; ok {
		c.keyValues[key] = value
		c.touch(key)
		return
	}
	if len(c.keyValues) >= c.capacity {
		evict := c.freqKeys[c.minFreq][0]
		c.freqKeys[c.minFreq] = c.freqKeys[c.minFreq][1:]
		delete(c.keyValues, evict)
		delete(c.keyFreqs, evict)
	}
	c.keyValues[key] = value
	c.keyFreqs[key] = 1
	c.freqKeys[1] = append(c.freqKeys[1], key)
	c.minFreq = 1
}
