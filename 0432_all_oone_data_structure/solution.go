// LeetCode 0432 - All O`one` Data Structure
// https://leetcode.com/problems/all-oone-data-structure/

type bucketNode struct {
	count int
	keys  map[string]struct{}
	prev  *bucketNode
	next  *bucketNode
}

type AllOne struct {
	head     bucketNode
	tail     bucketNode
	keyNodes map[string]*bucketNode
}

func AllOne() *AllOne {
	allOne := &AllOne{keyNodes: make(map[string]*bucketNode)}
	allOne.head.next = &allOne.tail
	allOne.tail.prev = &allOne.head
	return allOne
}

func (this *AllOne) insertAfter(anchor, node *bucketNode) {
	node.prev = anchor
	node.next = anchor.next
	anchor.next.prev = node
	anchor.next = node
}

func (this *AllOne) removeBucket(node *bucketNode) {
	node.prev.next = node.next
	node.next.prev = node.prev
}

func (this *AllOne) ensureCountNode(count int, after *bucketNode) *bucketNode {
	current := after.next
	for current != &this.tail && current.count < count {
		current = current.next
	}
	if current != &this.tail && current.count == count {
		return current
	}
	bucket := &bucketNode{count: count, keys: make(map[string]struct{})}
	this.insertAfter(current.prev, bucket)
	return bucket
}

func (this *AllOne) Inc(key string) {
	if bucket, ok := this.keyNodes[key]; ok {
		delete(bucket.keys, key)
		nextBucket := this.ensureCountNode(bucket.count+1, bucket)
		nextBucket.keys[key] = struct{}{}
		this.keyNodes[key] = nextBucket
		if len(bucket.keys) == 0 {
			this.removeBucket(bucket)
		}
		return
	}

	bucket := this.ensureCountNode(1, &this.head)
	bucket.keys[key] = struct{}{}
	this.keyNodes[key] = bucket
}

func (this *AllOne) Dec(key string) {
	bucket := this.keyNodes[key]
	delete(bucket.keys, key)
	if bucket.count == 1 {
		delete(this.keyNodes, key)
	} else {
		prevBucket := this.ensureCountNode(bucket.count-1, &this.head)
		prevBucket.keys[key] = struct{}{}
		this.keyNodes[key] = prevBucket
	}
	if len(bucket.keys) == 0 {
		this.removeBucket(bucket)
	}
}

func (this *AllOne) GetMaxKey() string {
	bucket := this.tail.prev
	if bucket == &this.head {
		return ""
	}
	for key := range bucket.keys {
		return key
	}
	return ""
}

func (this *AllOne) GetMinKey() string {
	bucket := this.head.next
	if bucket == &this.tail {
		return ""
	}
	for key := range bucket.keys {
		return key
	}
	return ""
}
